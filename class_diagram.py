"""_summary_
   
    Creating a class to hold a persons personal data
     
"""

class Person:

    def __init__(self, name, address, age, phone):
        self.name = name          # Private variable for name
        self.address = address    # Private variable for address
        self.age = age            # Private variable for age
        self.phone = phone        # Private variable for phone

    # Method to get user info as a formatted string
    def get_info(self):
        return (f"full name: {self.name}," 
                f"address: {self.address}," 
                f"age: {self.age}," 
                f"phone number: {self.phone}")

    # Getter for name
    def get_name(self):
        return self.name

    # Getter for address
    def get_address(self):
        return self.address

    # Getter for age
    def get_age(self):
        return self.age

    # Getter for phone
    def get_phone(self):
        return self.phone

    # Setter for name
    def set_name(self, name):
        self.name = name

    # Setter for address
    def set_address(self, address):
        self.address = address

    # Setter for age
    def set_age(self, age):
        self.age = age

    # Setter for phone
    def set_phone(self, phone):
        self.phone = phone



def main():
    
    # Collect user input
    name = input("Please enter your full name: ")
    address = input("Please enter your full address: ")
    age = int(input("Please enter your current age: "))
    phone = input("Please enter your full phone number: ")

    # Create a Person object
    person_1 = Person(name, address, age, phone)

    # Print the person's information
    print(person_1.get_info())

main()