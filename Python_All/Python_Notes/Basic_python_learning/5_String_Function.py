# String and String Functions in Python
# 1. Python has several built-in functions associated with the string data type. These functions let us easily modify and manipulate strings. Creating Strings is the simplest and easy to use in Python. To create a string in Python, we simply enclose a text in single as well as double-quotes.


# . type() => The returns the type of the object.
# . upper() => All the characters in a given string are uppers case.
# . lower() => All the characters in a given string are lower case.
# . capitalize() => The first character is the upper case
# . The title() => The first character in every word of the string is an upper case.
# . count() => Finds the number of times a specified value in the given string.
# . find() => Finds the first occurrence of the specified value.
# . replace() => Replaces a specified phrase with another specified phrase.
# . isalnum() => Checks whether all the characters in a given string is alphanumeric or not
# . isalpha() => returns True if all the characters in the string are alphabets
# . islower() => Checks if all characters in the string are lowercase
# . isupper() => Checks if all characters in the string are uppercase
# . strip() => The used to trim whitespaces from the string object

# 1.
s = "Shanmugavel"
print(s)
print(type(s))

# 2.
s = "Shanmuga vel"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("a"))
print(s.endswith("el"))
print(s.find("u"))
print(s.find("a",5))
print(s.replace("a","5"))

# 3.
a = "ragavan123"
print("Is Upper : ", a.isupper())
print("Is Lower : ", a.islower())
print("Is Alpha Numeric : ", a.isalnum())
print("Is Alpha : ", a.isalpha())

# 4.
m = "he\nis\ngood"
print(m)
print(m.splitlines())
print(m.splitlines(True))

# 5.
n = "Shanmugavel is a Good Boys"
print(n.split(" "))
n = "Shanmugavel,is,a,Good,Boys"
print(n.split(","))

# 6.
v = "       VEL      "
print(len(v))
print(len(v.strip()))
print(len(v.lstrip()))
print(len(v.rstrip()))

# 7.
r = "10-12-2024"
print(r.partition('-'))
