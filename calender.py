"""
    
    Creating a custom calender

"""
import calendar
from datetime import datetime

def main():

    year = datetime.now().year
    
    while True:
        try:
        # Ask user for the input of a month
            month = int(
                input("What month were you born (as a number, i.e. July would be 7)? "))
        # Ensure user inputs a number of a month
            if 1 <= month <= 12:
                break
        # Ask user to input a number of a month
            else:
                print("Please enter a number of a month.")
        # If user inputs anything other than a number
        except ValueError:
            print("Not Valid. Please enter a number of a month.")
        # Print the calender and current year
    print(calendar.month(year, month))


main()