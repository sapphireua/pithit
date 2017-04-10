pithit
======

Installation
------------

You don't need any installation, only Python >= 3.1 required on your
machine

Avaliable options
-----------------

`$ python3 main.py` - run without arguments, source file is
'source/players.csv'.

`$ python3 main.py -h`  - get help about available arguments.

`$ python3 main.py --drop_log_table` - drop log table in database,
after what system exit happens.

`$ python3 main.py --create_log_table` - create log table in database,
after what system exit happens.

`$ python3 main.py --drop_tables` - drop tables in database,
after what system exit happens.

`$ python3 main.py --create_tables` - create tables in database,
after what system exit happens.

`$ python3 main.py --source` - specify source file within 'source'
folder.

`$ python3 main.py --chunk_size` - specify size of records in one
transaction (integer). You should use this option in case of large
source csv file for reduce memory consumption.

Running
-------

`$ cd pithit`

`$ python3 main.py --drop_tables`

`$ python3 main.py --create_tables`

`$ python3 main.py`

or

`$ python3 main.py --source=players.csv --chunk_size=5000`


