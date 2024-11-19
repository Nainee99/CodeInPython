# -------------------------------
# Problem 5: Tip Calculator
# -------------------------------
# In the United States, it's customary to leave a tip for your server after dining in a restaurant,
# typically an amount equal to 15% or more of your meal’s cost.
#
# You’ve been provided with a basic tip calculator, but two functions need to be implemented:
# - `dollars_to_float`: This function should convert a string formatted as "$##.##" into a float by removing the dollar sign.
# - `percent_to_float`: This function should convert a string formatted as "##%" into a float by removing the percent sign and dividing by 100.
#
# Once these functions are implemented, the program will prompt the user for the cost of the meal and the tip percentage,
# calculate the tip, and print the result.
#
# Task:
# - Implement the `dollars_to_float` function to convert a dollar string into a float.
# - Implement the `percent_to_float` function to convert a percent string into a float.
# - Calculate the tip based on the meal's cost and the tip percentage, then display the amount to tip.
#
# Example:
# Input:
# - How much was the meal? $50.00
# - What percentage would you like to tip? 15%
#
# Output:
# - Leave $7.50
#
# -------------------------------

# Your code starts here:

def main():
    # Prompt for the meal cost and tip percentage
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculate the tip
    tip = dollars * percent
    
    # Output the tip amount, formatted to two decimal places
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # Remove "$" and convert the string to a float
    cleaned_str = d.replace("$", "").strip()
    return float(cleaned_str)

def percent_to_float(p):
    # Remove "%" and convert the string to a float, then divide by 100
    cleaned_str = p.replace("%", "").strip()
    return float(cleaned_str) / 100

# Call the main function to run the program
main()
