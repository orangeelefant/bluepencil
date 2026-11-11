# Changelog

## [Unreleased]
- Docs: internal text rewritten to ASD-STE100 English.

## [1.5.0] - 2026-11-04

- New `references/plain-writing.md`: the general writing standard (26 patterns with examples,
  false positives, audit, scope), built on blader/humanizer v3.1.0 (MIT). Rewrites and report
  prose follow it. README explains how to load it as an always-on Claude Code rule.
- `locales/sv.md`: Swedish equivalents for the plain-writing patterns and the full spaced en dash
  rule for Swedish client copy.

- TODO: spread-test follow-up closed after the maintainer confirmed the tightened scales.

- README credits list all 8 source rule sets (Turnitout-Humanizer was missing) and states their licenses.

- README ends with the shared Webraketen footer linking Portfolio, Case studies and webraketen.se.

## [1.4.0] - 2026-11-04

- First public release. Ten copywriting laws with 0-10 scales, language rules S1-S14, method
  rule M1, rewrite rules (protected facts, qualifiers, compare check, scope labels).
- `check.py` with Swedish and English locales, `--compare`, `--json`, `--brand`, `--service`.
- Scales for laws 3, 4, 6 and 9 tightened after a spread test (three runs per page spread up
  to 6 points before).
