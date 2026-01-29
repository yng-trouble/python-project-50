import argparse
from gendiff import parsing_files
from gendiff.gendiff import generate_diff

def run_gendiff():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='''Compares two configuration files and shows a difference.''')
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_parsed = parsing_files.read(args.first_file)
    second_parsed = parsing_files.read(args.second_file)
    generate_diff(first_parsed, second_parsed)

if __name__ == '__main__':
    run_gendiff()
