from tic_tac_toe.backend.board import initialize_board
from tic_tac_toe.frontend.menu_utils import print_greeting, get_players, get_board_size

if __name__ == '__main__':
    print_greeting()
    player1, player2 = get_players()
    board_size = get_board_size()
    initialize_board(board_size)

    while True:
        pass