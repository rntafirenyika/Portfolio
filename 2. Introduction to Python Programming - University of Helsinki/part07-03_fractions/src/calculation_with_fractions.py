#Takes the number of parts as its argument. Divides the number 1 into as many equal sized fractions as is specified by the argument, and return these in a list.

import fractions

def fractionate(amount):
    fracs = []
    for i in range(amount):
        frac = fractions.Fraction(1, amount)
        fracs.append(frac)
    return fracs

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))