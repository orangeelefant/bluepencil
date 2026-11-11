# Blue Pencil

A Claude Code skill. It reviews existing marketing copy against ten copywriting laws and fourteen language rules. It gives a score from 0 to 100 and proposes rewrites. The repo is public (MIT).

## Layout

- `SKILL.md`: the workflow that the agent follows.
- `references/laws.md`: the ten laws, the scales, the language rules S1-S14 and the method rule.
- `references/plain-writing.md`: the general writing standard (§1-§26). It also works as an always-on Claude Code rule. Do not change the §-numbers, because other files cite them.
- `references/locales/`: `sv.md` and `en.md`. They hold the language-specific rules and word lists.
- `scripts/check.py`: the mechanical pattern checker (standard library only, Python 3.9+).
- `tests/test_check.py`: unit tests for `check.py`.
- `local.md`: the house overlay for one role. Git ignores it. Never commit it.

## Commands

- Tests: `python3 -W error -m unittest discover tests`
- Check a file: `python3 scripts/check.py page.md --lang sv --brand "Acme"`
- Compare a rewrite: `python3 scripts/check.py --compare original.md proposal.md`

## Done means

The tests pass. The privacy grep in AGENTS.md finds nothing. CHANGELOG.md has a new line.
