# Takes a list of integers as its argument, print out lines of star characters.
def list_of_stars(list: list):
    for i in list:
        print(i * "*")

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])