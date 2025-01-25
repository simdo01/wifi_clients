# Query Client API Reference

## Functions

### `load_config()`
```python
"""Load configuration from config.ini file."""
```
- Reads database configuration
- Returns ConfigParser object
- Used to locate database file

### `query_clients()`
```python
"""Query and display all clients from the database."""
```
- Connects to SQLite database
- Retrieves all client records
- Formats output using tabulate
- Displays results in grid format

## Database Query

The main SQL query used:
```sql
SELECT mac_address, ip_address, vendor, first_seen, last_seen, description
FROM clients
ORDER BY last_seen DESC
```

## Output Format

### Headers
- MAC Address
- IP Address
- Vendor
- First Seen
- Last Seen
- Description

### Example Output
```
+-------------------+---------------+----------+---------------------+---------------------+-------------+
| MAC Address       | IP Address    | Vendor   | First Seen         | Last Seen          | Description |
+===================+===============+==========+=====================+=====================+=============+
| 00:11:22:33:44:55 | 192.168.1.100 | Samsung  | 2024-01-01 12:00:00| 2024-01-01 13:00:00| Johns Phone |
+-------------------+---------------+----------+---------------------+---------------------+-------------+
```

## Dependencies

- configparser: Configuration file parsing
- sqlite3: Database operations
- tabulate: Output formatting

## Usage Example

```python
if __name__ == "__main__":
    query_clients()
```

## Error Handling

The script handles:
- Database connection errors
- Configuration file errors
- Data formatting issues

## Integration

Can be:
- Run as standalone script
- Imported as module
- Used in other scripts 