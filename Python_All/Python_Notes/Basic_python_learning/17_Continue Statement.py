# Continue using While Loop in Python

# 1. The continue statement instructs a loop to continue to the next iteration. The continue statement is used to skip the remaining statements of the current loop and go to the next iteration.

# 2. This program is a Python script that uses a while loop to iterate over the numbers from 1 to 20, and prints only the odd numbers.

# . It starts by initializing a variable i to 1, which is used as the counter for the while loop. The while loop then runs as long as the value of i is less than or equal to 20.
# . Inside the while loop, there is an if statement that checks whether the remainder of i divided by 2 is equal to 0 using the modulo operator %. If the remainder is 0, it means that the number is even and the program will continue to the next iteration using the continue statement.
# . The continue statement causes the program to skip the rest of the code in the current iteration of the loop, and move on to the next iteration.
# . If the remainder is not 0, it means that the number is odd, and the program will print the current value of i and then increments the value of i by 1.
# . This process will repeat until i is no longer less than or equal to 20, at which point the while loop will exit and the program will end.
# . So the program is using a while loop to iterate over the numbers from 1 to 20, and using an if statement to check whether each number is even or odd. The program is only printing the odd numbers and skipping the even numbers using continue statement.


# Continue Statement

# 1
i = 1
while i <= 20:
    if i % 2 == 0:
        i = i + 1
        continue;
    print(i)
    i += 1








