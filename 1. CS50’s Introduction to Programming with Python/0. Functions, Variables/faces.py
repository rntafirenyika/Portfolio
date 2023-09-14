"""
Prompts the user for input, calls convert function on that input, and prints the result.
convert function accepts a string as input and returns that same input with any :) converted to 🙂 and any :( converted to 🙁.
"""

def main():
    """
    Prompts the user for input, calls convert on that input, and prints the result.
    """
    somewords = input("Please enter your words and emoticon. \n")
    convert(somewords)
    print(convert(somewords))

def convert(somewords):
    """
    Accepts a string as input and returns that same input with any :) converted to 🙂 and any :( converted to 🙁.
    """
    return somewords.replace(":)", "🙂").replace(":(", "🙁")


main()