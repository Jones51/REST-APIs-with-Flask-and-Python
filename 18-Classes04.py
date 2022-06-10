class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighting {self.weight}>"

    @classmethod
    def hardcover(cls, name,page_weight):
        return cls(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name,page_weight):
        return cls(name, Book.TYPES[1], page_weight)

book = Book.hardcover("Harry",  1500)
light = Book.paperback("Bible", 100)

print(book)
print(light)

