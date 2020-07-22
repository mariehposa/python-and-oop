# create a dictionary
my_dict = {
    'name': 'Lin Armstrong',
    'age': 23
}

# Access the items of a dictionary
print(my_dict.items())

# Change the value of a specific item in a dictionary
my_dict.update({'age': 24})
print(my_dict)

# Print all key names in a dictionary, one by one
for x in my_dict.keys():
    print(x)

# Print all values in a dictionary, one by one
for y in my_dict.values():
    print(y)

# Use the values() function to return values of a dictionary
# Loop through both keys and values, by using the items() function
# Check if a key exists
if 'name' in my_dict.keys():
    print('It exists')

# Get the length of a dictionary
print(len(my_dict))

# Add an item to a dictionary
my_dict['school'] = 'Lambda School'
my_dict.update({'profession': 'doctor'})

# Remove an item from a dictionary
my_dict.popitem()
my_dict.pop('age')

# Empty a dictionary
del my_dict

# Use the dict() constructor to create a dictionary
new_dict = dict()
print(new_dict)