# First asks the user for the number of items to be added.
# Then ask for the given number of values, one by one, and add them to a list in the order they were typed in. Finally, the list is printed out.

numbers = []
items = int(input("How many items: "))

count = 0
while items != count:
    item = int(input(f"Item {count+1}: "))
    numbers.append(item)
    count += 1

print(numbers)