from game_interface.pygame_class.rect import Rect
from game_interface.pygame_class.textbox import Textbox
from game_interface.pygame_class.line import Line
from game.board import HUMAN_STATE, BOT_STATE, BLANK_STATE
from bot.minimax import minimax_soft_alpha_beta, get_depth
from math import inf
from game.board import update_board
import random


# Helper functions
def get_board_line_objects(width, height):
    # Calculate boarder
    boarder_width = width * (1 / 10)
    boarder_height = height * (1 / 10)

    # Define board lines
    board_lines = [
        # First horizontal line
        Line("black", (boarder_width, boarder_height + (height - (2 * boarder_height)) * (1 / 3)), (width - boarder_width, boarder_height + (height - (2 * boarder_height)) * (1 / 3)), 3),
        # Second horizontal line
        Line("black", (boarder_width, boarder_height + (height - (2 * boarder_height)) * (2 / 3)), (width - boarder_width, boarder_height + (height - (2 * boarder_height)) * (2 / 3)), 3),
        # First vertical line
        Line("black", (boarder_width + (width - (2 * boarder_width)) * (1 / 3), boarder_height), (boarder_width + (width - (2 * boarder_width)) * (1 / 3), height - boarder_height), 3),
        # Second vertical line
        Line("black", (boarder_width + (width - (2 * boarder_width)) * (2 / 3), boarder_height), (boarder_width + (width - (2 * boarder_width)) * (2 / 3), height - boarder_height), 3)
    ]

    return board_lines


def get_board_rect_objects(width, height):
    # Get box coordinates/positions
    board_box_positions_range = [[], [], []]

    board_lines = get_board_line_objects(width, height)

    # Find max/min coordinates of the lines
    min_width = min(min(line.start_pos[0] for line in board_lines), min(line.end_pos[0] for line in board_lines))
    max_width = max(max(line.start_pos[0] for line in board_lines), max(line.end_pos[0] for line in board_lines))

    min_height = min(min(line.start_pos[1] for line in board_lines), min(line.end_pos[1] for line in board_lines))
    max_height = max(max(line.start_pos[1] for line in board_lines), max(line.end_pos[1] for line in board_lines))

    # Calculate grid area
    box_width = max_width - min_width
    box_height = max_height - min_height

    # Loop board
    for row in range(0, 3):
        for box in range(0, 3):
            board_box_positions_range[row].append(
                Rect((min_width + (box_width * (box / 3)), min_height + (box_height * (row / 3))), (box_width * (1 / 3), box_height * (1 / 3))))

    return board_box_positions_range


def render_move_state_on_board(screen, board):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Get coordinates of box
    board_box_positions_range = get_board_rect_objects(width, height)

    # Draw current moves on board
    for row, row_rect_instance in zip(board, board_box_positions_range):
        for box, box_rect_instance in zip(row, row_rect_instance):
            if box != BLANK_STATE:
                x_pos, y_pos = box_rect_instance.left_top
                width, height = box_rect_instance.width_height
                if box == BOT_STATE:
                    # Bot state
                    Textbox("O", "aqua", "freesans", 124, (x_pos + (width * 1 / 2)),
                            (y_pos + (height * 1 / 2))).draw_to_screen(screen)
                else:
                    # Human state
                    Textbox("X", "firebrick", "freesans", 124, (x_pos + (width * 1 / 2)),
                            (y_pos + (height * 1 / 2))).draw_to_screen(screen)


def human_move_handler(board, screen, event, player):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Get box coordinates/positions
    board_box_positions_range = get_board_rect_objects(width, height)

    # Check intersect, human move
    for row in range(0, 3):
        for box in range(0, 3):
            if board_box_positions_range[row][box].is_clicked_on(event):
                return row, box

    return None


def bot_move_handler(board, player):
    # Minimax algorithm
    _, moves = minimax_soft_alpha_beta(board, get_depth(board), True, -inf, +inf)
    move = random.choice(moves)

    return move
