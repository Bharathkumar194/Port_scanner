import socket
from datetime import datetime

# Function to scan ports
def port_scanner(target, start_port, end_port):
    print(f"\nStarting scan on host: {target}")
    print(f"Scanning ports from {start_port} to {end_port}...\n")
    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Short timeout
        result = sock.connect_ex((target, port))  # 0 means success (open port)
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"\nScan completed in: {total_time}")

# Main code
if __name__ == "__main__":
    target_host = input("Enter target IP or domain: ")
    try:
        target_ip = socket.gethostbyname(target_host)
        print(f"Resolved IP: {target_ip}")
        port_scanner(target_ip, 1, 100)
    except socket.gaierror:
        print("Error: Unable to resolve host.")
