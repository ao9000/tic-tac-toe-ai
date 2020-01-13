from minimax import minimax, get_depth


class Player:
    def __init__(self, bot, state, mark):
        self.bot = bot
        self.state = state
        self.mark = mark
        self.name = "Bot" if self.bot else "Human"

    @staticmethod
    def convert_index_to_move(index):
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
        if self.bot:
            # Minimax algorithm
            _, move = minimax(board, get_depth(board), True)
        else:
            # Prompt the user to select a move
            index = input("Enter move: ")
            move = Player.convert_index_to_move(int(index))

        return move
