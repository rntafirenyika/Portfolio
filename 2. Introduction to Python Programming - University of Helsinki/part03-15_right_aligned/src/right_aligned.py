# Asks the user for a string and then prints it out so that exactly 20 characters are displayed.
# If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

string = input("Please type in a string: \n")
star = "*" * (20 - len(string))
print(f"{star}{string}")