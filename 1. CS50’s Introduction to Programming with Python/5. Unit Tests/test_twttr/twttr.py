"""
Prompts the user for a string of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
"""
def main():

    txt = input("Input: ")
    print("Output: ", end="")
    print(shorten(txt))


def shorten(word):
    newword = []
    for t in word:
        if t.lower() in ["a", "e", "i", "o", "u"] :
            t = ""
        newword.append(t)
    newword = "".join(newword)
    return newword


if __name__ == "__main__":
    main()