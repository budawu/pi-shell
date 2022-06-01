import os
import main

while True:
    try:
        main.run()
        main.run_all_functions()
#        if main.run.tokens[0]  not in main.all_the_tokens:
#          print('Pysh: command not found')   
    except KeyboardInterrupt:
        print("\n")
        break