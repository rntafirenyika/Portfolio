"""
Prompts the user for names, one per line, until the user inputs control-d.
Assumes that the user will input at least one name.
Then bid adieu to those names, separating two names with one 'and', three names with two commas and one 'and', and n names with n-1 commas and one 'and'.
"""
import inflect
p = inflect.engine()

names = []

while True:
    try:
        nameInput = input("Name: ")
        names.append(nameInput)
    except EOFError:
        print()
        break

for name in names:
    if len(names) == 1:
        print(f"Adieu, adieu, to {name}")
    elif len(names) > 1:
        print("Adieu, adieu, to", p.join(names))