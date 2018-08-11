import os
import time
import shutil
from win32com.client import Dispatch
import win32file

# locals
try:
    from setup_tools import elevate, portable
except:
    import elevate, portable

files_copy  = ['metaeditor.exe', 'terminal.exe', 'terminal.ico' ]
dirs_copy   = ['logs', 'config', 'profiles', 'tester', ]
dirs_sym    = ['MQL4', 'history', 'templates', 'Sounds']


def is_admin():
    return elevate.is_admin()


def is_mt4_dir(directory):
    """Returns true if the folder is a MT dir"""
    # print(os.listdir(directory))
    return 'terminal.exe' in os.listdir(directory)


def create_symlinked_clone(target, n):
    """
    Clones the target
    TODO: make this copy terminals, etc. and symlink
    MQL, history, config
    """
    cwd = os.getcwd()
    new_dir = f'{target}-CLONE-{n}'

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        time.sleep(1)

    # symlink directories
    for sym in dirs_sym:
        new_path = os.path.join(cwd, new_dir, sym)
        target_path = os.path.join(cwd, target, sym)
        symlink(new_path, target_path)
        time.sleep(0.5)
    # copy files
    for f in files_copy:
        shutil.copy(
            os.path.join(cwd, target, f),
            os.path.join(cwd, new_dir, f))
    # copy dirs
    for f in dirs_copy:
        shutil.copytree(
            os.path.join(cwd, target, f),
            os.path.join(cwd, new_dir, f))

    portable.create_launch_shortcut(
        directory=os.path.join(cwd, new_dir),
        name=f'LAUNCH-{new_dir}')


def symlink(new_path, target_path):
    win32file.CreateSymbolicLink(new_path, target_path, 1)


def fix_symlinks():
    try:
        cwd = os.getcwd()
        mt_dirs = [i for i in os.listdir(cwd) if os.path.isdir(i) and is_mt4_dir(i)]
        for d in mt_dirs:
            for folder in dirs_sym:
                symlink(
                    os.path.join(cwd, d, folder),
                    os.path.join(cwd, 'MT4', folder),
                )
    except:
        pass


def clone(*args):
    
    if is_mt4_dir(os.getcwd()) or not is_mt4_dir(os.path.join(os.getcwd(), 'MT4')):
        raise Exception('Run from parent dir.')
    n = None
    while 1:
        try:
            n = int(
                input('Enter total sum of clone terminals for this directory.\n>'))
            if not 0 < n < 100:
                raise ValueError
        except ValueError:
            print('Invalid selection')
            continue
        break
    master_src = None
    clones = []
    dirs = list(
        d for d in os.listdir() 
            if os.path.isdir(d) and not d.startswith('.') and not d.startswith('__')
    )
    print(dirs)
    for f in dirs:
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
