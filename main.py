from github import Github

from os.path import expanduser

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

def interact_with_github(token):
    
    # using an access token
    gh = Github(token)

    # Then play with your Github objects:
    repos = get_repos(gh)
    [print(i,r.name) for (i,r) in enumerate(repos)]

def main():
    token = get_token()
    interact_with_github(token)
    


if __name__=="__main__":
    main()
