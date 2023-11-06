# Calculates the correct amount of tax for a gift from a close relative.

val = float(input("Value of gift: "))

tax = 0.0
if val >= 1000000:
    tax = 142100 + (val - 1000000) * 0.17
elif 200000 <= val < 1000000:
    tax = 22100 + (val - 200000) * 0.15
elif 55000 <= val < 200000:
    tax = 4700 + (val - 55000) * 0.12
elif 25000 <= val < 55000:
    tax = 1700 + (val - 25000) * 0.10
elif 5000 <= val < 25000:
    tax = 100 + (val - 5000) * 0.08

if tax > 0:
    print(f"Amount of tax: {tax} euros")
else:
    print("No tax!")