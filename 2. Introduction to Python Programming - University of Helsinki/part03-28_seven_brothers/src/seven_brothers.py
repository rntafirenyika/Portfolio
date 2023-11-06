# Prints out the names of the seven brothers in alphabetical order.

def seven_brothers():
    names = ["Aapo", "Eero", "Juhani", "Lauri", "Simeoni", "Timo", "Tuomas"]
    names.sort()
    for name in names:
        print(name)