# Lecture 2: Loops in Python
# CS50’s Introduction to Programming with Python

# -------------------------------
# 1. Basic While Loop
# -------------------------------
i = 0
while i < 3:
    print("meow")
    i += 1

# -------------------------------
# 2. For Loop with List
# -------------------------------
for i in [0, 1, 2]:
    print("meow")

# -------------------------------
# 3. For Loop with Range
# -------------------------------
for _ in range(3):
    print("meow")

# -------------------------------
# 4. User Input Validation
# -------------------------------
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

# -------------------------------
# 5. Nested Loops (Printing a Square)
# -------------------------------
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()  # Move to the next line

print_square(3)

# -------------------------------
# 6. Using Loops with Lists
# -------------------------------
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

# -------------------------------
# 7. Using Loops with Dictionaries
# -------------------------------
houses = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in houses:
    print(student, houses[student], sep=", ")
