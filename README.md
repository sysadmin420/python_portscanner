# python_portscanner
A lightweight network port scanner written in Python for TCP and UDP port scanning.

The scanner supports IPv4 and IPv6, configurable thread counts, common service detection, and basic HTTP/HTTPS server identification through HTTP response headers.

# Features:
- TCP port scanning
- UDP port scanning
- IPv4 support
- IPv6 support
- Configurable number of threads
- portbased common service detection
- HTTP/HTTPS service & version detection
- HTTP Server header detection --> prove service/ server & detect version
- Support for common network, database, remote-access, VPN, proxy, and other services

Requirements:
Python 3
requests

Install the required Python package with:

pip install requests

# Usage
IPv4 - Scan an IPv4 target:
python3 portscanner.py --ipv4 192.168.1.10


IPv6 - Scan an IPv6 target:
python3 portscanner.py --ipv6 2001:db8::1

Custom thread count:
The default number of threads is 100.
Change the number of threads with -t or --threads:
python3 portscanner.py --ipv4 192.168.1.10 --threads 50
or:
python3 portscanner.py --ipv4 192.168.1.10 -t 50

Example output
scanning 192.168.1.10...
port 22/TCP: open - ssh unknown
port 80/TCP: open - http nginx/1.24.0
port 443/TCP: open - https nginx/1.24.0
port 53/UDP: open - dns

Service Detection

The scanner contains a database of commonly used ports and their associated services.

For example:

22    → ssh
53    → dns
80    → http
443   → https
3306  → mysql
5432  → postgresql
3389  → rdp

These mappings represent commonly associated services and do not guarantee that a particular service is actually running on a port.

For HTTP/HTTPS services, the scanner additionally attempts to retrieve the HTTP Server response header to identify the server software and version when available.

Version 1.2
New features:
- HTTP/HTTPS header-based service and version detection
- Configurable thread count
- Expanded common-service database
- IPv6 support
- HTTPS support

Project Structure
python_portscanner/
├── portscanner.py
├── http_header.py
└── services.py


portscanner.py

Main scanner implementation including:

TCP scanning
UDP scanning
IPv4/IPv6 socket handling
Multithreading
Command-line argument parsing

http_header.py

Handles HTTP/HTTPS requests and extracts the Server response header for basic server/version identification.

services.py

Contains the database of commonly associated network services and ports.

Disclaimer

Only scan systems and networks that you own or have explicit permission to test.
