import sys

from constants import SOURCE_ROOT, SOURCE_FILE, PITCHERS_STRUCT, HITTERS_STRUCT, PITCHERS_SOURCE, TAG
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


def create_struct(parsed_data, tables, arguments):
    struct = {PITCHERS_STRUCT: [], HITTERS_STRUCT: []}

    for n, el in enumerate(parsed_data):
        if el.get(TAG) == PITCHERS_SOURCE:
            struct[PITCHERS_STRUCT].append(el)
        else:
            struct[HITTERS_STRUCT].append(el)
        if arguments.chunk_size:
            if n % arguments.chunk_size == 0 and n > 0:
                print('{} items was write, chunk write enabled '.format(n))
                insert_struct(tables, struct)
                struct[PITCHERS_STRUCT].clear()
                struct[HITTERS_STRUCT].clear()
    insert_struct(tables, struct)


def insert_struct(tables, struct):
    for tablename, data in struct.items():
        tables.insert(tablename, data)


def executor():
    arguments = parse_input()

    tables = DbHandler()

    service_args_handler(arguments, tables)

    source = source_path_handler(arguments)

    parsed_data = parse_csv(source)

    create_struct(parsed_data, tables, arguments)


if __name__ == "__main__":
    executor()
