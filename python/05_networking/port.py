import socket

Ports=[21, 22, 23, 25, 53, 80, 443, 3389]

def banner(message):
    print("=" * len(message))
    print(message)
    print("=" * len(message))
    
def timestamp():
    now = datetime.now()
    return now.strftime()

def portscan(tagedip, output="file.log"):
    with open(output, "a") as log:
        log.write(f"Scan started at : {timestamp()}")
        log.write(f"Scan started on tagged ip {tagedip}") 
        
        for port in Ports:
            try:
                with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
                    socket.timeout(1)
                    result = socket.connect_ex((tagedip,port))
                    if result == 0:
                        msg = f"[!] Port {port} is open"
                        print(msg)
                        log.write(msg + "\n")
                        
            except Exception as e:
                print(f"Error scanning port {port} on ip {tagedip}")
                log.write(f"Error scanning port {port} on ip {tagedip}")
                

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