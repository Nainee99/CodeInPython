# Advanced Practice File: Python Basics

# -------------------------------
# 1. Personalized Greeting with Input Validation
# -------------------------------
# Task: Prompt the user for their full name and ensure they provide input (no empty strings).
# Print a greeting with their name in title case.
# If they don't enter a name, prompt them again until valid input is provided.
def get_full_name():
    while True:
        full_name = input("Enter your full name: ").strip()
        if full_name:
            print("Hello,", full_name.title()) 
            break  # Exit the loop after a valid name is provided
        else:
            print("Please enter a valid name.")

get_full_name()

# -------------------------------
# 2. Perform and Display Mathematical Operations
# -------------------------------
# Task: Ask the user for two numbers (a and b).
# Perform the following operations:
# - Addition
# - Subtraction
# - Multiplication
# - Division (rounded to two decimal places)
# Display the results with descriptive labels.
def perform_math_operations():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"Addition: {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
    print(f"Division: {num1} / {num2} = {round(num1 / num2, 2)}")

perform_math_operations()

# -------------------------------
# 3. Function to Reverse a String
# -------------------------------
# Task: Create a function `reverse_string` that takes a string as input and returns the reversed string.
# Prompt the user to enter a sentence, reverse it using the function, and display the result.
def reverse_string(text):
    return text[::-1]

# Prompting the user for input and passing it to the function
sentence = input("Enter a sentence: ")
reversed_sentence = reverse_string(sentence)
print("Reversed sentence:", reversed_sentence)

# -------------------------------
# 4. Calculate Factorials
# -------------------------------
# Task: Write a function `factorial` that calculates the factorial of a number.
# Prompt the user for a non-negative integer and call the function.
# Display the result.
# If the input is invalid (e.g., a negative number or not an integer), prompt the user again.
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Function to get valid input from the user
def get_valid_input():
    while True:
        try:
            n = int(input("Enter a non-negative integer: "))
            if n < 0:
                print("Please enter a non-negative integer.")
            else:
                return n
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Get the valid input from the user
number = get_valid_input()

# Call the factorial function and display the result
print(f"The factorial of {number} is: {factorial(number)}")

# -------------------------------
# 5. Average and Median of a List
# -------------------------------
# Task: Ask the user to input a series of numbers (comma-separated).
# Convert the input into a list of numbers.
# Create a function to calculate the average of the list.
# Create another function to find the median of the list.
# Display both the average and the median.
# Input and list conversion with error handling
numbers_input = input("Enter a series of numbers (comma-separated): ")
try:
    # Split the input string into substrings
    raw_numbers = numbers_input.split(",")

    # Remove leading and trailing spaces from each substring
    cleaned_numbers = [num.strip() for num in raw_numbers]

    # Filter out any empty substrings
    non_empty_numbers = [num for num in cleaned_numbers if num]

    # Convert the remaining valid strings to floats
    numbers = [float(num) for num in non_empty_numbers]
    print("Numbers:", numbers)
except ValueError:
    print("Invalid input! Please enter only numbers separated by commas.")
    numbers = []

# Function to calculate the average of a list
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Function to calculate the median of a list
def calculate_median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:  # Even number of elements
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:  # Odd number of elements
        return sorted_numbers[n // 2]

# Display the results
if numbers:
    print("Average:", calculate_average(numbers))
    print("Median:", calculate_median(numbers))
else:
    print("No valid numbers provided.")


# -------------------------------
# 6. Higher-Order Function for Squaring
# -------------------------------
# Task: Define a function `apply_to_each` that takes a list and a function as arguments.
# Use this function to apply `square` (a function you define to return the square of a number)
# to each number in a list provided by the user (comma-separated).
# Display the resulting list.
# Function to square a number
def square(n):
    return n ** 2

# Higher-order function to apply any function (like square) to each element of a list
def apply_to_each(lst, func):
    return [func(x) for x in lst]

# Input from the user, assuming comma-separated numbers
numbers_input = input("Enter numbers separated by commas: ")

# Convert the input string to a list of numbers
numbers = [int(num.strip()) for num in numbers_input.split(",")]

# Apply the square function to each number in the list
squared_numbers = apply_to_each(numbers, square)

# Output the result
print(squared_numbers)


# -------------------------------
# 7. Check for Palindrome
# -------------------------------
# Task: Write a function `is_palindrome` that checks whether a given string is a palindrome.
# Ignore case and spaces when checking.
# Prompt the user for a string and use the function to display whether it's a palindrome.
def is_palindrome(s):
    # Preprocess the string: Remove spaces, special characters, and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Prompt the user for a string
string_input = input("Enter a string: ")

# Check and display whether it's a palindrome
if is_palindrome(string_input):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
# -------------------------------
# 8. Enhanced Main Function
# -------------------------------
# Task: Combine the above tasks into a `main()` function.
# - Greet the user.
# - Perform mathematical operations.
# - Reverse a user-provided string.
# - Calculate the factorial of a number.
# - Compute the average and median of a list.
# - Check if a string is a palindrome.
# Call the `main()` function if the script is run directly.
def main():
    print("Welcome to the Python Basics Practice Program!")

    # 1. Personalized Greeting
    print("\n--- Task 1: Personalized Greeting ---")
    get_full_name()
    
    # 2. Mathematical Operations
    print("\n--- Task 2: Perform Mathematical Operations ---")
    perform_math_operations()
    
    # 3. Reverse a String
    print("\n--- Task 3: Reverse a String ---")
    sentence = input("Enter a sentence: ")
    print("Reversed sentence:", reverse_string(sentence))
    
    # 4. Calculate Factorials
    print("\n--- Task 4: Calculate Factorial ---")
    number = get_valid_input()
    print(f"The factorial of {number} is: {factorial(number)}")
    
    # 5. Average and Median of a List
    print("\n--- Task 5: Average and Median of a List ---")
    numbers_input = input("Enter a series of numbers (comma-separated): ")
    try:
        numbers = [float(num.strip()) for num in numbers_input.split(",") if num.strip()]
        print("Average:", calculate_average(numbers))
        print("Median:", calculate_median(numbers))
    except ValueError:
        print("Invalid input! Please enter only numbers separated by commas.")
    
    # 6. Check for Palindrome
    print("\n--- Task 7: Check for Palindrome ---")
    string_input = input("Enter a string: ")
    if is_palindrome(string_input):
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")
    
    # 7. Generate Multiplication Table
    print("\n--- Task 9: Generate Multiplication Table ---")
    while True:
        try:
            n = int(input("Enter a number to generate a multiplication table: "))
            if n > 0:
                generate_multiplication_table(n)
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    print("\nThank you for using the Python Basics Practice Program!")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()


# -------------------------------
# 9. Challenge: Generate a Multiplication Table
# -------------------------------
# Task: Prompt the user for a number `n`.
# Create a multiplication table for numbers from 1 to `n`.
# Format the table as a neatly aligned grid.
def generate_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} x {j} = {i * j}", end="\t")
        print()  # Move to the next row after each iteration

# Get user input outside the function
while True:
    try:
        n = int(input("Enter a number to generate a multiplication table: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            generate_multiplication_table(n)
            break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
