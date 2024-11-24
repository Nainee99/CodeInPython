# Lecture 1: Advanced Practice Questions
# CS50’s Introduction to Programming with Python

# -------------------------------
# 1. Advanced Comparison
# -------------------------------
# Write a program that takes three integers, x, y, and z, as input.
# Compare them and:
# - Print "All numbers are equal" if x == y == z.
# - Print "All numbers are different" if x, y, and z are all distinct.
# - Otherwise, print "Some numbers are equal."

# -------------------------------
# 2. Grade Validation
# -------------------------------
# Extend the grading system from the earlier practice file:
# - Ensure the input is a valid score between 0 and 100.
# - If the input is invalid, print an error message and exit.
# - Otherwise, determine the grade as before.

# -------------------------------
# 3. Custom Parity Function
# -------------------------------
# Write a function `is_divisible(n, d)` that:
# - Returns True if n is divisible by d, False otherwise.
# Then, write a program that:
# - Asks the user for two numbers, n and d.
# - Uses `is_divisible` to determine if n is divisible by d.
# - Prints "Divisible" or "Not divisible" accordingly.

# -------------------------------
# 4. Nested Conditionals
# -------------------------------
# Write a program that asks the user for their age.
# Based on the input:
# - If the age is less than 13, print "Child".
# - If the age is between 13 and 19, print "Teenager".
# - If the age is 20 or older:
#   - If the age is exactly 21, print "You're an adult now!"
#   - Otherwise, print "Adult".

# -------------------------------
# 5. Simplified Hogwarts Sorting
# -------------------------------
# Write a program to sort Hogwarts students by name and house using functions:
# - Define a function `get_house(name)` that:
#   - Returns "Gryffindor" for "Harry", "Hermione", or "Ron".
#   - Returns "Slytherin" for "Draco".
#   - Returns "Unknown" for any other name.
# - Use this function to ask for multiple names in a loop (stop on "quit").
# - Print each name with its assigned house.

# -------------------------------
# 6. FizzBuzz with Modulo
# -------------------------------
# Write a program that prints numbers from 1 to 100.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# For multiples of both 3 and 5, print "FizzBuzz".
# Otherwise, print the number.

# -------------------------------
# 7. Multi-Condition Grading System
# -------------------------------
# Extend the grading system to handle custom grade ranges:
# - Ask the user for grade boundaries (e.g., 90 for "A").
# - Use these boundaries to calculate the grade.
# - Ensure all input boundaries are valid and ordered correctly.

# -------------------------------
# 8. Function Practice with Match
# -------------------------------
# Write a program that asks the user for a number.
# - Use a `match` statement to:
#   - Print "Small" for numbers between 1 and 10.
#   - Print "Medium" for numbers between 11 and 50.
#   - Print "Large" for numbers above 50.
#   - Print "Invalid" for any other input.
