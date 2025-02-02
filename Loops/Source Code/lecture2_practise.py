# Lecture 2: Practice Questions - Loops in Python
# CS50’s Introduction to Programming with Python

# -------------------------------
# 1. Sum of Digits
# -------------------------------
# Write a function `sum_of_digits(n)` that calculates the sum of the digits of a given integer `n`.
# For example, if n = 123, the function should return 6 (1 + 2 + 3).
def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

# Test the function with some example inputs
print(sum_of_digits(123))  # Output: 6

# -------------------------------
# 2. Fibonacci Sequence
# -------------------------------
# Write a function `fibonacci(n)` that returns the first `n` numbers of the Fibonacci sequence.
# The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

# Test the function with some example inputs
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# -------------------------------
# 3. Multiplication Table
# -------------------------------
# Write a function `multiplication_table(n)` that prints the multiplication table for a given number `n` up to 10.
# For example, if n = 5, the output should be:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Test the function with some example inputs
multiplication_table(5)


# -------------------------------
# 4. Reverse a String
# -------------------------------
# Write a function `reverse_string(s)` that takes a string `s` and returns the string in reverse order.
# For example, if s = "hello", the function should return "olleh".
def reverse_string(s):
    return s[::-1]

# Test the function with some example inputs
print(reverse_string("hello"))  # Output: olleh

# -------------------------------
# 5. Factorial Calculation
# -------------------------------
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.
# The factorial of n is the product of all positive integers less than or equal to n.
# For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
# Test the function with some example inputs
print(factorial(5))  # Output: 120

# -------------------------------
# 6. Print Multiples of 3
# -------------------------------
# Write a function `multiples_of_three(limit)` that prints all multiples of 3 from 1 up to a given `limit`.

def multiples_of_three(limit):
    for i in range(1, limit + 1):
        if i % 3 == 0:
            print(i)

# Test the function with some example inputs
multiples_of_three(20)

# -------------------------------
# 7. Nested Loops for Patterns
# -------------------------------
# Write a function `draw_square(size)` that draws a square pattern of asterisks (*) of size `size` using nested loops.
# For example, if size = 4, the output should be:
# ****
# ****
# ****
# ****
def draw_square(size):
    for i in range(size):
        print("*" * size)
    
# Test the function with some example inputs
draw_square(4)  # Output: ****

# -------------------------------
# 8. Countdown
# -------------------------------
# Write a function `countdown(n)` that counts down from `n` to 0, printing each number on a new line.
def countdown(n):
    for i in range(n, -1, -1):
        print(i)

# Test the function with some example inputs
countdown(5)

# -------------------------------
# 9. Count Occurrences
# -------------------------------
# Write a function `count_occurrences(lst, item)` that counts how many times an `item` appears in a list `lst`.
def count_occurrences(lst, item):
    return lst.count(item)

# Test the function with some example inputs
print(count_occurrences([1, 2, 3, 4, 4, 5], 4))  # Output: 2

# -------------------------------
# 10. String Repetition
# -------------------------------
# Write a function `repeat_string(s, n)` that repeats the string `s` `n` times.
# For example, if s = "hello" and n = 3, the output should be "hellohellohello".
def repeat_string(s, n):
    return s * n

# Test the function with some example inputs
print(repeat_string("hello", 3))  # Output: hellohellohello

# -------------------------------
# 11. Number Pyramid
# -------------------------------
# Write a function `number_pyramid(height)` that prints a pyramid of numbers with the given `height`.
# For example, if height = 5, the output should be:
#     1
#    121
#   12321
#  1234321
# 123454321

def number_pyramid(height):
    for i in range(height):
        print(" " * (height - i - 1), end="")
        for j in range(1, i + 2):
            print(j, end="")
        for j in range(i, 0, -1):
            print(j, end="")
        print()

# Test the function with some example inputs
number_pyramid(5)