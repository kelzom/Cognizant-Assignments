import logging

# Configure logging
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_error(error):
    logging.error(f"{error.__class__.__name__} occurred: {error}")

def display_menu():
    print("\nWelcome to the Error-Free Calculator!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_choice():
    while True:
        try:
            choice = int(input("> "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print("Oops! Division by zero is not allowed.")
        log_error(e)
        return None
    except ValueError as e:
        print("Invalid input! Please enter valid numbers.")
        log_error(e)
        return None
    else:
        return result

def main():
    while True:
        display_menu()
        choice = get_choice()

        if choice == 5:
            print("Goodbye!")
            break

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == 1:
            result = num1 + num2
            print(f"Result: {result}")
        elif choice == 2:
            result = num1 - num2
            print(f"Result: {result}")
        elif choice == 3:
            result = num1 * num2
            print(f"Result: {result}")
        elif choice == 4:
            result = divide_numbers(num1, num2)
            if result is not None:
                print(f"Result: {result}")
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()