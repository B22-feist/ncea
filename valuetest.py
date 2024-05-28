# Define a list containing dictionaries
list_of_dicts = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]

# Define the index you're looking for
index_to_find = 0  # For example, 0 refers to the first dictionary

# Check if the index is within the bounds of the list
if 0 <= index_to_find < len(list_of_dicts):

    # Access the dictionary at the specified index
    dictionary = list_of_dicts[index_to_find]
    
    # Print the value associated with the key 'name'
    if 'name' in dictionary:
        print(dictionary['name'])
    else:
        print("'name' key not found in the dictionary.")
else:
    print("Index out of range.")
