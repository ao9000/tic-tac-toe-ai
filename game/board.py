import numpy as np
from copy import deepcopy

BLANK_STATE = 0
HUMAN_STATE = 1
BOT_STATE = 2


def create_board():
    """
    Creates a 3 by 3 numpy array containing BLANK_STATE.

    :return: type: numpy.ndarray
    A blank Tic Tac Toe board represented using numpy array
    """
    return np.full((3, 3), BLANK_STATE, dtype=int)


def get_possible_moves(board):
    """
    Loops through the board to find all BLANK_STATE indexes and place them in a list.

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :return: type: list
    A list of available moves indexes (BLANK_STATE indexes)
    Move indexes are in numpy array format (<row_index>, <column_index>)
    """
    moves = list()

    # Loop board
    for row_index, row in enumerate(board, start=0):
        for box_index, box in enumerate(row, start=0):
            if box == BLANK_STATE:
                # Record indexes of valid moves
                moves.append((row_index, box_index))

    return moves


def win_check(board):
    """
    Checks the board for any winning combinations.

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :return: type: bool
    True if winning combination is found, else False
    """
    # Straight row win
    for row in board:
        if all(box == HUMAN_STATE for box in row) or all(box == BOT_STATE for box in row):
            return True

    # Vertical column win
    for col in zip(*board):
        if all(box == HUMAN_STATE for box in col) or all(box == BOT_STATE for box in col):
            return True

    # Diagonal win \ type
    if all([board[index][index] == HUMAN_STATE for index in range(len(board))]) or \
            all([board[index][index] == BOT_STATE for index in range(len(board))]):
        return True

    # Diagonal win / type
    if all([board[index][-(index+1)] == HUMAN_STATE for index in range(len(board))]) or \
            all([board[index][-(index+1)] == BOT_STATE for index in range(len(board))]):
        return True

    return False


def get_winning_combination_index(board):
    """
    Checks the board for any winning combinations and return the index of the winning indexes.

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :return: type: list
    List of winning indexes
    """
    # Straight row win
    for row_index, row in enumerate(board, start=0):
        if all(box == HUMAN_STATE for box in row) or all(box == BOT_STATE for box in row):
            return [(row_index, box_index) for box_index in range(0, 3)]

    # Vertical column win
    for col_index, col in enumerate(zip(*board), start=0):
        if all(box == HUMAN_STATE for box in col) or all(box == BOT_STATE for box in col):
            return [(row_index, col_index) for row_index in range(0, 3)]

    # Diagonal win \ type
    if all([board[index][index] == HUMAN_STATE for index in range(len(board))]) or \
            all([board[index][index] == BOT_STATE for index in range(len(board))]):
        return [(index, index) for index in range(0, 3)]

    # Diagonal win / type
    if all([board[index][-(index+1)] == HUMAN_STATE for index in range(len(board))]) or \
            all([board[index][-(index+1)] == BOT_STATE for index in range(len(board))]):
        return [(row_index, box_index) for row_index, box_index in zip(range(0, 3), reversed(range(0, 3)))]

    return None


def get_turn_number(board):
    """
    Calculates the total number of moves on the board. The number of moves on the board is the same as the turn number

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :return: type: int
    The number of moves on the board or the turn number
    """
    num_moves = 0

    for row in board:
        for box in row:
            if box != BLANK_STATE:
                num_moves += 1

    return num_moves


def is_board_full(board):
    """
    Check if the board is full, where no moves are available. (Terminal state)
    Use win_check() before this function to check for draw scenario

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :return: type: bool
    True if board is full, else False
    """
    # Check for any BLANK_STATE in board
    if not any(BLANK_STATE in row for row in board):
        return True

    return False


def display_board(board, players):
    """
    Converts all human & bot states on the board to mark and prints the board.

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :param players: type: list
    List containing both human & bot player class instances
    """
    # Convert numpy array into python list
    # Create a copy of the board
    board_copy = deepcopy(board.tolist())

    # Loop board
    for row_index, row in enumerate(board, start=0):
        for box_index, box in enumerate(row, start=0):
            if box == HUMAN_STATE:
                # Human mark
                board_copy[row_index][box_index] = next(player.mark for player in players if player.state == HUMAN_STATE)
            elif box == BOT_STATE:
                # Bot mark
                board_copy[row_index][box_index] = next(player.mark for player in players if player.state == BOT_STATE)
            else:
                # Blank mark
                board_copy[row_index][box_index] = "_"

    # Print board
    for row in board_copy:
        print(row)


def update_board(board, move, player):
    """
    Check if the selected move is valid and not occupied by other player state on the board.

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :param move: type: tuple or list
    Contain the column and row index of the selected move
    Selected move index is in numpy array format (<row_index>, <column_index>)

    :param player: type: player class instance
    The class instance of the player who is making the move (Bot or Human instance)

    :return: type: function
    Returns updated board if valid, else calls itself
    """
    # Check if the selected move is valid (BLANK_STATE)
    if board[move[0]][move[1]] == BLANK_STATE:
        # Replace blank with player state
        board[move[0]][move[1]] = player.state
    else:
        # Invalid move, prompt the user to select a move again
        print("Invalid move, please re-enter move...")
        return update_board(board, player.make_move(board), player)
