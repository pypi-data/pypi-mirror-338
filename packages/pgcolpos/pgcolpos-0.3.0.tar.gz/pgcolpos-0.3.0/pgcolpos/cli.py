#!/usr/bin/env python3
"""
pgcolpos - PostgreSQL Column Position Tool

A command-line utility to add or move columns to specific positions in PostgreSQL tables
while preserving all constraints, indexes, permissions, and references.

Usage:
  pgcolpos add <table> <column_name> <data_type> after <reference_column> [--db=<connection_string>] [--method=<method>] [--batch-size=<size>]
  pgcolpos move <table> <column_name> after <reference_column> [--db=<connection_string>] [--method=<method>] [--batch-size=<size>]
  pgcolpos analyze <table> [--db=<connection_string>]
  pgcolpos --help

Methods:
  standard       Recreate the entire table (default for small tables)
  batched        Recreate the table using batch processing (recommended for medium to large tables)
  view           Create a view with the desired column order (fastest, but only affects presentation)
  pg_repack      Use pg_repack extension (fastest for physical reordering, requires extension)

Examples:
  pgcolpos add users email varchar(255) after username --db="postgresql://user:pass@localhost/mydb"
  pgcolpos move products description after name --db="postgresql://user:pass@localhost/mydb" --method=batched
  pgcolpos analyze orders --db="postgresql://user:pass@localhost/mydb"
"""

import sys
import logging
from pgcolpos.main import (
    get_connection,
    add_column,
    move_column,
    add_column_batched,
    move_column_batched,
    add_column_view,
    add_column_with_pg_repack,
    estimate_migration_time
)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('pgcolpos.cli')

def print_help():
    """Print help information"""
    print(__doc__)

def analyze_table(conn, table_name):
    """Analyze a table and recommend the best approach"""
    results = estimate_migration_time(conn, table_name)
    
    if "error" in results:
        logger.error(f"Error analyzing table: {results['error']}")
        return
        
    print("\nTable Analysis Results:")
    print("=======================")
    
    table_info = results["table_info"]
    print(f"\nTable: {table_info['name']}")
    print(f"Total Size: {table_info['total_size']}")
    print(f"Table Size: {table_info['table_size']}")
    print(f"Index Size: {table_info['index_size']}")
    print(f"Row Count: {table_info['row_count']:,}")
    
    print("\nEstimated Operation Times:")
    estimated_times = results["estimated_times"]
    print(f"Standard Approach: {estimated_times['standard_approach']}")
    print(f"Batched Approach: {estimated_times['batched_approach']}")
    print(f"View Approach: {estimated_times['view_approach']}")
    print(f"pg_repack Approach: {estimated_times['pg_repack_approach']}")
    
    print(f"\nRecommended Approach: {results['recommended_approach']}")
    
    if results['recommended_approach'] == 'view_approach':
        print("\nNote: The view approach doesn't physically reorder the columns.")
        print("It only affects how they're presented when querying the view.")
    elif results['recommended_approach'] == 'pg_repack_approach':
        print("\nNote: The pg_repack approach requires the pg_repack extension.")
        print("If you don't have it installed, use the batched approach instead.")
        
    return results['recommended_approach']

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
        
        if command not in ["add", "move", "analyze"]:
            logger.error("Invalid command. Use 'add', 'move', 'analyze' or '--help'")
            sys.exit(1)
            
        # Parse method and batch size
        method = "standard"  # Default method
        batch_size = 10000   # Default batch size
        
        # Extract --method and --batch-size arguments
        for i, arg in enumerate(sys.argv):
            if arg.startswith("--method="):
                method = arg[9:]
                sys.argv.pop(i)
                break
                
        for i, arg in enumerate(sys.argv):
            if arg.startswith("--batch-size="):
                try:
                    batch_size = int(arg[13:])
                    sys.argv.pop(i)
                except ValueError:
                    logger.error("Batch size must be an integer")
                    sys.exit(1)
                break
                
        # Handle connection string
        for i, arg in enumerate(sys.argv):
            if arg.startswith("--db="):
                connection_string = arg[5:]
                sys.argv.pop(i)
                break
        
        # Analyze command
        if command == "analyze":
            if len(sys.argv) < 3:
                logger.error("Not enough arguments for 'analyze' command")
                print_help()
                sys.exit(1)
                
            table_name = sys.argv[2]
            conn = get_connection(connection_string)
            analyze_table(conn, table_name)
            conn.close()
            sys.exit(0)
        
        # Add command
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
        
        # Move command
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
                
        # Execute the command
        conn = get_connection(connection_string)
        
        # If method is 'auto', analyze the table first
        if method == "auto":
            recommended_method = analyze_table(conn, table_name)
            method = recommended_method
            logger.info(f"Auto-selected method: {method}")
        
        # Execute the appropriate method
        if command == "add":
            if method == "standard":
                add_column(conn, table_name, column_name, data_type, after_column)
            elif method == "batched":
                add_column_batched(conn, table_name, column_name, data_type, after_column, batch_size)
            elif method == "view":
                add_column_view(conn, table_name, column_name, data_type, after_column)
            elif method == "pg_repack":
                add_column_with_pg_repack(conn, table_name, column_name, data_type, after_column)
            else:
                logger.error(f"Unknown method: {method}")
                sys.exit(1)
        
        elif command == "move":
            if method == "standard":
                move_column(conn, table_name, column_name, after_column)
            elif method == "batched":
                move_column_batched(conn, table_name, column_name, after_column, batch_size)
            elif method == "view":
                logger.error("View method is not supported for move operation yet")
                sys.exit(1)
            else:
                logger.error(f"Unknown method: {method}")
                sys.exit(1)
            
        conn.close()
        
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()