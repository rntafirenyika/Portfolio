"""
Expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines.
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program exits via sys.exit.
Assumes that any line that starts with # is a comment. (A docstring is not considered a comment.)
Assumes that any line that only contains whitespace is blank.
"""
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".py") == False:
            sys.exit("Not a Python file")

    print(count_lines())

def count_lines():
    try:
        with open(f"{sys.argv[1]}", "r") as fp:
            count = 0
            for line in fp:
                if line.lstrip() != "" and line.lstrip().startswith("#") == False:
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()