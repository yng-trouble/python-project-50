from gendiff.gendiff import generate_diff
from tests.test_data.flat_json_expected import expected_result, parsed_json1, parsed_json2


def test_flat_json_diff():
    assert generate_diff(parsed_json1, parsed_json2) == expected_result