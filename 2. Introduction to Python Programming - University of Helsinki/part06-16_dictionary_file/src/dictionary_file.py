# Functions as a dictionary. The user can type in new entries or look for existing entries.

def read_file():
    dictionary = {}
    try:
        with open("dictionary.txt") as file:
            for row in file:
                row = row.strip().split(":")
                dictionary[row[0]] = row[1]
    except:
        pass
    return dictionary

dictionary = read_file()
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    response = int(input("Function: "))
    if response == 3:
        print("Bye!")
        break
    elif response == 1:
        temp = {}
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        if finnish not in dictionary:
            dictionary[finnish] = english
            temp[finnish] = english
            with open("dictionary.txt", "a") as file:
                file.write(f"{finnish}: {english}\n")
            print("Dictionary entry added")
    elif response == 2:
        name = input("Search term: ")
        for finnish, english in dictionary.items():
            if finnish.find(name) != -1 or english.find(name) != -1:
                print(f"{finnish} - {english.strip()}")
                


