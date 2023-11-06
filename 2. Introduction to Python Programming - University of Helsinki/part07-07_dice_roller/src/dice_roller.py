#Non-transitive dice - rolls the die specified by the argument.

from random import choice

def roll(die: str):
    A = [3, 3, 3, 3, 3, 6]
    B = [2, 2, 2, 5, 5, 5]
    C = [1, 4, 4, 4, 4, 4]

    match die:
        case "A":
            return choice(A)
        case "B":
            return choice(B)
        case "C":
            return choice(C)


def play(die1: str, die2: str, times: int):
    count1 = 0
    count2 = 0
    tie = 0
    for i in range(times):
        r1 = roll(die1)
        r2 = roll(die2)
        if r1 > r2:
            count1 += 1
        elif r2 >r1:
            count2 += 1
        else:
            tie += 1

    return (count1, count2, tie)