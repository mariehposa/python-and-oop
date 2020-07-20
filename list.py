# Create a list
my_list = [2, 3, 4, 6, 8]

# Access list items
print(my_list[0: 5])

# Change the value of a list item
my_list[4] = 7
print(my_list)

# Loop through a list
for x in my_list:
    print(x)

# Check if a list item exists
if 1 in my_list:
    print('It exists')
else:
    print('It does not exists')

# Get the length of a list
print(len(my_list))

# Add an item to the end of a list
my_list.append(8)
print(my_list)

# Add an item at a specified index
my_list.insert(0, 1)
print(my_list)

# Remove an item
my_list.pop()
print(my_list)

# Remove an item at a specified index
my_list.remove(0)
print(my_list)

# Empty a list
del my_list
print (my_list)

# Use the list() constructor to make a list