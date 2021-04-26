from gendiff.scripts.parse_file import parse_file


def generate_diff(file_path_1, file_path_2):
    """

    :param file_path_1: str
    :param file_path_2: str
    :return: str
    """
    decoded_data_1 = parse_file(file_path_1)
    decoded_data_2 = parse_file(file_path_2)

    if decoded_data_1 is None:
        decoded_data_1 = dict()
    if decoded_data_2 is None:
        decoded_data_2 = dict()

    keys_arr = sorted(set(decoded_data_1) | set(decoded_data_2))
    differences = []
    for key in keys_arr:
        value_1 = decoded_data_1.get(key)
        value_2 = decoded_data_2.get(key)
        if value_1 == value_2:
            differences.append(f"    {key}: {value_1}")
        else:
            if value_1 is not None:
                differences.append(f"  - {key}: {value_1}")
            if value_2 is not None:
                differences.append(f"  + {key}: {value_2}")
    output = '\n'.join(differences)
    return f'{{\n{output}\n}}' if len(differences) else ""