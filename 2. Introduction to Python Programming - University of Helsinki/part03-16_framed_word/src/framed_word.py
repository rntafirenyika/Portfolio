# Asks the user for a string and then prints out a frame of * characters with the word in the centre.

string = input("Word: ")

border = "*" * 30
spacing = " " * ((28 - len(string)) // 2)
if len(string) % 2 == 0:
    wordb = "*" + spacing + string + spacing + "*"
else:
    wordb = "*" + spacing + string + spacing + " *"

print(border)
print(wordb)
print(border)