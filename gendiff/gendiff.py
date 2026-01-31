def generate_diff(file1, file2):
    result_str = ''

    for key, value in file1.items():
        if key not in file2.keys():
            result_str += f'- {key}: {value}\n'
        
    for key, value in file2.items():
        if file1.get(key) == file2[key]:
            result_str += f'{key}: {value}\n'
        elif key in file1.keys() and file1[key] != file2[key]:
            result_str += f'- {key}: {file1[key]}\n'
            result_str += f'+ {key}: {file2[key]}\n'
        else:
            result_str += f'+ {key}: {value}\n'

    return result_str