import random
from player import Player
from board import create_board, PLAYER_STATE, BOT_STATE, win_check, is_board_full, update_board, display_board


def choose_mark():
    """Prompts the user to enter their mark. (Noughts or crosses) (X or O)"""

    # Get user input for customization
    marks = ["X", "O"]
    human_sign = str(input("Choose a mark {}: ".format(marks))).upper()

    # Integrity check for valid mark
    if human_sign not in marks:
        # Invalid, call function again
        print("Invalid sign")
        return choose_mark()
    else:
        # Valid, return human mark & bot mark
        if human_sign == marks[0]:
            return marks[0], marks[1]
        else:
            return marks[1], marks[0]


def main():
    """The main function of the application. Creates the board, players and turn
    system.
    """

    # Introduction
    print("Welcome to the game of Tic Tac Toe, your opponent is a bot running the Minimax algorithm")

    # Create Tic Tac Toe board
    board = create_board()

    # Create players
    human_mark, bot_mark = choose_mark()
    bot = Player(bot=True, state=PLAYER_STATE, sign=bot_mark)
    human = Player(bot=False, state=BOT_STATE, sign=human_mark)

    # Random starting player
    players = [bot, human]
    random.shuffle(players)

    # Loop turns
    while not win_check(board) and not is_board_full(board):
        for player in players:
            move = player.make_move(board)
            board = update_board(board, move, player)
            display_board(board, players)

            if win_check(board) or is_board_full(board):
                break


if __name__ == '__main__':
    main()
