# AGENTS.md

Read before changing anything in this repo.

- This repo is public. Never commit client names, client domains, client figures, private
  paths, emails, keys or tokens. `local.md` holds house-specific material and is gitignored.
- Before every commit, run the tests and the privacy grep, and fix every hit:
  `python3 -W error -m unittest discover tests`
  `git grep -niE 'secrets|api[_-]?key|token|@[a-z0-9-]+\.[a-z]{2,}' -- ':!AGENTS.md'`
- A change to `check.py` must keep existing hit counts unless the change is the point; say so in
  CHANGELOG.md.
- A change to a scale in `references/laws.md` changes scores. Note it in CHANGELOG.md.
- Push to `main`. One logical change per commit, with a CHANGELOG line in the same commit.
- Prose: plain English, short sentences, no em or en dashes outside quoted Swedish examples.
