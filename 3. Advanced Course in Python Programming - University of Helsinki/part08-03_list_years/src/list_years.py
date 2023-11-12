#Takes a list of date type objects as its argument.
#Return a new list, which contains the years in the original list in chronological order, from earliest to latest.

from datetime import date

def list_years(dates: list):
    years = []
    for date in dates:
        years.append(date.year)
    years.sort()
    return years
