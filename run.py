from Player import Player
from board import create_board, PLAYER_STATE, BOT_STATE, win_check, is_board_full, update_board, display_board


def main():
    board = create_board()

    p1 = Player(bot=False, state=PLAYER_STATE, sign='O')
    p2 = Player(bot=True, state=BOT_STATE, sign='X')
    players = [p1, p2]

    while not win_check(board) and not is_board_full(board):
        for player in players:
            move = player.make_move(board)
            board = update_board(board, move, player)
            display_board(board, players)

            if win_check(board) or is_board_full(board):
                break


if __name__ == '__main__':
    main()
