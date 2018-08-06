# import admin
import portable

ART = (
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
        'desc': 'Install as portable and add shortcut to desktop',
        'func': portable.main,
    },
    '2': {
        'desc': 'Clone terminal and symlink MQL, History folders',
        'func': lambda: print('cloning'),
    },
}

def print_menu():
    for k,v in menu.items():
        print(f'{k}: {v["desc"]}')


def main():
    print(ART)
    print_menu()
    action = None
    while 1:
        action = input('Please enter selection or press Enter to quit >')
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