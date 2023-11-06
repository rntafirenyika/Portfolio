#Asks the user to type in some text, perform a spell check, and print out feedback to the user.
#All misspelled words have stars around them.

string = input("Write text: ")
words = string.split()

dictionary = []
with open("wordlist.txt") as file:
    for line in file:
        line = line.strip()
        dictionary.append(line)

for i in range(len(words)):
    if words[i].lower() not in dictionary:
        words[i] = f"*{words[i]}*"
    if words[i] == words[-1]:
        print(words[i])
    else:
        print(f"{words[i]} ", end="")
