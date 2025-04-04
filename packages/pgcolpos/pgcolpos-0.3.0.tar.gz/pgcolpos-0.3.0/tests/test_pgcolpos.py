import unittest
from unittest.mock import patch, MagicMock, call
import psycopg2
import sys

# Add parent directory to path to import pgcolpos
sys.path.append('..')
from pgcolpos.main import (
    add_column, 
    move_column, 
    get_table_info, 
    get_constraints,
    add_column_batched,
    move_column_batched,
    add_column_view,
    add_column_with_pg_repack,
    estimate_migration_time
)

class TestPgColPos(unittest.TestCase):
    """Test the standard implementations"""
    
    @patch('pgcolpos.main.get_table_info')
    @patch('pgcolpos.main.get_constraints')
    @patch('pgcolpos.main.get_indexes')
    @patch('pgcolpos.main.get_permissions')
    @patch('pgcolpos.main.create_new_table')
    def test_add_column(self, mock_create_new_table, mock_get_permissions, 
                        mock_get_indexes, mock_get_constraints, mock_get_table_info):
        # Mock the database connection
        conn = MagicMock()
        
        # Set up mock return values
        mock_get_table_info.return_value = [
            ('id', 'integer', None, None, 'NO'),
            ('name', 'character varying', 255, None, 'YES')
        ]
        mock_get_constraints.return_value = ([], [])
        mock_get_indexes.return_value = []
        mock_get_permissions.return_value = []
        
        # Call the function to test
        add_column(conn, 'users', 'email', 'varchar(255)', 'name')
        
        # Verify the mocks were called with correct parameters
        mock_get_table_info.assert_called_once_with(conn, 'users')
        mock_get_constraints.assert_called_once_with(conn, 'users')
        mock_get_indexes.assert_called_once_with(conn, 'users')
        mock_get_permissions.assert_called_once_with(conn, 'users')
        
        # The last call should be to create_new_table with the proper columns
        # (including the new one after 'name')
        args, kwargs = mock_create_new_table.call_args
        self.assertEqual(args[0], conn)
        self.assertEqual(args[1], 'users')
        
        # Check that the original columns are preserved
        self.assertEqual(len(args[2]), 2)
        
        # Check that the new column set includes our new column in the right order
        new_columns = args[3]
        self.assertEqual(len(new_columns), 3)
        self.assertEqual(new_columns[0][0], 'id')
        self.assertEqual(new_columns[1][0], 'name')
        self.assertEqual(new_columns[2][0], 'email')
        self.assertEqual(new_columns[2][1], 'varchar(255)')

    @patch('pgcolpos.main.get_table_info')
    @patch('pgcolpos.main.get_constraints')
    @patch('pgcolpos.main.get_indexes')
    @patch('pgcolpos.main.get_permissions')
    @patch('pgcolpos.main.create_new_table')
    def test_move_column(self, mock_create_new_table, mock_get_permissions, 
                         mock_get_indexes, mock_get_constraints, mock_get_table_info):
        # Mock the database connection
        conn = MagicMock()
        
        # Set up mock return values
        mock_get_table_info.return_value = [
            ('id', 'integer', None, None, 'NO'),
            ('name', 'character varying', 255, None, 'YES'),
            ('email', 'character varying', 255, None, 'YES')
        ]
        mock_get_constraints.return_value = ([], [])
        mock_get_indexes.return_value = []
        mock_get_permissions.return_value = []
        
        # Call the function to test
        move_column(conn, 'users', 'email', 'id')
        
        # Verify the mocks were called with correct parameters
        mock_get_table_info.assert_called_once_with(conn, 'users')
        mock_get_constraints.assert_called_once_with(conn, 'users')
        mock_get_indexes.assert_called_once_with(conn, 'users')
        mock_get_permissions.assert_called_once_with(conn, 'users')
        
        # The last call should be to create_new_table with the columns reordered
        args, kwargs = mock_create_new_table.call_args
        self.assertEqual(args[0], conn)
        self.assertEqual(args[1], 'users')
        
        # Check that all columns are preserved
        self.assertEqual(len(args[2]), 3)
        
        # Check that the columns are in the right order with 'email' after 'id'
        new_columns = args[3]
        self.assertEqual(len(new_columns), 3)
        self.assertEqual(new_columns[0][0], 'id')
        self.assertEqual(new_columns[1][0], 'email')
        self.assertEqual(new_columns[2][0], 'name')

class TestPgColPosOptimized(unittest.TestCase):
    """Test the optimized implementations"""

    @patch('pgcolpos.main.get_table_info')
    @patch('pgcolpos.main.get_constraints')
    @patch('pgcolpos.main.get_indexes')
    @patch('pgcolpos.main.get_permissions')
    def test_add_column_batched(self, mock_get_permissions, mock_get_indexes, 
                              mock_get_constraints, mock_get_table_info):
        # Mock the database connection
        conn = MagicMock()
        cursor = MagicMock()
        conn.cursor.return_value = cursor
        server_cursor = MagicMock()
        conn.cursor.return_value.__enter__.return_value = server_cursor
        
        # Set up mock return values
        mock_get_table_info.return_value = [
            ('id', 'integer', None, None, 'NO'),
            ('name', 'character varying', 255, None, 'YES')
        ]
        mock_get_constraints.return_value = (
            [('pk_id', 'p', 'id')],  # Primary key constraint
            []  # Foreign keys
        )
        mock_get_indexes.return_value = [
            ('idx_name', 'name', False, 'CREATE INDEX idx_name ON users(name)')
        ]
        mock_get_permissions.return_value = [
            ('user1', 'SELECT'),
            ('user1', 'INSERT')
        ]
        
        # Mock server cursor fetchmany to return one batch of data then empty
        server_cursor.fetchmany.side_effect = [
            [(1, 'John'), (2, 'Jane')],  # First batch
            []  # No more data
        ]
        
        # Mock count query
        cursor.fetchone.return_value = (2,)  # Total row count
        
        # Call the function to test
        add_column_batched(conn, 'users', 'email', 'varchar(255)', 'name', batch_size=10)
        
        # Verify the mocks were called with correct parameters
        mock_get_table_info.assert_called_once_with(conn, 'users')
        mock_get_constraints.assert_called_once_with(conn, 'users')
        mock_get_indexes.assert_called_once_with(conn, 'users')
        mock_get_permissions.assert_called_once_with(conn, 'users')
        
        # Check that table creation was called with proper parameters
        create_table_calls = [call for call in cursor.execute.call_args_list 
                             if 'CREATE TABLE users_new' in str(call)]
        self.assertTrue(create_table_calls, "Table creation was not called")
        
        # Check that batch insertion was called
        self.assertTrue(any('INSERT INTO users_new' in str(call) 
                           for call in cursor.executemany.call_args_list),
                      "Batch insertion was not called")
        
        # Check that table renaming was called
        rename_calls = [call for call in cursor.execute.call_args_list 
                        if 'RENAME TO users' in str(call)]
        self.assertTrue(rename_calls, "Table renaming was not called")
        
        # Check commit was called
        conn.commit.assert_called()

    @patch('psycopg2.sql.SQL')
    @patch('psycopg2.sql.Identifier')
    def test_add_column_view(self, mock_identifier, mock_sql):
        # Mock the database connection
        conn = MagicMock()
        cursor = MagicMock()
        conn.cursor.return_value = cursor
        
        # Mock cursor fetchall to return the columns
        cursor.fetchall.return_value = [
            ('id',), ('name',), ('email',)
        ]
        
        # Call the function to test
        add_column_view(conn, 'users', 'email', 'varchar(255)', 'name')
        
        # Verify ALTER TABLE was called to add the column
        self.assertTrue(any('ALTER TABLE' in str(call) for call in mock_sql.call_args_list),
                      "ALTER TABLE was not called")
                      
        # Verify CREATE VIEW was called
        self.assertTrue(any('CREATE OR REPLACE VIEW' in str(call) for call in mock_sql.call_args_list),
                      "CREATE OR REPLACE VIEW was not called")
        
        # Check commit was called
        conn.commit.assert_called()

    @patch('pgcolpos.main.subprocess.run')
    def test_add_column_with_pg_repack(self, mock_subprocess_run):
        # Mock the database connection
        conn = MagicMock()
        cursor = MagicMock()
        conn.cursor.return_value = cursor
        
        # Mock check for pg_repack availability and installation
        cursor.fetchone.side_effect = [(1,), (1,)]  # Extension is available and installed
        
        # Mock cursor fetchall to return the columns
        cursor.fetchall.return_value = [
            ('id',), ('name',), ('email',)
        ]
        
        # Mock subprocess result
        mock_subprocess_run.return_value.returncode = 0
        mock_subprocess_run.return_value.stderr = ""
        
        # Mock connection parameters
        conn.get_dsn_parameters.return_value = {
            'host': 'localhost',
            'port': '5432',
            'user': 'postgres',
            'dbname': 'postgres'
        }
        
        # Call the function to test
        add_column_with_pg_repack(conn, 'users', 'email', 'varchar(255)', 'name')
        
        # Verify ALTER TABLE was called to add the column
        self.assertTrue(any('ALTER TABLE' in str(call) for call in cursor.execute.mock_calls),
                      "ALTER TABLE was not called")
                      
        # Check that pg_repack was called with correct parameters
        mock_subprocess_run.assert_called_once()
        call_args = mock_subprocess_run.call_args[0][0]
        self.assertEqual(call_args[0], 'pg_repack')
        self.assertTrue('-t' in call_args)
        self.assertTrue('users' in call_args)
        
        # Check commit was called
        conn.commit.assert_called()

    def test_estimate_migration_time(self):
        # Mock the database connection
        conn = MagicMock()
        cursor = MagicMock()
        conn.cursor.return_value = cursor
        
        # Mock size query results
        cursor.fetchone.side_effect = [
            # Table size info
            ('1.2 GB', '850 MB', '350 MB', 5000000),
            # System info
            (512, 4)
        ]
        
        # Call the function to test
        result = estimate_migration_time(conn, 'users')
        
        # Check the structure of the result
        self.assertIn('table_info', result)
        self.assertIn('estimated_times', result)
        self.assertIn('recommended_approach', result)
        
        # Verify table info
        table_info = result['table_info']
        self.assertEqual(table_info['name'], 'users')
        self.assertEqual(table_info['total_size'], '1.2 GB')
        self.assertEqual(table_info['row_count'], 5000000)
        
        # Verify estimated times exist
        estimated_times = result['estimated_times']
        self.assertIn('standard_approach', estimated_times)
        self.assertIn('batched_approach', estimated_times)
        self.assertIn('view_approach', estimated_times)
        self.assertIn('pg_repack_approach', estimated_times)
        
        # For a table of 5M rows, it should recommend batched or pg_repack
        self.assertIn(result['recommended_approach'], 
                    ['batched_approach', 'pg_repack_approach'])

    @patch('pgcolpos.main.get_table_info')
    @patch('pgcolpos.main.get_constraints')
    @patch('pgcolpos.main.get_indexes')
    @patch('pgcolpos.main.get_permissions')
    def test_move_column_batched(self, mock_get_permissions, mock_get_indexes, 
                               mock_get_constraints, mock_get_table_info):
        # Mock the database connection
        conn = MagicMock()
        cursor = MagicMock()
        conn.cursor.return_value = cursor
        server_cursor = MagicMock()
        conn.cursor.return_value.__enter__.return_value = server_cursor
        
        # Set up mock return values
        mock_get_table_info.return_value = [
            ('id', 'integer', None, None, 'NO'),
            ('name', 'character varying', 255, None, 'YES'),
            ('email', 'character varying', 255, None, 'YES')
        ]
        mock_get_constraints.return_value = (
            [('pk_id', 'p', 'id')],  # Primary key constraint
            []  # Foreign keys
        )
        mock_get_indexes.return_value = [
            ('idx_name', 'name', False, 'CREATE INDEX idx_name ON users(name)')
        ]
        mock_get_permissions.return_value = [
            ('user1', 'SELECT'),
            ('user1', 'INSERT')
        ]
        
        # Mock server cursor fetchmany to return one batch of data then empty
        server_cursor.fetchmany.side_effect = [
            [(1, 'John', 'john@example.com'), (2, 'Jane', 'jane@example.com')],  # First batch
            []  # No more data
        ]
        
        # Mock count query
        cursor.fetchone.return_value = (2,)  # Total row count
        
        # Call the function to test
        move_column_batched(conn, 'users', 'email', 'id', batch_size=10)
        
        # Verify the mocks were called with correct parameters
        mock_get_table_info.assert_called_once_with(conn, 'users')
        mock_get_constraints.assert_called_once_with(conn, 'users')
        mock_get_indexes.assert_called_once_with(conn, 'users')
        mock_get_permissions.assert_called_once_with(conn, 'users')
        
        # Check that table creation was called with proper parameters
        create_table_calls = [call for call in cursor.execute.call_args_list 
                             if 'CREATE TABLE users_new' in str(call)]
        self.assertTrue(create_table_calls, "Table creation was not called")
        
        # Check that batch insertion was called
        self.assertTrue(any('INSERT INTO users_new' in str(call) 
                           for call in cursor.executemany.call_args_list),
                      "Batch insertion was not called")
        
        # Check that table renaming was called
        rename_calls = [call for call in cursor.execute.call_args_list 
                        if 'RENAME TO users' in str(call)]
        self.assertTrue(rename_calls, "Table renaming was not called")
        
        # Check commit was called
        conn.commit.assert_called()


if __name__ == '__main__':
    unittest.main()