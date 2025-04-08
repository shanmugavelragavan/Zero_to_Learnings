# Property Decorator in Python

# 1. Python @property is one of the built-in decorators. The main purpose of any decorator is to change your class methods or attributes. A decorator feature in Python wraps in a function, appends several functionalities to existing code and then returns it. Methods and functions are known to be callable as they can be called. Therefore, a decorator is also a callable that returns callable. @property decorator in Python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property().

# 2. This is a Python program that defines a class named "user". The class has a constructor method __init__ that takes two parameters, "name" and "age", and sets them as instance variables "self.name" and "self.age" respectively.

# 3. The class also has a property method "msg" decorated with @property. This method returns a string that combines the name and age of the instance as "name is age years old".

# 4. An instance of the class named "o" is created with the name "Tutor Joes" and age 25. The values of the instance variables "name", "age", and "msg" are printed using dot notation. Then, the value of the "age" instance variable is changed to 45 and the "msg" property is printed again, showing the updated value.

# Property Decorator
 
class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # self.msg = self.name + " is " + str(self.age) + " years old"
    
    @property
    def msg(self):
        return self.name + " is " + str(self.age) + " years old"

o = user("Shanmugavel",20)
print(o.name)
print(o.age)
print(o.msg)
o.age = 21
print(o.msg)

















