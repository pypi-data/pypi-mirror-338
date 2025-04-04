#!/usr/bin/env python3
"""
PostgreSQL Column Position Tool.

Core functionality for adding or moving columns to specific positions
in PostgreSQL tables while preserving all constraints, indexes, and permissions.
Includes standard and optimized implementations for tables of all sizes.
"""

import sys
import psycopg2
from psycopg2 import sql
import logging
import subprocess
from typing import Dict, List, Tuple, Union, Any, Optional

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('pgcolpos')

#####################################
# Database Connection and Utilities #
#####################################

def get_connection(connection_string: str) -> psycopg2.extensions.connection:
    """Establish a database connection"""
    try:
        conn = psycopg2.connect(connection_string)
        return conn
    except Exception as e:
        logger.error(f"Connection error: {e}")
        sys.exit(1)

def get_table_info(conn: psycopg2.extensions.connection, table_name: str) -> List[Tuple]:
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

def get_constraints(conn: psycopg2.extensions.connection, table_name: str) -> Tuple[List[Tuple], List[Tuple]]:
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

def get_indexes(conn: psycopg2.extensions.connection, table_name: str) -> List[Tuple]:
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

def get_permissions(conn: psycopg2.extensions.connection, table_name: str) -> List[Tuple]:
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

def generate_new_column_definition(
    conn: psycopg2.extensions.connection, 
    table_name: str, 
    columns: List[Tuple], 
    new_column_name: str, 
    data_type: Optional[str], 
    after_column: str
) -> List[Tuple]:
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

#################################
# Standard Implementation       #
#################################

def create_new_table(
    conn: psycopg2.extensions.connection, 
    table_name: str, 
    columns: List[Tuple], 
    new_columns: List[Tuple], 
    constraints: List[Tuple], 
    foreign_keys: List[Tuple], 
    indexes: List[Tuple], 
    permissions: List[Tuple]
) -> None:
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

def add_column(
    conn: psycopg2.extensions.connection, 
    table_name: str, 
    column_name: str, 
    data_type: str, 
    after_column: str
) -> None:
    """Add a new column after a specific column using the standard approach"""
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

def move_column(
    conn: psycopg2.extensions.connection, 
    table_name: str, 
    column_name: str, 
    after_column: str
) -> None:
    """Move an existing column after a specific column using the standard approach"""
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

#################################
# Optimized Implementation      #
#################################

def add_column_view(
    conn: psycopg2.extensions.connection, 
    table_name: str, 
    column_name: str, 
    data_type: str, 
    after_column: str
) -> None:
    """
    Create a view that appears to have the column added at the desired position.
    This is the fastest approach but only affects how the data is presented, not stored.
    """
    cursor = conn.cursor()
    try:
        # First, add the column to the end of the table (fast operation)
        add_column_sql = sql.SQL("ALTER TABLE {} ADD COLUMN {} {}").format(
            sql.Identifier(table_name),
            sql.Identifier(column_name),
            sql.SQL(data_type)
        )
        logger.info(f"Adding column {column_name} to table {table_name}")
        cursor.execute(add_column_sql)
        
        # Get all columns in the table
        cursor.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = %s 
            ORDER BY ordinal_position
        """, (table_name,))
        
        columns = [row[0] for row in cursor.fetchall()]
        
        # Create column list in the desired order
        view_columns = []
        for col in columns:
            if col == column_name:
                # Skip it here, we'll add it after the reference column
                continue
            view_columns.append(col)
            if col == after_column:
                view_columns.append(column_name)
        
        # Create a view with the columns in the desired order
        view_name = f"{table_name}_view"
        create_view_sql = sql.SQL("CREATE OR REPLACE VIEW {} AS SELECT {} FROM {}").format(
            sql.Identifier(view_name),
            sql.SQL(", ").join(map(sql.Identifier, view_columns)),
            sql.Identifier(table_name)
        )
        
        logger.info(f"Creating view {view_name} with reordered columns")
        cursor.execute(create_view_sql)
        
        # Commit the transaction
        conn.commit()
        logger.info(f"Column {column_name} added to view {view_name} after {after_column}")
        logger.info(f"NOTE: Physical table structure remains unchanged. Use the view {view_name} for the desired column order.")
        
    except Exception as e:
        conn.rollback()
        logger.error(f"Error: {e}")
        raise
    finally:
        cursor.close()

def add_column_with_pg_repack(
    conn: psycopg2.extensions.connection, 
    table_name: str, 
    column_name: str, 
    data_type: str, 
    after_column: str
) -> None:
    """
    Add a column to a table using pg_repack for better performance with large tables.
    This requires the pg_repack extension to be installed.
    """
    cursor = conn.cursor()
    try:
        # Check if pg_repack extension is available
        cursor.execute("SELECT 1 FROM pg_available_extensions WHERE name = 'pg_repack'")
        if cursor.fetchone() is None:
            logger.error("pg_repack extension is not available. Please install it first.")
            return
            
        # Check if pg_repack extension is installed
        cursor.execute("SELECT 1 FROM pg_extension WHERE extname = 'pg_repack'")
        if cursor.fetchone() is None:
            logger.info("Creating pg_repack extension")
            cursor.execute("CREATE EXTENSION pg_repack")
            
        # First, add the column to the end of the table (fast operation)
        add_column_sql = sql.SQL("ALTER TABLE {} ADD COLUMN {} {}").format(
            sql.Identifier(table_name),
            sql.Identifier(column_name),
            sql.SQL(data_type)
        )
        logger.info(f"Adding column {column_name} to table {table_name}")
        cursor.execute(add_column_sql)
        conn.commit()
        
        # Get all columns in the table
        cursor.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = %s 
            ORDER BY ordinal_position
        """, (table_name,))
        
        columns = [row[0] for row in cursor.fetchall()]
        
        # Create a table definition with columns in the desired order
        reordered_columns = []
        for col in columns:
            if col == column_name:
                # Skip it here, we'll add it after the reference column
                continue
            reordered_columns.append(col)
            if col == after_column:
                reordered_columns.append(column_name)
                
        # Create a special DDL file for pg_repack
        ddl_file = f"/tmp/{table_name}_repack.sql"
        with open(ddl_file, "w") as f:
            f.write(f"ALTER TABLE {table_name} RENAME TO {table_name}_old;\n")
            f.write(f"CREATE TABLE {table_name} AS SELECT {', '.join(reordered_columns)} FROM {table_name}_old WITH NO DATA;\n")
            f.write(f"DROP TABLE {table_name}_old CASCADE;\n")
            
        # Use pg_repack with the custom DDL
        db_params = conn.get_dsn_parameters()
        cmd = [
            "pg_repack",
            "-h", db_params.get("host", "localhost"),
            "-p", db_params.get("port", "5432"),
            "-U", db_params.get("user", "postgres"),
            "-d", db_params.get("dbname", "postgres"),
            "-k",  # Keep constraints
            "-o", f"ddl={ddl_file}",
            "-t", table_name
        ]
        
        logger.info(f"Running pg_repack to reorganize table {table_name}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            logger.error(f"pg_repack failed: {result.stderr}")
            raise Exception(f"pg_repack failed: {result.stderr}")
            
        logger.info(f"Successfully reorganized table {table_name} with column {column_name} after {after_column}")
        
    except Exception as e:
        conn.rollback()
        logger.error(f"Error: {e}")
        raise
    finally:
        cursor.close()

def add_column_batched(
    conn: psycopg2.extensions.connection, 
    table_name: str, 
    column_name: str, 
    data_type: str, 
    after_column: str, 
    batch_size: int = 10000
) -> None:
    """
    Add a column to a large table using a batched approach to minimize locking and memory usage.
    This approach:
    1. Creates a new table with the desired column order
    2. Copies data in batches using a cursor
    3. Recreates indexes after data is loaded
    4. Swaps the tables
    """
    cursor = conn.cursor()
    try:
        # Get table information
        columns = get_table_info(conn, table_name)
        constraints, foreign_keys = get_constraints(conn, table_name)
        indexes = get_indexes(conn, table_name)
        permissions = get_permissions(conn, table_name)
        
        # Check if column already exists
        column_names = [col[0] for col in columns]
        if column_name in column_names:
            logger.error(f"Column '{column_name}' already exists in table '{table_name}'")
            return
            
        # Get a primary key or unique index for batching
        primary_key = None
        for constraint in constraints:
            constraint_name, constraint_type, column = constraint
            if constraint_type == 'p':  # Primary key
                primary_key = column
                break
                
        if not primary_key:
            # Look for a unique index if no primary key
            for index in indexes:
                index_name, column, is_unique, _ = index
                if is_unique:
                    primary_key = column
                    break
                    
        if not primary_key:
            logger.warning("No primary key or unique index found. Batching may be less efficient.")
            primary_key = columns[0][0]  # Use the first column as a fallback
            
        # Generate new column definitions
        new_columns = []
        for col in columns:
            col_name, col_type, max_length, default, nullable = col
            new_columns.append(col)
            if col_name == after_column:
                # Add the new column after this one
                new_columns.append((column_name, data_type, None, None, 'YES'))
                
        # Create a temporary table with the desired column order
        temp_table = f"{table_name}_new"
        create_stmt = f"CREATE TABLE {temp_table} (\n"
        
        column_definitions = []
        for col in new_columns:
            col_name, col_type, max_length, default, nullable = col
            
            # Build the column definition
            col_def = f"{col_name} {col_type}"
            if max_length:
                col_def += f"({max_length})"
            
            if default:
                col_def += f" DEFAULT {default}"
                
            if nullable == 'NO':
                col_def += " NOT NULL"
                
            column_definitions.append(col_def)
        
        create_stmt += ",\n".join(column_definitions)
        create_stmt += "\n)"
        
        logger.info(f"Creating new table: {temp_table}")
        cursor.execute(create_stmt)
        
        # Prepare the column list for copying data
        old_column_names = [col[0] for col in columns]
        new_column_names = [col[0] for col in new_columns if col[0] != column_name]  # Exclude the new column
        
        # Get the total number of rows
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        total_rows = cursor.fetchone()[0]
        logger.info(f"Total rows to migrate: {total_rows}")
        
        # Copy data in batches
        batches = max(1, total_rows // batch_size)
        logger.info(f"Will process in {batches} batches of {batch_size} rows")
        
        # Disable triggers temporarily for faster inserts
        cursor.execute(f"ALTER TABLE {temp_table} DISABLE TRIGGER ALL")
        
        # Create a server-side cursor for efficient batch processing
        with conn.cursor(name='table_copy_cursor') as server_cursor:
            server_cursor.execute(f"SELECT {', '.join(old_column_names)} FROM {table_name}")
            
            batch_num = 0
            rows_processed = 0
            
            while True:
                # Fetch a batch of rows
                rows = server_cursor.fetchmany(batch_size)
                if not rows:
                    break
                    
                batch_num += 1
                rows_processed += len(rows)
                
                # Start a subtransaction
                cursor.execute("SAVEPOINT batch_insert")
                
                try:
                    # Insert the batch
                    args_str = ','.join(['%s'] * len(rows))
                    cursor.executemany(
                        f"INSERT INTO {temp_table} ({', '.join(new_column_names)}) VALUES ({', '.join(['%s'] * len(new_column_names))})",
                        [[row[old_column_names.index(col)] for col in new_column_names] for row in rows]
                    )
                    
                    # Release the savepoint
                    cursor.execute("RELEASE SAVEPOINT batch_insert")
                    
                except Exception as e:
                    # If there's an error, rollback this batch but continue processing
                    cursor.execute("ROLLBACK TO SAVEPOINT batch_insert")
                    logger.error(f"Error inserting batch {batch_num}: {e}")
                    
                logger.info(f"Processed batch {batch_num}/{batches} ({rows_processed}/{total_rows} rows)")
                
        # Re-enable triggers
        cursor.execute(f"ALTER TABLE {temp_table} ENABLE TRIGGER ALL")
        
        # Drop constraints from the original table to avoid name conflicts
        for constraint in constraints:
            constraint_name, constraint_type, column = constraint
            if constraint_type == 'p':  # Primary key
                logger.info(f"Dropping primary key from {table_name}")
                cursor.execute(f"ALTER TABLE {table_name} DROP CONSTRAINT IF EXISTS {constraint_name}")
        
        for fk in foreign_keys:
            constraint_name, _, _, _, _ = fk
            logger.info(f"Dropping foreign key {constraint_name} from {table_name}")
            cursor.execute(f"ALTER TABLE {table_name} DROP CONSTRAINT IF EXISTS {constraint_name}")
            
        # Now recreate primary key and unique constraints on the new table
        for constraint in constraints:
            constraint_name, constraint_type, column = constraint
            
            if constraint_type == 'p':  # Primary key
                logger.info(f"Adding primary key on {column} to {temp_table}")
                cursor.execute(f"ALTER TABLE {temp_table} ADD PRIMARY KEY ({column})")
            elif constraint_type == 'u':  # Unique constraint
                logger.info(f"Adding unique constraint on {column} to {temp_table}")
                cursor.execute(f"ALTER TABLE {temp_table} ADD CONSTRAINT {constraint_name} UNIQUE ({column})")
        
        # Rename tables to swap them
        logger.info(f"Renaming tables to swap {table_name} and {temp_table}")
        cursor.execute(f"ALTER TABLE {table_name} RENAME TO {table_name}_old")
        cursor.execute(f"ALTER TABLE {temp_table} RENAME TO {table_name}")
        
        # Recreate foreign key constraints
        for fk in foreign_keys:
            constraint_name, table_name_fk, column_name_fk, referenced_table, referenced_column = fk
            logger.info(f"Recreating foreign key constraint: {constraint_name}")
            cursor.execute(f"""
                ALTER TABLE {table_name}
                ADD CONSTRAINT {constraint_name}
                FOREIGN KEY ({column_name_fk})
                REFERENCES {referenced_table} ({referenced_column})
            """)
        
        # Recreate indexes
        recreated_indexes = set()
        for index in indexes:
            index_name, column_name_idx, is_unique, index_def = index
            
            # Skip indexes that are part of constraints (they're recreated with the constraints)
            if is_unique or index_name in recreated_indexes:
                continue
                
            logger.info(f"Recreating index: {index_name}")
            # Use the full definition because it includes things like partial indexes, etc.
            modified_def = index_def.replace(f'"{table_name}_old"', f'"{table_name}"')
            cursor.execute(modified_def)
            recreated_indexes.add(index_name)
        
        # Restore permissions
        for permission in permissions:
            grantee, privilege_type = permission
            logger.info(f"Restoring {privilege_type} permission for {grantee}")
            cursor.execute(f"GRANT {privilege_type} ON {table_name} TO {grantee}")
            
        # Drop the old table
        logger.info(f"Dropping old table: {table_name}_old")
        cursor.execute(f"DROP TABLE {table_name}_old")
        
        # Commit everything
        conn.commit()
        logger.info(f"Successfully completed column addition on table {table_name}")
        
    except Exception as e:
        conn.rollback()
        logger.error(f"Error: {e}")
        raise
    finally:
        cursor.close()

def move_column_batched(
    conn: psycopg2.extensions.connection, 
    table_name: str, 
    column_name: str, 
    after_column: str, 
    batch_size: int = 10000
) -> None:
    """
    Move a column in a large table using a batched approach to minimize locking and memory usage.
    This is similar to add_column_batched but for moving an existing column.
    """
    cursor = conn.cursor()
    try:
        # Get table information
        columns = get_table_info(conn, table_name)
        constraints, foreign_keys = get_constraints(conn, table_name)
        indexes = get_indexes(conn, table_name)
        permissions = get_permissions(conn, table_name)
        
        # Check if column exists
        column_names = [col[0] for col in columns]
        if column_name not in column_names:
            logger.error(f"Column '{column_name}' does not exist in table '{table_name}'")
            return
        
        # Find the column to move
        column_to_move = None
        for col in columns:
            if col[0] == column_name:
                column_to_move = col
                break
                
        if column_to_move is None:
            logger.error(f"Column '{column_name}' not found in table structure")
            return
            
        # Generate new column definitions with the column moved to the new position
        new_columns = []
        column_added = False
        
        for col in columns:
            col_name = col[0]
            
            if col_name == column_name:
                # Skip it here, we'll add it after the reference column
                continue
                
            new_columns.append(col)
            
            if col_name == after_column:
                # Add the moved column after this one
                new_columns.append(column_to_move)
                column_added = True
                
        # If we didn't find the after_column, add the column at the end
        if not column_added:
            logger.error(f"Reference column '{after_column}' not found in table '{table_name}'")
            return
            
        # Get a primary key or unique index for batching
        primary_key = None
        for constraint in constraints:
            constraint_name, constraint_type, column = constraint
            if constraint_type == 'p':  # Primary key
                primary_key = column
                break
                
        if not primary_key:
            # Look for a unique index if no primary key
            for index in indexes:
                index_name, column, is_unique, _ = index
                if is_unique:
                    primary_key = column
                    break
                    
        if not primary_key:
            logger.warning("No primary key or unique index found. Batching may be less efficient.")
            primary_key = columns[0][0]  # Use the first column as a fallback
            
        # Create a temporary table with the desired column order
        temp_table = f"{table_name}_new"
        create_stmt = f"CREATE TABLE {temp_table} (\n"
        
        column_definitions = []
        for col in new_columns:
            col_name, col_type, max_length, default, nullable = col
            
            # Build the column definition
            col_def = f"{col_name} {col_type}"
            if max_length:
                col_def += f"({max_length})"
            
            if default:
                col_def += f" DEFAULT {default}"
                
            if nullable == 'NO':
                col_def += " NOT NULL"
                
            column_definitions.append(col_def)
        
        create_stmt += ",\n".join(column_definitions)
        create_stmt += "\n)"
        
        logger.info(f"Creating new table: {temp_table}")
        cursor.execute(create_stmt)
        
        # Get the total number of rows
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        total_rows = cursor.fetchone()[0]
        logger.info(f"Total rows to migrate: {total_rows}")
        
        # Copy data in batches
        batches = max(1, total_rows // batch_size)
        logger.info(f"Will process in {batches} batches of {batch_size} rows")
        
        # Disable triggers temporarily for faster inserts
        cursor.execute(f"ALTER TABLE {temp_table} DISABLE TRIGGER ALL")
        
        # Get column names for copying
        old_column_names = [col[0] for col in columns]
        new_column_names = [col[0] for col in new_columns]
        
        # Create a server-side cursor for efficient batch processing
        with conn.cursor(name='table_copy_cursor') as server_cursor:
            server_cursor.execute(f"SELECT {', '.join(old_column_names)} FROM {table_name}")
            
            batch_num = 0
            rows_processed = 0
            
            while True:
                # Fetch a batch of rows
                rows = server_cursor.fetchmany(batch_size)
                if not rows:
                    break
                    
                batch_num += 1
                rows_processed += len(rows)
                
                # Start a subtransaction
                cursor.execute("SAVEPOINT batch_insert")
                
                try:
                    # Insert the batch into the new table with reordered columns
                    args_str = ','.join(['%s'] * len(new_columns))
                    cursor.executemany(
                        f"INSERT INTO {temp_table} ({', '.join(new_column_names)}) VALUES ({', '.join(['%s'] * len(new_column_names))})",
                        [
                            [row[old_column_names.index(col[0])] for col in new_columns]
                            for row in rows
                        ]
                    )
                    
                    # Release the savepoint
                    cursor.execute("RELEASE SAVEPOINT batch_insert")
                    
                except Exception as e:
                    # If there's an error, rollback this batch but continue processing
                    cursor.execute("ROLLBACK TO SAVEPOINT batch_insert")
                    logger.error(f"Error inserting batch {batch_num}: {e}")
                    
                logger.info(f"Processed batch {batch_num}/{batches} ({rows_processed}/{total_rows} rows)")
                
        # Re-enable triggers
        cursor.execute(f"ALTER TABLE {temp_table} ENABLE TRIGGER ALL")
        
        # The rest follows the same process as add_column_batched
        # Drop constraints from the original table
        for constraint in constraints:
            constraint_name, constraint_type, column = constraint
            if constraint_type == 'p':  # Primary key
                logger.info(f"Dropping primary key from {table_name}")
                cursor.execute(f"ALTER TABLE {table_name} DROP CONSTRAINT IF EXISTS {constraint_name}")
        
        for fk in foreign_keys:
            constraint_name, _, _, _, _ = fk
            logger.info(f"Dropping foreign key {constraint_name} from {table_name}")
            cursor.execute(f"ALTER TABLE {table_name} DROP CONSTRAINT IF EXISTS {constraint_name}")
            
        # Recreate primary key and unique constraints on the new table
        for constraint in constraints:
            constraint_name, constraint_type, column = constraint
            
            if constraint_type == 'p':  # Primary key
                logger.info(f"Adding primary key on {column} to {temp_table}")
                cursor.execute(f"ALTER TABLE {temp_table} ADD PRIMARY KEY ({column})")
            elif constraint_type == 'u':  # Unique constraint
                logger.info(f"Adding unique constraint on {column} to {temp_table}")
                cursor.execute(f"ALTER TABLE {temp_table} ADD CONSTRAINT {constraint_name} UNIQUE ({column})")
        
        # Rename tables to swap them
        logger.info(f"Renaming tables to swap {table_name} and {temp_table}")
        cursor.execute(f"ALTER TABLE {table_name} RENAME TO {table_name}_old")
        cursor.execute(f"ALTER TABLE {temp_table} RENAME TO {table_name}")
        
        # Recreate foreign key constraints
        for fk in foreign_keys:
            constraint_name, table_name_fk, column_name_fk, referenced_table, referenced_column = fk
            logger.info(f"Recreating foreign key constraint: {constraint_name}")
            cursor.execute(f"""
                ALTER TABLE {table_name}
                ADD CONSTRAINT {constraint_name}
                FOREIGN KEY ({column_name_fk})
                REFERENCES {referenced_table} ({referenced_column})
            """)
        
        # Recreate indexes
        recreated_indexes = set()
        for index in indexes:
            index_name, column_name_idx, is_unique, index_def = index
            
            # Skip indexes that are part of constraints
            if is_unique or index_name in recreated_indexes:
                continue
                
            logger.info(f"Recreating index: {index_name}")
            modified_def = index_def.replace(f'"{table_name}_old"', f'"{table_name}"')
            cursor.execute(modified_def)
            recreated_indexes.add(index_name)
        
        # Restore permissions
        for permission in permissions:
            grantee, privilege_type = permission
            logger.info(f"Restoring {privilege_type} permission for {grantee}")
            cursor.execute(f"GRANT {privilege_type} ON {table_name} TO {grantee}")
            
        # Drop the old table
        logger.info(f"Dropping old table: {table_name}_old")
        cursor.execute(f"DROP TABLE {table_name}_old")
        
        # Commit everything
        conn.commit()
        logger.info(f"Successfully moved column {column_name} after {after_column} in table {table_name}")
        
    except Exception as e:
        conn.rollback()
        logger.error(f"Error: {e}")
        raise
    finally:
        cursor.close()

#################################
# Analysis Functionality        #
#################################

def estimate_migration_time(conn: psycopg2.extensions.connection, table_name: str) -> Dict[str, Any]:
    """
    Estimate the time required for migrating a large table.
    This helps users make informed decisions about which approach to use.
    """
    cursor = conn.cursor()
    try:
        # Get table size information
        cursor.execute("""
            SELECT 
                pg_size_pretty(pg_total_relation_size(%s)) as total_size,
                pg_size_pretty(pg_relation_size(%s)) as table_size,
                pg_size_pretty(pg_indexes_size(%s)) as index_size,
                (SELECT COUNT(*) FROM {}) as row_count
        """.format(table_name), (table_name, table_name, table_name))
        
        size_info = cursor.fetchone()
        if not size_info:
            return {"error": "Table not found"}
            
        total_size, table_size, index_size, row_count = size_info
        
        # Get system statistics
        cursor.execute("""
            SELECT 
                setting::numeric as maintenance_work_mem,
                (SELECT setting::numeric FROM pg_settings WHERE name = 'max_parallel_workers') as workers
            FROM 
                pg_settings 
            WHERE 
                name = 'maintenance_work_mem'
        """)
        
        system_info = cursor.fetchone()
        maintenance_work_mem, max_workers = system_info
        
        # Estimate timings based on heuristics
        # These are very rough estimates and will vary greatly based on hardware, etc.
        
        # Base time per million rows on average hardware
        base_time_per_million = 60  # seconds
        
        # Adjust for table size (larger tables take longer per row)
        size_factor = 1.0
        if row_count > 10000000:  # 10M+ rows
            size_factor = 1.5
        elif row_count > 1000000:  # 1M+ rows
            size_factor = 1.2
            
        # Adjust for available memory
        mem_factor = 1.0
        if maintenance_work_mem < 64:  # Less than 64MB
            mem_factor = 1.5
        elif maintenance_work_mem > 1024:  # More than 1GB
            mem_factor = 0.8
            
        # Adjust for available workers
        worker_factor = 1.0
        if max_workers >= 4:
            worker_factor = 0.7
            
        # Calculate time for normal approach (full table recreation)
        normal_time = (row_count / 1000000) * base_time_per_million * size_factor * mem_factor * worker_factor
        
        # Batched approach is usually faster for large tables
        batched_factor = 0.7 if row_count > 1000000 else 0.9
        batched_time = normal_time * batched_factor
        
        # View approach is almost instantaneous
        view_time = 0.1  # seconds
        
        # pg_repack approach
        pg_repack_factor = 0.5  # Usually about 50% faster than normal approach
        pg_repack_time = normal_time * pg_repack_factor
        
        # Format times as human-readable
        def format_time(seconds):
            if seconds < 1:
                return "less than 1 second"
            elif seconds < 60:
                return f"{int(seconds)} seconds"
            elif seconds < 3600:
                return f"{int(seconds/60)} minutes"
            else:
                hours = int(seconds / 3600)
                minutes = int((seconds % 3600) / 60)
                return f"{hours} hours, {minutes} minutes"
                
        return {
            "table_info": {
                "name": table_name,
                "total_size": total_size,
                "table_size": table_size,
                "index_size": index_size,
                "row_count": row_count
            },
            "estimated_times": {
                "standard_approach": format_time(normal_time),
                "batched_approach": format_time(batched_time),
                "view_approach": format_time(view_time),
                "pg_repack_approach": format_time(pg_repack_time)
            },
            "recommended_approach": "view" if row_count > 10000000 else 
                                    "pg_repack" if row_count > 1000000 else
                                    "batched" if row_count > 100000 else
                                    "standard"
        }
        
    except Exception as e:
        logger.error(f"Error estimating migration time: {e}")
        return {"error": str(e)}
    finally:
        cursor.close()