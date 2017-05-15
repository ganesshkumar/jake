import click
import sys

from tasks import tasks_manager

@click.group()
@click.version_option(version='0.0.2')
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
@click.option('-a', 'filter', flag_value='ALL')
@click.option('-c', 'filter', flag_value='COMPLETED')
def list(filter):
	"""list active tasks. -c to list completed tasks and -a to list all tasks"""
	if filter == 'ALL':
		tasks_manager.get_all()
	elif filter == 'COMPLETED':
		tasks_manager.get_completed_tasks()
	else:
		tasks_manager.get_active_tasks()

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