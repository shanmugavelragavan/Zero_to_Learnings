# Type Casting in Python

# 1. In Python, type casting is the process of converting one data type to another. Python is a dynamically-typed language, which means that the data type of a variable can change based on the value assigned to it. However, sometimes you may need to convert a variable from one data type to another.

# 2.There are several built-in functions in Python that can be used for type casting:

# . int(): Converts a value to an integer.
# . float(): Converts a value to a floating-point number.
# . str(): Converts a value to a string.
# . bool(): Converts a value to a Boolean (True or False).

# 3. This is a simple program in Python that performs the following operations:
# . Accepts two integer inputs from the user, a and b.
# . Adds a and b and stores the result in a variable c.
# . Converts the result stored in c to a string using the str() function.
# . Prints the message "Total : " followed by the result stored in c.
# 4. In this program, the user inputs are obtained using the input() function and then cast to integers using int(). The result of the addition of a and b is then stored in c, and to display it, the c is first converted to a string using str() before it's concatenated with the string "Total : " using the + operator. Finally, the result is displayed on the screen using the print() function.

# 1.
a = 10.0
print(a)
print(type(a))

# 2.
a = 10.0
print(a)
print(type(a))
b = int(a)
print(b)
print(type(b))

# 3.
a = input("Enter The Value of A : ")
b = input("Enter The Value of B : ")
c = a + b
print("Total : "+c)
print(type(a))

# 4.
a = int(input("Enter The Value of A : "))
b = int(input("Enter The Value of B : "))
c = a + b
print("Total : ",c)
print(type(a))

# 5.
a = int(input("Enter The Value of A : "))
b = int(input("Enter The Value of B : "))
c = a + b
print("Total : "+ str(c))

