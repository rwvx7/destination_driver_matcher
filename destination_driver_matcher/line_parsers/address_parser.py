
class AddressParser:
    """Class that parses US based addresses, does not support PO BOX or other special addresses"""
    def __init__(self):
        pass

    def parse(self, address_str):
        parsed_address = {}
        try:
            street_number, remainder = address_str.split(None, 1)
            addr = remainder.split(',')
            street_name = addr[0].strip()
            addr_specific_identifier = ''
            if (len(addr) > 3):
                addr_specific_identifier = ', '.join([x.strip() for x in addr[1:-2]])
            city = addr[-2].strip()
            state, zipcode = addr[-1].strip().split(None)

            parsed_address['street_number'] = street_number
            parsed_address['street_name'] = street_name
            parsed_address['city'] = city
            parsed_address['state'] = state
            parsed_address['zipcode'] = zipcode
            if addr_specific_identifier != '':
                parsed_address['addr_specific_identifier'] = addr_specific_identifier

            return parsed_address
        except (ValueError, IndexError) as exc:
            # ignore line if parsing results in error
            print(f"address parse error {address_str}")
            raise
