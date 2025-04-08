# While Else and For Else in Python

# Else block will be executed only if the loop isn't terminated by a break statement. The else clause executes after the loop completes normally. This means that the loop did not encounter a break statement. They are really useful once you understand where to use them.

# This program demonstrates the use of the else block in both while loops and for loops in Python.

# The first block of code is a while loop that starts with the variable "i" equal to 1 and continues to run until "i" is no longer less than or equal to 5. The loop prints the value of "i" on each iteration, and then increments "i" by 1. After the while loop completes its iterations, the else block is executed and prints the message "Loop Completed".

# The second block of code is a for loop that uses the range() function to iterate over the numbers from 1 to 20. On each iteration, the value of the iterator variable "i" is printed. After the for loop completes its iterations, the else block is executed and prints the message "For Loop Completed".


# Both While and for loop checks for the condition inside the loop and runs the loop until the condition is true. In the given code, we don't have any condition to break the loop that's why the both loops are running completely and printing "Loop Completed" or "For Loop Completed" respectively.

# Syntax:
#    while condition :
#               while block statement
#    else :
#               else block statement

# Syntax:
#    for variable_name in sequence :
#               for block statement
#    else :
#               else block statement

# While Else & For Else

# 1
i = 1
while i <= 5:
    # if i == 4:
    #     break
    print(i)
    i += 1
else:
    print("While Loop Completed")

# 2
for i in range(1,21):
    # if i == 5:
    #     break
    print(i)
else:
    ("For Loop Completed")