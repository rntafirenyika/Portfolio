# Takes two arguments: an integer and a string.
# Prints out a line of text, the length of which is specified by the first argument.
# Character used to draw the line is the first character in the second argument.
def line(size, text):
    # If the second argument is an empty string, the line consist of stars.
    if text != "":
        print(size*text[0])
    elif text == "":
        print(size*"*")

# Prints out a rectangle of hash characters.
def box_of_hashes(height):
    for i in range(height):
        line(10, "#")

# test function
if __name__ == "__main__":
    box_of_hashes(5)
