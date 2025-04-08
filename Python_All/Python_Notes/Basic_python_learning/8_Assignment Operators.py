# Assignment Operators in Python

# 1. Assignment operators are used to assigning value to a variable. The left side operand of the assignment operator is a variable and right side operand of the assignment operator is a value. This operator is used to assign the value on the right to the variable on the left


# 2. Compound Operator	Sample Expression	Expanded Form

# +=	a+=2	a=a+2
# -=	a-=6	a=a-6
# *=	a*=7	a=a*7
# /=	a/=4	a=a/4
# %=	a%=9	a=a%9
# **=	a**=3	a=a**3
# //=	a//=2	a=a//2

# 3. This program is using the assignment operators along with the basic arithmetic operations in python

# . a = 125: This line assigns the value 125 to the variable a.
# . print(a): This line prints the value of a which is 125.
# . a += 5: This line uses the shorthand assignment operator += to add 5 to the current value of a and assigns the result back to a. The value of a becomes 130.
# . print(a): This line prints the updated value of a which is 130.
# . a -= 10: This line uses the shorthand assignment operator -= to subtract 10 from the current value of a and assigns the result back to a. The value of a becomes 120.
# . print(a): This line prints the updated value of a which is 120.
# . a *= 10: This line uses the shorthand assignment operator *= to multiply the current value of a by 10 and assigns the result back to a. The value of a becomes 1200.
# . print(a): This line prints the updated value of a which is 1200.
# . a /= 10: This line uses the shorthand assignment operator /= to divide the current value of a by 10 and assigns the result back to a. The value of a becomes 120.
# . print(a): This line prints the updated value of a which is 120.
# . a %= 10: This line uses the shorthand assignment operator %= to find the remainder when dividing the current value of a by 10 and assigns the result back to a. The value of a becomes 0.0.
# . print(a): This line prints the updated value of a which is 0.0.
# . a **=10: This line uses the shorthand assignment operator **= to raise the current value of a to the power of 10 and assigns the result back to a. The value of a becomes 0.0.
# . print(a): This line prints the updated value of a which is 0.0.
# . a //= 10: This line uses the shorthand assignment operator //= to divide the current value of a by 10 and assigns the result rounded down to the nearest integer back to a. The value of a becomes 0.0.
# . print(a): This line prints the updated value of a which is 0.0.

# Assignment Operators
"""
=   Assignment
+=	Addition
-=	Subtraction
*=	Multiplication
/=	Division
%=	Modulus
**=	Exponentiation
//=	Floor division
"""

# 1
a = 125
print(a)
a += 5  # a=a+5
print(a)
a -= 10  # a=a-10
print(a)
a *= 10  # a=a*10
print(a)
a /= 10
print(a)
a %= 10
print(a)
a **=10
print(a)
a //= 10 
print(a)

