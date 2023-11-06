"""
Prompts the user for the answer to the Great Question of Life, the Universe and Everything,
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise outputs No.
"""

def main():
    #Prompts the user for an answer
    answer = formatans(input("What is the Answer to the Great Question of Life, the Universe, and Everything? \n"))

    #Diplays yes if answer is correct otherwise no
    if answer in ["42", "forty two", "forty-two"]:
        print("Yes")
    else:
        print("No")


def formatans(a):
    #function to strip out spaces and lower cases
    a = a.lower().strip()
    return a


main()