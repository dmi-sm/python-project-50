from gendiff import generate_diff


first_flat_json = 'gendiff/tests/fixtures/flat/file1.json'
second_flat_json = 'gendiff/tests/fixtures/flat/file2.json'
first_flat_yml = 'gendiff/tests/fixtures/flat/file1.yml'
second_flat_yaml = 'gendiff/tests/fixtures/flat/file2.yaml'
expected_flat_stylish = 'gendiff/tests/fixtures/flat/testflatstylish'

first_nested_json = 'gendiff/tests/fixtures/nested/file1.json'
second_nested_json = 'gendiff/tests/fixtures/nested/file2.json'
first_nested_yml = 'gendiff/tests/fixtures/nested/file1.yml'
second_nested_yaml = 'gendiff/tests/fixtures/nested/file2.yaml'
expected_nested_stylish = 'gendiff/tests/fixtures/nested/testnestedstylish'

expected_nested_plain = 'gendiff/tests/fixtures/nested/testnestedplain'


def test_flat_json_stylish_generate_diff():
    with open(expected_flat_stylish) as expected:
        result = generate_diff(first_flat_json, second_flat_json, 'stylish')
        assert result == expected.read()


def test_nested_json_stylish_generate_diff():
    with open(expected_nested_stylish) as expected:
        result = generate_diff(first_nested_json, second_nested_json, 'stylish')  # noqa: E501
        assert result == expected.read()


def test_nested_json_plain_generate_diff():
    with open(expected_nested_plain) as expected:
        result = generate_diff(first_nested_json, second_nested_json, 'plain')
        assert result == expected.read()


def test_nested_yml_stylish_generate_diff():
    with open(expected_nested_stylish) as expected:
        result = generate_diff(first_nested_yml, second_nested_yaml, 'stylish')
        assert result == expected.read()


def test_nested_yml_plain_generate_diff():
    with open(expected_nested_plain) as expected:
        result = generate_diff(first_nested_yml, second_nested_yaml, 'plain')
        assert result == expected.read()
