# PostgreSQL Column Position Tool (pgcolpos)

[![PyPI version](https://badge.fury.io/py/pgcolpos.svg)](https://badge.fury.io/py/pgcolpos)
[![Python Versions](https://img.shields.io/pypi/pyversions/pgcolpos.svg)](https://pypi.org/project/pgcolpos/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A command-line tool to add or move columns to specific positions in PostgreSQL tables while preserving all constraints, indexes, and permissions.

## Problem

PostgreSQL doesn't support the `AFTER` clause for column positioning like MySQL does. With standard PostgreSQL, new columns are always added at the end of a table, and there's no direct way to reposition existing columns.

## Solution

`pgcolpos` solves this by:

1. Analyzing the existing table structure, including columns, constraints, indexes, and permissions
2. Creating a new table with the desired column order
3. Migrating all data
4. Recreating all constraints, indexes, and permissions

## Installation

```bash
pip install pgcolpos
```

## Usage

### Adding a New Column After a Specific Position

```bash
pgcolpos add users email varchar(255) after username --db="postgresql://user:pass@localhost/mydb"
```

### Moving an Existing Column After a Specific Position

```bash
pgcolpos move products description after name --db="postgresql://user:pass@localhost/mydb"
```

### Help

```bash
pgcolpos --help
```

## API Usage

The tool can also be used programmatically in your Python code:

```python
from pgcolpos import add_column, move_column
import psycopg2

# Establish connection
conn = psycopg2.connect("postgresql://user:pass@localhost/mydb")

# Add a column
add_column(conn, "users", "email", "varchar(255)", "username")

# Move a column
move_column(conn, "products", "description", "name")

# Close connection
conn.close()
```

## Integration with Other Languages/Frameworks

### Node.js

```javascript
const { exec } = require('child_process');

function addColumnAfter(table, newColumn, dataType, afterColumn, connectionString) {
  return new Promise((resolve, reject) => {
    exec(`pgcolpos add ${table} ${newColumn} "${dataType}" after ${afterColumn} --db="${connectionString}"`, 
      (error, stdout, stderr) => {
        if (error) {
          reject(error);
          return;
        }
        resolve(stdout);
      });
  });
}

// Usage
addColumnAfter('users', 'email', 'varchar(255)', 'username', 'postgresql://user:pass@localhost/mydb')
  .then(console.log)
  .catch(console.error);
```

### PHP

```php
<?php
function addColumnAfter($table, $newColumn, $dataType, $afterColumn, $connectionString) {
    $command = "pgcolpos add {$table} {$newColumn} \"{$dataType}\" after {$afterColumn} --db=\"{$connectionString}\"";
    $output = shell_exec($command);
    return $output;
}

// Usage
$result = addColumnAfter('users', 'email', 'varchar(255)', 'username', 'postgresql://user:pass@localhost/mydb');
echo $result;
?>
```

### Java

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class PostgresColumnTool {
    public static String addColumnAfter(String table, String newColumn, String dataType, 
                                     String afterColumn, String connectionString) throws Exception {
        ProcessBuilder processBuilder = new ProcessBuilder(
            "pgcolpos", "add", table, newColumn, dataType, "after", afterColumn, 
            "--db=" + connectionString);
        
        Process process = processBuilder.start();
        
        BufferedReader reader = 
            new BufferedReader(new InputStreamReader(process.getInputStream()));
        
        StringBuilder output = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            output.append(line).append("\n");
        }
        
        int exitCode = process.waitFor();
        if (exitCode != 0) {
            throw new Exception("Command failed with exit code: " + exitCode);
        }
        
        return output.toString();
    }
    
    // Usage
    public static void main(String[] args) {
        try {
            String result = addColumnAfter("users", "email", "varchar(255)", "username", 
                                        "postgresql://user:pass@localhost/mydb");
            System.out.println(result);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### Ruby on Rails

In a migration file:

```ruby
def change
  # Using the command-line tool from a Rails migration
  connection_string = "postgresql://#{ENV['DB_USER']}:#{ENV['DB_PASS']}@#{ENV['DB_HOST']}/#{ENV['DB_NAME']}"
  
  # Add column after specific position
  system("pgcolpos add users email varchar(255) after username --db=\"#{connection_string}\"")
end
```

## Warning

This tool recreates your table, which might take some time for large tables. It's recommended to:

1. Run this during low-traffic periods
2. Take a backup before using the tool
3. Test in a development environment first

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.