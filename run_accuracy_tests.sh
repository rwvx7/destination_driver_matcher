#!/bin/bash

# ----- Accuracy Test Script -----
# This script test the application destination_driver_matcher output accuracy
# with brute force implementation.
# Sytem Requirements:
# - python3 installed at /usr/bin/python3
# - phthon3-pip installed
# - System ran `pip install -r requirements` on 'acme_env' virtualenv

a="../tests/temp/a.txt"
b="../tests/temp/b.txt"

source acme_env/bin/activate
mkdir tests/temp
cd destination_driver_matcher

printf '../data/destinations3.txt\n../data/drivers3.txt\n' | python main.py > ${a}
printf '../data/destinations3.txt\n../data/drivers3.txt\n' | python main.py -b > ${b}
if cmp --silent ${a} ${b} 
then
    echo "test1: pass"
else
    echo "test1: fail"
fi
rm ../tests/temp/*.txt

printf '../data/destinations4.txt\n../data/drivers4.txt\n' | python main.py > ${a}
printf '../data/destinations4.txt\n../data/drivers4.txt\n' | python main.py -b > ${b}
if cmp --silent ${a} ${b} 
then
    echo "test2: pass"
else
    echo "test2: fail"
fi
rm ../tests/temp/*.txt
rmdir ../tests/temp