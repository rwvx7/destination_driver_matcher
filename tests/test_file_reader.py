
from destination_driver_matcher.file_reader import FileReader
from destination_driver_matcher.models.driver import Driver
from pytest_mock import MockerFixture
import pytest


@pytest.fixture
def file_reader(mocker: MockerFixture):
    """Returns the parser"""
    def mock_init(self, data):
        self.data = data
    def mock_parse(line):
        return line
    mocker.patch.object(Driver, '__init__', mock_init)
    return FileReader(mock_parse, 'Driver')

def test_file_reader_no_file(file_reader):
    """Test if FileReader can return list of objects"""
    with pytest.raises(FileNotFoundError):
        file_reader.read_file("./tests/data/does_not_exist.txt")


# def test_file_reader(mocker: MockerFixture):
#     def mock_init(self, data):
#         self.data = data
#     def mock_parse(line):
#         return line
#     mocker.patch.object(Driver, '__init__', mock_init)
#     file_reader = FileReader(mock_parse, 'Driver')
#     list = file_reader.read_file("./tests/data/input1.txt")
#     print(list)