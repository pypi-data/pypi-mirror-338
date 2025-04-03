"""
PostgreSQL Column Position Tool

A utility to add or move columns to specific positions in PostgreSQL tables
while preserving all constraints, indexes, permissions, and references.
"""

__version__ = '0.1.0'

from .main import add_column, move_column

__all__ = ['add_column', 'move_column']