class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        status = 'Available' if self.is_available else 'Checked Out'
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"