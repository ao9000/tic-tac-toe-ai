import timeit
import statistics


def print_stats(title, time):
    print(title)
    print("Minimum time: {}, Average time: {}\n".format(round(min(time), 2), round(statistics.mean(time)), 2))


import_setup = """
from minimax import minimax, minimax_alpha_beta, get_depth
from tests import positions
from math import inf
"""

test_minimax = "minimax(positions.blank_board, get_depth(positions.blank_board), True)"

test_minimax_alpha_beta = "minimax_alpha_beta(positions.blank_board, get_depth(positions.blank_board), True, -inf, +inf)"


def main():
    # Just minimax
    time = timeit.Timer(test_minimax, setup=import_setup).repeat(10, 1)
    print_stats("Just minimax results", time)

    # Minimax with alpha beta pruning
    time = timeit.Timer(test_minimax_alpha_beta, setup=import_setup).repeat(10, 1)
    print_stats("Minimax with alpha-beta pruning", time)


if __name__ == '__main__':
    main()
