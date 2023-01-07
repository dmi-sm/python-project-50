# !/usr/bin/env python3
from gendiff.cli import parse_arguments
import gendiff


def main():
    args = parse_arguments()
    print(gendiff.generate_diff(args))


if __name__ == '__main__':
    main()
