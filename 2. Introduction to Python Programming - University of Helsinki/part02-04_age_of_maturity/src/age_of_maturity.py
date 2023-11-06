# Asks the user for their age. Prints out a message based on whether the user is of age or not, using 18 as the age of maturity.

age = int(input("How old are you? "))

if age >= 18:
    print("You are of age!")
else:
    print("You are not of age!")