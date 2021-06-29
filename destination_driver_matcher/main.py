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
    parser = argparse.ArgumentParser(description="Acme Inc destination driver matcher")
    parser.add_argument("--destinations", help="filename containing list of shipping destinations. This argument is ignored unless drivers file is also provided via --drivers")
    parser.add_argument("--drivers", help="filename containing list of drivers. This argument is ignored unless destinations file is also provided via --destinations")
    parser.add_argument("--log", help="Set log level. Must be one of: DEBUG, INFO, WARNING, ERROR, CRITICAL. Default is WARNING", default="WARNING")
    parser.add_argument("-b", "--brute-force", help="use brute force algorithm instead", action="store_true")
    args = parser.parse_args()

    loglevel = args.log.upper()
    if (loglevel != 'DEBUG'
        and loglevel != 'INFO'
        and loglevel != 'WARNING'
        and loglevel != 'ERROR'
        and loglevel != 'CRITICAL'):
        loglevel = 'WARNING'
    log_setup(loglevel)

    filename_destinations = args.destinations
    filename_drivers = args.drivers

    if filename_destinations == None or filename_drivers == None:
        filename_destinations = input("Enter filename for shipping destinations: ")
        filename_drivers = input("Enter filename for drivers: ")

    is_brute_force = args.brute_force

    print()
    print(f"using files:")
    print(f"shipping destinations: {filename_destinations}")
    print(f"drivers:               {filename_drivers}")

    run(filename_destinations, filename_drivers, is_brute_force)


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
