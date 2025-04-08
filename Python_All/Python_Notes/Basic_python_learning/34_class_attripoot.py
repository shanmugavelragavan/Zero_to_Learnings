# Class Attributes in Python

# Class attributes belong to the class itself they will be shared by all the instances. Such attributes are defined in the class body parts usually at the top, for legibility.

#   1. getattr ( object , name [ , default ] )

# object => object whose named attribute's value is to be returned
# name => string that contains the attribute's name
# default ( Optional ) => The value is returned when the named attribute is not found
#   2. setattr( object , name , value )
# object => object whose named attribute value is to be assigning.
# name => The assigned variable name
# default => The assigned variable value.
#   3. delattr( object , name )
# object => object whose named attribute value is to be removed.
# name => The attribute which is to be removed.
# This code is defining a class called Student with two class attributes, name and age. The values of these attributes are "Ram Kumar" and 25 respectively.

# The getattr() method is used to access the value of a class attribute. It takes the class name and the attribute name as arguments.
# If the attribute does not exist, it returns an error. However, you can provide a default value as the third argument, which will be returned if the attribute is not found.
# In the code, getattr(Student, 'name') returns the value of the name attribute, which is "Ram Kumar". The getattr(Student, 'gender', 'No Such Attribute Found') returns 'No Such Attribute Found' as the gender attribute is not present in the class.
# The class attributes can also be accessed using the dot notation, like Student.name and Student.age.
# The setattr() method is used to change the value of a class attribute. It takes the class name, the attribute name, and the new value as arguments.
# If the attribute does not exist, it creates a new attribute with the given value. In the code, setattr(Student, 'name', 'Tutor Joes') changes the value of the name attribute to "Tutor Joes".
# We can also create new attribute to class by using the dot notation, like Student.city = "Salem"
# The __dict__ attribute is a dictionary that contains the class and its attributes and methods. By using this we can check the attributes and methods of the class.
# The delattr() method is used to delete a class attribute. It takes the class name and the attribute name as arguments.
# In the code, delattr(Student,"city") deletes the city attribute from the class. And del Student.gender delete the gender attribute from the class.

class student():
    name = "Shanmugavel"
    age = 20

# getattr Method
print(getattr(student, "name"))
print(getattr(student, "age"))
print(getattr(student, "gender", "No Such Attribute Found"))

# Dot Notation
print(student.name)
print(student.age)

# Setattr
setattr(student,"name","Vel")
print(student.name)

setattr(student, "gender", "Male")
print(student.gender)

student.city = "Thanjavur"
print(student.city)

print(student.__dict__)
delattr(student,"city")
print(student.__dict__)
del student.gender
print(student.__dict__)