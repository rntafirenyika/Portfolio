# Asks the user to type in values and adds them to a list.
# After each addition, the list is printed out first in the order the items were added, then ordered from smallest to greatest.

numbers = []
while True:
    number = int(input("New item: "))
    if number == 0:
        print("Bye!")
        break
    numbers.append(number)
    print(f"The list now: {numbers}")
    print(f"The list in order: {sorted(numbers)}")