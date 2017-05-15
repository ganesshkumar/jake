from setuptools import setup

setup(
    name='jake',
    version='0.0.2',
    description='CLI for personal tools',
    author='Ganessh Kumar R P',
    author_email='rpganesshkumar@gmail.com',
    url='https://github.com/ganesshkumar/jake',
    download_url='',
    keywords=['personal assistant', 'tasks', 'todos'],
    py_modules=['jake'],
    install_requires=[
        'click',
        'tinydb'
    ],
    entry_points='''
        [console_scripts]
        jake=jake:cli
    '''
)
