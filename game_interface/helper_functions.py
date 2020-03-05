"""
    Contains functions that help with the execution of the tic-tac-toe pygame app
"""


from game.board import BLANK_STATE
from bot.minimax import minimax_soft_alpha_beta, get_depth
from math import inf
from game.board import update_board, BOT_STATE, HUMAN_STATE
from game.player import Player
import random


# Helper functions
def record_win(player, records):
    """
    Record a win of the respective player and reset the turn number

    :param player: type: class 'game.player.Player'
    Player class instance of the player that won

    :param records: type: dict
    Dictionary containing all the recorded statistics of the current run of the game
    """
    # Post game cleanup
    # Record win
    if player.bot:
        records["bot_win"] += 1
    else:
        records["human_win"] += 1

    # Clear turn number
    records['turn_num'] = 0


def record_draw(records):
    """
    Record a draw and reset the turn number

    :param records: type: dict
    Dictionary containing all the recorded statistics of the current run of the game
    """
    # Post game cleanup
    # Record draw
    records["draw"] += 1

    # Clear turn number
    records['turn_num'] = 0


def human_input_selection_screen_handler(interface_items, players, mouse_position):
    """
    Captures the user input during the selection screen, initializes the player class instances depending on the user's
    selection on and append them into the players list.

    :param interface_items: type: dict
    Dictionary containing all of the user interface (UI) items to be displayed. From this dict, we can find the
    references for the objects that the user selects

    :param players: type: list
    Starts off as an empty list, used to contain the initialized players when the user selects a mark

    :param mouse_position: type: tuple
    Tuple of the X & Y coordinates of the mouse cursor on the pygame window
    """
    if interface_items['x_sign'].is_mouse_hover(mouse_position) or interface_items['x_label'].is_mouse_hover(mouse_position):
        # Create players
        bot = Player(bot=True, state=BOT_STATE, mark="O")
        human = Player(bot=False, state=HUMAN_STATE, mark="X")
        players.append(bot)
        players.append(human)

    elif interface_items['o_sign'].is_mouse_hover(mouse_position) or interface_items['o_label'].is_mouse_hover(mouse_position):
        # Create players
        bot = Player(bot=True, state=BOT_STATE, mark="X")
        human = Player(bot=False, state=HUMAN_STATE, mark="O")
        players.append(bot)
        players.append(human)


# Handlers for move input during board scene
def human_move_input_handler(board, interface_items, mouse_position, human):
    """
    Captures the user input during the tic-tac-toe board scene and updates the board depending on the user's selection

    :param board: type: numpy.array
    The current state of the Tic Tac Toe board game

    :param interface_items: type: dict
    Dictionary containing all of the user interface (UI) items to be displayed. From this dict, we can find the
    references for the boxes in the grid

    :param mouse_position: type: tuple
    Tuple of the X & Y coordinates of the mouse cursor on the pygame window

    :param human: type: class 'game.player.Player'
    Player class instance of the human player
    """
    # Check intersect, human move
    for row in range(0, 3):
        for box in range(0, 3):
            if interface_items['game_board_rects'][row][box].is_mouse_hover(mouse_position):
                if board[row][box] == BLANK_STATE:
                    update_board(board, (row, box), human)


def bot_move_input_handler(board, bot):
    """
    Calls the minimax algorithm and calculates the best possible move for the board state and updates the best possible
    move on the board

    :param board: type: numpy.array
    The current state of the Tic Tac Toe board game

    :param bot: type: class 'game.player.Player'
    Player class instance of the bot player
    """
    # Minimax algorithm
    if all(box == BLANK_STATE for row in board for box in row):
        # To reduce load, random the first turn for bot
        row, box = (random.randint(-1, 2), random.randint(-1, 2))
    else:
        # Subsequent turn will not take long to calculate
        _, moves = minimax_soft_alpha_beta(board, get_depth(board), True, -inf, +inf)
        row, box = random.choice(moves)

    update_board(board, (row, box), bot)
