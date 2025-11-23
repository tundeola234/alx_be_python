#explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    # Part 1: Display the current date and time
    current_date = datetime.now()
    #Format the date and time in a readable way
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

# Part 2: Calculate a Future Date
def calculate_future_date():
    #Ask the user for the number of days to add
    days = int(input("Enter number of days to add:"))
    
    #Get today's date
    today = datetime.now()

    #Calculate the future date
    future_date = today + timedelta(days=days)

    #Format and display the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    #Print the future date
    print(f"Future date:, {formatted_future_date}")

    #Main Program flow
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
