# Locale: English (en)

Read this file when the page is in English. It adds English form and word lists to the rules in
`../laws.md`. Rewrites stay in English, in the page's variant (US or UK spelling). Run
`scripts/check.py --lang en`. Without the flag the script picks English unless the text has å, ä
or ö and more Swedish than English function words.

## What check.py checks in English mode

| Check | Rule | Catches |
|---|---|---|
| absolute | S1 | always, never, every time, everyone, nobody, guaranteed, the best, best-in-class, all our clients, completely, totally, hundreds of, thousands of, 100 % |
| stock-phrase | S4, S7 | the word list below |
| not-x-but-y | S6 | "not just X but Y", "it's not X, it's Y", "isn't about X, it's Y", "X, not Y", "no X, no Y" |
| colon-reveal | S7 | "The secret: ...", "The catch: ...", "Here's what: ..." and lines that open with The/One/Our/What before a colon and a lower-case word |
| warm-up | S7 | here's the thing, let's dive in, deep dive, without further ado, the truth is, the reality is, it turns out, let that sink in, make no mistake, full stop, look no further, what nobody tells you, in a world where, imagine a world |
| conditional-cta | S5 | don't hesitate, feel free to, if you have any questions, we look forward to, we'd love to hear, we're here to help, reach out today, contact us today |
| question-heading | S9 | headings that end in "?" |
| invisible-char | S12 | U+200B, U+200C, U+200D, U+2060, U+FEFF |
| long-paragraph | law 2 | paragraphs over 60 words |
| even-rhythm | S10 | four or more sentences with a length standard deviation under 2.5 words |
| we-sentences (summary line) | S3 | share of sentences that start with We, Our, Us or the company name (`--brand`) |

English mode skips the Swedish form checks and the heading-case check, because title case is
correct English.

## S4 English stock words

delve, foster, leverage, utilize, facilitate, empower, streamline, robust, cutting-edge,
state-of-the-art, paradigm shift, game-changer, tapestry, realm, beacon, multifaceted, meticulous,
intricate, paramount, transformative, elevate, embark, supercharge, harness, ever-evolving,
seamless, tailor-made, tailored, bespoke, one-stop shop, next level, world-class, top-notch,
high-quality, top quality, passion, innovative, unique, vibrant, stunning, breathtaking, renowned,
nestled, in the heart of, groundbreaking, diverse array, commitment to, unparalleled, unmatched,
hassle-free, peace of mind, crystal clear, industry-leading, market-leading, customer-centric,
holistic, synergy, showcase, testament, pivotal, unlock, unleash, revolutionize, skyrocket, take
your X to the next level.

Filler: in order to, in terms of, with regard to, going forward, it's worth noting, it's
important to note, at the end of the day, when it comes to, in today's fast-paced world.

Plain business words ("solution", "professional", "service") are not on the list. They become a
finding only under S2, when the sentence fails the competitor test.

S3 wins over S4. If readers search for the word ("bespoke kitchen" with impressions in Search
Console), it stays, with a proof next to it.

## S12 English form (manual checks)

check.py does not check these. Read for them.

| Rule | Right | Wrong |
|---|---|---|
| Currency symbol before the number, no space | $124.50, £95 | 124.50$, $ 124.50 |
| Thousands separator | 12,500 | 12 500, 12.500 |
| One date style per page | 4 November 2026 (UK), November 4, 2026 (US) | both on the same page |
| Plural after numbers above one | 1 hour, 2 hours | 2 hour |
| One list-comma style per page | Oxford comma throughout, or never | mixed |
| One heading case per page | title case throughout, or sentence case throughout | mixed |
| Spelling variant matches the market | colour (UK), color (US) | mixed on one page |
| Units | 24 hours, 15% or 15 percent, 2.3 times | 24h in body text, 2.3x in body text |

A percent sign with no space ("15%") is standard English. Dashes in client copy follow the
house style of the page. Flag only mixed use (em dash and spaced en dash on the same page).

## S14 English trade terms

Explain at first use what the reader gains: VAT registration, licensed and insured, bonded, SEO,
CTA, UX. Example: "We are licensed and insured" becomes "Our £5 million liability insurance
covers any damage in your home." Check the number against the source; never invent it.

## English examples

| Rule | Before | After |
|---|---|---|
| S1 | We always deliver the highest quality. | We walk through the flat with you before you hand back the keys. |
| S2 | Your trusted cleaning partner. | End-of-tenancy cleaning in Gothenburg, with a free re-clean if the landlord objects. |
| S5 | Don't hesitate to reach out! | Send your address and get a fixed price within 2 hours. |
| S6 | It's not just a website, it's a sales tool. | The site turns visitors into booked calls. |
| S7 | Here's the thing: price matters. | Every quote is a fixed price. |
| S11 | Quality speaks for itself. | We re-clean for free within 7 days if we missed something. |

The numbers above are synthetic. A rewrite never adds a number the source does not have: use a
placeholder such as `[NUMBER: jobs done in 2025]` and add the question to the report.
