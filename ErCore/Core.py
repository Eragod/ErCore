import os
import sys
import time
import random
import platform


class ECore:
    def __init__(self,
                 pre_functions: bool = False):
        self.t = None
        self.version = None
        self.pre_functions = pre_functions
        self.IS_WINDOWS = (platform.system() == 'Windows')
        self.IS_LINUX = (platform.system() == 'Linux')
        self.IS_MAC = (platform.system() == 'Darwin')

    def info(self):
        try:
            with open('VERSION', 'r') as ver:
                self.version = ver.read()
            print(f'Autor: Eragod\nProject: ErCore\nVersion: {self.version}')
        except Exception as e:
            print(f'Error!\n{e}')

    def wait(self, t):
        self.t = t
        time.sleep(self.t)

    def start(self):
        if self.IS_WINDOWS:
            file = input('file name: ')
            os.system(f'python {file}')

        if self.IS_LINUX:
            file = input('file name: ')
            os.system(f'python3 {file}')

        if self.IS_MAC:
            file = input('file name: ')
            os.system(f'python3 {file}')
