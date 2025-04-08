# Dictionary in Python
# A Python dictionary is a collection of key-value pairs where each key is associated with a value. dictionary are used to store multiple items in a single variable. To separate two items, you use a comma ( , ) . A dictionary is like a list except that it uses parentheses { key : value } .

# They are Immutable
# A set doesn’t allow duplicate elements
# The key cannot be changed
# This program demonstrates the usage of dictionaries in Python. A dictionary is a collection of key-value pairs, where each key is unique. Initially, a dictionary 'user' is created with key-value pairs of user's name, age, and marital status.

# The print statements show the dictionary, its type and the values corresponding to the keys "name" and "age".
# The keys() method returns the keys of the dictionary, and the values() method returns the values of the dictionary.
# The items() method returns a view of the dictionary's key-value pairs.
# For loops are used to iterate over the keys, values and items of the dictionary and print them.
# The in keyword is used to check if the "gender" key is present in the dictionary.
# The dictionary values can be updated using the update() method and the [] operator.
# The pop() method is used to remove the key-value pair with the given key, and the clear() method is used to remove all key-value pairs from the dictionary.
# Another dictionary 'users' is created that contains two dictionaries - 'user1' and 'user2' - as its values.

# The for loop is used to iterate over the keys of the dictionary, 'users', and print the values of the key "name" of each dictionary 'user1' and 'user2'.



# 1
user = {
    "name" : "Shanmugavel",
    "age" : 20,
    "isMarried" : False
}

print(user)
print(type(user))
print(user["name"])
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items())

for x in user:
    print(x," ",user[x])

for x in user.values():
    print(x)

for x in user.keys():
    print(x)

for x,y in user.items():
    print(x,y)

if "age" in user:
    print("Present")

if "gender" in user:
    print("Present")

# 2
# Changing Values
user.update({"gender" : "male"})
print(user)
user["age"] = 25
print(user)
user.pop("age")
print(user)
user.clear()
print(user)

# 3
