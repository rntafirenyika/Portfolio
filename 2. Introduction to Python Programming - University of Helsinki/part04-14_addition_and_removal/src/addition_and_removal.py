# Asks the user to choose between addition and removal.
# Adds an item to or removes an item from the end of a list.
my_list = []
while True:
    print(f"The list is now {my_list}")
    action = input(f"a(d)d, (r)emove or e(x)it: ")
    if my_list == [] and action == "d":
        my_list.append(1)
    elif action == "d":
        my_list.append(my_list[-1] + 1)
    elif action == "r":
        my_list.remove(my_list[-1])
    elif action == "x":
        print("Bye!")
        break