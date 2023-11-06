# Asks the user for strings using a loop, prints out each string underlined.

string = input("Please type in a string: ")

while string != "":
    print(string)
    print("-" * len(string))
    string = input("Please type in a string: ")