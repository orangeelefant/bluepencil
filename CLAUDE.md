# Blue Pencil

A Claude Code skill that reviews existing marketing copy against ten copywriting laws and
fourteen language rules, scores it 0-100 and proposes rewrites. Public, MIT.

## Layout

- `SKILL.md`: the workflow the agent follows.
- `references/laws.md`: the ten laws, scales, language rules S1-S14 and the method rule.
- `references/plain-writing.md`: the general writing standard (§1-§26). Also usable as an
  always-on Claude Code rule. Keep §-numbers stable; other files cite them.
- `references/locales/`: `sv.md` and `en.md`, language-specific rules and word lists.
- `scripts/check.py`: mechanical pattern checker (stdlib only, Python 3.9+).
- `tests/test_check.py`: unit tests for check.py.
- `local.md`: house overlay for one team. Gitignored, never committed.

## Commands

- Tests: `python3 -W error -m unittest discover tests`
- Check a file: `python3 scripts/check.py page.md --lang sv --brand "Acme"`
- Compare a rewrite: `python3 scripts/check.py --compare original.md proposal.md`

## Done means

Tests pass, the privacy grep in AGENTS.md returns nothing, and CHANGELOG.md has a line.
