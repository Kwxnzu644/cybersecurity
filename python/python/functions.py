#Functions allow you to organize your code into reusable blocks.
#They make your code easier to understand, test, and maintain.

#(name) is a parameter — it’s like a placeholder for any value you’ll pass in later.
#f this allows you to enter a variable only  its a formated string 
#sayhi ,name of the of the funcion

def sayhi (name = "friend"):
    print(f"hello, {name},welcome to cybersec by kwanzu111.")
    
sayhi()


#functions with arguements 
#(base , top=2(ALSO MAKING IT DEFAULT) this are parameters that are just filled in
# base is an input and exponent can be added  any value
#return is mostly used for math calculations

def power(base , top):
     return base ** top

base = int(input( "Enter a number ? "))
top = int(input( "enter the power ? "))
print(power(base,top))



def square(x):
    return x * x

print(square(5))


