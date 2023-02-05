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


def main():
    assert(len(sys.argv) == 2)
    token = get_token()
    gh = Github(token)
    repo = gh.get_repo(gh.get_user().login+"/"+sys.argv[1])
    print("Branches of ", repo.name)
    main_branch = None
    for b in repo.get_branches():
        if b.name == "main" or b.name == "master":
            main_branch = b
    if main_branch is None:
        raise Exception("Could not find a 'main' or 'master' branch!")
    path_to_current_end = []
    curr_commit = main_branch.commit.commit
    while True:
        path_to_current_end.append(curr_commit)
        if len(curr_commit.parents) == 0:
            break
        curr_commit = curr_commit.parents[0]
    print("="*70 + "\nMessages:")
    for c in path_to_current_end[::-1]:
        print(c.message)
        print("-"*10)
    print("="*70)


if __name__=="__main__":
    main()
