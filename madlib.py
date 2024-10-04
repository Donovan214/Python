"""Madlib with a song"""

# Bennie and the Jets song

def custom_song(name1, name2, name3, adjective1, adjective2, adjective3, vehicle, shoe, noun):
    print("\n\n")
    # first line in song
    print(f"Say, {name1} and {name2}, have you seen them yet")
    print(f"Ooh, but they're so {adjective1} out yeah")
    print(f"But {name3} and the {vehicle}")
    print(f"Yeah, but they're weird and they're wonderful")
    print(f"Oh, and {name3}, she's really keen")
    print(f"She's got {adjective2} {shoe}")
    print(f"A {adjective3} {noun}")
    print(f"You know I read it in a magazine, oh")
    print(f"{name3} and the {vehicle}")


input_name1 = input("Enter a female name: ")  # one female name required
input_name2 = input("Enter a male name: ")  # at least one male required
input_name3 = input("Enter a thrid name: ")
input_adjective1 = input("Enter an adjective: ")
input_adjective2 = input("Enter another adjective: ")
input_adjective3 = input("Enter a thrid adjective: ")
input_shoe = input("Enter a type of shoe: ")  # song has a type of shoe
input_noun = input("Enter a noun: ")
input_vehicle = input("Enter a type of vehicle: ")  # song displays a vehicle

custom_song(name1=input_name1, name2=input_name2, name3=input_name3, adjective1=input_adjective1, adjective2=input_adjective2,
            adjective3=input_adjective3, shoe=input_shoe, noun=input_noun, vehicle=input_vehicle)
