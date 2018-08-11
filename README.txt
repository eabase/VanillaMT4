Vanilla MT4 - build 1126

Forum thread https://www.forexfactory.com/showthread.php?t=803172

This is NOT affiliated with MetaQuotes. 

This is NOT a MT4 replacement/modification. 

The MT4 terminal and metaeditor have not been tampered with. You can (and should) check the MD5 sum against your current installations. 

This is a script to assist with:
    1. Create the appropriate launch shortcuts to run MT4 in "portable" mode
    2. Clone the main MT4 terminal for muliple terminal instances
        A. Symlink the clones
            1. Save space with one combined History file
            2. Keep ALL Expert Advisors, Indicators, and Scripts synced (all terminals use same folder)
            3. Keep templates synced (again same folder)

Operations:
    Initial Setup:
        1. Save this folder in an appropriate directory. Note: This directory can be changed after install, but if it is then you will need to run the setup again to update the Launch short-cuts.
        2. Run MT-Tools.exe and wait for the script to extract the files, create the launchers, and run the terminal for the first time. 
        3. Login to all current broker trading accounts. 
        4. Close terminal. 
        5. Replace the MQL4 folder with an existing MQL4 directory with your existing MQL programs.

    Cloning:
        1. Run MT-Tools.exe and select the option to clone the MT4 directory.
        2. When prompted enter the total SUM of the clones that you want in the directory. 

    Relocating entire MT4 directory and all clones to a different location/computer/VPS:
        1. Copy the parent directory and all of its contents to the target location
        2. Run the setup.exe program and select the option to Refresh Launch Shortcuts


!!! IMPORANT !!!
DO NOT RENAME THE DIRECTORIES