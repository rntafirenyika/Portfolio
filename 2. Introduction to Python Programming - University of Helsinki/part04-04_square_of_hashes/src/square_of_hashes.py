# Takes two arguments: an integer and a string.
# Prints out a line of text, the length of which is specified by the first argument.
# Character used to draw the line is the first character in the second argument.
def line(size, text):
    # If the second argument is an empty string, the line consist of stars.
    if text != "":
        print(size*text[0])
    elif text == "":
        print(size*"*")

# Draws a square of hash characters.
def square_of_hashes(size):
    for i in range(size):
        line(size, "#")

# test function
if __name__ == "__main__":
    square_of_hashes(3)
