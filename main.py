import sys

from constants import SOURCE_ROOT, SOURCE_FILE, PITCHERS, HITTERS
from database.db_handler import DbHandler
from parser import parse_input, parse_csv


def service_args_handler(arguments, tables):
    if arguments.drop_tables:
        tables.drop_table()
        sys.exit('Tables was successfully dropped')
    if arguments.create_tables:
        tables.create_table()
        sys.exit('Tables was successfully created')


def source_path_handler(arguments):
    source = '/'.join((SOURCE_ROOT, SOURCE_FILE))
    if arguments.source:
        source = '/'.join((SOURCE_ROOT, arguments.source))
    return source


def create_and_insert_struct(parsed_data, tables):
    struct = {PITCHERS: [], HITTERS: []}

    for n, el in enumerate(parsed_data):
        if el.get('position') == 'Pitcher':
            struct[PITCHERS].append(el)
        else:
            struct[HITTERS].append(el)
        if n % 5000 == 0:
            print(n)
            for tablename, data in struct.items():
                tables.insert(tablename, data)
                # for tablename, data in struct.items():
                #     tables.insert(tablename, data)


def executor():
    arguments = parse_input()

    tables = DbHandler()

    service_args_handler(arguments, tables)

    source = source_path_handler(arguments)

    parsed_data = parse_csv(source)

    create_and_insert_struct(parsed_data, tables)


if __name__ == "__main__":
    executor()
