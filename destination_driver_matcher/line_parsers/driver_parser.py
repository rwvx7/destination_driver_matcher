
class DriverParser:
    def __init__(self):
        pass

    def parse(self, driver_str):
        parsed = {}
        try:
            name = driver_str.strip()
            parsed['name'] = name
            return parsed
        except (ValueError, IndexError) as exc:
            # ignore line if parsing results in error
            print(f"driver parse error {driver_str}")
            raise
