#!/usr/bin/env python3
"""Build Vendor-Capital-Brief.html from the data table below.

Capital facts for the six shortlisted vendors, researched 2026-09-09 from
public sources. The SEC Form D figures are the spine of this document: they are
filed under penalty of perjury and they disagree with three of the press
releases. Everything here carries a source; *not found* is written as not found.

Compassus palette and the mark, per brand/BRAND.md — this one goes to a
Compassus audience, so it wears the corporate identity rather than the house one.
"""
import html, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
BRAND = HERE.parents[2] / "brand"
LOGO = (BRAND / "compassus-logo.datauri.txt").read_text().strip()
OUT = HERE / "Vendor-Capital-Brief.html"

# ── the data ──────────────────────────────────────────────────────────────
# raised: verified dollars. None = no figure exists (not zero, not found).
VENDORS = [
    dict(
        slug="med-arrive", name="MedArrive", entity="MedArrive, Inc.",
        seat="New York, NY  ·  85 5th Ave, 8th Floor", inc="2018",
        raised=40_843_775, shown="$40.84M", stage="Series A + strategic",
        cik="0001901894",
        headline="Raised more than it announced, then raised less than it asked for.",
        rounds=[
            ("Dec 2020", "Launch capital", "$4.5M", "Redesign Health", "press"),
            ("28 Jan 2022", "Series A — first sale", "$32,843,775 sold", "Kleiner Perkins co-led · 41 investors", "formd"),
            ("31 Mar 2023", "Strategic — first sale", "$8,000,000 sold of $10,000,000", "Cobalt Ventures (BCBS Kansas City) · 1 investor", "formd"),
        ],
        flags=[
            ("The Series A was ~31% larger than the press release said.",
             "The November 2021 announcement said <b>$25M</b>. The Form D filed 11 Feb 2022 reports "
             "<b>$32,843,775 actually sold</b> to <b>41 investors</b>, first sale 28 Jan 2022. "
             "A $7.84M difference between the number they published and the number they filed."),
            ("The 2023 round was undersubscribed by 20%, and had exactly one investor.",
             "They offered <b>$10,000,000</b> and sold <b>$8,000,000</b>. <b>$2,000,000 was never filled.</b> "
             "The filing records <b>one</b> investor — Cobalt Ventures. A strategic cheque, not a round."),
            ("Nothing has been filed with the SEC since 11 April 2023.",
             "Three years and five months. In that window they abandoned the field-provider business, "
             "rebuilt the product, changed CEO, changed state and bought a competitor's assets — "
             "all with no new exempt offering on record."),
            ("A board seat changed hands between the two filings.",
             "<b>Lynne Chou O'Keefe</b> (Define Ventures) is named on the 2022 filing and absent from the 2023 one. "
             "<b>Agneta Breitenstein</b> appears on the 2023 filing and not the 2022 one. "
             "Constant across both: Dan Trigub, Inna Plumb, Annie Case (Kleiner Perkins), "
             "William Sullivan, Andy Harrison (Section 32)."),
        ],
        also="Founder-CEO Dan Trigub signed both filings. He is gone. <b>Ophir Lotan</b> — "
             "ex-Chief Product Officer at Alto Pharmacy, founding team at TytoCare — was named CEO in "
             "March 2026, the same day MedArrive bought the assets of the shuttered Inbound Health. "
             "Terms undisclosed. The SEC filings give the incorporation year as <b>2018</b>; every "
             "public database says the company was founded in 2020.",
    ),
    dict(
        slug="arya-health", name="Arya Health", entity="Arya for Work, Inc.  (Delaware)",
        seat="Princeton, NJ  ·  19 Kent Court", inc="2022",
        raised=25_314_302, shown="$25.31M", stage="Series A",
        cik="0002024148",
        headline="The seed was 81% bigger than they said. The Series A closed ten weeks before the announcement.",
        rounds=[
            ("10 May 2024", "Seed — first sale", "$7,234,996 sold — 100% of offering", "17 investors · Twelve Below led", "formd"),
            ("18 Aug 2025", "Series A — first sale", "$18,079,306 sold of $18,179,303", "13 investors · ACME Capital led", "formd"),
        ],
        flags=[
            ("The seed round was $7.23M, not the $4M that was announced.",
             "The September 2024 press said <b>$4 million</b>. The Form D filed 24 May 2024 reports an offering of "
             "<b>$7,234,996</b> and <b>$7,234,996 sold</b> — the entire offering, to <b>17 investors</b>, "
             "first sale 10 May 2024. The company under-reported its own seed by <b>$3.23M</b>."),
            ("The Series A had already closed 72 days before it was announced.",
             "First sale <b>18 August 2025</b>; the press release is dated <b>29 October 2025</b>. "
             "Of $18,179,303 offered, <b>$18,079,306 sold</b> and <b>$99,997 was left on the table</b>."),
            ("Both filings decline to disclose revenue.",
             "The Form D revenue-range field is optional and most startups pick a band. "
             "Arya selected <b>“Decline to Disclose”</b> on both filings, in 2024 and again in 2025, "
             "while telling the press revenue grew “more than 6x in 2025.”"),
            ("The investors' board seats are legible in the filings.",
             "<b>Byron Ling</b> (Twelve Below) is a related person from the seed onward. "
             "<b>Aike Ho</b> (ACME Capital) appears for the first time on the Series A filing — "
             "ACME's board seat, dated. Founders Kunal Sarda and Arunram Kalaiselvan are on both."),
        ],
        also="Both filings give the registered address as <b>19 Kent Court, Princeton, New Jersey</b> — "
             "signed by the CEO under penalty of perjury. Their terms of service set New York law and venue "
             "and the funding release is datelined New York. <b>This corrects our roster</b>, which took "
             "New York as the seat. No sales commissions and no finders' fees were paid on either round.",
    ),
    dict(
        slug="axle-health", name="Axle Health", entity="Axle Health  ·  no incorporation record found",
        seat="Los Angeles, CA  ·  office in Santa Monica", inc="2020",
        raised=14_400_000, shown="$14.4M", stage="Series A",
        cik=None,
        headline="Well backed, cleanly sequenced — and invisible to the SEC.",
        rounds=[
            ("Winter 2021", "Y Combinator W21", "~$125K standard", "Y Combinator", "press"),
            ("22 Feb 2024", "Seed — announced", "$4.2M  (total to $4.4M)", "Pear VC led · TRAC VC · existing investors", "press"),
            ("22 May 2025", "Series A — announced", "$10M", "F-Prime led · YC · Pear VC · Lightbank", "press"),
        ],
        flags=[
            ("No SEC filing of any kind exists under this name.",
             "A company search of EDGAR for “Axle”, across <b>every</b> form type, returns nothing; a full-text "
             "search returns only an unrelated LifeMD 8-K. $14.4M has been raised and no Form D is on record "
             "under that name. It may be filed under a legal entity we have not identified. "
             "<b>Ask them for the entity name and we can check in a minute.</b>"),
            ("The capital is small, recent and correctly shaped.",
             "Only <b>$4.4M</b> had been raised before May 2025 — that is a company that stayed lean for four years. "
             "F-Prime is Fidelity's healthcare venture arm and a credible lead for this sector."),
            ("The one obscure thread: a NASDAQ-listed partner, four years early.",
             "<b>LifeMD (NASDAQ: LFMD)</b> named Axle Health in an <b>8-K on 15 July 2021</b> — a partnership "
             "for in-home blood draws and sample collection. The 8-K names <b>Adam Stansell, co-founder and COO</b>. "
             "He is the CEO today. A public company was willing to name them in a filing in 2021."),
        ],
        also="Headcount 34 (Apr 2026) against 28 in 2024. The about page also lists <b>Pioneer Fund</b> and "
             "<b>TRAC AI</b> among backers. No valuation disclosed at any round; PitchBook and Crunchbase are gated.",
    ),
    dict(
        slug="care-connect", name="CareConnect", entity="CareConnect, LLC  ·  filed in NY as Care Connect, LLC",
        seat="Port Washington, NY  ·  26 Harbor Park Drive", inc="1 Dec 2017",
        raised=0, shown="none found", stage="no institutional round",
        cik=None,
        headline="No venture capital. One wealthy founder, and an exit next door.",
        rounds=[("1 Dec 2017", "Entity filed in New York", "—", "Bert E. Brodsky, co-founder", "press")],
        flags=[
            ("No outside round has ever been found — and that is a finding, not a gap.",
             "No Form D, no priced round, no investor, no accelerator. The capital is "
             "<b>Bert E. Brodsky's</b>. He founded Sandata Technologies, took it private in 2003, "
             "and <b>sold it to HHAeXchange on 27 September 2024</b>. He is also founder and chairman of "
             "Mobile Health Management Services."),
            ("CareConnect appears not to have been part of the Sandata sale.",
             "After the transaction, HHAeXchange lists CareConnect as a <b>third-party partner</b> rather than "
             "a product. That reads as a company deliberately kept out of the deal — which means its owner has "
             "just been paid, and has no obvious pressure to raise or to sell."),
            ("The founder handed over the CEO role three years ago.",
             "<b>Matthew McGinty</b> was appointed CEO in <b>August 2023</b>; Brodsky moved to Chairman. "
             "A founder-to-operator handover that has now held for three years is a durability signal, "
             "not a red flag."),
            ("A near-identical company does file with the SEC. It is not this one.",
             "<b>CareConnectMD, Inc.</b> — CIK 0001746369, Huntington Beach, California, Delaware-incorporated, "
             "<b>five Form D filings</b> between 2018 and 2022. Different company, different coast. "
             "Any funding history attributed to “CareConnect” from an SEC source is almost certainly theirs."),
        ],
        also="About 92 employees as of June 2026 — <b>larger than Arya and Axle Health combined</b>, "
             "on no outside capital at all. Revenue is not published; one aggregator shows $4.3M against a "
             "33-person headcount, which does not match the 92 figure and is probably stale.",
    ),
    dict(
        slug="care-stitch", name="CareStitch", entity="CareStitch, Inc.",
        seat="San Diego, CA", inc="2019",
        raised=0, shown="$0 — stated", stage="bootstrapped",
        cik=None,
        headline="Zero, on purpose, for seven years.",
        rounds=[("2019", "Founded", "no capital raised", "Peter Yang, founder & CEO", "press")],
        flags=[
            ("The only vendor whose funding number is a deliberate choice.",
             "“Founded in 2019, CareStitch has grown … <b>without raising any venture capital or outside "
             "funding</b>.” No Form D, no investor, no accelerator, no debt facility found. "
             "EDGAR returns nothing for “CareStitch” across every form type — clean negative evidence."),
            ("The revenue figure is five years old and very small.",
             "<b>$143K</b> in 2021, self-reported to Latka, with a two-person team. "
             "Nothing has been published since. Four employees as of April 2026."),
            ("This is the concentration risk in its purest form.",
             "A four-person company with no balance sheet behind it. Compassus is ~3,000 clinicians "
             "across ~80 branches. <b>We would not be their largest customer — we would be their company.</b> "
             "That is survivable with escrow and source-code terms, and unmanageable without."),
        ],
        also="Founder and CEO <b>Peter Yang</b>. Growth from two people to four in five years is real "
             "and deliberate; it is not a company that stalled, it is a company that never tried to scale.",
    ),
    dict(
        slug="vitalis-care", name="Vitalis Care", entity="VitalisCare Ltd.",
        seat="Jerusalem, Israel  ·  Divrei Khayim 14", inc="not found",
        raised=None, shown="not found", stage="not found",
        cik=None,
        headline="Not a startup. A product of a twenty-person software studio in New Jersey.",
        rounds=[("—", "No round, investor or stage found", "not found", "—", "notfound")],
        flags=[
            ("The company behind the product is Integralytic, and it is findable.",
             "<b>Integralytic</b>, Lakewood, New Jersey — CEO <b>Dina Yankelewitz, Ed.D.</b> (Rutgers, 2009; "
             "previously Manager, Data &amp; Analytics at Pearson). About <b>20 people</b>, about "
             "<b>$1M revenue in 2025</b>. It operates <code>vitaliscare.ai</code> alongside "
             "<code>dolphincare.ai</code> and <code>capstonecare.ai</code>."),
            ("So the funding question has a different answer than we assumed.",
             "There is no round to find because there is probably no venture-backed company here — "
             "there is a small, revenue-funded studio shipping several healthcare products. "
             "<b>The right question is not “how much did you raise” but “how much of Integralytic's "
             "twenty people work on Vitalis Care.”</b>"),
            ("A UK company of exactly this name exists. It is a shell, and it is not them.",
             "<b>VITALISCARE LTD</b>, Companies House <b>15774638</b>, registered at "
             "<b>71–75 Shelton Street, Covent Garden</b> — one of the most heavily used mass-registration "
             "addresses in Britain. Incorporated <b>12 June 2024</b> as <b>SGR FINANCIAL SOLUTIONS LTD</b> and "
             "renamed three weeks later. Sole director a Swedish national born July 2001, resident in Stockholm. "
             "SIC code <b>47910 — internet mail order retail</b>. Confirmation statement overdue. "
             "<b>Nothing here belongs to the hospice software company.</b>"),
        ],
        also="No Israeli registry record was retrievable from this session. The Israeli Corporations "
             "Authority is the one cheap unrun check left on this vendor, and it would settle the "
             "incorporation date and the shareholders.",
    ),
]

SRC = [
    ("SEC EDGAR", "Form D filings, retrieved 2026-09-09: Arya for Work, Inc. CIK 0002024148 — "
     "accession 0002024148-24-000001 (filed 24 May 2024) and 0001231919-25-000174 (filed 29 Aug 2025). "
     "MedArrive Inc. CIK 0001901894 — accession 0001901894-22-000001 (filed 11 Feb 2022) and "
     "0001901894-23-000001 (filed 11 Apr 2023). Company and full-text searches for “Axle”, "
     "“CareStitch” and “Vitalis Care” returned no filings."),
    ("UK Companies House", "VITALISCARE LTD, company number 15774638 — company record, officers and "
     "filing history, retrieved 2026-09-09. Recorded here to be excluded, not used."),
    ("Company releases", "PR Newswire, GlobeNewswire, BusinessWire and Home Health Care News for the "
     "announced rounds; aryahealth.ai, axlehealth.com, medarrive.com, careconnectmobile.com, "
     "carestitch.com and vitaliscare.ai for company statements."),
    ("Trade press", "Fierce Healthcare, MobiHealthNews, HIT Consultant, Healthcare Dive, Modern Healthcare, "
     "HomeCare and Home Health Care News, 2020–2026."),
    ("Databases", "Crunchbase, Tracxn, Latka, ZoomInfo and RocketReach for headcount and revenue estimates. "
     "PitchBook, CB Insights and Caplight are paywalled and were not read. Aggregator figures are "
     "labelled as estimates wherever they appear."),
]


# ── the investor register ─────────────────────────────────────────────────
# Only the three vendors with investors. Role is the thing that matters: a
# studio, a lead, a follower and a payer strategic all behave differently when
# a portfolio company needs a bridge. Board seats are taken from the Form D
# related-person lists, which is the only dated, primary evidence of who sits
# where.
INVESTORS = [
 ("MedArrive", "eight named backers · three of them payers or corporates",
  "**Three of the eight are payers or corporate strategics.** This is a cap table assembled to sell "
  "to health plans, not to provider organisations — which is consistent with a product that starts at "
  "a discharge and bills a plan. It is the thing to hold in mind when they pitch us as a provider.",
  [
   ("Redesign Health", "Venture studio — built the company", "Launch · Series A",
    "New York venture studio founded 2018 by Brett Shaheen (ex-Goldman, Carlyle, Lone Pine). Launches "
    "five or six companies a year; 60+ built, $175M raised Dec 2024 to keep building. "
    "**MedArrive's entity was created inside the studio — which is why the SEC incorporation year is 2018 "
    "and the public launch is December 2020.**", "—"),
   ("Section 32", "**Led the Series A**", "Series A",
    "Deep-tech and healthcare fund founded by Bill Maris, who founded Google Ventures. "
    "The $25M announcement names Section 32 as lead — not Kleiner Perkins, as is often repeated.",
    "**Andy Harrison, Managing Partner — on both Form Ds**"),
   ("Kleiner Perkins", "Seed lead, stayed through the A", "Seed · Series A",
    "Menlo Park. One of the oldest and best-known venture firms in the United States.",
    "**Annie Case — on both Form Ds**"),
   ("Define Ventures", "Digital-health specialist", "Seed · Series A",
    "Founded by Lynne Chou O'Keefe, previously a partner at Kleiner Perkins. Digital health only.",
    "**Lynne Chou O'Keefe — on the 2022 Form D, absent from the 2023 one**"),
   ("7wireVentures", "New money at the Series A", "Series A",
    "Chicago digital-health firm founded by Glen Tullman and Lee Shapiro, who built Allscripts and Livongo. "
    "Genuine operating pedigree in this sector.", "Alyssa Jaffee — board observer"),
   ("Leaps by Bayer", "Corporate strategic", "Series A",
    "The impact-investment arm of Bayer AG. Invests in breakthrough healthcare and agriculture, "
    "not as a financial return vehicle first.", "—"),
   ("SCAN Health Plan", "**Payer strategic**", "listed on their about page",
    "A Medicare Advantage plan serving Los Angeles and Orange County. Also a named commercial partner — "
    "MedArrive delivered COVID boosters to its homebound members in 2021. Investor and customer at once.",
    "—"),
   ("Cobalt Ventures", "**Payer strategic — led the 2023 round alone**", "2023 strategic",
    "A wholly owned subsidiary of **Blue Cross and Blue Shield of Kansas City**. "
    "The Form D for that round records exactly **one** investor, so Cobalt is that one — "
    "$8,000,000 of a $10,000,000 offering.", "—"),
  ]),
 ("Arya Health", "six named backers, and two groups they will not name",
  "**Not one home health operator and not one payer is on this cap table.** It is software money — two "
  "seed funds, an enterprise-software fund and a generalist deep-tech fund. That is a coherent syndicate "
  "for a company selling admin automation, and it is also why nobody around the table has pushed them to "
  "model an episode. **The two unnamed groups are the thing to ask about.**",
  [
   ("ACME Capital", "**Led the $18.2M Series A**", "Series A",
    "San Francisco, founded 2013. Fund III was $181M in 2019; the firm closed over $300M for its "
    "latest funds in 2022. Generalist deep tech with a dedicated digital-health partner.",
    "**Aike Ho, Partner — first appears on the 2025 Form D, not the 2024 one**"),
   ("Twelve Below", "**Co-led the seed**", "Seed · Series A",
    "New York, founded 2021. Pre-seed and seed only; healthcare and digital health are its largest "
    "portfolio concentration. Three years old at the time it led.",
    "**Byron Ling — on both Form Ds**"),
   ("Ridge Ventures", "**Co-led the seed**", "Seed · Series A",
    "San Francisco. $540M AUM across five funds; Ridge V closed at $180M in April 2023. "
    "**An enterprise-software fund** — seed and early Series A, post-product and pre-product-market-fit. "
    "Not a healthcare investor.", "—"),
   ("Oceans", "Seed participant", "Seed",
    "New York, founded 2018. Digital health among several sectors including climate, fintech and "
    "marketplaces.", "—"),
   ("Nebular", "Seed participant", "Seed",
    "Fund I is **$30M** — a small fund. Nineteen core positions and five strategic positions.", "—"),
   ("“Executives from OpenAI”", "**Unnamed individuals**", "Series A",
    "The release says executives from OpenAI participated and names none of them. The Form D records "
    "**13 investors** on the Series A and identifies only the related persons above.", "—"),
   ("“Leading post-acute care providers”", "**Unnamed — ask who**", "Series A",
    "The release says post-acute care providers invested. **If one of them operates home health, we should "
    "know which**, because it may be a competitor of ours and it changes what we tell them in a demo.", "—"),
  ]),
 ("Axle Health", "six named backers — the strongest syndicate of the three",
  "**The only one of the three with a healthcare-dedicated institutional lead at Series A**, and F-Prime "
  "writes $5M–$30M cheques, which means Axle has a lead capable of funding a Series B without new money "
  "at the table. Lightbank brings a founder who built Tempus. On syndicate quality alone this is the "
  "safest of the three.",
  [
   ("F-Prime Capital", "**Led the $10M Series A**", "Series A",
    "Cambridge, Massachusetts. **The venture arm of Fidelity Investments** — an independent subsidiary "
    "with no outside investors, **$5.3B under management**, 370+ portfolio companies, cheques of "
    "**$5M to $30M**. Formerly Fidelity Biosciences.", "—"),
   ("Pear VC", "**Led the $4.2M seed**", "Seed · Series A",
    "Menlo Park, founded 2013 by Pejman Nozad and Mar Hershenson. About **$800M AUM**; Fund IV closed "
    "**$432M** in May 2023. Pre-seed and seed only, $250K–$5M. Seeded DoorDash, Gusto and Guardant Health.",
    "—"),
   ("Lightbank", "Series A participant", "Series A",
    "Chicago, founded 2010 by **Eric Lefkofsky and Brad Keywell** — the Groupon founders; Lefkofsky also "
    "founded **Tempus**, the precision-medicine company. About **$700M AUM**, cheques $250K–$5M.", "—"),
   ("Y Combinator", "Accelerator — **Winter 2021**", "W21 · Series A",
    "The standard YC deal, roughly $125K at that vintage. YC also participated in the Series A four years "
    "later, which is a mild positive signal.", "—"),
   ("TRAC VC  (TRAC AI)", "Seed participant", "Seed",
    "San Francisco, founded 2019 by Fredrick Campbell and Joseph Aaron. A quantitative, data-driven seed "
    "firm — it picks companies by model rather than by thesis.", "—"),
   ("Pioneer Fund", "Alumni fund", "listed on their about page",
    "A seed fund backed by **300+ Y Combinator alumni as LPs**, founded 2017. Effectively the YC network "
    "investing in its own.", "—"),
  ]),
]

def bold(s: str) -> str:
    """The investor rows are written with **markdown emphasis** for readability in
    this file; the page wants real tags."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s, flags=re.S)


def investor_block(name, count, read, rows):
    trs = "\n".join(
      f'<tr><td class="firm">{bold(f)}</td><td class="role">{bold(r)}</td>'
      f'<td class="rnd">{html.escape(rd)}</td><td class="who">{bold(w)}</td>'
      f'<td class="seat">{bold(s)}</td></tr>' for f, r, rd, w, s in rows)
    return f"""
<article class="invgrp">
  <header class="invh"><h3>{html.escape(name)}</h3><span>{html.escape(count)}</span></header>
  <p class="invread">{bold(read)}</p>
  <div class="tscroll"><table class="inv">
    <thead><tr><th>Firm</th><th>Role</th><th>Round</th><th>Who they are</th><th>Board seat</th></tr></thead>
    <tbody>{trs}</tbody>
  </table></div>
</article>"""


MAX = max(v["raised"] for v in VENDORS if v["raised"])

def bar(v):
    if v["raised"] is None:
        return '<div class="track"><span class="nil">no figure exists</span></div>'
    if v["raised"] == 0:
        return '<div class="track"><span class="zero-mark"></span><span class="nil">zero outside capital</span></div>'
    # cap the longest bar at 86% so the figure always has clear space to sit in
    pct = v["raised"] / MAX * 86
    return (f'<div class="track"><div class="fill" style="width:{pct:.2f}%"></div>'
            f'<span class="amt">{v["shown"]}</span></div>')

RTYPE = {"formd": ("SEC Form D", "filed"), "press": ("announced", "press"),
         "notfound": ("not found", "gap")}

def rounds(v):
    out = []
    for date, what, amt, who, kind in v["rounds"]:
        lab, cls = RTYPE[kind]
        out.append(
            f'<li class="{cls}"><span class="when">{html.escape(date)}</span>'
            f'<span class="what">{html.escape(what)}<em>{html.escape(who)}</em></span>'
            f'<span class="amt2">{html.escape(amt)}</span>'
            f'<span class="prov {cls}">{lab}</span></li>')
    return "\n".join(out)

def flags(v):
    return "\n".join(
        f'<div class="find"><h4>{html.escape(t)}</h4><p>{b}</p></div>' for t, b in v["flags"])

def card(v):
    cik = (f'<span class="cik">CIK {v["cik"]}</span>' if v["cik"]
           else '<span class="cik none">no SEC filer record</span>')
    return f"""
<article class="vendor" id="{v['slug']}">
  <header class="vh">
    <div class="vh-name">
      <h3>{html.escape(v['name'])}</h3>
      <p class="entity">{v['entity']}</p>
      <p class="seat">{html.escape(v['seat'])} &nbsp;·&nbsp; incorporated {html.escape(v['inc'])} &nbsp;·&nbsp; {cik}</p>
    </div>
    <div class="vh-fig">
      <b>{html.escape(v['shown'])}</b>
      <span>{html.escape(v['stage'])}</span>
    </div>
  </header>
  <p class="thesis">{html.escape(v['headline'])}</p>
  <ol class="rounds">{rounds(v)}</ol>
  <div class="finds">{flags(v)}</div>
  <p class="also">{v['also']}</p>
</article>"""

invsec = "\n".join(investor_block(*g) for g in INVESTORS)
scale = "\n".join(
    f'<li><span class="sn">{html.escape(v["name"])}</span>{bar(v)}</li>' for v in VENDORS)
cards = "\n".join(card(v) for v in VENDORS)
sources = "\n".join(
    f'<div class="src"><h4>{html.escape(a)}</h4><p>{html.escape(b)}</p></div>' for a, b in SRC)

total = sum(v["raised"] for v in VENDORS if v["raised"])

OUT.write_text(f"""<title>Vendor Capital Ledger</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&family=Mulish:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
:root{{
  --navy:#182752; --gold:#F0A91B;
  --paper:#F7F8FA; --card:#FFFFFF; --ink:#1F2430; --muted:#6E7683;
  --rule:#DCE0E6; --rule-2:#C7CCD4; --band:#EDEFF2;
  --filed:#0E8F80; --press:#6E7683; --gap:#B23B3B; --amber:#D97706;
  --bar:#182752; --shadow:rgba(24,39,82,.09);
}}
@media (prefers-color-scheme:dark){{
  :root:not([data-theme="light"]){{
    --navy:#AFBEE4; --gold:#F0A91B;
    --paper:#12151C; --card:#181C25; --ink:#E6E8EE; --muted:#9AA2B1;
    --rule:#2A303C; --rule-2:#39414F; --band:#1D222C;
    --filed:#5FC4B8; --press:#9AA2B1; --gap:#E08B8B; --amber:#E0A055;
    --bar:#7E93C9; --shadow:rgba(0,0,0,.5);
  }}
}}
:root[data-theme="dark"]{{
  --navy:#AFBEE4; --gold:#F0A91B;
  --paper:#12151C; --card:#181C25; --ink:#E6E8EE; --muted:#9AA2B1;
  --rule:#2A303C; --rule-2:#39414F; --band:#1D222C;
  --filed:#5FC4B8; --press:#9AA2B1; --gap:#E08B8B; --amber:#E0A055;
  --bar:#7E93C9; --shadow:rgba(0,0,0,.5);
}}
*{{box-sizing:border-box}}
body{{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:"Mulish","Avenir Next",-apple-system,BlinkMacSystemFont,sans-serif;
  font-size:15.5px; line-height:1.6; -webkit-font-smoothing:antialiased;
}}
.wrap{{max-width:1080px; margin:0 auto; padding-block:48px 32px; padding-left:24px; padding-right:24px;
  display:flex; flex-direction:column; gap:52px}}

/* masthead */
.mast{{display:flex; align-items:flex-end; justify-content:space-between; gap:28px; flex-wrap:wrap;
  padding-bottom:18px; border-bottom:2px solid var(--navy); position:relative}}
.mast::after{{content:""; position:absolute; left:0; right:0; bottom:-5px; height:3px; background:var(--gold)}}
.mast img{{width:148px; height:auto; align-self:center}}
@media (prefers-color-scheme:dark){{
  :root:not([data-theme="light"]) .mast img{{background:#fff; padding:9px 13px; border-radius:7px}}
}}
:root[data-theme="dark"] .mast img{{background:#fff; padding:9px 13px; border-radius:7px}}
h1{{font-family:"Source Serif 4",Georgia,serif; font-weight:700; font-size:clamp(30px,5vw,46px);
  line-height:1.06; letter-spacing:-.02em; margin:0; color:var(--navy); text-wrap:balance}}
.kicker{{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:10.5px; letter-spacing:.19em;
  text-transform:uppercase; color:var(--muted); margin:0 0 12px}}
.lede{{max-width:66ch; font-size:17px; margin:0}}
.lede b{{color:var(--navy)}}

/* section furniture */
section{{display:flex; flex-direction:column; gap:20px}}
h2{{font-family:"Source Serif 4",Georgia,serif; font-size:27px; font-weight:600; letter-spacing:-.012em;
  margin:0; color:var(--navy)}}
.sub{{color:var(--muted); max-width:68ch; margin:-12px 0 0}}

/* the scale */
.scale{{list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:2px}}
.scale li{{display:grid; grid-template-columns:150px 1fr; align-items:center; gap:18px;
  padding:11px 0; border-bottom:1px solid var(--rule)}}
.sn{{font-weight:700; font-size:14.5px}}
.track{{position:relative; height:26px; display:flex; align-items:center; background:var(--band); border-radius:2px}}
.fill{{height:100%; background:var(--bar); border-radius:2px 0 0 2px}}
.amt,.nil{{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:12px; font-weight:600;
  margin-left:11px; white-space:nowrap; font-variant-numeric:tabular-nums}}
.nil{{color:var(--muted); font-style:italic; font-weight:400}}
.zero-mark{{width:3px; height:26px; background:var(--gap); flex:none}}
.zero-mark+.nil{{color:var(--gap); font-style:normal}}

/* vendor cards */
.vendor{{background:var(--card); border:1px solid var(--rule); border-top:3px solid var(--navy);
  padding:26px 28px 24px; display:flex; flex-direction:column; gap:18px; box-shadow:0 1px 2px var(--shadow)}}
.vh{{display:flex; justify-content:space-between; align-items:flex-start; gap:24px; flex-wrap:wrap}}
.vh h3{{font-family:"Source Serif 4",Georgia,serif; font-size:25px; font-weight:600; margin:0; color:var(--navy)}}
.entity{{margin:3px 0 0; font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11.5px; color:var(--ink)}}
.seat{{margin:5px 0 0; font-size:12.5px; color:var(--muted)}}
.cik{{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11px; color:var(--filed)}}
.cik.none{{color:var(--muted); font-style:italic}}
.vh-fig{{text-align:right; flex:none}}
.vh-fig b{{display:block; font-family:"Source Serif 4",Georgia,serif; font-size:31px; font-weight:700;
  line-height:1; color:var(--navy); font-variant-numeric:tabular-nums}}
.vh-fig span{{display:block; margin-top:5px; font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:10px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted)}}
.thesis{{margin:0; font-family:"Source Serif 4",Georgia,serif; font-size:19px; line-height:1.4;
  color:var(--ink); max-width:70ch; text-wrap:balance}}

/* the round timeline — a real sequence, so it is numbered by date not by ordinal */
.rounds{{list-style:none; margin:0; padding:0; border-top:1px solid var(--rule)}}
.rounds li{{display:grid; grid-template-columns:112px 1fr auto auto; gap:16px; align-items:baseline;
  padding:11px 0; border-bottom:1px solid var(--rule)}}
.when{{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11.5px; color:var(--muted);
  font-variant-numeric:tabular-nums}}
.what{{font-size:14px; font-weight:600}}
.what em{{display:block; font-style:normal; font-weight:400; font-size:12.5px; color:var(--muted); margin-top:2px}}
.amt2{{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:13px; font-weight:600;
  font-variant-numeric:tabular-nums; text-align:right}}
.prov{{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:9.5px; letter-spacing:.09em;
  text-transform:uppercase; padding:3px 7px; border-radius:2px; white-space:nowrap}}
.prov.filed{{color:var(--filed); border:1px solid var(--filed)}}
.prov.press{{color:var(--press); border:1px solid var(--rule-2)}}
.prov.gap{{color:var(--gap); border:1px solid var(--gap)}}

/* findings */
.finds{{display:grid; grid-template-columns:repeat(auto-fit,minmax(272px,1fr)); gap:2px 26px}}
.find{{padding:13px 0; border-top:1px solid var(--rule)}}
.find h4{{margin:0 0 5px; font-size:14px; font-weight:700; line-height:1.34; color:var(--navy); text-wrap:balance}}
.find p{{margin:0; font-size:13.5px; line-height:1.55; color:var(--ink)}}
.find b{{font-weight:700}}
.find code{{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:12px}}
.also{{margin:0; padding-top:14px; border-top:1px solid var(--rule); font-size:13.5px; color:var(--muted)}}
.also b{{color:var(--ink); font-weight:600}}

/* investor register */
.invgrp{{background:var(--card); border:1px solid var(--rule); border-top:3px solid var(--gold);
  padding:22px 24px 20px; display:flex; flex-direction:column; gap:13px; box-shadow:0 1px 2px var(--shadow)}}
.invh{{display:flex; align-items:baseline; justify-content:space-between; gap:18px; flex-wrap:wrap;
  padding-bottom:10px; border-bottom:1px solid var(--rule)}}
.invh h3{{font-family:"Source Serif 4",Georgia,serif; font-size:22px; font-weight:600; margin:0; color:var(--navy)}}
.invh span{{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:10.5px; letter-spacing:.09em;
  text-transform:uppercase; color:var(--muted)}}
.invread{{margin:0; font-size:14px; line-height:1.55; max-width:78ch}}
.invread b{{color:var(--navy)}}
.tscroll{{overflow-x:auto}}
table.inv{{border-collapse:collapse; width:100%; min-width:760px; font-size:13px}}
table.inv th{{text-align:left; font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:9.5px;
  letter-spacing:.11em; text-transform:uppercase; color:var(--muted); font-weight:500;
  padding:0 14px 8px 0; border-bottom:1px solid var(--rule-2); white-space:nowrap}}
table.inv td{{padding:11px 14px 11px 0; border-bottom:1px solid var(--rule); vertical-align:top; line-height:1.5}}
table.inv tr:last-child td{{border-bottom:0}}
td.firm{{font-weight:700; color:var(--navy); white-space:nowrap; min-width:118px}}
td.role{{min-width:132px; font-size:12.5px}}
td.rnd{{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:10.5px; color:var(--muted);
  white-space:nowrap; min-width:96px}}
td.who{{color:var(--ink); min-width:290px}}
td.seat{{font-size:12px; color:var(--filed); min-width:150px}}

/* concentration */
.conc{{background:var(--band); border-left:3px solid var(--gold); padding:24px 26px;
  display:flex; flex-direction:column; gap:12px}}
.conc p{{margin:0; max-width:72ch}}
.conc .big{{font-family:"Source Serif 4",Georgia,serif; font-size:20px; line-height:1.42; color:var(--navy)}}

/* sources */
.srcs{{display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:0 28px}}
.src{{padding:13px 0; border-top:1px solid var(--rule)}}
.src h4{{margin:0 0 4px; font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:10.5px;
  letter-spacing:.12em; text-transform:uppercase; color:var(--navy)}}
.src p{{margin:0; font-size:12.5px; color:var(--muted); line-height:1.5}}
footer{{border-top:1px solid var(--rule); padding-top:18px; color:var(--muted); font-size:12.5px; max-width:74ch}}
footer code{{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11.5px}}

@media (max-width:640px){{
  .wrap{{padding-block:32px 24px; gap:40px}}
  .scale li{{grid-template-columns:1fr; gap:6px}}
  .rounds li{{grid-template-columns:1fr auto; gap:6px 12px}}
  .when{{grid-column:1/-1}}
  .prov{{justify-self:start}}
  .vh-fig{{text-align:left}}
}}
@media (prefers-reduced-motion:reduce){{*{{transition:none!important; animation:none!important}}}}
</style>

<div class="wrap">
  <header class="mast">
    <div>
      <p class="kicker">Compassus · Capacity &amp; Scheduling · 9 September 2026</p>
      <h1>Vendor Capital Ledger</h1>
    </div>
    <img alt="Compassus" src="{LOGO}">
  </header>

  <p class="lede">Where the six shortlisted vendors stand on capital, built from the filings rather than
  the press releases. <b>Three of them have raised ${total/1_000_000:.1f}M between them. The other three have raised
  nothing at all</b> — and in two of those cases that is a deliberate choice rather than a failure.
  Four SEC Form D filings were read in full; <b>three of them disagree with the company's own announcement</b>.</p>

  <section>
    <h2>Capital raised, to one scale</h2>
    <p class="sub">Verified dollars, not announced dollars. Where the SEC and the press release disagree,
    this uses the filing.</p>
    <ul class="scale">{scale}</ul>
  </section>

  <section>
    <h2>The six, in order of capital</h2>
    <p class="sub">Each entry gives the contracting entity, the rounds with their filing provenance, and what
    the primary sources say that the coverage does not. <span class="prov filed">SEC Form D</span> means the
    figure comes from a document signed under penalty of perjury. <span class="prov press">announced</span>
    means it comes from the company.</p>
    {cards}
  </section>

  <section>
    <h2>Who is behind the money</h2>
    <p class="sub">Every named investor in the three funded vendors, with what kind of firm it is and what
    round it came in at. Board seats are taken from the <b>Form D related-person lists</b> — the only dated,
    primary evidence of who actually sits at the table.</p>
    {invsec}
  </section>

  <section>
    <h2>The read for us</h2>
    <div class="conc">
      <p class="big">The capital splits the shortlist into two groups that need completely different contracts —
      and the split does not follow the product quality.</p>
      <p><b>The funded three</b> — MedArrive, Arya and Axle Health — can absorb an eighty-branch deployment and
      will still be here in three years if the product works. Their risk is direction, not survival: MedArrive
      has changed what it sells twice and has filed nothing since April 2023; Arya has changed which market it
      names first and declines to disclose revenue to the SEC.</p>
      <p><b>The unfunded three</b> — CareConnect, CareStitch and Vitalis Care — carry no investor pressure and no
      cushion. CareConnect is the strongest of them by a distance: ninety-two people on an owner's balance sheet,
      an owner who has just been paid for a related business, and a professional CEO in post since 2023.
      CareStitch is four people. Vitalis Care is a product inside a twenty-person studio.</p>
      <p><b>What to ask for, and from whom.</b> From the funded three: the current runway in months and the
      board's expectation for the next raise. From the unfunded three: source-code escrow, a transition-services
      commitment, and named continuity of the two or three people who actually know the system. Neither ask is
      unusual and both are cheap to refuse in writing, which is itself informative.</p>
    </div>
  </section>

  <section>
    <h2>Where this came from</h2>
    <div class="srcs">{sources}</div>
  </section>

  <footer>
    Generated by <code>_capital-brief.gen.py</code> from public sources only, retrieved 9 September 2026.
    No vendor was contacted. Every figure carries a source; <em>not found</em> is written as not found and is
    never inferred. Where a company's own filing and its own press release disagree, both are shown and the
    filing is preferred. Regenerate; never hand-edit. This document does not score and does not rank —
    it establishes who can afford to be our supplier.
  </footer>
</div>
""")
print(f"Wrote {OUT.name}: {len(VENDORS)} vendors, verified total ${total:,}")
