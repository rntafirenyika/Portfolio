# Asks the user for a number, prints out all integer numbers greater than zero but smaller than the input.

number = int(input("Upper limit: "))
run_mum = 1

while number > 0 and run_mum < number:
    print(f"{run_mum}")
    run_mum += 1