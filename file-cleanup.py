import os
import time
import sys

os.chdir(os.environ['HOME'] + '/Downloads')
it = os.scandir()

targets = list()
for entry in it:
    if not entry.name.startswith('.') and entry.is_file():
        stat = entry.stat()
        if stat.st_mtime < time.time() - 60*60*24:
            targets.append(entry)

if len(targets) == 0:
    sys.exit()

print('these files are older than 1 day:\n')
for target in targets:
    stat = target.stat()
    print('{} {:.2}MB'.format(target.name, stat.st_size / 1024 / 1024))

confirm = ''
while confirm != 'y' and confirm != 'n':
    confirm = input('\ndelete? (y/n)\n')

if confirm == 'y':
    for target in targets:
        os.remove(target.name)
        print('{} removed.'.format(target.name))

