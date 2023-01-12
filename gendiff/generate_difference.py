from gendiff.parse import get_content
from gendiff.formatters.stylish import get_stylish
from gendiff.diff_tree import get_diff_tree


def generate_diff(first_file, second_file, format=get_stylish):
    first = get_content(first_file)
    second = get_content(second_file)
    diff = format(get_diff_tree(first, second))

    return diff
