import argparse
from datetime import datetime
import re

# Keywords and suspicious IPs
highlights = ["attack", "unauthorized", "breach", "failed login", "hack","malware", "exploit", "hacking", "203.0.113.5", "198.51.100.7", "192.0.2.3"]
suspicious_ips = ["203.0.113.5", "198.51.100.7", "192.0.2.3"]

# Banner function
def banner(message):
    print("=" * len(message))
    print(message)
    print("=" * len(message))

# Timestamp function
def timestamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S %d-%m-%y")

# Scanner function
def filescanner(filename, output="file.log"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        
        found = False
        
        with open(output, "a") as log:
            log.write(f"\n--- Scan started at: {timestamp()} ---\n")
            log.write(f"File scanned: {filename}\n")
            
            for i, line in enumerate(lines):
                # Keyword match
                for keyword in highlights:
                    if keyword.lower() in line.lower():
                        result = f"[!] Found keyword '{keyword}' on line {i+1}: {line.strip()}"
                        print(result)
                        log.write(result + "\n")
                        found = True
                
                # IP regex match
                ip_matches = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
                for ip in ip_matches:
                    if ip in suspicious_ips:
                        result = f"[!] Found suspicious IP {ip} on line {i+1}: {line.strip()}"
                        print(result)
                        log.write(result + "\n")
                        found = True

            if not found:
                msg = f"No suspicious keyword or IP found in: {filename}"
                print(msg)
                log.write(msg + "\n")

            log.write(f"--- Scan completed for file: {filename} ---\n\n")

    except FileNotFoundError:
        print(f"[X] File not found: {filename}")
    except Exception as e:
        print(f"[X] Error accessing {filename}: {e}")

# CLI setup
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FILE SCANNER TOOL")
    parser.add_argument("-m", "--message", default="FILE SCANNER", help="Display banner")
    parser.add_argument("-f", "--file", nargs='+', required=True, help="Input file(s) to scan")
    parser.add_argument("-o", "--output", default="file.log", help="Log file to save results")

    args = parser.parse_args()

    banner(args.message)
    print(f"Scan started at: {timestamp()}\n")

    for file in args.file:
        filescanner(file, args.output)
