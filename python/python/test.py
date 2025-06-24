#1
name = "Alvin Kwamzu"
age = 20
programminglang = ["python" , "cpp" , "shell"]
print("name:",name)
print("age:",age)
print("My Favourite Programming Language:",programminglang)

#2

score = 40

if score>=50:
    print("passes")
elif score<50:
    print("failed")
else:
    print("failureeeee")

#3

for num in range (1,6):
     print(num)


#4

count = 10

while count>=6 :
       print(count)
       count -= 1 

#5



ages = [12, 17, 19, 24, 15, 30]

for age in ages:
      if age<18:
        print("minor")
      else:
        print("Adult")

# Python Functions & Control Structures Test

#1
def multiply(a,b):
 return a * b
  
print(multiply(4, 5))

#2
#setting friend a default name
def greet(name = "friend"):
  print(f"hello,{name}")

greet()

#3
def square_all(numbers):
    for num in numbers:
        print(num * num)

square_all([2, 4, 6])

#4

count = 7

while count>=1 :
 print("count",count)
 count -=1

 if count %2==0:
   print("even")
 else:
  print("odd")


#5 
#for this check the utils folder


#6
def check(x):
    if x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    else:
        return "Positive"

print(check(-2))
print(check(0))
print(check(10))

