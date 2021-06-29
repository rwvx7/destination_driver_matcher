
from destination_driver_matcher.algorithms.brute_force import BruteForce
from pytest_mock import MockerFixture
import pytest

def test_brute_force():
    """Test if brute force algorithm can run correctly"""
    cost_matrix = [[8, 15.75, 8], [8, 6.75, 8], [12, 3, 12]]

    brute_force = BruteForce(cost_matrix)
    row_ind, col_ind, sum = brute_force.execute()

    expected_row = [1, 0, 2]
    expected_col = [0, 1, 2]
    expected_sum = 35.75

    assert len(row_ind) == len(expected_row)
    assert len(col_ind) == len(expected_col)
    assert all([a == b for a, b in zip(row_ind, expected_row)])
    assert all([a == b for a, b in zip(col_ind, expected_col)])
    assert sum == expected_sum
