# Asks the user to type in an upper limit and the base. Prints out powers of base in order.

limit = int(input("Upper limit: "))
base = int(input("Base: "))
doubled = 1

while doubled <= limit:
    print(f"{doubled}")
    doubled *= base