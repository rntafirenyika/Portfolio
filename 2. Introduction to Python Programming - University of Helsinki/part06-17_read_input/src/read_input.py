# Asks the user for input until the user types in an integer which falls within the bounds given as arguments to the function.

def read_input(text: str, lLimit: int, uLimit: int) -> int:
    while True:
        try:
            num = int(input(text))
            if lLimit < num < uLimit:
                return num
        except ValueError:
            pass
        print(f"You must type in an integer between {lLimit} and {uLimit}")
