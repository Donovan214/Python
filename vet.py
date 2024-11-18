"""

Creating a Vetenary System for pets

"""

class Pet:
    # veterinary office name
    vet_name = "Veterinary Clinic"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter and Setter for owner_first_name
    def get_owner_first_name(self):
        return self.__owner_first_name

    def set_owner_first_name(self, first_name):
        self.__owner_first_name = first_name

    # Getter and Setter for owner_last_name
    def get_owner_last_name(self):
        return self.__owner_last_name

    def set_owner_last_name(self, last_name):
        self.__owner_last_name = last_name

    # Getter and Setter for pet_id
    def get_pet_id(self):
        return self.__pet_id

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    # Getter and Setter for pet_name
    def get_pet_name(self):
        return self.__pet_name

    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    # Getter and Setter for pet_type
    def get_pet_type(self):
        return self.__pet_type

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    # display pet and owner information
    def display_pet_info(self):
        print(f"Vet Name: {Pet.vet_name}")
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print("-" * 40)



def check_property(obj, property_name):
    return hasattr(obj, property_name)

def main():
    
    pet1 = Pet("Alice", "Smith", 101, "Buddy", "Dog")
    pet2 = Pet("John", "Doe", 102, "Whiskers", "Cat")
    pet3 = Pet("Mary", "Johnson", 103, "Goldie", "Fish")

    
    pet2.set_pet_name("Shadow")
    pet2.set_pet_type("Rabbit")

    
    pet1.display_pet_info()
    pet2.display_pet_info()
    pet3.display_pet_info()

    
    print(check_property(pet1, "_Pet__owner_first_name"))
    print(check_property(pet1, "owner_first_name"))
    print(check_property(pet2, "set_pet_name"))            
    print(check_property(pet3, "random_property"))

main()