#!/usr/bin/env python3
import argparse
import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as f1:
        json_1 = json.load(f1)
    with open(file_path2, 'r') as f2:
        json_2 = json.load(f2)

    keys_arr = sorted(set(json_1) | set(json_2))
    differences = []
    for key in keys_arr:
        value_1 = json_1.get(key)
        value_2 = json_2.get(key)
        if value_1 == value_2:
            differences.append(f"  {key}: {value_1}")
        else:
            if value_1 is not None:
                differences.append(f"- {key}: {value_1}")
            if value_2 is not None:
                differences.append(f"+ {key}: {value_2}")

    return "\n".join(differences)


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
