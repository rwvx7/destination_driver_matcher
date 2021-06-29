
from models.address import Address
from models.driver import Driver


class FileReader():
    supported_consumers = {'Address': Address, 'Driver': Driver}
    def __init__(self, line_parser, parsed_line_consumer):
        self._line_parser = line_parser
        self.failed_lines = []
        if parsed_line_consumer not in self.supported_consumers:
            raise KeyError(f"{parsed_line_consumer} is not a supported consumer")
        self._parsed_line_consumer = parsed_line_consumer

    def read_file(self, filename):
        list = []
        with open(filename, 'r') as reader:
            for line in reader:
                line = line.strip()
                try:
                    item = self._line_parser(line)
                    item = self.supported_consumers[self._parsed_line_consumer](item)
                    list.append(item)
                except (ValueError, IndexError) as exc:
                    self.failed_lines.append(line)
                except:
                    print(f"Unexpected parsing error {line}")
                    self.failed_lines.append(line)
        return list
