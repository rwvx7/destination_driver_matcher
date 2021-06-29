#!/usr/bin/env python

import argparse
from destination_driver_matcher import run
import logging

def main():
    """
    This is the entry point of the application. Does housekeeping work before running main functionality:
    - Parses user arguments
    - Logging setup
    - Ask for user input when needed
    """
    parser = argparse.ArgumentParser(description="Acme Inc driver destination scheduler")
    parser.add_argument("--destinations", help="filename containing list of shipping destinations")
    parser.add_argument("--drivers", help="filename containing list of drivers")
    parser.add_argument("--log", help="set log level. must be one of: DEBUG, INFO, WARNING, ERROR, CRITICAL")
    parser.add_argument("-b", "--brute-force", help="use brute force algorithm instead", action="store_true")
    args = parser.parse_args()

    loglevel = 'WARNING'
    if (args.log == 'DEBUG'
        or args.log == 'INFO'
        or args.log == 'WARNING'
        or args.log == 'ERROR'
        or args.log == 'CRITICAL'):
        loglevel = args.log
    log_setup(loglevel)

    filename_destinations = args.destinations
    filename_drivers = args.drivers
    filename_destinations = "../data/destinations3.txt"
    filename_drivers = "../data/drivers3.txt"

    if filename_destinations == None or filename_drivers == None:
        filename_destinations = input("Enter filename for shipping destinations: ")
        filename_drivers = input("Enter filename for drivers: ")

    is_brute_force = args.brute_force

    print()
    print(f"using files:")
    print(f"shipping destinations: {filename_destinations}")
    print(f"drivers:               {filename_drivers}")
    print(f"Use brute force: {is_brute_force}")

    run(filename_destinations, filename_drivers)


def log_setup(loglevel: str):
    """Logging setup"""
    llevel = getattr(logging, loglevel.upper())
    logging.basicConfig(
        level=llevel,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )

if __name__ == "__main__":
    main()
