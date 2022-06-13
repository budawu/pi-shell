#-*-coding:utf-8-*-
#This shell is by @budawu in 2022.
#Latest update: 2022.6.12
'''
CAUTION:

Remember to add the new function to the all_the_tokens list
and to the run_all_functions function
Remember  to explain the new function to the user
Remember to except the IndexError
Remember to use f-strings for syntax highlighting
e.g. print(f'{Fore.RED}cd: command not found{Fore.RESET}')
'''
import os
import shlex

from colorama import Fore,init

all_the_tokens=['echo','exit','cd','run$',]
PATH=os.getcwd()
init()
def run():
    sym=input(f"{PATH} {Fore.BLUE}π{Fore.RESET} ")
    global tokens
    tokens=shlex.split(sym)

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
            print(f'{Fore.RED}cd: too many arguments{Fore.RESET}')
    except IndexError:
        pass
    except FileNotFoundError as e:
        print(f'{Fore.RED}cd: {e}{Fore.RESET}')

def add():
    '''+'''
    
    try:
        nums=tokens[0].split('+')
        if len(nums)==1:
            '''when this,it's not a number,and it will be a error'''
            pass
        else:
            addends=[]
            for num in nums:
                num=int(num)
                addends.append(num)

            print(sum(addends))

    except IndexError:
        pass

def shcommand():
    '''run shell'''
    try:
        if tokens[0]=='run$':
            os.system(tokens[1])
    except IndexError:
        pass

def define():
    '''define vars'''
    try:
        if tokens[0]=='var':
            if len(tokens)==2:
                print(f'{Fore.RED}define: missing argument{Fore.RESET}')
    except IndexError:
        pass


def run_all_functions():
    '''run all the functions'''
    try:
        
        if tokens[0] not in all_the_tokens:
            print(f'{Fore.RED}ish: command not found{Fore.RESET}')
    except IndexError:
        pass
    echo()
    exit_()
    cd()
    add()
    shcommand()
