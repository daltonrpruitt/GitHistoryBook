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
    
def interact_with_github(token):
    
    # using an access token
    g = Github(token)

    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        print(repo.name)


def main():
    token = get_token()
    interact_with_github(token)
    


if __name__=="__main__":
    main()
