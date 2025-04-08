# List in Python
# Lists are used to store multiple items in a single variable.To separate two items, you use a comma ( , ) . List uses the square brackets [ ]. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Sequence Type
# Element of the list can access by index
# They are mutable
# This program demonstrates various built-in functions and methods that can be used with lists in Python.

# The first block of code shows how to create a list and access its elements using indexing. It also shows how to change the value of an element in a list using indexing.
# The second block of code shows how to create a list with different data types and how to access the elements of the list and their types.
# The third block of code demonstrates how to use the clear() method to remove all elements from a list, the copy() method to create a copy of a list, the count() method to count the number of occurrences of an element in a list, the index() method to find the index of an element in a list, the len() function to find the length of a list, the max() and min() functions to find the maximum and minimum element in a list, the pop() method to remove an element from a list using an index, and the remove() method to remove an element from a list using its value.
# The fourth block of code shows how to use the append() method to add elements to a list, the extend() method to add elements from another list, and the insert() method to insert an element at a specific index in a list.
# The fifth block of code demonstrates how to use the range() function to create a list of numbers, the list() function to convert a string to a list, and the sort() method to sort the elements of a list in ascending or descending order. It also shows how to use the key parameter to sort the elements based on a specific key and the reverse parameter to sort the elements in descending order.

# List in Python
"""
Sequence Type
Mutable
a[5]
a={1,2,3,4,5}
a[0]
"""

# 1
a = [1,2,3,4,5]
print(a)
print(type(a))
a[0] = 100
print(a)
print("-----------------------------")

# 2
print("Slicing")
print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])
print("-----------------------------")

# 3
a = [1,True,"Shanmugavel",2.5,[1,2,3,4]]
print(a)
print(type(a))
print(a[0], " type is ", type(a[0]))
print(a[1], " type is ", type(a[1]))
print(a[2], " type is ", type(a[2]))
print(a[3], " type is ", type(a[3]))
print(a[4], " type is ", type(a[4]))
print(a[4][1])
print("-----------------------------")

# 4
a = [10,25,35,45]
print(a)
a.clear()
print(a)
print("-----------------------------")

# 5
a = [10,25,35,45]
b = a.copy()
print(b)
print("-----------------------------")

# 6
a = [10,25,35,45,25,58,25]
print(a.count(25))
print(a.index(25))
print(len(a))
print(max(a))
print(min(a))

print(a)
a.pop(0) # remove Elements using index
print(a) 

a = [10,25,35,45,25,58,25]
a.remove(25) # values
print(a)
print("-----------------------------")

# 7
names = ["Shanmugavel"]
print(names)
names.append("Ragavan")
names.append("Yohish")
names.append("Sri Murugan")
print(names)

names2 = ["Moorthi","Karthi"]
names.extend(names2)
print(names)

names.insert(0,"Siva")
print(names)
print("-----------------------------")

# 8
print(list(range(5)))
print(list("Shanmugavel"))

a = [50,10,100,25,87]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a = ["Orange","Apple","Banana"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a = ["Orange","Apple","Banana"]
a.sort(key=len)
print(a)