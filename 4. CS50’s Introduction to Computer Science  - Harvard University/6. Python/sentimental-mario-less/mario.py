def main():
    # Get height from user
    height = get_int()

    # Set initial counter
    counter = 1

    # print the pyramid
    while counter <= height:
        print(" " * (height-counter), end="")
        print("#" * counter)
        counter += 1


def get_int():
    # Get interger from user else re-prompt until user input an interger between 1 and 8
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                return height
        except ValueError:
            print("That is not an integer")
            pass


if __name__ == "__main__":
    main()

