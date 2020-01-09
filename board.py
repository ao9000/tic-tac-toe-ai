import numpy as np
from copy import deepcopy

BLANK_STATE = 0
PLAYER_STATE = 1
BOT_STATE = 2


def create_board():
    return np.full((3, 3), BLANK_STATE, dtype=int)


def get_possible_moves(board):
    moves = list()

    for row_index, row in enumerate(board, start=0):
        for box_index, box in enumerate(row, start=0):
            if box == BLANK_STATE:
                moves.append((row_index, box_index))

    return moves


def win_check(board):
    # Straight row win
    for row in board:
        if all(box == PLAYER_STATE for box in row):
            return "Player Wins"
        elif all(box == BOT_STATE for box in row):
            return "Bot wins"

    # Vertical column win
    for col in zip(*board):
        if all(box == PLAYER_STATE for box in col):
            return "Player Wins"
        elif all(box == BOT_STATE for box in col):
            return "Bot wins"

    # Diagonal win \ type
    if all([board[index][index] == PLAYER_STATE for index in range(len(board))]):
        return "Player Wins"
    elif all([board[index][index] == BOT_STATE for index in range(len(board))]):
        return "Bot wins"

    # Diagonal win / type
    if all([board[index][-(index+1)] == PLAYER_STATE for index in range(len(board))]):
        return "Player Wins"
    elif all([board[index][-(index+1)] == BOT_STATE for index in range(len(board))]):
        return "Bot wins"

    return False


def is_board_full(board):
    # Draw
    if not any(BLANK_STATE in row for row in board):
        return True

    return False


def display_board(board, players):
    result = list(map(list, deepcopy(board)))
    for row_index, row in enumerate(board, start=0):
        for box_index, box in enumerate(row, start=0):
            if box == PLAYER_STATE:
                result[row_index][box_index] = next(player.sign for player in players if player.state == PLAYER_STATE)
            elif box == BOT_STATE:
                result[row_index][box_index] = next(player.sign for player in players if player.state == BOT_STATE)
            else:
                result[row_index][box_index] = "_"

    for row in result:
        print(row)


def update_board(board, move, player):
    if board[move[0]][move[1]] == BLANK_STATE:
        board[move[0]][move[1]] = player.state
    else:
        return update_board(board, player.make_move(board), player)

    return board
