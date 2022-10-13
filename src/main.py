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
import settings
from colorama import Fore
PATH = os.getcwd()

class PiShell:
    def __init__(self,token:list,mode,running:bool) -> None:
        self.token = token
        self.mode = mode
        self.running = running

#        print(self.token)
        
    def exit_(self) -> None:
        try:
            if self.token[0] == 'exit':
                py = 'exit(0)'
                if self.running == True:
                    exec(py)
                return py
                
        except IndexError:
            pass
        except TypeError:
            pass
    def echo(self):
        '''print'''
        try:
            if self.token[0]=='echo':
               py = f'print({self.token[1]})'
               if self.running == True: 
                  exec(py)

               return  py
        except IndexError:
            pass
        except TypeError:
            pass
    
    def cd(self):
        '''change directory'''
        try:
            if self.token[0] == 'cd' :
                code=f'os.chdir(\'{self.token[1]}\')'
                if self.running == True:
                    exec(code)
                global PATH
                PATH = os.getcwd()
                
                return code
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
            if self.token[0] == '$':
                code = f'os.system(\'{self.token[1]}\')'
                if self.running == True:
                    exec(code)            
                if len(self.token) == 1:
                    print(f'{Fore.RED}No input{Fore.RESET}')
        except IndexError:
            pass

    def pyimport(self)-> None:
        try:
            if self.token[0][0]=='%':
                code = f'import {self.token[0][1:]}'
                if self.running==True:
                    exec(code)
                return code
        except IndexError:
            pass
    


    def run(self):
        self.echo()
        self.exit_()
        self.cd()
        self.shcommand()


if __name__== '__main__':
    print(settings.START)
  
    while True:
        try:
            pish = PiShell(shell(input(f'{settings.PATHCOLOR}{PATH}{Fore.RESET}'+f"{settings.PROMPTCOLOR} ~π{Fore.RESET} ")),'shell',running=True)
            pish.run()
        except KeyboardInterrupt:
            exit()




    