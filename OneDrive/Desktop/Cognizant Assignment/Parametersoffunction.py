# Task 1
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

def add_numbers(num1, num2):
    return num1 + num2

# Task 2
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Task 3
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

# Task 4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
greet_user("kelzang")
result = add_numbers(5, 10)
print(f"The sum of 5 and 10 is {result}.")

describe_pet("Lucy")
describe_pet("Whiskers", "cat")

make_sandwich("Lettuce", "Tomato", "Onion")

factorial_result = factorial(5)
fibonacci_result = fibonacci(6)
print(f"Factorial of 5 is {factorial_result}.")
print(f"The 6th Fibonacci number is {fibonacci_result}.")