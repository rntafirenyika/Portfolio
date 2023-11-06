"""
Expects the user to provide two command-line arguments:
    1. the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
    2. the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assumes that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program exits via sys.exit with an error message.
"""

import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv") == False:
            sys.exit("Not a CSV file")

    readWriteFiles()

def readWriteFiles():
    try:
        students = []
        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].replace(" ", "").split(",")
                house = row["house"]
                students.append({"first": first, "last": last, "house": house})
        with open(f"{sys.argv[2]}", "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in students:
                writer.writerow(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()