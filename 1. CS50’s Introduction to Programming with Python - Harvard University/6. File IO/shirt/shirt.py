"""
Expects exactly two command-line arguments:
    1. in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    2. n sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program then overlays shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.
The program exits via sys.exit:
    -if the user does not specify exactly two command-line arguments,
    -if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    -if the input’s name does not have the same extension as the output’s name, or
    -if the specified input does not exist.
"""

import sys
from PIL import Image, ImageOps
import os

def main():
    root1, ext1 = os.path.splitext(sys.argv[1])
    root2, ext2 = os.path.splitext(sys.argv[2])
    allowed_types = [".jpg", ".jpeg", ".png"]
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ext1 not in allowed_types or ext2 not in allowed_types:
        sys.exit("Invalid file type")


    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        image1 = Image.open(sys.argv[1])
        image2 = ImageOps.fit(image1, size)
        image2.paste(shirt, shirt)
        image2.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")



if __name__ == "__main__":
    main()