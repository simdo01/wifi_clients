# Installation Guide

## Prerequisites

- Python 3.6+
- Nmap
- Root/Administrator privileges
- Pushover account

## Step-by-Step Installation

1. Clone the Repository
   ```bash
   git clone https://github.com/simdo01/wifi-monitor.git
   cd wifi-monitor
   ```

2. Create Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Install Nmap
   - Linux: `sudo apt-get install nmap`
   - Mac: `brew install nmap`
   - Windows: Download from [nmap.org](https://nmap.org/)

## Configuration

1. Copy example config:
   ```bash
   cp config.ini.example config.ini
   ```

2. Edit configuration:
   ```ini
   [nmap]
   network = 192.168.1.1/24
   scan_interval = 300

   [pushover]
   user_key = YOUR_KEY
   api_token = YOUR_TOKEN
   ```

## Verify Installation

Run the test command:
```bash
python -m pytest tests/
``` 