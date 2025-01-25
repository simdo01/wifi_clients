#!/usr/bin/env python3
import sqlite3
import configparser
from tabulate import tabulate

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def query_clients():
    config = load_config()
    conn = sqlite3.connect(config['database']['db_file'])
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT mac_address, ip_address, vendor, first_seen, last_seen, description
        FROM clients
        ORDER BY last_seen DESC
    ''')
    
    clients = cursor.fetchall()
    headers = ['MAC Address', 'IP Address', 'Vendor', 'First Seen', 'Last Seen', 'Description']
    
    print(tabulate(clients, headers=headers, tablefmt='grid'))
    
    conn.close()

if __name__ == "__main__":
    query_clients() 