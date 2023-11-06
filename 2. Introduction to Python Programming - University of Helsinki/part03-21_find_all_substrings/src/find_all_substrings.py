# Prints out all the substrings which are at least three characters long, and which begin with the character specified by the user.

word = input("Please type in a word: ")
char = input("Please type in a character: ")

while len(word) != 2:
    index = word.find(char)
    if len(word) - index > 2 and index != -1:
        print(word[index:index+3])
        word = word[index+1:]
    else:
        break