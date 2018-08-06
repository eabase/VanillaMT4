import os
import re
from win32com.client import Dispatch
import win32file
import elevate
import time
import shutil

files_copy = ['metaeditor.exe', 'terminal.exe',]
dirs_copy  = ['Sounds', 'logs', 'config', 'profiles', 'tester',]
dirs_sym   = ['MQL4', 'history', 'templates',]

def is_mt4_dir(directory):
    """Returns true if the folder is a MT dir"""
    print(os.listdir(directory))
    return 'terminal.exe' in os.listdir(directory)

def create_symlinked_clone(target, n):
    """
    Clones the target
    TODO: make this copy terminals, etc. and symlink
    MQL, history, config
    """
    cwd = os.getcwd()
    # to_copy = ['metaeditor.exe', 'terminal.exe', 'terminal.ico', 'tester']
    # to_symlink = ['']
    new_dir = f'{target}-CLONE-{n}'
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        time.sleep(1)
    
    #symlink directories
    for sym in dirs_sym:
        new_path = os.path.join(cwd, new_dir, sym)
        target_path = os.path.join(cwd, target, sym)
        input(f'debug target path is {target_path}')
        win32file.CreateSymbolicLink(new_path, target_path, 1)
        time.sleep(0.5)

    #copy files
    for f in files_copy:
        shutil.copy(
            os.path.join(cwd, target, f),
            os.path.join(cwd, new_dir, f))
    #copy dirs
    input('copy dirs')
    for f in dirs_copy:
        shutil.copytree(
            os.path.join(cwd, target, f),
            os.path.join(cwd, new_dir, f))

    # new_dir = os.path.join(os.getcwd(), new_dir)
    if os.path.exists(new_dir):
        for file in os.listdir(new_dir):
            if file.endswith('.lnk'):
                os.remove(os.path.join(new_dir, file))


def clone(n):
    if not elevate.is_admin():
        elevate.elevate_privilege()
        return None
    input('waiting at elevated prompt')
    if is_mt4_dir(os.getcwd()) or not is_mt4_dir(os.path.join(os.getcwd(), 'MT4')):
        raise Exception('Run from parent dir.')
    master_src = None
    clones = []
    dirs = list(d for d in os.listdir() if os.path.isdir(d) and not d.startswith('.') and not d.startswith('__'))
    print(dirs)
    for f in dirs:
        print(f)
        directory: str = f
        if is_mt4_dir(directory):
            if master_src is None and 'clone' not in directory.casefold():
                master_src = directory
            elif 'clone' in directory.casefold():
                clones.append(directory)
    if master_src is None:
        raise Exception('Master MT4 directory not found.')

    for i in range(len(clones) + 1, n + 1):
        create_symlinked_clone(master_src, i)

clone(1)