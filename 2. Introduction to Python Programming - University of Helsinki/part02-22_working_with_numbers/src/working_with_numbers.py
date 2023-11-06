# Asks the user for integer numbers. Keeps asking for numbers until the user types in zero.
# Prints out some statistics on the numbers entered.

count = 0
numsum = 0
positives = 0
negatives = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    elif number < 0:
        negatives += 1
    elif number > 0:
        positives += 1
    count += 1
    numsum += number
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {numsum}")
print(f"The mean of the numbers is {numsum / count}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")