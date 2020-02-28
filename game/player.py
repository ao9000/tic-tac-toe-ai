"""
    Player class

    Handles everything related to move selection by the bot or the human player.
"""

from bot.minimax import minimax_soft_alpha_beta, get_depth
import random
from math import inf


class Player:
    """
    Player class

    A player can be a human or bot.
    """
    def __init__(self, bot, state, mark):
        """
        Constructor for Person class.

        :param bot: type: bool
        True if the player is a bot, else False for human player

        :param state: type: int
        Integer representing the player's state (0 or 1 or 2)
        0 - BLANK_STATE
        1 - HUMAN_STATE
        2 - BOT_STATE

        :param mark: type: str
        String representing the player's mark. (Noughts or crosses) (X or O)
        """
        self._bot = bot
        self._state = state
        self._mark = mark

    @property
    def bot(self):
        return self._bot

    @property
    def state(self):
        return self._state

    @property
    def mark(self):
        return self._mark

    @staticmethod
    def convert_index_to_move(index):
        """
        Converts user input index (1-9) into move indexes. (<row_index>, <column_index>)

        :param index: type: int
        User input selected move index (1-9)

        :return: type: tuple
        Selected move index in numpy array format (<row_index>, <column_index>)
        """
        index_to_move_dict = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }

        return index_to_move_dict[index]

    def make_move(self, board):
        """
        Calls the minimax algorithm if the player is a bot, else request user input for human player.

        :param board: type: numpy.ndarray
        The current state of the Tic Tac Toe board game
        Input for the minimax algorithm to find the optimal move

        :return: type: tuple
        Selected move index in numpy array format (<row_index>, <column_index>)
        """
        if self._bot:
            # Minimax algorithm
            _, moves = minimax_soft_alpha_beta(board, get_depth(board), True, -inf, +inf)
            move = random.choice(moves)
        else:
            # Prompt the user to select a move
            index = input("Enter move: ")
            move = Player.convert_index_to_move(int(index))

        return move
