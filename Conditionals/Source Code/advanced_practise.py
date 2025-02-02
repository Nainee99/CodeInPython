# Lecture 1: Advanced Practice Questions
# CS50’s Introduction to Programming with Python

# -------------------------------
# 1. Temperature Range Check
# -------------------------------
# Write a program that asks for the temperature in Celsius and:
# - If the temperature is below 0, print "Freezing".
# - If the temperature is between 0 and 10 (inclusive), print "Cold".
# - If the temperature is between 11 and 25 (inclusive), print "Mild".
# - If the temperature is between 26 and 35 (inclusive), print "Warm".
# - If the temperature is above 35, print "Hot".
temperature = input("Enter the temperature in Celsius: ")
temperature = float(temperature)

if temperature < 0:
    print("Freezing")
elif 0 <= temperature <= 10:
    print("Cold")
elif 11 <= temperature <= 25:
    print("Mild")
elif 26 <= temperature <= 35:
    print("Warm")
else:
    print("Hot")


# -------------------------------
# 2. Voting Eligibility
# -------------------------------
# Write a program that asks the user for their age and:
# - If the age is less than 18, print "You are not eligible to vote".
# - If the age is between 18 and 65 (inclusive), print "You are eligible to vote".
# - If the age is over 65, print "You are eligible for senior voting privileges".
age = input("Enter your age: ")
age = int(age)

if age < 18:
    print("You are not eligible to vote")
elif 18 <= age <= 65:
    print("You are eligible to vote")
else:
    print("You are eligible for senior voting privileges")

# -------------------------------
# 3. Even or Divisible by 3
# -------------------------------
# Write a function `even_or_divisible_by_three(n)` that checks:
# - If n is divisible by 2, print "Even".
# - If n is divisible by 3, print "Divisible by 3".
# - If n is divisible by both 2 and 3, print "Even and Divisible by 3".
# - Otherwise, print "Neither".
def even_or_divisible_by_three(n):
    if n % 2 == 0 and n % 3 == 0:
        print("Even and Divisible by 3")
    elif n % 2 == 0:
        print("Even")
    elif n % 3 == 0:
        print("Divisible by 3")
    else:
        print("Neither")

# -------------------------------
# 4. Number Comparison with Conditions
# -------------------------------
# Write a function `compare_numbers(x, y)` that compares two integers:
# - If both x and y are positive, return "Both numbers are positive".
# - If both x and y are negative, return "Both numbers are negative".
# - If x is positive and y is negative, return "x is positive, y is negative".
# - If x is negative and y is positive, return "x is negative, y is positive".
# - If x and y are equal, return "The numbers are equal".
# - Otherwise, return "Numbers have different signs".
def compare_numbers(x, y):
    if x > 0 and y > 0:
        return "Both numbers are positive"
    elif x < 0 and y < 0:
        return "Both numbers are negative"
    elif x > 0 and y < 0:
        return "x is positive, y is negative"
    elif x < 0 and y > 0:
        return "x is negative, y is positive"
    elif x == y:
        return "The numbers are equal"
    else:
        return "Numbers have different signs"
    

print(compare_numbers(5, 10))  # Both numbers are positive

# -------------------------------
# 5. Age and Retirement Status
# -------------------------------
# Write a program that asks the user for their age and checks:
# - If the age is 65 or older, print "You are eligible for retirement".
# - If the age is between 45 and 64 (inclusive), print "You are nearing retirement".
# - If the age is between 20 and 44 (inclusive), print "You are working age".
# - If the age is below 20, print "You are not yet of working age".
age = input("Enter your age: ")
age = int(age)

if age >= 65:
    print("You are eligible for retirement")
elif 45 <= age <= 64:
    print("You are nearing retirement")
elif 20 <= age <= 44:
    print("You are working age")
else:
    print("You are not yet of working age")

# -------------------------------
# 6. Grade Feedback Based on Score
# -------------------------------
# Write a program that asks the user for a score between 0 and 100 and:
# - If the score is greater than or equal to 90, print "Excellent".
# - If the score is between 75 and 89 (inclusive), print "Good".
# - If the score is between 50 and 74 (inclusive), print "Satisfactory".
# - If the score is below 50, print "Fail".
# - If the score is not between 0 and 100, print "Invalid score".   
mark = input("Enter your score: ")
mark = int(mark)

if mark < 0 or mark > 100:
    print("Invalid score")
elif mark >= 90:
    print("Excellent")
elif 75 <= mark <= 89:
    print("Good")
elif 50 <= mark <= 74:
    print("Satisfactory")
else:
    print("Fail")

# -------------------------------
# 7. Discount Eligibility
# -------------------------------
# Write a program that asks the user for their purchase amount and:
# - If the amount is greater than or equal to 100, print "You get a 20% discount".
# - If the amount is between 50 and 99.99 (inclusive), print "You get a 10% discount".
# - If the amount is below 50, print "No discount available".
# - If the input is negative, print "Invalid amount".
amount = input("Enter the purchase amount: ")
amount = float(amount)

if amount < 0:
    print("Invalid amount")
elif amount >= 100:
    print("You get a 20% discount")
elif 50 <= amount <= 99.99:
    print("You get a 10% discount")
else:
    print("No discount available")

# -------------------------------
# 8. Leap Year Validator
# -------------------------------
# Write a function `is_leap_year(year)` that checks if a given year is a leap year:
# - If the year is divisible by 4, but not divisible by 100, return True.
# - If the year is divisible by 400, return True.
# - Otherwise, return False.
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
     return False

print(is_leap_year(2020))  # True
