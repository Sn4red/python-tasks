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

log('INFO', 'Trash contains these documents:')

for file in files:
    print(file)

