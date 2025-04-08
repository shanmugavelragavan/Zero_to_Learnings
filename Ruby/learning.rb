# 1. Hello World / Setup

puts "Hello, World!"

# 2. Drawing a Shape

puts "   /|"
puts "  / |"
puts " /  |"
puts "/___|"

# 3. Variables

character_name = "Shanmugavel"
character_age = 20  # Integer

puts "There once was a man named #{character_name}."
puts "He was #{character_age} years old."

character_name = "Ragavan"  
puts "He really liked the name #{character_name}."
puts "But didn't like being #{character_age}."

# (Alternative Corrected Version)
name = "Ragavan"
age = 19
puts "My name is " + name + " and my age is " + age.to_s + " years old."

# (OR using string interpolation, which is recommended)
puts "My name is #{name} and my age is #{age} years old."

# 4. Data Types

is_name = "Vel"       # String
is_age = 20           # Integer
height = 3.2          # Float
is_student = true     # Boolean
flaws = nil           # Nil (no value)
skills = ["Ruby", "Python", "JavaScript"]  # Array

# 5. Working With Strings

text = "  Hello Ruby!   "
puts text.upcase        # "HELLO RUBY!"
puts text.downcase      # "hello ruby!"
puts text.strip         # Removes extra spaces -> "Hello Ruby!"
puts text.strip.length  # Corrected length after removing spaces (11)
puts text.include?("Ruby")  # true
puts text[0, 5]         # "Hello" (substring)
puts text.index("b")    # Position of first 'b' (should return 8)
puts "Programming".upcase()  # "PROGRAMMING"

# 6. Math & Numbers

# Basic Arithmetic Operations
puts 5 + 3    # 8 (Addition)
puts 10 - 4   # 6 (Subtraction)
puts 6 * 7    # 42 (Multiplication)
puts 20 / 4   # 5 (Integer Division)
puts 10.0 / 4 # 2.5 (Floating-point Division)
puts 10 % 3   # 1 (Modulo - Remainder of 10/3)
puts 2 ** 3  # Exponentiation (2^3 = 8)

# Math Functions
puts Math.sqrt(25)    # 5.0 (Square root)
puts Math.log(1)      # 0.0 (Logarithm)
puts Math.log10(100)  # 2.0 (Logarithm base 10)
puts Math.sin(Math::PI / 2)  # 1.0 (Sine of 90°)
puts Math.cos(0)      # 1.0 (Cosine of 0°)

# Absolute Value
num = -20
puts num.abs()  # 20 (Absolute value)

# Rounding Numbers
num1 = 20.678
puts num1.round()   # 21 (Round to nearest integer)

num2 = 20.1
puts num2.ceil()    # 21 (Rounds up)

num3 = 20.9
puts num3.floor()   # 20 (Rounds down)

# Generating Random Numbers
puts rand()        # Random decimal between 0 and 1
puts rand(10)      # Random number between 0 and 9
puts rand(1..100)  # Random number between 1 and 100
puts rand(50..100) # Random number between 50 and 100

# Convert Strings to Numbers
str_num = "30"
puts str_num.to_i  # 30 (String to Integer)
puts str_num.to_f  # 30.0 (String to Float)

# Convert Numbers to Strings
num = 100
puts num.to_s  # "100" (Integer to String)

# Working with Large Numbers
large_num = 1_000_000
puts large_num  # 1000000 (Underscores improve readability)

# 7. Getting User Input

print "Enter your name: "
name = gets.chomp()

print "Enter your age: "
age = gets.chomp()

puts "Hello, #{name}, you are #{age} years old."

# 8. Building a Calculator

print "Enter first number: "
num1 = gets.chomp.to_f

print "Enter second number: "
num2 = gets.chomp.to_f

puts "Sum (float): #{num1 + num2}"
puts "Sum (integer): #{num1.to_i + num2.to_i}"
puts "Difference: #{num1 - num2}"
puts "Product: #{num1 * num2}"
puts "Quotient: #{num1 / num2}" if num2 != 0

# 9. Building a Mad Libs Game

print "Enter a color: "
color = gets.chomp()
print "Enter a plural noun: "
plural_noun = gets.chomp()
print "Enter a celebrity: "
celebrity = gets.chomp()

puts "Roses are #{color}"
puts "#{plural_noun} are blue"
puts "I love #{celebrity}"

# 10. Arrays

# Creating an Array
friends = ["Alice", "Bob", "Charlie", "Oscar"]

# Accessing Elements
puts friends[0]   # "Alice"  (First element)
puts friends[-1]  # "Oscar"  (Last element)
puts friends[2]   # "Charlie" (Third element)

# Array Properties & Methods
puts friends.length   # 4 (Number of elements)
puts friends.include?("Bob")  # true (Check if "Bob" is in the array)
puts friends.reverse  # ["Oscar", "Charlie", "Bob", "Alice"]
puts friends.sort     # ["Alice", "Bob", "Charlie", "Oscar"] (Sort alphabetically)

# Modifying an Array
friends[1] = "David"   # Replace "Bob" with "David"
puts friends.inspect   # ["Alice", "David", "Charlie", "Oscar"]

# Adding & Removing Elements
friends.push("Eve")    # Add "Eve" at the end
puts friends.inspect   # ["Alice", "David", "Charlie", "Oscar", "Eve"]

friends.pop            # Remove the last element
puts friends.inspect   # ["Alice", "David", "Charlie", "Oscar"]

friends.unshift("Zack")  # Add "Zack" at the beginning
puts friends.inspect     # ["Zack", "Alice", "David", "Charlie", "Oscar"]

friends.shift           # Remove the first element
puts friends.inspect    # ["Alice", "David", "Charlie", "Oscar"]

# Creating an Empty Array
empty_array = []
empty_array << "First Item"
puts empty_array.inspect  # ["First Item"]

# Using an Array with Numbers
numbers = [5, 2, 9, 1, 7]
puts numbers.sort.inspect # [1, 2, 5, 7, 9]
puts numbers.max          # 9 (Maximum value)
puts numbers.min          # 1 (Minimum value)
puts numbers.sum          # 24 (Sum of all numbers)

# Using Ranges to Create Arrays
range_array = (1..5).to_a
puts range_array.inspect  # [1, 2, 3, 4, 5]

# 11. Hashes (Dictionaries in Ruby)

# Using Symbols as Keys (Recommended)
student = {
  name: "Shanmugavel",
  age: 21,
  course: "Computer Science"
}

# Accessing Hash Values
puts student[:name]   # "Shanmugavel"
puts student[:age]    # 21
puts student[:course] # "Computer Science"

# Adding & Updating Values
student[:grade] = "A"  # Adding a new key-value pair
student[:age] = 22     # Updating an existing key
puts student.inspect   # {:name=>"Shanmugavel", :age=>22, :course=>"Computer Science", :grade=>"A"}

# Using Strings as Keys (Alternative)
person = {
  "name" => "Ragavan",
  "age" => 20,
  "city" => "Chennai"
}

puts person["name"]    # "Ragavan"
puts person["city"]    # "Chennai"

# Checking if a Key Exists
puts student.key?(:grade)  # true (Key exists)
puts student.key?(:height) # false (Key doesn't exist)

# Getting All Keys & Values
puts student.keys.inspect   # [:name, :age, :course, :grade]
puts student.values.inspect # ["Shanmugavel", 22, "Computer Science", "A"]

# Iterating Over a Hash
student.each do |key, value|
  puts "#{key}: #{value}"
end
# Output:
# name: Shanmugavel
# age: 22
# course: Computer Science
# grade: A

# Deleting a Key
student.delete(:grade)
puts student.inspect   # {:name=>"Shanmugavel", :age=>22, :course=>"Computer Science"}

# Default Value for Missing Keys
grades = Hash.new("Not Available")
grades[:math] = 90
puts grades[:math]      # 90
puts grades[:science]   # "Not Available" (Default value)

