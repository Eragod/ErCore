from setuptools import setup

setup(
    name='ErCore',
    version='0.1',
    packages=['ErCore'],
    entry_points={
        'console_scripts': [
            'ErCore = ErCore.cli:make_project_command'
        ]
    }
)
