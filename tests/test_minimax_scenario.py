from bot.minimax import minimax, minimax_soft_alpha_beta, minimax_alpha_beta, get_depth
from tests import get_all_possible_board_states
from math import inf
from game.board import HUMAN_STATE, BOT_STATE, create_board


def test_blank_board():
    board = create_board()

    minimax_result = minimax(board, get_depth(board), True)
    minimax_soft_alpha_beta_result = minimax_soft_alpha_beta(board, get_depth(board), True, -inf, +inf)
    minimax_alpha_beta_result = minimax_alpha_beta(board, get_depth(board), True, -inf, +inf)

    assert minimax_result == minimax_soft_alpha_beta_result

    assert minimax_alpha_beta_result[0] == minimax_result[0]
    assert minimax_alpha_beta_result[1][0] in minimax_result[1]


def test_board_human_1st_turn():
    for turn_num in range(1, 9):
        boards = get_all_possible_board_states(turn_num, HUMAN_STATE, BOT_STATE)

        is_maximizing_player = False if turn_num % 2 == 0 else True

        for board in boards:
            minimax_result = minimax(board, get_depth(board), is_maximizing_player)
            minimax_soft_alpha_beta_result = minimax_soft_alpha_beta(board, get_depth(board), is_maximizing_player, -inf, +inf)
            minimax_alpha_beta_result = minimax_alpha_beta(board, get_depth(board), is_maximizing_player, -inf, +inf)

            assert minimax_result == minimax_soft_alpha_beta_result

            assert minimax_alpha_beta_result[0] == minimax_result[0]
            assert minimax_alpha_beta_result[1][0] in minimax_result[1]


def test_board_bot_1st_turn():
    for turn_num in range(1, 9):
        boards = get_all_possible_board_states(turn_num, BOT_STATE, HUMAN_STATE)

        is_maximizing_player = True if turn_num % 2 == 0 else False

        for board in boards:
            minimax_result = minimax(board, get_depth(board), is_maximizing_player)
            minimax_soft_alpha_beta_result = minimax_soft_alpha_beta(board, get_depth(board), is_maximizing_player, -inf, +inf)
            minimax_alpha_beta_result = minimax_alpha_beta(board, get_depth(board), is_maximizing_player, -inf, +inf)

            assert minimax_result == minimax_soft_alpha_beta_result

            assert minimax_alpha_beta_result[0] == minimax_result[0]
            assert minimax_alpha_beta_result[1][0] in minimax_result[1]



