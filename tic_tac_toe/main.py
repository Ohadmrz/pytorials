from tic_tac_toe.backend.board import *
from tic_tac_toe.frontend.menu_utils import *


def switch_player(game_state):
    game_state['curr_player'] = player1 if \
        game_state['curr_player'] == player2 else player1

if __name__ == '__main__':

    print_greeting()

    player1, player2 = get_player_names()

    board_size = get_board_size()

    board = initialize_board(board_size)

    game_state = {
        'player2char': {player1: 'X', player2: '0'},
        'char2player': {'X': player1, '0':player2},
        'curr_player': player1,
        'board': board
    }

    while True:
        display_turn_prompt(game_state)
        turn: tuple = get_user_turn(game_state)
        update_board_with_turn(game_state['board'], turn)

        winner_char = get_winner(game_state['board'])
        if winner_char:
            print_win_msg(game_state['char2player'][winner_char])
            break
        elif no_moves_left(game_state['board']):
            print_draw_msg()
            break
        switch_player(game_state)

