<<<<<<< HEAD
"""

    Creating a Custom Error

"""


# Define a custom exception
class NotNumericError(Exception):

    def __init__(self, message):
        self.message = message

def main():
# Usage of the custom exception
    try:
        raise NotNumericError("Custom error occurred")
    except NotNumericError as e:
        print(f"Caught an error: {e.message}")
    else:
        print("Change Accepted")
    finally:
        print("Correct Number")

main()
=======
"""

    Creating a Custom Error

"""


# Define a custom exception
class NotNumericError(Exception):

    def __init__(self, message):
        self.message = message

def main():
# Usage of the custom exception
    try:
        raise NotNumericError("Custom error occurred")
    except NotNumericError as e:
        print(f"Caught an error: {e.message}")
    else:
        print("Change Accepted")
    finally:
        print("Correct Number")

main()
>>>>>>> 564fe1c8c2be3afd49ca744829d040aed521546c
