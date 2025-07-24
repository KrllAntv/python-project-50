from gendiff.generate_diff import generate_diff
import pytest

def read_file_test():
    with open('tests/test_data/expectation_diff.txt', 'r') as file:
        data = file.read()
        return data

def read_empty_file():
    return '{\n  \n}'

def test_generate_diff():
    assert generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.json') == read_file_test()
    assert generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.yaml') == read_file_test()
    assert generate_diff('tests/test_data/empty_file1.json', 'tests/test_data/empty_file2.json') == read_empty_file()


def test_unsupport_format():
    with pytest.raises(ValueError):
        generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.xml') #XML unsupported format 
    assert generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.json') == read_file_test()
