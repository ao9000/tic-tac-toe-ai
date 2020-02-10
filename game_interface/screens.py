import pygame
from game_interface.pygame_class.textbox import Textbox
from game_interface.pygame_class.line import Line
from game_interface.helper_functions import get_board_rect_objects, render_move_state_on_board


# Screen definitions
def draw_selection_screen(screen, event):
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
            return "X", "O"

    if o.is_mouse_hover() or nought.is_mouse_hover():
        o.text_color = "blue"
        o.draw_to_screen(screen)

        nought.text_color = "blue"
        nought.draw_to_screen(screen)

        if o.is_clicked_on(event) or nought.is_clicked_on(event):
            return "O", "X"

    return None, None


def draw_board(screen, event, board):
    # Get screen size
    width, height = screen.get_width(), screen.get_height()

    # Define board lines
    board_lines = [
        # First horizontal line
        Line("black", (0, height * (1 / 3)), (width, height * (1 / 3)), 3),
        # Second horizontal line
        Line("black", (0, height * (2 / 3)), (width, height * (2 / 3)), 3),
        # First vertical line
        Line("black", (width * (1 / 3), 0), (width * (1 / 3), height), 3),
        # Second vertical line
        Line("black", (width * (2 / 3), 0), (width * (2 / 3), height), 3)
    ]

    # Draw to screen
    for line in board_lines:
        line.draw_to_screen(screen)

    # Print updated states
    render_move_state_on_board(screen, board)

    # Get box coordinates/positions
    board_box_positions_range = get_board_rect_objects(width, height)

    # Check intersect, human move
    for row in range(0, 3):
        for box in range(0, 3):
            if board_box_positions_range[row][box].is_clicked_on(event):
                print(row, box)
                return row, box

    return None, None
