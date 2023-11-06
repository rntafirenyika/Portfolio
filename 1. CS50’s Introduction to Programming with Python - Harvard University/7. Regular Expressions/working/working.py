"""
Expects a str in either of the 12-hour format(9:00 AM to 5:00 PM or 9 AM to 5 PM) and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
ValueError raised if the input to convert is not in either of those formats or if either time is invalid.  
"""

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r'^([0-1]?[0-9]:?[0-5]?[0-9]?[ ][a|p][m])[ ]([t][o])[ ]([0-1]?[0-9]:?[0-5]?[0-9]?[ ][a|p][m])$', s, re.IGNORECASE)
    if match :
        return f"{ampm(match.group(1))} {match.group(2)} {ampm(match.group(3))}"
    else:
        raise ValueError



def ampm(str1):
    if match := re.search(r'^([0-1]?[0-9]):?([0-5]?[0-9]?)[ ]([a|p][m])$', str1.upper(), re.IGNORECASE):
        if match.group(2) != "" and int(match.group(1)) < 13:
            # Checking if last two elements of time
            # is AM and first two elements are 12
            if match.group(3) == "AM" and match.group(1) == "12":
                return "00:" + match.group(2)

            # remove the AM
            elif match.group(3) == "AM":
                return f"{int(match.group(1)):02}" + ":" + match.group(2)

            # Checking if last two elements of time
            # is PM and first two elements are 12
            elif match.group(3) == "PM" and match.group(1) == "12":
                return match.group(1) + ":" + match.group(2)

            else:
                # add 12 to hours and remove PM
                return str(int(match.group(1)) + 12) + ":" + match.group(2)
        elif match.group(2) == "" and int(match.group(1)) < 13:
            # Checking if last two elements of time
            # is AM and first two elements are 12
            if match.group(3) == "AM" and match.group(1) == "12":
                return "00:00"

            # remove the AM
            elif match.group(3) == "AM":
                return f"{int(match.group(1)):02}" + ":00"

            # Checking if last two elements of time
            # is PM and first two elements are 12
            elif match.group(3) == "PM" and match.group(1) == "12":
                return match.group(1) + ":00"

            else:
                # add 12 to hours and remove PM
                return str(int(match.group(1)) + 12) + ":00"

        else:
            raise ValueError




if __name__ == "__main__":
    main()