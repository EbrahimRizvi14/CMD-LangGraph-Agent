import subprocess
import os

current_cwd = os.getcwd()

while True:

    command = input(f'{current_cwd} > ')
    
    if command == 'exit':
        print('Exiting terminal...')
        break

    elif len(command) == 2 and command[1] == ':':
            if os.path.exists(command + '\\'):
                current_cwd = command + '\\'
    
    
    elif command.startswith('ai '):
        prompt = command[3:].strip()
        print(f'AI Prompt: {prompt}')
        

    elif command.startswith('cd '):
        
        if len(command) <= 3:
            print('Error: No target directory specified.')
            continue

        target = command[3:].strip()

        new_cwd = os.path.abspath(os.path.join(current_cwd, target))

        if os.path.isdir(new_cwd):
            current_cwd = new_cwd
        else:
            print(f'Error: Directory "{target}" does not exist.')

    else:
        subprocess.run(command, shell=True, cwd=current_cwd)