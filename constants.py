SOURCE_ROOT = 'source'
SOURCE_FILE = 'players.csv'

PITCHERS_STRUCT = 'Pitchers'
HITTERS_STRUCT = 'Hitters'

TAG = 'position'
PITCHERS_SOURCE = 'Pitcher'

TABLES = ['Pitchers', 'Hitters']
LOG_TABLE = 'Log'

DATABASE_ERROR_TEMPLATE = '{} happens'

DATABASE_CONNECTION_ERROR = 'Something wrong with connection establish, ' + DATABASE_ERROR_TEMPLATE
DROP_TABLE_ERROR = 'Can\'t drop tables, ' + DATABASE_ERROR_TEMPLATE
CREATE_TABLE_ERROR = 'Can\'t create tables, ' + DATABASE_ERROR_TEMPLATE
INSERTION_ERROR = 'You should create tables before perform insertion, ' + DATABASE_ERROR_TEMPLATE
