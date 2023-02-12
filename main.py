from github import Github

from os.path import expanduser
import sys, logging

def setup_logger():
    _logger = logging.getLogger(__name__)
    hdlr = logging.StreamHandler()
    fhdlr = logging.FileHandler("myapp.log")
    _logger.addHandler(hdlr)
    _logger.addHandler(fhdlr)
    _logger.setLevel(logging.DEBUG)
    return _logger



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
    
    logger = setup_logger()
    
    token = get_token()
    gh = Github(token)
    repo = gh.get_repo(gh.get_user().login+"/"+sys.argv[1])
    
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
    
    if logger.isEnabledFor(logging.DEBUG):
        messages_str = "="*25+"  Commit Messages   " + "="*25 + "\n"
        for c in path_to_current_end[::-1]:
            messages_str +=  c.message + "\n"
            messages_str +=  "-"*10 + "\n"
        messages_str += "="*70 + "\n"
        logger.debug("%s",messages_str)


if __name__=="__main__":
    main()
