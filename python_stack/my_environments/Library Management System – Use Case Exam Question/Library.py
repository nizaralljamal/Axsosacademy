from Book import Book

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author, isbn):
        """Creates a Book object and adds it to the library."""
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Added: {new_book}")

    def find_book(self, title):
        """Finds a book in the library by its title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        """Borrows a book from the library."""
        book = self.find_book(title)
        if book:
            if book.is_available:
                book.is_available = False
                print(f"You have borrowed '{title}'.")
            else:
                print(f"Sorry, '{title}' is already checked out.")
        else:
            print(f"Sorry, the book '{title}' is not in the library catalog.")

    def return_book(self, title):
        """Returns a book to the library."""
        book = self.find_book(title)
        if book:
            if not book.is_available:
                book.is_available = True
                print(f"You have returned '{title}'.")
            else:
                print(f"This book '{title}' was not checked out.")
        else:
            print(f"Invalid book. '{title}' is not in the library catalog.")

    def display_available_books(self):
        """Displays all available books in the library."""
        print(f"\n--- Available Books at {self.name} ---")
        available_books = [book for book in self.books if book.is_available]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)
        print("------------------------------------")

# --- Main execution block ---
if __name__ == "__main__":
    # 1. Create a library instance
    my_library = Library("Axsos Academy Library")

    # 2. Add books to the library
    my_library.add_book("The Lord of the Rings", "J.R.R. Tolkien", "978-0618640157")
    my_library.add_book("Pride and Prejudice", "Jane Austen", "978-0141439518")
    my_library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")

    # 3. Display available books
    my_library.display_available_books()

    # 4. Borrow a book
    print("\n--- Borrowing Books ---")
    my_library.borrow_book("Pride and Prejudice")
    my_library.borrow_book("The Great Gatsby") # Try to borrow a book not in the library

    # 5. Display available books again to see the change
    my_library.display_available_books()
    
    # 6. Try to borrow the same book again
    print("\n--- Trying to Borrow Again ---")
    my_library.borrow_book("Pride and Prejudice")

    # 7. Return a book
    print("\n--- Returning Books ---")
    my_library.return_book("Pride and Prejudice")
    my_library.return_book("Pride and Prejudice") # Try to return a book that wasn't borrowed

    # 8. Display available books one last time
    my_library.display_available_books()