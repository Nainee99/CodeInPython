# Lecture 1: Conditionals in Python
# CS50’s Introduction to Programming with Python

# -------------------------------
# 1. Demonstrating Conditionals
# -------------------------------
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# -------------------------------
# 2. Simplified Comparisons
# -------------------------------
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# -------------------------------
# 3. Grading System
# -------------------------------
score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# -------------------------------
# 4. Checking Parity
# -------------------------------
def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

num = int(input("Enter a number to check if it's even or odd: "))
if is_even(num):
    print("Even")
else:
    print("Odd")

# -------------------------------
# 5. Hogwarts House Sorting
# -------------------------------
name = input("What's your name? ").strip()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
