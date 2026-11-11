# Locale: Swedish (sv)

Read this file when the page is in Swedish. It adds Swedish form, word lists and trade terms to
the rules in `../laws.md`. Rewrites stay in Swedish. Run `scripts/check.py --lang sv` (the
script guesses Swedish when the text has å, ä or ö and more Swedish than English function words).

Swedish-mode checks:

- absolute (S1)
- stock-phrase (S4, S5)
- nominalization (S4)
- not-x-but-y (S6)
- colon-reveal (S7)
- english-leftover, decimal-point, serial-comma, plural-error, unit-format and
  title-case-heading (all S12)
- question-heading (S9)
- invisible-char (S12)
- long-paragraph (law 2)
- even-rhythm (S10)
- the we-sentence share on the summary line (S3)

## S12 Swedish form

| Rule | Right | Wrong |
|---|---|---|
| Decimal comma, space before the currency | 124,50 kr | 124.50 kr, 124,50kr |
| Dates written out, no leading zero | 4 november 2026 | November 4th 2026, 04/11 |
| Ordinals with colon | 3:e, 21:a | 3rd, 3e |
| Plural after numbers above one | 2 timmar, 1 timme | 2 timme, 1 timmar |
| No serial comma | fönster, ugn och kyl | fönster, ugn, och kyl |
| Capital only on the first word of a heading | Flyttstädning med fast pris | Flyttstädning Med Fast Pris |
| Space before percent and units | 15 %, 24 timmar, 2,3 gånger | 15%, 24h, 2,3x |
| Swedish button labels | Skicka förfrågan, Läs mer | Submit, Read more, Book now |

Dashes are allowed in Swedish customer copy (page copy, meta descriptions, blog posts, UI text, alt
text). The Swedish standard per Svenska skrivregler is a spaced en dash (" – "). An em dash (—)
is replaced with a spaced en dash. Use it as a Swedish writer would: sparingly, and never as the
universal connector.

This is the locale exception to §8 in `../plain-writing.md`. Other Swedish
text (chat replies, commit messages, internal docs) keeps the full dash ban. Proper nouns and abbreviations in headings keep
their capitals ("Städning i Göteborg", "SEO och webb").

## S3 Form of address

Use "du" for consumers and small firms. Use "ni" when the page speaks to an organisation or a
board decision. Keep the page's choice unless it does not fit the reader, and give the reason. A
page may switch to "ni" in a section aimed at businesses ("er verksamhet, era tider"). Keep the
register: "få" never becomes "erhålla".

## S4 Swedish stock words

Flag these, then replace them with the customer's own word or evidence:

skräddarsydd, helhetslösning, sömlös, smidig, i framkant, nästa nivå, brinner för, passion,
engagemang, engagerade, högkvalitativ, hög kvalitet, marknadsledande, marknadens ledande,
innovativ, kundfokus, mervärde, unik, professionell, proffsig, perfekt, kristallklar,
kvalitet och trygghet, gör skillnad.

Empty nominalisations: "utföra / genomföra / erbjuda + en -ning/-ande/-tion" becomes the verb
("vi utför en rengöring" becomes "vi rengör"). Service names are exempt: "Vi erbjuder
flyttstädning" stays, because readers search for "flyttstädning". Pass extra service names to
check.py with `--service "a,b"`.

S3 wins over S4. If readers search for the word ("skräddarsydd hemsida" with impressions in
Search Console), it stays, with evidence next to it.

## S5 Swedish empty calls to action

"Tveka inte att kontakta oss", "Varmt välkommen", "Hör gärna av dig", "Vi finns här för dig",
"Vi ser fram emot att höra om dina behov", "Om du vill veta mer". Each becomes the action and what
happens after it: "Skicka adressen, så får du ett fast pris inom 2 timmar."

## S6 and S7 in Swedish

- "Inte bara X utan Y", "X, inte Y" and "X – inte Y" become Y.
- "Inga mellanhänder, inga callcenter – bara hantverkaren": keep the risk part, rewrite the reveal
  ("Du pratar direkt med målaren").
- Colon reveals: "Hemligheten: ...", "Skillnaden: ...", "Poängen: ...", "räkna med samma sak: ...".
- Warm-ups: "Det som skiljer oss är ...", "Det viktiga är ...".

## Trade terms (S14) and trust claims (law 4)

- **RUT** (rutavdrag): a tax deduction for household services. The buyer pays half of the labour
  cost. The firm claims the rest from Skatteverket. Explain it once as "RUT halverar
  arbetskostnaden", with Skatteverket as source.
- **ROT** (rotavdrag): the same mechanism for repair and renovation labour, at the rate
  Skatteverket sets for the year. Check the current rate at skatteverket.se before you quote it.
- **F-skatt**: the firm is registered to pay its own tax, so the buyer does not owe employer
  contributions. An unsupported F-skatt claim is Critical under law 4.
- **Kollektivavtal** (collective agreement), **ansvarsförsäkring** (liability insurance) and
  **anställda** (employees): unsupported claims are Critical under law 4.
- Public sources for evidence on external sites: Reco (reviews), Allabolag (company register, F-skatt
  status, employee count), and the page's own schema.

## Plain writing in Swedish

`../plain-writing.md` gives its watch lists in English. In Swedish, apply the same patterns to
these equivalents. S6 and S7 above already cover the Swedish contrast and colon-reveal forms.

| Pattern | Swedish equivalents |
|---|---|
| §1 Not X but Y | *inte X utan Y*, *det handlar inte om X, utan om Y* |
| §3 Sayings that sound deep | *det handlar egentligen om*, *i grunden* |
| §4 Staged run-up | *låt oss dyka in i*, *här är vad du behöver veta* |
| §8 Colon reveals | *Hemligheten: rutiner.* (see S7 above for more) |
| §12, §13, §16 AI words, inflation, sales language | *avgörande*, *banbrytande*, *levande*, *pulserande*, *i hjärtat av* |
| §14 Vague connection | *kopplad till*, *i samband med* |
| §17 Borrowed authority | *experter menar*, *enligt branschrapporter* |
| §18 Avoiding is, are, has | *utgör*, *fungerar som* |

§9 qualifiers that make a claim true, in Swedish, are these:

- a lower bound ("från 4 900 kr")
- an upper bound ("upp till 30 %")
- an approximation ("cirka 200 kunder")
- a condition ("om du bokar före 1 maj")
- a scope ("i Göteborg")

 A draft that turns "Hemsida från 4 900 kr" into "Hemsida för 4 900 kr"
breaks the claim. "från" stays because the price varies.

## Swedish examples

| Rule | Before | After |
|---|---|---|
| S1 | Vi levererar alltid högsta kvalitet. | Vi besiktar med dig innan du lämnar nyckeln. |
| S2 | Din pålitliga städfirma. | Flyttstädning i Göteborg med besiktningsgaranti. |
| S8 | ... 4,8 av 5 på Reco. Så enkelt är det. | ... 4,8 av 5 på Reco. |
| S9 | Trött på att städa? Vi fixar det. | Hemstädning i Göteborg från 249 kr/tim efter RUT. |
| S11 | Kvaliteten talar för sig själv. | Vi gör om det kostnadsfritt inom 7 dagar om något missats. |
| S13 | Vad ingår? Vi anpassar alltid efter dina behov ... | Ugn, kyl, fönster och golv ingår. Förrådet kostar 300 kr extra. |

The numbers above are synthetic. A rewrite never adds a number the source does not have: use a
placeholder such as `[SIFFRA: antal städ 2025]` and add the question to the report.
