
import pytest
from destination_driver_matcher.line_parsers.driver_parser import DriverParser

@pytest.fixture
def parser():
    """Returns the parser"""
    return DriverParser()

@pytest.mark.parametrize('line, name',[
    ('', ''),
    ('a', 'a'),
    ('George Frideric Handel', 'George Frideric Handel'),
    ('Antonín Dvořák', 'Antonín Dvořák'),
    ('Raffaello Sanzio da Urbino', 'Raffaello Sanzio da Urbino'),
])
def test_parser(parser, line, name):
    parsed =  parser.parse(line)
    assert parsed['name'] == name

