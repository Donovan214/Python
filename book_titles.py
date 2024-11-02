"""
    Creating and sorting a list of books in a string 
    
"""

def main():
    # The list of entered books
    book_list = []
    # the number of starting books
    count = 0
    # the start of the while loop
    while count < 10:
        # user entering the book titles and Capitalizing each book
        books = input("Please enter the book title: ").title()

        book_list.append(books)
        # adding the books to total 10
        count += 1 
    # Ensuring the books are sorted alphabetically
    sorted_books = sorted(book_list)


    print("\nThe books are now sorted alphabetically:")
    # printing each book in alphabetical order
    for title in sorted_books:

        print(title)
        
main()