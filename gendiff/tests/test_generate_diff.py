from gendiff.generate_difference import generate_diff


first_flat_stylish = 'gendiff/tests/fixtures/flat/file1.json'
second_flat_stylish = 'gendiff/tests/fixtures/flat/file2.json'
expected_flat_stylish = 'gendiff/tests/fixtures/flat/testflatstylish'

first_nested_stylish = 'gendiff/tests/fixtures/nested/file1.json'
second_nested_stylish = 'gendiff/tests/fixtures/nested/file2.json'
expected_nested_stylish = 'gendiff/tests/fixtures/nested/testnestedstylish'


def test_flat_stylish_generate_diff():
    with open(expected_flat_stylish) as f:
        assert generate_diff(first_flat_stylish, second_flat_stylish) == f.read()


def test_nested_stylish_generate_diff():
    with open(expected_nested_stylish) as f:
        assert generate_diff(first_nested_stylish, second_nested_stylish) == f.read()
