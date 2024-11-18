"""

    Creating a Pet Class
    
"""

class Pet:
    def __init__(self, kind, breed, name):
        self.kind = kind
        self.breed = breed
        self.name = name

    # Getters
    def get_kind(self):
        return self.kind

    def get_breed(self):
        return self.breed

    def get_name(self):
        return self.name

    # Setters
    def set_kind(self, kind):
        self.kind = kind

    def set_breed(self, breed):
        self.breed = breed

    def set_name(self, name):
        self.name = name

    
    def print_details(self):
        print(f"Kind: {self.kind}, Breed: {self.breed}, Name: {self.name}")

def main():
    # Create three instances of the Pet class
    pet1 = Pet("Dog", "Labrador", "Buddy")
    pet2 = Pet("Cat", "Siamese", "Whiskers")
    pet3 = Pet("Parrot", "Macaw", "Polly")

    # Call print_details 
    pet1.print_details()
    pet2.print_details()
    pet3.print_details()

    # use of various features
    print(f"Class Name (__name__): {Pet.__name__}")
    print(f"Type of pet1: {type(pet1)}")
    print(f"Module (__module__): {Pet.__module__}")
    print(f"Base Classes (__bases__): {Pet.__bases__}")
    print(f"Access attribute using getattr: {getattr(pet1, 'name')}")
    print(f"Is pet1 an instance of Pet? {isinstance(pet1, Pet)}")

main()