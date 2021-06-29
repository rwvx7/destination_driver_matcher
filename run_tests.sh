#!/bin/bash

# ----- Test Script -----
# This script runs tests for destination_driver_matcher
# Sytem Requirements:
# - python3 installed at /usr/bin/python3
# - phthon3-pip installed
# - System ran `pip install -r requirements` on 'acme_env' virtualenv
# This script does the following:
# - pytest unit tests

source acme_env/bin/activate
PYTHONPATH=./destination_driver_matcher pytest
