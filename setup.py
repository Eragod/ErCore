from setuptools import setup, find_packages

with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

with open('ErCore/VERSION', 'r') as version_file:
    version = version_file.read().strip()

setup(
    name='ErCore',
    version=version,
    packages=find_packages(),
    author='Eragod',
    description='This is a core for my package',
    url="https://github.com/Eragod/ErCore",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={'console_scripts': ['ErCore make-project = ErCore.cli:make_project',
                                      'ErCore make-runner = ErCore.cli:make_runner']},
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent'],
)
