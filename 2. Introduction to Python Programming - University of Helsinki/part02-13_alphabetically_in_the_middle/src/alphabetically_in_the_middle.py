# Asks the user for three letters, prints out whichever of the three letters would be in the middle if the letters were in alphabetical order.

l1 = input("1st letter: ")
l2 = input("2nd letter: ")
l3 = input("3rd letter: ")

word = [l1, l2, l3]
word.sort()
print(f"The letter in the middle is {word[1]}")