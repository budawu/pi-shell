#this is a command for pi-shell.
import main
#from colorama import Fore
print(
    '''
____   _   _____            _ _ 
|  _ \(_) / ___|| |__   ___| | |
| |_) | | \___ \| '_ \ / _ \ | |
|  __/| |  ___) | | | |  __/ | |
|_|   |_| |____/|_| |_|\___|_|_|
    '''
    'pi-shell 0.0.3'
    'type "exit" or "\\" to exit.'
)
while True:
    try:
        main.shell()
        main.run_all_functions()
        

        
    except KeyboardInterrupt:
        print("\n")
        break 