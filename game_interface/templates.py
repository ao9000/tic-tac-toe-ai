"""
    Contain scene templates used in the tic-tac-toe pygame app
"""


from game_interface.pygame_class.textbox import Textbox
from game_interface.pygame_class.shapes.line import Line
from game_interface.pygame_class.shapes.rect import Rect
from game_interface.pygame_class.rectobj import RectObj
from game.board import get_winning_combination_index, BOT_STATE, HUMAN_STATE


# Screen definitions
def selection_screen(screen, mouse_position):
    """
    Render template for selection screen
    Selection screen is where the user selects his mark (X or O)

    Returns all of the objects that needs to be rendered to the screen

    :param screen: type: pygame.surface
    The surface/screen of the game to extract the height & width of the screen

    :param mouse_position: type: tuple
    Tuple of the mouse X & Y coordinates in pygame window

    :return: type: dict
    Dictionary of all the items to be rendered
    """
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


def board_information(screen, records):
    """
    Render template for board information
    Board information shows the number of draws and wins for human & bot

    Returns all of the objects that needs to be rendered to the screen

    :param screen: type: pygame.surface
    The surface/screen of the game to extract the height & width of the screen

    :param records: type: dict
    Dictionary containing all recorded statistics for the current run of the game

    :return: type: dict
    Dictionary of all the items to be rendered
    """
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Frame/layout of information board
    information_board_frame = Rect("light_grey", (0, 0), (width, (height * 1.5 / 10)), 0)

    # Header of the information board
    information_board_header = Textbox("Scoreboard", "black", "arial", 25, (width * 1 / 2), (height * 1 / 40))

    # Text to show number of draws
    draw_header = Textbox("Draws", "green", "arial", 20, (width * 1 / 2), (height * 0.75 / 10))
    draw_count = Textbox(str(records['draw']), "green", "arial", 30, (width * 1 / 2), (height * 1.25 / 10))

    # Text to show number of human wins
    human_win_header = Textbox("Human", "green", "arial", 20, (width * 1 / 3), (height * 0.75 / 10))
    human_win_count = Textbox(str(records['human_win']), "green", "arial", 30, (width * 1 / 3), (height * 1.25 / 10))

    # Text to show number of bot wins
    bot_win_header = Textbox("Bot", "green", "arial", 20, (width * 2 / 3), (height * 0.75 / 10))
    bot_win_count = Textbox(str(records['bot_win']), "green", "arial", 30, (width * 2 / 3), (height * 1.25 / 10))

    interface_items_dict = {
        'information_board_frame': information_board_frame,
        'information_board_header': information_board_header,
        'human_win_count': [human_win_count, human_win_header],
        'bot_win_count': [bot_win_count, bot_win_header],
        'draw_count': [draw_count, draw_header]
    }

    return interface_items_dict


def game_board(screen, board, players):
    """
    Render template for game board screen
    Game board screen contains the tic-tac-toe board and the current states of the board

    Returns all of the objects that needs to be rendered to the screen

    :param screen: type: pygame.surface
    The surface/screen of the game to extract the height & width of the screen

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :param players: type: list
    List containing both human & bot player class instances

    :return: type: dict
    Dictionary of all the items to be rendered
    """
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Calculate boarder
    left_boarder = width * (0.5 / 10)
    right_boarder = width * (0.5 / 10)
    top_boarder = height * (2 / 10)
    bottom_boarder = height * (0.5 / 10)

    # Define board lines
    # First horizontal line
    h1 = Line("black", (left_boarder, top_boarder + (height - (top_boarder + bottom_boarder)) * (1 / 3)), (width - right_boarder, top_boarder + (height - (top_boarder + bottom_boarder)) * (1 / 3)), 3)
    # Second horizontal line
    h2 = Line("black", (left_boarder, top_boarder + (height - (top_boarder + bottom_boarder)) * (2 / 3)), (width - right_boarder, top_boarder + (height - (top_boarder + bottom_boarder)) * (2 / 3)), 3)
    # First vertical line
    v1 = Line("black", (left_boarder + (width - (left_boarder + right_boarder)) * (1 / 3), top_boarder), (left_boarder + (width - (left_boarder + right_boarder)) * (1 / 3), height - bottom_boarder), 3)
    # Second vertical line
    v2 = Line("black", (left_boarder + (width - (left_boarder + right_boarder)) * (2 / 3), top_boarder), (left_boarder + (width - (left_boarder + right_boarder)) * (2 / 3), height - bottom_boarder), 3)

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
                RectObj((min_width + (game_board_width * (box / 3)), min_height + (game_board_height * (row / 3))),
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
    """
    Render template for highlight win
    Highlight win is the action of striking through any winning combinations on the board

    Returns all of the objects that needs to be rendered to the screen

    :param interface_items: type: dict
    Dictionary of all the items to be rendered previously
    This is to find the game board rects from the previously rendered game board

    :param board: type: numpy.ndarray
    The current state of the Tic Tac Toe board game

    :return: type: dict
    Dictionary of all the items to be rendered
    """
    # Get list of winning combination index, only required index 0 and 2
    winning_combination_index = get_winning_combination_index(board)

    # Draw winning combination line
    strikethrough = Line("blue", interface_items['game_board_rects'][winning_combination_index[0][0]][winning_combination_index[0][1]].get_middle_point_coordinates(),
         interface_items['game_board_rects'][winning_combination_index[2][0]][winning_combination_index[2][1]].get_middle_point_coordinates(), 10)

    interface_items_dict = {
        'strikethrough': strikethrough
    }

    return interface_items_dict
