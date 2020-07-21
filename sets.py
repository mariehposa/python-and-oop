# Create a set
my_set = {'rice', 'maize', 'oat'}

# Loop through a set
for x in my_set:
    print(x)

# Check if an item exists
if 'rice' in my_set:
    print('It exists')

# Add an item to a set
my_set.add('beans')

# Add multiple items to a set
my_set.update({'yam', 'egg'})
print(my_set)

# Get the length of a set
print(len(my_set))

# Remove an item in a set
my_set.remove('egg')

# Remove an item in a set by using the discard() method
my_set.discard('yam')

# Remove the last item in a set by using the pop() method
# Empty a set
# Delete a set
# Use the set() constructor to create a set