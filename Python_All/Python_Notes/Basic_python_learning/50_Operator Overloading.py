# Operator Overloading in Python

# 1. Operator overloading in Python is the ability to change the behavior of operators for user-defined data types. This is done by defining special methods for the operators in question. For example, the + operator can be redefined for a user-defined class to perform some specific operation. The special method that is used to overload the + operator is __add__(). Similarly, other operators like -, *, /, //, %, **, <, >, ==, != etc. can be overloaded using special methods like __sub__(), __mul__(), __truediv__(), __floordiv__(), __mod__(), __pow__(), __lt__(), __gt__(), __eq__(), __ne__() respectively.

# 2. In this code, a class named "Addition" is defined. It has an init method which initializes the attribute "a" and two special methods, add and sub. These special methods are known as magic methods or dunder methods, and they are used to overload operators in Python. The add method overloads the "+" operator, and sub method overloads the "-" operator.

# 3. When an object of the class is created, it takes a value as input, which is assigned to the attribute "a". The objects o1 and o2 are created with the values 10 and 20 respectively.

# 4. In the print statements, the "+" operator is used to add the values of the attribute "a" of the objects o1 and o2. The "-" operator is used to find the difference between the values of the attribute "a" of the objects o1 and o22. Since the operators are overloaded using the add and sub methods, these methods get called when the operators are used. The result is the sum and difference of the values of the attribute "a" of the objects o1 and o2 respectively.


"""
a = 10
b = 20
print(a + b)
 
a = "Shanmuga"
b = "Vel"
print(a + b)
 
"""
 
 
class Addition:
    def __init__(self, a):
        self.a = a
 
    def __add__(o1, o2):
        return o1.a + o2.a
 
    def __sub__(o1, o2):
        return o1.a - o2.a
 
 
o1 = Addition(10)
o2 = Addition(20)
 
print("Total      : ", (o1 + o2))
print("Difference : ", (o1 - o2))
 
"""
Operator	Magic Method
+	__add__(self, other)
-	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
 
Comparison Operators :
Operator	Magic Method
<	__LT__(SELF, OTHER)
>	__GT__(SELF, OTHER)
<=	__LE__(SELF, OTHER)
>=	__GE__(SELF, OTHER)
==	__EQ__(SELF, OTHER)
!=	__NE__(SELF, OTHER)
 
Assignment Operators :
Operator	Magic Method
-=	__ISUB__(SELF, OTHER)
+=	__IADD__(SELF, OTHER)
*=	__IMUL__(SELF, OTHER)
/=	__IDIV__(SELF, OTHER)
//=	__IFLOORDIV__(SELF, OTHER)
%=	__IMOD__(SELF, OTHER)
**=	__IPOW__(SELF, OTHER)
>>=	__IRSHIFT__(SELF, OTHER)
<<=	__ILSHIFT__(SELF, OTHER)
&=	__IAND__(SELF, OTHER)
|=	__IOR__(SELF, OTHER)
^=	__IXOR__(SELF, OTHER)
 
Unary Operators :
Operator	Magic Method
-	__NEG__(SELF, OTHER)
+	__POS__(SELF, OTHER)
~	__INVERT__(SELF, OTHER)
 
"""
