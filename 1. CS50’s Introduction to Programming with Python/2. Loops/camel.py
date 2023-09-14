"""
Prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
It is assumed that the user's input will indeed be in camel case.
Camel case in commonly used for variables' names when those names comprise multiple words,
whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase.
Snake case is whereby words are instead separated by underscores (_), with all letters in lowercase.
"""
txt = input("camelCase: ")
print("snake_case: ", end="")

for c in txt:
    if c.isupper():
        c = "_" + c.lower()
    print(c, end="")
print("")