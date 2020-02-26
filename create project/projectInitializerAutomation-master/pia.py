import click
import sys
import os
from github import Github


@click.command()
@click.option('--name', prompt='name', help='project name')

def main(name):
    """------------"""
    click.echo(name)
    click.echo(name)
    

def local(name):
    foldername = name
    path = os.environ.get('mp')
    _dir = path + '/' + foldername

    try:
        os.mkdir(_dir)
        os.chdir(_dir)
        os.system('git init')
        os.system(f'echo "# {foldername}" > README.md')
        os.system('git add README.md')
        os.system('git commit -m "first commit"')

        print(f'{foldername} created locally')
        os.system('code .')

    except Exception as e:
        print("errot" , e)


def remote(name):
    foldername = name
    path = os.environ.get('mp')         # add projects dirctory to the env vars
    token = os.environ.get('gt')        # add github token to the env vars
    _dir = path + '/' + foldername

    g = Github(token)
    user = g.get_user()
    login = user.login
    repo = user.create_repo(foldername)

    commands = [f'echo # {repo.name} >> README.md',
                'git init',
                f'git remote add origin https://github.com/{login}/{foldername}.git',
                'git add .',
                'git commit -m "Initial commit"',
                'git push -u origin master']

    try:
        os.mkdir(_dir)
        os.chdir(_dir)

        for c in commands:
            os.system(c)

        print(f'{foldername} created locally')
        os.system('code .')

    except Exception as e:
        print("errot" , e)


if __name__ == "__main__":
    main('')
 