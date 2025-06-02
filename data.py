import math
class Book:
    def __init__(self, title: str, authors: str,  rating: float, reviews: int, price: int, genre: str, year: int):
        self.authors = authors
        self.title = title
        self.rating = rating
        self.reviews = reviews
        self.price = price
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.authors} ({self.year}) - Genre: {self.genre}, Rating: {self.rating}, Reviews: {self.reviews}, Price: ${self.price}"

    def __repr__(self):
        return (f"Book(authors={repr(self.authors)}, title={repr(self.title)}, rating={self.rating}, "
                f"reviews={self.reviews}, price={self.price}, genre={repr(self.genre)}, year={repr(self.year)})")

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.authors == other.authors and
                self.title == other.title and
                self.rating == other.rating and
                self.reviews == other.reviews and
                self.price == other.price and
                self.genre == other.genre and
                self.year == other.year)