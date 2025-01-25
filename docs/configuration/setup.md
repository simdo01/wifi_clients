# Basic Setup

## Configuration File

The `config.ini` file contains all configuration settings for the WiFi Monitor. Here's a complete overview of all available options:

```ini
[nmap]
network = 192.168.1.1/24    # Network range to scan
scan_interval = 300         # Scan frequency in seconds

[database]
db_file = wifi_clients.db   # SQLite database filename

[pushover]
user_key = YOUR_USER_KEY    # Pushover user key
api_token = YOUR_API_TOKEN  # Pushover application token

[logging]
log_file = wifi_monitor.log # Log file location
max_size_mb = 10           # Maximum log file size in MB
backup_count = 5           # Number of backup log files to keep
log_level = INFO           # Logging level (DEBUG, INFO, WARNING, ERROR)
console_logging = true     # Enable/disable console output
```

## Initial Setup Steps

1. Create Configuration File
   ```bash
   cp config.ini.example config.ini
   ```

2. Configure Network Settings
   - Set your network range
   - Adjust scan interval if needed

3. Setup Pushover Integration
   - Create Pushover account
   - Generate application token
   - Add credentials to config

4. Configure Logging
   - Set desired log level
   - Adjust file rotation settings
   - Enable/disable console output

## Configuration Validation

The WiFi Monitor validates your configuration on startup:
- Checks for required settings
- Validates network range format
- Verifies Pushover credentials
- Ensures write permissions for logs and database

## Environment Variables

You can override config.ini settings using environment variables:
```bash
export WIFI_MONITOR_NETWORK=192.168.0.1/24
export WIFI_MONITOR_PUSHOVER_KEY=your_key
export WIFI_MONITOR_PUSHOVER_TOKEN=your_token
```

## Advanced Configuration

### Custom Log Formats
- File logging uses standard format
- Console logging uses colorized output
- Both configurable in code

### Database Location
- Default: current directory
- Can be absolute path
- Ensure write permissions 