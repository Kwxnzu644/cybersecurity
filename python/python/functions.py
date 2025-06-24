#Functions allow you to organize your code into reusable blocks.
# #They make your code easier to understand, test, and maintain.

#(name) is a parameter — it’s like a placeholder for any value you’ll pass in later.
#f this allows you to enter a variable its a formated string 
#sayhi ,name of the of the funcion

def sayhi (name):
    print(f"hello, {name},welcome to cybersec by kwanzu111.")
    
sayhi("kwanzu")


#functions with arguements 
#(base , exponent=2) this are parameters that are just filled in
# base is an input and exponent can be added  any value

def power(base , top=2):
     return base ** top

print(power(3))
print(power(3,3))


def square(x):
    return x * x

print(square(5))


