# Asks the user for a string. Prints out the input string in reversed order, from end to beginning.

word = input("Please type in a string: ")

length = len(word)
while length != 0:
    print(word[length - 1])
    length -= 1