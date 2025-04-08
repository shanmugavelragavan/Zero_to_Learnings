# Class Method Decorator in Python

# 1. This program defines a Python class "student" with the following attributes and methods:

# . count attribute: This is a class attribute that is shared by all objects of the class. It is initialized to 0.
# . __init__ method: This method is called when an object of the class is created. It initializes the name and age attributes with the passed values, and increments the count class attribute by 1 each time a new object is created.
# . printDetail method: This method prints the values of the name and age attributes.
# . total method: This method is a class method and returns the value of the count attribute, which keeps track of the total number of objects created.

# 2. The program then creates two objects o and a of the "student" class, passing the respective name and age as arguments. The printDetail method is then called on each object to print their details. Finally, the value of the count attribute is accessed using both the class name and an object reference, which returns the same result.

# Class Method Decorator

class student:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.count +=1

    def printDetail(self):
        print("Name : ",self.name," Age : ",self.age)
    
    @classmethod
    def total(cls):
        return cls.count

o = student("Shanmugavel",20)
o.printDetail()
print("Total Admission : ",o.total())
o = student("Vel",19)
o.printDetail()

print("Total Admission : ",student.total())