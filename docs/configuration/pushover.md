# Pushover Integration

## Overview
The WiFi Monitor uses Pushover to send notifications for:
- New device detection
- Hourly network summaries
- Log rotation events

## Setup Pushover

1. Create Account
   - Sign up at [Pushover.net](https://pushover.net)
   - Note your user key

2. Create Application
   - Log into Pushover
   - Create a new application
   - Save the application token

## Configuration

Add your Pushover credentials to `config.ini`:
```ini
[pushover]
user_key = YOUR_USER_KEY    # From your Pushover account
api_token = YOUR_API_TOKEN  # From your created application
```

## Notification Types

### New Device Detection
```
New WiFi client detected!
IP: 192.168.1.100
MAC: 00:11:22:33:44:55
Vendor: Samsung Electronics
```

### Hourly Summary
```
Hourly Summary: Found 12 active devices. 
Total devices in database: 25
```

### Log Rotation
```
Log file rotated. Previous log archived to wifi_monitor.log.1
```

## Security Considerations
- Keep credentials secure
- Never commit real credentials
- Use environment variables in production
- Regularly verify notification delivery 