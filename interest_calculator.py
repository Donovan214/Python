"""Calculating interest and using the return function"""

# return process of the simple interest
def calculate_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# the initial sum of money
principal_amount = int(input("Enter the principal amount: "))
# the rate of interest you will occur
interest_rate = int(input("Enter the interest rate as a whole number(5% would be 5): "))
# the length of time you have to pay back
investment_time = int(input("Enter the investment time in whole years: "))
# calculating the result of all gathered information
calculated_interest = calculate_interest(principal_amount, interest_rate, investment_time)

print(f"The simple interest for a principal amount of ${principal_amount:,.2f} \
                at an interest rate of {interest_rate}% over a period of \
                {investment_time} years is: ${calculated_interest:,.2f}")
