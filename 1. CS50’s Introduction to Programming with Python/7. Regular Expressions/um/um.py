"""
Expects a line of text as input as a str and returns, as an int, the number of times that “um” appears in that text, 
case-insensitively, as a word unto itself, not as a substring of some other word.
For instance, given text like hello, um, world, the count function returns 1. Given text like yummy, though, the function returns 0.
"""

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"\bum\b", s.lower())
    count = 0
    for i in match:
        count += 1
    return count



if __name__ == "__main__":
    main()