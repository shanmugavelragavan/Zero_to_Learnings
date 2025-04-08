# Try Block in Python

# In Python, the try block is used to enclose code that might raise an exception. If an exception is raised within the try block, the code in the corresponding except block is executed. This allows you to handle errors and exceptions in a controlled way, rather than letting the program crash.

# The try block in Python is used to enclose code that might raise an exception. If an exception is raised within the try block, it is caught by the associated except block, which can then handle the exception as desired. The basic structure of a try-except block in Python is as follows:

# Syntax:
#    try:
#               # code that might raise an exception
#    except ExceptionType1:
#               # code to handle ExceptionType1
#    except ExceptionType2:
#               # code to handle ExceptionType2
#    except:
#               # code to handle any other exception
#    else:
#               # code to run if no exception was raised
#    finally:
#               # code that will always be executed, regardless of whether an exception was raised or not


# The else block is optional, and is only executed if no exceptions were raised within the try block. The finally block is also optional, but is always executed after the try block, regardless of whether an exception was raised or not.




# try block in Python

try:
    a = 10 / 0
except Exception as e:
    print(e)

# Try Else
try:
    a = 10 / 25
except Exception as e:
    print(e)
else:
    print("A Value : ",a)

# Try else finally
try:
    a = 10 / 25
except Exception as e:
    print(e)
else:
    print("A Value : ",a)
finally:
    print("Thank You")

# Type of Exceptions in Python
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

# NameError Exception

# 1
try:
    print(a)
except NameError as e:
    print("A is not Defined")

# 2
try:
    print(10/0)
except ZeroDivisionError as e:
    print("Denominator can't be Zero")

# 3
try:
    a = int("Vel")
except ValueError as e:
    print("Please Enter Number Only")

# 4
try:
    a = [10,20,30,40]
    print(a[10])
except IndexError as e:
    print("Invalid Index")

# 5
try:
    f = open("text.txt")
except FileNotFoundError as e:
    print("File Not Found")
else:
    print(f.read)

# 6
try:
    a = 10/20
    print(a)
    b = [10,20,30,40]
    print(b[10])
except ZeroDivisionError as e:
    print("Denominator can't be Zero")
except IndexError as e:
    print("Invalid Index")
