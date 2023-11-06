#Returns a list containing n random words from the words.txt file.
#All words begin with the string specified by the second argument.
#No word will appear twice in the list.

from random import sample
 
def words(n: int, beginning: str):
    words = []
    with open("words.txt") as file:
        for word in file:
            if word.startswith(beginning):
                words.append(word.strip())
    if len(words) < 3:
        raise ValueError("Not enough words")
    else:
        select_words = sample(words, n)
    return select_words
 
if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)