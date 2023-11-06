# Takes a string as its argument.
# Prints out a histogram representing the number of times each letter occurs in the string.

def histogram(string: str):
    histogram = {}
    for letter in string:
        if letter not in histogram:
            histogram[letter] = 0
        # increment the value
        histogram[letter] += 1
    char = "*"
    for key, value in histogram.items():
        print(f"{key} {value * char}")
    return histogram