class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found!")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book issued successfully!")
        else:
            print("Book is not available!")

    def return_book(self, book):
        self.books.append(book)
        print("Book returned successfully!")

    def display_books(self):
        print("\nAvailable Books:")

        if len(self.books) == 0:
            print("No books available.")
        else:
            for book in self.books:
                print("-", book)


# Create library
library = Library()

library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Java Programming")

library.display_books()

library.issue_book("Python Programming")

library.display_books()

library.return_book("Python Programming")

library.display_books()

library.remove_book("Java Programming")

library.display_books()