"""
    Creating a CRUD (Create, Read, Update, Delete)

"""

def menu():
    print("Please select from the options below: ")
    while True:
        try:
                print(
                    "\\ Welcome! You can create new email entries, change email addresses, delete entries, find entries, or display entries.")
                print("1. Create a new entry")
                print("2. Display an entry by last name")
                print("3. Update an existing entry")
                print("4. Find the exsting entry by last name")
                print("5. Remove an entry")
                print("6. Quit")
                choice = int(
                    input("Please enter the number of your selection (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("That is not a valid number. Try again.")
        except ValueError:
                print("That is not a valid number. Try again.")


def create():
    print("Creating a new entry")
    customer = check()
    fname = input("Please enter the first name: ").capitalize()
    lname = input("Please enter the last name: ").capitalize()
    phone = input("Please enter the phone, include - (111-111-1111): ")
    email = input("Please enter the email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\\n"
    customer.append(entry)
    print(customer)
    save(customer)


def check():
    try:
        file = open("customer_list.txt", 'r')
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []
    

def save(output):
    with open("customer_list.txt", 'w') as file: 
        for line in output:
            file.write(line)
    print("File updated.")


def read():
    print("Reading an entry")


def update():
    customer = check()
    if not customer:
        print("Customer list is empty. Please create an entry first.")
        return

    lname = input(
        "Please enter the last name of the entry you want to update: ").capitalize()
    matching_entries = [entry for entry in customer if lname in entry]

    if not matching_entries:
        print(f"No entry found with the last name '{lname}'.")
        return

    print("\nMatching Entries:")
    for i, entry in enumerate(matching_entries, start=1):
        print(f"{i}. {entry.strip()}")

    try:
        choice = int(
            input("\nEnter the number of the entry you want to update: "))
        if 1 <= choice <= len(matching_entries):
            index = customer.index(matching_entries[choice - 1])
            print("\nUpdating the following entry:")
            print(matching_entries[choice - 1].strip())

            # Get updated details from the user
            fname = input("Enter new first name (leave blank to keep current): ").capitalize(
            ) or matching_entries[choice - 1].split(",")[0].strip()
            lname = input("Enter new last name (leave blank to keep current): ").capitalize(
            ) or matching_entries[choice - 1].split(",")[1].strip()
            phone = input(
                "Enter new phone (format: 111-111-1111, leave blank to keep current): ") or matching_entries[choice - 1].split(",")[2].strip()
            email = input(
                "Enter new email (leave blank to keep current): ") or matching_entries[choice - 1].split(",")[3].strip()

            # Update the entry
            updated_entry = f"{fname}, {lname}, {phone}, {email}\n"
            customer[index] = updated_entry

            save(customer)
            print("\nEntry updated successfully.")
        else:
            print("Invalid selection. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def find():
    print("Looking for that record for you.")
    lname = input("Please enter the last name you are looking for: ")
    customer = check()
    found = [entry for entry in customer if lname in entry]
    if found:
        for entry in found:
            print(entry)
    else:
        print("No entry found with that last name.")


def display():
    customer = check()
    if customer:
        print("Customer List:")
        for entry in customer:
            print(entry.strip())  # To remove extra newlines
    else:
        print("Customer list is empty.")


def delete():
    customer = check()
    lname = input(
        "Please enter the last name of the entry you want to delete: ")
    original_length = len(customer)
    customer = [entry for entry in customer if lname not in entry]
    if len(customer) < original_length:
        print("Entry deleted.")
        save(customer)
    else:
        print("No entry found to delete.")


def main():
    while True:
        choice = menu()
        if choice == 1:
            create()
        elif choice == 2:
            display()
        elif choice == 3:
            update()
        elif choice == 4:
            find()
        elif choice == 5:
            delete()
        elif choice == 6:
            print("Goodbye!")
            break


main()
