import subprocess

while True:
    command = input('> ')
    
    if command == 'ai':
        print('The AI is at your command')

    elif command == 'exit':
        print('Exiting terminal...')
        break

    else:
        subprocess.run(command, shell=True)