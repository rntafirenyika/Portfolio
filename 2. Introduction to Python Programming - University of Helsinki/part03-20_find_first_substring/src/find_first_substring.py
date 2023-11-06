# Asks the user to type in a string and a single character.
# Prints the first three character slice which begins with the character specified by the user.

word = input("Please type in a word: ")
char = input("Please type in a character: ")

index = word.find(char)
if (len(word) - 1) - index > 2 and index != -1:
    substring = word[index:index+3]
    print(substring)