# Elif Statement in Python

# 1. The elif condition is used to multiple conditional expressions after the if condition or between the if and else conditions. The elif block is executed if the specified condition evaluates to True.

#   Syntax :
#         if ( condition 1 ) :
#                // body of the statements will execute if the condition1 is true
#         elif ( condition 2 ) :
#                // body of the statements will execute if the condition2 is true
#         .
#         .
#         else :
#                // body of the statements will execute if the condition1 is false condition2 is False

# 2. This program is a Python script that prompts the user to enter a number of days and then calculates a fine based on that number.

# . It starts by using the input() function to ask the user to enter a number of days, which is stored in the "days" variable.
# . Then, the program uses an if-elif block to check the value of the "days" variable against a series of conditions.
# . If the value of "days" is equal to 0, the program prints "Good No Fine"
# . If the value of "days" is greater than or equal to 1 and less than or equal to 5, the program calculates the fine as 0.5 * days and prints the fine amount
# . If the value of "days" is greater than 5 and less than or equal to 10, the program calculates the fine as 1 * days and prints the fine amount
# . If the value of "days" is greater than 10 and less than or equal to 30, the program calculates the fine as 5 * days and prints the fine amount
# . If none of the above conditions are met, the program will print "Membership Cancel"

# 3.  So the program is checking the number of days and based on the number of days it is calculating the fine.

# elif Statement in Python
"""
0       No Fine
1-5     0.5
5-10    1
10-30   5
>30     Membership Cancel
"""

# 1
days = int(input("Enter The Days : "))
if days == 0:
    print("Good No Fine")
elif days >= 1 and days <= 5:
    print("Fine Amount : ", days * 0.5)
elif days > 5 and days <= 10:
    print("Fine Amount : ", days * 1)
elif days > 10 and days <= 30:
    print("Fine Amount : ", days * 5)
else:
    print("Membership Cancel")