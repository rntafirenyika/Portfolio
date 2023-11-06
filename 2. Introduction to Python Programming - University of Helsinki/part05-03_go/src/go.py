# Takes a two-dimensional array as its argument.
# Return the value 1 if player 1 won, and the value 2 if player 2 won.
# If both players have the same number of pieces on the board, returns the value 0.
def who_won(game_board: list):
    pl1 = 0
    pl2 = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                pl1 += 1
            elif game_board[i][j] == 2:
                pl2 += 1
    if pl1 > pl2:
        return 1
    elif pl2 > pl1:
        return 2
    else:
        return 0