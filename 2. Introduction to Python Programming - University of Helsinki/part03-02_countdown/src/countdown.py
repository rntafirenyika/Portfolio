# Prints count down from the number specified.

print("Are you ready?")
number = int(input("Please type in a number: "))
new_num = number
while new_num != 0:
    print(new_num)
    new_num -= 1
print("Now!")