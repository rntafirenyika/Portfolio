# Asks the user for a year, and prints out the next leap year.

year = int(input("Year: "))

next_leap = year
while True:
    if next_leap % 4 == 0:
        if next_leap < 100 or next_leap % 100 != 0 or (next_leap % 100 == 0 and next_leap % 400 == 0):
            if next_leap == year:
                next_leap += 4
            else:
                break
        else:
            next_leap += 1
    else:
        next_leap += 1

print(f"The next leap year after {year} is {next_leap}")