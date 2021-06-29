#!/bin/bash

# ----- Integration Test Script -----
# This script test the application destination_driver_matcher
# Sytem Requirements:
# - python3 installed at /usr/bin/python3
# - phthon3-pip installed
# - System ran `pip install -r requirements` on 'acme_env' virtualenv

a="../tests/temp/output.txt"

source acme_env/bin/activate
mkdir tests/temp
cd destination_driver_matcher

printf '../tests/data/01_input_destinations.txt\n../tests/data/01_input_drivers.txt\n' | python main.py > ${a}
if cmp --silent ${a} "../tests/data/01_expected_output.txt" 
then
    echo "test1: pass"
else
    echo "test1: fail"
fi
rm ../tests/temp/*.txt
rmdir ../tests/temp