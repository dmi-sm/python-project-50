import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='Gendiff',
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', type=str, help='first file')
    parser.add_argument('second_file', type=str, help='second file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    return args.first_file, args.second_file
