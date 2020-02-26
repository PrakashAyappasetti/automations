import os
from github import Github
token = os.environ.get('gt')        # add github token to the env vars

g = Github(token)
repo_name = input('enter the repoitory name >>> ')
try:
    repo = g.get_repo(full_name_or_id=f"{g.get_user().login}/{repo_name}")
    repo.delete()
except Exception as e:
    print(e)
