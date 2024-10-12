"""
Creating tuples with programming classes

"""


def main():
   # the different classes to choose from
   programming_classes = ("Intro to Python", "Advanced Python", "Database Essentials", "Web Development Basics",
              "Data Structures in Python", "Web Design")
   for choice in programming_classes:
       # listing all the classes to choose from
       print(choice)
       # tell you how many classes there are to choose from
   print("There are", len(programming_classes), "classes to choose from.")


main()
