# Takes a string argument, returns the character which has the most occurrences within the string.
def most_common_character(text: str) -> str:
    char = ""
    count = 0
    for i in text:
        charcount = text.count(i)
        if count == 0:
            char = i
            count = charcount
        elif charcount > count:
            char = i
            count = charcount
    return char

