# destination_driver_matcher
This python application matches shipment destinations to drivers while maximizing total suitability score of all shipments to all drivers. Each driver can only have one shipment and each shipment can only be offered to one driver.

Suitability score is calculated based on the following:
- If the length of the shipment's destination street name is even, the base suitability score (SS) is the number of vowels in the driver’s name multiplied by 1.5.
- If the length of the shipment's destination street name is odd, the base SS is the number of consonants in the driver’s name multiplied by 1.
- If the length of the shipment's destination street name shares any common factors (besides 1) with the length of the driver’s name, the SS is increased by 50% above the base SS.

# Table of Content
- [Application Background](#application-background)
- [Ubuntu cheatsheet](#ubuntu-cheatsheet)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Summary](#summary)
- [Useful Information](#useful-information)

## Application Background
To be Added

## Ubuntu Cheatsheet
If you are running Ubuntu (preferably 20.04 or later), The following is a quick run down of commands and scripts to complete the prerequisites, setup, and usage steps. The scripts have not been tested on other operating systems.
1. `$ sudo apt install python3-pip`
2. `$ pip3 install virtualenv`
3. With the project root directory as the current working directory, run the system_setup.sh script: `$ ./system_setup.sh`
4. Run `$ ./run_tests.sh` to run the unit tests
5. Run:
```
$ source acme_env/bin/activate
cd destination_driver_matcher
$ ./run_application.sh
```
to run the application

## Prerequisites
Linux, MacOS, or Windows with the following installed:
- Python3
- Python3-pip

Application was tested on Windows 10 WSL2 running Ubuntu-20.04 with Python 3.8.5

### Ubuntu
Python3 should already be installed by default. Run the following command in the bash terminal to confirm:
`$ python3 --version`

However, the Python Package Index tool (pip3) is not installed by default. You can install it by typing the follow in the bash terminal:
`$ sudo apt install python3-pip`

## Setup
With the prerequisites met, the follow has to be done as setup before the application can run:
1. Create and activate a python virtual environment (not required but highly recommended)
2. run: `$ pip install -r requirements.txt` to install required python packages

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

After the virtualenv is activated, packages installed using `pip` will only be available within that virtualenv. Now we can install the required packages by running:
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
### Python virtual environments
- https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe
- https://python-docs.readthedocs.io/en/latest/dev/virtualenvs.html
- https://pypi.org/project/virtualenvwrapper/
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment#using_django_inside_a_python_virtual_environment

