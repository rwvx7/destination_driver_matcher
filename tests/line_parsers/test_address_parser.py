
import pytest

from destination_driver_matcher.line_parsers.address_parser import AddressParser

@pytest.fixture
def parser():
    """Returns the parser"""
    return AddressParser()

# def test_parser_error(parser):
#     with pytest.raises(ValueError, IndexError):
#         parsed_address =  parser.parse("1 Chome-7-1 Konan, Minato City, Tokyo 108-0075, Japan")

@pytest.mark.parametrize('fulladdr, street_number, street_name, addr_specific_identifier, city, state, zipcode',[
    ('123 Fake Street, Springfield, SP 99999',
        '123', 'Fake Street', None, 'Springfield', 'SP', '99999'),
    ('One Apple Park Way, Cupertino, CA 95014',
        'One', 'Apple Park Way', None, 'Cupertino', 'CA', '95014'),
    ('400 Pine Street, Suite #140, Seattle, WA 98101',
        '400', 'Pine Street', 'Suite #140', 'Seattle', 'WA', '98101'),
    ('2901 S. Capital of Texas Hwy, Austin, TX 78746',
        '2901', 'S. Capital of Texas Hwy', None, 'Austin', 'TX', '78746'),
])
def test_parser(parser, fulladdr, street_number, street_name, addr_specific_identifier, city, state, zipcode):
    parsed_address =  parser.parse(fulladdr)
    errors = []

    if not parsed_address['street_number'] == street_number:
        errors.append(f"{parsed_address['street_number']} != {street_number}")

    if not parsed_address['street_name'] == street_name:
        errors.append(f"{parsed_address['street_name']} != {street_name}")

    if not parsed_address['city'] == city:
        errors.append(f"{parsed_address['city']} != {city}")

    if not parsed_address['state'] == state:
        errors.append(f"{parsed_address['state']} != {state}")

    if not parsed_address['zipcode'] == zipcode:
        errors.append(f"{parsed_address['zipcode']} != {zipcode}")

    if (addr_specific_identifier == None and
            'addr_specific_identifier' in parsed_address and
            parsed_address['addr_specific_identifier'] != None):
        errors.append(f"{parsed_address['addr_specific_identifier']} != {addr_specific_identifier}")
    
    if (addr_specific_identifier != None and
            ('addr_specific_identifier' not in parsed_address or
            parsed_address['addr_specific_identifier'] != addr_specific_identifier)):
        errors.append(f"{parsed_address['addr_specific_identifier']} != {addr_specific_identifier}")

    # assert no error message in errors list, else print the messages
    assert not errors, "errors:\n{}".format("\n".join(errors))

