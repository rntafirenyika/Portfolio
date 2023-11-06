# Looks for the longest series of neighbours within the list, and returns its length.
def longest_series_of_neighbours(mylist: list) -> int:
    longest = 0
    count = 0
    for i in range(len(mylist)):
        if (i + 1) >= len(mylist):
            break
        if mylist[i+1] - mylist[i] == 1 or mylist[i] - mylist[i+1] == 1:
            count += 1
        else:
            count = 0
        if count > longest:
            longest = count
    if longest > 0:
        longest += 1
    return longest