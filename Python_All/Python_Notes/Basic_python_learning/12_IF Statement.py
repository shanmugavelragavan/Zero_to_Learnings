# IF Statement in Python
# 1. The if statement is the most basic of all the control flow statements. It tells your program to execute a certain section of code only if a particular test evaluates to true. The if statement is written with the if keyword.

#   Syntax :
#         if ( condition ) :
#                // body of the statements will execute if the condition is true

# 2. This program is a simple implementation of an "if-else" statement in Python to check whether a given number is even or odd.

# n = int(input("Enter The Number : ")) - This line takes the input from the user and converts it to an integer.
# if n % 2 == 0: - The "if" statement checks if the value of n divided by 2 has a remainder of 0. If it's true, the following indented block of code is executed.
# print(n, " is Even Number") - If the condition in the if statement is true, this line will print the message "n is Even Number".

# 3. The program checks if the given number is even or odd by checking if it's divisible by 2 (i.e. n % 2 == 0), and if it is, the program outputs the message "n is Even Number".

# 1 
n = int(input("Enter The Number : "))
if n % 2 == 0:
    print(n,"Is Even Number")