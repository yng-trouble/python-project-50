from gendiff.gendiff import generate_diff
from tests.test_data.flat_expected import expected_result, parsed1, parsed2


def test_flat_diff():
    assert generate_diff(parsed1, parsed2) == expected_result