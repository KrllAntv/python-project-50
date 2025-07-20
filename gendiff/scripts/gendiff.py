import argparse
from gendiff.generate_diff import read_diff, stylish_format, sorted_diff

def main():
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

    diff1 = read_diff(args.first_file)
    diff2 = read_diff(args.second_file)

    sort_diff = sorted_diff(diff1, diff2)
    result = stylish_format(sort_diff)
    print(result)

if __name__ == '__main__':
    main()

