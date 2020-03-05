"""
    Contain scene templates used in the tic-tac-toe pygame app
"""


from game_interface.pygame_class.textbox import Textbox
from game_interface.pygame_class.line import Line
from game_interface.pygame_class.rect import Rect
from game.board import get_winning_combination_index, BOT_STATE, HUMAN_STATE


# Screen definitions
def selection_screen(screen, mouse_position):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Render text prompt
    title = Textbox("Select your mark!", "black", "arial", 64, (width * 1 / 2), (height * 1 / 10))

    # Render choices
    # X choice
    x_sign = Textbox("X", "firebrick", "arial", 124, (width * 1 / 3), (height * 1 / 2))
    x_label = Textbox("Cross", "firebrick", "arial", 34, (width * 1 / 3), (height * 2 / 3))

    # Check mouse position, light up choices for interactivity
    if x_sign.is_mouse_hover(mouse_position) or x_label.is_mouse_hover(mouse_position):
        # Change color
        x_sign.text_color = "red"
        x_label.text_color = "red"

    # O choice
    o_sign = Textbox("O", "aqua", "arial", 124, (width * 2 / 3), (height * 1 / 2))
    o_label = Textbox("Nought", "aqua", "arial", 34, (width * 2 / 3), (height * 2 / 3))

    # Check mouse position, light up choices for interactivity
    if o_sign.is_mouse_hover(mouse_position) or o_label.is_mouse_hover(mouse_position):
        # Change color
        o_sign.text_color = "blue"
        o_label.text_color = "blue"

    interface_items_dict = {
        'title': title,
        'x_sign': x_sign,
        'x_label': x_label,
        'o_sign': o_sign,
        'o_label': o_label
    }

    return interface_items_dict


def board_information(screen, player, records):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Text to show number of human wins
    human_win_count = Textbox("Human wins: {}".format(records['human_win']), "green", "arial", 12, (width * 1 / 6), (height * 1 / 20))

    # Text to show number of bot wins
    bot_win_count = Textbox("Bot wins: {}".format(records['bot_win']), "green", "arial", 12, (width * 2 / 6), (height * 1 / 20))

    # Text to show number of draws
    draw_count = Textbox("Draws: {}".format(records['draw']), "green", "arial", 12, (width * 4 / 6), (height * 1 / 20))

    # Text to show whose turn it is
    turn_name = Textbox("{}'s turn".format("Bot" if player.bot else "Human"), "green", "arial", 12, (width * 3 / 6), (height * 1 / 20))

    interface_items_dict = {
        'human_win_count': human_win_count,
        'bot_win_count': bot_win_count,
        'draw_count': draw_count,
        'turn_name': turn_name
    }

    return interface_items_dict


def game_board(screen, board, players):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Calculate boarder
    boarder_width = width * (1 / 10)
    boarder_height = height * (1 / 10)

    # Define board lines
    # First horizontal line
    h1 = Line("black", (boarder_width, boarder_height + (height - (2 * boarder_height)) * (1 / 3)), (width - boarder_width, boarder_height + (height - (2 * boarder_height)) * (1 / 3)), 3)
    # Second horizontal line
    h2 = Line("black", (boarder_width, boarder_height + (height - (2 * boarder_height)) * (2 / 3)), (width - boarder_width, boarder_height + (height - (2 * boarder_height)) * (2 / 3)), 3)
    # First vertical line
    v1 = Line("black", (boarder_width + (width - (2 * boarder_width)) * (1 / 3), boarder_height), (boarder_width + (width - (2 * boarder_width)) * (1 / 3), height - boarder_height), 3)
    # Second vertical line
    v2 = Line("black", (boarder_width + (width - (2 * boarder_width)) * (2 / 3), boarder_height), (boarder_width + (width - (2 * boarder_width)) * (2 / 3), height - boarder_height), 3)

    # Find coordinates of each box in the board
    # Find max/min coordinates of the lines
    game_board_lines = [h1, h2, v1, v2]

    min_width = min(min(line.start_pos[0] for line in game_board_lines), min(line.end_pos[0] for line in game_board_lines))
    max_width = max(max(line.start_pos[0] for line in game_board_lines), max(line.end_pos[0] for line in game_board_lines))

    min_height = min(min(line.start_pos[1] for line in game_board_lines), min(line.end_pos[1] for line in game_board_lines))
    max_height = max(max(line.start_pos[1] for line in game_board_lines), max(line.end_pos[1] for line in game_board_lines))

    # Calculate grid area
    game_board_width = max_width - min_width
    game_board_height = max_height - min_height

    # Divide area and define rect
    game_board_rects = [[], [], []]
    for row in range(0, 3):
        for box in range(0, 3):
            game_board_rects[row].append(
                Rect((min_width + (game_board_width * (box / 3)), min_height + (game_board_height * (row / 3))),
                     (game_board_width * (1 / 3), game_board_height * (1 / 3))))

    # Define objects of current moves on board
    # Get player marks
    bot_mark = next(player.mark for player in players if player.state == BOT_STATE)
    human_mark = next(player.mark for player in players if player.state == HUMAN_STATE)

    current_moves = []
    for row, row_rect_instance in zip(board, game_board_rects):
        for box, box_rect_instance in zip(row, row_rect_instance):
            x_pos, y_pos = box_rect_instance.left_top
            width, height = box_rect_instance.width_height
            if box == BOT_STATE:
                # Bot state or human state
                current_moves.append(Textbox(bot_mark, "aqua" if bot_mark == "O" else "firebrick", "arial", 124,
                                             (x_pos + (width * 1 / 2)), (y_pos + (height * 1 / 2))))
            elif box == HUMAN_STATE:
                # Human state
                current_moves.append(Textbox(human_mark, "aqua" if human_mark == "O" else "firebrick", "arial", 124,
                                             (x_pos + (width * 1 / 2)), (y_pos + (height * 1 / 2))))
            else:
                # Blank state
                current_moves.append(None)

    interface_items_dict = {
        'game_board_lines': game_board_lines,
        'game_board_rects': game_board_rects,
        'current_moves': current_moves
    }

    return interface_items_dict


def highlight_win(interface_items, board):
    # Get list of winning combination index, only required index 0 and 2
    winning_combination_index = get_winning_combination_index(board)

    # Draw winning combination line
    strikethrough = Line("blue", interface_items['game_board_rects'][winning_combination_index[0][0]][winning_combination_index[0][1]].get_middle_point_coordinates(),
         interface_items['game_board_rects'][winning_combination_index[2][0]][winning_combination_index[2][1]].get_middle_point_coordinates(), 10)

    interface_items_dict = {
        'strikethrough':strikethrough
    }

    return interface_items_dict
