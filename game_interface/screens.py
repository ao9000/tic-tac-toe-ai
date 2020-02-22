from game_interface.pygame_class.textbox import Textbox
from game_interface.pygame_class.line import Line
from game_interface.helper_functions import render_states_on_board, get_board_line_objects, get_board_rect_objects
from game.board import get_winning_combination_index, BOT_STATE, HUMAN_STATE
from game.player import Player


# Screen definitions
def draw_selection_screen(screen, event, players):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Render text prompt
    Textbox("Select your mark!", "black", "freesans", 64, (width * 1 / 2), (height * 1 / 10)).draw_to_screen(screen)

    # Render choices
    # X choice
    x = Textbox("X", "firebrick", "freesans", 124, (width * 1 / 3), (height * 1 / 2))
    x.draw_to_screen(screen)

    cross = Textbox("Cross", "firebrick", "freesans", 34, (width * 1 / 3), (height * 2 / 3))
    cross.draw_to_screen(screen)

    # O choice
    o = Textbox("O", "aqua", "freesans", 124, (width * 2 / 3), (height * 1 / 2))
    o.draw_to_screen(screen)

    nought = Textbox("Nought", "aqua", "freesans", 34, (width * 2 / 3), (height * 2 / 3))
    nought.draw_to_screen(screen)

    # Check mouse position, light up choices for interactivity
    if x.is_mouse_hover() or cross.is_mouse_hover():
        # Change color and draw
        x.text_color = "red"
        x.draw_to_screen(screen)

        cross.text_color = "red"
        cross.draw_to_screen(screen)

        if x.is_clicked_on(event) or cross.is_clicked_on(event):
            # Create players
            bot = Player(bot=True, state=BOT_STATE, mark="O")
            human = Player(bot=False, state=HUMAN_STATE, mark="X")
            players.append(bot)
            players.append(human)

    elif o.is_mouse_hover() or nought.is_mouse_hover():
        o.text_color = "blue"
        o.draw_to_screen(screen)

        nought.text_color = "blue"
        nought.draw_to_screen(screen)

        if o.is_clicked_on(event) or nought.is_clicked_on(event):
            # Create players
            bot = Player(bot=True, state=BOT_STATE, mark="X")
            human = Player(bot=False, state=HUMAN_STATE, mark="O")
            players.append(bot)
            players.append(human)


def draw_board_information(screen, player, records):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Text to show number of human wins
    Textbox("Human wins: {}".format(records['human_win']), "green", "freesans", 12, (width * 1 / 6), (height * 1 / 20)).draw_to_screen(screen)

    # Text to show number of bot wins
    Textbox("Bot wins: {}".format(records['bot_win']), "green", "freesans", 12, (width * 2 / 6), (height * 1 / 20)).draw_to_screen(screen)

    # Text to show whose turn it is
    Textbox("{}'s turn".format("Bot" if player.bot else "Human"), "green", "freesans", 12, (width * 3 / 6), (height * 1 / 20)).draw_to_screen(screen)

    # Text to show number of draws
    Textbox("Draws: {}".format(records['draw']), "green", "freesans", 12, (width * 4 / 6), (height * 1 / 20)).draw_to_screen(screen)


def draw_board(screen, board):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Draw to screen
    for line in get_board_line_objects(width, height):
        line.draw_to_screen(screen)

    # Print updated states on board
    render_states_on_board(screen, board)


def highlight_win(screen, board):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Get list of winning combination index
    winning_combination_index = get_winning_combination_index(board)
    del(winning_combination_index[1])
    start_index, end_index = winning_combination_index

    # Get box rect objects
    board_box_positions_range = get_board_rect_objects(width, height)

    # Draw winning combination line
    Line("blue", board_box_positions_range[start_index[0]][start_index[1]].get_middle_point_coordinates(),
         board_box_positions_range[end_index[0]][end_index[1]].get_middle_point_coordinates(), 10).draw_to_screen(screen)
