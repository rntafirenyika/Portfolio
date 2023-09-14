"""
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art.
Expects zero or two command-line arguments: Zero if the user would like to output text in a random font. Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text. Outputs that text in the desired font.
"""
from pyfiglet import Figlet
from random import choice
import sys


figlet = Figlet()

fonts = figlet.getFonts()

for ufont in fonts:
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid usage")
    elif sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    elif sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    elif len(sys.argv) == 1:
        ufont = figlet.setFont(font=choice(fonts))
    elif len(sys.argv) == 3:
        ufont = figlet.setFont(font=sys.argv[2])

text = input("Input: ")

print(figlet.renderText(text))




