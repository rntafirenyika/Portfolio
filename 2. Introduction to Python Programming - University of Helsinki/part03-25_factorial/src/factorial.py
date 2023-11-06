# Asks the user to type in an integer number.
# If the user types in a number equal to or below 0, the execution ends.
# Otherwise the program prints out the factorial of the number.

while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        print(f"Thanks and bye!")
        break
    i = 1
    factorial = 1
    while i <= number:
        factorial *= i
        i += 1
    print(f"The factorial of the number {number} is {factorial}")