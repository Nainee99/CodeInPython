# -------------------------------
# Problem 2: Bank Greeting
# -------------------------------
# In Season 7, Episode 24 of *Seinfeld*, Kramer visits a bank with a promise 
# that anyone not greeted with a “hello” would receive $100. However, Kramer 
# is greeted with a “hey,” leading to a compromise where he receives $20 instead.
#
# Task:
# - Write a program that prompts the user for a greeting.
# - The program should:
#   - Output "$0" if the greeting starts with "hello" (case-insensitive).
#   - Output "$20" if the greeting starts with "h" but is not "hello".
#   - Output "$100" otherwise.
#
# Requirements:
# - Ignore leading whitespace in the user's greeting.
# - Treat the user's greeting case-insensitively.
#
# Example:
# Input: hello
# Output: $0
#
# Input: hey
# Output: $20
#
# Input: goodbye
# Output: $100
#
# -------------------------------

# Your code starts here:
user_greeting = input("What is your greeting? ")
if user_greeting.strip().lower().startswith("hello"):
    print("$0")
elif user_greeting.strip().lower().startswith("h"):
    print("$20")
else:
    print("$100")


