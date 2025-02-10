number = 10
try:
    res = number / 0  # This will raise a ZeroDivisionError
    
except ZeroDivisionError:
    print("Can't be divided by zero!")

try:
    number = 0
    res = 100 / number
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")

#catching specific exception##
try:
    x = int("str")  # This will cause ValueError
    
    #inverse
    inv = 1 / x
    
except ValueError:
    print("Not Valid!")
    
except ZeroDivisionError:
    print("Zero has no inverse!")

##catching multiple exceptions###
a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")

##catch-all handlers##
try:
    # Simulate risky calculation: incorrect type operation
    res = "100" / 20
    
except ArithmeticError:
    print("Arithmetic problem.")
    
except:
    print("Something went wrong!")

##raise an exception###
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)

