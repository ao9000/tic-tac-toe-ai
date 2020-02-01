import timeit
import statistics


def print_stats(title, time):
    print(title)
    print("Minimum time: {:.2f}, Average time: {:.2f}\n".format(min(time), statistics.mean(time)))


import_setup = """
from bot.minimax import minimax, minimax_alpha_beta, minimax_soft_alpha_beta, get_depth
from game.board import create_board
from math import inf

board = create_board()
"""

test_minimax = "minimax(board, get_depth(board), True)"

test_minimax_alpha_beta = "minimax_alpha_beta(board, get_depth(board), True, -inf, +inf)"

test_minimax_soft_alpha_beta = "minimax_soft_alpha_beta(board, get_depth(board), True, -inf, +inf)"


def main():
    # Just minimax
    time = timeit.Timer(test_minimax, setup=import_setup).repeat(10, 1)
    print_stats("Pure minimax", time)

    # Minimax with alpha beta pruning
    time = timeit.Timer(test_minimax_alpha_beta, setup=import_setup).repeat(10, 1)
    print_stats("Alpha-beta pruning", time)

    # Minimax with soft alpha beta pruning
    time = timeit.Timer(test_minimax_soft_alpha_beta, setup=import_setup).repeat(10, 1)
    print_stats("Soft alpha-beta pruning", time)


if __name__ == '__main__':
    main()
