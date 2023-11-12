# Takes a list containing lists of integers as its argument.
# Using list comprehension, returns a new list containing the lengths of the lists within the argument list.
def lengths(lists: list):
    return [len(i) for i in lists]
