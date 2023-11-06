# Module for altering strings
import string

#Lowercase letters in the original will be converted to uppercase, and uppercase letters to lowercase.
def change_case(orig_string: str):
    new_str = ""
    for i in range(len(orig_string)):
        if orig_string[i].islower():
            new_str += orig_string[i].upper()
        elif orig_string[i].isupper():
            new_str += orig_string[i].lower()
        else:
            new_str += orig_string[i]
    return new_str

#Splits the parameter string in half, and returns the results in a tuple.
def split_in_half(orig_string: str):
    half = len(orig_string) // 2

    new_str1 = orig_string[0:half]
    new_str2 = orig_string[half:]

    return new_str1, new_str2

#Returns a new version of the parameter string, with all special characters removed.
def remove_special_characters(orig_string: str):
    new_str = ""
    letters = string.ascii_letters + string.digits + " "
    for i in range(len(orig_string)):
        if orig_string[i] not in letters:
            pass
        else:
            new_str += orig_string[i]
    return new_str
