class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# Takes two objects of type Book as its arguments.
# Prints out a message with the details of whichever is the older.
def older_book(book1: Book, book2: Book):
    if book2.year < book1.year:
        print(f"{book2.name} is older, it was published in {book2.year}")
    elif book2.year > book1.year:
        print(f"{book1.name} is older, it was published in {book1.year}")
    else:
        print(f"{book1.name} and {book2.name} were published in {book1.year}")