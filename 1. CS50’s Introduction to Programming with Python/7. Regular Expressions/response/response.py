"""
Prompts the user for an email address via input and then prints Valid or Invalid, respectively, if the input is a syntatically valid email address. 
"""

import validators


def main():
    print(checkValid(input("Whats your email address? ")))

def checkValid(e):
    validation = validators.email(e)
    try:
        if validation == True:
            return "Valid"
        else:
            return "Invalid"
    except Exception :
        return "Invalid"


if __name__ == "__main__":
    main()
