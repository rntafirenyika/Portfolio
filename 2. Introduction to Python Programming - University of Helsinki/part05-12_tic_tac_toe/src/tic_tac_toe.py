# Places the given symbol at the given coordinates on the board.
def play_turn(game_board: list, x: int, y: int, piece: str):
    valid_ccordinates = [0, 1, 2]
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if x not in valid_ccordinates or y not in valid_ccordinates or game_board[y][x] in ["X", "O"]:
                return False
            else:
                game_board[y][x] = piece
                return True