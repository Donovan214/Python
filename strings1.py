"""
    Finding the ASCII values of strings

"""

def main():
    # user inputs a single character
    user_input = input("Enter a character: ")

    while len(user_input) != 1:
        # if user enters more than one character 
        print("Please enter exactly one character.")
        # asking the user again to input a single character
        user_input = input("Enter a character: ")
    # takes users input and converts into a ASCII value
    ascii_value = ord(user_input)
    # shows the user the value of what they input
    print(f"the ASCII value of {user_input} is {ascii_value}")

    asc = int(input("Please enter an ASCII value: "))

    character = chr(asc)

    print(f"That character would be {character}")

main()