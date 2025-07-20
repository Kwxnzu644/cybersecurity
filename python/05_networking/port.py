import socket
import argparse
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

port_profiles = {
    "1": {"name": "Top 10 Common Ports", "ports": [21, 22, 23, 25, 53, 80, 110, 139, 443, 445]},
    "2": {"name": "Web Ports Only","ports": [80, 443]},
    "3": {"name": "Remote Access Ports","ports": [22, 23, 3389, 5900]},
    "4": {"name": "All (Red Team Mix)","ports": [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389, 5900]}
}
def banner(message):
    print(Fore.CYAN + "+" * len(message))
    print(Fore.CYAN + message)
    print(Fore.CYAN + "+" * len(message))
    
def timestamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def portscan(target, ports,output="file.log"):
    try:
        with open(output, "a") as log:
            log.write(f"\nScan started at: {timestamp()}\n")
            
            for port in ports:
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                        sock.settimeout(1)
                        result = sock.connect_ex((target, port))
                        if result == 0:
                            msg = f"[{timestamp()}] Port {port} is OPEN"
                            print(Fore.GREEN + msg)
                            log.write(msg + "\n")
                        else:
                            msg = f"[{timestamp()}] Port {port} is CLOSED"
                            print(Fore.RED + msg)
                except Exception as e:
                    err_msg = f"Error scanning port {port}: {e}"
                    print(err_msg)
                    log.write(err_msg + "\n")
    except Exception as e:
        print(f"Failed to write to log file: {e}")
def show_menu():
    print(Fore.YELLOW + "\nSelect a port profile:")
    for key, profile in port_profiles.items():
        print(Fore.CYAN + f"{key}. {profile['name']}")
    choice = input(Fore.YELLOW + "\nEnter option number (1-4): ").strip()
    if choice not in port_profiles:
        print(Fore.RED + "Invalid option. Exiting...")
        exit(1)
    return port_profiles[choice]["ports"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("-m", "--message", default="PORT SCANNER", help="Displays the banner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address to scan")
    parser.add_argument("-o", "--output", default="file.log", help="Output log file")

    args = parser.parse_args()

    banner(args.message)
    print(f"Scan started at: {timestamp()}\n")
    
    selected_ports = show_menu()
    
    
    portscan(args.target, selected_ports, args.output)
