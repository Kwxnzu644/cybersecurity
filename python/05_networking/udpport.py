import socket
import argparse
from datetime import datetime

def timestamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def udp_scan(target, ports):
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)

            sock.sendto(b"", (target, port))  # send empty UDP packet
            data, _ = sock.recvfrom(1024)
            print(f"[{timestamp()}] [OPEN] UDP Port {port} - Response: {data}")

        except socket.timeout:
            print(f"[{timestamp()}] [?] UDP Port {port} - No response (open|filtered)")

        except Exception as e:
            print(f"[{timestamp()}] [ERROR] UDP Port {port}: {e}")

        finally:
            sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UDP Port Scanner")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("-p", "--ports", nargs="+", type=int, help="List of UDP ports")
    args = parser.parse_args()

    udp_scan(args.target, args.ports)

    
    