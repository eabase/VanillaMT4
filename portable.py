from win32com.client import Dispatch
import os
import subprocess
import shutil
import time
import clone

def create_launch_shortcut(directory: str, name='LAUNCH-MT4'):
    """
    Creates the shortcut neccessary to launch MT4 in portable mode
    """
    if 'clone' not in directory.casefold():
        shortcut_locations = (
            directory, 
            os.path.join(os.environ["HOMEPATH"], "Desktop"),)
    else:
        shortcut_locations = (directory,)

    name = f"{name}.lnk"
    target = os.path.join(directory, 'terminal.exe')

    for location in shortcut_locations:
        print(f'creating shortcut for {location}')
        path = os.path.join(location, name)
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path) 
        shortcut.Targetpath = target
        shortcut.Arguments = '/portable'
        shortcut.WorkingDirectory = directory
        shortcut.IconLocation = target
        shortcut.save()

def refresh(*args):
    print('refresh!')
    cwd = os.getcwd()
    dirs = [os.path.join(cwd, a) for a in os.listdir(cwd) if os.path.isdir(a) and clone.is_mt4_dir(a)]
    def lnk_file(d):
        for f in os.listdir(d):
            if f.endswith('.lnk'):
                return f
        return None
    for d in dirs:
        create_launch_shortcut(d, lnk_file(d))


def launch_terminal(directory):
    """
    Launches the terminal for the first time in portable mode which will 
    automatically create the missing folders. 
    """
    program = os.path.join(directory, 'terminal.exe') + ' /portable'
    subprocess.Popen(program)

def main(*args):
    directory = os.path.join(os.getcwd(), 'MT4')
    print('Creating portable shortcuts')
    create_launch_shortcut(directory)
    print('launching terminal for setup')
    launch_terminal(directory)
    

if __name__ == '__main__':
    # main()
    refresh()