# Device Management

## Overview
The WiFi Monitor tracks devices by their MAC addresses and maintains a history of their network presence.

## Device Information

### Stored Data
- MAC Address (Primary Identifier)
- IP Address (Current/Last Known)
- Vendor Name
- First Seen Timestamp
- Last Seen Timestamp
- Custom Description

## Managing Devices

### Adding Descriptions
Use SQLite to add or update device descriptions:
```sql
sqlite3 wifi_clients.db
UPDATE clients 
SET description = 'Living Room Smart TV' 
WHERE mac_address = '00:11:22:33:44:55';
```

### Device Categories
Common device types to note in descriptions:
- Network Infrastructure (Routers, Access Points)
- Personal Devices (Phones, Laptops)
- IoT Devices (Smart Home)
- Guest Devices

## Best Practices

### Naming Conventions
- Use consistent naming patterns
- Include device type
- Note location if relevant
- Add owner information when appropriate

Example descriptions:
```
"Living Room - Samsung TV"
"Johns iPhone 13"
"Guest Laptop - Alice"
"IoT - Nest Thermostat"
```

### Device Management
- Regular inventory review
- Update descriptions promptly
- Document unknown devices
- Track guest devices
- Note temporary devices

## Security Tips

### Device Monitoring
- Review new device notifications
- Investigate unknown devices
- Track last seen timestamps
- Monitor connection patterns

### Documentation
- Keep device inventory updated
- Note authorized vs guest devices
- Document MAC address changes
- Track device replacements 