from win32com.client import Dispatch
import os
import subprocess
import shutil
import time

def create_launch_shortcut(directory, name='LAUNCH-MT4'):
    """
    Creates the shortcut neccessary to launch MT4 in portable mode
    """
    shortcut_locations = (
        directory, 
        os.path.join(os.environ["HOMEPATH"], "Desktop"),
    )
    name = f"{name}.lnk"
    target = os.path.join(directory, 'terminal.exe')

    for location in shortcut_locations:
        path = os.path.join(location, name)
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path) 
        shortcut.Targetpath = target
        shortcut.Arguments = '/portable'
        shortcut.WorkingDirectory = directory
        shortcut.IconLocation = target
        shortcut.save()
    # for _ in range(10):
    #     if os.path.isfile(name):
    #         shutil.copy(name, os.path.join(os.environ["HOMEPATH"], "Desktop"))
    #         break
    #     time.sleep(1)
    # else:
    #     print('Error copying shortcut to Desktop')
    

def launch_terminal(directory):
    """
    Launches the terminal for the first time in portable mode which will 
    automatically create the missing folders. 
    """
    program = os.path.join(directory, 'terminal.exe') + ' /portable'
    subprocess.Popen(program)

def main():
    directory = os.path.join(os.getcwd(), 'MT4')
    print('Creating portable shortcuts')
    create_launch_shortcut(directory)
    print('launching terminal for setup')
    launch_terminal(directory)
    input("Press Enter to exit")

if __name__ == '__main__':
    main()