# Prints out the message "hi" and then ask "Shall we continue?" until the user inputs "no".

while True:
    print("hi")
    answer = input("Shall we continue? ")
    if answer.lower() == "no":
        print("okay then")
        break