"""
Enables a user to place an order, prompting them for items, one per line, until the user inputs control-d.
After each inputted item, displays the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. 
User’s input is treated case insensitively. Input that isn’t an item is ignored. Assumed that every item on the menu will be titlecased.
"""

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

Total = 0

while True :
    try:
        item = input("Item: ").title()
        if item in menu:
            Total = Total + menu.get(item)
            print(f"Total: ${Total:.2f}")

    except EOFError:
        print()
        break









