from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


def set_format(format, tree):
    FORMATS = {
        'stylish': get_stylish(tree),
        'plain': get_plain(tree),
        'json': get_json(tree)
    }
    return FORMATS.get(format)
