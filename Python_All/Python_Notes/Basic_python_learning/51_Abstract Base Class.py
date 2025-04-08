# Abstract Base Class in Python

# 1. An Abstract Base Class (ABC) in Python is a special type of class that provides an interface to define the expected behaviors of its subclasses, but cannot be instantiated on its own.

# 2. An ABC is created using the abc module, which is part of the Python Standard Library. To create an ABC, a class is derived from ABC and one or more abstract methods are declared using the @abstractmethod decorator. Subclasses of an ABC must override these abstract methods, or they too will be treated as abstract and cannot be instantiated.

# 3. ABCs are used to define a common interface for related classes, so that it is easier to write generic code that works with objects of different types, as long as they adhere to the expected interface. This can help enforce modularity and reduce code duplication, and make it easier to maintain code and add new features.

# 4. In this code, the "Bank" class is an abstract base class (ABC) which defines three abstract methods "loan", "credit" and "debit" which must be implemented by any class that inherits from it. The "HDFC" class inherits from the "Bank" class and implements all the abstract methods defined in the "Bank" class and also have a new method "card" which is specific to this class. When an instance of the "HDFC" class is created and the methods "loan", "credit" and "debit" are called on it, they will execute the specific implementation of those methods in the "HDFC" class.


from abc import ABC, abstractmethod
 
 
class Bank(ABC):
    @abstractmethod
    def loan(self): pass
 
    @abstractmethod
    def credit(self): pass
 
    @abstractmethod
    def debit(self): pass
 
class HDFC(Bank):
    def loan(self):
        print("We can Provide 7.5% Interest Loan")
 
    def credit(self):
        print("HDFC Provide Credit")
 
    def debit(self):
        print("HDFC Provide Debit")
 
    def card(self):
        print("HDFC Provide Credit Card")
o=HDFC()
o.loan()
o.credit()
o.debit()
o.card()
 
