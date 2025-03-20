# Task 1: Working with Lists
# Create a list of favorite fruits
favorite_fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original list:", favorite_fruits)

# Append a new fruit to the list
favorite_fruits.append("fig")
print("After adding a fruit:", favorite_fruits)

# Remove one fruit from the list
favorite_fruits.remove("apple")
print("After removing a fruit:", favorite_fruits)

# Print the list in reverse order using slicing
reversed_list = favorite_fruits[::-1]
print("Reversed list:", reversed_list)

# Task 2: Exploring Dictionaries
# Create a dictionary with personal information
my_info = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Add a new key-value pair for "favorite color"
my_info["favorite color"] = "Blue"

# Update the "city" key with a new value
my_info["city"] = "San Francisco"

# Print all keys and values using a loop
print("\nKeys:", ", ".join(my_info.keys()))
print("Values:", ", ".join(str(value) for value in my_info.values()))

# Task 3: Using Tuples
# Create a tuple with favorite movie, song, and book
favorite_things = ("Inception", "Bohemian Rhapsody", "1984")
print("\nFavorite things:", favorite_things)

# Try to change one of the elements (this will raise an error)
try:
    favorite_things[0] = "The Matrix"
except TypeError as e:
    print("Oops! Tuples cannot be changed.")

# Print the length of the tuple
print("Length of tuple:", len(favorite_things))