from game.board import BOT_STATE, BLANK_STATE
from bot.minimax import minimax_soft_alpha_beta, get_depth
from math import inf
from game.board import update_board
import random


# Helper functions
def record_win(player, records):
    # Post game cleanup
    # Record win
    if player.bot:
        records["bot_win"] += 1
    else:
        records["human_win"] += 1

    # Clear turn number
    records['turn_num'] = 0


def record_draw(records):
    # Post game cleanup
    # Record draw
    records["draw"] += 1

    # Clear turn number
    records['turn_num'] = 0


def human_move_handler(board, interface_items, mouse_position, human):
    # Check intersect, human move
    for row in range(0, 3):
        for box in range(0, 3):
            if interface_items['game_board_rects'][row][box].is_mouse_hover(mouse_position):
                if board[row][box] == BLANK_STATE:
                    update_board(board, (row, box), human)


def bot_move_handler(board, player):
    # Minimax algorithm
    if all(box == BLANK_STATE for row in board for box in row):
        # To reduce load, random the first turn for bot
        row, box = (random.randint(-1, 2), random.randint(-1, 2))
    else:
        # Subsequent turn will not take long to calculate
        _, moves = minimax_soft_alpha_beta(board, get_depth(board), True, -inf, +inf)
        row, box = random.choice(moves)

    update_board(board, (row, box), player)
