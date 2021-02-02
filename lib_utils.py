#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import os

class Banner:

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.banner = os.path.join(self.base_dir, 'banner.txt')

    def get_banner(self):
        clear()
        with open(self.banner, 'r') as banner:
            return '\033[35m' + banner.read()

def clear():
    os.system('clear')
        