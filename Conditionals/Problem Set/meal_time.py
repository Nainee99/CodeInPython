# -------------------------------
# Problem 5: Meal Time
# -------------------------------
# In some countries, meals are typically eaten at specific times of the day:
# - Breakfast: Between 7:00 and 8:00
# - Lunch: Between 12:00 and 13:00
# - Dinner: Between 18:00 and 19:00
#
# Task:
# - Implement a program that:
#   1. Prompts the user for a time (in 24-hour format, e.g., "7:30").
#   2. Converts the input time into a float representing the number of hours.
#   3. Determines whether it's breakfast time, lunch time, or dinner time.
#   4. Outputs the appropriate meal, or nothing if it's not a meal time.
#
# Structure:
# - Define a `main` function to handle the input and output logic.
# - Define a `convert` function to convert a time string into hours as a float.
#
# Example:
# Input: 7:30
# Output: breakfast time
#
# Input: 12:45
# Output: lunch time
#
# Input: 20:00
# Output: (No output)
#
# Hints:
# - Use the `split` method to separate hours and minutes from the time string.
# - Convert minutes into hours by dividing by 60, then add to the hours.
#
# -------------------------------

# Your code starts here:
# -------------------------------
def main():
    # Prompt the user for a time in 24-hour format
    time = input("Enter a time (24-hour format): ")

    # Convert the input time into hours as a float
    hours = convert(time)

    # Determine the meal time
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")


def convert(time):
    """
    Converts a time string in 24-hour format (e.g., "7:30") to the corresponding
    number of hours as a float.
    """
    try:
        # Split the time into hours and minutes
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

        # Convert minutes into hours and add to hours
        return hours + minutes / 60
    except ValueError:
        # If the input is invalid, raise an error
        raise ValueError("Invalid time format. Please use HH:MM format.")


if __name__ == "__main__":
    main()
