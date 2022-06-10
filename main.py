import os
import shlex

from colorama import Fore


all_the_tokens=['echo','exit','cd',]
PATH=os.getcwd()

def run():
    sym=input(f"{Fore.BLUE}{PATH} ∞{Fore.RESET} ")
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
            os.chdir(tokens[1])
            PATH=os.getcwd()
        if len(tokens) >= 3:
            print(Fore.RED+'cd: too many arguments'+Fore.RESET)
    except IndexError:
        pass

def run_all_functions():
    '''run all the functions'''
    try:
        if tokens[0] not in all_the_tokens:
            print(Fore.RED+'ish: command not found'+Fore.RESET)
    except IndexError:
        pass
    echo()
    exit_()
    cd()
