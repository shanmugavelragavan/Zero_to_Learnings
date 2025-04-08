# Multiple Inheritance in Python

# 1. Multiple Inheritance is a feature of object-oriented programming where a class can inherit attributes and methods from multiple parent classes. In Python, a class can inherit from multiple parent classes by specifying multiple base classes in the class definition, separated by commas. The class that inherits from multiple parent classes is called a derived or child class, while the parent classes are known as base or parent classes.

#   Syntax :
#          class Parent1 :
#                   # attributes and methods of Parent1
#          class Parent2 :
#                   # attributes and methods of Parent2
#          class Child( Parent1, Parent2 ) :
#                   # attributes and methods of Child

# Multiple Inheritance
 
class Father:
    def fishing(self):
        print("Fishing in Rivers")
 
    def chess(self):
        print("Playing Chess From Father")
 
 
class Mother:
    def cooking(self):
        print("Cooking Food")
 
    def chess(self):
        print("Playing Chess From Mother")
 
 
class Son(Mother,Father):
    def ride(self):
        print("Riding Bicycle")
o = Son()
o.ride()
o.fishing()
o.cooking()
o.chess()
