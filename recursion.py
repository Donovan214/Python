
# Understanding Main Functions and Other Functions in Python
def greet(name):
    """
    Function to greet a person with their name.
    
    :param name: str - The name of the person to greet.
    :return: None
    """
    print(f"Hello, {name}!")


def main():
    """
    Main function to drive the program.
    """
    # Asking for user input
    user_name = input("Enter your name: ")

    # Calling the greet function
    greet(user_name)

# Launching the program
main()


# Understanding the Fibonacci Sequence with Python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
print(fibonacci(5))  # Output: 5



# Doubling Penny Exercise: Recursive Function in Python
def double_penny(days, amount=0.01):
    """
    Recursive function to calculate the amount of money when a penny is doubled every day.

    days: int - The number of days over which the penny is doubled.
    amount: float - The current amount of money. Default is 0.01, representing 1 penny.
    return: float - The total amount of money after the specified number of days.
    """
    if days == 1:
        return amount
    else:
        return double_penny(days - 1, amount * 2)

# Example usage


def main():
    days = int(input("Enter the number of days: "))
    total_amount = double_penny(days)
    print(f"Total amount after {days} days: ${total_amount:,.2f}")


main()
