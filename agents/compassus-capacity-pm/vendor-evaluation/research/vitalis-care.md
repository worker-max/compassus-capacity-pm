# Vitalis Care — research dossier

Researched 2026-09-05 · sources retrieved 2026-09-05 · confidence: **medium**

*Confidence note.* Product facts are high: seven product pages were read directly and they are
unusually specific for a company this small. The HCHB relationship is high — it is claimed on
several of their own pages, it is the reason the product exists, and a named customer's job title
contains the words "HCHB operations". Company facts are **low**: no founding date, no headcount, no
funding, no investor and no corporate filing was found, and the legal entity is registered outside
the United States. Customer facts are low: one named customer. Written before reading the vendor's
return.

**Identity.** The questionnaire roster says *VitalisCare*. The company writes itself **Vitalis
Care**, two words, and its apps as *Vitalis Vantage*, *Vitalis Ray* and so on. The legal entity on
its own privacy policy is **VitalisCare Ltd., Divrei Khayim 14, Jerusalem, Israel 9447916.** The CEO
is **Dina Yankelewitz**, who is simultaneously founder and CEO of **Integralytic** (Lakewood, New
Jersey), a healthcare AI company; the relationship between the two entities is **not found** and
should be asked. Confirm the return's contact email domain is `vitaliscare.ai`. Several similarly
named US companies exist — **VitalCaring**, a real home health and hospice provider, is the
dangerous one; also Vitalis Health, VitalCare and Vitalis Healthcare at Home (Australia). None is
this company.

---

## At a glance

The machine-readable face of this dossier. `_research-matrix.gen.py` reads these rows to
build `Vendor-Research-Matrix.xlsx`; the prose below is the record. Bracketed numbers are
source ids from the *Sources* list at the foot of this file. *Not found* is a finding.

| Fact | Finding |
|---|---|
| **COMPANY** | |
| Founded · HQ | *not found* · **Jerusalem, Israel** [6] |
| Legal entity | **VitalisCare Ltd.**, Divrei Khayim 14, Jerusalem [6] |
| Ownership · raised · last round | *not found* — no round, investor, stage or valuation |
| Headcount · trend | *not found* |
| Leadership from home health | CEO from mathematics education; built “with HCHB operations experts” [4] [8] |
| Pivots or rebrands in 3 years | none found |
| Home health share of business | 0% — **hospice only** [1] [8] |
| **PRODUCT** | |
| HCHB evidence | **Claimed on their own pages, and the strongest on the roster** — “no double-entry”, an “Original HCHB schedule view”, a customer whose title is Director of HCHB operations. Still no published mechanism [1] [3] [10] |
| Other EMRs named | none — HCHB is the only one [1] [3] |
| Scheduling unit | A hospice visit in a benefit period [3] |
| Capacity | Thin — visit adequacy, missed units, a transition prediction [1] [2] |
| Scheduling | Real — weekly optimised schedules, Provider Matches [3] |
| Engagement | Absent — no patient outreach |
| Decide or advise | **Advise** — “approve, adjust, or decline with a click” [3] |
| Clinician app | Sync360 and Guide described; **no app-store listing found** |
| **CUSTOMERS** | |
| Named home health customers | none — hospice only |
| Largest known deployment | *not found* |
| Customer count | 1 named — Moments Hospice [1] |
| Impact figures with a baseline | **0 of ~7**, and two mileage figures contradict: 30% on the site, 55–65% from the CEO [1] [3] [8] |
| Independent customer voice | *not found* — the other quotes are initialled [2] |
| **TRUST AND CONTINUITY** | |
| Security attestation | HIPAA · SOC 2 Type II, claimed [1] |
| Uptime · SLA | *not found* |
| Named dependencies | AWS, Azure, Google Workspace, ClickUp, Streak, **the OpenAI API** [6] |
| Pricing signal | By patient census size, per app [1] |
| **THE READ** | |
| Confidence | medium |
| The one thing to check | Real HCHB integration, no visible corporate existence, contradicting figures. |

## One paragraph

Vitalis Care is a small, privately held company, legally registered in Jerusalem and led from the
United States, that sells **seven narrow apps that sit on top of Homecare Homebase for hospice
agencies**. It does not replace the EMR and does not try to: its pitch is that HCHB holds the data
and Vitalis makes it usable. The apps are Vantage (an end-of-life prediction model and a HOPE
dashboard), Ray (HOPE compliance and visit timelines), Sync (schedule generation with route and
mileage optimisation), Sync360 (a field mobile app), Align (documentation compliance and denial
prevention), Guide (voice-to-text bedside documentation) and Bridge (SNF–hospice payment
reconciliation). The scheduling product recommends provider matches on preferences, routing and
mileage, and the human approves, adjusts or declines — which is the operating posture Compassus has
already chosen. The company is nominated for a 2026 Hospice News product award and its CEO has
spoken on a hospice law podcast. **It is a hospice company, not a home health company**, its size
and funding are unknown, and its two published mileage-saving figures do not agree with each other.

## The company

| Fact | Finding | Source · date |
|---|---|---|
| Founded | **Not found.** No founding year on the site, in press, or in any database located. The product is recent enough that its compliance apps are built around HOPE, the hospice assessment instrument in force from October 2025, which places meaningful development in 2024–2026. | search + site, 2026-09-05 |
| Headquarters, offices | **VitalisCare Ltd., Divrei Khayim 14, Jerusalem, Israel 9447916**, per its own privacy policy. The CEO operates from the United States. The site gives no US office address. | [6] |
| Ownership and funding | **Not found.** No funding round, no investor, no stage, no valuation. Privately held is the reasonable read but is **not confirmed**. Crunchbase and PitchBook have no profile found for this entity. | search, 2026-09-05 |
| Headcount, and trend | **Not found.** No headcount anywhere. No LinkedIn company page for VitalisCare located; LinkedIn is gated in any case. Sister company **Integralytic** is reported at about **$1M annual revenue (2025)** and based in Lakewood, New Jersey, which is a size signal for the group but not for this entity. | [5] · [7] |
| Leadership | **Dina Yankelewitz, CEO.** Doctorate in **mathematics education**; former university professor; moved into "data analytics and AI way before most of the world knew about ChatGPT"; founder and CEO of **Integralytic**. She says the product was built "in partnership with hospice clinical leaders, medical directors, and **HCHB operations experts**". **No other executive is named anywhere.** No CTO, no clinical officer, no commercial officer found by name. | [4] · [5] · [8] |
| Acquisitions, mergers, pivots, rebrands | **None found.** The product surface has grown to seven apps but the market has not changed. | search, 2026-09-05 |
| Litigation, breaches, regulatory actions | **Not found.** A non-US private entity will not surface in US registries or PACER-style searches, so this absence is weaker than it looks. | search, 2026-09-05 |
| Lines of business, and the share that is home health | **One business: hospice.** Every page, every app, every quote is hospice. The compliance apps are built on HOPE and the SIA (service intensity add-on); Bridge is SNF–hospice reconciliation, which only exists in hospice. **Skilled home health share: no evidence of any. Not a single home health claim, customer or feature was found.** | [1] · [2] · [3] · [8] |

## The product

| Fact | Finding | Source · date |
|---|---|---|
| What it does, in their words | "The operating platform for hospice — keeping operations seamless so you can focus on delivering exceptional care." And, on the podcast: "Vitalis was built to solve the challenges hospices face every day — from missed units and clunky schedules to mileage fraud, billing gaps, and compliance headaches." **Seven named apps:** Vantage (end-of-life prediction model, HOPE dashboard, alerts, visit adequacy), Ray (HOPE compliance dashboard, visit timelines), **Sync** (AI-optimised schedules by route and patient preference), **Sync360** (field mobile app, route tracking, mileage monitoring), Align (documentation performance, Medicare denial prevention), Guide (voice-to-text bedside notes), Bridge (SNF–hospice reconciliation and payment tracking). | [1] · [2] · [3] · [8] |
| What it does, in a customer's words | **One named customer voice: Emma Stroup, "Director of HCHB operations", Moments Hospice.** The Ray page carries additional quotes attributed only to initials ("S.M."), including "Running reports in HCHB used to take forever, but now I can see everything quickly and accurately." **No conference talk, panel or independent interview by a customer found.** The CEO herself appeared on Husch Blackwell's *Hospice Insights* podcast on 16 Jul 2025 — an independent venue, but she is the vendor. | [1] · [2] · [8] |
| Capacity, scheduling, engagement — which arenas the public material covers | **Capacity: thin but present.** *Visit adequacy* tracking and *missed units* are capacity-adjacent, and Vantage claims to predict which patients are transitioning, which is demand forecasting of a kind. There is no capacity envelope, no productivity target, no discipline-mix planning, no staffing-to-census model. **Scheduling: real, and the closest fit of any vendor researched so far.** Sync produces "weekly optimized schedules"; *Provider Matches* factor "preferences, routing, and mileage"; the user can "approve, adjust, or decline with a click". Sync360 tracks route and mileage in the field. The unit is a hospice visit in a benefit period, not a visit in a PDGM episode — closer to ours than a shift or a clinic slot, but not ours. **Engagement: absent.** No patient outreach, no confirmation, no intake, no clinician engagement product. | [1] · [3] |
| Evidence of an HCHB integration | **The strongest of any vendor researched so far, and still a claim.** Their own pages say "Vitalis integrates directly with HCHB. No double-entry" and "no extra steps, just smooth, automatic syncing in the background". Sync offers an "Original HCHB schedule view" as an option, which is a detail a vendor without an integration would be unlikely to invent. A named customer's job title is **Director of HCHB operations**. The product's entire premise is being an HCHB overlay. **But:** no HCHB partner listing found (HCHB's own partner brochure is gated, see [10]), no joint press release, no mechanism published — no direction, no frequency, no interface named. **RF-01 still applies**, more weakly than elsewhere, and the demo should walk it. | [1] · [2] · [3] · [10] |
| Other EMR integrations named | **None.** HCHB is the only EMR named anywhere. That is a dependency as much as a strength — see Durability. | [1] · [2] · [3] |
| Agentic or automated patient outreach | **Absent.** No patient-facing capability of any kind found. Guide's voice-to-text is clinician-facing dictation, not an outbound agent. | site, 2026-09-05 |
| Clinician-facing app | **Sync360** and **Guide** are described as field apps with route tracking, mileage monitoring and bedside voice notes. **No App Store or Google Play listing was found** for Vitalis, Vitalis Care, Sync360 or Guide; the delivery channel may be web or a managed enterprise build. Ratings and review counts therefore **not found**. | search, 2026-09-05 |
| Pricing signals | "Pricing for Vitalis apps is based on your **patient census size** and specific needs; contact us for a personalized quote." Per-census pricing, priced per app. That is a modular, land-and-expand model, and it means the seven apps are seven line items. | [1] |
| Security and continuity | **"HIPAA and SOC 2 Type II compliant"** is claimed on the site. The privacy policy names its **subprocessors**, which almost no vendor does and is to their credit: **Amazon Web Services** and **Microsoft Azure** for hosting, **Google Workspace**, **ClickUp**, **Streak**, and **the OpenAI API**. **The OpenAI API as a named subprocessor for a product handling clinical data is a specific thing to ask about** — what flows to it, under what agreement, with what retention. **No uptime figure, no SLA, no status page found.** Data residency is not stated and the entity is Israeli. | [1] · [6] |

## The customers

| Fact | Finding | Source · date |
|---|---|---|
| Named home health customers, with size | **None.** No home health customer, because there is no home health product. | search, 2026-09-05 |
| Named customers, any setting | **One: Moments Hospice** (a Medicare-certified hospice serving Minnesota and, per its own material, several other states), quoted through **Emma Stroup, Director of HCHB operations**. Size not found. Every other quote is anonymous or initialled. | [1] · [9] |
| Largest known deployment | **Not found.** No customer count, no census count, no branch count anywhere. The CEO refers to "daily engagement across multiple branches", unquantified. | [1] · [8] |
| Customers lost or churned | **Not found.** | search, 2026-09-05 |
| Case studies — what was measured, period, baseline | No case study document found. Figures, all without period, baseline, agency count or method: **"30% reduction in travel time and mileage — reported by Sync users"** (Sync page); **"55 to 65%"** reduction in "actual time spent on driving and mileage" (CEO, podcast, Jul 2025); **"94% accuracy"** identifying transitioning patients (podcast); **"93% required visits performed"**, **"99% accuracy rate"**, **"75% less manual work"**, **"58% less time per patient"** (Ray page). **The mileage figure does not reconcile: 30% on the site, 55–65% from the CEO. That is RF-18 in print, before the return is even opened.** The site also uses a problem statistic — inefficient scheduling costing "up to $1.6 million per 1,000 patients" — which is not a result and should not be read as one. | [1] · [3] · [8] |

## What the outside view says about the questionnaire

Written 2026-09-05, before reading the return.

- **A1.** Expect a confident HCHB claim, and expect it to be more real than most. This product has no
  reason to exist without HCHB. The right question is not *do you integrate* but *how*: read or
  write, which direction, what latency, through which interface, and who owns the schedule when both
  systems change it. **RF-02** is the live risk here, not RF-01 — a scheduling overlay on a system of
  record is precisely the two-systems-both-owning-the-schedule failure mode. Ask for the customer who
  will confirm write-back.
- **A2.** **RF-16, both halves, and this is the headline.** Home health is not a minority of their
  business, it is none of it — they are a hospice company. And with one named customer, no headcount,
  no funding and no customer count, Compassus at roughly eighty branches and three thousand
  clinicians would almost certainly be their largest customer by a wide multiple. Expect **RF-06** on
  references: they may not have three at branch-director level.
- **A3.** Two published mileage figures that do not agree — 30% and 55–65% — plus five more
  percentages with no baseline or period. **RF-05 and RF-18 both, and cite the discrepancy by name.**
- **C6.** SOC 2 Type II and HIPAA claimed; no uptime, no SLA. **RF-07** unless the return supplies a
  figure and a commitment. Then ask the harder questions: OpenAI API as a named subprocessor, data
  residency for an Israeli entity, and where PHI physically sits.
- **D1 and D2.** The public posture is *recommend and the human accepts* — "approve, adjust, or
  decline with a click" — which matches our settled position, and the CEO says AI should be "a tool
  that services us and informs us rather than one that's in the driver's seat". **This is a point in
  their favour and should be recorded as such**, not just checked for RF-14.
- **E2 and Durability.** No funding, no headcount, no founding date, one named customer, a foreign
  legal entity and a CEO who runs a second company. **This is the weakest company-facts picture of
  any vendor researched so far.** Section E and the reference calls have to carry the whole weight.
- **Who wrote this.** A doctorate in mathematics education, a professorship, and a self-taught path
  into analytics is an unusual and genuinely interesting founder profile, and the product's
  specificity about HOPE, SIA and missed units says someone in the building knows hospice
  regulation well. Expect a return that is precise about hospice compliance and either silent or
  translated about PDGM, OASIS, LUPA and recertification.

*Second pass after reading the return: to be added below, dated.*

## Durability read — evidence only

- Founding date not found. Product built around HOPE, in force from October 2025, so the current
  surface is at most two years old.
- Capital: **no funding round, investor, stage or valuation found.** Sister company Integralytic is
  reported at about $1M revenue for 2025.
- Legal entity is **VitalisCare Ltd., Jerusalem, Israel.** No US entity was found. Contracting,
  data residency, service of process and business continuity all sit on that fact.
- The CEO is also founder and CEO of another company. Divided attention is a fact, not a verdict.
- Main business: hospice, entirely. **Single-EMR dependency: the product is an HCHB overlay and
  names no other EMR.** If HCHB changes its interface, closes it, or ships the same feature, the
  company's addressable market changes overnight. HCHB has been shipping its own AI tools since
  September 2025.
- Concentration: one named customer. Customer count not found.
- Our size against theirs: we would be a different order of magnitude on any measure we can see, and
  we cannot see most of them.
- Recognition: nominated for the **2026 Hospice News Product of the Year Award**; the CEO appeared on
  Husch Blackwell's *Hospice Insights* podcast, 16 Jul 2025. Real industry presence, small.

## Questions the research raises

For the demo or the reference call. One line each.

1. What is the corporate structure? VitalisCare Ltd. is registered in Jerusalem — is there a US entity, and who would we be contracting with?
2. What is the relationship between Vitalis Care and Integralytic, and how does the CEO split her time?
3. How many hospice customers do you have today, how many branches, and what is your total census under management?
4. **Walk the HCHB integration live.** Read or write? Which direction, what latency, what interface, since when? Show a schedule change land in HCHB.
5. When a scheduler moves a visit in HCHB and Sync has already moved it, who wins, and who is told?
6. Is the mileage saving 30% or 55–65%? Give the period, baseline and agency count for whichever it is.
7. You have no home health product. What would it take to build one, who would pay for it, and what would we be — a customer or a development partner?
8. The OpenAI API is a named subprocessor. What data reaches it, under what agreement, with what retention and what training exclusion?
9. Where does PHI physically reside, and under whose jurisdiction?
10. How many people work at Vitalis Care, and how many of them are engineers?
11. Have you raised outside capital? What is your runway?
12. Will three hospice customers take reference calls at branch-director level?
13. HCHB has been shipping its own AI tools since September 2025. What happens to Vantage and Ray if HCHB ships them?
14. Sync360 tracks mileage. Is there an app-store listing, or is it an enterprise build? What are its ratings?

## Not found

Looked for and not found, so nobody looks again (as of 2026-09-05):

- A founding date, a headcount, a funding round, an investor or a valuation.
- A US legal entity or a US office address.
- Any executive other than the CEO.
- Any home health product, feature, claim or customer.
- Any EMR other than HCHB.
- Any HCHB-side listing, joint press release, or published integration mechanism.
- A customer count, a census count or a branch count.
- An app-store listing for Sync360, Guide or any Vitalis app.
- An uptime figure, SLA or status page.
- Any patient-facing capability.
- Litigation, breaches or regulatory actions — and note that a non-US private entity would not
  surface in the US searches that were run, so this absence carries little weight.
- Pricing beyond "based on your patient census size".

## Gated

- LinkedIn company and person pages (headcount, trend, employee list).
- Crunchbase and PitchBook — no profile found for this entity, which for a company this small may
  mean it does not exist rather than that it is gated.
- Israeli corporate registry (Rasham HaChavarot), which would give the incorporation date, the
  registered officers and the filing history. **This is the single highest-value gap in this
  dossier and the first thing a session with access should pull.**
- HCHB's Recommended Partner brochure PDF — see [10].

## Sources

Retrieved 2026-09-05. "Read" means the page was opened directly this session.

1. vitaliscare.ai, home page. "The operating platform for hospice"; seven apps named and described; Moments Hospice testimonial (Emma Stroup, Director of HCHB operations); "Vitalis integrates directly with HCHB. No double-entry"; "HIPAA and SOC 2 Type II compliant"; census-based pricing. Read.
2. vitaliscare.ai/ray/. HOPE compliance dashboard; metrics 93% / 99% / 75% / 58%; initialled testimonials including the HCHB reporting quote; 2026 Hospice News Product of the Year nomination and vote solicitation. Read.
3. vitaliscare.ai/sync. Weekly optimised schedules; *Provider Matches* on preferences, routing and mileage; "approve, adjust, or decline with a click"; "Original HCHB schedule view"; "30% reduction in travel time and mileage — reported by Sync users"; the $1.6M-per-1,000-patients problem statistic. Read.
4. LinkedIn, Dina Yankelewitz profile headline (CEO, Vitalis Care). Gated; headline only.
5. ZoomInfo, "Dina Yankelewitz — Chief Executive Officer at Vitalis Care"; CB Insights and RocketReach, Integralytic (Lakewood, New Jersey; ~$1M annual revenue, 2025; Yankelewitz founder and CEO). Partially gated.
6. **vitaliscare.ai/privacy-policy.** Legal entity **VitalisCare Ltd., Divrei Khayim 14, Jerusalem, Israel 9447916**; subprocessors AWS, Microsoft Azure, Google Workspace, ClickUp, Streak, **OpenAI API**; site "Powered By nextbracket.io". Read. **The most informative single page on this company.**
7. Integralytic company profiles (LinkedIn, ZoomInfo, RocketReach, CB Insights). Gated or thin.
8. Husch Blackwell, *Hospice Insights: The Law and Beyond*, "AI in Action: Exploring How AI Is Helping Hospices Do Things in New Ways", with Meg Pekarske and Dina Yankelewitz, **16 Jul 2025**; also on JD Supra and Apple Podcasts. Source of the founder's background, the 55–65% mileage figure, the 94% transition-accuracy figure, and the "not in the driver's seat" position on AI. Read.
9. Moments Hospice, agency material (Medicare-certified hospice, Minnesota and other states). Used only to size the one named customer; size not established.
10. hchb.com, "HCHB Recommended Partner Solutions" brochure PDF (2025.10, HubSpot-hosted). Downloaded; **not readable** — a Figma export with no extractable text layer, over the fetch size limit. **Gated.** Whether Vitalis appears on HCHB's own partner list is therefore unresolved.
11. RamaOnHealthcare, "Transparency 'Front, Center' for AI in Hospice", 2026, and Hospice News coverage referencing the product award nomination. Indexed.
