
import pytest
from destination_driver_matcher.models.address import Address


@pytest.mark.parametrize('addr, street_name',[
    ('empty_address', None),
    ('fake_address1', 'Fake Street'),
    ('fake_address2', 'Providence Place'),
    ('fake_address3', 'Pine Street'),
])
def test_street_name(request, addr, street_name):
    address = request.getfixturevalue(addr)
    assert address.street_name == street_name

@pytest.mark.parametrize('addr, full_addr',[
    ('fake_address1', '123 Fake Street, Springfield, SP 99999'),
    ('fake_address2', '20 Providence Place, Providence, RI 02903'),
    ('fake_address3', '400 Pine Street, Suite #140, Seattle, WA 98101'),
])
def test_get_full_address(request, addr, full_addr):
    address = request.getfixturevalue(addr)
    assert address.get_full_address() == full_addr

@pytest.mark.parametrize('addr, street_name_length',[
    ('fake_address1', 11),
    ('fake_address2', 16),
    ('fake_address3', 11),
])
def test_get_street_name_length(request, addr, street_name_length):
    address = request.getfixturevalue(addr)
    assert address.get_street_name_length() == street_name_length

@pytest.mark.parametrize('addr, is_length_street_name_even',[
    ('fake_address1', False),
    ('fake_address2', True),
    ('fake_address3', False),
])
def test_is_length_street_name_even(request, addr, is_length_street_name_even):
    address = request.getfixturevalue(addr)
    assert address.is_length_street_name_even() == is_length_street_name_even

def test_get_street_name_length_error(empty_address):
    with pytest.raises(ValueError):
        empty_address.get_street_name_length()

def test_is_length_street_name_even_error(empty_address):
    with pytest.raises(ValueError):
        empty_address.is_length_street_name_even()

