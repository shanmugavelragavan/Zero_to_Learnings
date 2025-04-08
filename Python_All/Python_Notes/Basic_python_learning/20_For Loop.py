# For Loop in Python

# 1. The for loop is used to repeat a specific block of code which you want to repeat a fixed number of times. The for loop is a control flow statement that is used to repeatedly execute a group of statements as long as the condition is satisfied.

# Syntax:
#    for variable_name in sequence :
#               body of loop

# 2. This program is a Python script that demonstrates the use of the for loop and the built-in range() function.

# . The first for loop uses the range() function to create an iterator that generates a sequence of numbers from 0 (inclusive) to 21 (exclusive) with a step of 2. The for loop iterates over the numbers in the sequence and prints each one to the screen.
# . The second for loop uses the range() function to create an iterator that generates a sequence of numbers from 0 to 4. The for loop iterates five times, each time prompting the user to input a number using the built-in input() function.
# . The values entered by the user are stored in variables a and b, and then the program print the sum of a and b as output. So the program is using the for loop and the range() function to iterate over a sequence of numbers and for each iteration, it prompts the user to enter two numbers and print the sum of those numbers.
# . The first for loop iterates over a sequence of even numbers and the second for loop iterates 5 times and each iteration it prompts user to enter two numbers.


# 1
for i in range(20):
    print(i)

# 2
for i in range(1,21):
    print(i)

# 3
for i in range(5):
    a=int(input("Enter a No : "))
    b=int(input("Enter a No : "))
    print(a + b)