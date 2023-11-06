#Prints out the absolute value of the integer

number = int(input("Please type in a number: "))

if number < 0:
    number = number * -1

print(f"The absolute value of this number is {number}")