# Functions in Python

# Python allows us to divide a large program into the basic building blocks known as a function. function is a group of related statements that performs a specific task. A function is a reusable block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# Two Types of Function :
#         1. User-defined Function: We can create our own function based on our requirements.
#         2. Standard Library Function: These are built-in function in python that are available to use.

# Syntax:
#    def function_name ( Parameter list ) :
#         // function block

# Return Syntax:
#      return expression

# Function Types :

# No Return Type With Argument Function
# No Return Type Without Argument Function
# Return Type Without Argument Function
# Return Type With Argument Function


def welcome():
    print("Wlcome to Shanmugavel")

welcome()

# No Return Type Without Argument Function in Python

def add():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c  = a + b
    print("Total",c)

add()

# No Return Type Without Argument Function in Python

def sub(a,b):
    c = a - b
    print("Difference : ",c)

sub(25,2)

# Return Type Without Argument Function in 
def mul():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c  = a * b
    return c

x = mul()
print("Mul : ",x)

# Return Type With Argument Function in 
def div(a,b):
    c = a / b
    return c

x = div(25,2)
print("Division : ",x)

# Arbitrary Arguments Function in Python
def class_10(*students):
    print(students)

class_10("Shanmugavel","Ragavan","Yohish","Sri Murugan","Himrish")

def class_10(*students):
    print(students)
    for user in students:
        print(user)
class_10("Shanmugavel","Ragavan","Yohish","Sri Murugan","Himrish")

# Keyword Arguments Function in Python
def massage(name,age):
    print(name,"age is ",age)

massage(age=20, name="Shanmugavel")

# Arbitrary Keyword Arguments Function in Python
def bioData(**data):
    print(data)

bioData(name="Shanmugavel",age=20,gender="Male")

# Default Parameter Function in Python
def users(name,city="Thanjavur"):
    print(name,"is from",city)

users("Shanmugavel","Chennai")
users("Ragavan")

# Passing a List as Argument in Function Pyhton
def total(marks):
    return sum(marks)

print("Total : ",total([55,78,67,123,30]))

# Recursive Function
1 * 2 * 3 * 4 * 5 = 120

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

print("Factorial : ",factorial(5))

"""
factorial(5)
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1 = 120
"""

# Lambda Function in Python
c = lambda a: a + 50
print(c(10))

c = lambda a, b: a * b
print(c(10, 25))

