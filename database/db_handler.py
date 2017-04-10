import logging
import sqlite3
import sys

from constants import TABLES, DROP_TABLE_ERROR, CREATE_TABLE_ERROR, DATABASE_CONNECTION_ERROR, INSERTION_ERROR, \
    LOG_TABLE


class DbHandler(object):
    def __init__(self, db_path='database/pithit.db'):
        self.db_path = db_path
        self.logger = logging.getLogger('main_logger')

    def _connection(self):
        try:
            return sqlite3.connect(self.db_path)
        except Exception as e:
            self.logger.error(DATABASE_CONNECTION_ERROR.format(e))
            sys.exit()

    def create_logging_table(self):
        with self._connection() as conn:
            try:
                conn.execute('CREATE TABLE IF NOT EXISTS {} ('
                             'created text PRIMARY KEY, '
                             'name text, '
                             'loglevel text, '
                             'message text, '
                             'module text, '
                             'funcname text)'.format(LOG_TABLE)
                             )
            except sqlite3.OperationalError as e:
                sys.exit(CREATE_TABLE_ERROR.format(e))

    def drop_logging_table(self):
        with self._connection() as conn:
            try:
                conn.execute('DROP TABLE IF EXISTS {}'.format(LOG_TABLE))
            except sqlite3.OperationalError as e:
                self.logger.error(DROP_TABLE_ERROR.format(e))
                sys.exit()

    def insert_logging_record(self, data):
        with self._connection() as conn:
            try:
                conn.execute('INSERT INTO log VALUES(:asctime, :name, :levelname, :message, :module, :funcName)', data)
            except sqlite3.OperationalError as e:
                sys.exit(INSERTION_ERROR.format(e))

    def create_table(self):
        with self._connection() as conn:
            for tablename in TABLES:
                try:
                    conn.execute('CREATE TABLE IF NOT EXISTS {tablename} ('
                                 'id text PRIMARY KEY, '
                                 'first_name text, '
                                 'last_name text, '
                                 'position text, '
                                 'weight int)'.format(tablename=tablename))
                except sqlite3.OperationalError as e:
                    self.logger.error(CREATE_TABLE_ERROR.format(e))
                    sys.exit()

    def drop_table(self):
        with self._connection() as conn:
            try:
                for el in TABLES:
                    conn.execute('DROP TABLE IF EXISTS {}'.format(el))
            except sqlite3.OperationalError as e:
                self.logger.error(DROP_TABLE_ERROR.format(e))
                sys.exit()

    def insert(self, tablename, data):
        with self._connection() as conn:
            try:
                conn.executemany('INSERT OR REPLACE INTO {tablename} VALUES('
                                 'COALESCE((SELECT id FROM {tablename} WHERE id = :playerID), :playerID), '
                                 'COALESCE((SELECT first_name FROM {tablename} WHERE id = :playerID), :nameFirst), '
                                 'COALESCE((SELECT last_name FROM {tablename} WHERE id = :playerID), :nameLast), '
                                 'COALESCE((SELECT position FROM {tablename} WHERE id = :playerID), :position), '
                                 ':weight)'.format(tablename=tablename), data)
            except sqlite3.OperationalError as e:
                self.logger.error(INSERTION_ERROR.format(e))
                sys.exit()
