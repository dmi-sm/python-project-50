import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='Gendiff',
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', type=str, help='first file path')
    parser.add_argument('second_file', type=str, help='second file path')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        choices=('stylish', 'plain', 'json'),
        metavar='FORMAT',
        help='format style, supported: %(choices)s. Default: %(default)s'
    )
    return parser.parse_args()
