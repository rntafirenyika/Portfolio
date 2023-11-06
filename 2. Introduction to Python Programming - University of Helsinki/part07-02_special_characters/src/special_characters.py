#Takes a string as its argument,separates the characters in the string into three other strings, and return these in a tuple.
#The first string contains the lowercase and uppercase ASCII letters.
#The second string contains all punctuation characters defined by the string constant punctuation.
#The third string contains all the other characters (including whitespace).

import string

def separate_characters(my_string: str):
    letters = ""
    pun = ""
    other = ""
    
    for i in my_string:
        if i in string.ascii_letters:
            letters += i
        elif i in string.punctuation:
            pun += i
        else:
            other += i

    return letters, pun, other


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])