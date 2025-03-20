# Task 1: Countdown Timer

start_number = int(input("Enter the starting number: "))

# Countdown using a while loop
while start_number >= 1:
    print(start_number, end=" ")
    start_number -= 1


print("Blast off! 🚀")

# Task 2: Multiplication Table

number = int(input("\nEnter a number: "))

# Generate the multiplication table using a for loop
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Task 3: Factorial Calculation

number = int(input("\nEnter a number: "))

# Initialize the factorial result to 1
factorial = 1

# Calculate the factorial using a for loop
for i in range(1, number + 1):
    factorial *= i

# Print the result in a friendly format
print(f"The factorial of {number} is {factorial}.")