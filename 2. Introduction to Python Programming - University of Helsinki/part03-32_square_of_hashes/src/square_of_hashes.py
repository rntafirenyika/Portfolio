# Takes an integer argument.
# Prints out a square of hash characters, and the argument specifies the length of the side of the square.
def hash_square(length):
    for i in range(length):
        for j in range(length):
            print("#", end="")
        print("")
# test function
if __name__ == "__main__":
    hash_square(5)