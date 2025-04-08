# Logical Operators in Python

# 1. Logical operators are used to combine multiple conditions in a single expression in Python. The three logical operators in Python are and, or, and not.

# . and: This operator returns True if both the conditions on either side of the operator are True, otherwise it returns False.
# . or: This operator returns True if either of the conditions on either side of the operator is True, otherwise it returns False.
# . not: This operator inverts the truth value of a single condition. If a condition is True, the not operator will make it False and vice versa.

# This program is using logical operators in Python to check if the value of a variable a falls within a certain range.

# . a = 25: This line assigns the value 25 to the variable a.
# . print(a >= 10 and a <= 20): This line uses the logical operator and to check if the value of a is greater than or equal to 10 AND less than or equal to 20. Since 25 is not in the range 10 to 20, the output will be False.
# . print(a >= 10 or a <= 20): This line uses the logical operator or to check if the value of a is greater than or equal to 10 OR less than or equal to 20. Since 25 is greater than 10 the output will be true
# . print(not(a >= 10 and a <= 20)): This line uses the logical operator not to check if the value of a is not in the range of 10 to 20. The output will be True because 25 is not in the range 10 to 20.

# Logical Operators in Python
"""
and 
or 
not 
"""

# 1
a = 25
print(a >= 10 and a <= 20)
print(a >= 10 or a <= 20)
print(not(a >=  10 and a <= 20))