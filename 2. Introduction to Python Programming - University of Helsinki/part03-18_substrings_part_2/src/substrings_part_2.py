# Asks the user to type in a string. Prints out all the substrings which end with the last character, from the shortest to the longest.

string = input("Please type in a string: ")
length = len(string)
count = length - 1

while length != 0:
    print(string[count:])
    count -= 1
    length -= 1