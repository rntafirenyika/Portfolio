# Takes a list of strings as its argument, return a new list containing the longest string in the original list.
# If more than one are equally long, returns all of the longest strings.
def all_the_longest(mylist: list) -> list:
    longest = ""
    for i in mylist:
        if longest == "":
            longest = i
        elif len(i) > len(longest):
            longest = i
    longall = []
    for i in mylist:
        if len(i) == len(longest):
            longall.append(i)
    return longall