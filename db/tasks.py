from db import db
from tinydb import Query

tasks = db.table('tasks')

def add(text):
	return tasks.insert({'text': text, 'completed': False, 'active': True})

def get_all():
	Task = Query()
	return tasks.search(Task.active == True)

def active():
	Task = Query()
	return tasks.search((Task.completed == False) & (Task.active == True))

def completed():
	Task = Query()
	return tasks.search((Task.completed == True) & (Task.active == True))

def check(task_id):
	return tasks.update({'completed': True},  eids=[task_id])

def uncheck(task_id):
	return tasks.update({'completed': False},  eids=[task_id])

def remove(task_id):
	return tasks.update({'active': False},  eids=[task_id])
