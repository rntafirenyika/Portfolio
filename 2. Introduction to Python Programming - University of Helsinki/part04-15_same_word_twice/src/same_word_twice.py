# Asks the user for words.
# If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.

words = []
while True:
    word = input("Word: ")
    if word not in words:
        words.append(word)
    else:
        break
print(f"You typed in {len(words)} different words")