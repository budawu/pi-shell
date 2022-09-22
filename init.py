import os
import shlex
from colorama import Fore
def shell(sym):
    '''read the command line'''
    try:
        try:
            argstr=shlex.split(sym)
            return argstr
        except ValueError:
            pass
    except EOFError:
        print('\n')