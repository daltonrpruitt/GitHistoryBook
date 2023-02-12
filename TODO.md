# Base Use Case
- assumes user GitHub token in stored in `~/.github/my_gh_token.txt`
1. User gives script the full name of a repo on command line
2. Script pulls down the commits for that repo
3. Script formats the commits into a latex document and renders the PDF from that document (maybe HTML, too?)

# Starting out
- [x] get access to GitHub
- [x] get list of commits
- [ ] Organize commits into hierarchy for latex output
  - Repo is Article title
    - branch name is section title - may not be relevant anymore?
      - commit first line is subheading?? 
      - commit remaining message is paragraph
  - This seems very irrelevant given the fact I am only doing one branch now...
- [x] Put commit message contents into latex
- [x] Render the output latex into PDF
- [x] open PDF (in default app)


# Nice-to-haves
- [ ] Logging levels set dynamically via files, see [docs](https://docs.python.org/3/library/logging.config.html)
- [ ] Multi-branch output
  - ideally, if a commit came from a different branch originally, I would like to see it as a subsection of the main branch (or a chapter if the main branch is the entire "book"). However, this may not be possible given that branches are typically deleted after merging; this would lose such information. 
- [ ] Add profile avatars as icons on commit message line
  - see [this SO post](https://stackoverflow.com/questions/30229231/python-save-image-from-url) for inspiration on how to download
  - I assume I'd need to cache based on url to make sure I don't download same images repeatedly.
- [ ] Create files in subdirectory hidden from git
  - don't pollute the outer directory?
