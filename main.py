from github import Github, Commit

import os, re
import sys, logging
# from datetime import datetime
from typing import List

logger = None  # not passing the logger around


def setup_logger():
    global logger
    logger = logging.getLogger(__name__)
    hdlr = logging.StreamHandler()
    fhdlr = logging.FileHandler("myapp.log")
    logger.addHandler(hdlr)
    logger.addHandler(fhdlr)
    logger.setLevel(logging.DEBUG)


def get_token():
    home = os.path.expanduser("~")
    try:
        token = open(home + "/.github/my_gh_token.txt").read()
        return token
    except FileNotFoundError as e:
        print("Cannot find token file! :", e)
        raise e


def get_repos(gh):
    return [repo for repo in gh.get_user().get_repos()]


def get_chronological_commits(repo):
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
    path_to_current_end.reverse()

    if logger.isEnabledFor(logging.DEBUG):
        messages_str = "=" * 25 + "  Commit Messages   " + "=" * 25 + "\n"
        for c in path_to_current_end[::-1]:
            messages_str += c.message + "\n"
            messages_str += "-" * 10 + "\n"
        messages_str += "=" * 70 + "\n"
        logger.debug("%s", messages_str)

    return path_to_current_end


def commits_to_latex_str(commits: List[Commit.Commit]):
    latex_string = r"\documentclass{article}"+ "\n\n"
    latex_string += r"\usepackage[margin=0.5in]{geometry}" + "\n\n"

    # latex_string += r"\usepackage{titlesec}" + "\n\n"
    # latex_string += r"\titleformat{\section}  % which section command to format" + "\n"
    # latex_string += r"   {\fontsize{14}{16}\bfseries} % format for whole line" + "\n"
    # latex_string += r"   {} % how to show number" + "\n"
    # latex_string += r"   {1em} % space between number and text" + "\n"
    # latex_string += r"   {} % formatting for just the text" + "\n"
    # latex_string += r"   [] % formatting for after the text" + "\n\n"
    
    latex_string += r"\begin{document}"
    latex_string += "\n\n"

    for commit in commits:
        full_message = re.sub(r"_", r"\_", commit.message)
        full_message = re.sub(r"`", r"'", full_message)
        header, body = None, None
        try:
            header, body = full_message.split("\n\n")
        except ValueError:
            header = full_message

        logger.debug("header='%s'", header)
        logger.debug("body='%s'", body) if body is not None else logger.debug("<No body>") 
        
        # commit_message = re.sub(r"\n", r"\\", commit_message)
        commit_date_time = commit.committer.date.strftime("%Y-%m-%d %H:%M:%S")
        logger.debug("commit_date_time='%s'", commit_date_time)

        latex_string += r"\textbf{" + commit_date_time+": "+header+"}\n\n" 
        if body is not None: latex_string += f"{body}\n\n"
        latex_string += r"\vspace{0.5cm}" + "\n\n"
        
    latex_string += r"\end{document}\n"
    return latex_string


def main():
    assert len(sys.argv) == 2

    setup_logger()

    token = get_token()
    gh = Github(token)
    repo = gh.get_repo(gh.get_user().login + "/" + sys.argv[1])

    commits = get_chronological_commits(repo)
    
    latex_string = commits_to_latex_str(commits)
    open(f"{repo.name}.tex", "w").write(latex_string)
    os.system(f"pdflatex.exe {repo.name}.tex")
    os.startfile(f"{repo.name}.pdf")

if __name__ == "__main__":
    main()
