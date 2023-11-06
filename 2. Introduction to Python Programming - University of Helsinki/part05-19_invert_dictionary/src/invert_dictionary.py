# takes a dictionary as its argument.
# Inverts the dictionary so that values become keys and keys become values.
def invert(dictionary: dict):
    copy_dict = {}
    for key, value in dictionary.items():
        copy_dict[key] = value
    dictionary.clear()
    for key, value in copy_dict.items():
        dictionary[value] = key