# AGENTS.md

Read this file before you change anything in this repo.

- This repo is public. Do not commit customer names, customer domains, customer figures, private paths, emails, keys or tokens. `local.md` holds house-specific material. Git ignores it.
- Before each commit, run the tests and the privacy grep. Fix each finding:
  `python3 -W error -m unittest discover tests`
  `git grep -niE 'secrets|api[_-]?key|token|@[a-z0-9-]+\.[a-z]{2,}' -- ':!AGENTS.md'`
- A change to `check.py` must keep the existing finding counts, unless the change is the point. In that case, write it in CHANGELOG.md.
- A change to a scale in `references/laws.md` changes the scores. Write it in CHANGELOG.md.
- Push to `main`. Make one logical change in each commit. Put a CHANGELOG line in the same commit.
- Write plain English with short sentences. Do not use em dashes or en dashes, except in quoted Swedish examples.
