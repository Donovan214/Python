"""
NATO Phonetic Alphabet    

https://chatgpt.com/share/6709c24b-64e4-8003-936f-ee96ae48aeb0
Used ChatGPT for helping with the for loop in the code
"""
# dictionary for the code
nato_alphabet = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliette",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-Ray",
    "Y": "Yankee",
    "Z": "Zulu"
}
# coverting the word into the NATO alphabet
def spell_word(user_word):
    nato = []
    for letter in user_word:
        # turns the lower case in uppercase
        if letter.upper() in nato_alphabet:
            # turns user input into NATO alphabet
            nato.append(nato_alphabet[letter.upper()])
        else:
            nato.append(letter)
        
    return nato

# main function of the code
def main():
    # user inputs a word
    user_word = input("Please input a word: ")

    user_input = spell_word(user_word)
    # returns the word back in NATO alphabet
    print(user_input)
main()