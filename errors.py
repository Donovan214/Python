"""
_summary_
    Sample using try and except    
    
"""


def calculate_discount(price, discount):
    assert 0 <= discount <= 100, "Discount must be between 0 and 100"
    return price * (100 - discount) / 100


def main():
    

    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"10 is divided by {num} is: {result}")

    except ZeroDivisionError:
        print("Oops! That can not be divided by zero. Try another number.")

    except ValueError:
        print("That's not a number!")
    except:
        print("That is not a valid input! Please try another number.")


    # try:
    #     # some code that might raise different types of exceptions
    # except Exception as e:
    #     print(f"An error occurred: {e}")

    # try:

    #     # Some operation
    # except SomeException:
    #     # Handle exception
    #     raise  # Re-raise the caught exception

    main()
