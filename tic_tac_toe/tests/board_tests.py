from tic_tac_toe.backend.board import get_row_winner


def test_row_winner1():
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    ret_val = get_row_winner(board)
    assert ret_val is None, \
        'Detected a winner in an empty board'


def test_row_winner2():
    board = [
        ['0', '0', '0'],
        ['X', 'X', None],
        [None, None, None]
    ]
    ret_val = get_row_winner(board)
    assert ret_val == '0', \
        '0 should be a winner'