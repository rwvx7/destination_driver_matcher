


import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import List

class Hungarian:
    """
    Runs the Hungarian algorithm implemented in scipy to find maximum cost
    More information:
    https://en.wikipedia.org/wiki/Hungarian_algorithm
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html
    """
    def __init__(self, cost_matrix):
        self._cost_matrix = cost_matrix

    def execute(self):
        cost_matrix = np.array(self._cost_matrix)
        row_ind, col_ind = linear_sum_assignment(cost_matrix=cost_matrix, maximize=True)
        sum = cost_matrix[row_ind, col_ind].sum()
        return row_ind, col_ind, sum



