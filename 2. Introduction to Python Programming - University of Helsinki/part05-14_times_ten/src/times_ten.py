# Creates and returns a new dictionary.
# The keys of the dictionary are the numbers between start_index and end_index inclusive.
# Value mapped to each key is the key times ten.
def times_ten(start_index: int, end_index: int):
    table = {}
    for i in range(start_index, end_index+1):
        table[i] = i * 10
    return table