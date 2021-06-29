
from models.address import Address
from models.driver import Driver
from typing import List

class ResultOutputer:
    def __init__(self, destinations: List[Address], drivers: List[Driver]):
        self._destinations = destinations
        self._drivers = drivers

    def output_to_terminal(self, row_ind: List[int], col_ind: List[int], sum: float):
        driver_dest_pairings = self._organize_results(row_ind, col_ind)
        print()
        print("----- Results -----")
        print(f"Total suitability score: {sum}")
        print(f'{"Destination":64}   Driver')
        driver_dest_pairings.sort(key=lambda x: (x[0], x[1]))
        for pair in driver_dest_pairings:
            print(f"{pair[0]:64} - {pair[1]}")

    def _organize_results(self, row_ind: List[int], col_ind: List[int]):
        driver_dest_pairings = []
        for i, j in zip(row_ind, col_ind):
            destination = self._destinations[i]
            driver = self._drivers[j]
            driver_dest_pairings.append([destination.get_full_address(), driver.name])
        return driver_dest_pairings
