# Keeps asking the user for words. If the user types in end, prints out the story the words formed, and finish.
# Loop ends also if the user types in the same word twice.

story = ""
prev_word = ""

while True:
    word = input("Please type in a word: ")
    if word == "end" or word == prev_word:
        break
    else:
        story += word + " "
        prev_word = word
print(story)