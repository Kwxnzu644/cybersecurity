import argparse
from datetime import datetime

# List of suspicious words
words = ["attack", "unauthorized", "breach", "failed login", "hack", "malware", "exploit", "hacking"]

# Print a nice banner
def title(heading):
    print("#" + "=" * len(heading) + "#")
    print(heading)
    print("#" + "=" * len(heading) + "#")

# Return current timestamp
def get_timestamp():
    now = datetime.now()
    return now.strftime("%y-%m-%d %H:%M:%S")

# Scanner function
def scanner(filename, output_file="log.txt"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        with open(output_file, "a") as log:
            log.write(f"\nScan started at {get_timestamp()}\n")
            log.write(f"Scanning file: {filename}\n\n")
            # Write all content
            for line in lines:
                log.write(line)
            log.write("\n")

            # Scan for keywords
            found = False
            
            for i, line in enumerate(lines):
                for word in words:
                    if word.lower() in line.lower():
                        result = f"[!] On File {filename} Found '{word}' on line {i+1}: {line.strip()}"
                        print(result)
                        log.write(result + "\n")
                        found = True

            if not found:
                msg = f"No keywords detected in {filename}"
                print(msg)
                log.write(msg + "\n")

            log.write("...Scan Completed...\n")

    except FileNotFoundError:
        print(f"File not Found: {filename}")
    except Exception as e:
        print(f"Unable to Access the file {filename}: {e}")

# Main
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FILE TOOL SCANNER")
    parser.add_argument("-m", "--message", default="SECSERVE FILE SCANNER TOOL", help="Display banner")
    parser.add_argument("-f", "--file", required=True, help="File to scan")
    parser.add_argument("-o", "--output", default="log.txt", help="File to save scan results")
    args = parser.parse_args()

    title(args.message)
    print(f"scan started at: {get_timestamp()}")
    scanner(args.file, args.output)
