"""
Calculating Factorials

"""

# returns the number and checks it
def factorial (n):
    if n == 1 or 0:
        return n 
    else:
        return factorial(n - 1)
    
    # main function of code
def main():
    # user inputs a number
    n = int(input("Please enter a positive number: "))

    fact_check = factorial(n)
    # returns the number with how many times it can be returned
    print(f"The factorial of {n} is {fact_check}")


main()