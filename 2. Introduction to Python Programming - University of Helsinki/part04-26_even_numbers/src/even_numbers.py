# Takes a list of integers as an argument.
# Returns a new list containing the even numbers from the original list.
def even_numbers(mylist: list) -> list:
    evens = []
    for i in mylist:
        if i % 2 == 0:
            evens.append(i)
    return evens