# create a dictionary
my_dict = {
    'name': 'Lin Armstrong',
    'age': 23
}

# Access the items of a dictionary
print(my_dict.items())

# Change the value of a specific item in a dictionary
my_dict.update({'age': 24, 'profession': 'doctor'})
print(my_dict)

# Print all key names in a dictionary, one by one
print(my_dict.keys())

# Print all values in a dictionary, one by one
for x in my_dict.values():
    print(x)
    
# Use the values() function to return values of a dictionary
# Loop through both keys and values, by using the items() function
# Check if a key exists
# Get the length of a dictionary
# Add an item to a dictionary
# Remove an item from a dictionary
# Empty a dictionary
# Use the dict() constructor to create a dictionary