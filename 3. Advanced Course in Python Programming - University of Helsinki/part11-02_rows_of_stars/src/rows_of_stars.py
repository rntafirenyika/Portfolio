# Takes a list of integers as its argument.
# Using list comprehension, return a new list containing rows of stars.
# The length of each row corresponds to the integer at the same index in the original list.

def rows_of_stars(numbers: list):
    return [i * '*' for i in numbers]
