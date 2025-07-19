import argparse
from datetime import datetime
import re
import socket
import subprocess

# Suspicious terms and IPs
keywords = ["attack", "unauthorized", "breach", "failed login", "hack", "malware", "exploit", "hacking"]
ips = ["203.0.113.5", "198.51.100.7", "192.0.2.3"]
Ports = [21, 22, 23, 25, 53, 80, 443, 3389]

# Banner function
def banner(message):
    print("=" * len(message))
    print(message)
    print("=" * len(message))

# Timestamp
def timestamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S %d-%m-%y")

# Ping scanner
def pingscan(target, output):
    try:
        response = subprocess.run(["ping", "-c", "1", target], capture_output=True, text=True)
        msg = f"[✔] Target {target} is Online" if response.returncode == 0 else f"[✘] Target {target} is Offline"
        with open(output, "a") as log:
            log.write(f"\n--- Ping Scan at {timestamp()} ---\n")
            log.write(msg + "\n")
        print(msg)
    except Exception as e:
        with open(output, "a") as log:
            log.write(f"Error pinging {target}: {e}\n")
        print(f"Error pinging {target}: {e}")

# Port scanner
def portscan(target, output):
    with open(output, "a") as log:
        log.write(f"\n--- Port Scan at {timestamp()} on {target} ---\n")
        for port in Ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(1)
                    result = sock.connect_ex((target, port))
                    msg = f"[✔] Port {port} is OPEN" if result == 0 else f"[✘] Port {port} is CLOSED"
                    log.write(msg + "\n")
                    print(msg)
            except Exception as e:
                log.write(f"Error scanning port {port}: {e}\n")
                print(f"Error scanning port {port}: {e}")

# Log file scanner
def logscan(file, output):
    try:
        with open(file, "r") as f:
            lines = f.readlines()
        found = False
        with open(output, "a") as log:
            log.write(f"\n--- Log Scan at {timestamp()} on file {file} ---\n")
            for i, line in enumerate(lines):
                for word in keywords:
                    if word.lower() in line.lower():
                        msg = f"[!] Found keyword '{word}' on line {i+1}: {line.strip()}"
                        log.write(msg + "\n")
                        print(msg)
                        found = True
                ip_match = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
                for ip in ip_match:
                    if ip in ips:
                        msg = f"[!] Found suspicious IP '{ip}' on line {i+1}: {line.strip()}"
                        log.write(msg + "\n")
                        print(msg)
                        found = True
            if not found:
                msg = f"No suspicious keywords or IPs found in {file}"
                log.write(msg + "\n")
                print(msg)
            log.write("---- Scan Complete ----\n")
    except FileNotFoundError:
        print(f"[X] File not found: {file}")
    except Exception as e:
        print(f"[X] Error scanning file {file}: {e}")

# Main CLI handler
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Secverse Threat Suite: Ping, Port, and Log Scanner")
    parser.add_argument("-m", "--message", default="SECSERVE: Red Team Threat Suite", help="Banner message")
    parser.add_argument("-f", "--file", nargs="+", required=True, help="File(s) to scan for logs")
    parser.add_argument("-t", "--target", required=True, help="Target IP to scan")
    parser.add_argument("-o", "--output", default="file.log", help="Output log file")

    args = parser.parse_args()

    banner(args.message)
    print(f"Scan started at: {timestamp()}\n")

    # Run scans
    for file in args.file:
        logscan(file, args.output)
    pingscan(args.target, args.output)
    portscan(args.target, args.output)
