# Vendor roster

**Version 1 · 2026-09-05.** Six vendors named by the PM; more to come.

This file fixes the slug and the identity of every vendor before anyone researches one. It exists
because *Care Connect* matched five companies and cost a research session an hour. Nobody researches
a vendor until it has a row here.

**Slug rule.** The company's own spelling, lowercased, hyphenated at the word breaks the company's
own capitalisation shows. `UnityAI` → `unity-ai`. `CareConnect` → `care-connect`. `AutoMynd` →
`auto-mynd`. The dossier is `research/<slug>.md`. Slugs are never renamed; if a company rebrands,
the row records the new name and the slug stays.

**Identity rule.** Every row pins one legal entity and one website. The PM confirms the pin against
the contact email domain on the vendor's questionnaire return **before** the dossier is used to
inform a mark. If the domain does not match, stop and say so.

---

## The roster

| # | As the PM named it | Their own spelling | Slug | Site | Dossier |
|---|---|---|---|---|---|
| 1 | Unity AI | UnityAI | `unity-ai` | unityai.co | written · high |
| 2 | Care Connect | CareConnect | `care-connect` | careconnectmobile.com | written · high |
| 3 | Servis.ai | servis.ai | `servis-ai` | servis.ai | written · medium |
| 4 | VitalisCare | Vitalis Care | `vitalis-care` | vitaliscare.ai | written · medium |
| 5 | AutoMynd | AutoMynd | `auto-mynd` | automynd.com | written · medium |
| 6 | Carestitch | CareStitch | `care-stitch` | carestitch.com | written · medium |

More to come. Add a row before researching, not after.

## Identity pins

| Slug | Legal entity | Address on record | Confirm the return's email domain is |
|---|---|---|---|
| `unity-ai` | UnityAI, Inc. | Nashville, Tennessee | `unityai.co` |
| `care-connect` | CareConnect, LLC (filed in New York as *Care Connect, LLC*, 1 Dec 2017) | 26 Harbor Park Drive, Port Washington, NY 11050 | `careconnectmobile.com` |
| `servis-ai` | servis.ai, formerly **FreeAgent CRM** (FreeAgent Network, Inc.) | Campbell, California; development office Aguascalientes, Mexico | `servis.ai` (a `freeagentcrm.com` domain is the same company) |
| `vitalis-care` | **VitalisCare Ltd.** | Divrei Khayim 14, Jerusalem, Israel 9447916 | `vitaliscare.ai` |
| `auto-mynd` | AutoMynd | Reston, Virginia | `automynd.com` |
| `care-stitch` | CareStitch, Inc. | San Diego, California | `carestitch.com` |

## Names that are not these vendors

Written down so nobody researches the wrong company twice.

- **Unity AI** — not Unity Software Inc. (games), not Unity Health (South African insurer). Every
  litigation search returns the games company.
- **Care Connect** — not CareConnect Inc. (careconnectinc.com, an AI consultancy for adult day
  health centres), not Netsmart's CareConnect interoperability product, not the defunct Northwell
  health plan, not the dozen local home care agencies of that name, and **not the Corilus
  CareConnect general-practice software in Belgium**, which is what the StatusGator outage page
  tracks. See `care-connect.md` §Second pass.
- **Servis.ai** — not Servis (appliances), not ServiceTitan, not Service.ai. The company answers to
  both *servis.ai* and *FreeAgent CRM*; review-site listings are still filed under *FreeAgent
  Network*.
- **VitalisCare** — not VitalCaring (a US home health and hospice provider), not Vitalis Health,
  not VitalCare, not Vitals Global Healthcare, not Vitalis Healthcare at Home (Australia).
  The name is close enough to a large US provider that a mis-search is likely.
- **AutoMynd** — no close collisions found.
- **Carestitch** — no close collisions found. CareStar and Caremark are unrelated.

## What each one is, in one line

| Slug | In one line | Arena it actually plays in | Scheduling unit |
|---|---|---|---|
| `unity-ai` | Voice AI agents for the front office of multi-site outpatient clinics | Engagement, real; scheduling clinic-shaped | A clinic appointment slot |
| `care-connect` | Caregiver workforce platform for home care aide agencies | Caregiver engagement and shift fill | An hourly shift on a case |
| `servis-ai` | A general business-operations platform (a rebranded CRM) with a healthcare landing page | None of the three, natively | A field rep's visit on a route |
| `vitalis-care` | Seven small apps bolted onto HCHB for **hospice** operations, one of which schedules | Scheduling and compliance, hospice-shaped | A hospice visit in a benefit period |
| `auto-mynd` | An AI-first home health **EMR** — a replacement for the system of record, not a partner to it | Documentation first; scheduling claimed | A visit in an episode |
| `care-stitch` | A four-person San Diego company selling home health scheduling and dispatch | Scheduling, correctly shaped; capacity thin | A visit in an episode |

## The one thing to check on each

| Slug | Read this first |
|---|---|
| `unity-ai` | They have never had a home health customer. Zero, not few. |
| `care-connect` | Their site now claims an HCHB integration with no mechanism and no HCHB-side listing. |
| `servis-ai` | The product is a CRM. The scheduler moves *reps* to *customers*; there is no episode, discipline or authorization in the data model. |
| `vitalis-care` | Real HCHB integration, real hospice customers, an Israeli company of unknown size — and the mileage saving is 30% on one page and 55–65% on another. |
| `auto-mynd` | Unfunded, under ten people, but the only vendor so far with home health clinicians on staff and a founder out of Bayada operations. It wants to replace HCHB. |
| `care-stitch` | Four employees. We would be their largest customer by an order of magnitude, and it would not be close. |

---

*Maintained by the research sessions. Add a vendor here before researching it, and update the
dossier column when a dossier lands.*
