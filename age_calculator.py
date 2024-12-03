"""
    Creating a Python code to determain your age and brithday 
    
"""


from datetime import datetime

def main():

    try:
        today = datetime.today()
    # User inputs year born 
        birth_year = int(input("What year were you born (in 4 digits)? "))
    # User inputs month born
        month = int(input("What month were you born (as a number, i.e. July would be 7)? "))
    # User inputs day born
        day = int(input("What day of the month were you born (in number)? "))
    # Displays Users birthday
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")

        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output)
    # Displays the number of days
        delta = today - birthday
        print(f'Difference is {delta.days} days')
    # Displays Users current age    
        delta_years = delta.days // 365.25
        print(f'You are {delta_years} years old')

    except Exception as e:
        print(f"Nope!: {e}")
        main()

main()
