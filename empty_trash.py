import os
import sys
import subprocess

from utils.logger import log

# Defines the absolute path to the user's trash files.
trash_directory = os.path.expanduser('~/.local/share/Trash/files')
files = os.listdir(trash_directory)

if not files:
    log('INFO', 'The trash is empty!')
    sys.exit()

log('INFO', 'Deleting the following files:')
    
for file in files:
    print(file)

try:
    # The script uses `gio trash --empty` to tell the OS to empty the user's
    # trash safely.
    result = subprocess.run(
        ['gio', 'trash', '--empty'],capture_output = True,
        text = True, check = True
    )

    log('DONE', 'Trash deleted. Your digital life just got cleaner.')
except subprocess.CalledProcessError as error:
    log('ERROR', 'Execution error!')

    print('stdout: ', error.stdout)
    print('stderr: ', error.stderr)
    print('returncode: ', error.returncode)
    
