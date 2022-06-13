#this is a command for pi-shell.
import main

while True:
    try:
        main.run()
        main.run_all_functions()
        

        
    except KeyboardInterrupt:
        print("\n")
        break 