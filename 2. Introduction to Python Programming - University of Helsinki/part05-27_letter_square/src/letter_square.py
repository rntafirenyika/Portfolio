# Prints out a square of letters.
import string

layers = int(input("Layers: "))
chars = list(string.ascii_uppercase)
width = layers * 2 - 1

for i in range(width):
    for j in range(width):
        distance = max(abs(layers - 1 - i), abs(layers - 1 - j))
        print(chars[distance], end="")
    print()
