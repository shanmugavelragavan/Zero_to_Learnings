# Class Method in Python

# This code defines a class called Student with class attributes name and age and a class method printall(). The printall() method is defined within the class and it prints the values of class attributes name and age.

# Student.printall() calls the class method and prints the values of class attributes name and age.
# print(Student.__dict__) prints the class attributes and methods in a dictionary form.
# getattr(Student, "printall") gets the attribute of the class Student by the name of the attribute which is printall and returns the function definition.
# getattr(Student, "printall")() gets the attribute of the class Student by the name of the attribute which is printall and calls the function.
# Student.__dict__['printall']() gets the attribute of the class Student by the name of the attribute which is printall from the class dictionary and calls the function.
# All three ways of calling the class method printall() will print the same output which is "Name : Tutor Joes", "Age : 25"


# Class Methods

class student:
    name = "Shanmugavel"
    age = 20

    def printall():
        print("Name : ",student.name)
        print("Age : ",student.age)

student.printall()
print(student.__dict__)

print(getattr(student,"printall"))
getattr(student,"printall")()

student.__dict__["printall"]()