# Takes a list of integers as an argument, returns the arithmetic mean of the values in the list.
def mean(list : list) -> float:
    return sum(list) / len(list)

# test function
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)