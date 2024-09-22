"""This code demonstrates the use of logical operators in Python"""

# gathering information

integer_1 = int(input("Enter an integer A  "))
integer_2 = int(input("Enter another integer B  "))
# and operator
if integer_1 > 0 and integer_2 > 0:
    print("Both numbers are greater than 0")
if integer_1 < 100 and integer_2 < 100:
    print("Both numbers are lower than 100")

# or operator
if integer_1 > 0 or integer_2 > 0:
    print("One of the numbers is greater than 0")
else:
    print("Neither number is great than 0")

# not operator
if not integer_1 > integer_2:
    print("A in not bigger than B.")
else:
    print("A is greater than B")
