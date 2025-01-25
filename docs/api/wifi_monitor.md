# WiFi Monitor API Reference

## WifiMonitor Class

Main class that handles network scanning, database operations, and notifications.

### Methods

#### `__init__(self)`
```python
"""Initialize WiFi monitor with config, logging, database, and Nmap scanner."""
```
- Loads configuration
- Sets up logging
- Initializes database
- Creates Nmap scanner instance

#### `load_config(self)`
```python
"""Load configuration from config.ini file."""
```
- Reads and parses config.ini
- Returns ConfigParser object

#### `setup_logging(self)`
```python
"""Configure file logging with rotation and console logging with loguru."""
```
- Configures file logging with rotation
- Sets up optional console logging
- Handles log rotation notifications

#### `setup_database(self)`
```python
"""Initialize SQLite database with clients table if it doesn't exist."""
```
- Creates database if not exists
- Sets up clients table schema
- Handles database connections

#### `scan_network(self)`
```python
"""Scan network for devices using Nmap and return list of found clients."""
```
- Performs Nmap network scan
- Collects device information
- Returns list of found devices

#### `update_database(self, clients)`
```python
"""Update database with scanned clients, return list of new devices."""
```
- Updates existing device records
- Adds new devices
- Returns list of newly discovered devices

#### `get_total_devices(self)`
```python
"""Return total count of devices in database."""
```
- Queries database for total device count

#### `send_pushover_notification(self, data)`
```python
"""Send notification via Pushover API for new devices, summaries, or log rotations."""
```
- Handles different notification types
- Sends data to Pushover API
- Manages notification errors

#### `should_send_summary(self)`
```python
"""Check if hourly summary notification should be sent."""
```
- Tracks notification timing
- Returns True if summary is due

#### `run(self)`
```python
"""Main loop: scan network, update database, and send notifications."""
```
- Continuous monitoring loop
- Handles scanning and notifications
- Manages error recovery

### Database Schema

```sql
CREATE TABLE clients (
    mac_address TEXT PRIMARY KEY,
    ip_address TEXT,
    vendor TEXT,
    first_seen TIMESTAMP,
    last_seen TIMESTAMP,
    description TEXT
)
```

### Error Handling

The class implements specific error handling for:
- Network scanning errors
- Database operations
- API communication
- Configuration issues

### Usage Example

```python
monitor = WifiMonitor()
monitor.run()
``` 