# Lecture 1: Practice Questions
# CS50’s Introduction to Programming with Python

# -------------------------------
# 1. Age Group Categorization
# -------------------------------
# Write a function `age_group(age)` that takes an integer `age` as input.
# The function should return a string based on the following conditions:
# - "Child" if age is less than 12
# - "Teenager" if age is between 12 and 19 (inclusive)
# - "Adult" if age is between 20 and 64 (inclusive)
# - "Senior" if age is 65 or older
def age_group(age):
    if age < 12:
        return "Child"
    elif 12 <= age <= 19:
        return "Teenager"
    elif 20 <= age <= 64:
        return "Adult"
    else:
        return "Senior"

print(age_group(25))  # Adult

# -------------------------------
# 2. Leap Year Checker
# -------------------------------
# Write a function `is_leap_year(year)` that determines whether a given year is a leap year.
# A year is a leap year if:
# - It is divisible by 4.
# - But if it is divisible by 100, it must also be divisible by 400 to be a leap year.
# Return True if the year is a leap year, otherwise return False.

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(2020))  # True

# -------------------------------
# 3. Divisibility Check
# -------------------------------
# Write a function `check_divisibility(a, b)` that checks if integer `a` is divisible by integer `b`.
# If `a` is divisible by `b`, return "Divisible".
# Otherwise, return "Not divisible".

def check_divisibility(a, b):
    if a % b == 0:
        return "Divisible"
    else:
        return "Not divisible"
    
print(check_divisibility(10, 2))  # Divisible

# -------------------------------
# 4. Positive or Negative
# -------------------------------
# Write a function `positive_or_negative(n)` that takes a number `n` as input and returns:
# - "Positive" if n is greater than 0
# - "Negative" if n is less than 0
# - "Zero" if n is equal to 0

def positive_or_negative(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
    
print(positive_or_negative(5))  # Positive

# -------------------------------
# 5. Temperature Converter
# -------------------------------
# Write a function `convert_temperature(celsius)` that takes a temperature in Celsius and converts it to Fahrenheit.
# Use the formula: Fahrenheit = (Celsius * 9/5) + 32.
# The function should return the temperature in Fahrenheit.
def convert_temperature(celsius):
    Fahrenheit = (celsius * 9/5) + 32
    return Fahrenheit

print(convert_temperature(0))  # 32.0
# -------------------------------
# 6. Vowel or Consonant
# -------------------------------
# Write a function `is_vowel(letter)` that takes a letter as input.
# Return True if the letter is a vowel ('a', 'e', 'i', 'o', 'u', case-insensitive).
# Otherwise, return False.
def is_vowel(letter):
    if letter.lower() in 'aeiou':
        return True
    else:
        return False

print(is_vowel('a'))  # True

# -------------------------------
# 7. Number Classification
# -------------------------------
# Write a function `classify_number(n)` that takes an integer `n` as input and classifies it as:
# - "Positive even" if the number is positive and even.
# - "Positive odd" if the number is positive and odd.
# - "Negative even" if the number is negative and even.
# - "Negative odd" if the number is negative and odd.
# - "Zero" if the number is zero.
def classify_number(n):
    if n > 0 and n % 2 == 0:
        return "Positive even"
    elif n > 0 and n % 2 != 0:
        return "Positive odd"
    elif n < 0 and n % 2 == 0:
        return "Negative even"
    elif n < 0 and n % 2 != 0:
        return "Negative odd"
    else:
        return "Zero"
    
print(classify_number(5))  # Positive odd

