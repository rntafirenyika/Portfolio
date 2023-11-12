# Takes two integers as its arguments.
# Generator produces even numbers starting from beginning and ending with, at most, maximum.
def even_numbers(beginning: int, maximum: int):
    for i in range(beginning, maximum+1):
        if i % 2 == 0:
            yield i
