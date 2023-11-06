# Asks the user for an index and a new value, replace the value at the given index, and print the list again.
numbers = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    if index == -1:
        break
    new_val = int(input("New value: "))

    numbers[index] = new_val

    print(numbers)