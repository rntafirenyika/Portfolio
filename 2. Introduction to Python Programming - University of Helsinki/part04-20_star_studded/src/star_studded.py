# Asks the user to type in a string, prints each input character on a separate line, and a star (*) after each character on a seperate line.
string = input("Please type in a string: ")

for char in string:
    print(char)
    print("*")