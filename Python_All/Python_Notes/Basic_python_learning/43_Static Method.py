# Static Method in Python

# 1. A static method in Python is a method that belongs to a class rather than an instance of the class. It can be called on the class itself, rather than on an instance of the class. Static methods are defined using the @staticmethod decorator, and do not have access to any class-specific state. They are typically used for utility functions that don't need to access any instance-specific data.

# 2. This code demonstrates the use of a static method in Python. A static method is a method that belongs to a class rather than an instance of the class. In the example, the welcome() method is a static method that can be called on the class itself or on an instance of the class. The @staticmethod decorator is used to define a static method. The code creates two instances of the student class, s1 and s2, and demonstrates that the welcome() method can be called on both the class and the instances.

# Static Method in Python

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printDetail(self):
        print("Name : ",self.name," Age : ",self.age)

    @staticmethod
    def welcome():
        print("Welcome to our institution")
        
s1 = student("Shanmugavel",20)
s1.printDetail()
s1.welcome()


s2 = student("Ragavan",19)
s2.printDetail()
s2.welcome()