import logging

from database.db_handler import DbHandler


class LogToDbHandler(logging.Handler):
    def emit(self, record):
        self.format(record)
        table = DbHandler()
        table.insert_logging_record(record.__dict__)
