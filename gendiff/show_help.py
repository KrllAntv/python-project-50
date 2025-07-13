import argparse

parser = argparse.ArgumentParser(
    prog='gendiff',
    description='Compares two configuration files and shows a difference.',
    )

parser.add_argument('first_file')
parser.add_argument('second_file')

def shows_help():
    parser.print_help()
