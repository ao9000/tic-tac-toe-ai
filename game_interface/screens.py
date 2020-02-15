from game_interface.pygame_class.textbox import Textbox
from game_interface.pygame_class.line import Line
from game_interface.helper_functions import render_states_on_board, get_board_line_objects
from game.board import win_check, is_board_full, BLANK_STATE, BOT_STATE, HUMAN_STATE
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


def draw_board_information(screen, player):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Text to show whose turn it is
    Textbox("{}'s turn".format("Bot" if player.bot else "Human"), "green", "freesans", 12, (width * 1 / 2), (height * 1 / 20)).draw_to_screen(screen)


def draw_board(screen, board):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Draw to screen
    for line in get_board_line_objects(width, height):
        line.draw_to_screen(screen)

    # Print updated states on board
    render_states_on_board(screen, board)


def draw_results(screen, board, player):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    if win_check(board):
        # Display winner
        Textbox("{} wins!".format("Bot" if player.bot else "Human"), "black", "freesans", 64, (width * 1 / 2),
                (height * 1 / 2)).draw_to_screen(screen)
    else:
        # Draw
        Textbox("Draw!", "black", "freesans", 64, (width * 1 / 2), (height * 1 / 2)).draw_to_screen(screen)
