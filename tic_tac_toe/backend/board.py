def initialize_board(board_size: int):
    """
    Initialize the game board according to the board size
    received from the user
    """
    pass

def update_board_with_turn(board):
    """
    Update game board with new user turn
    """
    pass


def no_moves_left(board):
    """
    Check whether the game is finished (no more moves left - the board is full)
    """
    pass


def has_winner(board):
    """
    Check whether there is a winner.
    This function should use the following functions to detect
    whether there is a winner:
    row_wins()
    column_wins()
    diagonal_wins()
    """
    pass


def row_wins(board):
    """
    Check whether there is a winner in a row
    """
    pass


def column_wins(board):
    """
    Check whether there is a winner in a column
    """
    pass


def diagonal_wins(board):
    """
    Check whether there is a winner in one of the diagonals
    :return:
    """
    pass


#bonus
def game_stuck(board):
    """
    Bonus: check whether the game is stuck (it is useless to
    continue a game if no one can win - the board is not full,
    but every row, column, and diagonal is filled both with X and O)
    """
    pass