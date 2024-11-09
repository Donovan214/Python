"""
    Making a list of flowers correctly putting them in order

"""


def main():

    flower_list = []
    # user inputs the flowers they have
    print("Please enter the flowers name (type 'done' when finished): ")

    while True:
        flower = input("Flower name: ").strip()
        if flower.lower() == 'done':
            break
        elif flower:
            flower_list.append(flower)
    # sorting the flowers
    flower_list.sort()
    # the list of flowers
    print("\nHere is the list of flowers: ")
    # putting the list of flowers with a number
    for i, flower in enumerate(flower_list, start=1):
        print(f"{i}. {flower}")
    # user able to look up the flower they wish
    search_flower = input("\nEnter the flower you would like to look up: ").strip()
    # user input could or could not be found
    if search_flower in flower_list:
        print(f"'{search_flower}' has been found in the list.")
    else:
        print(f"'{search_flower}' could not be found in the list.")
    # user able to enter the number of the flower and search that way
    try:
        index = int(index("\nEnter the number for the flower you would like to access: ")) - 1
        print(f"This is the flower with number {index + 1} is '{flower_list[index]}'")
    # all errors 
    except ValueError:
        print(f"Please enter a number.")
    except IndexError:
        print(f"That's not a number! Please enter a number within the list.")
    except Exception as e:
        print("Error has occured: ", e)


main()