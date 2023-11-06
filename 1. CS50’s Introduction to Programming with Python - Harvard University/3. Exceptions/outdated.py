"""
Prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636.
Output that same date in YYYY-MM-DD format.
If the user’s input is not a valid date in either format, prompts the user again. Assumed that every month has no more than 31 days.
"""

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        #get the date from the user
        rawUserDate = input("Date: ")
        user_date = rawUserDate.replace(" ", "/").replace(",", "").title()
        #split input into month, day and year
        m, d, y = user_date.split("/")
        d = int(d)
        y = int(y)
        if m.isalpha() and "," in rawUserDate:
            for mn in month:
                if m == mn:
                    m = month.index(m) + 1
                    m = int(m)
        elif m.isnumeric():
            m = int(m)
        else:
            pass
        newDate = f"{y}-{m:02}-{d:02}"
        if int(d) <= 31 and int(m) <= 12:
            print(newDate)
            break

    except (KeyError, ValueError):
        pass