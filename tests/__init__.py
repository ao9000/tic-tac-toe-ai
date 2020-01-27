from board import create_board, get_possible_moves
from copy import deepcopy
from itertools import combinations
from math import floor, ceil
from board import win_check


def get_all_possible_board_states(turn_num, primary_state, secondary_state):
    # Check for valid turn number
    if turn_num < 0 or turn_num > 9:
        raise ValueError("Turn number must be between 0 and 9")

    # Return blank board for turn 0
    if not turn_num:
        return create_board()

    boards = []
    temp_boards = []

    board = create_board()

    # Player for that turn number
    for move in combinations(get_possible_moves(board), ceil(turn_num / 2)):
        temp_boards.append(deepcopy(board))
        for row, box in move:
            temp_boards[-1][row][box] = secondary_state if turn_num % 2 == 0 else primary_state

    # Other player
    for board in temp_boards:
        for move in combinations(get_possible_moves(board), floor(turn_num / 2)):
            boards.append(deepcopy(board))
            for row, box in move:
                boards[-1][row][box] = primary_state if turn_num % 2 == 0 else secondary_state

            # Remove all won/terminal board states
            if win_check(boards[-1]):
                del boards[-1]

    return boards
