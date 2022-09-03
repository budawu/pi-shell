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
f'Pi-shell {main.version}'
'Type "exit" or Ctrl+C to exit.'
)
while True:
    try:
        main.shell()
        main.run_all_functions()
        

        
    except KeyboardInterrupt:
        print("\n")
        break 