# UI imports
import pygame
import sys
from game_interface.color import color_to_rgb
from game_interface.screens import draw_board, draw_selection_screen

# Game logic imports
import random
from game.player import Player
from game.board import create_board, HUMAN_STATE, BOT_STATE, win_check, is_board_full, update_board
from bot.minimax import minimax_soft_alpha_beta, get_depth
from math import inf

# Initialize module
pygame.init()

# Define screen size
width, height = 600, 600
screen_size = (width, height)

# Define & launch screen
screen = pygame.display.set_mode(screen_size)

# Define clock
clock = pygame.time.Clock()

# Game window name
pygame.display.set_caption("Tic Tac Toe")

# Create Tic Tac Toe board
board = create_board()

# Define whose turn
player = None

# Define page states
intro = True
game = True

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
            if not player.bot:
                # Draw tic tac toe board
                move = draw_board(screen, event, board)
            else:
                _, moves = minimax_soft_alpha_beta(board, get_depth(board), True, -inf, +inf)
                move = random.choice(moves)

            # Check if a move is returned
            if all(index is not None for index in move):
                # Update selected move
                board = update_board(board, move, player)
                print(board)

                # Cycle turns
                player = bot if player == human else human

    # Update screen
    pygame.display.update()
    # How many times to update screen in a second (Tick rate or FPS)
    clock.tick(20)

