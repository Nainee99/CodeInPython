# -------------------------------
# Problem 2: Playback Speed
# -------------------------------
# Some people have a habit of lecturing speaking rather quickly,
# and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed,
# or even by having them pause between words.
#
# In this program, you will prompt the user for input and then output that same input,
# replacing each space with "..." (i.e., three periods).
#
# Task:
# - Prompt the user for a string.
# - Replace every space with three periods ("...").
#
# Example:
# Input: "This is a test"
# Output: "This...is...a...test"
#
# -------------------------------

# Your code starts here:
string_input = input("Please enter a string: ")
print(string_input.replace(" ", "..."))
