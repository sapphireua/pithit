import sqlite3

from constants import TABLES


class DbHandler(object):
    def __init__(self, db_path='database/pithit.db'):
        self.db_path = db_path

    def _connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self._connection() as conn:
            for tablename in TABLES:
                try:
                    conn.execute('CREATE TABLE {tablename} ('
                                 'id text PRIMARY KEY, '
                                 'first_name text, '
                                 'last_name text, '
                                 'position text, '
                                 'weight int)'.format(tablename=tablename))
                except sqlite3.OperationalError as e:
                    print(e)
                    continue

    def drop_table(self):
        with self._connection() as conn:
            for el in TABLES:
                conn.execute('DROP TABLE IF EXISTS {}'.format(el))

    def insert(self, tablename, data):
        with self._connection() as conn:
            conn.executemany('INSERT OR REPLACE INTO {tablename} VALUES('
                             'COALESCE((SELECT id FROM {tablename} WHERE id = :playerID), :playerID), '
                             'COALESCE((SELECT first_name FROM {tablename} WHERE id = :playerID), :nameFirst), '
                             'COALESCE((SELECT last_name FROM {tablename} WHERE id = :playerID), :nameLast), '
                             'COALESCE((SELECT position FROM {tablename} WHERE id = :playerID), :position), '
                             ':weight)'.format(tablename=tablename), data)
