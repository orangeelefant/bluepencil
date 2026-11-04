#!/usr/bin/env python3
"""bluepencil check: mechanical pattern checks for marketing copy (Swedish and English).

Copyright (c) 2026 Webraketen. Released under the MIT License.

Usage:
  check.py FILE                            hits per check, one line each
  check.py --compare ORIGINAL PROPOSAL     FAIL if any check has more hits in PROPOSAL
  --lang sv|en                             language; guessed from the text when omitted
  --brand NAME                             count sentences starting with NAME as we-sentences
  --service "a,b"                          extra service names exempt from nominalization
  --json                                   machine-readable output

Reads markdown or plain text. Each hit prints category, line number, match and excerpt.
Hits are leads for a reviewer, who decides which ones are real findings.

Adding a language means adding one entry to LOCALES.
"""
import argparse
import difflib
import json
import re
import statistics
import sys

# Shared across locales.
QUESTION_HEADING = r"^#+ .*\?\s*$"
PLACEHOLDER = r"\[[A-ZÅÄÖ]+:[^\]]*\]"
NOISE = r"©|rättigheter|cookie|Alltid aktiv"
INVISIBLE = "​‌‍⁠﻿"
# Customer quotes are never edited, so hits inside them are noise.
# A quote next to a name, or a quote followed by "- Name", is removed before checking.
QUOTE = r"[„“”\"»«][^„“”\"»«]{3,}[„“”\"»«]"
SAYS = r"(?:säger|skriver|berättar|says|said|writes)\s+"
QUOTE_NAME_AFTER = QUOTE + r"\s*(?:[,–—-]\s*(?:" + SAYS + r")?|" + SAYS + r")[A-ZÅÄÖ][a-zåäö]+"
QUOTE_NAME_BEFORE = r"\b[A-ZÅÄÖ][a-zåäö]+(?: [A-ZÅÄÖ]\.?)?\s*:\s*" + QUOTE
SV_WORDS = r"\b(och|att|det|som|för|med|är|på|inte|vi|du|har|kan|till|av|ett|en)\b"
EN_WORDS = r"\b(the|and|to|of|you|we|is|for|with|in|a|your|our|it|on|are)\b"

# Each locale: checks run line by line as (category, regex, flags), in output order.
# "service_stems" exempts service names ("erbjuder städning") from the "service_check" category.
# "title_case_headings" flags headings where every word is capitalized.
# "detect" decides language guessing; English is the fallback.
LOCALES = {
    "sv": {
        "checks": [
            ("absolute",
             r"\b(alltid|aldrig|alla (?:våra )?(?:kunder|jobb|uppdrag|projekt)|garanterat|garanterad|bäst|"
             r"helt och hållet|fullständigt|varje gång|hundratals|tusentals)\b|\b100\s?%", re.I),
            ("stock-phrase",
             r"\b(skräddarsydd\w*|helhetslösning\w*|sömlös\w*|smidig\w*|i framkant|nästa nivå|"
             r"brinner för|passion\w*|engagemang|engagerade|högkvalitativ\w*|marknadsledande|"
             r"innovativ\w*|kundfokus\w*|mervärde\w*|unik\w*|professionell\w*|kvalitet och trygghet|"
             r"tveka inte|varmt välkommen|hör gärna av dig|vi finns här för dig|ser fram emot|kristallklar\w*|"
             r"höga? kvalitet|marknadens ledande|perfekt\w*|proffsig\w*|gör skillnad\w*)\b", re.I),
            ("nominalization",
             r"\b(utför(?:a|t)?|genomför(?:a|t)?|erbjud(?:a|er)) (en |ett )?\w+(ning|ande|tion)\b", re.I),
            ("not-x-but-y",
             r"\binte (bara|enbart|endast|för att)\b.{0,80}\butan\b|(?<!inte )\b\w+(,| [–—]) inte \w+|"
             r"\binte bara\b[^.]{0,60}\.\s+\w+ ska\b|\binga \w+, inga \w+ [–—] bara\b", re.I),
            ("colon-reveal",
             r"^[A-ZÅÄÖ][^:\n\[]{2,40}: [a-zåäö]|"
             r"\b(samma sak|hemligheten|skillnaden|poängen|nyckeln|svaret)\s?: [a-zåäö]", 0),
            ("english-leftover",
             r"\b(Submit|Read more|Learn more|Contact us|Get started|Book now|Click here|See details|Send)\b", re.I),
            ("decimal-point", r"\b\d+\.\d{2}\s?(kr|SEK|:-)", 0),
            ("serial-comma", r"\b\w+, \w+, och \w+", 0),
            ("plural-error",
             r"\b1 (timmar|dagar|veckor|offerter|rum|kvadratmetrar)\b|\b([2-9]|\d{2,}) (timme|dag|vecka|offert)\b",
             re.I),
            ("unit-format", r"\b\d+h\b|\d%|\b\d+(,\d+)?x\b", 0),
            ("question-heading", QUESTION_HEADING, 0),
        ],
        "service_check": "nominalization",
        "service_stems": ["städ", "flytt", "målning", "putsning", "tvätt", "rengöring", "sanering",
                          "montering", "renovering", "webbdesign"],
        "title_case_headings": True,
        "we_start": r"^(Vi|Vår|Våra|Vårt)\b",
        "detect": {"chars": "[åäö]", "words": SV_WORDS},
    },
    "en": {
        # Word lists trimmed for sales copy: common business English ("solution",
        # "professional") is left out. Title case is correct English, so no heading-case check.
        "checks": [
            ("absolute",
             r"\b(always|never|every time|everyone|everybody|nobody|guaranteed?|the best(?! part)|best[- ]in[- ]class|"
             r"all (?:of )?our (?:clients|customers|projects|jobs)|completely|totally|"
             r"hundreds of|thousands of)\b|\b100\s?%(?!\s*$)(?! of\b)", re.I),
            ("stock-phrase",
             r"\b(delv\w*|foster(?:s|ing)?(?! (?:care|home|parent|child|famil))|leverag\w*|utiliz\w*|facilitat\w*|"
             r"empower\w*|streamlin\w*|robust|"
             r"cutting[- ]edge|state[- ]of[- ]the[- ]art|paradigm shift|game[- ]?changer\w*|tapestry|realm|beacon|"
             r"multifaceted|meticulous\w*|intricate|paramount|transformative|elevat\w*|embark\w*|supercharg\w*|"
             r"harness\w*|ever[- ]evolving|seamless\w*|tailor[- ]made|tailored|bespoke|one[- ]stop[- ]shop|"
             r"next level|world[- ]class|top[- ]notch|high[- ]quality|top quality|passion\w*|innovative|"
             r"unique|vibrant|stunning|breathtaking|renowned|nestled|in the heart of|groundbreaking|"
             r"diverse array|commitment to|unparalleled|unmatched|hassle[- ]free|peace of mind|crystal[- ]clear|"
             r"industry[- ]leading|market[- ]leading|customer[- ]centric|holistic|synerg\w*|showcas\w*|"
             r"testament|pivotal|unlock\w*|unleash\w*|revolutioni[sz]\w*|skyrocket\w*|take your \w+ to the next|"
             r"in order to|in terms of|with regard to|going forward|it's worth noting|it is worth noting|"
             r"it's important to note|at the end of the day|when it comes to|in today's \w+ (?:world|age|landscape))\b",
             re.I),
            ("not-x-but-y",
             r"\bnot (?:just|only|merely|simply)\b.{0,80}\bbut\b|"
             r"\b(?:it|this|that)(?:'s| is) not\b[^.]{0,60}[,;.] (?:it|this|that)(?:'s| is)\b|"
             r"\bisn't (?:about )?\w+[^.]{0,40}[,;.] it's\b|"
             r"(?<!not )\b\w+(?:,| [–—]) not (?:a |an |the )?\w+\b(?! (?:only|just|included|yet)\b)|"
             r"\bno \w+, no \w+\b", re.I),
            ("colon-reveal",
             r"^(?:The|One|Our|Your|What|This|That|Here's)\b[^:\n\[*,]{2,40}: [a-z]|"
             r"\b(?:the (?:best|worst) part|the (?:secret|catch|kicker|key|difference|point|answer|result|truth|twist))"
             r"\s?: [a-z]", 0),
            ("warm-up",
             r"\b(here's (?:the thing|the deal|the kicker|what|why|how)|let's (?:dive|explore|break|unpack|be honest)|"
             r"dive (?:into|in)|deep dive|without further ado|the (?:uncomfortable |simple )?truth is|the reality is|"
             r"it turns out|let that sink in|make no mistake|full stop|look no further|"
             r"what (?:most people|nobody|no one) (?:gets? wrong|tells you|talks about)|"
             r"the part (?:everyone|most people) (?:miss|skip)\w*|in a world where|imagine a world)\b", re.I),
            ("conditional-cta",
             r"\b(don't hesitate|do not hesitate|feel free to|if you have any questions|we look forward to|"
             r"we'?d love to (?:hear|help|chat)|we would love to|we're here to help|we are here to help|"
             r"we're here for you|reach out (?:to us )?today|get in touch today|contact us today)\b", re.I),
            ("question-heading", QUESTION_HEADING, 0),
        ],
        "service_check": None,
        "service_stems": [],
        "title_case_headings": False,
        "we_start": r"^(We|Our|Us)\b",
        "detect": {"chars": None, "words": EN_WORDS},
    },
}
FALLBACK_LANG = "en"


def guess_language(text):
    """A locale wins when its characters appear and its function words outnumber English ones."""
    t = text.lower()
    en_count = len(re.findall(LOCALES["en"]["detect"]["words"], t))
    for lang, loc in LOCALES.items():
        chars = loc["detect"]["chars"]
        if chars and re.search(chars, t) and len(re.findall(loc["detect"]["words"], t)) > en_count:
            return lang
    return FALLBACK_LANG


def paragraphs(text):
    """(start line, joined text) for each prose paragraph. Headings, lists, tables and quotes end one."""
    out, buf, start = [], [], 0
    prev = ""
    for i, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        heading_continuation = prev.startswith("#") and prev.endswith("  ")
        prev = line if not heading_continuation else ""
        if not stripped or heading_continuation or stripped.startswith(("#", "|", "-", "*", ">", "!", "[")):
            if buf:
                out.append((start, " ".join(buf)))
                buf = []
            continue
        if not buf:
            start = i
        buf.append(stripped)
        if stripped.endswith("?"):
            out.append((start, " ".join(buf)))
            buf = []
    if buf:
        out.append((start, " ".join(buf)))
    return out


def sentences(paragraph):
    return [s for s in re.split(r"(?<=[.!?])\s+", paragraph) if len(s.split()) > 1]


def clean(text):
    """Blank out quotes, images, footer noise and link-heavy lines. Line numbers stay intact."""
    out = []
    for line in text.splitlines():
        if line.lstrip().startswith(">") or re.search(QUOTE + r"\s*[–—-]\s*[A-ZÅÄÖ]", line):
            out.append("")
            continue
        line = re.sub(QUOTE_NAME_AFTER, "", line)
        line = re.sub(QUOTE_NAME_BEFORE, "", line)
        line = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)
        line = re.sub(PLACEHOLDER, "X", line)
        if line.count("](") >= 3 or re.search(NOISE, line, re.I):
            line = ""
        line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)
        out.append(line)
    return "\n".join(out)


def check(text, brand=None, lang="sv", services=()):
    """Return (hits, we_sentences, total_sentences, we_percent). A hit is (category, line, excerpt, match)."""
    loc = LOCALES[lang]
    text = clean(text)
    lines = text.splitlines()
    hits = []
    stems = loc["service_stems"] + [s.strip().lower() for s in services if s.strip()]

    for category, pattern, flags in loc["checks"]:
        exempt = category == loc["service_check"]
        for nr, line in enumerate(lines, 1):
            for m in re.finditer(pattern, line, flags):
                if exempt and any(st in m.group(0).split()[-1].lower() for st in stems):
                    continue
                hits.append((category, nr, line.strip()[:110], m.group(0)))

    # Names are capitalized words mid-sentence in body text (places, brands).
    names = set()
    if loc["title_case_headings"]:
        body = "\n".join(line for line in lines if not line.startswith("#"))
        names = set(re.findall(r"(?<=[a-zåäö,] )([A-ZÅÄÖ][a-zåäö]{2,})", body))
    for nr, line in enumerate(lines, 1):
        if any(c in line for c in INVISIBLE):
            hits.append(("invisible-char", nr, repr(line.strip()[:60]), "U+200x"))
        if loc["title_case_headings"] and line.startswith("#"):
            words = re.findall(r"[A-Za-zÅÄÖåäö]{3,}", line)
            common = [w for w in words if not w.isupper() and w not in names]
            if len(common) >= 2 and all(w[0].isupper() for w in common):
                hits.append(("title-case-heading", nr, line.strip()[:110], line.strip()))

    all_sentences = []
    for start, para in paragraphs(text):
        word_count = len(para.split())
        if word_count > 60:
            hits.append(("long-paragraph", start, para[:110], f"{word_count} words"))
        ss = sentences(para)
        all_sentences += ss
        lengths = [len(s.split()) for s in ss]
        questions = sum(s.rstrip().endswith("?") for s in ss)
        if len(lengths) >= 4 and statistics.pstdev(lengths) < 2.5 and questions < 3:
            hits.append(("even-rhythm", start, para[:110], f"lengths {lengths}"))

    we = [s for s in all_sentences if re.match(loc["we_start"], s) or (brand and s.startswith(brand))]
    percent = round(100 * len(we) / len(all_sentences)) if all_sentences else 0
    return hits, len(we), len(all_sentences), percent


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def count(hits):
    per = {}
    for h in hits:
        per[h[0]] = per.get(h[0], 0) + 1
    return per


def report(path, brand=None, lang=None, services=(), as_json=False):
    text = read(path)
    source = "given" if lang else "guessed"
    lang = lang or guess_language(text)
    hits, we, total, percent = check(text, brand, lang, services)
    per = count(hits)
    if as_json:
        print(json.dumps({
            "file": path,
            "language": lang,
            "language_source": source,
            "hits": [{"category": c, "line": n, "match": m, "excerpt": e} for c, n, e, m in hits],
            "summary": dict(sorted(per.items())),
            "we_sentences": {"count": we, "total": total, "percent": percent},
        }, ensure_ascii=False, indent=2))
        return per
    for category, nr, excerpt, match in hits:
        print(f"{category}\tline {nr}\t[{match}]\t{excerpt}")
    print("---")
    summary = "summary: " + ", ".join(f"{k} {v}" for k, v in sorted(per.items())) if per else "summary: 0 hits"
    print(f"{summary} | language: {lang} ({source})")
    print(f"we-sentences: {we} of {total} ({percent} %)")
    return per


def compare(original, proposal, lang=None, services=(), as_json=False):
    """Exit 1 (FAIL) when any category has more hits in the proposal than in the original."""
    a = read(original)
    b = read(proposal)
    lang = lang or guess_language(a)
    pa = count(check(a, lang=lang, services=services)[0])
    pb = count(check(b, lang=lang, services=services)[0])
    increased = {k: (pa.get(k, 0), v) for k, v in pb.items() if v > pa.get(k, 0)}
    # Change: share of the original (or the proposal) that does not survive verbatim.
    m = difflib.SequenceMatcher(None, a, b, autojunk=False)
    kept = sum(x.size for x in m.get_matching_blocks())
    removed = 1 - kept / max(len(a), 1)
    added = 1 - kept / max(len(b), 1)
    change = round(100 * max(removed, added))
    if as_json:
        print(json.dumps({
            "language": lang,
            "change_percent": change,
            "result": "FAIL" if increased else "PASS",
            "increased": {k: {"before": f, "after": t} for k, (f, t) in increased.items()},
            "original": dict(sorted(pa.items())),
            "proposal": dict(sorted(pb.items())),
        }, ensure_ascii=False, indent=2))
        return 1 if increased else 0
    print(f"change: {change} %")
    if increased:
        for k, (before, after) in increased.items():
            print(f"FAIL\t{k}\t{before} -> {after}")
        return 1
    print("PASS: no check increased")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="check.py", description="Pattern checks for marketing copy.")
    p.add_argument("file", nargs="?", help="markdown or text file to check")
    p.add_argument("--compare", nargs=2, metavar=("ORIGINAL", "PROPOSAL"),
                   help="FAIL if any check has more hits in PROPOSAL")
    p.add_argument("--lang", choices=sorted(LOCALES), help="language; guessed when omitted")
    p.add_argument("--brand", help="sentences starting with this name count as we-sentences")
    p.add_argument("--firma", dest="brand", help=argparse.SUPPRESS)
    p.add_argument("--service", help="comma-separated service names exempt from nominalization")
    p.add_argument("--tjanst", dest="service", help=argparse.SUPPRESS)
    p.add_argument("--json", action="store_true", help="machine-readable output")
    args = p.parse_args(argv)
    services = args.service.split(",") if args.service else ()
    if args.compare:
        return compare(*args.compare, args.lang, services, args.json)
    if not args.file:
        p.print_usage(sys.stderr)
        return 2
    report(args.file, args.brand, args.lang, services, args.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
