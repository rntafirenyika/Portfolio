# Asks for the height, and prints out a rectangle of hash characters accordingly.

width = int(input("Width: "))
height  = int(input("Heigh: "))

while height != 0:
    print("#" * width)
    height -= 1