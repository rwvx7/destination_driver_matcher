
import itertools
import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import List

class BruteForce:
    """
    Solves the Linear Sum Assignment problem by brute force.
    """
    def __init__(self, cost_matrix):
        self._cost_matrix = cost_matrix

    def execute(self):
        cost_matrix = np.array(self._cost_matrix)
        m, n = cost_matrix.shape

        max_cost = None
        best_row_ind = None
        best_col_ind = None

        long_length = max(m,n)
        short_length = min(m,n)

        short_ind = list(range(short_length))
        for long_ind in itertools.permutations(range(long_length), short_length):
            # Brute force every combination and check if sum is the largest
            cost = None
            if (long_length == m):
                cost = cost_matrix[long_ind, short_ind].sum()
            else:
                cost = cost_matrix[short_ind, long_ind].sum()

            if max_cost == None or cost > max_cost:
                max_cost = cost
                best_row_ind = long_ind if long_length == m else short_ind
                best_col_ind = short_ind if long_length == m else long_ind
        
        best_row_ind = list(best_row_ind)
        best_col_ind = list(best_col_ind)
        return best_row_ind, best_col_ind, max_cost
