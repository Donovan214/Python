"""
   Creating a list and making the exceptions that are needed 
    
"""
top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
               "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]


def main():
    
    try:
        # The number at which we are replacing the artist
        index = int(input("Enter the index of the artist to replace (0-9): "))
        # the new artist replacing the old artist
        new_artist = input("Enter the new artist name: ")
        # putting the new artist in the old artist place
        top_artists[index] = new_artist
        # informing the user what they replaced
        print(f"The artist {index} has been replaced with {new_artist}.")

    except (ValueError, IndexError):
        print("Operator error. Please enter a valid artist.")


main()
