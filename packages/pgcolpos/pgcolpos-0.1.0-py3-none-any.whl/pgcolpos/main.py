#!/usr/bin/env python3
"""
pgcolpos - PostgreSQL Column Position Tool

A command-line utility to add or move columns to specific positions in PostgreSQL tables
while preserving all constraints, indexes, permissions, and references.

Usage:
  pgcolpos add <table> <column_name> <data_type> after <reference_column> [--db=<connection_string>]
  pgcolpos move <table> <column_name> after <reference_column> [--db=<connection_string>]
  pgcolpos --help

Examples:
  pgcolpos add users email varchar(255) after username --db="postgresql://user:pass@localhost/mydb"
  pgcolpos move products description after name --db="postgresql://user:pass@localhost/mydb"
"""

import sys
import getopt
import psycopg2
from psycopg2 import sql
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('pgcolpos')

def get_connection(connection_string):
    """Establish a database connection"""
    try:
        conn = psycopg2.connect(connection_string)
        return conn
    except Exception as e:
        logger.error(f"Connection error: {e}")
        sys.exit(1)

def get_table_info(conn, table_name):
    """Get all column information for a table"""
    cursor = conn.cursor()
    
    # Get columns and their types
    cursor.execute("""
        SELECT column_name, data_type, character_maximum_length, 
               column_default, is_nullable
        FROM information_schema.columns
        WHERE table_name = %s
        ORDER BY ordinal_position
    """, (table_name,))
    
    columns = cursor.fetchall()
    
    if not columns:
        logger.error(f"Table '{table_name}' does not exist or has no columns")
        sys.exit(1)
        
    cursor.close()
    return columns

def get_constraints(conn, table_name):
    """Get all constraints for a table"""
    cursor = conn.cursor()
    
    # Get primary key constraints
    cursor.execute("""
        SELECT con.conname, con.contype, att.attname
        FROM pg_constraint con
        JOIN pg_attribute att ON att.attrelid = con.conrelid AND att.attnum = ANY(con.conkey)
        JOIN pg_class rel ON rel.oid = con.conrelid
        JOIN pg_namespace nsp ON nsp.oid = rel.relnamespace
        WHERE rel.relname = %s
    """, (table_name,))
    
    constraints = cursor.fetchall()
    
    # Get foreign key constraints
    cursor.execute("""
        SELECT
            tc.constraint_name,
            tc.table_name,
            kcu.column_name,
            ccu.table_name AS foreign_table_name,
            ccu.column_name AS foreign_column_name
        FROM
            information_schema.table_constraints AS tc
        JOIN
            information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name
        JOIN
            information_schema.constraint_column_usage AS ccu ON ccu.constraint_name = tc.constraint_name
        WHERE
            tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s
    """, (table_name,))
    
    foreign_keys = cursor.fetchall()
    
    cursor.close()
    return constraints, foreign_keys

def get_indexes(conn, table_name):
    """Get all indexes for a table"""
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT
            i.relname AS index_name,
            a.attname AS column_name,
            ix.indisunique AS is_unique,
            pg_get_indexdef(ix.indexrelid) AS index_definition
        FROM
            pg_class t,
            pg_class i,
            pg_index ix,
            pg_attribute a
        WHERE
            t.oid = ix.indrelid
            AND i.oid = ix.indexrelid
            AND a.attrelid = t.oid
            AND a.attnum = ANY(ix.indkey)
            AND t.relkind = 'r'
            AND t.relname = %s
        ORDER BY
            i.relname, a.attnum
    """, (table_name,))
    
    indexes = cursor.fetchall()
    cursor.close()
    return indexes

def get_permissions(conn, table_name):
    """Get all permissions for a table"""
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT grantee, privilege_type
        FROM information_schema.role_table_grants
        WHERE table_name = %s
    """, (table_name,))
    
    permissions = cursor.fetchall()
    cursor.close()
    return permissions

def generate_new_column_definition(conn, table_name, columns, new_column_name, data_type, after_column):
    """Generate the column definition for the new table in the desired order"""
    new_columns = []
    new_column_added = False
    after_column_found = False
    
    for col in columns:
        column_name = col[0]
        
        if column_name == after_column:
            after_column_found = True
            new_columns.append(col)
            
            # Add the new column after the reference column
            if data_type:  # This is for 'add' command
                new_columns.append((new_column_name, data_type, None, None, 'YES'))
                new_column_added = True
        elif column_name == new_column_name and not data_type:  # This is for 'move' command
            # Skip it here, we'll add it after the reference column
            continue
        else:
            new_columns.append(col)
    
    # If we're moving a column and found the after_column
    if not data_type and after_column_found and not new_column_added:
        # Find the column we're moving
        for col in columns:
            if col[0] == new_column_name:
                # Insert it after the 'after_column' entry in new_columns
                for i, entry in enumerate(new_columns):
                    if entry[0] == after_column:
                        new_columns.insert(i + 1, col)
                        new_column_added = True
                        break
                break
    
    if not after_column_found:
        logger.error(f"Reference column '{after_column}' not found in table '{table_name}'")
        sys.exit(1)
        
    if not new_column_added and not data_type:
        logger.error(f"Column '{new_column_name}' not found in table '{table_name}'")
        sys.exit(1)
    
    return new_columns

def create_new_table(conn, table_name, columns, new_columns, constraints, foreign_keys, indexes, permissions):
    """Create a new table with the desired column order and migrate data"""
    cursor = conn.cursor()
    temp_table_name = f"{table_name}_new"
    
    try:
        # Begin transaction
        conn.autocommit = False
        
        # Step 1: Create a new table with the desired column order
        create_stmt = "CREATE TABLE {} (\n".format(temp_table_name)
        
        column_definitions = []
        for col in new_columns:
            col_name, data_type, max_length, default, nullable = col
            
            # Build the column definition
            col_def = f"{col_name} {data_type}"
            if max_length:
                col_def += f"({max_length})"
            
            if default:
                col_def += f" DEFAULT {default}"
                
            if nullable == 'NO':
                col_def += " NOT NULL"
                
            column_definitions.append(col_def)
        
        create_stmt += ",\n".join(column_definitions)
        create_stmt += "\n)"
        
        logger.info(f"Creating new table: {temp_table_name}")
        cursor.execute(create_stmt)
        
        # Step 2: Copy data from the original table to the new table
        old_column_names = [col[0] for col in columns]
        new_column_names = [col[0] for col in new_columns if col[0] in old_column_names]
        
        insert_stmt = sql.SQL("INSERT INTO {} ({}) SELECT {} FROM {}").format(
            sql.Identifier(temp_table_name),
            sql.SQL(', ').join(map(sql.Identifier, new_column_names)),
            sql.SQL(', ').join(map(sql.Identifier, new_column_names)),
            sql.Identifier(table_name)
        )
        
        logger.info(f"Copying data from {table_name} to {temp_table_name}")
        cursor.execute(insert_stmt)
        
        # Step 3: Drop the original table
        logger.info(f"Dropping original table: {table_name}")
        cursor.execute(f"DROP TABLE {table_name} CASCADE")
        
        # Step 4: Rename the new table to the original name
        logger.info(f"Renaming {temp_table_name} to {table_name}")
        cursor.execute(f"ALTER TABLE {temp_table_name} RENAME TO {table_name}")
        
        # Step 5: Recreate primary key and unique constraints
        for constraint in constraints:
            constraint_name, constraint_type, column_name = constraint
            
            if constraint_type == 'p':  # Primary key
                logger.info(f"Recreating primary key constraint on {column_name}")
                cursor.execute(f"ALTER TABLE {table_name} ADD PRIMARY KEY ({column_name})")
            elif constraint_type == 'u':  # Unique constraint
                logger.info(f"Recreating unique constraint on {column_name}")
                cursor.execute(f"ALTER TABLE {table_name} ADD CONSTRAINT {constraint_name} UNIQUE ({column_name})")
        
        # Step 6: Recreate foreign key constraints
        for fk in foreign_keys:
            constraint_name, table_name, column_name, referenced_table, referenced_column = fk
            logger.info(f"Recreating foreign key constraint: {constraint_name}")
            cursor.execute(f"""
                ALTER TABLE {table_name}
                ADD CONSTRAINT {constraint_name}
                FOREIGN KEY ({column_name})
                REFERENCES {referenced_table} ({referenced_column})
            """)
        
        # Step 7: Recreate indexes
        # Note: Primary key and unique constraints already create indexes,
        # so we only need to recreate non-constraint indexes
        recreated_indexes = set()
        for index in indexes:
            index_name, column_name, is_unique, index_def = index
            
            # Skip indexes that are part of constraints (they're recreated with the constraints)
            if is_unique or index_name in recreated_indexes:
                continue
                
            logger.info(f"Recreating index: {index_name}")
            # We use the full definition because it includes things like partial indexes, etc.
            cursor.execute(index_def)
            recreated_indexes.add(index_name)
        
        # Step 8: Restore permissions
        for permission in permissions:
            grantee, privilege_type = permission
            logger.info(f"Restoring {privilege_type} permission for {grantee}")
            cursor.execute(f"GRANT {privilege_type} ON {table_name} TO {grantee}")
        
        # Commit the transaction
        conn.commit()
        logger.info(f"Successfully completed operation on table {table_name}")
        
    except Exception as e:
        conn.rollback()
        logger.error(f"Error: {e}")
        sys.exit(1)
    finally:
        cursor.close()
        conn.autocommit = True

def add_column(conn, table_name, column_name, data_type, after_column):
    """Add a new column after a specific column"""
    # Get table structure
    columns = get_table_info(conn, table_name)
    constraints, foreign_keys = get_constraints(conn, table_name)
    indexes = get_indexes(conn, table_name)
    permissions = get_permissions(conn, table_name)
    
    # Check if column already exists
    column_names = [col[0] for col in columns]
    if column_name in column_names:
        logger.error(f"Column '{column_name}' already exists in table '{table_name}'")
        sys.exit(1)
    
    # Generate new column order
    new_columns = generate_new_column_definition(
        conn, table_name, columns, column_name, data_type, after_column
    )
    
    # Create the new table with the desired column order
    create_new_table(conn, table_name, columns, new_columns, constraints, foreign_keys, indexes, permissions)

def move_column(conn, table_name, column_name, after_column):
    """Move an existing column after a specific column"""
    # Get table structure
    columns = get_table_info(conn, table_name)
    constraints, foreign_keys = get_constraints(conn, table_name)
    indexes = get_indexes(conn, table_name)
    permissions = get_permissions(conn, table_name)
    
    # Check if column exists
    column_names = [col[0] for col in columns]
    if column_name not in column_names:
        logger.error(f"Column '{column_name}' does not exist in table '{table_name}'")
        sys.exit(1)
    
    # Generate new column order
    new_columns = generate_new_column_definition(
        conn, table_name, columns, column_name, None, after_column
    )
    
    # Create the new table with the desired column order
    create_new_table(conn, table_name, columns, new_columns, constraints, foreign_keys, indexes, permissions)

def print_help():
    """Print help information"""
    print(__doc__)

def main():
    # Default connection string
    connection_string = "postgresql://postgres:postgres@localhost/postgres"
    
    try:
        # Parse command-line arguments
        if len(sys.argv) < 2:
            print_help()
            sys.exit(1)
            
        if sys.argv[1] == "--help":
            print_help()
            sys.exit(0)
            
        command = sys.argv[1]
        
        if command not in ["add", "move"]:
            logger.error("Invalid command. Use 'add', 'move', or '--help'")
            sys.exit(1)
        
        # Parse arguments based on command
        if command == "add":
            if len(sys.argv) < 6:
                logger.error("Not enough arguments for 'add' command")
                print_help()
                sys.exit(1)
                
            table_name = sys.argv[2]
            column_name = sys.argv[3]
            data_type = sys.argv[4]
            
            if sys.argv[5] != "after" or len(sys.argv) < 7:
                logger.error("Missing 'after' keyword or reference column")
                print_help()
                sys.exit(1)
                
            after_column = sys.argv[6]
            
            # Check for connection string
            if len(sys.argv) > 7 and sys.argv[7].startswith("--db="):
                connection_string = sys.argv[7][5:]
        
        elif command == "move":
            if len(sys.argv) < 5:
                logger.error("Not enough arguments for 'move' command")
                print_help()
                sys.exit(1)
                
            table_name = sys.argv[2]
            column_name = sys.argv[3]
            
            if sys.argv[4] != "after" or len(sys.argv) < 6:
                logger.error("Missing 'after' keyword or reference column")
                print_help()
                sys.exit(1)
                
            after_column = sys.argv[5]
            
            # Check for connection string
            if len(sys.argv) > 6 and sys.argv[6].startswith("--db="):
                connection_string = sys.argv[6][5:]
                
        # Execute the command
        conn = get_connection(connection_string)
        
        if command == "add":
            add_column(conn, table_name, column_name, data_type, after_column)
        elif command == "move":
            move_column(conn, table_name, column_name, after_column)
            
        conn.close()
        
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()