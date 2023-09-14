"""
Prompts the user for a time and outputs whether it's breakfast time, lunch time, or dinner time.
If it's not time for a meal, the program does not output anything at all.
"""

def main():
    """
    It is assumed that the user's input will be formatted in 24-hour time as #:## or ##:##.
    And it is assumed that each meal's time range is inclusive.
    For instance, whether it's 7:00, 7:01, 7:59, or 8:00, or anytime in between, it's time for breakfast.
    """
    #Prompts the user for the time
    time = input("What time is it? ")

    #Prints "breakfast time", "lunch time", "dinner time" or nothing if it is not a meal time.
    print(convert(time))

def convert(time):
    """
    Converts time, a str in 24-hour format, to the corresponding number of hours as a float.
    For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert returns 7.5 (i.e., 7.5 hours).
    """
    hours, minutes = time.split(":")
    unitime = float(hours) + (float(minutes)/60)
    if 7.0 <= unitime <= 8.0:
        return "breakfast time"
    elif 12.0 <= unitime <= 13.0:
        return "lunch time"
    elif 18.0 <= unitime <= 19.0:
        return "dinner time"
    else:
        return ""


if __name__ == "__main__":
    main()