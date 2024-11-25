

# Trying to open a file and handle exceptions
try:
    # Open the file in read mode
    directory = open('addresses.txt', 'r')
    # Read file content
    content = directory.read()
    print(content)
    directory.close()  # Always close the file
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)


def main():
# Writing user input to a file
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    # Open or create the file in write mode
    with open('writing_file/contacts.txt', 'a') as file:
        file.write(name + ', ' + phone + '\n')

main()


# Reading Entire File Content
try:
    with open('reading_files/example.txt', 'r') as file:
        content = file.read()
    print(content)
except IOError:
    print("An IOError has occurred.")


# Reading File Line by Line
try:
    with open('reading_files/example.txt', 'r') as file:
        line = file.readline() # priming read
        line = line.strip('\n')
        while line:
            print(line, end=' ')
            line = file.readline()
            line = line.strip('\n')
except IOError:
    print("An IOError has occurred.")


# Reading All Lines into a List
try:
    with open('reading_files/example.txt', 'r') as file:
        lines = file.readlines()
    print(lines)
except IOError:
    print("An IOError has occurred.")

