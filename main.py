#-*-coding:utf-8-*-
#This shell is written by @budawu in 2022.
#Latest update: 2022.8.28
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
import re

from colorama import Fore,init

version='0.0.4'
all_the_tokens=['echo','exit','cd','run$','var','runpy']
definevars={
    'PATH':os.getcwd(),
}
PATH=os.getcwd()
init()
def shell():
    '''initialize the shell'''
    sym=input(f'{Fore.YELLOW}{PATH}{Fore.RESET}'+f"{Fore.BLUE} ~π{Fore.RESET} ")
    global tokens
    try:
        tokens=shlex.split(sym)
    except ValueError:
        pass

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
    except ValueError:
        pass
        
    except FileNotFoundError as e:
        print(f'{Fore.RED}cd: {e}{Fore.RESET}')


#def add():
#    '''+'''
    
#    try:
#        nums=tokens[0].split('+')
#        if len(nums)==1:
#            '''when this,it's not a number,and it will be a error'''
#            pass
#        else:
#            addends=[]
#            for num in nums:
#                num=int(num)
#                addends.append(num)

#         print(sum(addends))

#    except IndexError:
#        pass

def operation(expression):
    '''operations'''
    ans=eval(expression)
    
    return ans


        


def shcommand():
    '''
    run shell for system command,if the OS is Windows,it will be CMD,if
    the OS is Linux,it will be $SHELL(usually bash or zsh)
    '''

    try:
        if tokens[0]=='$':
            os.system(tokens[1])
    except IndexError:
        pass

def define():
    '''define vars'''
    try:
        if tokens[0]=='var':
            if len(tokens)==2:
                definevars[tokens[1]]=None
                print(definevars)
            elif len(tokens)==3:
                definevars[tokens[1]]=tokens[2]
                print(definevars)
    except IndexError:
        pass

class Var:
    def __init__(self,name,value,type):
        self.name=name
        self.value=value
        self.type=type
    
    
        
    def type_expression(self):
        '''expressions'''
        mo=re.compile(r'[$]\+-\*/\d')
        self.search(mo)

        

        

def using_var():
    '''using var'''
    try:
        if tokens[0][0]=='$':
            if tokens[0][1:] in definevars:
                print(definevars[tokens[0][1:]])
            else:
                print(f'{Fore.RED}{tokens[0]}: variable not found{Fore.RESET}')
    except IndexError:
        pass

def run_python():
    '''call Python code'''
    try:
        if tokens[0]=='runpy':
            try:
                exec(tokens[1])
            except IndexError:
                pass
        
            except Exception as e:
                print(f'{Fore.RED}{e}{Fore.RESET}')
    except IndexError:
        pass
        

def run_all_functions():
    '''run all the functions'''
    try:
        
        if tokens[0] not in all_the_tokens:
            print(f'{Fore.RED}{tokens[0]}: command not found{Fore.RESET}')
    except IndexError:
        pass
    except ValueError:
        pass
    echo()
    exit_()
    cd()

    shcommand()
    define()
    using_var()
    run_python()

