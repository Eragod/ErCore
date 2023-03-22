from setuptools import setup

with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

with open('ErCore/VERSION', 'r') as version_file:
    version = version_file.read().strip()

setup(
    name='ErCore',
    version=version,
    packages=['ErCore'],
    author='Eragod',
    description='This is a core for my package',
    url="https://github.com/Eragod/ErCore",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={'console_scripts': ['ErCore = ErCore.cli:make_project_command']},
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent'],
)
