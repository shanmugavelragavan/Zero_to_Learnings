# Break using While Loop in Python

# 1. The break statements are your way of asking the loop to stop and execute the next statement. When a break statement is encountered inside a loop, the loop is immediately terminated and the program control resumes at the next statement following the loop

# 2. This program is a Python script that uses a while loop to iterate over the numbers from 1 to 20, but it exits the loop when the number 7 is encountered.

# . It starts by initializing a variable i to 1, which is used as the counter for the while loop. The while loop then runs as long as the value of i is less than or equal to 20.
# . Inside the while loop, there is an if statement that checks whether the value of i is equal to 7 using the comparison operator ==. If the value is 7, it means that the number is 7 and the program will exit the loop using the break statement.
# . The break statement is used to exit a loop prematurely. When the break statement is encountered inside a loop, the loop is immediately terminated and the program continues with the next statement following the loop.
# . If the value of i is not equal to 7, it means that the number is not 7, and the program will print the current value of i and then increments the value of i by 1.
# . This process will repeat until i is no longer less than or equal to 20, or until i is equal to 7 at which point the while loop will exit using the break statement and the program will end.
# . So the program is using a while loop to iterate over the numbers from 1 to 20, and using an if statement with break statement to check whether the number is 7 or not. When the number is 7, the while loop exits and the program ends.


# Break Statement

# 1

i = 1
while i <= 20:
    if i == 7:
        break
    print(i)
    i += 1











