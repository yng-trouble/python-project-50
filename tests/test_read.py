from gendiff.parsing_files import read

from tests.test_data.read_expected import expected_flat


def test_read_json():
    path_to_example = 'tests/test_data/example.json'
    assert read(path_to_example) == expected_flat

def test_read_yaml():
    path_to_example = 'tests/test_data/example.yml'
    assert read(path_to_example) == expected_flat

