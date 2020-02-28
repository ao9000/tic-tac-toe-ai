"""
    Compares the difference in time taken to run different approaches of the minimax algorithm.

    Minimax without any pruning (Pure minimax):
    This approach of the minimax algorithm features only itself without any pruning of the branches in the decision tree

    This approach is the slowest compared to the other approaches as it calculates each and every branch possibilities
    without any pruning to speed up the process.

    Minimax with alpha-beta pruning:
    This approach of the minimax algorithm features full alpha-beta pruning. Alpha beta pruning is where the pruning of
    decision tree occurs based on the alpha and beta values. Alpha value is used by the maximizing player while beta
    value is used by the minimizing player. This approach prunes all the values that is equal or smaller/larger than
    the required threshold depending on the player.

    This approach is the fastest compared to the other approaches as it only calculates only the first best route and
    skips the rest of the routes

    Minimax with soft alpha-beta pruning:
    This approach of the minimax algorithm features partial alpha-beta pruning. This approach prunes all the values
    that are only smaller/larger than the required threshold depending on the player.

    This approach is the compromise of pure minimax and alpha-beta pruning. This approach only calculates all of the
    best route and skips the rest of the routes
"""

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
