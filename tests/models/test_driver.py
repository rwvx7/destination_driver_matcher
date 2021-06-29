
import pytest
from destination_driver_matcher.models.driver import Driver

@pytest.mark.parametrize('parsed_data, expect_ans',[
    ({'name': ''}, ''),
    ({'name': '007'}, '007'),
    ({'name': 'Miyamoto Musashi'}, 'Miyamoto Musashi'),
    ({'name': 'Dvořák'}, 'Dvořák'),
    ({'name': 'Wolfgang Amadeus Mozart'}, 'Wolfgang Amadeus Mozart'),
    ({'name': 'Dr. Stephen Strange'}, 'Dr. Stephen Strange'),
])
def test_name(parsed_data, expect_ans):
    driver = Driver(parsed_data)
    assert driver.name == expect_ans

@pytest.mark.parametrize('parsed_data, expect_ans',[
    ({'name': ''}, 0),
    ({'name': '007'}, 3),
    ({'name': 'Miyamoto Musashi'}, 16),
    ({'name': 'Dvořák'}, 6),
    ({'name': 'Wolfgang Amadeus Mozart'}, 23),
    ({'name': 'Dr. Stephen Strange'}, 19),
])
def test_name_length(parsed_data, expect_ans):
    driver = Driver(parsed_data)
    assert driver.get_name_length() == expect_ans

@pytest.mark.parametrize('parsed_data, expect_ans',[
    ({'name': ''}, 0),
    ({'name': '007'}, 0),
    ({'name': 'Miyamoto Musashi'}, 7),
    ({'name': 'Dvořák'}, 1),
    ({'name': 'Wolfgang Amadeus Mozart'}, 8),
    ({'name': 'Dr. Stephen Strange'}, 4),
])
def test_get_num_vowels_in_name(parsed_data, expect_ans):
    driver = Driver(parsed_data)
    assert driver.get_num_vowels_in_name() == expect_ans

@pytest.mark.parametrize('parsed_data, expect_ans',[
    ({'name': ''}, 0),
    ({'name': '007'}, 0),
    ({'name': 'Miyamoto Musashi'}, 8),
    ({'name': 'Dvořák'}, 3),
    ({'name': 'Wolfgang Amadeus Mozart'}, 13),
    ({'name': 'Dr. Stephen Strange'}, 12),
])
def test_get_num_consonants_in_name(parsed_data, expect_ans):
    driver = Driver(parsed_data)
    assert driver.get_num_consonants_in_name() == expect_ans

def test_non_str_name():
    with pytest.raises(ValueError):
        Driver(7)