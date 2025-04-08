# Date Time Functions in Python

# Python datetime module is provided in Python to work with dates and times. A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects. These classes provide a number of functions to deal with dates, times and time intervals.

# Here are some examples of common date and time-related functions in Python:

# datetime.now(): Returns the current date and time.
# datetime.date(): Returns date object of today's date.
# datetime.time(): Returns the current time.
# datetime.datetime(): Returns the current date and time as a datetime object.
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0): Represents the difference between two date or time values.
# The strftime() function is used to convert date and time objects to their string representation.
#       Syntax :
#            strftime ( format )


# List of format codes

# Directive	Description	Example
# %A	Weekday full name	Monday
# %a	Weekday short name	Mon
# %d	Day of month (1-31)	26
# %b	Month of short name	Dec
# %B	Month of full name	December
# %Y	Year of full version , without century	2022
# %y	Year of short version	22
# %w	Weekday as a number ( 0-Sun , 1-Mon , 2-Tue , 3-Wed , 4-Thu , 5-Fri , 6-Sat )	1(Monday)
# %W	Week number of Year ( Monday as the first day of week ( 00-53 ) )	48
# %m	Month as a Number ( 1(Jun) - 12(Dec) )	12(Dec)
# %H	Hours ( 00-23 )	15
# %M	Minute ( 00-59 )	50
# %S	Second ( 00-59 )	23
# %p	PM / AM	PM
# %c	Local version of date and time	Mon Dec 26 15 : 50 : 23 2022
# %X	Local version of time	15:50:23
# %x	Local version of date	12/26/22




# Date Time in Python

import datetime as dt

current_date = dt.date.today()
print("Current Date : ",current_date)

# 1
new = dt.date(2025, 10, 10)
print(new)
print("Year : ",new.year)
print("Month : ",new.month)
print("day : ",new.day)
print("-----------------------------------------")

# 2
a = dt.time(10,45,5,555505)
print(a)
print("hour : ",a.hour)
print("minute : ",a.minute)
print("second : ",a.second)
print("microsecond : ",a.microsecond)
print("-----------------------------------------")

# 3
current_time = dt.datetime.now()
print("Current Time : ",current_time)
print("-----------------------------------------")

# 4
new = dt.datetime(2024,12,28,12,2,10)
print(new)
print(new.date())
print(new.time())
print("-----------------------------------------")

# 5
current = dt.datetime.now()
new_year = dt.datetime(2025,1,1)
difference = new_year - current
print(difference)
print("-----------------------------------------")

# 6
current = dt.datetime.now()
print(current)
s = current.strftime("%A %b %D %Y")
print(s)