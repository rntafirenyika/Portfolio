# Takes a list of integers and a limit value (also in integer format) as its arguments.
# Using list comprehension, returns a new list without the values which are smaller than the limit value.
def remove_smaller_than(numbers: list, limit: int):
    return [i for i in numbers if i >= limit]