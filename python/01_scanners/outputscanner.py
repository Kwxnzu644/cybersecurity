import argparse
from datetime import datetime
import re

# Keywords to scan for
highlights = ["attack", "unauthorized", "breach", "failed login", "hack", "malware", "exploit", "hacking","203.0.113.5", "198.51.100.7", "192.0.2.3"]
suspicious_ips = ["203.0.113.5", "198.51.100.7", "192.0.2.3"]

# Header printer
def Header(title):
    print("=" * len(title))
    print(title)
    print("=" * len(title))

# Timestamp function
def timestamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S %d-%m-%y")

# File scanner function
def filescanner(filename, outputfile="highlights.txt"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        found = False

        with open(outputfile, "a") as logs:
            logs.write(f"\n--- Scan started at: {timestamp()} ---\n")
            logs.write(f"Scanning file: {filename}\n")

            for i, line in enumerate(lines):
                 for keyword in highlights:
                    if keyword.lower() in line.lower():
                        result = f"[!] Found '{keyword}' on line {i+1}: {line.strip()}"
                        print(result)
                        logs.write(result + "\n")
                        found = True
                  # Check for suspicious IPs using regex
                 ips_found = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
                 for ip in ips_found:
                    if ip in suspicious_ips:
                        result = f"[!] Found suspicious IP '{ip}' on line {i+1}: {line.strip()}"
                        print(result)
                        logs.write(result + "\n")
                        found = True 
                        
            if not found:
                msg = f"No keywords found in {filename}"
                print(msg)
                logs.write(msg + "\n")

            logs.write(f"--- Scan completed on: {timestamp()} ---\n\n")

    except FileNotFoundError:
        print(f"[X] Error: File not found: {filename}")
    except Exception as e:
        print(f"[X] Error accessing file {filename}: {e}")

# Command-line interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FILE SCANNER 2.0")
    parser.add_argument("-m", "--message", default="FILE SCANNER EXTENSION", help="Display the title")
    parser.add_argument("-o", "--output", default="highlights.txt", help="Save results to file")
    parser.add_argument("-f", "--file", required=True, nargs="+",help="File to scan")

    args = parser.parse_args()

    Header(args.message)
    print(f"Scan started at: {timestamp()}")
    
    for file in args.file:  # <-- loop through multiple files
        filescanner(file, args.output)