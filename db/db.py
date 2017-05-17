from tinydb import TinyDB, Query
import os

DATABASE_NAME = 'jake'

__db = TinyDB('{}/{}.json'.format(os.environ['HOME'], DATABASE_NAME))
__tables = {}

def get_table(name):
	if name in __tables:
		return __tables[name]
	else:
		__tables[name] = __db.table(name)
		return __tables[name]
		