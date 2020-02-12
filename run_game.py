# UI imports
import pygame
import sys
from game_interface.color import color_to_rgb
from game_interface.screens import draw_board, draw_selection_screen, draw_results

# Game logic imports
import random
from game.player import Player
from game.board import create_board, HUMAN_STATE, BOT_STATE, win_check, is_board_full, update_board
from game_interface.helper_functions import bot_move_handler, human_move_handler


def main():
    # Initialize module
    pygame.init()

    # Define screen size
    width, height = 600, 600
    screen_size = (width, height)

    # Define & launch screen
    screen = pygame.display.set_mode(screen_size)

    # Game window name
    pygame.display.set_caption("Tic Tac Toe")

    # Define clock
    clock = pygame.time.Clock()

    # Create Tic Tac Toe board
    board = create_board()

    # Define whose turn
    player = None

    # Define page states
    intro = True
    game = True
    result = True

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

            # White background/ clear background
            screen.fill(color_to_rgb("white"))

            if intro:
                # Draw selection screen
                human_mark, bot_mark = draw_selection_screen(screen, event)

                # Proceed to next screen if user selected a choice & assign players
                if human_mark and bot_mark:
                    intro = False

                    bot = Player(bot=True, state=BOT_STATE, mark=bot_mark)
                    human = Player(bot=False, state=HUMAN_STATE, mark=human_mark)

                    # Random starting player
                    player = random.choice([bot, human])
            elif game:
                # Draw tic tac toe board
                draw_board(screen, board)

                # Prompt to show who starts first
                pass

                # Make a move (bot/human)
                if player.bot:
                    # Bot turn
                    move = bot_move_handler(board, player)
                else:
                    # Human turn
                    move = human_move_handler(board, screen, event, player)

                if move:
                    # Cycle turns & Update move
                    update_board(board, move, player)

                    # Proceed to next game once winner is found or draw
                    if win_check(board) or is_board_full(board):
                        # Animation that shows the winning row
                        pass

                        # Move on to next screen
                        game = False
                        continue

                    player = human if player.bot else bot

            elif result:
                draw_results(screen, player)

        # Update screen
        pygame.display.update()
        # How many times to update screen in a second (Tick rate or FPS)
        clock.tick(20)


if __name__ == '__main__':
    main()

