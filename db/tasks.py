import re
from db import db
from tinydb import Query

tasks = db.table('tasks')

def add(text):
	return tasks.insert({'text': text, 'completed': False, 'active': True})

def get_all(search_term, case_sensitive):
	Task = Query() 
	return tasks.search((Task.active == True) & (Task.text.test(__compare, search_term, case_sensitive)))

def active(search_term, case_sensitive):
	Task = Query()
	return tasks.search((Task.completed == False) & (Task.active == True) & (Task.text.test(__compare, search_term, case_sensitive)))

def completed(search_term, case_sensitive):
	Task = Query()
	return tasks.search((Task.completed == True) & (Task.active == True) & (Task.text.test(__compare, search_term, case_sensitive)))

def check(task_id):
	return tasks.update({'completed': True},  eids=[task_id])

def uncheck(task_id):
	return tasks.update({'completed': False},  eids=[task_id])

def remove(task_id):
	return tasks.update({'active': False},  eids=[task_id])

def __compare(val, search_term, case_sensitive):
	search_term = __normalize('(^|.*\\s){}($|\\s.*)'.format(search_term))
	pattern = re.compile(search_term) if case_sensitive else re.compile(search_term, re.IGNORECASE)
	return pattern.match(val)

def __normalize(search_term):
	"""Normalize search term"""
	return search_term if search_term is not None else ''