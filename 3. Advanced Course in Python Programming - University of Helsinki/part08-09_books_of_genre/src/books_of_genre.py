class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

    # enables easy printing of a Book object
    def __repr__(self):
        return f"{self.name} ({self.author}), {self.year} - genre: {self.genre}"

# Takes a list of objects of type Book and a string representing a genre as its arguments.
# Returns a new list, which contains the books with the desired genre from the original list.
def books_of_genre(books: list, genre: str):
    results = []
    for book in books:
        if book.genre == genre:
            results.append(book)
    return results
