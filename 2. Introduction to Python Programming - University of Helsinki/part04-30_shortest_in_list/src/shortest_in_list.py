# Takes a list of strings as its argument, returns whichever of the strings is the shortest.
def shortest(mylist: list) -> str:
    shortest = ""
    for i in mylist:
        if shortest == "":
            shortest = i
        elif len(i) < len(shortest):
            shortest = i
    return shortest