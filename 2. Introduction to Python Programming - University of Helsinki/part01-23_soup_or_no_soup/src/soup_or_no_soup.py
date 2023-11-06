#Soup or no soup - If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost.

name = input("Please tell me your name: ")

if name != "Jerry":
    portions = int(input("How many portions of soup? "))
    print(f"The total cost is {portions * 5.90}")

print("Next please!")