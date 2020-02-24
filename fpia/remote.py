import sys
import os
from github import Github

foldername = str(sys.argv[1])
path = os.environ.get('mp')         # add projects dirctory to the env vars
token = os.environ.get('gt')        # add github token to the env vars
_dir = path + '/' + foldername

try:
    g = Github(token)
    user = g.get_user()
    login = user.login
    repo = user.create_repo(foldername)
except:
    print("something wrong on github api access side")

commands = ['git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

try:
    os.chdir(path)
    os.system(f'flutter create {foldername}')
    os.chdir(_dir)
    for c in commands:
        os.system(c)

    print(f'{foldername} initialized')
    os.system('code .')

except:
    print("create <foldername>")
