#Improved version of the password generator. The function now takes three arguments.
#If the second argument is True, the generated password will also contain one or more numbers.
#If the third argument is True, the generated password will also contain one or more of these special characters: !?=+-()#.

import string
from random import choices, choice

def generate_strong_password(length: int, use_digits: bool, use_special_chars: bool):
    # Define character sets
    chars = string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += "!?=+-()#"

    # Ensure that the password contains at least one digit
    if use_digits:
        password = [choice(string.digits)]
    else:
        password = []

    # Ensure that the password contains at least one special character
    if use_special_chars:
        password.append(choice("!?=+-()#"))

    # Add characters to the password from the character set
    password += choices(chars, k=length - len(password))

    # Shuffle the password to randomize the order
    from random import shuffle
    shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
