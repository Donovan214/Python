"""
    Demostrating how to import and use random    

"""
# Getting the random number generated
import random

def main():
    # Generating the random number
    real_number = random.randint(1, 100)
    # Using the while loop in order for the user to guess the number
    while True:

        try:
            # user input a guess or quits the guessing
            guess = input("Enter the number you'd like to guess or type quit to exit: ")

            if guess.lower() == 'quit':
                # in case the user wants to quit the guessing
                print("Thank you for your guess. The number was: ", real_number)

                break

            guess = int(guess)

            if guess == real_number:
                # guessed the random number 
                print("You got the number correct. Congratulations!")

                break

            so_close = abs(guess - real_number)

            if so_close <= 5:
                # very close to the random number
                print("Very Hot")

            elif so_close <= 15:
                # closer to the random number
                print("Hot")

            elif so_close <= 25:
                # somewhat close to the random number
                print("Cool")

            else:
                # Too far away from the random number
                print("Cold")

        except ValueError:
            # User inputs a number that not within the range
            print("The input can not be used. Try a number between 1 and 100.")

main()