import time
import platform

from std import colors, style


class ECore:
    def __init__(self):
        self.version = 1.1
        self.IS_WINDOWS = (platform.system() == 'Windows')
        self.IS_LINUX = (platform.system() == 'Linux')
        self.IS_MAC = (platform.system() == 'Darwin')

    def info(self):
        try:
            print(f'Autor: Eragod\nProject: ErCore\nVersion: {self.version}')
        except Exception as error:
            print(f'{colors["Red"]}Error!\n{error}\nError!{colors["Reset"]}')

    def make_runner(self):
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

    @staticmethod
    def logger(function):
        try:
            if function is not None:
                second = time.localtime().tm_sec
                minute = time.localtime().tm_min
                hour = time.localtime().tm_hour
                print(f'{style["BOLD"]}{colors["Red"]}{hour}:{minute}:{second}:{colors["Reset"]}',
                      f'{function.__name__} Start work!')
                function()
                second = time.localtime().tm_sec
                minute = time.localtime().tm_min
                hour = time.localtime().tm_hour
                print(f'{style["BOLD"]}{colors["Red"]}{hour}:{minute}:{second}:{colors["Reset"]}',
                      f'{function.__name__} End work!')
            else:
                ...
        except Exception as error:
            print(f'{error}')


def EDecor(iteration: int = 1):
    def EraDeCore(func):
        def wrapper(*args, **kwargs):
            for _ in range(iteration):
                func(*args, **kwargs)
        return wrapper
    return EraDeCore
