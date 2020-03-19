class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("Hands ON ML")
book3 = Book("Hands ON ML")
book4 = Book("Hands ON ML")

shelf = BookShelf(book, book2, book3, book4)
print(len(shelf.books))

print(shelf)


