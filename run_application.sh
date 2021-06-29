#!/bin/bash

# ----- Run Script -----
# This script runs the application destination_driver_matcher
# Sytem Requirements:
# - python3 installed at /usr/bin/python3
# - phthon3-pip installed
# - System ran `pip install -r requirements` on 'acme_env' virtualenv

source acme_env/bin/activate
cd destination_driver_matcher
python main.py
