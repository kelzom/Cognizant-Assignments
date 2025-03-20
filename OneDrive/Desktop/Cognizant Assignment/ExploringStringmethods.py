# Task 1: String Slicing and Indexing
my_string = "Python is amazing!"

# Extract the first 6 characters
first_word = my_string[:6]
print("First word:", first_word)

# Extract the word "amazing"
amazing_part = my_string[10:17]
print("Amazing part:", amazing_part)

# Reverse the entire string
reversed_string = my_string[::-1]
print("Reversed string:", reversed_string)

# Task 2: String Methods
my_string = " hello, python world! "

# Remove extra spaces using strip()
stripped_string = my_string.strip()
print("\nStripped string:", stripped_string)

# Capitalize the first letter using capitalize()
capitalized_string = stripped_string.capitalize()
print("Capitalized string:", capitalized_string)

# Replace "world" with "universe" using replace()
replaced_string = capitalized_string.replace("world", "universe")
print("Replaced string:", replaced_string)

# Convert the string to uppercase using upper()
uppercase_string = replaced_string.upper()
print("Uppercase string:", uppercase_string)

# Task 3: Check for Palindromes
# Ask the user to input a word
word = input("\nEnter a word: ")

# Check if the word is a palindrome
if word == word[::-1]:
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"No, '{word}' is not a palindrome.")