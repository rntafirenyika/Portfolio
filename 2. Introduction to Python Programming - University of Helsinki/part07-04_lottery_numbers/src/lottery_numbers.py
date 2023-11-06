#Generates as many random numbers as specified by the first argument.
#All numbers should fall within the bounds lower to upper.
#The numbers are returned as a list in ascending order.

from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper + 1))
    weekly_draw = sample(number_pool, amount)
    weekly_draw.sort()
    return weekly_draw

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)