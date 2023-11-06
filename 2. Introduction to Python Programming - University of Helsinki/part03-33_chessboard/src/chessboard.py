# Prints out a chessboard made out of ones and zeroes.
# The function takes an integer argument, which specifies the length of the side of the board.
def chessboard(length):
    Einput = "10" * length
    Oinput = "01" * length

    for i in range(length):
        if i % 2 == 0:
            print(Einput[0:length])
        elif i % 2 != 0:
            print(Oinput[0:length])
# Testing the function
if __name__ == "__main__":
    chessboard(3)