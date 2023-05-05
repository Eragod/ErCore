import time
import platform

from std.Base import *


class ECore:
    def __init__(self):
        self.version = 1.5
        self.IS_WINDOWS = (platform.system() == 'Windows')
        self.IS_LINUX = (platform.system() == 'Linux')
        self.IS_MAC = (platform.system() == 'Darwin')

    def info(self):
        try:
            print(f'Autor: Eragod\nProject: ErCore\nVersion: {self.version}')
        except Exception as error:
            print(f'{f_red}Error!\n{error}\nError!{reset}')

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
                print(f'{bold}{f_red}{hour}:{minute}:{second}:{reset}',
                      f'{function.__name__} Start work!')
                function()
                second = time.localtime().tm_sec
                minute = time.localtime().tm_min
                hour = time.localtime().tm_hour
                print(f'{bold}{f_red}{hour}:{minute}:{second}:{reset}',
                      f'{function.__name__} End work!')
            else:
                ...
        except Exception as error:
            print(f'{f_red}Error!\n{error}\nError!{reset}')


def EDecor(iteration: int = 1):
    def EraDeCore(func):
        def wrapper(*args, **kwargs):
            for _ in range(iteration):
                func(*args, **kwargs)
        return wrapper
    return EraDeCore
