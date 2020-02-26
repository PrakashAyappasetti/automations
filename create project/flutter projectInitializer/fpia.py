import argparse
import os
from github import Github


def local():
    try:
        if os.path.exists(path):
            os.chdir(path)
        else:
            print('Cannot create a file when that file already exists')
            exit()
        os.system(f'flutter create {foldername}')
        os.chdir(_dir)
        os.system('git init')
        os.system(f'echo "# {foldername}" > README.md')
        os.system('git add README.md')
        os.system('git commit -m "first commit"')

        print(f'{foldername} created locally')
        os.system('code .')

    except Exception as e:
        print(e)


def remote():
    try:
        g = Github(token)
        user = g.get_user()
        login = user.login
        user.create_repo(foldername)
    except Exception as e:
        print(e)

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

    except Exception as e:
        print(e)


if __name__ == "__main__":

    UserProfile = os.environ.get('USERPROFILE')

    # add projects dirctory to the env vars
    path = f'{UserProfile}\\Desktop'
    token = os.environ.get('gt')            # add github token to the env vars

    p = argparse.ArgumentParser()
    p.add_argument('name', help='name of the project')
    p.add_argument('-f', default='r', help='name of the project')
    args = p.parse_args()

    foldername = args.name
    _dir = path + '\\' + foldername

    if args.f == 'l':
        local()
    elif args.f == 'r':
        remote()
    else:
        print('fpia --help for help')
