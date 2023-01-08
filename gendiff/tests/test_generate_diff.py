from gendiff.generate_difference import generate_diff
from gendiff.parser import parser


first_file = 'gendiff/tests/fixtures/file1.json'
second_file = 'gendiff/tests/fixtures/file2.json'
expected = 'gendiff/tests/fixtures/test'
expected1 = 'gendiff/tests/fixtures/test1'


def test_generate_diff():
    with open(expected) as f:
        assert generate_diff(first_file, second_file) == f.read()


def test_parser():
    with open(expected1) as f:
        assert str(parser(first_file)) == f.read()
