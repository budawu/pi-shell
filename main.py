import os
#import funcbase

all_the_tokens=['echo','exit','',]


def run():
    PATH=os.getcwd()
    sym=input(f"{PATH} -Pysh◆")
    global tokens
    tokens=sym.split()

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

def run_all_functions():
    '''run all the functions'''
    try:
        if tokens[0] not in all_the_tokens:
            print('Pysh: command not found')
    except IndexError:
        pass
    echo()
    exit_()