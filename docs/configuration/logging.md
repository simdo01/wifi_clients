# Logging Configuration

## Overview
The WiFi Monitor implements two types of logging:
- File logging with rotation
- Optional colorized console output using loguru

## Configuration Settings

In `config.ini`:
```ini
[logging]
log_file = wifi_monitor.log  # Log file location
max_size_mb = 10            # Maximum log file size in MB
backup_count = 5            # Number of backup log files to keep
log_level = INFO            # Logging level (DEBUG, INFO, WARNING, ERROR)
console_logging = true      # Enable/disable console output
```

## Log Levels

- **DEBUG**: Detailed information for troubleshooting
  - Device discovery details
  - Database operations
  - Network scanning events

- **INFO**: General operational messages
  - Monitor startup/shutdown
  - New device detection
  - Hourly summaries

- **WARNING**: Issues that need attention
  - Configuration problems
  - Network scan delays
  - Database warnings

- **ERROR**: Serious problems
  - Scan failures
  - Database errors
  - Notification failures

## File Logging

### Rotation
- Logs rotate at specified size (default 10MB)
- Keeps specified number of backups (default 5)
- Naming: wifi_monitor.log, wifi_monitor.log.1, etc.
- Sends notification on rotation

### Format
```
2024-01-01 12:00:00 - WifiMonitor - INFO - WiFi Monitor initialized
2024-01-01 12:00:01 - WifiMonitor - DEBUG - Starting network scan
```

## Console Logging

### Colorized Output
```
12:00:00 | INFO     | Starting WiFi Monitor
12:00:01 | DEBUG    | Found device: 00:11:22:33:44:55
```

### Features
- Color-coded by log level
- Includes timestamp
- Shows function and line number
- Can be disabled in config

## Log Management

### Best Practices
- Regular log review
- Monitor disk usage
- Archive old logs
- Secure log files

### Troubleshooting
- Increase to DEBUG level for issues
- Check file permissions
- Verify rotation settings
- Monitor log growth 