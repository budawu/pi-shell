#-*-coding:utf-8-*-
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
from init import *


PATH = os.getcwd()

VERSION = 'v0.2'
class PiShell:
    def __init__(self,token,mode) -> None:
        self.token = token
        self.mode = mode
#        print(self.token)
        
    def exit_(self) -> None:
        try:
            if self.token[0] == 'exit':
                exit(0)
        except IndexError:
            pass
        except TypeError:
            pass
    def echo(self):
        '''print'''
        try:
            if self.token[0]=='echo':
                print(self.token[1])
        except IndexError:
            pass
        except TypeError:
            pass
    
    def cd(self):
        '''change directory'''
        try:
            if self.token[0] == 'cd' :
                os.chdir(self.token[1])
                global PATH
                PATH = os.getcwd()
            if len(self.token)>2:
                print(f'{Fore.RED}cd:too many arguments{Fore.RESET}')
        
        except IndexError:
            pass
        except FileNotFoundError as e:
            print(f'{Fore.RED}cd: {e}{Fore.RESET}')
    
    def operation(self):
        '''operations'''
        exp = eval(str(self.token))
        if self.mode == 'script':
            return exp 
        if self.mode == 'shell':
            print(exp)
            return exp

    def shcommand(self):
        '''
        run shell for system command,
        if the OS is Windows,it will be CMD,if
        the OS is Linux,it will be $SHELL(usually bash or zsh)
        '''
        try:
            if self.token[0] == 'run$':
                os.system(self.token[1])
                if len(self.token) == 1:
                    print(f'{Fore.RED}No input{Fore.RESET}')
        except IndexError:
            pass

    def python(self):
        '''run python code'''
        try:
            if self.token[0]== 'py':
                exec(self.token[1:])
        except IndexError:
            pass

    def run(self):
        self.echo()
        self.exit_()
        self.cd()
        self.shcommand()
        self.python()

if __name__== '__main__':
    print(
    '''
____   _   _____            _ _ 
|  _ \(_) / ___|| |__   ___| | |
| |_) | | \___ \| '_ \ / _ \ | |
|  __/| |  ___) | | | |  __/ | |
|_|   |_| |____/|_| |_|\___|_|_|
    '''
f'Pi-shell {VERSION}\n'
 'Type "exit" or Ctrl+C to exit.'
)  
    while True:
        try:
            pish = PiShell(shell(input(f'{Fore.YELLOW}{PATH}{Fore.RESET}'+f"{Fore.BLUE} ~π{Fore.RESET} ")),'shell')
            pish.run()
        except KeyboardInterrupt:
            exit()




    