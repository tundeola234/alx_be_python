class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False   # private-like attribute

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book to the library (make available)."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []   # private list

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark the book as checked out if it exists and is available."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # book not found

    def return_book(self, title):
        """Return a book to available status."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")