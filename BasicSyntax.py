import random

if 5 > 2:
  print("indentation is used to indicate block of code")

# if 5 > 2:
# print("This block gives error as there is no indentation")

if 5 > 2:
 print("Number of spaces must greater than 0") 
if 5 > 2:
        print("Block of code should have same no.of spaces for indentation") 

# if 5 > 2:
#  print("This block throws an error!")
#         print("As no.of spaces differ for lines in the same block of code!")

#VARIABLES
x = 5
y = "Hello, World!"
"""This is used as multy line comment."""
print(x)
print(y)

#many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print(random.randrange(1, 10)) #prints random number

#CASTING
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
#acessing string as array
a = "Hello, World!"
print(a[1])
print(b[2:5]) #slice the string from position 2 to 5 (not included)
print(b[:5])  #slice from the start
print(b[2:])  #slice to the end
print(b[-5:-2]) #negative indexing
print(len(a)) #length of an array
#looping through an array
for x in "python":
  print(x)
txt = "To check if a certain phrase or character is present in a string, we can use the keyword in"
print("character" in txt)
print("not" not in txt) #not present in string

#MODIFY STRINGS
a = "Hello, World!  "
print(a.upper())    #uppercase
print(a.lower())    #lowercase
print(a.strip())    #removes whitespace from the begining or the end
print(a.replace("H", "J"))  #replacing the string
print(a.split(","))  #splits based on the seperator

#f-string
age = 23
txt = f"My name is Bhudevi, I am {age}"
print(txt)