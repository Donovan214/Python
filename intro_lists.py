"""working on lists"""

# append
# Example: Adding an item to a list
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  # Output: [1, 2, 3, 4]

# remove
# Example: Removing an item from a list
# my_list = [1, 2, 3, 2]
# my_list.remove(2)
# print(my_list)  # Output: [1, 3, 2]

# sort
# Example: Sorting a list
# my_list = [3, 1, 4, 1, 5, 9, 2]
# my_list.sort()
# print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 9]

# reverse
# Example: Reversing a list
# my_list = [1, 2, 3]
# my_list.reverse()
# print(my_list)  # Output: [3, 2, 1]

# pop
# Example: Using pop to remove an item
# my_list = [1, 2, 3]
# popped_item = my_list.pop()
# print(popped_item)  # Output: 3
# print(my_list)      # Output: [1, 2]

# len
# Example: Getting the length of a list
# my_list = [1, 2, 3]
# print(len(my_list))  # Output: 3

# List of months in a year
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
# Corresponding list of the number of days in each month
# # Note: This list ignores leap years for February
num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Iterate through each month using a for loop for i in range(len(months)):
# Retrieve the month name from the months list

for i in range(len(months)):
    month = months[i]
    # Retrieve the number of days from the num_of_days list
    days = num_of_days[i]
    # Print the month and its corresponding number of days
    # using the f formatting prevents a problem from concatenating the num_of_days which are integers into the string
    print(f"{month} has {days} days")
    # This loop steps through each index from 0 to 11 (for 12 months)
    # and uses the index to access elements from both lists.
