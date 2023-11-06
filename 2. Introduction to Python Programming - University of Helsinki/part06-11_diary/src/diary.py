# Simple diary - Saves diary entries to a txt file.

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    key = int(input("Function: "))
    if key == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(entry + "\n")
        print("Diary saved")
    elif key == 2:
        print("Entries:")
        with open("diary.txt", "r") as file:
            for line in file:
                print(f"{line.strip()}")
    elif key == 0:
        print("Bye now!")
        break
    print()