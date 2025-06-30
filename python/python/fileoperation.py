# Write some text to a file

with open('testoutput.txt', 'w') as f:
    f.write("This is a line written to the file.\n")
    f.write("this is another line written.\n")
# f.write(...): Writes the string to the file. \n creates a new line.

# Add more lines to an existing file
with open('testoutput.txt', 'a') as f:
    f.write("This line is appended.\n")

#open('test_output.txt', 'r'): Opens the file for reading.
#for line in f:: Loops through each line in the file.
#line.strip(): Removes any leading/trailing whitespace and newlines.

# Read text from a file
with open('testoutput.txt', 'r') as f:
    for line in f:
        print(f.strip())

#helpful when readin comma sep values
import csv

with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)#creates a writable object that lets you write

    writer.writerow(['username', 'password'])
    writer.writerow(['admin', 'secret123'])

# Reading the CSV back
with open('test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
