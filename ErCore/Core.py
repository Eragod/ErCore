import os
import sys
import time
import random


class ECore:
    def __init__(self,
                 pre_functions: bool = False):
        self.pre_functions = pre_functions

    def info(self):
        if self.pre_functions is True:
            with open('VERSION', 'r') as version:
                print(f'Version: {version.read()}')

        print("Autor: Eragod\nProject: ErCore")
