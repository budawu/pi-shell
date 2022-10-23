import os
import shlex

def shell(sym):
    '''read the command line'''
    try:
        try:
            code=shlex.split(sym)
            return code
        except ValueError:
            pass
    except EOFError:
        print('\n')

