"""
Expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str.
Assumes that the value of src will be surrounded by double quotes.
And assumes that the input will contain no more than one such URL. 
"""

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r'.+src=\"https?://(?:www\.)?youtube\.com/embed/(\w+?)\"', s, re.IGNORECASE)
    if url:
        return (f'https://youtu.be/{url.group(1)}')
    else:
        return None



if __name__ == "__main__":
    main()