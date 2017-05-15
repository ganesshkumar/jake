import click
from db import tasks

def add(text):
	id = tasks.add(text)
	click.echo(click.style('Task #{} successfully added'.format(id), fg='green'))

def get_all():
	task_list = tasks.get_all()	
	print_tasks(task_list)

def get_completed_tasks():
	task_list = tasks.completed()
	print_tasks(task_list)

def get_active_tasks():
	task_list = tasks.active()
	print_tasks(task_list)

def check(task_id):
	tasks.check(task_id)
	get_all()

def uncheck(task_id):
	tasks.uncheck(task_id)
	get_all()

def remove(task_id):
	tasks.remove(task_id)
	click.echo(click.style('Task #{} successfully removed'.format(task_id), fg='green'))	

def print_tasks(tasks):
	for index, task in enumerate(tasks):
		text = u'{} {} {}'.format(u'\u2713' if task['completed'] else ' ', task.eid, task['text'])
		text = click.style(text, fg='green') if task['completed'] else text
		click.echo(text)