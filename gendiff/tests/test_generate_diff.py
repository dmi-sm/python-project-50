import pytest
from gendiff.generate_difference import generate_diff


files = 'files/file1.json', 'files/file2.json'
result = 'gendiff/tests/fixtures/test'


@pytest.mark.parametrize('paths, expected', [(files, result)])
def test_generate_diff(paths, expected):
    with open(expected) as f:
        assert generate_diff(paths) == f.read()
