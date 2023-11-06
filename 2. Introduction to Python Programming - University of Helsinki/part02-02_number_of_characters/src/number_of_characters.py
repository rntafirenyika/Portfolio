#Asks the user for a word and then prints out the number of characters, if there was more than one typed in.

word = input("Please type in a word: ")
lenth = len(word)
if lenth > 1:
    print(f"There are {lenth} letters in the word {word}")

print("Thank you!")