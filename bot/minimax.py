"""
    Minimax is a artificial intelligence that uses recursion to create a decision tree that lists all of the
    possible moves of each turn, scores each move and finally selects the move with the best score for the player.

    Minimax assumes both players will play perfectly each time. Therefore, if the human player ever make a mistake,
    the human player will lose.

    Minimax concept:
    There are two type of players in the decision tree, a minimizing player and maximizing player. The minimizing player
    wants to get the lowest possible score possible while the maximizing player wants to get the highest possible score.

    Since minimax runs through all of the possibilities in a decision tree, the time taken to map and account for all of
    the possible moves is significant. Alpha beta pruning is used to skip calculating links in the decision tree that
    do not affect the outcome of the results.
"""

from math import inf
from copy import deepcopy
from game.board import BOT_STATE, HUMAN_STATE, BLANK_STATE, win_check


def heuristic_evaluation(board, depth):
    """
    Gives a minimax score for the state of the board.

    Scoring rules are as follows:
    More than 0 means maximizing player (Bot) wins, the greater the winning score the shorter move is required
    Less than 0 means minimizing player (Human) wins, the smaller the winning score the shorter move is required
    Exactly 0 means a draw

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :param depth: type: int
    How deep the decision tree to search
    The depth at the top of the tree is 0, as you go deeper, depth increases
    Maximum depth is 9, as Tic Tact Toe only have 9 moves available

    :return: type: int
    The minimax score of the board
    """
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

    # No winner/draw
    return 0


def get_possible_branches(board, is_maximizing_player):
    """
    Loops through the board to find possible moves. This function is different from get_possible_moves() in board.py
    Instead of returning all available moves, the function will return the possible board states from the possible moves
    Think of it like a multi-verse of possible boards states.

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :param is_maximizing_player: type: bool
    True if maximizing player's turn (Bot)
    False if minimizing player's turn (Human)

    :return: type: tuple
    Returns a list of all possible boards states in a turn and a list containing the move indexes made in the corresponding board
    """
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
    """
    Loops the Tic Tac Toe board and counts the number of PLAYER_STATES (HUMAN_STATE or BOT_STATE)
    Depth refers to how deep to search in the decision tree.

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :return: type: int
    The total number of HUMAN_STATE and BOT_STATE on the board
    """
    depth = 0

    # Loop board
    for row in board:
        for box in row:
            if box != BLANK_STATE:
                depth += 1

    return depth


def get_winner_from_score(score):
    """
    Interprets the minimax score into a winner message.

    :param score: type: int
    The minimax score of the current board

    :return: type: str if winner is found, else None
    Winner message if winner is found, else None
    """
    if score > 0:
        return "bot"
    elif score < 0:
        return "human"
    else:
        return None


def minimax(board, depth, is_maximizing_player):
    """
    Using minimax algorithm to find the optimal move for the current state of the game.

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :param depth: type: int
    How deep the decision tree to search
    The depth at the top of the tree is 0, as you go deeper, depth increases
    Maximum depth is 9, as Tic Tact Toe only have 9 moves available

    :param is_maximizing_player: type: bool
    True if maximizing player's turn (Bot)
    False if minimizing player's turn (Human)

    :return: type: tuple
    Contains the best minimax score and a list of moves that is derived from that score
    """
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


def minimax_soft_alpha_beta(board, depth, is_maximizing_player, alpha, beta):
    """
    Using minimax algorithm to find the optimal move for the current state of the game.

    This version of the minimax algorithm includes a soft alpha beta pruning. The soft pruning only prunes values that
    are absolutely not possible to make any impact in the results.

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :param depth: type: int
    How deep the decision tree to search
    The depth at the top of the tree is 0, as you go deeper, depth increases
    Maximum depth is 9, as Tic Tact Toe only have 9 moves available

    :param is_maximizing_player: type: bool
    True if maximizing player's turn (Bot)
    False if minimizing player's turn (Human)

    :return: type: tuple
    Contains the best minimax score and a list of moves that is derived from that score
    """
    # Check if last node
    if win_check(board) or depth == 9:
        return heuristic_evaluation(board, depth), None

    best_moves = []

    if is_maximizing_player:
        max_score = -inf

        # Loop possible moves in a single turn
        for branch, move in zip(*get_possible_branches(board, True)):
            score, _ = minimax_soft_alpha_beta(branch, depth + 1, False, alpha, beta)

            if score > max_score:
                max_score = score
                best_moves = [move]
            elif score == max_score:
                best_moves.append(move)

            # Alpha beta pruning
            alpha = max(alpha, score)
            if beta < alpha:
                break

        return max_score, best_moves
    else:
        min_score = +inf

        # Loop possible moves in a single turn
        for branch, move in zip(*get_possible_branches(board, False)):
            score, _ = minimax_soft_alpha_beta(branch, depth + 1, True, alpha, beta)

            if score < min_score:
                min_score = score
                best_moves = [move]
            elif score == min_score:
                best_moves.append(move)

            # Alpha beta pruning
            beta = min(beta, score)
            if beta < alpha:
                break

        return min_score, best_moves


def minimax_alpha_beta(board, depth, is_maximizing_player, alpha, beta):
    """
    Using minimax algorithm to find the optimal move for the current state of the game.

    This version of the minimax algorithm includes alpha beta pruning. The pruning prunes all the values that is
    equal or smaller/larger than the required threshold depending on the player. Thus, this version can only return 1
    move, as the other moves are pruned.

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :param depth: type: int
    How deep the decision tree to search
    The depth at the top of the tree is 0, as you go deeper, depth increases
    Maximum depth is 9, as Tic Tact Toe only have 9 moves available

    :param is_maximizing_player: type: bool
    True if maximizing player's turn (Bot)
    False if minimizing player's turn (Human)

    :return: type: tuple
    Contains the best minimax score and a single move that is derived from that score
    """
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
