# Bitwise Operators in Python

# 1. In Python, bitwise operators are used to perform bitwise calculations on integers. The integers are first converted into binary and then operations are performed on bit by bit, hence the name bitwise operators. Then the result is returned in decimal format. Bitwise AND operator: Returns 1 if both the bits are 1 else 0

# Operator	Description
# &	Bitwise AND
# |	Bitwise OR
# ^	Bitwise XOR
# ~	Bitwise NOT
# <<	Left shift
# >>	Right shift

# This program uses bitwise operations in Python.

# . a & b: The "&" operator performs a bitwise AND operation, resulting in the value 9 (binary representation of 25 is 11001 and 45 is 101101, so the AND operation is 100001 which is 9 in decimal).
# . a | b: The "|" operator performs a bitwise OR operation, resulting in the value 61 (binary representation of 25 is 11001 and 45 is 101101, so the OR operation is 111101 which is 61 in decimal).
# . a ^ b: The "^" operator performs a bitwise XOR operation, resulting in the value 52 (binary representation of 25 is 11001 and 45 is 101101, so the XOR operation is 010100 which is 52 in decimal).
# . ~a: The "~" operator performs a bitwise NOT operation, resulting in the value -26 (in binary, the NOT of 11001 is 00110, which is -26 in two's complement).
# . a << 2: The "<<" operator performs a bitwise left shift operation, resulting in 100 (the binary representation of 25 is 11001, so the left shift operation is 100100 which is 100 in decimal).
# . a >> 2: The ">>" operator performs a bitwise right shift operation, resulting in 6 (the binary representation of 25 is 11001, so the right shift operation is 00110 which is 6 in decimal)

# Bitwise Operators
"""
& 	AND
|	OR
^	XOR
~ 	NOT
<<	Zero fill left shift
>>	Signed right shift
"""

# 1
a = 25
b = 45
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 2)
print(a >> 2)