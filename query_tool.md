# Running the DB Query Tool
## Features

### Data Display
- Shows all recorded devices in a grid format
- Includes all device information:
  - MAC Address
  - IP Address
  - Vendor
  - First Seen timestamp
  - Last Seen timestamp
  - Description (if set)
- Sorted by most recently seen devices first
1. Ensure virtual environment is activated:
   ```bash
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

2. Run the query tool:
   ```bash
   python query_clients.py
   ```

## Output Format
The tool displays data in a grid format:
```
+-------------------+---------------+----------+---------------------+---------------------+-------------+
| MAC Address | IP Address | Vendor | First Seen | Last Seen | Description |
+===================+===============+==========+=====================+=====================+=============+
| 00:11:22:33:44:55 | 192.168.1.100 | Samsung | 2024-01-01 12:00:00| 2024-01-01 13:00:00| Johns Phone |
+-------------------+---------------+----------+---------------------+---------------------+-------------+
```

### Section 4 (Managing Descriptions and Limitations):

#### Managing Device Descriptions
To add or update device descriptions, use SQLite directly:

sqlite3 wifi_clients.db

Then run SQL commands:

-- Add/Update description
UPDATE clients 
SET description = 'Living Room TV' 
WHERE mac_address = '00:11:22:33:44:55';

-- Remove description
UPDATE clients 
SET description = NULL 
WHERE mac_address = '00:11:22:33:44:55';

Limitations
Read-only interface
No filtering or search capabilities
Cannot modify data through the tool
Requires direct database access for modifications
