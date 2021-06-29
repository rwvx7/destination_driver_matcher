from destination_driver_matcher.models.address import Address
from destination_driver_matcher.models.driver import Driver
from pytest_mock import MockerFixture
import pytest
from destination_driver_matcher.suitability_scorer import SuitabilityScorer


def test_suitability_scorer(fake_address1, fake_address2, fake_address3,
                            fake_driver1, fake_driver2, fake_driver3):
    """Test if SuitabilityScorer can run"""
    destinations = [fake_address1, fake_address2, fake_address3]
    drivers = [fake_driver1, fake_driver2, fake_driver3]
    scorer = SuitabilityScorer(destinations, drivers)
    cost_matrix = scorer.calc_scores()

    expected = [[8, 8, 12], [15.75, 6.75, 3], [8, 8, 12]]

    rows, cols = len(drivers), len(destinations)
    assert all([cost_matrix[i][j] == expected[i][j] for j in range(cols) for i in range(rows)])
