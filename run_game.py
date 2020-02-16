# UI imports
import pygame
import sys
from game_interface.color import color_to_rgb
from game_interface.screens import draw_board, draw_selection_screen, draw_board_information

# Game logic imports
import random
import time
from game.board import create_board, HUMAN_STATE, BOT_STATE, win_check, is_board_full, get_turn_number
from game_interface.helper_functions import bot_move_handler, human_move_handler

# Define screen size
width, height = 600, 600

# Define FPS
tick_rate = 30


def setup_game():
    # Initialize module
    pygame.init()

    # Define screen dimensions
    screen_size = (width, height)
    screen = pygame.display.set_mode(screen_size)

    # Define game window caption
    pygame.display.set_caption("Tic Tac Toe")

    # Define game clock
    clock = pygame.time.Clock()
    # tick rate
    clock.tick(tick_rate)

    return screen, clock


def main():
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

            # White background/clear previous objects
            screen.fill(color_to_rgb("white"))

            if intro:
                # Draw selection screen
                draw_selection_screen(screen, event, players)

                # Proceed to next screen if user selected a choice & assign players
                if players:
                    # Unpack players
                    bot, human = players[0], players[1]

                    # Random starting player
                    player = random.choice(players)

                    # Move on to game screen
                    intro = False
            elif game:

                # Draw board information
                draw_board_information(screen, player, records)
                
                # Draw tic tac toe board
                draw_board(screen, board)

                # Check if game is finished
                if win_check(board):
                    # Game is finished

                    # Animation that shows the winning row
                    pass

                    # Post game cleanup
                    # Record win
                    if player.bot:
                        records["bot_win"] += 1
                    else:
                        records["human_win"] += 1

                    # Clear turn number
                    records['turn_num'] = 0

                    # Random starting player
                    player = random.choice(players)

                    # Reset board
                    board = create_board()
                elif is_board_full(board):
                    # Draw check
                    records["draw"] += 1

                    # Post game cleanup
                    # Clear turn number
                    records['turn_num'] = 0

                    # Random starting player
                    player = random.choice(players)

                    # Reset board
                    board = create_board()
                else:
                    # Not finished

                    # Make a move (bot/human)
                    if player.bot:
                        # Bot turn
                        bot_move_handler(board, player)
                    else:
                        # Human turn
                        human_move_handler(board, screen, event, player)

                    # Cycle turns
                    if get_turn_number(board) != records["turn_num"]:
                        if not win_check(board) and not is_board_full(board):
                            player = human if player.bot else bot
                            records["turn_num"] = get_turn_number(board)

        # Update screen
        pygame.display.update()


if __name__ == '__main__':
    main()

