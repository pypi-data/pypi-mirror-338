"""
PostgreSQL Column Position Tool

A utility to add or move columns to specific positions in PostgreSQL tables
while preserving all constraints, indexes, permissions, and references.
"""

__version__ = '0.3.0'

# Import all functions from main module
from .main import (
    get_connection,
    add_column,
    move_column,
    add_column_batched,
    move_column_batched,
    add_column_view,
    add_column_with_pg_repack,
    estimate_migration_time
)

__all__ = [
    'get_connection',
    'add_column',
    'move_column',
    'add_column_batched',
    'move_column_batched',
    'add_column_view',
    'add_column_with_pg_repack',
    'estimate_migration_time'
]