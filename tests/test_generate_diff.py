from gendiff.generate_diff import generate_diff
import pytest


def read_file_test(arg):
    with open(str(arg), 'r') as file:
        data = file.read()
        return data
     

def read_empty_file():
    return '{\n}'


def test_generate_diff():
    assert generate_diff(
        'tests/test_data/file1.json',
        'tests/test_data/file2.json'
    ) == read_file_test('tests/test_data/expectation_diff.txt')
    assert generate_diff(
        'tests/test_data/file1.json',
        'tests/test_data/file2.yaml'
    ) == read_file_test('tests/test_data/expectation_diff.txt')
    assert generate_diff(
        'tests/test_data/test_file1.json',
        'tests/test_data/test_file2.json'
    ) == read_file_test('tests/test_data/expect_diff.txt')
    assert generate_diff(
        'tests/test_data/empty_file1.json',
        'tests/test_data/empty_file2.json'
    ) == read_empty_file()


def test_unsupport_format():
    with pytest.raises(ValueError):
        generate_diff(
            'tests/test_data/file1.json',
            'tests/test_data/file2.xml'
        )  # XML unsupported format


def test_plain():
    assert generate_diff(
        'tests/test_data/test_file1.json',
        'tests/test_data/test_file2.json',
        'plain'
        ) == read_file_test('tests/test_data/test_plain.txt')
    assert generate_diff(
        'tests/test_data/test_file1.json',
        'tests/test_data/test_file2.yaml',
        'plain'
    ) == read_file_test('tests/test_data/test_plain.txt')