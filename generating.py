<<<<<<< HEAD
"""

    Use of Generator Function

"""


# Generator function to create two-letter combinations from a list of characters
def two_letter_combinations(characters):
    # loops to form combinations of two characters
    for first_char in characters:

        for second_char in characters:
            
            if first_char != second_char:
                
                yield first_char + second_char 
                 


def main():
    # Call the generator function and print each combination
    if __name__ == "__main__":
        # 5 letters
        char_list = ['z', 'x', 'y', 'w', 'v']

        # Call the generator function
        for combination in two_letter_combinations(char_list):
            # Print combination
            print(combination)  

main()
=======
"""

    Use of Generator Function

"""


# Generator function to create two-letter combinations from a list of characters
def two_letter_combinations(characters):
    # loops to form combinations of two characters
    for first_char in characters:

        for second_char in characters:
            
            if first_char != second_char:
                
                yield first_char + second_char 
                 


def main():
    # Call the generator function and print each combination
    if __name__ == "__main__":
        # 5 letters
        char_list = ['z', 'x', 'y', 'w', 'v']

        # Call the generator function
        for combination in two_letter_combinations(char_list):
            # Print combination
            print(combination)  

main()
>>>>>>> 564fe1c8c2be3afd49ca744829d040aed521546c
