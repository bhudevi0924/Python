def my_function():
  print("Hello from a function")

my_function()

######function with argument###
def my_function(fname):
  print(fname)

my_function("Emil")

##arbitrary arguments##
def my_function(*numbers):
  print(numbers[2])         #accessing value

my_function("one", "two", "three")

###keyword argument#######
def my_function(value3, value2, value1):
  print(value3)

my_function(value1 = "Black", value2 = "Blue", value3 = "White")

###arbitrary keyword arguments########
def my_function(**color):
  print(color["black"])

my_function(black = "Black", blue = "Blue")

####default parameter value#####
def my_function(name = "Bhudevi Dobbala"):
  print(name)

my_function("Bhudevi")
my_function("Devi")
my_function()

###passing list as an argument#####
def my_function(numbers):
  for x in numbers:
    print(x)

numbersList = [1,2,3]
my_function(numbersList)

####return values##########
def my_function(x):
  return 5 * x

print(my_function(3))

###positional-only arguments### (parameters that can only be specified by their position, not by keyword.)
def my_function(x, /):
  print(x)

my_function(3)
#my_function(x = 3)       #This will throw an error as it has keyword argument

###keyword only argument####
def my_function(*, x):
  print(x)

my_function(x = 3)
#my_function(3)          #This will throw an error as the funtion allows only keyword argument

###combile positional-only and keyword-only####
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

##Recursion###
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Results:")
tri_recursion(6)

