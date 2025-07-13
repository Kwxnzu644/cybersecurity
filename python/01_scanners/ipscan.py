import argparse
import re
from datetime import datetime

# List of known suspicious IPs
IPS = ["203.0.113.5", "198.51.100.7", "192.0.2.3"]

# Function to display a banner title
def heading(title):
    print("+" + "-" * len(title) + "+")
    print(title)
    print("+" + "-" * len(title) + "+")

# Function to get current time
def time_stamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

# IP Scanner function
def ipscan(filename, output_file="logging.txt"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        with open(output_file, "a") as log:
            log.write(f"\n--- Scan started at: {time_stamp()} ---\n")
            log.write(f"Scanning file: {filename}\n")

            found = False

            for i, line in enumerate(lines):
                # Find all IPs in the line using regex
                ip_matches = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
                for match_ip in ip_matches:
                    if match_ip in IPS:
                        result = f"[!] Found suspicious IP {match_ip} on line {i+1}: {line.strip()}"
                        print(result)
                        log.write(result + "\n")
                        found = True

            if not found:
                msg = f"No suspicious IPs found in {filename}."
                print(msg)
                log.write(msg + "\n")

            log.write("--- Scan completed successfully ---\n")

    except FileNotFoundError:
        print(f"[X] File not found: {filename}")
    except Exception as e:
        print(f"[X] Error accessing {filename}: {e}")

# Main program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is an IP Address Scanner")
    parser.add_argument("-m", "--message", default="IP ADDRESS SCANNER", help="Display the title")
    parser.add_argument("-f", "--file", required=True, help="Log file to scan")
    parser.add_argument("-o", "--output", default="logging.txt", help="Save scan results to this file")

    args = parser.parse_args()

    heading(args.message)
    print(f"Scan started at: {time_stamp()}")
    ipscan(args.file, args.output)
