# Takes a list of integers as its argument, returns the sum of the positive values in the list.
def sum_of_positives(list: list) -> int:
    total = 0
    for i in list:
        if i > 0:
            total += i
    return total
    
if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)