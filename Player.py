from minimax import minimax, get_depth


class Player:
    def __init__(self, bot, state, sign):
        self.bot = bot
        self.state = state
        self.sign = sign

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
            move = minimax(board, get_depth(board), True)
        else:
            index = input("Enter move: ")
            move = Player.convert_index_to_move(int(index))

        return move
