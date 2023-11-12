import re

# Returns True if the string passed as an argument contains an abbreviation for a day of the week.
def is_dotw(my_string: str):
    abbrevs = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for abbrev in abbrevs:
        if re.search(f"^{abbrev}.*", my_string):
            return True
    return False

# Checks whether all characters in the given string are vowels.
def all_vowels(my_string: str):
    if re.search(f"^[aeiouAEIOU]*$", my_string):
        return True
    return False

# Checks whether a string in the format XX:YY:ZZ is a valid time in the 24-hour format, with two digits each for hours, minutes and seconds.
def time_of_day(my_string: str):
    if re.search(r"^(?:[0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string):
        return True
    return False