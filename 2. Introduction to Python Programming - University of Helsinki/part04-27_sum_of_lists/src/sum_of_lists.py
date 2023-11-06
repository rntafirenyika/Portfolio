# Takes two lists of integers as arguments.
# Returns a new list which contains the sums of the items at each index in the two original lists.

def list_sum(mylist1: list, mylist2: list) -> list:
    summed = []
    for i in range(len(mylist1)):
        summed.append(mylist1[i] + mylist2[i])
    return summed