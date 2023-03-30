import os
import sys
import datetime
import platform


def make_project():
    try:
        name = str(input('Enter project name: '))
        readme = str(input('Add readme file?[Y/N]: '))
        python = str(input('Add python file?[Y/N]: '))
        license = str(input('Add license file?[Y/N]: '))
        os.mkdir(name)
        os.chdir(name)
        if readme.lower() == 'y':
            with open('README.md', 'w') as read:
                read.write(f'# {name}')
        if python.lower() == 'y':
            with open('main.py', 'w') as py:
                py.write(f'# {name}\ndef main(name):\n    print("Hello " + name)')
        if license.lower() == 'y':
            print('only MIT work')
            license_type = str(input('Enter license type:'))
            if license_type.lower() == 'mit':
                mit_l = f"""MIT License
                Copyright © {datetime.date.year} {name}
                Permission is hereby granted, free of charge, to any person obtaining a copy of this software
                and associated documentation files (the “Software”), to deal in the Software without
                restriction, including without limitation the rights to use, copy, modify, merge, publish,
                distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
                Software is furnished to do so, subject to the following conditions:

                The above copyright notice and this permission notice shall be included in all copies or
                substantial portions of the Software.

                THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
                BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
                NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
                DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
                FROM,OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

                with open('LICENSE', 'w') as lt:
                    lt.write(mit_l)
            else:
                print('Error! WORK ONLY MIT LICENSE (try again)')
        else:
            print('')
    except ValueError as error:
        print('!!!' * 20)
        print(error)
        print('!!!' * 20)
        print('Helper: pls restart command and enter string')
    finally:
        print('1000-7 = ')  # this is a prank
        sys.exit(1000 - 7)


def make_runner():
    IS_WINDOWS = (platform.system() == 'Windows')
    IS_LINUX = (platform.system() == 'Linux')
    IS_MAC = (platform.system() == 'Darwin')
    file = input('file name: ')
    if IS_WINDOWS:
        with open(f'run.bat', 'w') as runner:
            runner.write(f'@echo off\npython {file}.py\npause')
    if IS_LINUX:
        with open(f'run.sh', 'w') as runner:
            runner.write(f'#!/bin/bash\n\npython3 {file}.py')
    if IS_MAC:
        with open(f'run.sh', 'w') as runner:
            runner.write(f'#!/bin/bash\n\npython3 {file}.py')
