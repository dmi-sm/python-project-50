# !/usr/bin/env python3
from gendiff.cli import parse_arguments
from gendiff.gendiff import generate_diff


def main():
    args = parse_arguments()
    print(generate_diff(args))


if __name__ == '__main__':
    main()
