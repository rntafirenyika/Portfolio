# Takes a list of integers as its argument.
# Find and remove the smallest item in the list.
# Assume there is a single smallest item in the list.
def remove_smallest(numbers: list):
    smallest = ""
    for number in numbers:
        if smallest == "":
            smallest = number
        elif number < smallest or smallest == "":
            smallest = number
    numbers.remove(smallest)


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)