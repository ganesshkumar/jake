import click
from db import tasks

def add(text):
	id = tasks.add(text)
	click.echo(click.style('Task #{} successfully added'.format(id), fg='green'))

def get_all(search_term, case_sensitive):
	task_list = tasks.get_all(search_term, case_sensitive)	
	print_tasks(task_list)

def get_completed_tasks(search_term, case_sensitive):
	task_list = tasks.completed(search_term, case_sensitive)
	print_tasks(task_list)

def get_active_tasks(search_term, case_sensitive):
	task_list = tasks.active(search_term, case_sensitive)
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
		text = u'{} {} {}'.format(u'\u2713' if task['completed'] else u'\u00b7', task.eid, task['text'])
		text = ' '.join([__style_keyword(text_part, task) for text_part in text.split()])
		click.echo(text)

def __style_keyword(keyword, task):
	if keyword.startswith('@'):
		return click.style(keyword, fg='cyan')
	elif keyword.startswith(':'):
		return click.style(keyword, fg='magenta')
	elif keyword.startswith('#'):
		return click.style(keyword, fg='blue')
	else:
		return click.style(keyword, fg='green' if task['completed'] else 'white')