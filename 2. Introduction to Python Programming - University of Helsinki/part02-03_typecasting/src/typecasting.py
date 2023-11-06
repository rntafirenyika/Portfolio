# Splitting integer and decimal parts from number input.

number = float(input("Please type in a number: "))
print(f"Integer part: {int(number)}")
print(f"Decimal part: {number - int(number)}")