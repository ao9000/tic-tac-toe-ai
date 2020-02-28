"""
    Text based version of tic-tac-toe with minimax algorithm artificial intelligence (AI) game
"""

import random
from game.player import Player
from game.board import create_board, HUMAN_STATE, BOT_STATE, win_check, is_board_full, update_board, display_board


def choose_mark():
    """
    Prompts the user to enter their mark. (Noughts or crosses) (X or O)

    :return: type: tuple if valid, function call if not valid
    The human player's mark followed by bot's mark
    """
    # Get user input for customization
    marks = ["X", "O"]
    human_mark = str(input("\nChoose a mark {}: ".format(marks))).upper()

    # Integrity check for valid mark
    if human_mark not in marks:
        # Invalid response, call function again
        print("Invalid mark")
        return choose_mark()
    else:
        # Valid
        # Removes human mark from list, leaving only bot mark
        marks.remove(human_mark)
        # Return human mark & bot mark
        return human_mark, marks[0]


def main():
    """
    The main function of the application.
    Creates the board, players and loop their turns infinitely until a winner is found.
    """
    # Introduction
    print("Welcome to the game of Tic Tac Toe, your opponent is a bot running the Minimax algorithm")

    # Create Tic Tac Toe board
    board = create_board()

    # Create players
    human_mark, bot_mark = choose_mark()
    bot = Player(bot=True, state=BOT_STATE, mark=bot_mark)
    human = Player(bot=False, state=HUMAN_STATE, mark=human_mark)

    # Random starting player
    players = [human, bot]
    random.shuffle(players)

    # Loop turns
    while True:
        for player in players:
            print("\n{}'s turn".format(player_name := "Bot" if player.bot else "Human"))
            move = player.make_move(board)
            update_board(board, move, player)
            display_board(board, players)

            # Break infinite loop under conditions
            if win_check(board):
                return print("Game over. {} wins!".format(player_name))
            elif is_board_full(board):
                return print("Game over. Draw!")


if __name__ == '__main__':
    main()
