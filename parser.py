import argparse
import csv
import sys


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('--create_tables', help='create tables', action='store_true')
    parser.add_argument('--drop_tables', help='drop tables', action='store_true')
    parser.add_argument('--chunk_size', help='specify size of records in one transaction (integer)', type=int)
    parser.add_argument('--source', help='specify path to source file within \'source\' directory '
                                         '(by default \'players.csv\')')
    return parser.parse_args()


def parse_csv(path):
    try:
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                yield row
    except FileNotFoundError:
        sys.exit('Make shore that you provide correct source name in *.csv format')
