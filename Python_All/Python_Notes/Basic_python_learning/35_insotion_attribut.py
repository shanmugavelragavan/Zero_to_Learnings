# Instance Attributes in Python

# A class is a blueprint for the creation of different objects. When the objects get created to form the class, they no longer depend on the class attribute. Also, the class has no control over the attributes of the instances created.

# Syntax of Object:
#       object_name = class_name ( arguments )

# Example of Object:
#       s = student ( )

# The code is defining a class called user with one class attribute, course with value Java. The user.__dict__ is a dictionary that contains the class and its attributes and methods. It will print the class attribute course in the form of dictionary.

# user.course is used to access the class attribute value which is Java.
# o = user() creates an object o of the class user. o.__dict__ will print an empty dictionary because the object o does not have any instance attribute.
# o.course will print the class attribute value which is Java.
# o.course = "C++" will change the value of class attribute to C++ for object o .
# o.__dict__ will print the dictionary with class attribute course with value C++.
# o2 = user() creates another object o2 of the class user. o2.course will print the class attribute value which is Java because object o2 does not have any instance attribute to change the class attribute value.


class user:
    course = "Python"

o = user()
print(user.__dict__)
print(user.course) # Print Class Attribute
print(o.__dict__)
print(o.course)
o.course = "C++"
print(o.__dict__)
print(o.course)

o2 = user()
print(o2.course)