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


def pinger(target, output ="file.log"):
    try:
        response = subprocess.run(["ping","-c","1",target], capture_output=True , text=True)
        if response.returncode == 0:
            result = f"Target {target} is Online "
            print(result)
        else:
            result = f"Target {target} is Offline"
            print(result)
        
        with open(output , "a") as log:
            log.write(f"\nscan started at {timestamp()}\n")
            log.write("\n" + result)
              
    except Exception as e:
        msg = f"Unable to ping target {target}"
        print(msg)
        
        with open(output, "a") as log:
            log.write("\n" + msg)
        
                 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PING TARGETS")
    parser.add_argument("-m","--message",default="PING TARGET" ,help="DISPLAYS THE BANNER")
    parser.add_argument("-t","--target",required = True,help="INPUT THE IP ADRESS")
    parser.add_argument("-o","--output", default="file.log",help="SAVES THE OUTPUT")
    
    args = parser.parse_args()
    
    
    banner(args.message)
    
    print(f"Scan started at : {timestamp()}")
    
    pinger(args.target, args.output)
    
            
            
