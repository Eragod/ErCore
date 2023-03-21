from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name='ErCore',
    version='0.2',
    packages=['ErCore'],
    author='Eragod',
    description='This is a core for my package',
    url="https://github.com/Eragod/ErCore",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={'console_scripts': ['ErCore = ErCore.cli:make_project_command']},
)
