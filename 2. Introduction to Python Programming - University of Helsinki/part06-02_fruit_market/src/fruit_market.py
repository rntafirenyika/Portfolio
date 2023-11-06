#Reads the file and returns a dictionary based on the contents.

def read_fruits():
    fruits = {}
    with open("fruits.csv") as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruit = parts[0]
            fruits[fruit] = float(parts[1])
    return fruits
