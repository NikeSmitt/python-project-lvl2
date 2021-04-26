import json
import yaml


def parse_json(file_path):
    return json.load(open(file_path))


def parse_yaml(file_path):
    return yaml.safe_load(open(file_path))


def parse_file(file_path):
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        return parse_yaml(file_path)
    return parse_json(file_path)
