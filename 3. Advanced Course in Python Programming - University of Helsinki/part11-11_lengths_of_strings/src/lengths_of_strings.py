# Takes a list of strings as its argument.
# Using list comprehension, returns a dictionary with the strings in the list as the keys and their lengths as the values.
def lengths(strings: list):
    return {i: len(i) for i in strings}
