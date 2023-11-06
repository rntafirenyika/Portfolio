# Takes a list of strings as its argument.
# Returns a new list with all of the items on the original list reversed.
# The order of items is reversed on the new list.
def everything_reversed(mylist: list) -> list:
    rev = []
    for i in mylist[::-1]:
        rev.append(i[::-1])
    return rev