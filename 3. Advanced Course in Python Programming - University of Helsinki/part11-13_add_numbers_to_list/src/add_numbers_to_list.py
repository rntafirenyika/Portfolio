# Takes a list of numbers as its argument.
# Using recursion, adds new numbers to the list until the length of the list is divisible by five.
def add_numbers_to_list(numbers: list):
    if len(numbers) % 5 != 0:
        numbers.append(numbers[-1]+1)
        add_numbers_to_list(numbers)
