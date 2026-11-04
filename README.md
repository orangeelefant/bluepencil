# Blue Pencil

Blue Pencil is a Claude Code skill that reviews marketing copy you already have. It scores a web
page, landing page, ad, video script or email from 0 to 100 against ten copywriting laws. Every
finding quotes the exact line and gets a severity. Critical and High findings also get a rewrite
that keeps the original facts.

A small Python script flags stock phrases, unsupported absolutes and locale errors. It also fails
any rewrite that has more of them than the original. Blue Pencil works in English and Swedish.

## What a report looks like

A short synthetic example for a cleaning firm's home page:

```markdown
# Copy review: acmecleaning.example (home page)

https://acmecleaning.example · medium: page · 2026-11-04

## Score: 58/100

The first screen never says what Acme Cleaning sells or where, so a reader from search leaves before the price.

| # | Law | Score | Main finding |
|---|---|---|---|
| 1 | The first screen does the headline's job | 4/10 | "Welcome to Acme Cleaning" names no service or town |
| 4 | Give the reason, with proof | 4/10 | "Always the same trusted team" has no proof |
| 9 | Ask for the action and remove the risk | 7/10 | Clear CTA, no risk reversal |
| ... | | | |

## Findings

### Headline names no service or town · Critical · law 1

> Welcome to Acme Cleaning

A reader on a phone has to scroll before seeing an offer, a town or a price.

**Rewrite** (64 %, New text):
> End-of-tenancy cleaning in Gothenburg, fixed price from [PRICE: lowest fixed price]

## Questions for the client

- What is your lowest fixed price for end-of-tenancy cleaning?
```

## Install

Blue Pencil runs in Claude Code as a skill.

```bash
git clone https://github.com/orangeelefant/bluepencil ~/.claude/skills/bluepencil
```

`scripts/check.py` needs Python 3 and nothing else. A browser crawler (for
example crawl4ai's `crwl`) and a screenshot tool help with live pages. Search Console and
analytics access (PostHog or GA4) are optional.

To add your own tools, paths and conventions, copy `local.md.example` to `local.md` and edit it.
Blue Pencil reads `local.md` first.

## Usage

In Claude Code:

```text
/bluepencil https://acmecleaning.example
/bluepencil ./site/src/pages/pricing.astro page
/bluepencil "Spotless homes, every time. Book today!" ad
Review the copy on these three pages and tell me which one to fix first.
```

Reports go to `./bluepencil-reports/<slug>-<date>/`. Several pages get one report each plus a
`SUMMARY.md` with the scores side by side, contradictions between pages and the three changes to
make first.

## How scoring works

Each law gets 0, 4, 7 or 10 points, with written criteria for each step. In-between scores are
allowed.

Laws that do not fit the medium get `n/a` (sound off counts only for video, answer first
only for pages meant to rank), and the total is rescaled to 100. One Critical finding under law 4
caps that law at 4. Law 10 is judged once per site, because tracking is shared across pages.

Each finding gets a severity:

- Critical: the reader cannot tell the offer, the CTA is missing, or the page claims something
  the source contradicts.
- High: probably costs enquiries.
- Medium: makes the text heavier or less credible.
- Low: polish.

Rewrites keep prices, numbers, names, places, service names and customer quotes as they are. A
missing fact becomes a placeholder and a question for the client. Each rewrite is labelled by how
much text it changes: up to 50 % is a rewrite, over 50 % is new text, over 80 % needs a client
decision.

## The ten laws

1. The first screen does the headline's job (Ogilvy).
2. The point comes first in every line (Nielsen Norman Group, Sugarman).
3. Start from the reader (Halbert, Schwartz).
4. Give the reason, with proof (Kennedy).
5. Concrete benefit, with an exact number (Hopkins).
6. Answer first, for search and AI answers (Pew, CXL).
7. Write for sound off, for video (Meta guidance).
8. One big idea per text (Masterson and Forde).
9. Ask for the action and remove the risk (Lewis, Halbert, Sugarman).
10. Test, don't guess (Hopkins, Caples).

Full checks and scales: `references/laws.md`.

## The language rules

- S1 Claims carry proof.
- S2 The competitor test: if a sentence stays true with a competitor's name, it is generic.
- S3 The reader's words, the right register.
- S4 Stock words become the customer's words.
- S5 Empty calls to action become an action.
- S6 State the claim directly ("not just X but Y" becomes Y).
- S7 No warm-up phrases or colon reveals.
- S8 Sections end on a fact.
- S9 Question headings get a real answer.
- S10 Rhythm fits the situation.
- S11 Every sentence has an actor.
- S12 Locale form: numbers, dates, currency, heading case.
- S13 FAQ answers start with the answer.
- S14 Explain each trade term once.

Locale details: `references/locales/en.md` and `references/locales/sv.md`.

## Plain writing, as an always-on rule

`references/plain-writing.md` is the writing standard Blue Pencil's rewrites and reports follow:
26 patterns of chatbot prose with before and after examples, a list of false positives, and an
audit to run before delivering text. It also works as an always-on Claude Code rule, so every
reply, commit message and document the agent writes follows it:

```bash
ln -s ~/.claude/skills/bluepencil/references/plain-writing.md ~/.claude/rules/plain-writing.md
```

## check.py

```bash
python3 scripts/check.py page.md --brand "Acme Cleaning"   # hits per check, line by line
python3 scripts/check.py page.md --lang en                 # force English checks (sv or en)
python3 scripts/check.py page.md --service "carpet cleaning,window cleaning"  # extra service names
python3 scripts/check.py page.md --json                    # machine-readable output
python3 scripts/check.py --compare original.md proposal.md # PASS or FAIL, exit 1 on FAIL
```

The script prints one line per hit, a summary line with the detected language, and the share of
sentences that start with "We", "Our" or the company name. `--compare` prints how much of the
text changed, then FAIL for each check that has more hits in the proposal. Hits are candidates.
The reviewer decides which become findings.

## Limits

- Source confidence varies. `references/laws.md` labels each number "confirmed" (primary source
  or classic book) or "unconfirmed" (secondary sources). Do not quote unconfirmed numbers to a
  client as fact.
- Scores are guided judgment. Three independent runs on the same page spread up to 6 points
  before the scales were tightened in version 3.2. Compare scores from the same version.
- Blue Pencil judges the text. It does not measure conversion.
- Locales: English and Swedish. Other languages get the language-neutral rules only.

## Credits and sources

The laws draw on David Ogilvy, Claude Hopkins, John Caples, Eugene Schwartz, Gary Halbert, Joseph
Sugarman, John E. Kennedy, Michael Masterson and John Forde, E. St. Elmo Lewis, Nielsen Norman
Group, Pew Research Center and CXL.

The language rules were synthesized from a study of these eight open-source rule sets. Six are
MIT licensed. Humanizr/Humanizer and Turnitout-Humanizer state no license GitHub can detect. The
laws and S1-S14 are restated in our own words. `references/plain-writing.md` is the exception: it
builds on blader/humanizer v3.1.0 and copies substantial parts of its wording, under its MIT
license (Copyright (c) 2025 Siqi Chen), which the file reproduces.

- blader/humanizer
- hardikpandya/stop-slop
- petergyang/no-ai-slop
- hexiecs/talk-normal
- op7418/Humanizer-zh
- epoko77-ai/im-not-ai
- Humanizr/Humanizer
- AhmadHassan-BTed/Turnitout-Humanizer

Made by Webraketen (webraketen.se).

## License

MIT.

---
**Webraketen on GitHub:** [Portfolio](https://github.com/orangeelefant/portfolio) · [Case studies](https://github.com/orangeelefant/case-studies) · [Blue Pencil](https://github.com/orangeelefant/bluepencil) · [webraketen.se](https://webraketen.se)
