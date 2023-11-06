# Takes a list of strings as its argument. Returns the length of the longest string.
def length_of_longest(mylist: list) -> int:
    longest = 0
    for i in mylist:
        if len(i) > longest:
            longest = len(i)
    return longest