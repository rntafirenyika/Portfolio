# Asks the user for a string. Prints out a message based on whether the second character and the second to last character are the same or not.

word = input("Please type in a string: \n")

if word[1] == word[-2]:
    print(f"The second and the second to last characters are {word[1]}")
else:
    print("The second and the second to last characters are different")