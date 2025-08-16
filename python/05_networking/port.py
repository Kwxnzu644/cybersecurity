import socket
import argparse
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

def banner(message):
    print(Fore.RED + "=" * len(message))
    print(message)
    print(Fore.RED + "=" * len(message))

def timestamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def portscan(target, ports, output="file.log"):
    try:
        with open(output, "a") as log:
            log.write(f"Scan Started at {timestamp()} \n")
            
            for port in ports:
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                        sock.settimeout(1)
                        result = sock.connect_ex((target, port))
                        if result == 0:
                            msg = Fore.GREEN + Style.BRIGHT + f"[!] Port {port} is Open"
                        else:
                            msg = Fore.RED + Style.BRIGHT + f"[x] Port {port} is Closed"
                        
                        print(msg)
                        log.write(msg + "\n")
                        
                except Exception as e:
                    print(f"Error scanning port {port} on {target}: {e}")
    except Exception as e:
        print(f"Unable to write the file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", default="PORT SCANNER", help="Displays the banner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address to scan")
    parser.add_argument("-o", "--output", default="file.log", help="Output log file")
    parser.add_argument("-p", "--ports", nargs="+", type=int, default=[21, 22, 80, 443],
                        help="List of ports to scan (space-separated)")

    args = parser.parse_args()

    banner(args.message)
    print(f"Scan started at: {timestamp()}\n")
    portscan(args.target, args.ports, args.output)
