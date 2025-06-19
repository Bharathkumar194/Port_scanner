# 🔍 Basic Port Scanner in Python

This is a simple **Port Scanner** built using Python that scans a target host for open ports within a given range. It's a beginner-friendly project demonstrating the use of the `socket` module for basic network tasks.

## 📌 Features

- Scans a target IP address or domain name
- Reports which ports are open (default: ports 1–100)
- Uses TCP (connect) method via socket
- Lightweight and easy to run
- Beginner-friendly and customizable

## 🚀 How It Works

The script attempts to connect to each port in the specified range using a TCP socket. If the connection is successful (i.e., `connect_ex()` returns 0), the port is considered open.

## 🧪 Sample Output

Enter target IP or domain: example.com
Resolved IP: 93.184.216.34

Starting scan on host: 93.184.216.34
Scanning ports from 1 to 100...

Port 80: OPEN

Scan completed in: 0:00:01.245678


## 🛠️ Requirements

- Python 3.x (no external libraries required)

## 🧾 How to Run

```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
python port_scanner.py
