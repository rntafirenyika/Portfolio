"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
25 cents, 10 cents, and 5 cents.
The program prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, outputs how many cents in change the user is owed.
It is assumed that the user will only input integers, and ignore any integer that isn't an accepted denomination.
"""

i = 50

while i > 0:
    amount = int(input("Insert coin: "))
    if amount in [5, 10, 25] :
        i = i - amount
    if i >= 0 :
        print(f"Amount Due: {i}")
    else:
        change = i * -1
        print(f"Change owed: {change}")