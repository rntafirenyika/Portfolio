#Takes the lengths of the two sides adjacent to the right angle of an orthogonal triangle.
#Returns the length of the hypotenuse, or the side opposite to the right angle.
from math import sqrt

def hypotenuse(leg1: float, leg2: float):
    leg3 = sqrt(leg1**2 + leg2**2)
    return leg3

if __name__ == "__main__":
    print(hypotenuse(3,4)) # 5.0
    print(hypotenuse(5,12)) # 13.0
    print(hypotenuse(1,1)) # 1.4142135623730951