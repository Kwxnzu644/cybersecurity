
#variable
age = 20

# If/elif/else 
if age < 18:
    print("You are a minor.")
elif age > 50:
    print("You are an adult.")
else:
    print("You are a senior.")

name = input(f"your name is?")
score = int(input("your score is?"))

if score > 50 :
    print(f"you have passed {name}")
else:
    print(f"you have failed {name}")
 
# For loop 
#variables
#Python takes each item(variables that are declared) from the list names, one at a time, and assigns it to the variable name
#is executed each at a time
names = ["Alice", "Bob", "Kwanzu"]

for name in names:
    print("come,", name)


for number in range(1, 6):
    print(number)



# While loop example

#Starts at count = 1

#Prints the number

#Increases count by 1

#Keeps repeating until count is greater than 

counter = 0

while counter < 5:
    print("Counter is:", counter)
    counter += 1