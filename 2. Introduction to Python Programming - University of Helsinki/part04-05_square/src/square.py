# Takes two arguments: an integer and a string.
# Prints out a line of text, the length of which is specified by the first argument.
# Character used to draw the line is the first character in the second argument.
def line(size, text):
    # If the second argument is an empty string, the line consist of stars.
    if text != "":
        print(size*text[0])
    elif text == "":
        print(size*"*")

# Prints out a square of characters, and takes two arguments.
# The first parameter specifies the length of the side of the square.
# The second parameter specifies the character used to draw the square.
def square(size, character):
    for i in range(size):
        line(size, character)

# test function
if __name__ == "__main__":
    square(5, "o")