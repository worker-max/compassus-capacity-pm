# Rubric Review and Process Findings

A review of the v3.0 scorecard as a working instrument, conducted 2026-09-14 against the eleven scored
returns. **What the rubric gets right, where it leaks, and the field-wide blind spots it exposed.**

## What the rubric gets right

Worth stating, because these are design choices other evaluations get wrong:

1. **The questionnaire is the rubric.** Every question has a row, in form order. There is no translation
   layer between what was asked and what gets scored, which is why the notes columns are usable as
   evidence rather than as opinion.
2. **Section grades are the product; the total is a sort key.** Stated explicitly on the Start Here tab.
   This is what lets judgment override arithmetic legitimately.
3. **"Where Section C contradicts Section B, believe Section C."** A blanket in-scope claim in the
   self-assessment cannot survive a thin mechanism answer. It caught real overclaiming — AutoMynd most
   obviously.
4. **Conditional is orthogonal to the band.** Integration not live shows as Conditional whatever the
   total, so a strong product cannot hide a missing integration behind a good score.
5. **Intangibles carry no points and are allowed to disagree** — *"if this section never disagrees with
   the numbers, it is not doing anything"* — with a written bias guard requiring a reason and initials.
6. **Scoring 4 on sophistication is not automatically good.** "Runs it" sits above the Assist boundary
   Compassus has set for assignment and coverage, so the top mark can signal overreach. The rubric
   scores capability; the reader supplies the judgment.

## The five structural findings

### 1. Stop-checks have no enforcement point
The rule is explicit — *"resolved before advancing, not traded against points."* **Two vendors advanced
with stop-checks open:** MedArrive (A2, zero home health customers; A3, impact from a different business)
and HCHB (C6, no uptime figure or contractual commitment). Nothing in the Questions tab reserves a place
to settle them either.

**Fix:** a stop-check resolution row above Section A on the Questions tab, so the first thing a demo
settles is the thing that was supposed to block it. Otherwise the rule is decoration.

### 2. Home health fluency does gate work while carrying zero points
CareConnect (64) was excluded for home health fluency and client base — a legitimate call, and the right
kind of call for this rubric to permit. But **the sheet scored that same read as Neutral, not Concern,
and marked their durability Strong.** The factor that actually decided the outcome sits in a section
worth nothing and reads mild.

**Fix, recommended:** promote it to a stop-check — *"HH client base or demonstrated HH fluency;
stop-check if neither."* It is the one thing in this process a demo cannot manufacture. The alternative
is to accept that the total will keep disagreeing with the shortlist.

### 3. The shortlist needs its exceptions written down
CareConnect at 64 is out; MedArrive at 48 with a Decline band and two open stop-checks is in. Both
decisions are defensible. **Neither is recorded anywhere in the workbook.**

The reasoning as stated by the initiative lead:
- **CareConnect out** — majority home care client base, ~15% home health, no named home health clients,
  much of the Compassus requirement at spec level. Home care scheduling is largely set days and times;
  home health is dynamic. Their concepts need upgrading from home care.
- **MedArrive in** — the engine is real and proven at scale in home-based care, and they ran their own
  700-clinician field operation across 11 states. The gap is market exposure, not capability.

**The distinction has to hold under scrutiny**, because MedArrive has *less* home health exposure than
CareConnect, not more. Write both lines into the Notes block or the shortlist cannot be defended in six
weeks.

### 4. The Questions tab asks but cannot record
18 slots per vendor, no cell for the answer, no verdict, no route back to the mark. **If the demo is
meant to move a score, there must be somewhere to write what the demo produced.** Add answered / dodged /
changes-the-mark alongside each question.

### 5. Section C gets three slots for seven questions
Section A gets three slots for three sub-questions. Section C — worth 20 points, covering C1 capacity
through C7 the patient — gets three for seven. Section B gets three for nine graded areas. Either give C
more rows, or write the selection rule into the header: *the three areas where this vendor's return was
thinnest.*

**Minor, same tab:** only column D is sized (34 chars); E–R are default width and unusable for question
text. Vendor 12–20 placeholder columns are still present in a round with six vendors — hide them.

## The field-wide blind spots

What *nobody* answered well. These are more useful than any individual vendor's gaps, because they
describe the market rather than a company — and they should shape requirements, not just the demo.

1. **Payment fluency is absent.** PDGM, LUPA, OASIS and recert appear in almost no return. Axle used the
   vocabulary unprompted; MedArrive earned it in a different business; Zeeva has it with no customers;
   CareConnect names the home-health metrics they *don't* have. Everyone else is silent. **The market is
   selling scheduling engines, not home health episode management.**
2. **"Can we take this referral today?" is mostly unanswered.** Only Axle and Arya gave a real
   referral-against-capacity mechanism. HCHB explicitly does not forecast referrals or discharges. This
   is the front door of the whole operating model and the market has not built it.
3. **Clinician fit is the weakest section across every vendor** — 0.25 to 0.75, no exceptions. Several
   returns describe a feedback loop and never the moment a clinician says no. This matches the knowledge
   base's standing finding that change management, not algorithm quality, decides adoption.
4. **Engagement is thin and sold as roadmap.** Patient-facing work is absent (VitalisCare, Servis.ai),
   staged late (Arya), roadmap (CareStitch, MedArrive), or just texting (HCHB).
5. **Incentives are nobody's product.** Manual waitlist (Axle), needs Workday (VitalisCare), out of scope
   (MedArrive), half-scoped (CareConnect), no mechanism at all (AutoMynd).
6. **Durability goes unstated.** Five of the six advancing say nothing about company size, funding stage,
   or how central home health is to the business. Only HCHB is Strong.
7. **Measured impact rarely survives its own baseline.** A3 was Watch for almost everyone. Only Arya and
   HCHB cleared it.

## The unresolved external fact

**HCHB's own data freshness is contested across three returns** and it affects architecture, not just
vendor choice:

| Vendor | Claim |
|---|---|
| Arya | Sub-5-minute for SOCs, visits and schedule changes, via Citrix screen automation tuned by data criticality |
| Axle Health | HCHB's refresh lags **up to 30 minutes** — enough that they switched their integration off |
| HCHB | No latency; native, same as updating in the system |
| CareConnect | ~20 minutes on a read-replica pattern, in a plan that assumes **"HCHB Business Connect"** as a FHIR/HL7 layer |
| VitalisCare | Notes HCHB's own delayed logs, unprompted |

Related and also unverified: whether HCHB's self-serve FHIR marketplace exists before 2027. **Confirm
both directly with HCHB.** Multiple vendors' integration plans are resting on the answer, and Compassus
is the only party in the room who can ask the source.

## Process notes worth keeping

- **Candor correlates with quality.** The returns that admitted the most — Axle switching off a live
  integration, AutoMynd's eight failed pilots, CareStitch's list of what it doesn't ingest, Arya's
  one-customer disclosure — were also the most specific everywhere else. A vendor who claims everything
  has told us something.
- **Watch for two registers.** Servis.ai's engineer-level questionnaire and sales-register proposal PDF
  disagree on the HCHB integration method, and only the PDF uses PDGM/NOA language. Whoever answers the
  form is not always whoever writes the pitch.
- **Watch the single flagship account.** CareConnect's A3, D3 and E3 evidence all comes from the same
  5,000-caregiver deployment. One customer producing every number is a concentration risk in the
  evidence, not just in the business.
- **"The room test" is deliberately unscored until after the demo** — three vendors have a provisional
  read, the rest are blank by design. Fill it after each call.
