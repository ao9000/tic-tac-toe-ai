"""
    Pygame based version of tic-tac-toe with minimax algorithm artificial intelligence (AI) game
"""

# UI imports
import pygame
import sys
from game_interface.color import color_to_rgb
from game_interface.templates import game_board, selection_screen, board_information, highlight_win

# Game logic imports
import random
from game.board import create_board, win_check, is_board_full, get_turn_number
from game_interface.helper_functions import bot_move_input_handler, human_move_input_handler, record_draw, record_win, human_input_selection_screen_handler

# Define screen size
width, height = 600, 600


def setup_game():
    """
    Setup the pygame game window and tick rate properties

    :return: type: tuple
    Contains the pygame.surface and pygame.clock objects for the game

    pygame.surface class is responsible for the the window properties such as the dimension and caption settings
    pygame.clock class is responsible for the frame per second (fps) or tick rate of the game
    """
    # Initialize module
    pygame.init()

    # Define screen dimensions
    screen_size = (width, height)
    screen = pygame.display.set_mode(screen_size)

    # Define game window caption
    pygame.display.set_caption("Tic Tac Toe")

    # Define game clock
    clock = pygame.time.Clock()

    return screen, clock


def render_items_to_screen(screen, interface_items):
    """
    Renders all the items in interface_items dictionary to the screen

    :param screen: type: pygame.surface
    The surface/screen of the game for displaying purposes

    :param interface_items: type: dict
    Dictionary containing all of the user interface (UI) items to be displayed
    """
    # List to exclude rendering
    exclude_list = [
        'game_board_rects'
    ]

    for key, value in interface_items.items():
        if key not in exclude_list:
            if isinstance(value, list):
                for move in value:
                    if move:
                        move.draw_to_screen(screen)
            else:
                value.draw_to_screen(screen)


def post_game_delay():
    """
    Forces the screen to update while adding a delay and clearing any events that were added during the delay.

    Used for adding a delay between multiple tic-tac-toe games. This is to provide time for the player to react to what
    is happening in the game.
    """
    # Refresh screen & add delay
    pygame.display.update()
    # Caution, when wait is active, event gets stored in a queue waiting to be executed.
    # This causes some visual input lag. Must clear the event queue after done with pygame.time.wait
    pygame.time.wait(2000)
    pygame.event.clear()


def main():
    """
    The main function of the game.
    Responsible for the setup of game window properties, creating players, scheduling scenes in the game, recording
    player statistics and looping the game.
    """
    # Setup game
    screen, clock = setup_game()

    # Create list of players
    players = []
    # Define whose turn
    player = None

    # Define stats recording
    records = {
        # Record turn number
        'turn_num': 0,
        # Record bot wins
        'bot_win': 0,
        # Record human wins
        'human_win': 0,
        # Record draws
        'draw': 0
    }

    # Define screen states
    intro = True
    game = True

    # Create a blank Tic Tac Toe board
    board = create_board()

    # Game loop
    while True:
        # tick rate
        clock.tick(30)

        mouse_position = pygame.mouse.get_pos()
        mouse_clicked = False

        for event in pygame.event.get():
            # Break loop if window is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Break loop if ESC key is pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True

        # White background/clear previous objects
        screen.fill(color_to_rgb("white"))

        if intro:
            # Draw selection screen
            interface_items = selection_screen(screen, mouse_position)
            render_items_to_screen(screen, interface_items)

            # Handle user input
            if mouse_clicked:
                human_input_selection_screen_handler(interface_items, players, mouse_position)

            # Proceed to next screen if user selected a choice & assign players
            if players:
                # Unpack players
                bot, human = players[0], players[1]

                # Random starting player
                player = random.choice(players)

                # Move on to game screen
                intro = False
        elif game:
            # Game scene
            # Draw board information
            interface_items = board_information(screen, records)
            render_items_to_screen(screen, interface_items)

            # Draw tic tac toe board
            interface_items = game_board(screen, board, players)
            render_items_to_screen(screen, interface_items)

            # Check if game is finished
            if win_check(board):
                # Game is finished
                # Highlight the winning row
                interface_items = highlight_win(interface_items, board)
                render_items_to_screen(screen, interface_items)

                # Add delay
                post_game_delay()

                # Record stats
                record_win(player, records)

                # Reset board
                board = create_board()

                # Next game, random starting turn again
                player = random.choice(players)
            elif is_board_full(board):
                # Game is finished

                # Add delay
                post_game_delay()

                # Record stats
                record_draw(records)

                # Reset board
                board = create_board()

                # Next game, random starting turn again
                player = random.choice(players)
            else:
                # Game not finished
                # Make a move (bot/human)
                if player.bot:
                    # Bot turn
                    bot_move_input_handler(board, bot)
                else:
                    if mouse_clicked:
                        # Human turn
                        human_move_input_handler(board, interface_items, mouse_position, human)

                # Cycle turns
                if get_turn_number(board) != records["turn_num"]:
                    if not win_check(board) and not is_board_full(board):
                        # Subsequent turns
                        player = human if player.bot else bot
                        records["turn_num"] = get_turn_number(board)

        # Update screen
        pygame.display.update()


if __name__ == '__main__':
    main()

