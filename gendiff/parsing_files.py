import json 


def read(path_to_file):
    if path_to_file[-4:] == 'json':
        json_file = json.load(open(path_to_file))
        return json_file
