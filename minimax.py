from math import inf
from copy import deepcopy
from board import BOT_STATE, PLAYER_STATE, BLANK_STATE, win_check


def heuristic_evaluation(board):
    # Straight row win
    for row in board:
        if all(box == PLAYER_STATE for box in row):
            return -10
        elif all(box == BOT_STATE for box in row):
            return 10

    # Vertical column win
    for col in zip(*board):
        if all(box == PLAYER_STATE for box in col):
            return -10
        elif all(box == BOT_STATE for box in col):
            return 10

    # Diagonal win \ type
    if all([board[index][index] == PLAYER_STATE for index in range(len(board))]):
        return -10
    elif all([board[index][index] == BOT_STATE for index in range(len(board))]):
        return 10

    # Diagonal win / type
    if all([board[index][-(index + 1)] == PLAYER_STATE for index in range(len(board))]):
        return -10
    elif all([board[index][-(index + 1)] == BOT_STATE for index in range(len(board))]):
        return 10

    # No winners or draw
    return 0


def get_possible_branches(board, is_maximizing_player):
    branches = []
    moves = []

    for row in range(0, 3):
        for box in range(0, 3):
            if board[row][box] == BLANK_STATE:
                # Record move
                moves.append((row, box))

                # Create alternate branches
                branches.append(deepcopy(board))
                branches[-1][row][box] = BOT_STATE if is_maximizing_player else PLAYER_STATE

    return branches, moves


def get_depth(board):
    depth = 0

    # Loop board
    for row in board:
        for box in row:
            if box == BLANK_STATE:
                depth += 1

    return depth


def minimax(board, depth, is_maximizing_player):
    # Check if last node
    if win_check(board) or depth == 0:
        return heuristic_evaluation(board), None

    best_move = ()

    if is_maximizing_player:
        max_score = -inf

        # Loop possible moves in a single turn
        for branch, move in zip(*get_possible_branches(board, True)):
            score, _ = minimax(branch, depth - 1, False)

            if score > max_score:
                max_score = score
                best_move = move

        return max_score, best_move
    else:
        min_score = +inf

        # Loop possible moves in a single turn
        for branch, move in zip(*get_possible_branches(board, False)):
            score, _ = minimax(branch, depth - 1, True)

            if score < min_score:
                min_score = score
                best_move = move

        return min_score, best_move

# def minimax(board, depth, is_maximizing_player):
#     # Check if last node
#     if win_check(board) or depth == 0:
#         return heuristic_evaluation(board)
#
#     if is_maximizing_player:
#         max_score = -inf
#
#         # Loop possible moves in a single turn
#         for branch, move in zip(*get_possible_branches(board, True)):
#             score = minimax(branch, depth - 1, False)
#
#             max_score = max(max_score, score)
#
#         return max_score
#     else:
#         min_score = +inf
#
#         # Loop possible moves in a single turn
#         for branch, move in zip(*get_possible_branches(board, False)):
#             score = minimax(branch, depth - 1, True)
#
#             min_score = min(min_score, score)
#
#         return min_score
