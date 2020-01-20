from timeit import default_timer as timer
from minimax import minimax, get_depth
import tests.positions as positions


start = timer()
minimax(positions.blank_board, get_depth(positions.blank_board), True)
end = timer()
print(end-start)
