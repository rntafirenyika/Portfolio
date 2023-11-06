# Takes a list of strings as an argument.
# Returns a new list, containing only those items from the original which do not consist of solely uppercase characters.
def no_shouting(mylist: list) -> list:
    noshout = []
    for i in mylist:
        if not i.isupper():
            noshout.append(i)
    return noshout