# Personal Firewall Using Python and Scapy

## Project Overview

This project implements a Personal Firewall using Python and Scapy on Kali Linux. The firewall monitors network traffic in real time, applies packet filtering rules, blocks suspicious IP addresses and ports, and maintains logs for security analysis.

## Objectives

* Monitor incoming and outgoing network traffic
* Analyze packet information
* Block unwanted IP addresses
* Block insecure ports
* Generate security logs
* Understand firewall concepts and packet filtering

## Technologies Used

* Python 3.13
* Scapy
* Kali Linux
* VirtualBox
* iptables

## Features

* Real-time packet monitoring
* IP address filtering
* Port filtering
* Event logging
* Traffic analysis

## Project Structure

```text
PersonalFirewall/
│
├── firewall.py
├── logs.txt
├── README.md
├── report.pdf
└── screenshots/
```

## Installation

### Update System

```bash
sudo apt update
sudo apt upgrade -y
```

### Verify Python

```bash
python3 --version
```

### Verify Scapy

```bash
python3
```

```python
from scapy.all import *
```

## Running the Firewall

```bash
sudo python3 firewall.py
```

Expected Output:

```text
FIREWALL ACTIVE
```

## Testing

Open a second terminal:

```bash
ping google.com
```

The firewall will display detected traffic and log network events.

## Sample Output

```text
FIREWALL ACTIVE

ALLOWED 192.168.1.10 -> 142.250.183.14

BLOCKED PORT 23
```

## Log File

Logs are stored in:

```text
logs.txt
```

View logs using:

```bash
cat logs.txt
```

## Screenshots

### Firewall Running

firewall_running.png

### Traffic Monitoring

packet_monitoring.png

### Logs

logs.png

### iptables Rules

iptables.png


* Network Monitoring
* Packet Analysis
* Security Research
* Cybersecurity Education
* Firewall Demonstration

## Future Enhancements

* GUI Dashboard
* Intrusion Detection System Integration
* Machine Learning-Based Anomaly Detection
* Email Alerts
* Real-Time Visualization

## Skills Learned

* Python Programming
* Network Security
* Packet Analysis
* Firewall Configuration
* Traffic Monitoring
* Cybersecurity Fundamentals

## Author

Madhu

Cybersecurity Project – Personal Firewall Using Python and Scapy
