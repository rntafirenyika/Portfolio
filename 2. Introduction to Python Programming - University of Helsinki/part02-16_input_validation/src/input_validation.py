# Asks the user for integer numbers, if the number is above zero, prints out the square root of the number using the Python sqrt function.
# Asks for another number.

from math import sqrt

while True:
    number = float(input("Please type in a number: "))
    if number == 0:
        print("Exiting...")
        break
    elif number < 0:
        print("Invalid number")
    else:
        print(f"{sqrt(number)}")