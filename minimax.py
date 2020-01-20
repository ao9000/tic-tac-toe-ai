from math import inf
from copy import deepcopy
from board import BOT_STATE, HUMAN_STATE, BLANK_STATE, win_check


def heuristic_evaluation(board, depth):
    # Straight row win
    for row in board:
        if all(box == HUMAN_STATE for box in row):
            return -10 + depth
        elif all(box == BOT_STATE for box in row):
            return +10 - depth

    # Vertical column win
    for col in zip(*board):
        if all(box == HUMAN_STATE for box in col):
            return -10 + depth
        elif all(box == BOT_STATE for box in col):
            return +10 - depth

    # Diagonal win \ type
    if all([board[index][index] == HUMAN_STATE for index in range(len(board))]):
        return -10 + depth
    elif all([board[index][index] == BOT_STATE for index in range(len(board))]):
        return +10 - depth

    # Diagonal win / type
    if all([board[index][-(index + 1)] == HUMAN_STATE for index in range(len(board))]):
        return -10 + depth
    elif all([board[index][-(index + 1)] == BOT_STATE for index in range(len(board))]):
        return +10 - depth

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
                branches[-1][row][box] = BOT_STATE if is_maximizing_player else HUMAN_STATE

    return branches, moves


def get_depth(board):
    depth = 0

    # Loop board
    for row in board:
        for box in row:
            if box != BLANK_STATE:
                depth += 1

    return depth


def get_winner_from_score(score):
    if score > 0:
        return "bot"
    elif score < 0:
        return "human"
    else:
        return None


def minimax(board, depth, is_maximizing_player):
    # Check if last node
    if win_check(board) or depth == 9:
        return heuristic_evaluation(board, depth), None

    best_moves = []

    if is_maximizing_player:
        max_score = -inf

        # Loop possible moves in a single turn
        for branch, move in zip(*get_possible_branches(board, True)):
            score, _ = minimax(branch, depth + 1, False)

            if score > max_score:
                max_score = score
                best_moves = [move]
            elif score == max_score:
                best_moves.append(move)

        return max_score, best_moves
    else:
        min_score = +inf

        # Loop possible moves in a single turn
        for branch, move in zip(*get_possible_branches(board, False)):
            score, _ = minimax(branch, depth + 1, True)

            if score < min_score:
                min_score = score
                best_moves = [move]
            elif score == min_score:
                best_moves.append(move)

        return min_score, best_moves


def minimax_alpha_beta(board, depth, is_maximizing_player, alpha, beta):
    # Check if leaf node
    if win_check(board) or depth == 9:
        return heuristic_evaluation(board, depth), None

    best_moves = None

    if is_maximizing_player:
        max_score = -inf

        # Loop possible moves in a single turn
        for branch, move in zip(*get_possible_branches(board, True)):
            score, _ = minimax_alpha_beta(branch, depth + 1, False, alpha, beta)

            if score > max_score:
                max_score = score
                best_moves = [move]

            # Alpha beta pruning
            alpha = max(alpha, score)
            if beta <= alpha:
                break

        return max_score, best_moves
    else:
        min_score = +inf

        # Loop possible moves in a single turn
        for branch, move in zip(*get_possible_branches(board, False)):
            score, _ = minimax_alpha_beta(branch, depth + 1, True, alpha, beta)

            if score < min_score:
                min_score = score
                best_moves = [move]
            elif score == min_score:
                best_moves.append(move)

            # Alpha beta pruning
            beta = min(beta, score)
            if beta <= alpha:
                break

        return min_score, best_moves
