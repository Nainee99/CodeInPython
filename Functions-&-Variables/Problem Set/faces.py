# -------------------------------
# Problem 3: Making Faces
# -------------------------------
# Before there were emoji, there were emoticons, 
# where text like :) was a happy face and text like :( was a sad face. 
# Nowadays, programs tend to convert emoticons to emoji automatically!
#
# In this program, you will implement a function `convert` that accepts a string as input
# and returns that same string with any ":)" converted to "🙂" and any ":(" converted to "🙁".
# All other text should remain unchanged.
#
# Task:
# - Implement a function called `convert` to replace ":)" with "🙂" and ":(" with "🙁".
# - Create a `main` function that prompts the user for input, calls the `convert` function, and prints the result.
#
# Example:
# Input: "Hello :) How are you :( today?"
# Output: "Hello 🙂 How are you 🙁 today?"
#
# -------------------------------

# Your code starts here:
def convert(s):
    return s.replace(":)", "🙂").replace(":(", "🙁")

def main():
    user_input = input("Please enter a string: ")
    result = convert(user_input)
    print(result)

# Call the main function if the script is run directly
if __name__ == "__main__":
    main()