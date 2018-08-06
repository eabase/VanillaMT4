import clone
import portable
import os
import time

ASCII_ART = (
    ' __     __                     __  __  __                    __       __  ________  __    __ \n'
    '|  \   |  \                   |  \|  \|  \                  |  \     /  \|        \|  \  |  \\\n'
    '| $$   | $$ ______   _______   \$$| $$| $$  ______          | $$\   /  $$ \$$$$$$$$| $$  | $$\n'
    '| $$   | $$|      \ |       \ |  \| $$| $$ |      \  ______ | $$$\ /  $$$   | $$   | $$__| $$\n'
    ' \$$\ /  $$ \$$$$$$\| $$$$$$$\| $$| $$| $$  \$$$$$$\|      \| $$$$\  $$$$   | $$   | $$    $$\n'
    '  \$$\  $$ /      $$| $$  | $$| $$| $$| $$ /      $$ \$$$$$$| $$\$$ $$ $$   | $$    \$$$$$$$$\n'
    '   \$$ $$ |  $$$$$$$| $$  | $$| $$| $$| $$|  $$$$$$$        | $$ \$$$| $$   | $$         | $$\n'
    '    \$$$   \$$    $$| $$  | $$| $$| $$| $$ \$$    $$        | $$  \$ | $$   | $$         | $$\n'
    '     \$     \$$$$$$$ \$$   \$$ \$$ \$$ \$$  \$$$$$$$         \$$      \$$    \$$          \$$\n\n'
    '*********************************************************************************************\n' 
)

menu = {
    '1': {
        'desc': 'Clone and Symlink',
        'func': clone.clone,
    },
    '2': {
        'desc': 'Refresh Launch Shortcuts',
        'func': portable.refresh,
    },
}

def print_menu():
    for k,v in menu.items():
        print(f'{k}: {v["desc"]}')

def is_init():
    return not os.path.exists('MT4')

def unpack():
    print('Unzipping archive. please standby...')
    import zipfile
    zip_ref = zipfile.ZipFile('RUN_SETUP.zip', 'r')
    zip_ref.extractall(os.getcwd())
    zip_ref.close()
    time.sleep(5)
    if os.path.exists('MT4'):
        return True
    raise Exception('Error unpacking archive. Did you remove or rename it?')

def main():
    print(ASCII_ART)

    if is_init():
        if unpack():
            portable.main()
        input('Please wait for the terminal to load and then setup your accounts.\n'
            '\n........this may take a while during the initial launch.......Be patient.'
            '\nPress Enter to exit')
        exit()


    print_menu()
    action = None
    while 1:
        action = input('Please enter selection or press Enter to quit\n>')
        if action and action not in menu:
            print('Invalid option selected...')
        else:
            break
    if not action:
        exit('No actions were performed')
    print(f'Proceeding with <<{menu[action]["desc"]}>>')
    n = None
    if action == '1':
        if clone.is_admin():
            while 1:
                try:
                    n = int(input('Enter total sum of clone terminals for this directory.\n>'))
                    if not 0 < n < 100:
                        raise ValueError
                except ValueError:
                    print('Invalid selection')
                    continue
                break

    menu[action]['func'](n)
    
 

if __name__ == '__main__':
    main()