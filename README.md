# destination_driver_matcher
This python application matches shipment destinations to drivers while maximizing total suitability score of all shipments to all drivers. Each driver can only have one shipment and each shipment can only be offered to one driver.

Suitability score is calculated based on the following:
- If the length of the shipment's destination street name is even, the base suitability score (SS) is the number of vowels in the driver’s name multiplied by 1.5.
- If the length of the shipment's destination street name is odd, the base SS is the number of consonants in the driver’s name multiplied by 1.
- If the length of the shipment's destination street name shares any common factors (besides 1) with the length of the driver’s name, the SS is increased by 50% above the base SS.

# Table of Content
- [Application Overview](#application-overview)
- [Ubuntu Cheatsheet](#ubuntu-cheatsheet)
- [MacOS Cheatsheet](#macos-cheatsheet)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Summary](#summary)
- [Useful Information](#useful-information)

## Application Overview
The application does the following:
1. Reads the shipping destinations file.
2. Reads the drivers file.
3. Calculate the suitability score for each shipping destination and driver combination.
4. To find the best shipping destination to driver pairs that maximize total suitability score, what needs to be solved is the [Linear Sum Assignment Problem](#linear-sum-assignment-problem). With the results from step 3, the application uses the scipy implementation of the Hungarian Algorithm to find the maximum suitability score and the best matches.
5. Print results to screen.

This application was tested on Windows 10 WSL2 running Ubuntu-20.04 with Python 3.8.5 and MacOS Big Sur. However, it should work on Windows 10 natively and other Linux distros as well.

## Ubuntu Cheatsheet
If you are running Ubuntu (preferably 20.04 or later), The following is a quick run down of commands and scripts to complete the prerequisites, setup, and usage steps.
1. `$ sudo apt install python3-pip`
2. `$ pip3 install virtualenv`
3. `$ git clone https://github.com/rwvx7/destination_driver_matcher.git` to clone this project to your machine.
4. `$ cd destination_driver_matcher` to make project root directory your current working directory.
4. With the project root directory as the current working directory, run the system_setup.sh script: `$ ./system_setup.sh`. This script has not been tested on other operating systems.
5. Run `$ ./run_tests.sh` to run the unit tests
6. Run:
```
$ source acme_env/bin/activate
$ cd destination_driver_matcher
$ python main.py
```
to run the application

## MacOS Cheatsheet
The following is a quick run down of commands and scripts to complete the prerequisites, setup, and usage steps for MacOS (Tested on MacOS Big Sur). This guide uses the Python3 installation installed from Homebrew.
1. Install [Homebrew](https://brew.sh/)
2. `$ brew update && brew upgrade` to upgrade to newest version of Homebrew.
3. `$ brew install python3` to install Python3 and pip3
4. `$ git clone https://github.com/rwvx7/destination_driver_matcher.git` to clone this project to your machine.
5. `$ cd destination_driver_matcher` to make project root directory your current working directory.
6. `$ pip3 install virtualenv` to install virtualenv
7. `$ virtualenv acme_env` to create a python virtual environment named `acme_env`
8. `$ source acme_env/bin/activate` to start virtualenv
9. `$ pip install -r requirements.txt` to install required packages
10. Run `$ ./run_tests.sh` to run the unit tests.
11. Run:
```
$ source acme_env/bin/activate
$ cd destination_driver_matcher
$ python main.py
```
to run the application

## Prerequisites
Linux, MacOS, or Windows with the following installed:
- Python3
- Python3-pip

Mozilla has a guide for setting up a Django development environment, the part about [setting up Python3](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment#installing_python_3) can be applied here to install Python3 and pip. More guides are available [here](#python3-guides).

### Ubuntu
Python3 should already be installed by default. Run the following command in the bash terminal to confirm:
`$ python3 --version`

However, the Python Package Index tool (pip3) is not installed by default. You can install it by typing the follow in the bash terminal:
`$ sudo apt install python3-pip`

## Setup
With the prerequisites met, the follow has to be done as setup before the application can run:
1. Clone or download the project from github.
2. Create and activate a python virtual environment (not required but highly recommended)
3. run: `$ pip install -r requirements.txt` to install required python packages

Setting up a [python virtual environment](#python-virtual-environments) is recommended to run the application. [virtualenv](https://pypi.org/project/virtualenv/) is a popular tool for this.

The script `system_setup.sh` is prepared to help make the setup process easier. However the user has to ensure virtualenv is installed first. This script will do the following:
1. Create a virtualenv called `acme_env`
2. install packages required by destination_driver_matcher to the `acme_env` virtualenv

### Ubuntu
To install virtualenv, run the following command:
`$ pip3 install virtualenv`

To create a virtual environment, run the following while in the project root directory:
`$ virtualenv acme_env`

A folder named `acme_env` will be created in the current directory and python executables related to that python virtual environment will be stored there.

To activate the virtualenv, run the following:
`$ source acme_env/bin/activate`

When virtualenv is active, packages installed using `pip` will only be available within that virtualenv.

Now we can install the required packages by running:
`$ pip install -r requirements.txt`

To deactivate current virtualenv, run the following:
`$ deactivate`

## Usage
A few scripts have been provided to make running the application easier:
- `$ ./run_tests.sh` runs the unit tests associated with the application.
- `$ ./run_integration_tests.sh` runs the integration test for the application.
- `$ ./run_accuracy_tests.sh` runs the accuracy tests to check if output results are the same with brute force approach.

To run the application, do the following:
1. Activate virtualenv: `$ source acme_env/bin/activate`
2. To run the unit tests: `$ PYTHONPATH=./destination_driver_matcher pytest`
3. To run the application:
```
$ cd destination_driver_matcher
$ python main.py
```
4. Deactivate virtualenv: `$ deactivate`

Running the application via command line arguments is also available:
- `-h, --help`: shows help message
- `--destinations <filename>`: File containing list of destinations. This argument is ignored unless drivers file is also provided via --drivers
- `--drivers <filename>`: File containing list of drivers. This argument is ignored unless destinations file is also provided via --destinations
- `--log <log_level`: Sets log level. Must be one of: DEBUG, INFO, WARNING, ERROR, CRITICAL. Default is WARNING
- `-b, --brute-force`: Tells application to use brute force algorithm instead

For example
`python main.py --destination ../data/destinations4.txt --drivers ../data/drivers4.txt --log INFO`
tells the application to use the destinations file `../data/destinations4.txt`, drivers file `../data/drivers4.txt`, and sets the logging level to INFO.

## Summary
Summary of steps to take:
1. Install python3 if it doesn't exist in system
2. Install python3 pip if it doesn't exist in system
3. [Install a python virtual environment](#python-virtual-environments)
4. activate a python virtual environment
5. While python virtual environment is active:
   1. Run `pip install -r requirements.txt` to install required packages
   2. Run `python main.py` to start the application


## Useful Information
### Linear Sum Assignment Problem
- https://en.wikipedia.org/wiki/Hungarian_algorithm
- https://brilliant.org/wiki/hungarian-matching/
- https://brilliant.org/discussions/thread/intuition-behind-the-hungarian-algorithm/
### Python3 Guides
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment#installing_python_3
- https://realpython.com/installing-python/
### Python virtual environments
- https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe
- https://python-docs.readthedocs.io/en/latest/dev/virtualenvs.html
- https://pypi.org/project/virtualenvwrapper/
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment#using_django_inside_a_python_virtual_environment
