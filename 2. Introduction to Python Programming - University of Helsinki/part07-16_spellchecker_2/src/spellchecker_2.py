#Perform a spell check and print out a list of suggestions for the misspelled words.

from difflib import  get_close_matches

string = input("Write text: ")
words = string.split()

dictionary = []
with open("wordlist.txt") as file:
    for line in file:
        line = line.strip()
        dictionary.append(line)

mis_words = []
for i in range(len(words)):
    if words[i].lower() not in dictionary:
        mis_words.append(words[i])
        words[i] = f"*{words[i]}*"
    if words[i] == words[-1]:
        print(words[i])
    else:
        print(f"{words[i]} ", end="")


print("suggestions:")
for word in mis_words:
    sug_words = get_close_matches(word, dictionary)
    print(f"{word}: ", end="")
    if sug_words:
        for sug_word in sug_words:
            if sug_word == sug_words[-1]:
                print(f"{sug_word}")
            else:
                print(f"{sug_word}, ", end="")
