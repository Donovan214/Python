"""This code demonstrates the use of logical operators in Python"""

# gathering information

integer_1 = int(input("Enter an integer  "))
integer_2 = int(input("Enter another integer  "))
# and operator
if integer_1 > integer_2:
    print("Both numbers are greater than 0")
elif integer_2 < integer_1:
    print("Both numbers are lower than 100")
else:
    print("Neither number is greater than 0")

# or operator
