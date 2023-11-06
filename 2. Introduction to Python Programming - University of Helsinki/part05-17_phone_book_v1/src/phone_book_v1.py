# Phonebook application for storing name and number, and searching the entries. 
phonebook = {}
while True:
    response = int(input("command (1 search, 2 add, 3 quit): "))
    if response == 3:
        print("quitting...")
        break
    elif response == 2:
        name = input("name: ")
        number = input("number: ")
        phonebook[name] = number
        print("ok!")
    elif response == 1:
        name = input("name: ")
        if name in phonebook:
            print(phonebook[name])
        else:
            print("no number")