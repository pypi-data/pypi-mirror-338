import unittest
from unittest.mock import patch, MagicMock
import psycopg2
import sys

# Add parent directory to path to import pgcolpos
sys.path.append('..')
from pgcolpos.main import add_column, move_column, get_table_info, get_constraints

class TestPgColPos(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()