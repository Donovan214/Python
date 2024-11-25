<<<<<<< HEAD
"""

    Creating an Employee database

"""


class Employee:

    def __init__(self, name, number):

        self.name = name
        self.number = number
    # Getter and Setter for name
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    # Getter and Setter number
    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number


class ProductionWorker(Employee):

    def __init__(self, name, number, shift_number, hourly_rate):
        self.name = name
        self.number = number
        self.shift_number = shift_number
        self.hourly_rate = hourly_rate

    def get_shift_number(self):
        return self.shift_number

    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

    def get_hourly_rate(self):
        return self.hourly_rate

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate


def main():
    # Collect user input
    print("Enter the following details of the Employee:")
    name = input("Enter Employee Name: ")
    number = int(input("Enter Employee Number: "))
    pay_rate = float(input("Enter Pay Rate: "))
    shift = int(input("Enter Shift Number (1 for day, 2 for night): "))

    worker = ProductionWorker(name, number, shift, pay_rate)
    # Give employee details back
    print("Details of Employee:")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_number())
    print("Shift:", "Night" if worker.get_shift_number() == 2 else "Day")
    print("Pay Rate:", worker.get_hourly_rate())

main()
=======
"""

    Creating an Employee database

"""


class Employee:

    def __init__(self, name, number):

        self.name = name
        self.number = number
    # Getter and Setter for name
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    # Getter and Setter number
    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number


class ProductionWorker(Employee):

    def __init__(self, name, number, shift_number, hourly_rate):
        self.name = name
        self.number = number
        self.shift_number = shift_number
        self.hourly_rate = hourly_rate

    def get_shift_number(self):
        return self.shift_number

    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

    def get_hourly_rate(self):
        return self.hourly_rate

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate


def main():
    # Collect user input
    print("Enter the following details of the Employee:")
    name = input("Enter Employee Name: ")
    number = int(input("Enter Employee Number: "))
    pay_rate = float(input("Enter Pay Rate: "))
    shift = int(input("Enter Shift Number (1 for day, 2 for night): "))

    worker = ProductionWorker(name, number, shift, pay_rate)
    # Give employee details back
    print("Details of Employee:")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_number())
    print("Shift:", "Night" if worker.get_shift_number() == 2 else "Day")
    print("Pay Rate:", worker.get_hourly_rate())

main()
>>>>>>> b950b21acae417bdd4e628b7d3de2d150057568f
