from setuptools import setup, find_packages

setup(
    name='ErCore',
    version='1.0',
    packages=find_packages(),
    author='Eragod',
    description='Core for projects',
    url="https://github.com/Eragod/ErCore",
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    entry_points={'console_scripts': ['ErCore-project = ErCore.cli:make_project',
                                      'ErCore-runner = ErCore.cli:make_runner']},
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent'],
)
