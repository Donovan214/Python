

#  Function definition
def greet(name):
    print("Hello, " + name + "!")

# Calling the function
greet("Monty")

def magic_py(): # Functions are like magic
    print("It's Magic!") # Call them and something happens

magic_py()

def months(years):
    # calculate how many months old you are (round to years)
    months = 12 * years
    print(f"you are {months} months old!")
months(35)

years = int(input("How many years old are you? "))
months(years)


def add_numbers(number1, number2):
    # number1 and number2 are parameters
    return number1 + number2


result = add_numbers(5, 3)
# 5 and 3 are arguments

# Global variable
number = 10


def multiply(number):
    # The parameter 'number' shadows the global variable 'number'
    return number * 2


# Calling the function
result = multiply(5)

print("Result:", result)
print("Global number:", number)


# Define a function to calculate the area of a rectangle
def rectangle(width, height):
    # Calculate the area (width multiplied by height)
    area = width * height
    # Print the area with a descriptive message
    print(f"The area of the rectangle is {area} square units.")


# Call the rectangle function with width=4 and height=5
rectangle(4, 5)

# Define another function to calculate the area of a rectangle


def calculate_rectangle_area(width, height):
    # Calculate the area and store it in a variable
    area = width * height
    # Use an f-string for more readable code
    print(f"The area of the rectangle is {area} square units.")


# Call the calculate_rectangle_area function with named arguments for clarity
calculate_rectangle_area(width=4, height=5)

# Mary had a little lamb song
def song(name, adjective, animal, place, noun1, noun2):
    print("\n\n")
    print(f"{name} had a {adjective} {animal},")
    print(f"{name} had a {adjective} {animal},")
    print(f"And everywhere that {name} went")
    print(f"The {animal} was sure to go.")
    print()
    print(f"It followed her to {place}")
    print(f"Which was against the {noun1},")
    print(f"It made the {noun2} laugh and play")
    print(f"To see a {animal} at {place}.")


input_name = input("Enter a name: ")
input_adjective = input("Enter an adjective: ")
input_animal = input("Enter an animal: ")
input_place = input("Enter a place: ")
input_noun1 = input("Enter a noun: ")
input_noun2 = input("Enter another noun: ")

song(name=input_name, adjective=input_adjective, animal=input_animal,
     place=input_place, noun1=input_noun1, noun2=input_noun2)

# Returning a result froma function
def add_numbers(number1, number2):
    #add two numbers together
    total = number1 + number2
    return total


# Using the function
result = add_numbers(5, 3)
print("The sum is:", result)
