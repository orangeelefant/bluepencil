# The ten laws (version 3.2)

Each law has an origin, a list of checks and a score scale. Always judge what the reader
actually sees: the mobile view for pages, the first seconds for video.

Source confidence: **confirmed** means a primary source was read, or the claim comes from a
classic book. **Unconfirmed** means the number comes from secondary sources such as agency
blogs. Unconfirmed numbers guide the review. Do not quote them to a client as fact.

Each scale has four steps. In-between scores are allowed when the text falls between two
steps (for example 2 or 5). When two steps fit at once, pick the lower one and name the
criterion that pulled it down. The medium decides what the "first screen" is, per the table
in SKILL.md. For ads it is the headline plus the first 125 characters, with no screenshot.

Locale-specific rules (number format, word lists, forms of address, tax and trade terms) live
in `locales/<lang>.md`. Read the file for the page's language before step 3.

---

## Method rule

Every finding quotes the line it is based on, word for word. No quote, no finding. The report
never says "AI-written". It names the pattern, quotes the line and gives the fix.

Pattern strength decides when a hit becomes a finding:

- Strong patterns become a finding on the first hit: S1, S2, S5, S6, S11.
- Weak patterns become a finding only at two hits on the same page, or together with another
  pattern: S4, S7, S9, S12.

`scripts/check.py` finds candidates for S1, S4, S5, S6, S7, S9, S10 and S12. The reviewer
decides which candidates become findings.

---

## Language rules (S1-S14, apply across all laws)

Merged from about 145 rules in eight open-source rule sets (see Credits in README.md). Each
language rule names the law its findings go to. A finding that fits no law goes under
"Outside the laws" in the report.

- **S1 Claims carry proof.** Absolute words (always, never, everyone, best, 100 %,
  guaranteed) and "X matters to us" with no number, name or mechanism in the same sentence
  are findings under law 4. A mechanism is a step the reader can check ("we walk through the
  flat with you before you hand back the keys"). An adjective ("with great care") or a
  guarantee is not a mechanism. Words that state scope ("all windows, inside and out") are not
  absolute claims. Product names the client has confirmed ("100 % Satisfaction Guarantee" in
  the product docs) are protected and not flagged.
- **S2 The competitor test.** Swap the company name and town for a competitor's. If the
  sentence is still true, it is generic (law 4). Count those sentences on the first screen and
  write the count. Exception: the line that only names service, town and customer type
  ("End-of-tenancy cleaning in Gothenburg") should be true for competitors too; it does law 1's
  job. If you can see other sites built by the same author or agency in the same trade and
  town, test against them too. Shared FAQs and sections, word for word, are findings.
- **S3 The reader's words, the right register.** Use the word customers search for (Search
  Console). Pick the form of address for the situation, per the locale file. Change the page's
  choice only when it does not fit the reader, and give the reason. Count sentences that start
  with "We", "Our" or the company name (law 3).
- **S4 Stock words become the customer's words.** Tailored, one-stop shop, seamless,
  cutting-edge, next level, passionate about. "Perform/offer + noun" becomes the verb, unless
  the noun is the service name readers search for. S3 wins: if readers search for the word
  ("bespoke website", 79 impressions on the pricing page), it stays, with a proof next to it.
  The locale file lists the stock words for each language.
- **S5 Empty calls to action become an action.** "Don't hesitate to contact us", "If you want
  to know more", "We look forward to hearing from you" become what the reader does and what
  happens next (law 9).
- **S6 State the claim directly.** "Not just X but Y" and "X, not Y" become Y. A negative line
  that removes a real risk stays ("No lock-in period" on a subscription, "No setup fee"). Judge
  each part on its own: in "No middlemen, no call centre, just the tradesperson", the risk part
  stays and the reveal is rewritten ("You talk directly to the painter").
- **S7 No warm-up.** "What sets us apart is...", "The important thing is..." and colon reveals
  ("The secret: ...") become a direct statement. Colons in lists, labels and prices stay. S7 is
  a weak pattern: a single colon that carries the sender's voice ("one thing counts:") stays.
- **S8 Sections end on a fact.** The last sentence is a fact or the next step. A slogan after a
  proof ("It's that simple.") is cut.
- **S9 Question headings get a real answer.** "Tired of cleaning? We've got it covered."
  becomes offer, town and price (law 1).
- **S10 Rhythm fits the situation.** In running text: no runs of three, no fragment lines, no
  even sentence length (check.py flags a standard deviation under 2.5 words). H1 and lead
  paragraph count as running text. In USP rows, price boxes and lines next to a button, runs of
  three, fragments and bold may stay when each part is its own fact.
- **S11 Every sentence has an actor.** You, we or the company. Things that act ("Quality speaks
  for itself", "The result is...") are rewritten with whoever does something. Passive voice may
  stay in lists of what is included ("The oven is cleaned"). A plain sentence that describes the
  page's mechanism and names who carries it may stay ("A fixed price moves the risk to us."). S11
  targets vague abstract subjects with vague verbs.
- **S12 Locale form.** Numbers, dates, ordinals, currency, plurals after numbers, list commas,
  heading case, dashes and button language follow the page's locale. The rules and examples are
  in `locales/<lang>.md`. Invisible characters (U+200B, U+200C, U+200D, U+2060, U+FEFF) are
  flagged in every language.
- **S13 FAQ answers start with the answer.** Yes, no or a number first, then the reason (law 6).
  If there is no true yes or no, start with the condition ("Only if...", "It depends on the
  number of windows: ..."). The qualifier rule in SKILL.md wins over S13.
- **S14 Explain each trade term once.** Tax deductions, licences, registrations and terms like
  SEO get, at first use, what the reader gains from them, with a source. After that the term
  stands alone (law 5). First use counts in body text; menu, footer, buttons and price lines on
  the first screen do not count. The explanation goes in the first paragraph after the first
  screen. It must be complete: "the deduction halves the labour cost", not "the tax office pays
  half". A price page with several packages marks one as recommended for a named customer type
  (law 9).

---

## 1. The first screen does the headline's job

Origin: Ogilvy, *Confessions of an Advertising Man* (1963): five times as many people read the
headline as the body copy (confirmed). Meta study via secondary sources: 47 % of a video ad's
value comes in the first 3 seconds (unconfirmed). TikTok's own creative guidance: state the
offer within 3 seconds.

Check on the first screen (see the table in SKILL.md):

- What is sold, to whom, and what the reader gets out of it. The audience is the customer type
  (consumer, business) plus the market: the town for local services ("in Gothenburg"), the
  country for a seller working nationwide or abroad ("for UK companies").
- Whether the headline works without the image and without the rest of the page.
- Whether the first screen promises something the rest of the page takes back (a "Fixed price"
  stamp on an example that later "depends on condition"). Log that finding under law 4.

| Score | Criterion |
|---|---|
| 10 | Offer, audience and benefit can all be read on the first screen |
| 7 | Two of three |
| 4 | The headline is clear but generic ("Welcome to ...", "We make a difference") |
| 0 | The first screen does not say what is sold |

## 2. The point comes first in every line

Origin: Nielsen Norman Group eye-tracking studies: readers take in about 20-28 % of the words
on a page, and mobile sessions are shorter (unconfirmed for the 2025 figures, confirmed for
scanning as a pattern). Sugarman: every sentence should make the reader read the next one.

Check:

- Whether headings, subheadings and the first words of each paragraph carry the content alone.
- Paragraphs over 60 words (about 4 lines at 390 px). Count them with a script.
- Subheadings that are labels ("About us", "Services") instead of statements.
- Ads, email and video without subheadings: judge the first words of each sentence and what
  shows before "See more" (Meta cuts primary text at about 125 characters). Count the
  characters.

| Score | Criterion |
|---|---|
| 10 | The headings alone give the offer and the next step, and no paragraph is over 60 words |
| 7 | The headings alone give the offer, at most three paragraphs over 60 words |
| 4 | Label or question headings dominate, or more than three paragraphs over 60 words |
| 0 | Wall of text with no structure |

## 3. Start from the reader

Origin: Halbert, "the starving crowd": the right audience beats better copy (confirmed).
Schwartz, *Breakthrough Advertising* (1966): copy channels a desire that already exists, and
must match the reader's awareness level in five steps: unaware, problem aware, solution aware,
product aware, most aware (confirmed).

Check:

- Which level the page assumes. Compare with Search Console queries when you have them: "end of
  tenancy cleaning price gothenburg" means a product-aware reader who wants the price now.
- Ads without Search Console: derive the level from the audience or campaign goal if given
  (retargeting = product aware, cold audience = problem aware). Otherwise state the assumption.
- The reader's words on the page: take the five biggest query words in Search Console that are
  not place or service names ("subscription", "book", "urgent", "price") and search the page for
  them. A word with more than 10 % of impressions and 0 hits on the page is a Medium finding,
  High above 25 %. Place names in Search Console that the page never mentions become a question
  to the client: does the firm work there?
- Count a sentence as "about the company" when its subject is we, our or the company name.
  Reviews and source lines do not count. Write the count in the finding.

| Score | Criterion |
|---|---|
| 10 | The opening matches the reader's level and the reader's words |
| 7 | Right level, but the company's words instead of the reader's |
| 4 | Wrong level, or more than half of the sentences are about the company |
| 0 | Wrong level and almost only sentences about the company |

## 4. Give the reason, with proof

Origin: John E. Kennedy (1904): advertising is "salesmanship in print", and every claim needs a
reason (confirmed). Studies from 2025 (Journal of Retailing and Consumer Services; Journal of
Interactive Advertising): ads labelled as AI-generated got lower trust (confirmed in summaries,
effect size unconfirmed).

Check:

- Each promise ("best", "fast", "quality") against a reason or proof nearby: a number, a review
  with a name, a certification, a guarantee with terms, a real photo.
- Generic phrases that could sit on any competitor's site.
- **Critical** is a claim about contracts, tax or business registration, insurance,
  certification, guarantee or employees that the product docs contradict, give no support for,
  or list as unanswered. An unsupported claim about staffing ("the same cleaner every time",
  "the same team") is **High**. External site with no docs: look for proof on the page and in
  public sources (review sites, company registers, schema). If nothing turns up, the same
  grading applies.
- Contradictions between pages (step 2b in SKILL.md) belong to this law.
- One Critical finding under this law caps its score at 4.
- A guarantee does not prove an absolute claim. "Always happy customers" does not become true
  through a "satisfaction guarantee"; the guarantee is risk reversal under law 9.
- A review that is the company's own text, or has no name and town, does not count as proof.

| Score | Criterion |
|---|---|
| 10 | Every main promise has a concrete proof next to it |
| 7 | Every main promise has a proof that supports that exact promise, but the proof sits far from it |
| 4 | At least one main promise lacks proof that supports it. A star rating supports happy customers, not promises about staffing, condition or guarantees |
| 0 | Only claims |

## 5. Concrete benefit, with an exact number

Origin: Hopkins, *Scientific Advertising* (1923): specific claims are believed, general ones are
not (confirmed).

Check:

- Whether features ("tax deduction", "our own machines") are translated into what the reader
  gets.
- Round or vague numbers ("many happy customers") where an exact number is available.

| Score | Criterion |
|---|---|
| 10 | The benefit is concrete and carries at least one exact number |
| 7 | Concrete benefit without numbers |
| 4 | Features without benefit |
| 0 | Neither benefit nor features, only adjectives |

## 6. Answer first (search and AI answers)

Applies to pages meant to be found through search. Origin: Pew Research (July 2025): searchers
rarely click the links in Google's AI Overviews (confirmed second-hand). CXL, 100 AI Overviews:
55 % of cited passages came from the top 30 % of the page (small sample, unconfirmed).

Check:

- Whether the page's main question is answered in the first 2-3 sentences. The main question is
  the Search Console query with the most impressions. Without Search Console it is the search
  phrase in the title tag or the H1, and the answer is what is sold and where. Price belongs to
  the main question only when the query contains "price" or "cost". Otherwise a missing price is
  a finding under law 5.
- Price, area served and time taken: are they in text, not only in an image or a PDF?
- Law 6 is judged on the HTML text, including text hidden on mobile. Search engines and AI
  answers read it. Law 1 is judged on the 390 px screenshot.
- Answers that exist only in structured data (FAQPage schema) and not as visible text count as
  "only in an image" (4). The reader cannot see them.

| Score | Criterion |
|---|---|
| 10 | The main question is answered in the first paragraph, in text, with numbers |
| 7 | The answer is in the first paragraph without numbers, or with numbers above the middle of the page |
| 4 | The answer is further down or only in an image |
| 0 | No answer |

## 7. Write for sound off (video)

Applies to moving images. Origin: Meta's guidelines treat captions as required. "85 % watch
without sound" is repeated everywhere but has no primary source (unconfirmed). TikTok is more
often played with sound on.

Check:

- Whether the message gets through with sound off: captions and on-screen text.
- Whether the offer shows as text within 3 seconds.

| Score | Criterion |
|---|---|
| 10 | The whole message and the CTA get through without sound |
| 7 | Captions exist, but the offer comes after 3 seconds |
| 4 | Partly captioned |
| 0 | The message needs sound |

## 8. One big idea per text

Origin: Masterson and Forde, *Great Leads* (2011) (confirmed).

Check:

- Whether the text can be summed up in one sentence. Try it and write the sentence in the
  finding.
- Competing messages on the first screen, or several equal CTAs.

| Score | Criterion |
|---|---|
| 10 | One idea carries the whole text |
| 7 | One main idea with side tracks |
| 4 | Two or three ideas compete |
| 0 | No idea can be pointed out |

## 9. Ask for the action and remove the risk

Origin: AIDA, E. St. Elmo Lewis (1898). A guarantee moves risk from buyer to seller: Halbert and
Sugarman (confirmed).

Check:

- Whether the CTA says what happens ("Get a price in 2 minutes") instead of "Submit" or "Read
  more".
- Ad buttons come from the platform's fixed list (Meta: for example "Learn more", "Book now",
  "Get quote", "Contact us"). Suggest only a label from that list and put the precise promise in
  the headline or text.
- Whether the CTA shows on the first mobile screen and after each proof section.
- Risk the reader carries: lock-in, unknown price, what happens after the click. Is there a
  guarantee, price guarantee or "no lock-in" in text near the CTA?
- Does the risk reversal answer the risk the reader has for this service? Moving out: the final
  inspection. Regular home cleaning: lock-in and keys. Payment up front: what happens if the
  customer rejects the sketch. "No lock-in" on a one-off purchase answers no risk.
- Does the CTA promise something the next step does not keep ("price within 24 hours" when the
  price comes 24 hours after a phone call)? Read the page the button leads to.
- Links to other companies in the same trade, anywhere on the page, lead the reader away from
  the CTA. Each such link is a Medium finding under "Outside the laws".

| Score | Criterion |
|---|---|
| 10 | Clear CTA that says what happens, visible early, with risk reversal next to it that answers the main service's risk per the list above |
| 8 | As 10, but the risk reversal covers only the quote or price ("free", "non-binding quote", "valid for 30 days") |
| 7 | Clear CTA without risk reversal |
| 4 | Generic CTA ("Contact us") or far down the page |
| 0 | No CTA |

## 10. Test, don't guess

Origin: Hopkins (1923) and Caples, *Tested Advertising Methods* (1932) (confirmed).

The review cannot test the text. Law 10 is therefore judged on whether the site can be measured
and whether the report proposes a test. Judge it once per site (see SKILL.md step 4). Pasted text
with no known domain or ad account: `n/a`, and the report still proposes a test.

- Look for tracking in the repo, if you have it:
  `grep -rnE "capture\(|gtag\(|dataLayer|fbq\(|posthog|lead_form_submit|phone_click|send_to:" <repo>/src`.
  Tracking often sits in a shared client file, not in the page.
- Count real events in your analytics tool for the last 90 days. PostHog example:
  `select event, count() from events where properties.$host like '%<domain>%' and timestamp > now() - interval 90 day group by event order by count() desc`.
  GA4: the `eventName` dimension with `eventCount` over the same window. Code that tracks but
  shows 0 events in 90 days counts as unmeasured; the key is probably missing in production. A
  button click or a submitted form both count as measured. Note CTA paths without tracking, such
  as anchor links the event does not catch.
- Earlier tests: search `CHANGELOG.md` for "test", "variant", "A/B", and list experiments in the
  analytics tool.
- External site with no repo and no accounts: judge on the tracking code in the HTML (`gtag(`,
  `posthog`, `fbq(`, `dataLayer`). Code exists but conversions cannot be seen: at most 4.
- The report proposes a test for the critical finding: one variant, one metric. If the site has
  fewer than 100 conversions a month, propose a before/after comparison over four weeks with
  dates and a metric, because an A/B test will not reach an answer in time. (The 100 limit is a
  rule of thumb.)

| Score | Criterion |
|---|---|
| 10 | The CTA is measured and an earlier test or variant exists |
| 7 | The CTA is measured |
| 4 | Page views are measured, the CTA is not |
| 0 | No tracking found |
