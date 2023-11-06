# Takes two arguments: an integer and a string.
# Prints out a line of text, the length of which is specified by the first argument.
# Character used to draw the line is the first character in the second argument.
def line(size, text):
    # If the second argument is an empty string, the line consist of stars.
    if text != "":
        print(size*text[0])
    elif text == "":
        print(size*"*")

# Prints first the triangle, and then the rectangle below it.
# The first two parameters specify a triangle, and the character used to draw it.
# The first parameter also specifies the width of a rectangle, while the third parameter specifies its height.
# The fourth parameter specifies the filler character of the rectangle.
def shape(width, tchar, rheight, rchar):
    for i in range(width):
        line((i + 1), tchar)
    for j in range(rheight):
        line(width, rchar)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")