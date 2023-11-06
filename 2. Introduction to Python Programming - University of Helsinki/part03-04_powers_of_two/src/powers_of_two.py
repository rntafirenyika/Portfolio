# Asks the user to type in an upper limit. Prints out powers of two in order.

limit = int(input("Upper limit: "))
doubled = 1

while doubled <= limit:
    print(f"{doubled}")
    doubled *= 2