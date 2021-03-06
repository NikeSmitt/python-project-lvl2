#!/usr/bin/env python3
from gendiff.scripts.generate_diff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()

    output = generate_diff(args.first_file, args.second_file)
    print(output)


if __name__ == "__main__":
    main()
