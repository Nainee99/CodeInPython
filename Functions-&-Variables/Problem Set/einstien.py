# -------------------------------
# Problem 4: Einstein
# -------------------------------
# Even if you haven’t studied physics (recently or ever!), you might have heard of Einstein's famous equation:
#
# E = mc^2
#
# Where:
# - E is energy (measured in Joules)
# - m is mass (measured in kilograms)
# - c is the speed of light (measured approximately as 300,000,000 meters per second)
#
# The formula expresses the equivalence of mass and energy.
#
# In this program, you will prompt the user for the mass (in kilograms),
# and calculate the equivalent energy (in Joules) using the formula E = mc^2.
#
# Task:
# - Prompt the user for mass as an integer (in kilograms).
# - Calculate the equivalent energy in Joules using E = mc^2.
# - Output the energy as an integer.
#
# Example:
# Input: 10
# Output: 90000000000000000
#
# -------------------------------

# Your code starts here:
# Define the constant for the speed of light
SPEED_OF_LIGHT = 300000000  # in meters per second

# Function to calculate energy from mass using E = mc^2
def calculate_energy(mass):
    return mass * SPEED_OF_LIGHT ** 2

# Main function to get user input and output the calculated energy
def main():
    mass = int(input("Enter mass in kilograms: "))
    energy = calculate_energy(mass)
    print(f"The equivalent energy is {energy} Joules.")

# Call the main function if the script is run directly
if __name__ == "__main__":
    main()