"""Names and sorting them"""

# list of names
names = ["Josh", "Patrick", "Trevor", "Aaron", "Matthew"]

swapped = True

# Sorting the names by the alphabet
while swapped:
    swapped = False  
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            swapped = True  
            names[i], names[i + 1] = names[i + 1], names[i]

# Print the sorted list alphabetically
print(names)

# Reverse the list of names
names.reverse()

print(names)
