# Math Functions in Python

# The Python Math Library provides us access to some common math functions and constants in Python. The math module is used to access mathematical functions in the Python. Some of the most popular mathematical functions are defined in the math module. All methods of this functions are used for integer or real type objects, not for complex numbers.

# sqrt ( ) => The square root of the argument
# ceil ( ) => Rounds float value up to an integer value
# floor ( ) => Rounds float value down to an integer value
# fabs ( ) => Value is return to the absolute ( positive ) value
# pow ( ) => Returns the value of the first parameter raised to the second parameter
# factorial ( ) => Returns the factorial of a number
# The code you provided will perform the following operations when executed:

# math.sqrt(4): This will return the square root of 4, which is 2.0
# math.ceil(1.55555): This will round up the decimal number 1.55555 to the nearest integer, which is 2
# math.floor(1.55555): This will round down the decimal number 1.55555 to the nearest integer, which is 1
# math.factorial(5): This will return the factorial of 5, which is 120 (5! = 5 x 4 x 3 x 2 x 1)
# math.fabs(-5): This will return the absolute value of -5, which is 5
# math.pow(2, 3): This will raise 2 to the power of 3, which is 8
# math.log2(2): This will return the logarithm of 2 to the base 2, which is 1.0
# math.log10(2): This will return the logarithm of 2 to the base 10, which is approximately 0.30103
# math.pi: This will return the value of pi (π), which is approximately 3.14159
# math.e: This will return the value of Euler's number (e), which is approximately 2.71828

import math

print(math.sqrt(4))
print(math.ceil(1.55555))
print(math.floor(1.55555))
# 5! => 1*2*3*4*5
print(math.factorial(5))
print(math.fabs(-5))
print(math.pow(2, 3))
print(math.log2(2))
print(math.log10(2))
print(math.pi)
print(math.e)
