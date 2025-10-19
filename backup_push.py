import sys

from git import Repo
from utils.logger import log
from datetime import datetime, timedelta

repository = Repo('/home/sn4red/.emacs.d/sn4red-org-roam-vault')

modified_files = [item.a_path for item in repository.index.diff(None)]
mdr_files = [
    item.a_path
    for item in repository.index.diff(None)
    if item.change_type == 'D'
]
new_files = repository.untracked_files

if any([modified_files, mdr_files, new_files]):
    for index, file in enumerate(modified_files):
        if index == 0:
            log('INFO', 'Modified Files:')
        print(file)

    for index, file in enumerate(mdr_files):
        if index == 0:
            log('INFO', 'Moved/Deleted/Renamed files:')
        print(file)

    for index, file in enumerate(new_files):
        if index == 0:
            log('INFO', 'New Files:')
        print(file)

    while True:
        log('CONFIRMATION', 'Push to remote?')
        confirmation = input('(y/n):').strip().lower()

        if confirmation in ('y', 'n'):
            break

        log('WARNING', 'Please, confirm with y/n.')

    if confirmation == 'y':
        repository.git.add(all = True)

        last_commit_message = repository.head.commit.message
        last_commit_splitted = last_commit_message.split()
        last_commit_number = int(last_commit_splitted[-2])
        last_commit_date = last_commit_splitted[-1]

        # `date()` is used to remove the time component.
        # The resulting object is a `date`, not a formatted string, so it will
        # be formatted below when needed.
        current_date = datetime.now().date()
        previous_date = datetime.strptime(last_commit_date, "%m-%d-%Y").date()

        if current_date == previous_date:
            commit_message = (
                f'Backup {last_commit_number + 1} {last_commit_date}'
            )
        else:
            next_day = previous_date + timedelta(days = 1)
            reformatted_next_day = next_day.strftime("%m-%d-%Y")
            
            commit_message = (
                f'Backup 1 {reformatted_next_day}'
            )

        repository.index.commit(commit_message)
        repository.git.push()
                    
        log('DONE', 'Synced repository with remote.')
    if confirmation == 'n':
        sys.exit()
else:
    log('INFO', 'Nothing to commit. Working tree clean.')
