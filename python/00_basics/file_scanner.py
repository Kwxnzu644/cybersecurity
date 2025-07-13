# file_scanner.py - A script to scan a file for cybersecurity-related keywords

# Define a list of keywords to search for, indicating potential security issues
KEYWORDS = ["attack", "unauthorized", "breach", "failed login"]

# Define a function to scan a file for keywords and print matching lines
def scan_file(filename):
    # Try to open and read the file, handling potential errors
    try:
        # Open the file in read mode, using a with statement to ensure proper closure
        with open(filename, "r") as f:
            # Read all lines into a list for processing
            lines = f.readlines()
            # Iterate over lines with their indices for line number reporting
            for i, line in enumerate(lines):
                # Check each keyword in the KEYWORDS list
                for kw in KEYWORDS:
                    # Case-insensitive check for the keyword in the line
                    if kw.lower() in line.lower():
                        # Print an alert with the keyword, line number (1-based), and line content
                        print(f"[!] Found '{kw}' on line {i+1}: {line.strip()}")
    # Handle the case where the file doesn't exist
    except FileNotFoundError:
        # Print an error message with the filename
        print(f"[X] File not found: {filename}")



# Check if the script is run directly (e.g., `python file_scanner.py`)
if __name__ == "__main__":
    # Prompt the user to enter the filename to scan 
    fname = input("Enter file to scan: ")
    # Call scan_file with the provided filename (fixed from 'filename' to 'fname')
    scan_file(fname)