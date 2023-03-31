import time
import platform
from __version__ import __version__


class ECore:
    def __init__(self):
        self.t = 5
        self.version = __version__
        self.IS_WINDOWS = (platform.system() == 'Windows')
        self.IS_LINUX = (platform.system() == 'Linux')
        self.IS_MAC = (platform.system() == 'Darwin')

    def info(self):
        try:
            print(f'Autor: Eragod\nProject: ErCore\nVersion: {self.version}')
        except Exception as error:
            print(f'Error!\n{error}\nError!')

    @staticmethod
    def wait(t):
        time.sleep(t)

    def start(self):
        file = input('file name: ')
        if self.IS_WINDOWS:
            with open(f'run.bat', 'w') as runner:
                runner.write(f'@echo off\npython {file}.py\npause')
        if self.IS_LINUX:
            with open(f'run.sh', 'w') as runner:
                runner.write(f'#!/bin/bash\n\npython3 {file}.py')
        if self.IS_MAC:
            with open(f'run.sh', 'w') as runner:
                runner.write(f'#!/bin/bash\n\npython3 {file}.py')


def EDecor(iteration: int = 1):
    def EraDeCore(func):
        def wrapper(*args, **kwargs):
            for _ in range(iteration):
                func(*args, **kwargs)

        return wrapper

    return EraDeCore
