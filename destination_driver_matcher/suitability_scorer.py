
import math
from models.address import Address
from models.driver import Driver
from typing import List

class SuitabilityScorer:
    def __init__(self, destinations: List[Address], drivers: List[Driver]):
        self._destinations = destinations
        self._drivers = drivers

    def calc_scores(self):
        results = [[0 for j in range(len(self._drivers))] for i in range(len(self._destinations))]
        for i, destination in enumerate(self._destinations):
            for j, driver in enumerate(self._drivers):
                results[i][j] = self.get_score(destination, driver)
        return results

    def get_score(self, destination, driver):
        score = 0
        if destination.is_length_street_name_even():
            score = self.get_score_street_name_length_even(driver)
        else:
            score = self.get_score_street_name_length_odd(driver)
        if self.hasCommonFactorsBesidesOne(destination.get_street_name_length(), driver.get_name_length()):
            score *= 1.5
        return score

    def get_score_street_name_length_even(self, driver: Driver):
        return driver.get_num_vowels_in_name() * 1.5

    def get_score_street_name_length_odd(self, driver: Driver):
        return driver.get_num_consonants_in_name()

    def hasCommonFactorsBesidesOne(self, num1, num2):
        return math.gcd(num1, num2) > 1

