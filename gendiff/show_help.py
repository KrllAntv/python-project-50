import argparse
from gendiff.generate_diff import check_diff

parser = argparse.ArgumentParser(
    prog='gendiff',
    description='Compares two configuration files and shows a difference.',
    )

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument(
    '-f', '--format',
    dest='format',
    help='set format of output',
)
args = parser.parse_args()

def shows_help():
    #parser.print_help()
    result = check_diff(args.first_file, args.second_file)
    print(result)
