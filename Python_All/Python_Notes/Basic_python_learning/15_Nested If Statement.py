# Nested If Statement in Python

# 1. Nested If Statement means to place one If inside another If Statement. Nested ifs are very common in programming. when you nest ifs, the main thing to remember is that an else statement always refers to the nearest if statement that is within the same block as the else and that is not already associated with an else.

#   Syntax:
#     if ( Expression 1 ) :
#         // Executes when the Expression 1 is true
#            if ( Expression 2 ) :
#              // Executes when the Expression 2 is true

# 2.This program is a Python script that prompts the user to enter three marks, then calculates the total and average of those marks, and then uses if-else statements to determine the result and grade based on the marks.

# . It starts by using the input() function to ask the user to enter three marks, m1, m2, and m3, which are then stored in variables. The program then calculates the total of the marks by adding the three marks and stores it in the variable 'total' and also calculates the average of the marks by dividing total with 3.0 and stores it in the variable 'average'
# . Then, the program uses an if-elif block to check the value of the three marks against a series of conditions.
# . If all three marks are greater than or equal to 35, the program will print "Result : Pass" and then again check the average of the marks and calculate the grade If average is greater than or equal to 90 and less than or equal to 100, the program will print "Grade : A" If average is greater than or equal to 80 and less than or equal to 89, the program will print "Grade : B" If average is greater than or equal to 70 and less than or equal to 79, the program will print "Grade : C" If none of the above conditions are met, the program will print "Grade : D"
# . If any of the three marks is less than 35, the program will print "Result : Fail" and "Grade : No Grade"

# 3. So the program is checking the student's three marks, calculating the total and average of the marks, and then determining the result and grade based on the marks and average.

# Nested If Statement in Python
"""
3 Marks as Input
Total
Average
Result
If Pass Grade
    90-100 A
    80-89 B
    70-79 C
    Else D
"""

# 1
mark1 = int(input("Enter Your Mark-1 : "))
mark2 = int(input("Enter Your Mark-2 : "))
mark3 = int(input("Enter Your Mark-3 : "))
total = mark1 + mark2 + mark3
average = total / 3.0

print("Total : ",total)
print("Average : ",average)
if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    print("Result : Pass")
else:
    print("Result : Fail")
    print("Grade : No Grade")
    

# 2
mark1 = int(input("Enter Your Mark-1 : "))
mark2 = int(input("Enter Your Mark-2 : "))
mark3 = int(input("Enter Your Mark-3 : "))
total = mark1 + mark2 + mark3
average = total / 3.0

print("Total : ",total)
print("Average : ",average)
if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    print("Result : Pass")
    if average >= 90 and average <= 100:
        print("Grade A")
    elif average >= 80 and average <= 89:
        print("Grade B")
    elif average >= 70 and average <= 79:
        print("Grade c")
    else:
        print("Grade D")
else:
    print("Result : Fail")
    print("Grade : No Grade")
