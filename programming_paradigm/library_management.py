# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned / available."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        """String representation used when listing books."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        # Private list of Book instances
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("add_book expects a Book instance")

    def check_out_book(self, title):
        """
        Check out the first available book matching title.
        Returns True if successful, False otherwise.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """
        Return the first checked-out book matching title.
        Returns True if successful, False otherwise.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print each available book in the order they were added."""
        for book in self._books:
            if book.is_available():
                print(str(book))
