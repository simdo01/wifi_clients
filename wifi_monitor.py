#!/usr/bin/env python3
import configparser
import http.client
import logging
from logging.handlers import RotatingFileHandler
import sqlite3
import sys
import time
import urllib.parse
from datetime import datetime
from loguru import logger
import nmap

class WifiMonitor:
    """Monitor WiFi network for devices using Nmap, store data in SQLite, and send Pushover notifications."""
    def __init__(self):
        """Initialize WiFi monitor with config, logging, database, and Nmap scanner."""
        self.config = self.load_config()
        self.setup_logging()
        self.setup_database()
        self.nm = nmap.PortScanner()
        self.last_summary_time = None
        self.logger.info("WiFi Monitor initialized")
        logger.info("WiFi Monitor initialized")

    def load_config(self):
        """Load configuration from config.ini file."""
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config

    def setup_logging(self):
        """Configure file logging with rotation and console logging with loguru."""
        log_file = self.config['logging']['log_file']
        max_bytes = int(self.config['logging']['max_size_mb']) * 1024 * 1024
        backup_count = int(self.config['logging']['backup_count'])
        log_level = getattr(logging, self.config['logging']['log_level'].upper())
        console_logging = self.config['logging'].getboolean('console_logging', True)  # Default to True if not specified

        # Setup file logging as before
        self.logger = logging.getLogger('WifiMonitor')
        self.logger.setLevel(log_level)

        # Create formatter for file logging
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Create custom RotatingFileHandler that sends notification on rollover
        class NotifyRotatingFileHandler(RotatingFileHandler):
            """Rotating file handler that sends a notification when log files are rotated."""
            def __init__(self, monitor_instance, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.monitor = monitor_instance

            def doRollover(self):
                super().doRollover()
                # Send notification about log rotation
                self.monitor.send_pushover_notification({
                    'log_rotation': True,
                    'message': f"Log file rotated. Previous log archived to {self.baseFilename}.1"
                })

        # Create and add file handler
        file_handler = NotifyRotatingFileHandler(
            self,
            filename=log_file,
            maxBytes=max_bytes,
            backupCount=backup_count
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Setup loguru for console logging if enabled
        logger.remove()  # Remove default handler
        if console_logging:
            logger.add(
                sys.stderr,
                format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
                level=log_level,
                colorize=True
            )

    def setup_database(self):
        """Initialize SQLite database with clients table if it doesn't exist."""
        self.logger.info("Setting up database")
        conn = sqlite3.connect(self.config['database']['db_file'])
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                mac_address TEXT PRIMARY KEY,
                ip_address TEXT,
                vendor TEXT,
                first_seen TIMESTAMP,
                last_seen TIMESTAMP,
                description TEXT
            )
        ''')
        conn.commit()
        conn.close()
        self.logger.debug("Database setup complete")

    def scan_network(self):
        """Scan network for devices using Nmap and return list of found clients."""
        logger.debug("Starting network scan")
        self.logger.debug("Starting network scan")
        network = self.config['nmap']['network']
        self.nm.scan(hosts=network, arguments='-sn')
        
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Format timestamp as string
        clients = []
        
        for host in self.nm.all_hosts():
            if 'mac' in self.nm[host]['addresses']:
                client = {
                    'ip_address': host,
                    'mac_address': self.nm[host]['addresses']['mac'],
                    'vendor': self.nm[host]['vendor'].get(self.nm[host]['addresses']['mac'], 'Unknown'),
                    'timestamp': current_time
                }
                clients.append(client)
                logger.debug("Found device: {} ({})", client['mac_address'], client['ip_address'])
                self.logger.debug("Found device: %s (%s)", client['mac_address'], client['ip_address'])
        
        logger.info("Scan complete. Found {} devices", len(clients))
        self.logger.info("Scan complete. Found %d devices", len(clients))
        return clients

    def update_database(self, clients):
        """Update database with scanned clients, return list of new devices."""
        logger.debug("Updating database with scan results")
        self.logger.debug("Updating database with scan results")
        self.logger.debug("Updating database with scan results")
        conn = sqlite3.connect(self.config['database']['db_file'])
        cursor = conn.cursor()
        new_clients = []

        for client in clients:
            cursor.execute('SELECT mac_address FROM clients WHERE mac_address = ?', 
            (client['mac_address'],))
            
            if cursor.fetchone() is None:
                self.logger.info("New client found: %s (%s)", client['mac_address'], client['ip_address'])
                cursor.execute('''
                    INSERT INTO clients (mac_address, ip_address, vendor, first_seen, last_seen, description)
                    VALUES (?, ?, ?, datetime(?), datetime(?), ?)
                ''', (client['mac_address'], client['ip_address'], client['vendor'],
                client['timestamp'], client['timestamp'], None))
                new_clients.append(client)
            else:
                cursor.execute('''
                    UPDATE clients 
                    SET ip_address = ?, last_seen = ?
                    WHERE mac_address = ?
                ''', (client['ip_address'], client['timestamp'], client['mac_address']))

        conn.commit()
        conn.close()
        return new_clients

    def get_total_devices(self):
        """Return total count of devices in database."""
        conn = sqlite3.connect(self.config['database']['db_file'])
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM clients')
        total = cursor.fetchone()[0]
        conn.close()
        return total

    def send_pushover_notification(self, data):
        """Send notification via Pushover API for new devices, summaries, or log rotations."""
        logger.debug("Sending Pushover notification")
        self.logger.debug("Sending Pushover notification")
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        
        if 'log_rotation' in data:
            message = data['message']
        elif 'summary' in data:
            message = data['message']
        else:
            message = (f"New WiFi client detected!\n"
            f"IP: {data['ip_address']}\n"
            f"MAC: {data['mac_address']}\n"
            f"Vendor: {data['vendor']}")

        try:
            conn.request("POST", "/1/messages.json",
                urllib.parse.urlencode({
                    "token": self.config['pushover']['api_token'],
                    "user": self.config['pushover']['user_key'],
                    "message": message,
                }), { "Content-type": "application/x-www-form-urlencoded" })
            
            response = conn.getresponse()
            if response.status == 200:
                self.logger.debug("Pushover notification sent successfully")
            else:
                self.logger.error("Failed to send Pushover notification: %s %s", response.status, response.reason)
        except (http.client.HTTPException, ConnectionError) as e:
            self.logger.error("Pushover notification error: %s", str(e))

    def should_send_summary(self):
        """Check if hourly summary notification should be sent."""
        if self.last_summary_time is None:
            return True
        
        current_time = datetime.now()
        time_difference = current_time - self.last_summary_time
        # Return True if more than 1 hour has passed
        return time_difference.total_seconds() >= 3600

    def run(self):
        """Main loop: scan network, update database, and send notifications."""
        logger.info("Starting WiFi Monitor")
        self.logger.info("Starting WiFi Monitor")
        while True:
            try:
                clients = self.scan_network()
                new_clients = self.update_database(clients)
                
                # Send notifications for new clients
                for client in new_clients:
                    self.send_pushover_notification(client)
                
                # Send summary notification once per hour
                if self.should_send_summary():
                    total_devices = self.get_total_devices()
                    self.send_pushover_notification({
                        'summary': True,
                        'message': f"Hourly Summary: Found {len(clients)} active devices. "
                        f"Total devices in database: {total_devices}"
                    })
                    self.last_summary_time = datetime.now()
                
                scan_interval = int(self.config['nmap']['scan_interval'])
                self.logger.debug("Sleeping for %d seconds", scan_interval)
                time.sleep(scan_interval)
                
            except (nmap.PortScannerError, sqlite3.Error, http.client.HTTPException, ConnectionError) as e:
                self.logger.error("Error occurred: %s", str(e))
                time.sleep(60)  # Wait a minute before retrying

if __name__ == "__main__":
    monitor = WifiMonitor()
    monitor.run() 