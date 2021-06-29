#!/bin/bash

# ----- System Setup Script -----
# Sytem Requirements:
# - python3 installed at /usr/bin/python3
# - phthon3-pip installed
# This script does the following:
# - creates a virtualenv called 'acme_env' in the current working directory
# - activates virtualenv 'acme_env'
# - calls pip and installs the packages specified in requirements.txt

virtualenv -q -p /usr/bin/python3 acme_env
source acme_env/bin/activate
pip install -r requirements.txt
