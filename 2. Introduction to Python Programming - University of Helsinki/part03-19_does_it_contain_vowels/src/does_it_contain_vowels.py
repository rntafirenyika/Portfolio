# Asks the user to input a string, prints out different messages if the string contains any of the vowels a, e or o.

string = input("Please type in a string: ")

if "a" in string:
    print("a found")
else:
    print("a not found")

if "e" in string:
    print("e found")
else:
    print("e not found")

if "o" in string:
    print("o found")
else:
    print("o not found")