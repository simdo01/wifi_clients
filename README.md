# WiFi Network Monitor

A Python-based tool that monitors your network for connected devices using Nmap. It tracks device history in SQLite and sends notifications via Pushover when new devices are detected.

## Features

- Continuous network monitoring using Nmap
- Device tracking with MAC address, IP, and vendor information
- SQLite database storage for device history
- Pushover notifications for:
  - New device detection
  - Hourly network summaries
  - Log rotation events
- Configurable logging with file rotation
- Optional colorized console output using loguru
- Query tool for viewing device history

## Requirements

- Python 3.6+
- Nmap installed on system
- Root/Administrator privileges (for Nmap scanning)
- Pushover account and API credentials

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/wifi-monitor.git
   cd wifi-monitor
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Documentation

The project documentation is built using MkDocs. To view the documentation:

1. Install documentation dependencies:
   ```bash
   pip install mkdocs-material mkdocstrings[python] mkdocs-autorefs
   ```

2. View documentation locally:
   ```bash
   mkdocs serve
   ```
   Then open http://127.0.0.1:8000 in your browser

3. Build static documentation:
   ```bash
   mkdocs build
   ```
   The built documentation will be in the `site` directory

## Configuration

Edit `config.ini` with your settings:

```ini
[nmap]
network = 192.168.1.1/24    # Your network range
scan_interval = 300         # Scan frequency in seconds

[pushover]
user_key = YOUR_USER_KEY
api_token = YOUR_API_TOKEN

[logging]
log_file = wifi_monitor.log
max_size_mb = 10
backup_count = 5
log_level = INFO
console_logging = true      # Enable/disable console output
```

## Usage

### Start Monitoring

Run with root/administrator privileges:
```bash
sudo python wifi_monitor.py  # Linux/Mac
# or
python wifi_monitor.py      # Windows (as Administrator)
```

### Query Device History

View all known devices:
```bash
python query_clients.py
```

### Update Device Descriptions

Use SQLite to add descriptions:
```bash
sqlite3 wifi_clients.db
```
```sql
UPDATE clients 
SET description = 'Living Room TV' 
WHERE mac_address = '00:11:22:33:44:55';
```

## Notifications

The program sends Pushover notifications for:
- New devices detected on network
- Hourly summaries of active and total devices
- Log file rotation events

## Security Considerations

- Requires root/administrator privileges
- Stores network device information
- Secure your config.ini (contains API credentials)
- Configure network range appropriately

## Limitations

- Requires Nmap installation
- May miss offline devices
- Network range must be accessible
- Some devices may not respond to Nmap scans

## License

[Your chosen license]

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- Your Name 