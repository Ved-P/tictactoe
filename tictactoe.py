"""
Tic Tac Toe Player
"""

import math

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

    num_x = 0
    num_o = 0

    for row in board:
        for space in row:
            if space == X:
                num_x += 1
            elif space == O:
                num_y += 1

    if num_x == num_y:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    result_board = list(board)

    if result_board[action[0]][action[1]] == EMPTY:
        result_board[action[0]][action[1]] == player(board)
        return result_board
    else:
        raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][2] != EMPTY:
            return board[row][0]

    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[2][col] != EMPTY:
            return board[0][col]

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    for row in board:
        for space in row:
            if space == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    else if winner(board) == O:
        return -1
    else if terminal(board):
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

def max_value(board):

    if terminal(board):
        return utility(board)

    value = -100
    best_action = None

    for action in actions(board):
        new_value = min_value(result(board, action))
        if new_value > value:
            value = new_value
            best_action = action

    return best_action
