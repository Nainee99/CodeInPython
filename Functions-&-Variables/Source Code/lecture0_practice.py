# Lecture 0 Practice File: Introduction to Python
# CS50’s Introduction to Programming with Python

# -------------------------------
# 1. Print a Greeting
# -------------------------------
# Task: Print "hello, world" to the console.
print("hello, world")

# -------------------------------
# 2. Ask for the User's Name
# -------------------------------
# Task: Prompt the user for their name and print a greeting using their name.
# Use string methods to format the name properly (e.g., title case).
name = input("what's your name?").title().strip()
print(f"hello,{name}")

# -------------------------------
# 3. Simple Arithmetic
# -------------------------------
# Task: Ask the user for two numbers (x and y).
# Calculate their sum and display it to the user.
x=int(input("what's X?"))
y=int(input("what's Y?"))
z=x+y
print("the sum is:", z)

# -------------------------------
# 4. Create a Greeting Function
# -------------------------------
# Task: Define a function `hello` that takes a name as an argument.
# If no name is provided, the function should greet "world" by default.
# Call the function with a user-provided name.
def hello(to="world"):
    print("hello",to)
hello()
hello("nainee")
# -------------------------------
# 5. Create a Function to Calculate Squares
# -------------------------------
# Task: Define a function `square` that takes a number as input
# and returns its square. 
# Ask the user for a number, pass it to the function, and display the result.
def squared(n):
    n=int(input("Enter a number:"))
    print("The square of the number is:",n*n)

# -------------------------------
# 6. Division with Rounding
# -------------------------------
# Task: Ask the user for two numbers (x and y).
# Perform a division (x / y) and display the result rounded to two decimal places.
a=float(input("what's X?"))
b=float(input("what's Y?"))
c=round(a/b , 2)
print(f"The answer of {a} and {b} is: {c:2f}")

# -------------------------------
# 7. Create a Main Function
# -------------------------------
# Task: Combine the above tasks into a single `main()` function.
# - Greet the user.
# - Ask for two numbers and display their sum.
# - Ask for a number, square it, and display the result.
# - Perform a division with two numbers and display the rounded result.
# Call the `main()` function if the script is run directly.
def main():
    print("Hello, world")

    x = int(input("What's X? (Enter an integer) "))
    y = int(input("What's Y? (Enter an integer) "))
    z = x + y
    print("The sum is:", z)

    num = int(input("Enter a number to square: "))
    print(f"The square of the number is: {squared(num)}")

    a = float(input("What's X? (Enter a float) "))
    b = float(input("What's Y? (Enter a float) "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        c = round(a / b, 2)
        print(f"The answer of {a} and {b} is: {c:.2f}")

# Call the main function to run the program
if __name__ == "__main__":
    main()


# -------------------------------
# 8. Challenge: Improve the Program
# -------------------------------
# Task: 
# - Add input validation (e.g., ensure the user enters numbers where required).
# - Handle division by zero gracefully.
# - Enhance the greeting to ask for the user's preferred title (e.g., Mr., Ms., Dr.).
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    print("Hello, world")

    x = get_number("What's X? (Enter a number) ")
    y = get_number("What's Y? (Enter a number) ")
    z = x + y
    print("The sum is:", z)

    num = get_number("Enter a number to square: ")
    print(f"The square of the number is: {squared(num)}")

    a = get_number("What's X? (Enter a number) ")
    b = get_number("What's Y? (Enter a number) ")
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        c = round(a / b, 2)
        print(f"The answer of {a} and {b} is: {c:.2f}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
