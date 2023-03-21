import argparse
import os


def make_project(name, directory):
    os.mkdir(directory)
    os.rename(directory, name)
    os.chdir('..')

    with open('README.md', 'w') as readme:
        readme.write(f'# {name}')


def make_project_command():
    parser = argparse.ArgumentParser(description='Create a new project')
    parser.add_argument('name', help='name of the project')
    parser.add_argument('--dir', default='.', help='directory to create project in')
    args = parser.parse_args()
    make_project(args.name, args.dir)
