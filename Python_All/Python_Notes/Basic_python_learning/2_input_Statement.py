# Input Function in Python Programming

# 1. The input() function takes the user's input in the next single line, so whatever user writes in a signle line would be assign to to a variable. The input ( ) function helps to enter data at run time by the user and returns it as a string. This function prompts the user for an input from the keyboard.

# 2. Once the user has give the input and pressed enter One of the most important things to note here is that we're storing whatever the user entered into a variable. The output function print ( ) is used to display the result of the program on the screen after execution.

# 3. Use the int ( ) Function to Check if the Input Is an Integer in Python. The int ( ) function can convert a given string integer value to an integer type. Use the float ( ) Function to Check if the Input Is an decimal number in Python. The float ( ) function can convert a given string decimal number value to an float type.

# The program takes input from the user in three different forms:

# 1. A string input, taken using the input() function, stored in the "name" variable, and its type and value are printed.
# 2. Two integer inputs, taken using the input() function and converted to integers using int(), stored in the variables "a" and "b", their sum is calculated and stored in "c", and the sum and type of "a" are printed.
# 3. Two float inputs, taken using the input() function and converted to float using float(), stored in the variables "a" and "b", their sum is calculated and stored in "c", and the sum and type of "a" are printed.

# Getting input in Python

# 1.
name = input("Enter Name :")
print(type(name))
print(name)

# 2.
a = input("Enter The Value of A : ")
b = input("Enter The Value of B : ")
c = a+b
print(c)
print(type(a))

# 3
a = int(input("Enter The Value of A : "))
b = int(input("Enter The Value of B : "))
c = a+b
print(c)
print(type(a))

# 4
a = float(input("Enter The Value of A : "))
b = float(input("Enter The Value of B : "))
c = a+b
print(c)
print(type(a))


# Multiple Values in Single Line

# 1. The program takes input from the user in the form of three names separated by either space or comma, stored in the variables name1, name2, name3. In the first input, the input() function is used to take the input, and the split() function is used to separate the names by space and store them in the respective variables. The values of the variables are then printed.

# 2. In the second input, the input() function is used to take the input, and the split() function is used to separate the names by a comma and store them in the respective variables. The values of the variables are then printed.

# 1.
name1,name2,name3 = input("Enter 3 Names : ").split()
print("Name 1 : ",name1)
print("Name 2 : ",name2)
print("Name 3 : ",name3)

# 2
name1,name2,name3 = input("Enter 3 Names : ").split(',')
print("Name 1 : ",name1)
print("Name 2 : ",name2)
print("Name 3 : ",name3)


# Multiple Line String Input in Python

# 1. The program defines a string variable a containing a multi-line text string. The data type of the variable a is str. The program then uses the print function to display the data type of a, which is str, and the value of a which is the text string itself.

# 2. The program is a Python script that takes multi-line input from the user in the form of a paragraph.

# 1. A list "para" is initialized.
# 2. The user is prompted to "Enter a Para : "
# 3. The "while" loop is used to get multi-line input.
# . The line input is taken using the "input()" function and stored in the variable "line".
# . The "if" condition checks if the line is not empty, if it is not, the line is added to the list "para" using the "append()" method.
# . If the line is empty, the loop breaks.
# 4. The list "para" is printed.
# 5. The "join()" method is used to join the list "para" with a line break and store it in the variable "output".
# 6. The final output is printed.

# 1.
a = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
"""
print(type(a))
print(a)

# 2.
para = [25,22,33]
print(para)

# 3.
para = [25,22,33]
print(type(para))
print(para[2])

# 4.
para = ["25","22","33"]
print('|'.join(para))

# 5.
para = []
print("Enter a Para : ")

while True:
    line = input()
    if line:
        para.append(line)
    else:
        break
    print(para)

# 6.
para=[]
print("Enter a Para : ")

while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
    print(para)

    output='\n'.join(para)
    print(output)