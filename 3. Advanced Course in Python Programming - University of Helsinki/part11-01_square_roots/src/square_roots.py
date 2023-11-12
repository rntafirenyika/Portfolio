# Takes a list of integers as its argument.
# Using list comprehension, returns a new list containing the square root of numbers in a list.

from math import sqrt

def square_roots(numbers: list):
    return [sqrt(i) for i in numbers]