# Base Use Case
- assumes user GitHub token in stored in `~/.github/my_gh_token.txt`
1. User gives script the full name of a repo on command line
2. Script pulls down the commits for that repo
3. Script formats the commits into a latex document and renders the PDF from that document (maybe HTML, too?)

# Starting out
- [ ] get access to GitHub
- [ ] get list of commits
- [ ] Organize commits into hierarchy for latex output
  - Repo is Article title
    - branch name is section title
      - commit first line is subheading?? 
      - commit remaining message is paragraph
- [ ] Put commit message contents into latex
- [ ] Render the output latex into PDF
- [ ] open PDF (in default app)


