# Creating and using a list
tools = ["nmap", "wireshark", "hashcat"]

print(tools[1])         # Output: nmap

tools.append("john")    # Add an item
print(tools)

tools.remove("hashcat") # Remove an item
print("Length:", len(tools)) # number of the tools

# Creating and using a dictionary
user = {"name": "Kwanzu", "role": "student", "active": True}
print(user["name"])

user["country"] = "Kenya" #this is to add
print(user)

del user["active"] #this is to remove

print(user)

# Using sets
ports = {22, 80, 443, 22}  # Duplicate 22 ignored
print(ports)

ports.add(8080)

ports.remove(80)

print(ports)

# Using tuples
credentials = ("admin", "password123")
print(credentials[0])
# credentials[0] = "root"  # This would cause an error (tuples can't be changed)

# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)
