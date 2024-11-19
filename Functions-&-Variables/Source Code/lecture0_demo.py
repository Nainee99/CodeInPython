# Lecture 0: Introduction to Python
# CS50’s Introduction to Programming with Python

# -------------------------------
# 1. Your First Python Program
# -------------------------------
# The famous "Hello, world!" program.
print("hello, world")  # Output: hello, world

# -------------------------------
# 2. Adding User Input and Variables
# -------------------------------
# Ask the user for their name and greet them.
name = input("What's your name? ").strip().title()
print(f"hello, {name}")  # Output: hello, <User's Name>

# -------------------------------
# 3. Demonstrating Arithmetic Operations
# -------------------------------
# Simple calculator that adds two numbers
x = float(input("Enter the first number (x): "))
y = float(input("Enter the second number (y): "))
z = round(x + y, 2)  # Adding and rounding to 2 decimal places
print(f"The sum of {x} and {y} is {z:.2f}")

# -------------------------------
# 4. Creating and Using Functions
# -------------------------------
# A function to greet a user
def hello(to="world"):
    """Greet a user with a default or provided name."""
    print(f"hello, {to}")

# Using the hello function
name = input("What's your name? ").strip().title()
hello(name)  # Personalized greeting
hello()  # Default greeting

# -------------------------------
# 5. Using Functions to Perform Calculations
# -------------------------------
def square(n):
    """Return the square of a number."""
    return n * n

# Asking user for a number to square
x = int(input("Enter a number to square: "))
print(f"The square of {x} is {square(x)}")

# -------------------------------
# 6. Combining it All in a Main Function
# -------------------------------
def main():
    """Run the main program."""
    print("\n--- Welcome to the Python Program ---\n")

    # Greet the user
    name = input("What's your name? ").strip().title()
    hello(name)

    # Perform arithmetic
    x = float(input("Enter the first number (x): "))
    y = float(input("Enter the second number (y): "))
    z = round(x / y, 2)  # Division with rounding
    print(f"The result of {x} divided by {y} is {z:.2f}")

    # Square a number
    num = int(input("Enter a number to square: "))
    print(f"The square of {num} is {square(num)}")

# Calling the main function
if __name__ == "__main__":
    main()
