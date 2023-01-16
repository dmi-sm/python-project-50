from gendiff.parse import get_content
from gendiff.diff_tree import get_diff_tree
from gendiff.formatters.formatter import set_format


def generate_diff(first_file, second_file, format):
    first = get_content(first_file)
    second = get_content(second_file)

    diff_tree = get_diff_tree(first, second)
    formatted_diff = set_format(format, diff_tree)

    return formatted_diff
