# WiFi Network Monitor

Welcome to the WiFi Network Monitor documentation. This tool helps you monitor your network for connected devices using Nmap, with SQLite storage and Pushover notifications.

## Overview

The WiFi Monitor provides:
- Real-time device detection
- Historical device tracking
- Push notifications for new devices
- Hourly network summaries
- Configurable logging

## Quick Start

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure settings in `config.ini`

3. Run the monitor:
   ```bash
   sudo python wifi_monitor.py
   ```

## Project Structure

```
wifi-monitor/
├── wifi_monitor.py     # Main monitoring script
├── query_clients.py    # Database query utility
├── config.ini         # Configuration file
├── requirements.txt   # Python dependencies
└── docs/             # Documentation
``` 