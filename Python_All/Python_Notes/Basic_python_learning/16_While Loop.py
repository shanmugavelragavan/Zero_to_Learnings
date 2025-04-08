# While Loop in Python

# 1. The while loop is repeats a statement or block while its controlling expression is true.The condition can be any Boolean expression. The body of the loop will be executed as long as the conditional expression is true. When condition becomes false, control passes to the next line of code immediately following the loop.

# . If the condition to true, the code inside the while loop is executed.
# . The condition is evaluated again.
# . This process continues until the condition is false.
# . When the condition to false, the loop stops.

#     Syntax:
#       while ( Condition ) :
#           // body of statement

# 2. The first while loop in the code you provided will continue to execute and print the numbers from 1 to 10. It initializes the variable i to 1 and then uses the while loop to check if i is less than or equal to 10. If the condition is true, it prints the current value of i and then increments the value of i by 1. This process will repeat until i is no longer less than or equal to 10, at which point the while loop will exit.

# 3. The second while loop in the code is designed to print the even numbers from 2 to 20. It initializes the variable i to 2, and the variable n to 20. Then, it uses the while loop to check if i is less than or equal to 20. If the condition is true, it prints the current value of i and then increments the value of i by 2. This process will repeat until i is no longer less than or equal to 20, at which point the while loop will exit.

# While Loop
"""
1.While Loop
2.For Loop
"""

# 1
i = 1
while i <= 10:
    print(i)
    i += 1

print("--------------------------------")

# 2
print("Even Numbers : ")

num = 20
i = 2
while i <= 20:
    print(i)
    i += 2