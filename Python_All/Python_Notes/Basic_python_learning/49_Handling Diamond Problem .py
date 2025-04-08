# Handling Diamond Problem in Python

# 1. The diamond problem occurs when two classes have a common parent class, and another class has both those classes as base classes. The diamond problem is the generally used term for an ambiguity that arises when two classes B and C inherit from a superclass A, and another class D inherits from both B and C.

# 2. This program is an example of inheritance in Python. It defines four classes: A, B, C, and D. Class B and Class C inherit from Class A, and Class D inherits from both Class B and Class C.

# 3. Class A has a method display that prints "I am the display of Class A". Class B and Class C both override the display method and have their own implementation that prints "I am the display of Class B" and "I am the display of Class C", respectively.

# 4. Finally, a class D object "o" is created and the display method is called on it. Since Class D has its own implementation of the display method, it will override the implementations in Class B and Class C, and print "I am the display of Class D".


class A:
    def display(self):
        print("I am the display of Class A")
 
 
class B(A):
    def display(self):
        print("I am the display of Class B")
 
 
class C(A):
    def display(self):
        print("I am the display of Class C")
 
 
class D(B, C):
    def display(self):
        print("I am the display of Class D")
 
 
o = D()
o.display()
 
 