# file_scanner.py

KEYWORDS = ["attack", "unauthorized", "breach", "failed login"]

def scan_file(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                for kw in KEYWORDS:
                    if kw.lower() in line.lower():
                        print(f"[!] Found '{kw}' on line {i+1}: {line.strip()}")
    except FileNotFoundError:
        print(f"[X] File not found: {filename}")

if __name__ == "__main__":
    fname = input("Enter file to scan: ")
    scan_file(fname)
