# Takes a list of integers as an argument, returns the difference between the smallest and the largest value in the list.
def range_of_list(list: list) -> int:
    sorted_list = sorted(list)
    return sorted_list[-1] - sorted_list[0]

# test function
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)