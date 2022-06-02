import sys
import os
import shlex


all_the_tokens=['echo','exit','cd',]
PATH=os.getcwd()

def run():
    sym=input(f"{PATH} -Pysh◆")
    global tokens
    tokens=shlex.split(sym)

def addfunc(token,runfunc):
    if tokens[0]==token:
        token.append(all_the_tokens)
        runfunc()
def echo():
    try:
        if tokens[0]=='echo':
            print(tokens[1])
    except IndexError:
        pass

def exit_():
    try:
        if tokens[0]=='exit':
            print('\n')
            exit()
    except IndexError:
        pass
def cd():
    try:
        if tokens[0]=='cd':
            global PATH
            PATH=sys.path.append(tokens[1])
        if len(tokens) >= 3:
            print('cd: too many arguments')
    except IndexError:
        pass

def run_all_functions():
    '''run all the functions'''
    try:
        if tokens[0] not in all_the_tokens:
            print('Pysh: command not found')
    except IndexError:
        pass
    echo()
    exit_()
    cd()
