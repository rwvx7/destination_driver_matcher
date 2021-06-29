
import pytest
from destination_driver_matcher.models.address import Address
from destination_driver_matcher.models.driver import Driver

@pytest.fixture
def empty_address():
    """Returns an empty Address"""
    return Address()

@pytest.fixture
def fake_address1():
    """Returns a test Address"""
    return Address({
        'street_number':    '123',
        'street_name':      'Fake Street',
        'city':             'Springfield',
        'state':            'SP',
        'zipcode':          '99999'})

@pytest.fixture
def fake_address2():
    """Returns a test Address"""
    return Address({
        'street_number':    '20',
        'street_name':      'Providence Place',
        'city':             'Providence',
        'state':            'RI',
        'zipcode':          '02903'})

@pytest.fixture
def fake_address3():
    """Returns a test Address"""
    return Address({
        'street_number':            '400',
        'street_name':              'Pine Street',
        'addr_specific_identifier': 'Suite #140',
        'city':                     'Seattle',
        'state':                    'WA',
        'zipcode':                  '98101'})

@pytest.fixture
def fake_address4():
    """Returns a test Address"""
    return Address({
        'street_number':            '747',
        'street_name':              'Broadway',
        'city':                     'Seattle',
        'state':                    'WA',
        'zipcode':                  '98122'})



@pytest.fixture
def empty_driver():
    """Returns a no name driver"""
    return Driver()

@pytest.fixture
def fake_driver1():
    return Driver({'name': 'Miyamoto Musashi'})

@pytest.fixture
def fake_driver2():
    return Driver({'name': 'Bucky Barnes'})

@pytest.fixture
def fake_driver3():
    return Driver({'name': 'Franz Liszt'})


