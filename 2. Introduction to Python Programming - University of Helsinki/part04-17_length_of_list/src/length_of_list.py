# Takes a list as its argument and returns the length of the list.
def length(list : list) -> int:
    return len(list)

# test function
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)