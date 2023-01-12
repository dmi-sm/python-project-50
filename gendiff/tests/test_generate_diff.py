from gendiff.generate_difference import generate_diff


first_plane = 'gendiff/tests/fixtures/plane/file1.json'
second_plane = 'gendiff/tests/fixtures/plane/file2.json'
expected_plane = 'gendiff/tests/fixtures/plane/testplane'

first_nested = 'gendiff/tests/fixtures/nested/file1.json'
second_nested = 'gendiff/tests/fixtures/nested/file2.json'
expected_nested = 'gendiff/tests/fixtures/nested/testnested'


def test_plane_generate_diff():
    with open(expected_plane) as f:
        assert generate_diff(first_plane, second_plane) == f.read()


def test_nested_generate_diff():
    with open(expected_nested) as f:
        assert generate_diff(first_nested, second_nested) == f.read()
