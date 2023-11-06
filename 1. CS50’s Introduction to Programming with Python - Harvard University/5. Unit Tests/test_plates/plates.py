"""
Prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
Requirements:
1. “All vanity plates must start with at least two letters.”
2. “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
3. “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
4. “No periods, spaces, or punctuation marks are allowed.”
"""
def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and no_punct(s) is True and check_digits(s) is True:
        return True
    else:
        return False



def no_punct(p):
    if p.isalnum() == True:
        return True
    else:
        return False


def check_digits(q):
    for i, c in enumerate(q):
        if q.isalpha() :
            return True
        else:
            if c.isdigit() :
                d = q[i:]
                if d.isdigit():
                    e = int(d[0:1])
                    if e != 0:
                        return True
                    else:
                        return False
                else:
                    return False








if __name__ == "__main__":
    main()