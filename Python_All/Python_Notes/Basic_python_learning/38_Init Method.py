# Init Method in Python

# 1.The __init__ method, also known as the constructor method, is a special method in Python classes that gets called automatically when a new instance of the class is created. The __init__ method is used to initialize the attributes of the class and set them to the default values.

# 2. This is a Python program defining a class named "user". The class has a constructor method __init__ that takes a name parameter and sets it as an instance variable "self.name". The class also has a method printall that prints the instance variable "self.name".

# 3. Two instances of the class, o1 and o2, are created with the names "Tutor Joes" and "Joes" respectively. The printall method is called on each instance to print its name, and the __dict__ attribute is printed to show the instance variables and their values.

# 4. Finally, the __dict__ attribute of the class itself is printed to show the class variables and their values, if any.

# init method

class user:
    def __init__(self,name):
        print("Call When new Instance Created")
        self.name = name

    def printall(self):
        print("Name : ",self.name)

o1 = user("Shanmugavel")
o1.printall()
print(o1.__dict__)
o2 = user("Vel")
o2.printall()
print(o2.__dict__)
print(user.__dict__)