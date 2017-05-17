import click
import sys

from tasks import tasks_manager

@click.group()
@click.version_option(version='0.0.4')
def cli():
  """CLI for personal tools"""
  pass

# Commands for isen
@cli.group()
def tasks():
	"""Tasks to be done"""
	pass

# Commands for task group
@tasks.command()
@click.argument('task', type=click.STRING, required=True)
def add(task):
	"""add a new task"""
	tasks_manager.add(task)

@tasks.command()
@click.option('-a', 'filter', flag_value='ALL', help='show all tasks')
@click.option('-c', 'filter', flag_value='COMPLETED', help='show completed tasks')
@click.option('-s', default=None, type=click.STRING, help='search term')
@click.option('-cs', 'case_sensitive', flag_value=True, help='case sensitive search')
def list(filter, s, case_sensitive=False):
	"""list active tasks. -c to list completed tasks, -a to list all tasks and -s <search_term> to search tasks"""
	if filter == 'ALL':
		tasks_manager.get_all(s, case_sensitive)
	elif filter == 'COMPLETED':
		tasks_manager.get_completed_tasks(s, case_sensitive)
	else:
		tasks_manager.get_active_tasks(s, case_sensitive)

@tasks.command()
@click.argument('id', type=click.INT, required=True)
def check(id):
	"""mark a task as completed"""
	tasks_manager.check(id)

@tasks.command()
@click.argument('id', type=click.INT, required=True)
def uncheck(id):
	"""unmark a task to make it active"""
	tasks_manager.uncheck(id)

@tasks.command()
@click.argument('id', type=click.INT, required=True)
def remove(id):
	"""remove a task"""
	tasks_manager.remove(id)