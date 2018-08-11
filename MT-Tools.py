import os
import time
import sys
from setup_tools import clone, portable

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

def launchall():
    cwd = os.getcwd()
    for f in os.listdir(cwd):
        if os.path.isdir(f) and clone.is_mt4_dir(f):
            portable.launch_terminal(os.path.join(cwd, f))

menu = {
    '1': {
        'desc': 'Launch all terminals in this directory. (Release the clones!)',
        'func': launchall,
    },
    '2': {
        'desc': 'Clone and Symlink (Elevates to Admin)',
        'func': clone.clone,
    },
    '3': {
        'desc': 'Repair Launch Shortcuts / Symlinks',
        'func': portable.refresh,
    },
}


def print_menu():
    for k, v in menu.items():
        print(f'{k}: {v["desc"]}')


def is_init():
    return not os.path.exists('MT4')


def unpack():
    print('Unzipping archive. please standby...')
    import zipfile
    zip_ref = zipfile.ZipFile(os.path.join('files', 'RUN_SETUP.zip'), 'r')
    zip_ref.extractall(os.getcwd())
    zip_ref.close()
    time.sleep(5)
    if os.path.exists('MT4'):
        return True
    raise Exception('Error unpacking archive. Did you remove or rename it?')

def setup_update():
    if is_init():
        if unpack():
            portable.main()
        input('\nPlease wait for the terminal to load and then setup your accounts.'
              '\n...this may take a while during the initial launch. Wait for it.'
              '\nPress Enter to exit')
        exit()

def main():
    args = sys.argv[1:]
    if '--launchall' in args:
        launchall()
        exit('Launching all terminals...')

    print(ASCII_ART)
    setup_update()
    print_menu()

    action = None
    while True:
        action = input('Please enter selection or press Enter to quit\n>')
        if action and action not in menu:
            print('Invalid option selected...')
        else:
            break

    if not action:
        exit('No actions were performed')
    print(f'Proceeding with <<{menu[action]["desc"]}>>')

    menu[action]['func']()


if __name__ == '__main__':
    main()
