# -------------------------------
# Problem 1: Deep Thought
# -------------------------------
# In Douglas Adams' *The Hitchhiker’s Guide to the Galaxy*, the supercomputer 
# Deep Thought reveals that the Answer to the Great Question of Life, the Universe, 
# and Everything is 42.
#
# Task:
# - Write a program that prompts the user for their answer to the Great Question.
# - The program should:
#   - Output "Yes" if the user inputs:
#       - 42 (as a string or integer)
#       - "forty-two" (case-insensitive)
#       - "forty two" (case-insensitive)
#   - Output "No" for all other inputs.
#
# Hints:
# - No need to convert the user’s input to an integer. Comparing it as a string works!
# - Case-insensitivity can be handled using `.lower()`.
#
# Example:
# Input: 42
# Output: Yes
#
# Input: forty-two
# Output: Yes
#
# Input: forty two
# Output: Yes
#
# Input: 43
# Output: No
#
# -------------------------------

# Your code starts here:
user_answer = input("What is your answer to the Great Question? ")
if user_answer.lower() in ["42", "forty-two", "forty two"]:
    print("Yes")
else:
    print("No")


