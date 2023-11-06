# Asks the user for a positive integer number.
# Prints out a list of multiplication operations until both operands reach the number given by the user.

number = int(input("Please type in a number: "))
i = 1
while i < number + 1:
    j = 1
    while j < number + 1:
        print(f"{i} x {j} = {i*j}")
        j += 1
    i += 1