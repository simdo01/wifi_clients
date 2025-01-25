# Monitoring Guide

## Starting the Monitor

Run with appropriate privileges:

```bash
# Linux/Mac
sudo python wifi_monitor.py

# Windows (as Administrator)
python wifi_monitor.py
```

## Understanding Output

### Console Output
```
2024-01-01 12:00:00 | INFO     | Starting WiFi Monitor
2024-01-01 12:00:01 | DEBUG    | Found device: 00:11:22:33:44:55 (192.168.1.100)
```

### Log File
Located at `wifi_monitor.log`:
```
2024-01-01 12:00:00 - WifiMonitor - INFO - WiFi Monitor initialized
2024-01-01 12:00:01 - WifiMonitor - DEBUG - Starting network scan
```

## Notifications

### New Devices
```
New WiFi client detected!
IP: 192.168.1.100
MAC: 00:11:22:33:44:55
Vendor: Samsung Electronics
```

### Hourly Summaries
```
Hourly Summary: Found 12 active devices. 
Total devices in database: 25
```

## Troubleshooting

Common issues and solutions:
1. Permission denied
   - Run with sudo/administrator
2. Nmap errors
   - Verify Nmap installation
3. Database errors
   - Check write permissions