
from algorithms.brute_force import BruteForce
from algorithms.hungarian import Hungarian
from file_reader import FileReader
from line_parsers.address_parser import AddressParser
from line_parsers.driver_parser import DriverParser
import logging
from models.address import Address
from models.driver import Driver
from result_outputer import ResultOutputer
from suitability_scorer import SuitabilityScorer

def run(filename_destinations, filename_drivers, is_brute_force = False):
    """Main function for the Driver Destination Matcher"""
    try:
        logging.info("Reading Destinations file")
        address_parser = AddressParser()
        address_reader = FileReader(address_parser.parse, 'Address')
        destinations = address_reader.read_file(filename_destinations)
        logging.info(f"num destinations read: {len(destinations)}; failed: {len(address_reader.failed_lines)}")
        if len(address_reader.failed_lines) > 0:
            logging.warning(f"{len(address_reader.failed_lines)} shipping destinations failed to import")

        logging.info("Reading Drivers file")
        driver_parser = DriverParser()
        driver_reader = FileReader(driver_parser.parse, 'Driver')
        drivers = driver_reader.read_file(filename_drivers)
        logging.info(f"num drivers read: {len(drivers)}; failed: {len(driver_reader.failed_lines)}")
        if len(driver_reader.failed_lines) > 0:
            logging.warning(f"{len(driver_reader.failed_lines)} drivers failed to import")

        logging.info("Calculating suitability score for each driver for each destination")
        scorer = SuitabilityScorer(destinations, drivers)
        cost_matrix = scorer.calc_scores()
        logging.debug(f"cost matrix: {cost_matrix}")

        logging.info("Finding best matches between drivers and destinations")
        logging.info(f"Use brute force: {is_brute_force}")
        algorithm = BruteForce(cost_matrix) if is_brute_force else Hungarian(cost_matrix)
        row_ind, col_ind, sum = algorithm.execute()

        logging.info("Preparing results...")
        result_outputer = ResultOutputer(destinations, drivers)
        result_outputer.output_to_terminal(row_ind, col_ind, sum)

    except FileNotFoundError as exc:
        error_str = f"File does not exist: {str(exc)}"
        logging.error(error_str)
    except Exception as exc:
        error_str = f"Unexpected error: {str(exc)}"
        logging.error(error_str)
        logging.error(exc.with_traceback())

