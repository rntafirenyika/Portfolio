"""
Prompts the user for items, one per line, until the user inputs control-d
Outputs the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.  
User’s input is treated case-insensitively.
"""

grocery = []
grocerydict = {}


while True:
    try:
        items = input(" ").upper()
        grocery.append(items)
        for i in range(len(grocery)):
            items = [(i, grocery[i])]
            grocerydict.update(items)
    except KeyError:
        pass
    except EOFError:
        print()
        break

listcount = {}
glist = sorted(grocerydict.values())
for items in glist:
    if items in listcount:
        listcount[items] += 1
    else:
        listcount[items] = 1
for key, value in listcount.items():
    print(value, key, sep=" ")