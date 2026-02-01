import json

import yaml


def read(path_to_file):
    parsed_file = None
    if path_to_file[-4:] == 'json':
        parsed_file = json.load(open(path_to_file))
    elif path_to_file[-3:] == 'yml' or path_to_file[-4:] == 'yaml':
        file = open(path_to_file, 'r')
        parsed_file = yaml.safe_load(file)

    return parsed_file

