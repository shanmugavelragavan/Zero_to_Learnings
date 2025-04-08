# Single Inheritance in Python

# Single Inheritance in Python refers to a situation where a derived class inherits from a single base class. The derived class inherits all the attributes and methods of the base class and can also have additional attributes and methods of its own. This is the simplest form of inheritance, where a child class inherits from one parent class. The child class can access all the public and protected methods and attributes of the parent class.

#   Syntax :
#          class base1 :
#               body of base class
#          class derived( base1) :
#               body of derived class

# This program defines two classes, Nokia and Nokia1100. The Nokia class contains two class-level attributes, company and website, and a method contact_details which prints the company's address. The Nokia1100 class is a subclass of the Nokia class, and it contains two instance-level attributes, name and year, and a method product_details which prints the product details.

# An object of the Nokia1100 class is created and referred to by the name mobile. The product_details and contact_details methods are called on the mobile object, printing the product details and company's address, respectively.


class Nokia:
    company = "Nokia India"
    webiste = "www.nokia-india.com"
    
    def contact_details(self):
        print("Address : Cherry Road,Near By Bus Stand, Chennai")

class Nokia1100(Nokia):
    def __init__(self):
        self.name = "Nokia 1100"
        self.year = 1998

    def product_details(self):
        print("Name    : ",self.name)
        print("Year    : ",self.year)
        print("Company : ",self.company)
        print("Website : ",self.webiste)

mobile = Nokia1100()
mobile.product_details()
mobile.contact_details()
