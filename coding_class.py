"""
    Deomstration of writing and instantiating a class
"""

# Class definition for a Student
class Student:
    # Initializer with private variables
    def __init__(self, first_name, last_name, studentID, year):
        self.__first_name = first_name  # Private variable for first name
        self.__last_name = last_name    # Private variable for last name
        self.__studentID = studentID    # Private variable for student ID
        self.__year = year              # Private variable for academic year

    # Method to get student's info as a formatted string
    def get_info(self):
        return f"{self.__first_name} {self.__last_name}, ID: {self.__studentID}, Year: {self.__year}"

    # Getter for first_name
    def get_first_name(self):
        return self.__first_name

    # Getter for last_name
    def get_last_name(self):
        return self.__last_name

    # Getter for studentID
    def get_studentID(self):
        return self.__studentID

    # Getter for year
    def get_year(self):
        return self.__year

    # Setter for first_name
    def set_first_name(self, first_name):
        self.__first_name = first_name

    # Setter for last_name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    # Setter for studentID
    def set_studentID(self, studentID):
        self.__studentID = studentID

    # Setter for year
    def set_year(self, year):
        self.__year = year

def main():
    student_1 = Student("Aaron", "Donovan", "123456", "Freshman")
    print(student_1.get_info())
    print(student_1.get_first_name(), student_1.get_last_name())


    student_2 = Student("Barbra", "Streisand", "987654", " Junior")
    print(student_2.get_info())

main()

# Class definition

class Student:
    # Class variable
    school_name = "McHenry County College"

    def __init__(self, first_name, last_name, student_id, grade_level="Freshman"):
        # Instance variables
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__grade_level = grade_level

    # Getter and Setter for first_name
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_student_id(self):
        return self.__student_id

    def get_grade_level(self):
        return self.__grade_level

    def set_first_name(self, value):
        self.__first_name = value

    def set_last_name(self, value):
        self.__last_name = value

    def set_student_id(self, value):
        self.__student_id = value

    def set_grade_level(self, value):
        self.__grade_level = value

    # Method to print student details
    def print_student_details(self):
        print("Student Details:", vars(self))

    # Method to print basic info about the student
    def print_info(self):
        print(self.__first_name + " " + self.__last_name)
        print(self.__student_id)
        print(self.__grade_level)

# Main function to demonstrate usage of the Student class


def main():
    # Creating an instance of Student
    ducktor_quacks = Student("Meri", "Quacksalot", '009234', "Super Senior")
    print("\n\n\n")
    print(ducktor_quacks.get_first_name())
    ducktor_quacks.print_student_details()
    ducktor_quacks.print_info()

    print("\n\n\n")
    ducktor_quacks.set_grade_level("Ducktorate")
    ducktor_quacks.print_info()


# Calling the main function
main()
