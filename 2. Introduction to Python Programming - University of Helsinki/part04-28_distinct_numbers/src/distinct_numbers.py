# Takes a list of integers as its argument.
# Returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.
def distinct_numbers(mylist: list):
    distinct = []
    for i in mylist:
        if i not in distinct:
            distinct.append(i)
    return sorted(distinct)