# Identity Operators in Python

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location. th operators test if the two operands share an identity. We have two identity operators is and is not. The is operators test If two operands have the same identity, it returns True. Otherwise, it returns False.

# This program is about comparing the equality of objects in Python.

# Two lists, a and b, are created with the same values [1, 2].
# A third list c is assigned the reference of a.
# The id() function is used to print the memory addresses of a, c, and b.
# The is operator is used to check if two objects are pointing to the same memory location.
# The == operator is used to check if two objects have the same values.
# The is not operator is used to check if two objects are not pointing to the same memory location.
# The != operator is used to check if two objects do not have the same values.


"""
is
is not
"""
# 1
a = [1,2]
b = [1,2]
c = a
print(id(a))
print(id(c))
print(id(b))
print(a is c)
print(a is b)
print(a == b)

print(a is not c)
print(a is not b)
print(a != b)