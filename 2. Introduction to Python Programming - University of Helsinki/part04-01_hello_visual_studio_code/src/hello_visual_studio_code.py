# Asks the user which editor they are using, keep on asking until the user types in Visual Studio Code.
while True:
    answer = input("Editor: ")

    if answer.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif answer.lower() in ["word", "notepad"]:
        print("awful")
    else:
        print("not good")