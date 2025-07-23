from gendiff.generate_diff import generate_diff
import pytest

def read_file_test():
    with open('tests/test_data/expectation_diff.txt', 'r') as file:
        data = file.read()
        return data

def test_generate_diff():
    assert generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.json') == read_file_test()


@pytest.mark.xfail(raises=ValueError)
def test_unsupport_format():
    assert generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.yml')