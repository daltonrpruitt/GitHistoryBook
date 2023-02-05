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
- [ ] Put commit message contents into latex
- [ ] Render the output latex into PDF
- [ ] open PDF (in default app)


# Nice-to-haves
- [ ] Logging levels set dynamically via files, see [docs](https://docs.python.org/3/library/logging.config.html)
- [ ] Multi-branch output
  - ideally, if a commit came from a different branch originally, I would like to see it as a subsection of the main branch (or a chapter if the main branch is the entire "book"). However, this may not be possible given that branches are typically deleted after merging; this would lose such information. 