# Query Tool Usage

## Overview
The Query Tool provides a command-line interface to view and manage devices stored in the WiFi Monitor database.

## Basic Usage

View all devices:
```bash
python query_clients.py
```

Output format:
```
+-------------------+---------------+----------+---------------------+---------------------+-------------+
| MAC Address       | IP Address    | Vendor   | First Seen         | Last Seen          | Description |
+===================+===============+==========+=====================+=====================+=============+
| 00:11:22:33:44:55 | 192.168.1.100 | Samsung  | 2024-01-01 12:00:00| 2024-01-01 13:00:00| Johns Phone |
| AA:BB:CC:DD:EE:FF | 192.168.1.101 | Apple    | 2024-01-01 12:30:00| 2024-01-01 13:30:00| Living Room |
+-------------------+---------------+----------+---------------------+---------------------+-------------+
```

## Managing Device Descriptions

### Add Description
```sql
sqlite3 wifi_clients.db
UPDATE clients 
SET description = 'Living Room TV' 
WHERE mac_address = '00:11:22:33:44:55';
```

### Remove Description
```sql
sqlite3 wifi_clients.db
UPDATE clients 
SET description = NULL 
WHERE mac_address = '00:11:22:33:44:55';
```

## Database Fields

- **MAC Address**: Unique device identifier
- **IP Address**: Last known IP address
- **Vendor**: Manufacturer name if available
- **First Seen**: Initial detection timestamp
- **Last Seen**: Most recent detection
- **Description**: Optional user-added note

## Tips

### Sorting
- Results are sorted by Last Seen time
- Most recently seen devices appear first
- Helps identify active vs inactive devices

### Descriptions
- Use meaningful descriptions
- Include device location
- Note device owner if relevant
- Update when device changes

### Best Practices
- Regular database review
- Update outdated descriptions
- Document unknown devices
- Monitor for unexpected entries 