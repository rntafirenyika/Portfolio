"""
Expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.
"""
import re
import sys

def main():
    print(validate(input("IP address: ")))



def validate(ip):
    try:
        matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
        if 0 <= int(matches.group(1)) <= 255 and 0 <= int(matches.group(2)) <= 255 and 0 <= int(matches.group(3)) <= 255 and 0 <= int(matches.group(4)) <= 255 :
            return True
        else:
            return False
    except AttributeError:
        return False


if __name__ == "__main__":
    main()