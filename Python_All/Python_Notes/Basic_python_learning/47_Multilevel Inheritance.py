# Multilevel Inheritance in Python

# 1.Multilevel Inheritance is a mechanism in object-oriented programming where a class inherits from another class, which in turn inherits from another class. This process continues until the topmost class is reached. In this way, inheritance relationships form a hierarchy of classes, with the base class being at the top, and the derived classes being at the bottom. The derived class inherits the attributes and behavior of the class it inherits from and can also add new attributes and behavior to those inherited.

#   Syntax :
#          class base1 :
#                   body of base class
#          class derived1( base1 ) :
#                   body of derived class
#          class derived2( derived1 ) :
#                   body of derived class

# 2. This code demonstrates multilevel inheritance in Python, where a derived class (Son) inherits from a base class (Father), and the base class (Father) in turn inherits from another base class (GrandFather). The class Son is able to access the methods ownHouse and ownBike from GrandFather and Father classes respectively. The class Son also has its own method ownBook.


# Multilevel Inheritance
 
class GrandFather:
    def ownHouse(self):
        print("Grandpa House")
 
 
class Father(GrandFather):
    def ownBike(self):
        print("Father's Bike")
 
 
class Son(Father):
    def ownBook(self):
        print("Son Have a Book")
 
 
o = Son()
o.ownHouse()
o.ownBike()
o.ownBook()
