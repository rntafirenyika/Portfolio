# Returns a new generator for generating random words based on the parameters given.
from random import choice

def word_generator(characters: str, length: int, amount: int):
    return ("".join(choice(characters) for i in range(length)) for j in range(amount))
