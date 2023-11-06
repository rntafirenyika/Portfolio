# Prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.
def spruce(size):
    spacer = size - 1
    multiplier = 1
    
    print("a spruce!")
    for i in range(size):
        space = " " * spacer
        print(space + ("*" * multiplier))
        spacer -= 1
        multiplier += 2
    print((" " * (size - 1)) + "*")

# test function
if __name__ == "__main__":
    spruce(3)