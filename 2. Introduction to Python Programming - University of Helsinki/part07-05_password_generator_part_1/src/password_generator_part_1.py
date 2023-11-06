#Creates passwords of a desired length, consisting of lowercase characters a to z.

import string
from random import choice

def generate_password(length: int):
    pwd = ""
    for i in range(length):
        pwd += choice(string.ascii_lowercase)
    return pwd

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))