# Tuple in Python
# Tuple are used to store multiple items in a single variable.To separate two items, you use a comma ( , ) . A tuple is like a list except that it uses parentheses ( ) . Once you define a tuple, you can access an individual element by its index. A tuple is a collection of objects which ordered and immutable, you cannot change its elements. Tuples are sequences, just like lists.

# This program demonstrates the usage of tuples in Python. A tuple is a collection of ordered and immutable elements, that are enclosed within parentheses. The elements in a tuple can be of different data types.

# The first line creates a tuple and assigns it to the variable 'a'. Then, the program prints the tuple and its type, which is <class 'tuple'>.
# The next lines show how to access the elements of the tuple using indexing and slicing, just like in lists.
# The next lines convert the tuple to a list and append an element to it, then converts the list back to a tuple.
# The for loop iterates through the elements of the tuple and the if-else statement checks if a certain element is present in the tuple.
# The len() function is also used to get the length of the tuple.
# The next lines show how to concatenate and repeat tuples using the + and * operators respectively.
# The program also demonstrates how to use the count() and index() methods, which are also available for tuples as well as lists. It also shows how to use the min() and max() functions on tuple.


# Tuple in Python
# Immutable
# Surrounded by Round Brackets (1,1,5)

# 1
a = (1, 2.5, True, "Ram")
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
b = list(a)
print(b)
b.append("Raja")
print(b)
print(type(b))
a = tuple(b)
print(a)
print(type(a))

for i in a:
    print(i)

if "Raj" in a:
    print("Raja is Found")
else:
    print("Not Found")
print(len(a))

# 2
a = (1,)
print(type(a))
del a
a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
c = a + b
print(c)
print(c.count(7))

# 3
a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
c = (a, b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])
x = ('vel',) * 10
print(x)

# 4
a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
print(min(b))
print(max(a))