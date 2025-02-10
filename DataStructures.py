####LISTS###########
# Creating a List with
List = ["Blue", "White", "Black"]
print(List)

# Creating a Multi-Dimensional List
List2 = [['one', 'two'], ['three']]

# accessing a element from the list using index number
print(List[0])  
print(List[2]) 

print(List[-1])         # accessing a element using negative indexing

####DICTIONARY###########
# Creating a Dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print(Dict)
print(Dict['Name'])    # accessing a element using key

print(Dict.get(1))     # accessing a element using get() method

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)

#####TUPLE###########
# Creating a Tuple with the use of Strings
Tuple = ('one', 'two')
print(Tuple)
    
# Creating a Tuple with the use of list
list1 = [1, 2, 4, 5, 6]
Tuple = tuple(list1)

print(Tuple[0])     # Accessing element using indexing
print(Tuple[-1])    # Accessing element from last (negative indexing)

###########SET###########
# Creating a Set with  a mixed type of values (Having numbers and strings) 
Set = set([1, 2, 'value1', 4, 'one', 6, 'value1'])
print(Set) 
# Accessing element using for loop 
for i in Set: 
    print(i, end =" ") 
print()
# Checking the element using in keyword 
print("value1" in Set)

#####FROZEN SET######
normal_set = set(["a", "b","c"]) # Same as {"a", "b","c"}
print(normal_set)

frozen_set = frozenset(["e", "f", "g"]) # A frozen set
print(frozen_set)
# cause error as we are trying to add element to a frozen set
# frozen_set.add("h")

########STRING#########
String = "Python"
print(String) 
print(String[0])   # Printing First character
print(String[-1])  # Printing Last character 

########BYTEARRAY########### (stores values in hexa decimal form)
# Creating bytearray
a = bytearray((12, 8, 25, 2))        #stored as single byte in memory
print(a)
print(a[1])   # accessing elements

# modifying elements 
a[1] = 3
print(a)

# Appending elements
a.append(30)
print(a)