# Takes a string argument and an integer argument, and prints out a square of characters.
def squared(text, size):
    Sinput = text * size**2

    index = 0
    for i in range(size):
        print(Sinput[index:index+size])
        index += size
# Testing the function
if __name__ == "__main__":
    squared("aybabtu", 5)