#Reads the file and returns the largest number in the file.

def largest():
    with open("numbers.txt") as file:
        numbers = []
        for line in file:
            line = line.replace("\n", "")
            numbers.append(int(line))
    return max(numbers)

