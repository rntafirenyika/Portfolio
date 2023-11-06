# Asks the user to type in a sentence, prints out the first letter of each word in the sentence, each letter on a separate line.

sentence = input("Please type in a sentence: ")
space = " "

print(sentence[0])
while True:
    index = sentence.find(space)
    if index != -1:
        print(sentence[index+1])
        sentence = sentence[index+1:]
    else:
        break