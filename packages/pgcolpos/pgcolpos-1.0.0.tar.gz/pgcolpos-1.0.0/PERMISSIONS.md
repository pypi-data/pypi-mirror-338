# PostgreSQL Permissions for Column Position Tool

This document outlines the permissions required to use the PostgreSQL Column Position Tool (pgcolpos).

## Required Permissions

The database user executing the commands must have one of the following:

1. **Ownership of the tables** being modified (recommended)
2. **Superuser privileges** on the PostgreSQL server

### Specific Permissions Required

If you want to grant the minimum required permissions rather than using a superuser:

#### For Table Analysis
- SELECT on the target table
- SELECT on various catalog tables:
  - pg_catalog.pg_class
  - pg_catalog.pg_namespace
  - pg_catalog.pg_attribute
  - pg_catalog.pg_constraint
  - pg_catalog.pg_index
  - pg_catalog.pg_settings
  - pg_catalog.pg_available_extensions
  - pg_catalog.pg_extension
  - information_schema.role_table_grants
  - information_schema.columns
  - information_schema.table_constraints
  - information_schema.key_column_usage
  - information_schema.constraint_column_usage

#### For Adding/Moving Columns
- Table OWNERSHIP is required for:
  - Adding columns
  - Creating new tables
  - Dropping tables
  - Renaming tables
- CREATE permission on the schema
- USAGE permission on the schema
- TEMP permission on the database (for some operations)

## Setting Up Permissions

### Option 1: Make the User a Table Owner

To ensure your user has ownership of a table:

```sql
-- For existing tables
ALTER TABLE your_table OWNER TO your_user;

-- For new tables, create them as the user who will perform operations
```

### Option 2: Grant Superuser Privileges (Development Only)

For development or controlled environments only:

```sql
ALTER USER your_user WITH SUPERUSER;
```

**Warning**: This grants full administrative access to the database server and should not be used in production environments.

### Option 3: Schema-Wide Ownership

To make a user automatically the owner of all new tables in a schema:

```sql
-- Grant schema ownership
ALTER SCHEMA public OWNER TO your_user;

-- For PostgreSQL 9.0+, set default privileges
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON TABLES TO your_user;
```

## Permission Helper Script

You can run the following script as a database superuser to grant the required permissions:

```sql
-- Grant schema privileges
GRANT USAGE, CREATE ON SCHEMA public TO your_user;

-- Grant table ownership (repeat for each table)
ALTER TABLE your_table OWNER TO your_user;

-- Grant catalog access
GRANT SELECT ON pg_catalog.pg_class TO your_user;
GRANT SELECT ON pg_catalog.pg_namespace TO your_user;
GRANT SELECT ON pg_catalog.pg_attribute TO your_user;
GRANT SELECT ON pg_catalog.pg_constraint TO your_user;
GRANT SELECT ON pg_catalog.pg_index TO your_user;
GRANT SELECT ON pg_catalog.pg_settings TO your_user;
GRANT SELECT ON pg_catalog.pg_available_extensions TO your_user;
GRANT SELECT ON pg_catalog.pg_extension TO your_user;
GRANT SELECT ON pg_catalog.pg_roles TO your_user;

-- Grant information schema access
GRANT SELECT ON information_schema.role_table_grants TO your_user;
GRANT SELECT ON information_schema.columns TO your_user;
GRANT SELECT ON information_schema.table_constraints TO your_user;
GRANT SELECT ON information_schema.key_column_usage TO your_user;
GRANT SELECT ON information_schema.constraint_column_usage TO your_user;

-- Grant database-level privileges
GRANT TEMP ON DATABASE your_database TO your_user;
```

## Troubleshooting Permission Issues

Common permission errors:

1. **must be owner of table XXX**: This user isn't the table owner
   - Solution: Use ALTER TABLE XXX OWNER TO your_user;

2. **permission denied for schema public**: User can't create objects in schema
   - Solution: GRANT USAGE, CREATE ON SCHEMA public TO your_user;

3. **permission denied for relation pg_XXX**: User can't query system catalogs
   - Solution: Grant the appropriate SELECT permissions on catalog tables