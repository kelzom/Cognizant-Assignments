# Task 1: Handling ZeroDivisionError and ValueError
print("Task 1: Handling ZeroDivisionError and ValueError")
try:
    number = float(input("Enter a number: "))
    result = 100 / number
    print(f"100 divided by {number} is {result}.")
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a valid number.")

# Task 2: Handling IndexError, KeyError, and TypeError
print("\nTask 2: Handling IndexError, KeyError, and TypeError")
try:
    # IndexError example
    my_list = [1, 2, 3]
    print(my_list[5])  
except IndexError:
    print("IndexError occurred! List index out of range.")

try:
    # KeyError example
    my_dict = {"name": "Alice", "age": 25}
    print(my_dict["address"])  
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

try:
    # TypeError example
    result = "Hello" + 42  
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

# Task 3: 
print("\nTask 3: Using try...except...else...finally")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input! Please enter numeric values.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")