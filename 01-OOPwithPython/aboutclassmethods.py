class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    ##for recreating the object
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g"


    ## cls is the class , here it is "Book"
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)



print(Book.TYPES)

book = Book("Harry Potter", "hardcover", 1500)

print(book)

book_harry = Book.hardcover("Harry Potter", 1500)
print(book_harry)

book_harry_light = Book.paperback("Harry Potter", 1500)
print(book_harry_light)