# Range in Python

# 1. The program is a Python script that demonstrates the use of the built-in range() function.

# . The range() function creates an iterator that generates a sequence of numbers within a given range.
# . In the first line, range(5) creates an iterator that generates a sequence of numbers from 0 (inclusive) to 5 (exclusive). The list() function is used to convert the iterator to a list, so the output is [0, 1, 2, 3, 4].
# . In the second line, range(2, 5) creates an iterator that generates a sequence of numbers from 2 (inclusive) to 5 (exclusive). The output is [2, 3, 4].
# . In the third line, range(0, 21, 2) creates an iterator that generates a sequence of numbers from 0 (inclusive) to 21 (exclusive) with a step of 2. The output is [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20].
# . In the fourth line, range(1, 20, 2) creates an iterator that generates a sequence of numbers from 1 (inclusive) to 20 (exclusive) with a step of 2. The output is [1, 3, 5, 7, 9, 11, 13, 15, 17, 19].
# . So the program is using the range() function and list() function to create a range of numbers with different start, stop and step values. The range() function creates an iterator and the list() function is used to convert the iterator to a list.

# Range in Python
"""
1-5  =>1,2,3,4,5
0-5 =>2,4  +2
range(5)  =>0,1,2,3,4
range(2,5)  =>
"""

# 1
print(list(range(5)))
print(list(range(2, 5)))  # n-1
print(list(range(0, 21, 2)))
print(list(range(1, 20, 2)))
