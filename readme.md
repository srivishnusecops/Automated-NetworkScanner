# Automated Network Scanner

**Automated Network Scanner** is a Python-based tool designed to perform fast and efficient network scans using **Masscan** and **Nmap**. This tool allows users to execute a variety of scan types, from basic ping sweeps to more advanced vulnerability and protocol scans. It integrates both Masscan and Nmap to help security professionals and network administrators assess the security of their networks.

## Features

- **Masscan Integration**: High-speed scanning for SYN and TCP scans over specified port ranges.
- **Nmap Integration**: Advanced scanning options including SYN scan, Ping scan, Host alive check, and more.
- **Command-line interface (CLI)** for user-friendly navigation.
- **JSON Output**: Scan results are saved in JSON format for easy parsing and analysis.

## Scan Types Available

### Masscan
- **SYN Scan**: Performs a SYN scan on a target network.
- **TCP Scan**: Scans for open TCP ports using a full connect scan.

### Nmap
- **Host Alive Check**: Checks if the host is online.
- **Ping Scan**: Detects live hosts using ICMP ping.
- **SYN Scan**: Stealthy scan using SYN packets.
- **TCP Scan**: Regular TCP connect scan.
- **UDP Scan**: Scans for open UDP ports.
- **Vulnerability Scan**: Scans for common vulnerabilities using Nmap scripts.
- **Null Scan**, **Xmas Scan**, and more.

## Prerequisites

Before running this tool, ensure the following dependencies are installed:

- **Python 3.x** (recommended version: 3.6 or above)
- **Masscan** (installed on your system)
- **Nmap** (installed on your system)

Install Python dependencies by running:

```bash
pip install -r requirements.txt
