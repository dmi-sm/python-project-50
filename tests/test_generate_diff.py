import os
from gendiff import generate_diff


first_json = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
second_json = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
first_yml = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')
second_yaml = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.yaml')

stylish = os.path.join(os.path.dirname(__file__), 'fixtures', 'stylish')
plain = os.path.join(os.path.dirname(__file__), 'fixtures', 'plain')


def test_json_stylish_generate_diff():
    with open(stylish) as expected:
        result = generate_diff(first_json, second_json, 'stylish')
        assert result == expected.read()


def test_json_plain_generate_diff():
    with open(plain) as expected:
        result = generate_diff(first_json, second_json, 'plain')
        assert result == expected.read()


def test_yml_stylish_generate_diff():
    with open(stylish) as expected:
        result = generate_diff(first_yml, second_yaml, 'stylish')
        assert result == expected.read()


def test_yml_plain_generate_diff():
    with open(plain) as expected:
        result = generate_diff(first_yml, second_yaml, 'plain')
        assert result == expected.read()
