import sys

from git import Repo, exc
from utils.logger import log
from datetime import datetime, timedelta

try:
    repository = Repo('/home/sn4red/Documents/Projects/testing')

    old_commit = repository.head.commit.hexsha
    origin = repository.remote(name = 'origin')
    origin.pull()
    new_commit = repository.head.commit.hexsha

    if old_commit == new_commit:
        log('DONE', 'Repository is already up to date.')
    else:
        log('DONE', 'Repository synced with remote.')
    
except exc.InvalidGitRepositoryError:
    log('ERROR', 'There is no Git repository in this location!')
    sys.exit()
except exc.NoSuchPathError:
    log('ERROR', 'The path provided does not exist!')
    sys.exit()
except exc.GitCommandError as error:
    log('ERROR', 'Git operation failed.')

    print(f'Command: {error.command}')
    print(f'Status: {error.status}')
    print(f'Error message: {error.stderr}')

