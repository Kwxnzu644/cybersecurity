# file_scanner.py - Scans a file for cybersecurity keywords and displays a banner

import argparse  # Import argparse to create a command-line interface

# Define a list of keywords to search for, indicating potential security issues
KEYWORDS = ["attack", "unauthorized", "breach", "failed login", "hack", "malware", "exploit", "hacking"]


# Define a function to display a formatted banner with a message
def print_banner(message):

    # Print a line of '=' characters matching the message length
    print("=" * len(message))

    # Print the message
    print(message)

    # Print another line of '=' characters for symmetry
    print("=" * len(message))

# Define a function to scan a file for keywords
def file_scanner(filename):

    # Try to open and read the file, handling potential errors
    try:
        # Open the file in read mode, ensuring proper closure
        with open(filename, "r", encoding="utf-8") as f:
            # Read all lines into a list for processing
            lines = f.readlines()
            # Iterate over lines with their indices for line number reporting
            for i, line in enumerate(lines):
                # Check each keyword in the KEYWORDS list
                for word in KEYWORDS:
                    # Case-insensitive check for the keyword in the line
                    if word.lower() in line.lower():
                        # Format and print an alert with the keyword, line number, and line content
                        result = f"[!] Found '{word}' on line {i+1}: {line.strip()}"
                        print(result)

    # Handle the case where the file doesn't exist
    except FileNotFoundError:
        print(f"[X] File not found: {filename}")
    # Handle other potential file errors (e.g., permission issues)
    except Exception as e:
        print(f"[X] Error accessing file {filename}: {e}")

# Check if the script is run directly (e.g., `python file_scanner.py`)
if __name__ == "__main__":
    # Create an ArgumentParser object to define the CLI
    parser = argparse.ArgumentParser(description="FILE SCANNER TOOL")
    # Add a required argument for the banner message
    parser.add_argument("-m", "--message", default="SECSERVE FILE SCANNER TOOL", help="Message for the banner (default: 'SECSERVE FILE SCANNER TOOL')")
    # Add a required argument for the file to scan
    parser.add_argument("-f", "--file", required=True, help="File to scan for keywords")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    # Display the banner with the provided message
    print_banner(args.message)
    # Scan the file for keywords, passing the output file if provided
    file_scanner(args.file)