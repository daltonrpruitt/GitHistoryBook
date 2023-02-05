from github import Github

from os.path import expanduser
import sys

def get_token():
    home = expanduser("~")

    # First create a Github instance:

    try:
        token = open(home+"/.github/my_gh_token.txt").read()
        return token
    except FileNotFoundError as e:
        print("Cannot find token file! :", e)
        raise e
    

def get_repos(gh): return [repo for repo in gh.get_user().get_repos()]


def get_repo_by_name(gh, repo_name):
    repos = get_repos(gh)
    for r in repos:
        if repo_name in r.name:
            return r
    raise Exception("Could not find repo named '"+repo_name+"'!")


def main():
    assert(len(sys.argv) == 2)
    token = get_token()
    gh = Github(token)
    repo = get_repo_by_name(gh, sys.argv[1])
    print(repo)


if __name__=="__main__":
    main()
