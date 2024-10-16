"""
    Adding exceptions to the formula given.

"""

# Simple Python program to calculate the square of a number

def square_number():
    try:        
        # user enters inputs data
        number = int(input("Enter a number to square: "))
        # if input was correct, should calculate code
        squared_number = int(number) ** 2
        # when done calculating should output print message
        print(f"The square of {number} is {squared_number}.")

        # if an error occurs, message will ask user to input correct data
    except ValueError:
        print("The input is not a number. Please Enter a Number.")


square_number()

