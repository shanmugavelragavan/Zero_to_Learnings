# Membership operators in Python

# Membership operators are used to test if a sequence is presented in an object. The use membership operators to check whether a value or variable exists in a sequence (string, list, tuples, sets, dictionary) or not. They are two membership python operators in and not in. The in Operator is checks if a value is a member of a sequence. The not in Operator is checks if a value is not a member of a sequence.

# The program checks if the value 22 is present in the list a and if it's not present in the list a. The in operator returns True if the element is present in the list and False if it's not. The not in operator returns True if the element is not present in the list and False if it's present.

# In this case, the output of print(22 in a) is False, as 22 is not present in the list a.
# The output of print(22 not in a) is True, as 22 is not present in the list a.


# 1
a = [10,25,45,88]
print(45 in a)
print(22 not in a)