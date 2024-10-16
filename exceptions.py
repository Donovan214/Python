# Try and Except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")



# Else and Finally
try:
    result = 10 / 5
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")
finally:
    print("Execution completed.")


