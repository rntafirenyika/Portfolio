# Takes a list of floating point numbers as its argument.
# Returns a new list, which contains each element of the original list in string format, rounded to two decimal points.
def formatted(mylist: list) -> list:
    flist = []
    for i in mylist:
        flist.append(f"{i:.2f}")
    return flist