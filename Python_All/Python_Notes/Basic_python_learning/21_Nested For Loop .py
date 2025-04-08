# Nested For Loop in Python

# 1. The nested loop refers to a loop within a loop, an inner loop within the body of an outer one. Nested loops are useful when for each pass through the outer loop, you need to repeat some action on the elements in the outer loop. The nested loop is a one iteration of the outer loop is first executed, after which the inner loop is executed. The execution of the inner loop continues till the condition described in the inner loop is satisfied.

# Syntax:
#    // outer for loop
#    for variable_name in sequence :
#              // inner for loop
#               for variable_name in sequence :
#                     // body of loop

# 2. This program is a Python script that demonstrates the use of nested for loops and the built-in range() function.

# 3. The program contains three main parts, each one using a different approach to accomplish different tasks.

# . In the first part of the program, there is a nested for loop where the outer loop uses the range() function to create an iterator that generates a sequence of numbers from 0 to 5. The inner for loop uses the same function to create an iterator that generates a sequence of numbers from 0 to the current value of the outer loop variable. The inner loop prints an asterisk character (*) for each value of the inner loop variable. The inner print statement uses the end parameter to specify that no newline character should be added after the asterisk. As a result, the program prints a right-angled triangle pattern of asterisks.
# . In the second part of the program, there is another nested for loop where the outer loop uses the range() function to create an iterator that generates a sequence of numbers from 5 to 1 with a step of -1. The inner for loop uses the same function to create an iterator that generates a sequence of numbers from 0 to the current value of the outer loop variable. As in the first part, the inner loop prints an asterisk character (*) for each value of the inner loop variable. The inner print statement uses the end parameter to specify that no newline character should be added after the asterisk. As a result, the program prints another right-angled triangle pattern of asterisks, but this time in reverse order.
# . In the third part of the program, there is another nested for loop where the outer loop uses the range() function to create an iterator that generates a sequence of numbers from 65 to 69. The inner for loop uses the same function to create an iterator that generates a sequence of numbers from 65 to 69. The inner loop prints a character represented by the ASCII code of the current value of the inner loop variable using the built-in chr() function. The inner print statement uses the end parameter to specify that no newline character should be added after the character. As a result, the program prints a matrix of 5x5 containing the characters A, B, C, D and E.

# Nested For Loop
"""
*
**
***
****
*****

*****
****
***
**
*

ABCDE
ABCDE
ABCDE
ABCDE
ABCDE

A-Z => 65-90
a-z=> 97-122

"""

# 1
for i in range(5):
    for j in range(i):
        print("*",end="")
    print("")

print("-----------------------------")

# 2
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

print("-----------------------------")

# 3
for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")