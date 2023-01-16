from gendiff import generate_diff


first_flat = 'gendiff/tests/fixtures/flat/file1.json'
second_flat = 'gendiff/tests/fixtures/flat/file2.json'
expected_flat_stylish = 'gendiff/tests/fixtures/flat/testflatstylish'

first_nested = 'gendiff/tests/fixtures/nested/file1.json'
second_nested = 'gendiff/tests/fixtures/nested/file2.json'
expected_nested_stylish = 'gendiff/tests/fixtures/nested/testnestedstylish'

expected_nested_plain = 'gendiff/tests/fixtures/nested/testnestedplain'


def test_flat_stylish_generate_diff():
    with open(expected_flat_stylish) as expected:
        result = generate_diff(first_flat, second_flat)
        assert result == expected.read()


def test_nested_stylish_generate_diff():
    with open(expected_nested_stylish) as expected:
        result = generate_diff(first_nested, second_nested, 'stylish')
        assert result == expected.read()


def test_nested_plain_generate_diff():
    with open(expected_nested_plain) as expected:
        result = generate_diff(first_nested, second_nested, 'plain')
        assert result == expected.read()
