from tinydb import TinyDB, Query
import os

db = TinyDB('{}/.jake_data.json'.format(os.environ['HOME']))

def get_db():
	return db