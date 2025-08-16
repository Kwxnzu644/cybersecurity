import argparse
import socket
import subprocess
from colorama import Fore, init, Style
from datetime import datetime

init(autoreset=True)

def banner(message):
    print(Fore.CYAN + Style.BRIGHT + "=" * len(message))
    print(message)
    print(Fore.CYAN + Style.BRIGHT + "=" * len(message))

def timestamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def pinger(target, output="file.log"):
    try:
        response = subprocess.run(["ping", "-c", "1", target], capture_output=True, text=True)
        if response.returncode == 0:
            print(f"Target {target} is Online")
        else:
            print(f"Target {target} is Offline")
    except Exception as e:
        print(f"Unable to ping target {target} : {e}")

def portscan(target, port, output="file.log"):
    try:
        with open(output, "a") as log:
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((target, port))
                if result == 0:
                    msg = f"Port {port} is Open"
                else:
                    msg = f"Port {port} is Closed"
                log.write("\n" + msg)
                print(msg)
    except Exception as e:
        print(f"Unable to scan port {port} : {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--message", default="NETWORK TOOL", help="DISPLAY THE BANNER")
    parser.add_argument("-o", "--output", default="file.log", help="OUTPUT SAVE FILE")
    parser.add_argument("-p", "--port", type=int, default=443, help="INPUT PORT")
    parser.add_argument("-t", "--target", required=True, help="INPUT TARGET")

    args = parser.parse_args()
    banner(args.message)

    print(f"Scan started at {timestamp()}")

    pinger(args.target, args.output)
    portscan(args.target, args.port, args.output)
