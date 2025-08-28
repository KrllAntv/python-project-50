import argparse

from gendiff.scripts.generate_diff import generate_diff

parser = argparse.ArgumentParser(
    prog='gendiff',
    description='Compares two configuration files and shows a difference.',
    )

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument(
    '-f', '--format',
    default='stylish',
    help='set format of output',
    type=str
    )


def main():
    args = parser.parse_args()

    data = generate_diff(args.first_file, args.second_file, args.format)
    print(data)


if __name__ == '__main__':
    main()

