# -------------------------------
# Problem 4: Math Interpreter
# -------------------------------
# Python allows you to perform arithmetic operations like addition, subtraction, multiplication, and division.
# In this program, you will create a simple math interpreter that takes a user's arithmetic expression and calculates the result.
#
# Task:
# - Prompt the user for an arithmetic expression formatted as `x y z`:
#   - `x` is an integer.
#   - `y` is an operator (+, -, *, or /).
#   - `z` is an integer.
# - Calculate the result of the expression.
# - Output the result as a floating-point number formatted to one decimal place.
#
# Assumptions:
# - The input will be properly formatted with one space between `x`, `y`, and `z`.
# - Division (`/`) will not involve dividing by zero.
#
# Example:
# Input: 10 + 5
# Output: 15.0
#
# Input: 8 / 2
# Output: 4.0
#
# Hints:
# - Use Python's `split` method to separate the input into three parts.
# - Convert `x` and `z` to integers, and use `y` to determine the operation.
# - Perform the operation using conditional statements.
#
# -------------------------------

# Your code starts here:
def math_interpreter():
    # Prompt the user for an arithmetic expression
    expression = input("Enter an arithmetic expression (x y z): ")
    # Split the input into parts
    expression = expression.split()
    
    try:
        # Parse the input into variables
        x = int(expression[0])
        y = expression[1]
        z = int(expression[2])
        
        # Calculate the result based on the operator
        if y == "+":
            result = x + z
        elif y == "-":
            result = x - z
        elif y == "*":
            result = x * z
        elif y == "/":
            result = x / z
        else:
            return "Error: Invalid operator. Please use +, -, *, or /."
        
        # Output the result as a floating-point number formatted to one decimal place
        return f"Result: {round(result, 1)}"
    
    except (ValueError, IndexError):
        return "Error: Please provide a valid arithmetic expression in the format 'x y z'."

# Test the function
print(math_interpreter())
