#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def add_env_file():
    env_file = """# Load env variables with dotenv package in settings.py (or elsewhere)

## settings.py
# from dotenv import load_dotenv
# from pathlib import Path 
# env_path = Path('.') / '.env'
# load_dotenv(env_path)


### sample .env file ###

# CONFIG_PATH=${HOME}/.config/foo
# S3_BUCKET=YOURS3BUCKET
# SECRET_KEY=YOURSECRETKEYGOESHERE"""

    with open(os.path.join(PROJECT_DIRECTORY, '.env'), 'w+') as f:
        f.write(env_file)


def add_folder(folderpath):
    os.makedirs(os.path.join(PROJECT_DIRECTORY, folderpath), exist_ok=True)


if __name__ == '__main__':

    add_env_file()
    folders_to_add = ['cache', 'data/final', 'data/raw' ]
    for folder in folders_to_add:
        add_folder(folder)

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
