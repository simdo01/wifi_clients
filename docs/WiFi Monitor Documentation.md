# WiFi Monitor Documentation

## Overview
The WiFi Monitor is a Python-based tool that continuously monitors your network for connected devices using Nmap. It stores device information in a SQLite database and sends notifications via Pushover when new devices are detected.

## Requirements
- Python 3.6+
- Nmap installed on the system
- Root/Administrator privileges (for Nmap scanning)
- Pushover account and API credentials
- Required Python packages (install via `pip install -r requirements.txt`):
  - python-nmap
  - tabulate

  ## Configuration
The program uses `config.ini` for all configuration settings:

### Nmap Settings
ni
[nmap]
network = 192.168.1.1/24 # Network range to scan in CIDR notation
scan_interval = 300 # Scan frequency in seconds


### Database Settings
ini
[database]
db_file = wifi_clients.db # SQLite database filename

ini
[database]
db_file = wifi_clients.db # SQLite database filename

### Pushover Settings
ini
[pushover]
user_key = YOUR_USER_KEY # Pushover user key
api_token = YOUR_API_TOKEN # Pushover application token

### Logging Settings
ini
[logging]
log_file = wifi_monitor.log # Name of the log file
max_size_mb = 10 # Maximum size of log file before rotation (in MB)
backup_count = 5 # Number of backup log files to keep
log_level = INFO # Logging level (DEBUG, INFO, WARNING,

## Logging System

### Log Levels
- DEBUG: Detailed information for debugging purposes
  - Network scan starts/completions
  - Individual device discoveries
  - Database operations
  - Sleep/wake cycles
- INFO: General operational information
  - Program initialization
  - New device discoveries
  - Scan summaries
- ERROR: Error conditions
  - Scan failures
  - Database errors
  - Pushover notification failures

### Log Format
Each log entry includes:
- Timestamp
- Logger name (WifiMonitor)
- Log level
- Message content

Example:
2024-01-01 12:00:00 - WifiMonitor - INFO - WiFi Monitor initialized
2024-01-01 12:00:00 - WifiMonitor - DEBUG - Starting network scan
2024-01-01 12:00:01 - WifiMonitor - INFO - Scan complete. Found 5 devices


### Log Rotation
- Logs automatically rotate when they reach the configured size (default 10MB)
- Maintains specified number of backup files (default 5)
- Naming convention: wifi_monitor.log, wifi_monitor.log.1, wifi_monitor.log.2, etc.
- Sends Pushover notification when rotation occurs
- Rotation notification includes path to archived log file

### Output Destinations
- File: All logs written to configured log file
- Console: Real-time output to console/terminal
- Pushover: Notifications for new devices and log rotations

## Notifications
The program sends three types of Pushover notifications:

1. New Device Detection:
New WiFi client detected!
IP: 192.168.1.100
MAC: 00:11:22:33:44:55
Vendor: Samsung Electronics

2. Hourly Summary (sent once per hour):
Hourly Summary: Found 12 active devices. Total devices in database: 25


3. Log Rotation:
Log file rotated. Previous log archived to wifi_monitor.log.1

Section 5 (Database Schema):

Database Schema
The SQLite database (wifi_clients.db) contains a single table with the following structure:
| Column | Type | Description |
|-------------|-----------|--------------------------------|
| mac_address | TEXT | Primary key, device MAC address|
| ip_address | TEXT | Device IP address |
| vendor | TEXT | Device manufacturer |
| first_seen | TIMESTAMP | First detection time |
| last_seen | TIMESTAMP | Most recent detection time |
| description | TEXT | Optional user description |

Section 6 (Running and Limitations):

Running the Program
1. Setup:

   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt

  2. Configure:
Edit config.ini with your network and Pushover credentials
Ensure database path is writable
Configure logging settings as needed
3. Run:
   sudo python wifi_monitor.py  # Linux/Mac
   # or
   python wifi_monitor.py  # Windows (as Administrator)

   Security Considerations
Requires root/administrator privileges
Stores sensitive network information
Secure your config.ini file (contains Pushover credentials)
Consider network range carefully to avoid scanning unauthorized networks
Limitations
Requires Nmap installation
May miss devices that are offline during scan
Network range must be accessible to scanning host
Some devices may not respond to Nmap scans

