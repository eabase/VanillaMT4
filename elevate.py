import win32api
import win32con
import win32event
import win32process
from win32com.shell.shell import ShellExecuteEx
from win32com.shell import shellcon
import sys
import os
import traceback
import types
import ctypes


def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()


def elevate_privilege(cmd_line_seq: list=None, wait: bool=True):
    python_exe = sys.executable
    if cmd_line_seq is None:
        cmd_line_seq = [python_exe] + sys.argv
    elif not isinstance(cmd_line_seq, (list, tuple,)):
        raise ValueError
    script_to_run = f'"{cmd_line_seq[0]}"'
    params = " ".join(f'"{x}"' for x in cmd_line_seq[1:])
    # input(f'file = {script_to_run}\nparams = {params}\nEnter to continue...')
    procInfo = ShellExecuteEx(
        nShow=win32con.SW_SHOWNORMAL,
        fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
        lpVerb='runas',
        lpFile=script_to_run,
        lpParameters=params
    )
    if wait:
        procHandle = procInfo['hProcess']
        _ = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        return_code = win32process.GetExitCodeProcess(procHandle)
        print("Process handle {} returned code {}".format(procHandle, return_code))
    else:
        return_code = None
    return return_code


def main():
    return_code = 0
    if not is_admin():
        return_code = elevate_privilege()
    else:
        return_code = 0
        input('Press Enter to exit.')
    return return_code


if __name__ == "__main__":
    sys.exit(main())
