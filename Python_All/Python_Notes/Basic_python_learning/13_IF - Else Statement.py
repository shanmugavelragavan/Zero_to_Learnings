# IF - Else Statement in Python

# 1. The if-else statement is used to execute both the true part and the false part of a given condition. If the condition is true, the if block code is executed and if the condition is false, the else block code is executed.

#   Syntax :
#         if ( condition ) :
#                // body of the statements will execute if the condition is true
#         else :
#                // body of the statements will execute if the condition is false

# 2. This program is a simple Python script that prompts the user to enter their name and age, and then checks if the entered age is greater than or equal to 18. If the age is greater than or equal to 18, the program prints a message stating that the person is eligible to vote, along with their name and age. If the age is less than 18, the program prints a message stating that the person is not eligible to vote, along with their name and age.

# 1
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
if age >= 18:
    print(name,"age is",age,"Eligible For Vote")
else:
    print(name,"age is",age,"Not Eligible For Vote")