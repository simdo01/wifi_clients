# Network Configuration

## Nmap Settings

The network scanning configuration controls how the WiFi Monitor searches for devices.

### Network Range

```ini
[nmap]
network = 192.168.1.1/24
```

- Use CIDR notation
- Common home networks:
  - 192.168.1.1/24
  - 192.168.0.1/24
  - 10.0.0.1/24

### Scan Interval

```ini
[nmap]
scan_interval = 300
```

- Value in seconds
- Recommended: 300-600 seconds
- Lower values increase network load

## Scan Types

The monitor uses Nmap's host discovery:
- Non-intrusive scanning (-sn flag)
- No port scanning
- MAC address detection
- Vendor identification

## Security Considerations

- Scan only networks you own/manage
- Consider bandwidth impact
- Respect privacy guidelines 