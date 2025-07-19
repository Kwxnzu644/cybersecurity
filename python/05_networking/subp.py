import argparse
from datetime import datetime
import subprocess

def banner(message):
    print("=" * len(message))
    print(message)
    print("=" * len(message))

def timestamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def pinger(target_ip, output="file.log"):
    try:
        response = subprocess.run(["ping","-c","1",target_ip], capture_output=True, text=True)
        if response.returncode == 0:
            result = f"[!] Target {target_ip} is online."
        else:
            result = f"[x] Target {target_ip} is NOT online."
        with open(output, "a") as log:
            log.write(f"Scan at {timestamp()} - {result}\n")
        print(result)
    except Exception as e:
        print(f"Unable to ping the target {target_ip} : {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ping checker")
    parser.add_argument("-m", "--message", default="PING CHECKER", help="DISPLAYS THE BANNER")
    parser.add_argument("-o", "--output", default="file.log", help="SAVES THE OUTPUT")
    parser.add_argument("-t", "--target", required=True, help="TARGETS AN IP")

    args = parser.parse_args()

    banner(args.message)
    
    print(f"Scan started at: {timestamp()}")

    if args.target:
        pinger(args.target, args.output)
