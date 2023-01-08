from gendiff.parser import parser


STATUS = {
    'in_first': '  - ',
    'in_second': '  + ',
    'both': '    '
}


def generate_diff(first, second, format=None):
    first = dict(sorted((parser(first)).items()))
    second = dict(sorted((parser(second)).items()))
    all_keys = sorted(set(first | second))
    diff = '{\n'

    for key in all_keys:
        if key in first and key not in second:
            diff += f'{STATUS["in_first"]}{key}: {first[key]}\n'
        elif key in second and key not in first:
            diff += f'{STATUS["in_second"]}{key}: {second[key]}\n'
        elif first[key] != second[key]:
            diff += f'{STATUS["in_first"]}{key}: {first[key]}\n'
            diff += f'{STATUS["in_second"]}{key}: {second[key]}\n'
        else:
            diff += f'{STATUS["both"]}{key}: {first[key]}\n'
    diff += '}'

    return diff
