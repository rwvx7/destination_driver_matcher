

class Address:
    """Class to represent an address."""
    def __init__(self, parsed_address = {}):
        """
        params: parsed_address: dict()
        required to have the following keys:
        'street_number', 'street_name', 'city', 'state', 'zipcode'
        optional keys:
        'addr_specific_identifier' -- this is used to store floor#, suite#, apt#, etc.
        """
        self._parsed_address = parsed_address

    @property
    def street_name(self):
        return self._parsed_address.get("street_name", None)

    def get_full_address(self):
        address = self._parsed_address['street_number'] + ' ' + self._parsed_address['street_name'] + ', '
        if 'addr_specific_identifier' in self._parsed_address:
            address += self._parsed_address['addr_specific_identifier'] + ', '
        address += self._parsed_address['city'] + ', ' + self._parsed_address['state'] + ' ' + self._parsed_address['zipcode']
        return address

    def get_street_name_length(self):
        if self.street_name == None:
            raise ValueError("street_name does not exist therefore length is undefined")
        return len(self.street_name)

    def is_length_street_name_even(self):
        return (self.get_street_name_length() % 2 == 0)



