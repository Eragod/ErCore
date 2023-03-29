import os
import time
import platform


class ECore:
    def __init__(self):
        self.t = 5
        self.version = None
        self.IS_WINDOWS = (platform.system() == 'Windows')
        self.IS_LINUX = (platform.system() == 'Linux')
        self.IS_MAC = (platform.system() == 'Darwin')

    def info(self):
        try:
            with open('VERSION', 'r') as ver:
                self.version = ver.read()
            print(f'Autor: Eragod\nProject: ErCore\nVersion: {self.version}')
        except Exception as e:
            print(f'Error!\n{e}\nError!')

    def wait(self, t):
        self.t = t
        time.sleep(self.t)

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
