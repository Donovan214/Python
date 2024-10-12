


english_to_spanish = {
    "one": "uno",
    "two": "dos",
    "three": "tres",
    "four": "cuatro",
    "five": "cinco",
    "six": "seis",
    "seven": "siete",
    "eight": "ocho",
    "nine": "nueve",
    "ten": "diez"
}

my_dict = {'name': 'John', 'age': 30}
value = my_dict['name']  # Access 'John'

my_dict = {'name': 'John', 'age': 30}
value = my_dict['name']  # Access 'John'

my_dict = {'name': 'John', 'age': 30}
for key in my_dict:
    print(key, my_dict[key])  # Access both key and value

my_dict = {'name': 'John', 'age': 30}
for key, value in my_dict.items():
    print(key, value)  # Access both key and value


# Creating a Multiple Choice Test Program
# Start

# Define main function:
#     Initialize a dictionary 'questions' with English words as keys and lists of Spanish options as values
#     Set score to 0

#     For each word in the 'questions' dictionary:
#         Print the question asking for the Spanish equivalent of the English word
#         Enumerate over the options and print them as multiple-choice options

#         Prompt user to input the number corresponding to their answer
#         If the selected option matches the correct translation:
#             Print "Correct!"
#             Increment score by 1
#         Else:
#             Print "Oops! That's not right."

#     After all questions are asked, print the final score

# End main function

# Call main function

# End

# Ask the user to input the number corresponding to their answer answer = input("Enter the correct number: ") 
# Check if the selected option matches the correct translation in the 'english_to_spanish' 
# dictionary if questions[word][int(answer)-1] == english_to_spanish[word]: print("Correct!") 
# Increment the score for a correct answer score += 1 else: print("Oops! That's not right.") 
# After all questions have been asked, print the final score print(f"Your score: {score}/{len(questions)}") 
# Call the main function to execute the program main()
