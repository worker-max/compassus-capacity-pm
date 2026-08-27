# Numbers Audit — Business Case Register, Capacity and Scheduling

**Target.** `C:\Users\chigh\compassus-capacity-pm\agents\compassus-capacity-pm\artifacts\business-case-register.md` (first pass, 21 Aug 2026).

**Sources checked against.** `artifacts/reimbursement-research/01`–`07`, `artifacts/payer-types-and-episode-economics.md`, `knowledge/business-case-format-2026-08.md`, `knowledge/whiteboard-session-2026-08-13.md`, `knowledge/discovery-session.md`.

**Audit date.** 26 Aug 2026. Adversarial read. Assumption: the author worked fast.

**Headline.** The register's *arithmetic* is almost entirely correct — I could not find a single mis-multiplication except one. The failures are in **what is being multiplied**: a validation check that cannot fail, a fully-allocated cost used where a marginal cost belongs, a revenue base that is mislabelled, a national all-payer margin borrowed as if it were the organisation's, and four load-bearing constants that appear nowhere in the sourced corpus. Three of the four largest bars on the proposed waterfall move materially once corrected.

**Two scope notes.** (1) The register contains **no turnover lever sized at ~$2.1M** and **no "30%-plus increase in operating margin" claim**. Both were in my brief. I audit the underlying method for each anyway, because both are clearly *implied* by the document and one of them is sitting in the upside panel unsized. Findings H-05 and H-08. (2) `C:\Users\chigh\ccsi-business-case\` did not exist; created for this deliverable.

---

## HIGH severity

### H-01. The consistency check is circular. It cannot fail, and it validates nothing.

**Claim (§1).** "260M of episodic revenue at a CY2026 base period payment of 2,038 dollars implies roughly 128,000 payment periods a year. At the national average of 8.4 visits per period that is about 1.07M episodic visits, and at MedPAC's implied 193 dollars fully-allocated cost per visit that is about 207M dollars of visit cost against 260M of revenue — a 20 percent margin, against MedPAC's 21.2 percent for freestanding agencies on traditional Medicare. **The anchors hang together.**"

**Error.** The $193 cost per visit was not observed. Research file 04 §3.2 *derives* it as `$245 payment per visit × (1 − 0.212 margin) = $193`, where 0.212 is the very MedPAC margin the check then claims to have independently reproduced. Substitute the derivation back in and the whole check collapses to an identity:

```
implied margin = 1 − 0.788 × (8.4 × $245 / $2,038.22)
               = 1 − 0.788 × 1.0098
               = 20.4%
```

There is **no Compassus input anywhere in that expression.** The $260M cancels out entirely — it appears in the numerator and the denominator. The check is a pure function of three national constants (8.4, $245, $2,038.22) and the assumed margin. It would return ~20% if Compassus's episodic revenue were $260M, $26M or $2.6B.

What the check actually tests, once unwound, is whether `$245 × 8.4 = $2,058` is close to `$2,038.22`. It is — because $2,057 was MedPAC's *2024 average payment per full period* and $2,057.35 was the *CY2025 base rate*, and CY2026 came in 0.93% below CY2025. So the "20 percent margin" result is a restatement of a 0.93% rate change, dressed as a margin validation.

**Aggravating.** The register attributes $193 to MedPAC ("MedPAC's implied 193 dollars"). MedPAC published no such figure. Research file 04 labels it **[MODELED — ILLUSTRATIVE]** and states in its own reading instructions that such figures "must never be presented to a client as an observed benchmark." The register presents it as one.

**Corrected treatment.** Delete the check, or replace it with one that carries information. A genuinely independent cross-check is available from the anchors already in the document:

| Route | Computation | Result |
|---|---|---|
| Revenue → visits | $260M episodic ÷ ~$1,963 blended period revenue × 8.3 visits | ~1.10M episodic visits |
| Non-episodic → visits | $289M ÷ ~$150 contracted per-visit rate | ~1.9M non-episodic visits |
| **Total implied visit volume** | | **~3.0M visits/yr** |
| Capacity → visits | 3,000 clinicians × 230 productive days × 4.5 visits/day | ~3.1M visits/yr |

Those two routes are independent, they agree within 4%, and the agreement is *informative* — it says the clinician base is running at roughly full utilisation, which is a real (and awkward) finding for a case whose largest upside is throughput growth. That is the check that should be in §1.

**Severity: HIGH.** A CFO who unwinds this once will discount every derived number in the document.

---

### H-02. U2's "$24M of cost" applies a fully-allocated cost to a marginal visit. Correct figure is ~$14M.

**Claim (§5, U2).** "One extra nursing visit per period cuts period operating profit by 28 percent. Across 128,000 periods, a single avoidable visit per period is roughly **24M dollars of cost**."

**Error.** The two sentences use two different costs and only the first is right.

- The 28% is `$109 marginal SN direct cost ÷ $387 period operating profit` = 28.2%. Correct — a marginal visit carries direct cost only.
- The $24M is `128,000 × $193` = $24.7M. $193 is the **fully-allocated** blended cost, which includes G&A, intake, QA/coding, clinical management, EMR and unallocated overhead. None of that is incurred by an incremental visit inside an existing period. Loading a marginal visit with allocated overhead is the single most common cost-model error in operational business cases, and a CFO will find it.

**Corrected figure.**

| Basis | Computation | Result |
|---|---|---|
| Register, as written | 128,000 × $193 | $24.7M |
| Correct, marginal SN | 128,000 × $109 | **$14.0M** |
| Correct, marginal at national discipline mix (~$100) | 132,450 × $100 | **$13.2M** |
| **Defensible range** | | **$13M – $14.5M** |

**Overstatement: 72%.** This is the only outright arithmetic-selection error in the document, and it sits on the number the register uses to argue that the utilisation lever and the VBP lever are the same size (Q2). At $14M against a $13M VBP maximum, Q2's framing still survives — but only just, and it should be restated on the corrected number.

**Severity: HIGH.** Checkable in ten seconds and internally self-contradicting within one paragraph.

---

### H-03. "In-scope episodic revenue" and "non-episodic by difference" are mislabelled. The $260M is Medicare FFS, not all episodic.

**Claim (§1).** "In-scope episodic revenue | ~260M dollars | Coding business case, VBP lever" and "Non-episodic revenue, by difference | ~289M dollars, 53 percent of the book."

**Error.** The $260M is sourced from the coding case's **VBP lever** — a 0.5% VBP swing on "in-scope episodic revenue" (`business-case-format-2026-08.md`). HHVBP payment adjustments apply **only to Medicare FFS home health payments** (research file 07 §1: "Max payment adjustment ±5% of Medicare FFS home health payments"). So finance's $260M is a **Medicare fee-for-service** base, not an "episodic" base.

Episodic Medicare Advantage exists and is not trivial. The only published payment-model mix (research file 02, Prusynski et al., one operator, 19 states) puts **episodic MA at 15.2% of stays — 40.4% of all MA stays.** Under the register's own derivation, every dollar of episodic-MA revenue is sitting inside the "non-episodic 289M."

**What breaks.**

| Lever | Dependency | Effect of the error |
|---|---|---|
| W7 (evening confirmation) | "pays only on the non-episodic half" | Overstated. Part of the $289M is episodic MA, where an extra visit earns nothing — same as FFS. |
| Q4 (payer contracting) | "1 percent on 289M = 2.9M" | Base contaminated with episodic revenue the lever's mechanism does not address. |
| R4 (benefit and cap) | "non-episodic only" | Same contamination. |
| §1 "53 percent of the book" | Derived by difference | The non-episodic share is **lower** than 53%; the true figure is unknown. |
| R2, §1 visit math | 7% LUPA, 8.4 visits, $2,038 rate — all FFS-only constants | Correct **only if** $260M is genuinely FFS-only, which contradicts the label. |

The register cannot have it both ways. Either $260M is FFS (in which case §1's math is right and the "episodic/non-episodic" split in W7/Q4/R4 is wrong), or $260M is all-episodic (in which case §1's LUPA/visit/rate math is wrong because it applies FFS constants to MA contracts). **One of the two is wrong today.**

**Corrected treatment.** Add a fourth anchor row — *Medicare FFS revenue* — and stop deriving the non-episodic base by subtraction. §9 already asks for "actual episodic period count and average period payment"; add "revenue split by payer class and by payment mechanic (episodic / per-visit / per-unit)." Until then, W7, Q4 and R4 should carry an explicit "base contaminated" flag.

**Severity: HIGH.** It is a labelling error, not an arithmetic one, but it propagates into four levers and the document's headline characterisation of the book.

---

### H-04. The "blended 20 percent" margin is not blended. The all-payer figure is 5.0 percent, and it inverts G1's thesis.

**Claim (§6, G1).** "A 2 percent lift on 549M dollars is **11M dollars of revenue**, and the margin on it is higher than the **20 percent blended rate** because the branch infrastructure is already paid for." Repeated in §11 rule 5: "converted at contribution margin, not at the blended 20 percent."

**Error, part one — the label.** The 20% came from §1's episodic-only arithmetic, which was itself derived from MedPAC's **FFS Medicare margin for freestanding HHAs (21.2%)**. That is a Medicare-cost-report margin on Medicare-only revenue against allocated Medicare cost. It is not blended and it is not all-payer.

MedPAC's actual all-payer figure sits in research file 04 §9.2, verified: **the all-payer margin for freestanding HHAs in 2024 was 5.0 percent**, against the 21.2% FFS margin. Research file 04 draws the inference explicitly: *"for the blended all-payer result to be 5.0 percent, everything that is not FFS Medicare must be earning approximately −11 percent."*

**Error, part two — the thesis inverts.** G1 applies a 2% growth lift to **$549M of all-payer revenue** and asserts the incremental margin is *above* 20%. On the corpus's own arithmetic:

- Growth on the FFS half is genuinely high-margin — the flat period payment means an extra *admission* (not an extra visit) is strongly accretive.
- Growth on the non-FFS half runs at approximately **−11%** in aggregate nationally. Two percent more MA and Medicaid volume, absent a rate renegotiation, is **margin-dilutive**.

So "a 2 percent lift on 549M is 11M of revenue at above-20% margin" is wrong twice: wrong margin reference, and wrong sign on more than half the base. The defensible version is a 2% lift **on the FFS/episodic base only** — 2% × $260M = **$5.2M of revenue**, at a genuinely high incremental margin — with non-FFS growth stated as a volume story that requires a rate story to be worth anything.

**Error, part three — the margin-lift framing (not in the document, but implied).** If the case eventually claims "$10M of net benefit against a ~5% all-payer margin on $549M is a 30%-plus increase in operating margin," the arithmetic is right (`$549M × 5.0% = $27.5M`; `$10M ÷ $27.5M = 36%`) and the framing is illegitimate as constructed:

1. **5.0% is a national MedPAC cost-report benchmark for freestanding HHAs**, not Compassus's margin. Compassus is a large multi-state hospice-and-home-health operator; its home health segment margin is a finance input that exists internally. Substituting a national benchmark for a knowable internal number, when the benchmark happens to be the one that maximises the multiplier, is the exact move a CFO is trained to catch.
2. Research file 04 §9.3 carries an explicit warning that the 21.2% cost-report margin and the 8–13% adjusted-EBITDA margins public operators report "**must never be compared directly in a client deliverable**." The same warning applies here. Pick 13% EBITDA instead of 5.0% cost-report and the same $10M becomes a **14%** lift, not 36%.
3. The multiplier is hypersensitive to a denominator the case does not own. Any figure between 14% and 36% is defensible from public data, which means none of them is.

**Corrected treatment.** Never state a margin-lift multiple on a borrowed denominator. State the net benefit in dollars, and let finance apply it to the real segment margin. If a multiple is wanted, show it as a sensitivity band (`at 5% margin → 36%; at 8% → 23%; at 13% → 14%`) with the denominator named as a §9 input.

**Severity: HIGH.**

---

### H-05. The LUPA sizing is wrong in three places. They partly offset, which is why it looks plausible.

**Claim (§4, R2).** "At a national LUPA rate near 7 percent, roughly 8,900 of 128,000 periods a year are LUPA periods, each losing on the order of **1,200 dollars** against the full period payment — about **10.7M dollars of annual exposure**. 81.12 percent of subsequent-period LUPAs were one visit short. If a quarter of the one-short cases turn out to be operationally caused… recovery is on the order of **2.2M dollars a year**."

Arithmetic checks out as written: `128,000 × 7% = 8,960`; `8,900 × $1,200 = $10.68M`; `8,900 × 81.12% × 25% × $1,200 = $2.17M`. Three of the four inputs are wrong.

**(a) $1,200 per LUPA period is too low — and it is below the register's own companion document.**

`payer-types-and-episode-economics.md` §3 puts the cliff at "roughly 1,300 dollars per period" and §4 at "**1,258 to 1,386 dollars**." The register used $1,200, below its own stated floor.

Worse, the population being sized is **subsequent-period** LUPAs (that is what the 81.12% statistic covers), and subsequent periods **do not receive the LUPA add-on** — research file 01 §3.1: the add-on applies to "the only period, or the initial period in a sequence." So the correct loss on precisely this population is larger than the add-on-inclusive $1,363 in the corpus's worked example. Computed from CY2026 per-visit rates:

| LUPA threshold | Visits delivered (one short) | LUPA payment, no add-on | Loss vs $2,038.22 |
|---|---|---|---|
| 2 | 1 | ~$185 | **~$1,853** |
| 3 | 2 | ~$370 | **~$1,668** |
| 4 | 3 | ~$555 | **~$1,483** |
| 5 | 4 | ~$740 | **~$1,298** |
| **Centre of range** | | | **~$1,450 – $1,550** |

**(b) The 81.12% is a subsequent-period statistic applied to all LUPA periods.**

McBee's finding covers subsequent-period LUPAs. The register applies it to all 8,900. Initial-period LUPAs have a different failure mode entirely — early discharge, death, hospitalisation, patient refusal — and are far less often one visit short and far less often operationally recoverable. If subsequent periods are ~60% of LUPAs, the one-visit-short pool is **~4,500**, not the 7,220 the register implies. **Overstated by ~60%.**

**(c) 25% "operationally recoverable" is invented. It appears nowhere in the corpus.**

I grepped all seven research files and both reference documents. There is no 25% figure, no recoverability estimate, and no study of LUPA causation. It is the single most leveraged number in the lever — the headline scales linearly with it — and it has no evidence base whatsoever. Research file 04 §7 goes only as far as calling front-loading "the highest-leverage single change available," labelled **[VERIFIED premise, modeled conclusion]**.

**(d) The 7% rate is FFS-only and agency-specific.** MedPAC's 7% is national FFS. Episodic MA contracts carry a LUPA construct only if the plan writes one (`payer-types` §4: "None inherent, unless the plan's own episode construct carries one"). And agency LUPA rates vary from ~2% to >12%. §9 already asks for the actual rate; until it arrives the number must be a band.

**(e) Gross revenue, not margin.** The recovered visit costs ~$110 to deliver. R2 books the gross $1,200.

**Corrected sizing.**

| Line | Register | Corrected | Basis |
|---|---|---|---|
| Periods | 128,000 | 132,000 | M-01 below |
| LUPA periods @ 7% | 8,900 | 9,250 | |
| Loss per one-short subsequent LUPA | $1,200 | **$1,500** | CY2026 per-visit rates, no add-on |
| One-visit-short pool | 7,220 | **~4,500** | 81.12% of subsequent-period LUPAs only |
| Gross exposure (all LUPAs) | $10.7M | **~$13.9M** | but see caveat |
| Recovery @ 25%, net of visit cost | $2.2M | **~$1.57M** | |
| **Recovery band @ 10% / 25% / 40%** | — | **$0.63M / $1.57M / $2.51M** | |

Note the offsetting: too-low loss per period × too-large pool ≈ the register's answer by accident. The corrected central figure is **~30% below** the stated $2.2M.

**And the word "exposure" is wrong.** $13.9M is not exposure. Most LUPAs are clinically correct — the patient was hospitalised, died, refused, or genuinely needed two visits. Presenting the full LUPA population as recoverable revenue is the framing that leads directly to the behaviour §12 forbids. Size only the addressable subset, and say so in the bar label.

**Severity: HIGH.**

---

### H-06. W1 hardens a whiteboard "perhaps" into a $12M waterfall bar with no ramp, no attribution split, and no severance cost.

**Claim (§3, W1).** "At 200 roles released and a loaded cost of 60,000 dollars, this is on the order of **12M dollars a year**, and it is the largest single hard lever in the initiative."

**On the $60,000.** Direct external validation was unavailable this session (BLS, Salary.com and ZipRecruiter all returned 403/404 to automated retrieval; the session's web-search budget was exhausted before I reached them). Reconstructing from what is in the corpus plus published wage structure:

| Component | Value | Basis |
|---|---|---|
| Base wage, SOC 43-6013 (medical secretaries / admin assistants) | ~$44,000–$48,000 | The occupational class discovery describes — "schedulers are administrators, not schedulers" (`discovery-session.md` §1) |
| Fringe loading, wages → total compensation | ×1.40–1.45 | BLS ECEC: benefits ~30–31% of total compensation |
| **Implied fully loaded** | **$62,000 – $70,000** | |
| Corpus cross-check: CMS's own PRA method | ×2.00 on wage | Research file 05, CY2026 final rule 90 FR 55560 — but that doubling covers overhead *and* fringe |
| Corpus cross-check: research file 05 clinician burden | ×1.30 | Explicitly a fringe-only multiplier, low end |

**Verdict: $60,000 is at or slightly below the bottom of the defensible range for wages-plus-fringe, and clearly too low if it is meant to be a fully burdened departmental cost** (a 300-person function carries team leads, supervisors, workspace, systems seats and training). Corrected range **$62,000–$70,000** for fringe-loaded, **$72,000–$85,000** blended-with-supervision.

Direction of the error is *against* the register — at $66,000 the bar is $13.2M, not $12M. **That is not the problem.** The problem is the headcount and the shape of the bar:

1. **"Perhaps 100."** The whiteboard record reads: "roughly 300 schedulers today, **perhaps** 100 in target state" (`whiteboard-session-2026-08-13.md` line 142). The register converted a hedged aspiration into a committed 200-role release and called it "the largest single hard lever." A single bar worth **more than twice the entire net of the reference coding business case ($5.6M)** rests on one word in one whiteboard session.
2. **The register concedes two haircuts and applies neither.** It states "not all of it is attributable to this platform, because part of the reduction comes from workflow automation that should arguably not exist at all," and "the release is phased across the rollout, so year one carries a fraction." The §10 waterfall then shows one undiscounted bar. Two named haircuts, zero quantification, and no year-one column anywhere in the document.
3. **"Capacity released" is not cash.** Roles released by attrition, redeployment or elimination have completely different P&L consequences and completely different timing. Finance cannot book a bar that does not say which.
4. **No severance or retention cost.** 200 role eliminations at 4–12 weeks' pay plus benefits continuation is a **$3–6M one-time cost** that appears nowhere. Nor does retention pay for the schedulers who must stay through cutover — a well-known failure mode when a function is publicly told two-thirds of it is going away.
5. **Scope unverified.** Are all 300 schedulers on the home health side? Compassus runs home health, hospice, palliative and community care. The $549M anchor is home health revenue. If the 300 spans hospice, an unknown share of the $12M does not belong in this case.

**Corrected treatment.** Split into three explicit bars: *steady-state gross release* (200 × $66,000 = $13.2M), *attribution to this platform* (×, unknown, needs an owner), *year-one realisation* (×, phased). Add a one-time severance/transition cost bar. Show year one and steady state as separate columns.

**Severity: HIGH.** This is the case's biggest number and its softest.

---

### H-07. The waterfall adds revenue bars to cost bars and nets them without converting revenue to margin.

**Claim (§10).** A single "Total net benefit" summing: Scheduler capacity released, Premium labour offset, Overtime reduction, Non-billable visits avoided, LUPA leakage recovered, Discipline and role match, Rebook waste removed, less five cost bars.

**Error.** Those bars are two different currencies.

| Bar | Currency |
|---|---|
| W1 Scheduler capacity, W3 Premium labour, W4 Overtime, U1 Discipline match, U3 Rebook waste | **Cost removed** — flows to operating profit 1:1 |
| R1 Non-billable visits avoided, R2 LUPA leakage recovered | **Gross revenue** — must be netted of the cost of delivering the associated visit, and of sequestration |

The register catches this exactly once — §11 rule 5, for G1 only ("must be converted at contribution margin, not at the blended 20 percent"). The same rule is not applied to R1 or R2, which are *on the waterfall* where G1 is not.

**Corrected treatment.** Every revenue bar needs a stated conversion. For R2: subtract ~$110 of visit cost per recovered period. For R1: subtract the delivery cost of the visit that becomes billable — though note R1's visits were *already delivered*, so for R1 the gross revenue genuinely is the margin, and that should be said rather than assumed. And see M-06 on sequestration.

**Severity: HIGH.** A mixed-currency waterfall is the first thing a CFO's FP&A team will rebuild, and the rebuild will come back smaller.

---

### H-08. The turnover extrapolation (implied, unsized) will not survive the study it rests on.

**Not present in the register.** §9 lists "Clinician turnover rate and replacement cost → Turnover lever"; §10 puts "clinician retention" in the upside panel unsized. My brief describes a ~$2.1M figure from applying a 9.2 percentage-point effect to a worst-quartile population of ~500. **No such figure exists in the register or anywhere in the project.** If it is being carried verbally, it should not be, for the following reasons.

**The study.** Bergman, Song, David, Spetz & Candon, *Medical Care Research and Review* 2021 (PMC9122113). HR, payroll and visit-level data from one top-five US home health organisation: 3,716 nurses, 30+ states, **January 2016 – March 2019**. Finding: moving a **full-time RN** from the 75th to the 25th percentile of schedule volatility cut annual quit probability by **9.2 percentage points**.

**Why the extrapolation fails.**

1. **Full-time only.** Research file 05 §6.1, emphatically: "The relationship **disappeared entirely for part-time nurses**… Segment the claim by employment status or it will not survive contact with a customer's data." A "worst-quartile population of ~500" drawn from 3,000 clinicians is a mixed population of FT and PT, RN, LPN, therapist and aide. The effect is documented for **FT RNs and LPNs only**. Therapists and aides are outside the evidence entirely.
2. **The effect size is an upper bound, not a treatment effect.** 75th→25th percentile is a near-total elimination of one nurse's schedule volatility. No platform delivers that to a whole quartile. The Penn LDI summary frames the same result at the 5th/95th percentiles — the effect is a distributional statement, not a dose-response curve you can apply at partial strength.
3. **Data years 2016–2019.** Pre-PDGM, pre-pandemic, pre-MA-majority. Visits per period were 10.2 then and 8.4 now. Baseline voluntary separation in that dataset was FT RN 27.14% — close to today's 25.46% (HCS 2025), which is the one reassuring thing about it.
4. **No home-health replacement cost exists.** Research file 05 §6.3, flagged in bold: "there is **no rigorously sourced, home-health-specific RN or therapist replacement cost** in the published literature. Every credible dollar figure is hospital-derived." The defensible construction is ≈1.3× salary, **with the transfer stated openly**.
5. **The corpus's own sizing is an order of magnitude away from $2.1M.** File 05 §6.3 computes `0.092 × $124,000 ≈ $11,400 per FT RN per year` and sizes a 20-RN branch at ~$114,000/yr. Scaled naively to 500 that is **$5.7M** — which shows how badly behaved the extrapolation is, not that $5.7M is right.
6. **It contradicts the house precedent by 10×.** The reference coding business case put **DCS turnover reduction at $0.21M** on the waterfall for this same organisation (`business-case-format-2026-08.md`). A $2.1M turnover lever in an adjacent case is ten times the internally accepted figure. That contradiction alone would sink it in a steering committee.

**Corrected treatment.** Size it only against the FT RN and FT LPN population, at a stated partial-effect fraction, on a replacement cost carried at 1.3× the branch's own loaded salary, and state the 2016–2019 vintage. A defensible band for 500 *eligible FT nurses* at a 25–50% realisation of the 9.2pp effect and $104,000–$124,000 replacement cost is **$1.2M – $2.9M**, and even that should sit in the upside panel — except that the house format has already accepted turnover as a **waterfall** lever, which is an inconsistency the register should resolve deliberately rather than by silence.

**Severity: HIGH** if quoted as a hard number; the risk is that it is currently invisible and therefore unaudited.

---

## MEDIUM severity

### M-01. The period count is understated by ~4%. Dividing revenue by the BASE rate is the wrong denominator.

**Claim (§1).** "$260M ÷ $2,038.22 ⇒ roughly 128,000 payment periods."

The arithmetic is right ($127,563). The denominator is wrong in kind. `$2,038.22` is the **national standardised** rate — before case-mix weight, before wage index, and it is the rate for a **full** period. Actual revenue per period across the whole population is lower, because ~7% of periods are LUPAs paying a few hundred dollars.

| Component | Value |
|---|---|
| Full periods, 93% × $2,038.22 (avg CMW × WI ≈ 1.0, budget-neutral nationally) | $1,895.5 |
| LUPA periods, 7% × ~$700 | $49.0 |
| Outlier payments, ~+1% | +$19 |
| **Blended revenue per period** | **~$1,963** |
| **$260M ÷ $1,963** | **~132,500 periods** |

**Direction: dividing by the base rate UNDERSTATES period count**, by roughly 4%. Every per-period sizing in the document (R2, R3, U2) is correspondingly conservative — which is the safe direction, but it should be stated rather than accidental.

**Two things could push it the other way.** Case-mix weight and wage index are budget-neutral *nationally*, not for any one operator: a book concentrated in high-wage-index metros with above-average acuity has revenue per period above $2,038 and therefore *fewer* periods. And if any part of the $260M is episodic MA (H-03), MA episodic payment is "typically less… compared to TM" (Prusynski et al., research file 02) — pushing the count up again.

**Corrected: state a range, ~125,000–140,000**, not "roughly 128,000." §9 already flags this correctly ("Actual episodic period count and average period payment | Replaces the derived 128,000"); §1 should carry the same humility.

**Severity: MEDIUM.**

---

### M-02. 8.4 visits per period is a *full-period* figure applied to all periods. The all-period figure is 8.3.

**Claim (§1).** "At the national average of 8.4 visits per period that is about 1.07M episodic visits."

MedPAC Table 8-4's 8.4 is explicitly "per **full** 30-day period (a period that met or exceeded its LUPA threshold)." Research file 04 §2.1 carries the correct all-period figure in the very next paragraph, **verified**: "Counting LUPA periods as well as full periods, the average number of in-person visits per 30-day period was **8.3 in 2024**."

| Route | Computation | Result |
|---|---|---|
| Register | 128,000 × 8.4 | 1.075M |
| All-period rate, corrected count | 132,500 × 8.3 | **1.100M** |
| Bottom-up | 123,200 full × 8.4 + 9,270 LUPA × 3.0 | **1.063M** |
| **Defensible range** | | **1.03M – 1.10M** |

The register's 1.07M lands inside the range — by luck, from two offsetting errors (understated periods × overstated visits/period). Present it as a range.

**Also.** 8.4 is a traditional-Medicare-FFS national figure. MedPAC explicitly **does not publish an MA visits-per-period figure** (research file 04 §2.4, endnote 5). If any of the $260M is MA, this constant does not cover it.

**Severity: MEDIUM.**

---

### M-03. U1's therapy share understates the corpus; the substitution ceiling is unmodelled; "paraprofessional" is the wrong word.

**Claim (§5, U1).** "At a 30 dollar loaded cost differential per visit, therapy at roughly 40 percent of 1.07M episodic visits, and a 15 percent shift, this is on the order of **1.9M dollars a year**." (`1.07M × 0.40 × 0.15 × $30 = $1.926M` ✓)

**Input 1 — $30 differential. SOUND.** Research file 04 §3.3 gives PT $105 vs PTA $74 (**$31**), RN $109 vs LPN $78 (**$31**), OT $101 vs COTA $76 (**$25**). A blended $29–30 is well supported. *Caveat:* those are **[MODELED — ILLUSTRATIVE]**, built on BLS national mean wages at a 1.30 burden multiplier plus a $17 travel allowance, and are **direct variable cost only**. The register presents $30 as fact with no such flag.

**Input 2 — "therapy at roughly 40 percent." Understated.** MedPAC 2024: therapy 3.8 of 8.4 visits = **45.2%**. Correcting: `1.07M × 0.452 × 0.15 × $30 = **$2.18M**`. Conservative direction, but there is no reason to round 45% down to 40% when the verified figure sits in the corpus.

**Input 3 — "a 15 percent shift." Invented, and bounded by regulation the register does not mention.** No source anywhere in the corpus. And the ceiling is not free: Medicare requires the **PT** (not the PTA) to perform the initial evaluation, the periodic reassessment, and the discharge; state practice acts cap PTA supervision ratios; and DE-08's opt-out is by design a clinician veto. A 15% shift of *all* therapy visits may or may not be reachable — nobody has checked what fraction of therapy visits are even eligible.

**Terminology error.** The register says "**paraprofessional** substitution" and cites DE-08's "default to the paraprofessional." In home health, *paraprofessional* means the aide (research file 04 §3.3: **$47/visit**, a **$58–$62** differential from RN/PT). *PTA, COTA and LPN* are **assistants** — licensed, and the population the $30 differential actually describes. The register is running aide language over assistant economics. They are different clinical decisions, different differentials, and different regulatory constraints.

**Unmodelled cost.** Shifting ~64,000 visits requires roughly **45–55 additional PTA/COTA/LPN FTE** (at 6 visits/day × 230 days). National PTA employment is 112,430 against 267,330 PTs. Recruitment cost, ramp time and availability are real and appear in no cost bar.

**Corrected range: $1.6M – $2.4M**, dependent on a shift-rate input that does not exist, with a recruitment cost bar attached.

**Severity: MEDIUM.**

---

### M-04. The anti-double-counting section is incomplete. Six overlaps it missed.

§11 has five rules. They are correct as far as they go — W2 inside W1, U1's freed capacity is G1, R2/U3 counted once in R2, W7 non-episodic only, G1 at contribution margin. Missing:

| # | Overlap | Why it matters |
|---|---|---|
| a | **R2 × R1** | R2's 25% "operationally caused" explicitly names "an authorization hold." A visit not delivered because auth had not arrived is an R1 write-off candidate *and*, if it dropped the period below the floor, an R2 LUPA. Both bars are on the waterfall. Direct double count. |
| b | **W1 × U3** | Exception recovery and rebook handling **is** scheduler work. If 200 scheduler roles are released, the administrative cost of rebooking is already inside W1. U3 must be limited to the clinician *slot* cost only, and must say so. |
| c | **U1 × W3/W4** | If therapy visits are currently being covered by contract or premium labour, substituting to a PTA both removes premium spend (W3) and captures the $30 differential (U1). Same dollar, two bars. |
| d | **R2 × R3** | A certification period lost or shortened at recert (R3) frequently *presents* as a LUPA period (R2). Same failure, two levers. |
| e | **Q1 × U2** | Q1 notes OASIS functional measures are dose-responsive to visit timing. U2's entire defensible lever is "place the same visits better." That is one intervention paying twice — once as margin (U2), once as VBP (Q1). §11's rule set is silent, and **Q2 actively invites the double count** by declaring the two levers peers without saying they may be the same money. |
| f | **W5 × W3/W4** | Preventing five-of-seven nurses being approved off the same day directly prevents the premium and overtime coverage W3 and W4 monetise. W5 is currently unsized so there is no dollar collision *today* — the moment it is sized, there is. |

**Also worth a rule.** §11 rule 5 says G1 must not be added to "any lever that already assumes the same freed capacity" but names none. It should name W1, W6 and W7 explicitly — all three claim to free time that G1 then sells.

**Severity: MEDIUM.**

---

### M-05. G2's moratorium framing — "the single strongest framing available" — expires in roughly ten weeks.

**Claim (§6, G2).** "CMS imposed a national six-month moratorium on new home health and hospice Medicare enrollment in **May 2026**… While it holds, growth cannot be bought with new locations… it is the single strongest framing available for the steering committee."

**Faithful to source** (research file 07: announced May 2026, effective immediately, six months, all initial enrolment applications and certain majority-ownership changes). **But the register omits two facts that change how it should be used.**

1. **It expires around November 2026.** As of the register's own date (21 Aug 2026) that is roughly ten weeks out — before this initiative reaches its scale phase. Anchoring "the single strongest framing available for the steering committee" to a policy that may lapse before the pilot readout is a presentation risk, not an analytical one, but it is the kind of thing that makes a case look dated three months after it is written.
2. **It is "extendable in six-month increments"** — the register omits this, which is the fact that would actually justify the framing. Include it.

**Minor internal tension.** G2 says growth "cannot be bought with new locations"; G4 says "growth by integration matters more." The source notes acquisition is *also* constrained, by the change-of-majority-ownership provision. G4 should acknowledge that rather than presenting integration as the open door G2 closed.

**Corrected treatment.** Reframe as: *while it holds and for as long as CMS extends it* — and add the durable version of the argument, which does not depend on the moratorium at all (SOC capacity is the binding constraint on branch growth regardless of enrolment policy).

**Severity: MEDIUM.**

---

### M-06. Sequestration is missing. Every Medicare revenue bar is 2% too high.

The 2% Medicare sequester applies to Medicare fee-for-service payments. It appears nowhere in the register, nowhere in `payer-types-and-episode-economics.md` §5's CY2026 reference table, and in none of the sizing formulas.

**Affected:** R2 (LUPA recovery), R3 (recert capture), Q1 (VBP — the adjustment is applied to FFS payments), and the §1 revenue-to-period derivation if $260M is stated gross of sequester rather than net.

**Effect:** −2% on every FFS revenue bar. Small in isolation (~$30k on R2's corrected $1.57M) but it is exactly the kind of omission that tells a CFO the model was not built by someone who works with Medicare cash.

**Also missing from the reference table and therefore from any forward view:** the register does not flag **MedPAC's Recommendation 8 (adopted 17–0, March 2026): reduce the CY2026 base rate by 7 percent for CY2027**. Research file 04, verified. If that lands, every episodic dollar in this case moves 7% — and the case has a multi-year rollout. That belongs in §8 as a named risk, not absent.

**Severity: MEDIUM.**

---

### M-07. Q1 mislabels the VBP weight. "OASIS functional measures" are 22%, not 40%.

**Claim (§7, Q1).** "OASIS functional measures are **40 percent** of the total performance score and are dose-responsive, which ties them directly to visit timing."

**Source (research file 07 §1.2, CY2026 finalized, verified):**

| Measure | Weight (larger-volume) |
|---|---|
| Improvement in Dyspnea | 7.00% |
| Improvement in Management of Oral Medications | 11.00% |
| Discharge Function Score | 15.00% |
| Improvement in Bathing (M1830) | 3.50% |
| Improvement in Upper Body Dressing (M1810) | 1.75% |
| Improvement in Lower Body Dressing (M1820) | 1.75% |
| **OASIS category subtotal** | **40.00%** |

40% is the **whole OASIS category**. Dyspnea and Oral Medications are not functional measures. **Functional measures total 22.00%** (Discharge Function Score + the three new bathing/dressing measures).

**Also unstated:** the weights differ by cohort — the OASIS subtotal is **50%** for smaller-volume agencies (which have no HHCAHPS weight at all). With a multi-branch estate spanning both cohorts, "40 percent" is right for neither uniformly.

The rest of Q1 is accurate and well done — the ACH/ED-use retirement, the PPH/DTC-PAC/MSPB-PAC replacement set, the ±5% maximum, and the 0.5% × $260M = $1.3M house convention are all faithful.

**Severity: MEDIUM.**

---

### M-08. Q4 applies a per-visit-MA clinical finding to a base that includes Medicaid, whose rates are not negotiable.

**Claim (§7, Q4).** "Per-visit Medicare Advantage stays carry 12 percent higher odds of mid-stay inpatient transfer than episodic ones… Against roughly 289M dollars of non-episodic revenue, a 1 percent rate or mix improvement is **2.9M dollars**."

**The evidence is sound and correctly represented** — Prusynski et al., per-visit MA vs episodic MA, 12% higher odds (CI 1.06–1.18), and the register's causal read matches the authors' own. Good work.

**The sizing is not.** The $289M includes commercial and Medicaid. **Medicaid rates are set by state fee schedule or MCO contract; you cannot negotiate a 1% lift out of a state fee schedule.** The lever's mechanism — evidence better transfer performance to win rate or mix — works only against commercially negotiable contracts, principally MA and commercial. The addressable base is a subset of $289M whose size is unknown.

**And per H-03, the $289M base is contaminated** with episodic MA, which the argument does not address.

**One thing the register under-claims:** a 1% *rate* improvement is 1% of revenue flowing at ~100% to margin. As a margin lever it is worth far more than a 1% volume lever. That should be said — it is the strongest thing about Q4.

**Corrected: $2.9M is an upper bound on an unknown base.** Size it after the payer-class revenue split (H-03) arrives.

**Severity: MEDIUM.**

---

### M-09. R1's "structurally forced to work at risk" overstates the regulation. §484.55 has three triggers, not one.

**Claim (§4, R1).** "the federal condition of participation requires the initial assessment within 48 hours of referral — faster than many plans' authorization turnaround — so the branch is **structurally forced** to work at risk."

**42 CFR §484.55(a)(1)**, as quoted correctly in research file 04: the initial assessment visit must occur **"within 48 hours of referral, within 48 hours of the patient's return home, *or on the practitioner-ordered start-of-care date*."**

The third trigger is the one the register drops, and it is the one that matters. A practitioner-ordered SOC date is a **compliant, documented way to wait for authorization**. The branch is therefore not *structurally forced* to work at risk — it faces a real and often bad trade-off between clinical urgency and payment risk, which is a strong enough argument on its own without overstating the regulation.

Research file 06 gives the honest version: hospitals request an initial visit within 24–48 hours of discharge while MA authorization turnaround runs three to six days, sometimes 14. That is a *referral-source-pressure* argument, not a *regulatory-compulsion* argument. Restate it that way; it survives challenge and the current version does not.

The backdating claim ("zero to five days at most payers") is **verified and faithful** (research file 06 §2.3: Anthem Ohio 2 days, out-of-state 0–5, Carelon 5 business days, Optum will not backdate after day 14).

**Severity: MEDIUM.**

---

### M-10. W2's 20-second constant is invented and the estimate is hypersensitive to it.

**Claim (§3, W2).** "At 55 notifications per scheduler per day across 300 schedulers, at 20 seconds each to open, read and close, the fleet spends roughly 92 hours a day, about 11 full-time equivalents."

Arithmetic ✓: `55 × 300 × 20s = 330,000s = 91.7 hours`; `91.7 ÷ 8 = 11.5 FTE`.

**Two soft inputs.**

- **55 notifications.** Discovery says "50–60 per day"; the whiteboard says "roughly 50 a day." The register took the midpoint of the wider range. At 50 the answer is 10.4 FTE. Minor.
- **20 seconds. No source.** To open a chart in an EMR, read a notification, judge actionability and close it. Twenty seconds is aggressive; 45 seconds is at least as plausible, and at 45 seconds the figure is **26 FTE and ~$1.6M**.

**Note the direction.** The author chose the value that makes W2 *small*. That is conservative for the number, but it works against the narrative — W2 exists in the document precisely because it is "the most-cited frustration in the scheduler's day," and $690k of it (11.5 × $60k, 5.8% of W1) does not carry that story. Either measure the handling time or present a band (10–26 FTE) and let the range make the point.

**Consistency ✓:** W2 at 11.5 FTE sitting inside W1's 200 released roles is internally coherent, and the "do not add them" rule is correct.

**Minor unit note.** W2 computes a *daily* hours figure and converts to FTE without stating working days. 92 hours/day ÷ 8 = 11.5 FTE only if notification volume is per working day. It presumably is; say so.

**Severity: MEDIUM.**

---

## LOW severity

### L-01. $193 is a 2024 cost applied against CY2026 revenue.

MedPAC's $245 payment-per-visit and 21.2% margin are **2024** figures; the derived $193 is therefore a 2024 cost. §1 applies it against the **CY2026** base rate of $2,038.22. Two years of wage inflation are missing from the cost side while the revenue side is fully current. This flatters the implied margin — which, per H-01, is meaningless anyway, but the same $193 is reused in U2 where it is load-bearing (and wrong for a different reason).

Research file 04 §3.2 offers the year-consistent alternative and the register did not take it: `$2,038.22 × (1 − 0.19) = $1,651` fully-allocated per period for CY2026, anchored to MedPAC's own 2026 projection.

### L-02. §1 uses MedPAC's 2024 actual (21.2%) when MedPAC's CY2026 projection (19%) is the year-matched figure.

Same vintage problem, other direction. Research file 07: "MedPAC projects a **19% FFS Medicare margin in 2026**." If §1's check is retained at all it should compare against 19%, not 21.2%.

### L-03. The register demotes turnover to the upside panel; the house precedent puts it on the waterfall.

`business-case-format-2026-08.md` records "**Turnover reduction is already accepted as a hard waterfall lever**, not an upside item — the coding case puts DCS turnover reduction at 0.21M on the waterfall itself." §10 of the register puts "clinician retention" in the upside panel. Not wrong — the evidence for a *clinician* turnover effect is weaker than for a *DCS* one — but the divergence from the house precedent should be stated deliberately rather than left to look like an oversight.

### L-04. The ePA framing overstates near-term benefit and omits the live-today obligation.

§8 cites "the electronic prior authorization requirement effective 1 January 2027." Correct (CMS-0057-F FHIR Prior Authorization API, research file 06 §6.4) but the register omits three things: it binds **payers, not providers**; it excludes traditional Medicare (which has no home health PA anyway); and UnitedHealthcare's own PA submission API is listed as "**Coming soon**, no launch date" (research file 02). Meanwhile the register omits the obligation that is **already live**: CMS-0057-F's 7-calendar-day standard / 72-hour expedited decision SLAs and structured denial reason codes, effective **1 January 2026** — a far more actionable near-term signal for an authorization-aware scheduling platform than a 2027 API.

### L-05. R4 sizes in visits; Medicaid pays in units.

R4 says "Sizing is unbillable post-cap visits times the rate." `payer-types` §7 is explicit that the authorization unit is "**Visits, hours, or 15-minute increments. Not interchangeable**," and §9 records Ohio Medicaid's 8-hour daily / 14-hour weekly caps and Texas Medicaid's rolling-seven-day metering. A visit-based formula will silently mis-size the Medicaid share. Same applies to any per-visit sizing on the non-episodic side.

### L-06. §12's "18 percent" needs its denominator.

"Industry utilisation has already fallen 18 percent." Verified (MedPAC, 10.2 → 8.4, −18.0%) — but that is **visits per full period**, not total industry utilisation, which fell far further (total in-person visits 99.7M → 65.4M, **−34.4%**). Name the measure.

### L-07. The OIG audit is a 120-claim sample from a pre-PDGM era.

"A federal audit found 21 percent of claims just above the threshold non-compliant" — faithful (OIG A-09-18-03031, 25 of 120, $191.8M extrapolated), but it is **July 2020**, on 60-day-episode claims with the old uniform threshold, on a sample of 120. As a *guardrail* it is entirely sufficient and the register uses it correctly. If it is ever used to size anything, the sample size will not carry it.

### L-08. No contingency, no year-one column, no ROI percentage.

The house format states ROI "as a percentage against cost, alongside the net" — the coding case shows 276%. §10's waterfall has no ROI line, no contingency bar, and no year-one/steady-state distinction anywhere in the document despite W1 explicitly conceding a phased release.

---

## Missing costs

Any complete case must carry these. None appears in §10.

| # | Missing cost | Rough scale | Note |
|---|---|---|---|
| 1 | **Severance / transition for 200 released roles** | $3–6M one-time | 4–12 weeks' pay + benefits continuation. The single largest omission. |
| 2 | **Retention pay through cutover** | $0.5–1.5M | Standard when a function is told two-thirds of it is going. |
| 3 | **Internal project team** | 15–30% of external cost | PM, BA, clinical informatics, IT, plus backfill for SMEs pulled into design. |
| 4 | **HCHB / Workday interface build + recurring vendor interface fees** | Recurring | The register notes the Workday→HCHB PTO integration exists; a scheduling platform needs more, and EMR interface fees recur. |
| 5 | **Data remediation** | One-time, non-trivial | Territory/geocode, clinician competency, credentialing, availability, PTO. Routing by drive time (W6) is inert without clean geodata. |
| 6 | **Parallel-run / dual-running during phased rollout** | Recurring through rollout | Directly implied by W1's own phasing concession. |
| 7 | **Cutover productivity dip (the J-curve)** | Year one net-negative | Well documented for scheduling/EMR change. The case has no year-one column to put it in. |
| 8 | **PTA / COTA / LPN recruitment and ramp for U1** | 45–55 FTE hires | See M-03. |
| 9 | **Payer rules library — ongoing, not build** | Permanent FTE load | §10 has it as a cost bar; §8 correctly calls it "an onboarding cost and a durable moat" but its *recurring* nature (per contract, per branch, on every renegotiation) is not sized. |
| 10 | **Clinical governance for DE-08 opt-out** | Recurring | Supervision, audit, documentation of substitution decisions. |
| 11 | **Compliance / self-audit tooling for threshold-adjacent monitoring** | Recurring | §8 names the risk; the mitigation costs money. |
| 12 | **Cost of the recovered LUPA visits** | ~$110 × recovered periods | Netted in my H-05 correction; absent from the register. |
| 13 | **Licence escalators / volume-based pricing** | Recurring, compounding | §10's "Platform licence" bar reads as a flat annual. |
| 14 | **Contingency reserve** | 10–15% | Absent entirely. |
| 15 | **Sequestration on revenue bars** | −2% | See M-06. |

---

## Claims checked and found SOUND

Everything below I verified against the sourced corpus and could not fault. This is most of the document, and it is worth saying so.

**Arithmetic — every one of these computes exactly as stated:**

| Claim | Check |
|---|---|
| $549M − $260M = $289M, 53% of the book | ✓ 52.6% |
| $260M ÷ $2,038.22 = ~128,000 | ✓ 127,563 (denominator disputed at M-01; the division is right) |
| 128,000 × 8.4 = ~1.07M | ✓ 1,075,200 |
| 1.07M × $193 = ~$207M | ✓ $206.5M |
| 7% × 128,000 = ~8,900 | ✓ 8,960 |
| 8,900 × $1,200 = ~$10.7M | ✓ $10.68M |
| 8,900 × 81.12% × 25% × $1,200 = ~$2.2M | ✓ $2.17M |
| 1.07M × 40% × 15% × $30 = ~$1.9M | ✓ $1.926M |
| 55 × 300 × 20s = ~92 hrs/day ≈ 11 FTE | ✓ 91.7 hrs, 11.5 FTE |
| 0.5% × $260M = $1.3M; 5% × $260M = $13M | ✓ |
| 1% × $289M = $2.9M | ✓ $2.89M |
| 2% × $549M = $11M | ✓ $10.98M |
| One extra nursing visit = 28% of period operating profit | ✓ $109 ÷ $387 = 28.2% — **and it correctly uses marginal cost against operating profit**, which makes the $24M error two sentences later all the odder |

**Facts faithfully represented from the research corpus:**

- CY2026 national standardized 30-day period rate **$2,038.22** — and the register correctly avoids the widely-circulated **wrong** figure of $1,933.61 (the proposed rate). Good catch by the author.
- LUPA thresholds **2 to 5 visits**; case-mix weight range **0.5364 to 1.9558**.
- Visits per full period fell **10.2 → 8.4** between 2019 and 2024 (−18.0%), while discharge to community fell **85.2% → 82.8%**. Both verified MedPAC.
- **Travel sits in the non-labour 25.1% share and is never wage-index adjusted.** Verified against CY2024 and CY2026 final rules. W6's framing is exactly right, including the rural double-squeeze implication.
- Star ratings: **0.88pp / 0.81pp** (Schwartz et al.) and **0.25pp, statistically insignificant** (Jun Li). The register's "roughly 0.8" and "statistically insignificant 0.25" are faithful, and **Q3's conclusion — do not build ROI on star-rating referral lift — is correct and well disciplined.**
- **12% higher odds of mid-stay inpatient transfer** for per-visit vs episodic MA (Prusynski et al., CI 1.06–1.18), with the mechanism correctly attributed to loss of agency discretion over visit mix and timing. The register's causal read matches the authors' own conclusion verbatim.
- **OIG: 21% of threshold-adjacent claims non-compliant**, contractors committed to targeting the cluster (A-09-18-03031). Faithful.
- **Points-system wage exposure: $44.16 headline resolved to $30.06/hr actual, a 32% gap.** Verified, research file 05 §4.
- **HHVBP measure-set change:** ACH and ED-use retired after CY2025 performance year, replaced by PPH, DTC-PAC and MSPB-PAC; **±5% maximum adjustment**; **0.5% swing on episodic revenue is the house convention**. All verified. This is the most accurate section in the document.
- **Telehealth counts toward nothing** — not the floor, not the visit count, not payment. Verified.
- **Backdating windows 0–5 days at most payers.** Verified across four named payers.
- **National enrollment moratorium, May 2026, six months, including certain ownership changes.** Verified (see M-05 for the omissions).
- **CMS-0057-F FHIR Prior Authorization APIs effective 1 January 2027.** Verified (see L-04 for the framing caveat).
- **$30 loaded cost differential per visit.** Matches PT→PTA $31, RN→LPN $31, OT→COTA $25.
- **~300 schedulers today / ~100 target, ~3,000 clinicians, 50–60 auth notifications/day, 7+ tasks per three-discipline admission, 40–50 census per RN/LPN pair.** All faithful to the whiteboard and discovery records.

**Reasoning that is correct and unusually well disciplined:**

- **W7's payer-class inversion.** "Under episodic payment an additional visit earns nothing, so this lever pays only on the non-episodic half." The logic is exactly right (the base is mislabelled per H-03, but the *reasoning* is sound and is the kind of distinction most cases get wrong).
- **U3's framing** — under a fixed period payment, rebook waste lands on margin rather than showing up as lost revenue, "which makes it a cleaner argument for coordination investment than the lost-revenue framing." Correct and well put.
- **U2's refusal to frame the lever as fewer visits**, grounded in the front-loading evidence and the utilisation-already-fell-18% counterweight. This is the single best judgement call in the document and it is the one that will earn clinical credibility.
- **R2's absolute gate** — recovery limited to clinically indicated visits lost to operational failure, with the OIG targeting risk stated in the same breath. Correct, and correctly placed.
- **§11 rules 1–4** are all valid as far as they go (see M-04 for what they miss).
- **§12's six prohibitions.** Every one is faithful to a sourced guardrail. Keep this section unchanged.
- **§9's input list.** Comprehensive, and the "pay-model split is the highest-value single input" call is exactly right — research file 05 says the same thing in bold twice ("the platform's single most important qualifying question"). The observation that the named pilot candidates are the per-visit offices, which are the best adoption sites and the worst margin-proof sites, is the sharpest paragraph in the document.
- **The `[MODELED]` / `[VERIFIED]` discipline of the underlying corpus is excellent.** The register's failure is that it strips those labels on the way through — not that the research was weak.

---

## Corrected summary of the sized levers

| Lever | As written | Corrected / range | Confidence |
|---|---|---|---|
| Periods per year | 128,000 | **125,000 – 140,000** (central ~132,500) | Low — needs actuals |
| Episodic visits | 1.07M | **1.03M – 1.10M** | Low |
| W1 Scheduler capacity | $12.0M/yr | **$13.2M gross steady-state**, × unknown attribution, × unknown year-one phasing, **less $3–6M one-time severance** | Very low |
| W2 Auth noise (inside W1) | 11 FTE / ~$0.7M | **10 – 26 FTE / $0.6M – $1.6M** | Very low |
| R2 LUPA recovery | $2.2M/yr | **$0.63M / $1.57M / $2.51M** at 10/25/40% recovery | Very low |
| R2 gross LUPA exposure | $10.7M | **~$13.9M**, but "exposure" is the wrong word | Low |
| U1 Discipline match | $1.9M/yr | **$1.6M – $2.4M**, less PTA/LPN recruitment cost | Low |
| U2 One avoidable visit/period | $24M | **$13M – $14.5M** | Medium |
| Q1 VBP @ house convention | $1.3M | ✓ **$1.3M** | Medium |
| Q4 Payer contracting | $2.9M | **Upper bound on an unknown base** | Very low |
| G1 Growth @ 2% | $11M revenue | **$5.2M on the FFS base**; non-FFS growth may be dilutive | Low |
| Turnover (unsized) | — | **$1.2M – $2.9M**, FT RN/LPN only, 2016–2019 vintage | Very low |

---

## Verdict

**No. Not as they stand.**

The register is a strong *analytical* document with a weak *financial* one inside it. The research underneath is genuinely good — sourced, dated, labelled, and honest about its gaps. The register's failure is a translation failure: it strips the `[MODELED — ILLUSTRATIVE]` labels off national benchmarks on the way into a dollar figure, and it presents a self-referential check as corroboration.

Four things must change before a CFO sees it:

1. **Delete the §1 consistency check** or replace it with the visits-versus-capacity cross-check, which is independent and informative.
2. **Fix U2's $24M** to the marginal-cost figure of ~$14M. It is the only outright arithmetic-selection error and it is trivially checkable.
3. **Split W1 into gross / attributable / year-one, and add the severance bar.** A $12M undiscounted bar built on the word "perhaps" is the case's largest credibility risk.
4. **Stop calling 20% a blended margin.** The all-payer figure is 5.0%, it is in the corpus, and it inverts G1's thesis on more than half the revenue base.

Then rebuild §10 as a two-currency waterfall with a year-one column, and put every invented constant — 25% LUPA recoverability, 15% substitution shift, 20 seconds per notification, 200 roles, $60,000 loaded — into §9 as a named, owned input with a sensitivity band. §13 already proposes exactly that assumptions model. **Build it before the readout, not after.**
