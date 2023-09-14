"""
Expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate module.
The table is formatted using the library’s grid format.
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program exits via sys.exit.
"""

import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv") == False:
            sys.exit("Not a CSV file")

    print(tabulate(read_file(), headers="keys", tablefmt="grid"))

def read_file():
    try:
        pizzaMenu = []
        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizzaMenu.append(row)
            return pizzaMenu
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()