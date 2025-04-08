# Class and Object in Python

# Python is an object oriented programming language. Almost everything in Python is an object is simply a collection of data (variables) and methods (functions) that act on those data. A Class is like an object constructor, or a "blueprint" for creating objects. You can create many objects from the same class type.

# Example :
#    A dog has states - color, name, breed as well as behaviors – wagging the tail, barking, eating. An object is an instance of a class.

# Syntax of Class:
#       class Class_Name :
#             # statements

# Example of Class:
#       class student :
#             name = " Tutor joe's "
#             age = 30


# Syntax of Object:
#       object_name = class_name ( arguments )

# Example of Object:
#       s = student ( )

# The code you provided defines a class called "car" using the class keyword, and creates an empty class using the pass statement. It then creates an object of the class car called swift.

# The type() function is used to check the type of the variable passed to it.

# print(type(a)) will print the type of variable a which is int.
# print(type(car)) will print the type of variable car which is class.
# The isinstance() function is used to check if an object is an instance of a class.

# print(isinstance(swift,car)) will print True as the object swift is an instance of the class car.
# print(isinstance(a,int)) will print True as the variable a is of type int.
# print(type(swift)) will print the type of variable swift which is car.


class car():
    pass

a = 10
print(type(a))
print(type(car))
swift = car()

print(isinstance(swift,car))
print(isinstance(a,int))
print(type(swift))