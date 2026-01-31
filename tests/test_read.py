from gendiff.parsing_files import read

expected_result = {
  "host": "hexlet.io",
  "timeout": 50,
  "verbose": True
}


def test_read_json():
    path_to_example = 'tests/test_data/example.json'
    assert read(path_to_example) == expected_result
