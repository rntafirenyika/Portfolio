"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    if [slot for slots in board for slot in slots].count(EMPTY) % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None

    available_moves = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                available_moves.add((i, j))

    return available_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcopy = copy.deepcopy(board)

    active_player = player(board)

    if active_player == X:
        boardcopy[action[0]][action[1]] = X
    elif active_player == O:
        boardcopy[action[0]][action[1]] = O
    else:
        raise ValueError('Invalid action')
    return boardcopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    moves = []
    #Append rows and columns
    for i in range(len(board)):
        moves.append(board[i])
        moves.append([col[i] for col in board])
    #Append primary diagonal
    moves.append([board[i][i] for i in range(len(board))])
    #Append secondary diagonal
    moves.append([board[i][-1 - i] for i in range(len(board))])
    if any(line.count(X) == 3 for line in moves):
        return X
    elif any(line.count(O) == 3 for line in moves):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if any(slot == EMPTY for slot in [slot for slots in board for slot in slots]) == False or winner(board) != None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    gamewinner = winner(board)

    if gamewinner == X:
        return 1
    elif gamewinner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def maxvalue(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, minvalue(result(board, action)))
        return v


    def minvalue(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, maxvalue(result(board, action)))
        return v

    if terminal(board):
        return None

    winning_actions = []
    tie_actions = []

    for action in actions(board):
        vmax = -math.inf
        vmin = math.inf
        maxval = max(vmax, minvalue(result(board, action)))
        minval = min(vmin, maxvalue(result(board, action)))

        if player(board) == X:
            if maxval > 0:
                winning_actions.append(action)
            elif maxval == 0:
                tie_actions.append(action)
        if player(board) == O:
            if minval < 0:
                winning_actions.append(action)
            elif minval == 0:
                tie_actions.append(action)

    if winning_actions != []:
        return winning_actions[0]
    else:
        return tie_actions[0]