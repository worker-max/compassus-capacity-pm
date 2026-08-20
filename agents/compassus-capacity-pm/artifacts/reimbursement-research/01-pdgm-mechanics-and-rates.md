# Medicare Home Health PDGM — Payment Mechanics and Current Rates

**Research date:** 2026-08-18
**Purpose:** grounding for a home-health branch capacity-and-scheduling platform.
**Verification method:** every number below was pulled from a primary source fetched live on 2026-08-18 — Federal Register raw text, the CMS claims-processing transmittal, the CMS published case-mix data file, the Medicare Claims Processing Manual, eCFR, or the CMS Review Choice Demonstration page. Values recomputed from CMS's own stated factors are labeled **[derived]**. Anything not confirmed is labeled **UNVERIFIED**.

---

## 0. The two rules that currently matter

| Rule | ID | FR citation | Published | Status |
|---|---|---|---|---|
| CY2026 HH PPS Final Rule | CMS-1828-F | 90 FR 55342 | 2025-12-02 (CMS issued 2025-11-28) | **In effect**, effective 2026-01-01 |
| CY2027 HH PPS Proposed Rule | CMS-1844-P | 91 FR 41216 | 2026-07-06 | **Proposed**, comments close **2026-08-31** |

- CY2026 final rule: https://www.federalregister.gov/documents/2025/12/02/2025-21767 (doc 2025-21767; effective_on 2026-01-01; pp. 55342–…)
- CY2026 CMS fact sheet: https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-home-health-prospective-payment-system-final-rule-cms-1828-f (dated 2025-11-28)
- CY2027 proposed rule: https://www.federalregister.gov/documents/2026/07/06/2026-13602/calendar-year-2027-home-health-prospective-payment-system-hh-pps-rate-update-requirements-for-the-hh (doc 2026-13602; 91 FR 41216–41327; RIN 0938-AV80; comments close 2026-08-31)
- Operational rate instruction: CMS Transmittal **R13488CP / CR 14304**, https://www.cms.gov/files/document/r13488cp.pdf (released 2025-11-20; effective 2026-01-01; implementation 2026-01-05)
- Plain-language version: MLN Matters **MM14304**, https://www.cms.gov/files/document/mm14304-home-health-prospective-payment-system-cy-2026-rate-update.pdf (article released 2025-12-11)

**Rate-year trigger (important for a scheduling platform):** the CY rate is selected by the claim **statement "Through" date**, not the start of care. "The contractor shall apply the CY 2026 HH PPS payment rates for periods with claim statement 'Through' dates on or after January 1, 2026." — R13488CP, requirement 14304.2 (2025-11-20). A 30-day period straddling the New Year is paid entirely at the new year's rates.

---

## 1. 30-day payment period vs 60-day certification period

**Unit of payment.** For periods beginning on or after 2020-01-01 an HHA receives "a unit of payment equal to a national, standardized prospective 30-day payment amount." — 42 CFR 484.205(b)(2), https://www.ecfr.gov/current/title-42/section-484.205 (current as of 2026-08-18). Same in Medicare Claims Processing Manual (MCPM) Ch. 10 §10.1.4 (Rev. 10758, eff. 2022-01-01), https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c10.pdf

**Certification is still 60 days.** Recertification "is required at least every 60 days when there is a need for continuous home health care." — 42 CFR 424.22(b)(1), https://www.ecfr.gov/current/title-42/section-424.22. Two 30-day payment periods map onto one 60-day certification period.

**Face-to-face encounter:** must occur "no more than 90 days prior to the home health start of care date or within 30 days of the start of the home health care" — 42 CFR 424.22(a)(1)(v). CY2026 final rule broadened §424.22(a)(1)(v) so any physician — not only the certifying practitioner or the acute/post-acute practitioner — may perform the F2F, aligning with CARES Act §3708 (CMS fact sheet, 2025-11-28).

**Number/duration of periods.** Unlimited non-overlapping 30-day periods; a period may be shorter than 30 days (transfer, or discharge + readmission to the same HHA in the same period), in which case payment is pro-rated. — MCPM Ch. 10 §10.1.5.

**Functional level persistence.** "A patient's functional impairment level remains the same for the first and second 30-day periods of care unless there is a significant change in condition that warrants an 'other follow-up' assessment prior to the second 30-day period." — 91 FR 41228 (2026-07-06). One OASIS drives both 30-day periods in a cert.

### Sequencing: early vs late, and the 60-day gap rule

- The **first** 30-day period in a sequence is **early**; every subsequent period in the sequence is **late**.
- "A subsequent 30-day period of care would not be considered early unless there is a gap of more than **60 days** between the end of one previous period of care and the start of another."
- "Information regarding the timing of a 30-day period of care comes from **Medicare home health claims data and not the OASIS assessment**."
— all three: CY2027 proposed rule, 91 FR 41227–41228 (2026-07-06).

Practical consequence: only one period per patient sequence is ever "early." Long-stay patients sit permanently in the "late" columns, which carry materially lower case-mix weights.

### Admission source: community vs institutional (claims-based)

- Institutional = an inpatient **acute care hospital, IPF, SNF, IRF, or LTCH** stay within **14 days prior** to the home health admission.
- Institutional **also** covers "patients that had an acute care hospital stay during a previous 30-day period of care and within 14 days prior to the subsequent, contiguous 30-day period of care and for which the patient was **not** discharged from home health and readmitted." (Note: for that continuing-period case the rule text names *acute care hospital* only, not SNF/IRF/LTCH/IPF.)
- Everything else is a community admission.
— 91 FR 41227 (2026-07-06).

**How it is reported on the claim.** On an **initial** period (From date = Admission date) the HHA reports **occurrence code 61** (hospital discharge date) or **occurrence code 62** (SNF/IRF/LTCH/IPF discharge date) when the stay ended within 14 days of the From date. On **continuing** periods only occurrence code **61** is reported. Only one of 61/62 may appear; more than one causes an RTP. The 14-day window is counted backward from the day before the From date, and a discharge on the admission day itself also qualifies. — MCPM Ch. 10 §40.2 (Occurrence Codes and Dates).

CMS additionally validates admission source against Medicare claims history; the occurrence code is the provider's assertion, and CMS's claims data is the arbiter (the rule text says the categorization depends on "what healthcare setting was utilized in the 14 days prior," sourced from claims). Exact edit/post-pay adjustment behavior beyond the RTP rules above: **UNVERIFIED**.

---

## 2. The 432 case-mix groups

432 = **4** (admission source × timing) × **12** (clinical groups) × **3** (functional impairment levels) × **3** (comorbidity subgroups). Confirmed by direct count of the CMS published file: 432 rows. CMS calls them home health resource groups (HHRGs). — 90 FR 55379 (2025-12-02).

### The twelve clinical groupings

Verbatim from the CMS data file (`CY 2026 Final HH PDGM Case Mix Weights and LUPA Thresholds.csv`) with the HIPPS letter from MCPM Ch. 10 §10.1.9:

| HIPPS pos. 2 | Clinical group |
|---|---|
| A | MMTA – Other |
| B | Neuro (Neuro Rehab) |
| C | Wound (Wounds) |
| D | Complex (Complex Nursing Interventions) |
| E | MS Rehab (Musculoskeletal Rehab) |
| F | Behavioral Health |
| G | MMTA – Surgical Aftercare |
| H | MMTA – Cardiac (Cardiac & Circulatory) |
| I | MMTA – Endocrine |
| J | MMTA – GI/GU |
| K | MMTA – Infectious (Infectious Disease/Neoplasms/Blood-forming Diseases) |
| L | MMTA – Respiratory |

MMTA = Medication Management, Teaching and Assessment. Assigned from the **principal diagnosis** reported on the claim. — 90 FR 55379.

### Functional impairment levels

Three levels — low, medium, high. Driven by OASIS items **M1800–M1860 and M1033** (grooming, bathing, dressing, ambulating, transferring, risk of hospitalization). Each response carries points; the summed score maps to a level. "Each clinical group has a **separate** set of functional thresholds," set so roughly one third of periods in each clinical group land in each level. — 90 FR 55368–55369 and 55379–55380 (2025-12-02); OASIS item list detail at 84 FR 60490.

### Comorbidity adjustment subgroups (none / low / high)

- **Low**: one reported secondary diagnosis appears on the HH-specific comorbidity subgroup list.
- **High**: two or more secondary diagnoses appear on the HH-specific **interaction** list, where the pair together drives higher resource use than either alone.
- **None**: neither condition met.
— 90 FR 55370–55371 (2025-12-02).

**How the list is built (this is why it must be reference data, not code):** a fixed-effects regression of 30-day resource use on comorbidity indicators, controlling for admission source, clinical group, timing and functional level, with HHA fixed effects. A diagnosis joins the **low** list if its coefficient is statistically significant (p ≤ 0.05) **and** exceeds the 50th percentile of positive significant coefficients. A pair joins the **high** list if the two coefficients plus their interaction term sum to **more than $150** and the interaction is significant (p ≤ 0.05). Candidate diagnoses must also be reported in more than **0.1%** of 30-day periods and have at least median resource use. — 90 FR 55370 and 55380 (2025-12-02).

**CY2026 counts:** **20** low comorbidity subgroups and **98** high comorbidity interaction subgroups (final; the proposed rule had 20 / 100). — 90 FR 55371.
**CY2027 proposed counts:** **21** low and **100** high. — 91 FR 41236-ish, proposed rule §II.D.3.

### HIPPS code construction

Five positions. — MCPM Ch. 10 §10.1.9 (Rev. 10758), corroborated by decoding all 432 rows of the CMS file.

| Position | Encodes | Values |
|---|---|---|
| 1 | Admission source + timing | 1 = Community Early · 2 = Institutional Early · 3 = Community Late · 4 = Institutional Late |
| 2 | Clinical group | A–L (table above) |
| 3 | Functional impairment level | A = Low · B = Medium · C = High |
| 4 | Comorbidity adjustment | 1 = None · 2 = Low · 3 = High |
| 5 | Placeholder | always `1` |

Example: `1FC11` = Early / Community, Behavioral Health, High functional, no comorbidity adjustment — CY2026 weight 1.0804, LUPA threshold 4.

**CY2026 case-mix weight range: 0.5364 to 1.9558** (computed across all 432 rows of the CMS file). That is a **3.65×** spread between the cheapest and richest group at the same wage index — the single biggest driver of per-visit-hour revenue variance in a branch's schedule.

---

## 3. LUPA

### What it is

If a 30-day period's visit count is **below** its group's threshold, the period is paid **per visit** instead of at the case-mix-adjusted period rate. If the threshold is met, full period payment applies (subject to PEP/outlier). "If the LUPA visit threshold is four, and a 30-day period of care has four or more visits, it is paid the full 30-day period payment amount; if the period of care has three or fewer visits, payment is made using the per-visit payment amounts." — 90 FR 55367–55368 (2025-12-02). Regulation: 42 CFR 484.205(d)(1) and 484.230.

### How thresholds are set

**10th percentile of visits within the payment group, with a floor of 2.** "If a payment group has a 10th percentile of visits that is less than two, we set the LUPA threshold for that payment group to be equal to two." Reevaluated **every year** using the most current utilization data at the time of rulemaking. — 90 FR 55367 and 55380 (2025-12-02). Original policy: 83 FR 56492 (CY2019 final rule).

### CY2026 threshold range and distribution

Computed directly from the CMS published file (all 432 groups):

| Threshold (visits) | # of case-mix groups |
|---|---|
| 2 | 119 |
| 3 | 165 |
| 4 | 134 |
| 5 | 14 |

**Range: 2 to 5 visits.** No group has a threshold of 6 or 7 in CY2026.

By clinical group (min–max threshold): Complex 2–3 · MMTA-Infectious 2–3 · Behavioral Health, MMTA-Cardiac, MMTA-GI/GU, MMTA-Other, MMTA-Respiratory, MMTA-Surgical Aftercare 2–4 · MS Rehab and Neuro 2–5 · Wound 3–5 · MMTA-Endocrine 3–5.

### How many groups changed for CY2026 — flag a discrepancy

- **The rule preamble says 18.** "a total of 18 case-mix groups have a decline in their LUPA threshold of a single visit" — 90 FR 55368 (2025-12-02).
- **The published CY2026 data file, diffed against the CY2025 file, says otherwise:** **28 groups decreased** by one visit, **15 groups increased** by one visit, **389 unchanged**. (Computed on 2026-08-18 by diffing `cy2026-hh-pdgm-case-mix-weights-lupa-thresholds.zip` against `cy-2025-final-home-health-case-mix-weights.zip`. CY2025 distribution was 2→120, 3→151, 4→146, 5→15.)

The 28/15/389 split is also what third-party rule summaries report for the final rule. **Treat the published data file as authoritative and ignore the preamble sentence** — the "18" appears to be carried-over proposed-rule language. Build the platform against the file.

### CY2026 per-visit payment amounts (LUPA rates)

Source: CMS Transmittal R13488CP, Tables 3 and 4 (effective 2026-01-01). These are pre-wage-index; they are wage-adjusted by the beneficiary's site of service. Method: CY2025 per-visit rate × wage-index budget-neutrality factor **1.0005** × payment update.

| Discipline | CY2025 per-visit | **CY2026 (QRP-compliant, ×1.0240)** | CY2026 (non-compliant, ×1.0040) |
|---|---|---|---|
| Home Health Aide | $78.20 | **$80.12** | $78.55 |
| Medical Social Services | $276.85 | **$283.64** | $278.10 |
| Occupational Therapy | $190.08 | **$194.74** | $190.94 |
| Physical Therapy | $188.79 | **$193.42** | $189.64 |
| Skilled Nursing | $172.73 | **$176.96** | $173.51 |
| Speech-Language Pathology | $205.22 | **$210.25** | $206.14 |

Note: the permanent and temporary behavior adjustments are **not** applied to per-visit rates — only to the case-mix-adjusted 30-day rate. — 90 FR 55408 (2025-12-02).

### LUPA add-on for the first visit in an initial/only period

A LUPA period that is **the only period, or the initial period, in a sequence of adjacent periods** gets the first SN / PT / SLP / OT visit multiplied by an add-on factor before wage adjustment. Factors were re-derived in the CY2025 rule from CY2023 claims (previously unchanged since CY2014):

| Discipline | Add-on factor (CY2025 onward, still in force for CY2026) |
|---|---|
| Skilled Nursing | **1.7200** |
| Physical Therapy | **1.6225** |
| Speech-Language Pathology | **1.6696** |
| Occupational Therapy | **1.7238** |

— R13488CP Table 7; narrative at 90 FR 55408–55409 (2025-12-02) and 89 FR 88426–88427 (CY2025 final rule). The OT factor is discrete as of CY2025; PT is no longer used as an OT proxy.

Caution: MM14304's *background* paragraph quotes the superseded CY2014 factors (1.8451 SN / 1.6700 PT / 1.6266 SLP). Table 7 of the transmittal carries the current ones. Use the table.

### Where the authoritative per-group threshold table lives

- **Landing page:** https://www.cms.gov/medicare/payment/prospective-payment-systems/home-health-pps/home-health-pps-case-mix-weights
- **CY2026 direct download:** https://www.cms.gov/files/zip/cy2026-hh-pdgm-case-mix-weights-lupa-thresholds.zip
- **Format:** a ZIP containing both `CY 2026 Final HH PDGM Case Mix Weights and LUPA Thresholds.xlsx` and a Section-508 `.csv` version. The CSV is machine-readable, 432 data rows, columns: `HIPPS`, `Clinical Group and Functional Level`, `Admission Source and Timing`, `Comorbidity Adjustment (0/1/2)`, `Recalibrated Weight for 2026`, `LUPA Visit Threshold (LUPAs have fewer visits than the threshold)`.
- Prior years are on the same page (CY2020–CY2025), same ZIP-of-XLSX+CSV shape, so a year-keyed loader works.
- The same table is also printed as Table 8 in the final rule, but as a **TIFF image** in the Federal Register — not machine-readable. Use the ZIP.
- CMS also mirrors these on the HHA Center page: https://www.cms.gov/medicare/enrollment-renewal/providers-suppliers/home-health-agency-center
- **CY2027 file:** not yet posted to the case-mix-weights page as of 2026-08-18 (checked; only CY2020–CY2026 present). Proposed CY2027 weights/thresholds exist only as Table 24 image in 91 FR 41216.

---

## 4. CY2026 final rule (CMS-1828-F) specifics

### The national standardized 30-day period payment amount

From R13488CP Table 1 (exact CMS arithmetic):

| Component | Value |
|---|---|
| CY2025 national standardized 30-day period payment | $2,057.35 |
| × Permanent behavior adjustment factor (−1.023%) | 0.98977 |
| × Case-mix weights recalibration budget-neutrality factor | 1.0052 |
| × Wage index budget-neutrality factor | 1.0025 |
| × CY2026 HH payment update factor (+2.4%) | 1.024 |
| = 30-day period payment **without** temporary adjustment | **$2,101.26** |
| × Temporary adjustment factor (−3.0%) | 0.97000 |
| = **CY2026 national standardized 30-day period payment** | **$2,038.22** |

For HHAs that **do not** submit required quality data (update factor 1.004): **$1,998.41** (pre-temporary $2,060.22). — R13488CP Table 2.

Change in the base rate: **−$19.13 per 30-day period, −0.93%** vs CY2025 [derived from the two CMS-published rates].

### Behavior adjustments

- **Permanent: −1.023%** (factor 0.98977), applied to the CY2026 rate, covering PDGM implementation behavior for **CY2020–CY2022 only**. Reduced from the **−4.059%** proposed, after comments argued post-CY2022 behavior change was attributable to OASIS-E, HHVBP expansion and MA penetration rather than PDGM. Prior partial permanent adjustments: −3.925% (CY2023), −2.890% (CY2024), −1.975% (CY2025). Cumulative still-outstanding permanent adjustment identified for CY2020–CY2022 was −9.480% after those three. — CMS fact sheet 2025-11-28; 91 FR 41237–41238.
- **Temporary: −3.0%** (factor 0.97000), reduced from the **−5.0%** proposed. Statutorily one-year-only: "the temporary adjustment factor for CY 2026 should **not** be included in the starting payment rate for CY 2027" per §1895(b)(3)(D)(iii). Total temporary-adjustment dollars owed from CY2020–CY2022 is **$4.76 billion**; CMS has recouped only a fraction. — 90 FR 55406 (2025-12-02); CMS fact sheet 2025-11-28.

### Market basket

Market basket **+3.2%**, minus a **0.8** percentage-point productivity adjustment = **+2.4%** payment update. **+0.4%** for HHAs failing quality reporting (2.4 − 2.0). — MM14304 (2025-12-11); 90 FR 55405.

### Wage index

- Continues to use pre-floor, pre-reclassified **inpatient hospital** wage data.
- Permanent **5% cap** on any year-over-year wage index decrease (in force since CY2023); for CY2026 the cap is calculated at the **county** level as well as the CBSA level, following OMB Bulletin 23-01 delineations adopted in CY2025.
- Counties whose capped value differs from their CBSA use a **5-digit "50xxx" transition code** on the claim. The CY2026 transition-code county list is Table 6 of R13488CP and is also a tab in the CY2026 wage index file. Some counties that needed a code in CY2025 no longer do in CY2026.
- Labor-related share **74.9%** / non-labor **25.1%**. — 91 FR 41235 (restating current policy).
— MM14304 / R13488CP (2025-11-20).

### Outliers

- **FDL ratio for CY2026: 0.37** (up from 0.35 in CY2025; the proposed rule had 0.46). — 90 FR 55420 (2025-12-02).
- **Loss-sharing ratio: 0.80** — Medicare pays 80% of estimated cost above the threshold.
- **National target: total outlier payments ≤ 2.5%** of total HH PPS payments (§1895(b)(5)(A)).
- **Per-agency cap: outliers ≤ 10%** of that HHA's total annual HH PPS payments; excess outliers are simply not paid, with quarterly reconciliation each February, May, August, November.
- Cost imputation: sum over disciplines of (15-minute units × wage-adjusted cost-per-unit), capped at **32 units (8 hours) per day summed across all six disciplines**; when a day exceeds 8 hours across disciplines, the lowest cost-per-unit discipline is discounted first.
— MCPM Ch. 10 §10.1.21; MM14304; 42 CFR 484.240.

**CY2026 cost-per-unit rates for outlier calculation** (R13488CP Table 5; 1 unit = 15 min):

| Discipline | Avg minutes/visit | QRP-compliant cost/unit | Non-compliant cost/unit |
|---|---|---|---|
| Home Health Aide | 63 | 19.08 | 18.70 |
| Medical Social Services | 56.5 | 75.30 | 73.83 |
| Occupational Therapy | 47.1 | 62.02 | 60.81 |
| Physical Therapy | 46.6 | 62.26 | 61.04 |
| Skilled Nursing | 44.8 | 59.25 | 58.09 |
| Speech-Language Pathology | 48.1 | 65.57 | 64.28 |

### Net rate change

CMS's own aggregate estimate for CY2026 vs CY2025: **−1.3%, −$220 million**, composed of +2.4% payment update (+$405M), −0.9% permanent adjustment (−$150M), −2.7% temporary adjustment (−$460M), −0.1% FDL update (−$15M). — CMS fact sheet, 2025-11-28.

At the base-rate level the change is **−$19.13 / −0.93%** per 30-day period.

### Other CY2026 items

- Case-mix weights, functional levels, comorbidity subgroups and LUPA thresholds all recalibrated on **CY2024 claims as of 2025-07-11**.
- Non-routine supplies remain **bundled** into the 30-day rate; there is no separate NRS conversion factor under PDGM. DME furnished as a home health service is still paid on the DME fee schedule and sits outside the 30-day amount. — MM14304; 42 CFR 484.205(f).
- Disposable NPWT device payment CY2026: **$282.10** (CY2025 $276.57 × 1.02, from CPI-U 2.7% − 0.7% productivity).
- **Rural add-on: none.** No rural add-on appears anywhere in the CY2026 final rule or the CY2027 proposed rule; the BBA-2018 rural add-on schedule ended with CY2022. Confirmed by absence in both rule texts; the statutory sunset itself is **UNVERIFIED** against the statute in this pass.
- **Effective dates:** rule effective **2026-01-01**; CY2026 rates apply to claims with **Through dates on or after 2026-01-01** (R13488CP req. 14304.2); Pricer implementation date **2026-01-05**.

---

## 5. CY2027 proposed rule (CMS-1844-P) — YES, it has been published

**It exists and the comment window is still open as of today.**

- **Federal Register citation: 91 FR 41216**, published **2026-07-06**, pp. 41216–41327, document number 2026-13602, RIN 0938-AV80.
- **Comment deadline: 2026-08-31.**
- CMS fact sheet: https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-home-health-prospective-payment-system-proposed-rule-fact-sheet-cms-1844-p
- Full text: https://www.federalregister.gov/documents/full_text/text/2026/07/06/2026-13602.txt

### Proposed rate

| Component | Value |
|---|---|
| Starting rate (CY2026 **without** temporary adjustment) | $2,101.26 |
| × Case-mix weights recalibration budget-neutrality factor | 1.0045 |
| × Wage index budget-neutrality factor | 1.0009 |
| × CY2027 payment update factor (+2.1%) | 1.021 |
| = pre-temporary 30-day rate [derived] | $2,156.98 |
| × Temporary adjustment factor (−3.0%) | 0.97000 |
| = **proposed CY2027 30-day period payment** | **$2,092.27** |

The $2,092.27 figure is corroborated by trade summaries; the arithmetic above reproduces it exactly from CMS's stated factors. Non-QRP-compliant CY2027 rate **[derived, ≈$2,051.29]** using the 0.1% update — **UNVERIFIED** against the rule's Table 26.

### Proposed adjustments and updates

| Item | CY2026 final | CY2027 proposed |
|---|---|---|
| Market basket | +3.2% | **+3.1%** |
| Productivity adjustment | −0.8 pp | **−1.0 pp** |
| Payment update | +2.4% | **+2.1%** (0.1% for non-QRP) |
| Permanent behavior adjustment | −1.023% | **none proposed** |
| Temporary behavior adjustment | −3.0% | **−3.0%** |
| Case-mix recalibration BN factor | 1.0052 | 1.0045 |
| Wage index BN factor (30-day) | 1.0025 | 1.0009 |
| Wage index BN factor (per-visit) | 1.0005 | 0.9997 |
| Outlier FDL ratio | 0.37 | **0.29** |
| Base 30-day rate | $2,038.22 | **$2,092.27** |

**No permanent adjustment for CY2027.** CMS says it is holding the permanent-adjustment calculation to CY2020–CY2022 data as finalized in CY2026: "we propose to not apply a permanent adjustment to the CY 2027 payment rate." It nonetheless publishes an *illustrative* −4.062% figure showing what a CY2020–CY2025 permanent adjustment would be, and notes the temporary-adjustment balance grew because CY2025 was paid at $2,057.35 rather than the budget-neutral $2,036.29. — 91 FR 41238–41239.

### Proposed recalibration and structural changes

- Case-mix weights, **functional impairment levels**, **comorbidity subgroups**, and **LUPA thresholds** all recalibrated on **CY2025 claims as of 2026-03-15**.
- **LUPA thresholds:** 18 groups decline by one visit, 2 groups increase by one visit; thresholds to be re-updated in the final rule on more complete CY2025 data. Proposed table = Table 24.
- **Comorbidity subgroups:** 21 low, 100 high interaction subgroups (Tables 21 and 22), also to be posted on the HHA Center page.
- **No change to the 432-group architecture, the 12 clinical groups, the three functional levels, the three comorbidity tiers, or HIPPS construction.**
- **RFI on a home-health-specific wage index** — CMS continues to use hospital wage data for CY2027 but is soliciting input on building an HH-specific index. This is the one item that could materially restructure geographic payment in future years.
- **RFI / discussion on palliative care as a home health service**, following the FY2027 Hospice rule RFI (91 FR 17359).
- **HH QRP** changes and alignment work with the expanded **HHVBP** model.
- **Medicare-wide provider enrollment** provisions: retroactive revocations and broadened revocation/denial grounds.
- **DME benefit expansion** for certain external infusion pumps and associated home infusion drugs; DMEPOS F2F clarification for replacement items; DMEPOS CBP country-of-origin collection.

### Proposed aggregate impact

**+2.4%, +$420 million** vs a projected CY2026 baseline of $17.575 billion, taking CY2027 spend to roughly $18 billion. Composed of +2.1% payment update (+$370M) and +0.3% from the FDL update (+$50M). — 91 FR (proposed rule, Regulatory Impact Analysis).

### Proposed CY2027 per-visit rates

CMS states the method (CY2026 per-visit × 0.9997 × 1.021) but publishes the table as an image. **[derived]**, ±$0.02 from CMS's rounding:

| Discipline | CY2027 proposed per-visit [derived] |
|---|---|
| Home Health Aide | ≈$81.78 |
| Medical Social Services | ≈$289.51 |
| Occupational Therapy | ≈$198.77 |
| Physical Therapy | ≈$197.42 |
| Skilled Nursing | ≈$180.62 |
| Speech-Language Pathology | ≈$214.60 |

Do not hard-code these. The final rule (expected ~Nov 2026) will restate them with updated market basket data — CMS explicitly reserves the right to change the market basket and productivity figures in the final rule.

---

## 6. Other mechanics that change episode economics

### Notice of Admission (NOA) and the late-NOA penalty

- **One NOA per admission**, not per period: "The NOA is a one-time submission to establish the home health period of care and covers contiguous 30-day periods of care until the individual is discharged." A new NOA is required only after a discharge is reported. — 42 CFR 484.205(j)(1); MCPM Ch. 10 §10.1.10.3.
- **Timely = submitted to AND accepted by the MAC within 5 calendar days after the start of care date.** — 42 CFR 484.205(j)(1); MCPM §10.1.10.3.
- **Prerequisites to submit:** physician/allowed-practitioner written or verbal orders containing the services required for the initial visit, and the initial visit made / patient admitted. — 42 CFR 484.205(j)(2).
- **Penalty (42 CFR 484.205(j)(3)):**
  1. Medicare does not pay for the days from start of care to the NOA filing date;
  2. the wage- and case-mix-adjusted 30-day period payment is **reduced by 1/30th for each day** from the SOC date until the NOA filing date;
  3. **no LUPA payments** are made for visits falling in the late-NOA window;
  4. the reduction cannot exceed the total payment of the claim;
  5. the non-covered days are **provider liability** and **must not be billed to the beneficiary**.
- MCPM adds that the reduction applies to the period payment **including outlier payment**.
- **Exceptions (four grounds, 42 CFR 484.205(j)(4) / MCPM §10.1.10.3):** (1) fire/flood/earthquake or similar events damaging the HHA's ability to operate; (2) a CMS or MAC systems issue beyond the HHA's control; (3) newly certified HHA notified late of certification or awaiting its MAC user ID; (4) other circumstances the MAC or CMS deems beyond the HHA's control. Request exception via the claim **Remarks** field, with modifier **KX** appended (MCPM §40.2).
- **Documented sub-case:** an NOA filed within 5 days but returned for correction due to an inadvertent error (e.g. a changed MBI) qualifies if the HHA shows original submission date, return/acceptance date, and that it resubmitted within **two business days** of availability (or cancelled within two business days and refiled within two business days of the cancellation finalizing). MACs will **not** grant MBI-change exceptions where the change was accessible to the HHA more than two weeks before admission.
- **Transfers:** the NOA carries **condition code 47** when another HHA may have an open admission period. — MCPM §40.1.
- Whether the late-NOA reduction is appealable: **UNVERIFIED**. The regulation frames it as a payment reduction and provider liability; no appeal-rights language was located in 42 CFR 484.205 or MCPM Ch. 10.

### Occurrence code 50

- **Required on every HH claim.** The HHA enters occurrence code 50 with the **OASIS assessment completion date (OASIS item M0090)** for the assessment corresponding to that period.
- Missing OC 50 → claim is **Returned to Provider (RTP)**, unless condition code **DR** is present (disaster waiver of OASIS reporting), in which case the provider-submitted HIPPS is used and the claim/OASIS matching is bypassed.
- With OC 50 present, a **matching assessment must be found in iQIES** or the claim will not process. The assessment must have OASIS M0100 Reason for Assessment = **01, 03, 04, or 05**. Matching keys include M0010 (CCN) and M0063 (Medicare number).
- Common failure modes CMS names: OASIS submitted after the claim; assessment inactivated; claim matched to a non-payment RFA; OC 50 date not equal to the M0090 date.
- The claims system uses OC 50 to fetch the OASIS items that drive the functional level: "For each 30-day period of care, the Medicare claims processing system looks for occurrence code 50 on the claim to correspond to the M0090 date of the applicable assessment." — 91 FR 41228.
— MCPM Ch. 10 §10.1.10.4 and §40.2.

**Platform implication:** OASIS completion → iQIES acceptance is a hard gate ahead of billing. Schedule the assessment and its transmission, not just the visit.

### PEP — partial period payment adjustment

- Triggered by exactly two situations: (a) the patient is **discharged and readmitted to the same HHA within the same 30-day period**, or (b) the patient **transfers to another HHA during a 30-day period**. — 42 CFR 484.235; MCPM Ch. 10 §10.1.15.
- Signalled on the claim by **Patient Discharge Status code 06**. Pricer then computes the proration.
- **Proration formula:** days of service ÷ 30, where days of service = total days counted **from and including the day of the first billable service to and including the day of the last billable service**. (Not calendar days of the period — service-span days.)
- Remit coding: Group CO / CARC B20 / RARC N120.
- **Death exception:** if the beneficiary dies during a period, **full** payment is made and PEP does **not** apply, because no further home care can occur in that period. Claim Through date = date of death; the claim may be submitted before day 30. — MCPM §10.1.16.
- LUPA interaction: **UNVERIFIED** in the sources reviewed — MCPM does not state explicitly how a PEP and a LUPA stack. (Operationally a LUPA period is paid per visit and the PEP proration is a proration of the *period* payment, so the two should be mutually exclusive in effect, but this was not confirmed against a primary source.)

### Transfer and discharge/readmission rules

- **Transfer:** receiving HHA submits an NOA with **condition code 47**. The prior admission period is **automatically closed** in Medicare systems as of the date services began at the receiving HHA; the new admission period opens the same day; the last claim in the closed period is **pro-rated**. The receiving HHA must document that it told the beneficiary the prior HHA will stop receiving Medicare payment, that it checked a Medicare inquiry system, and that it contacted the initial HHA on the effective transfer date. — MCPM §10.1.13.
- **Discharge and readmit to the same HHA in the same 30 days:** first payment is **pro-rated**; a new NOA may open a new admission period if the CCN matches; the next period starts on the date of the first readmission service, **resetting the 30-day clock**. — MCPM §10.1.14.
- **Inpatient stays do not force discharge.** If the HHA does not discharge and the patient returns within the same 30-day period, the same period continues. If the HHA **does** discharge expecting non-return and the patient returns in the same period, "the discharge is not recognized for Medicare payment purposes" — all services before and after the inpatient stay go on **one claim**.
- **Inpatient stay spanning the end of a 30-day period:** no discharge required. Bill the next period as if contiguous — From date = day 31 even if it falls inside the inpatient stay, with the first visit date after hospital discharge. Medicare allows the HH claim to overlap the inpatient claim on days with no HH visits. — MCPM §10.1.14.
- Two agencies must **never** both bill as primary for the same beneficiary in the same admission period. — MCPM §10.1.5.1.

### Outlier payments

Covered in §4 above. Key operational points for a scheduling platform: outliers are computed from **15-minute units** of actual visit time, capped at **32 units/day across all disciplines**; the HHA submits nothing to claim one; and the **10% agency-level annual cap** means outlier revenue is not linear — high-utilization scheduling can hit a wall that is only resolved in quarterly reconciliation.

### Review Choice Demonstration (RCD) — current status

Source: https://www.cms.gov/data-research/monitoring-programs/medicare-fee-service-compliance-programs/prior-authorization-and-pre-claim-review-initiatives/review-choice-demonstration-home-health-services — page last modified **2026-07-14**; most recent substantive update posted **2025-09-16** (updated statistics).

- **Active.** Effective **2024-06-01** CMS extended RCD for home health services **an additional 5 years** (i.e. through approximately **2029-05-31**; the page does not state an explicit end date — **the exact end date is UNVERIFIED**).
- **States: Illinois, Ohio, Texas, North Carolina, Florida, Oklahoma.** No national expansion; no additional states added since Oklahoma (effective 2023-12-01).
- **Initial choices are now two, not three:** (1) **Pre-claim review**, (2) **Postpayment review**. Choice 3 (Minimal Review with 25% Payment Reduction) was **removed** as part of the 2024 extension. Providers who do not select default to **Choice 2, postpayment review**.
- After a 6-month cycle, HHAs meeting a **90% full provisional affirmation rate** on a minimum of 10 requests/claims unlock reduced-review options (spot-check of a small claim sample).
- Statutory authority: §402(a)(1)(j) of the Social Security Amendments of 1967. RCD "does not alter the Medicare home health benefit."
- Administered by **Palmetto GBA**; provider portal handles choice selection. Contact: homehealthrcd@cms.hhs.gov.

---

## 7. Therapy under PDGM

**Therapy volume no longer drives payment. Full stop.**

"Beginning in CY 2020, section 1895(b)(4)(B)(ii) of the Act **eliminated the use of therapy thresholds** in calculating payments for CY 2020 and subsequent years. Prior to implementation of the PDGM, HHAs could receive an adjustment to payment based on the number of therapy visits provided during a 60-day episode of care." — 91 FR 41229 (2026-07-06).

**What replaced it:** the six case-mix variables — admission source, period timing, clinical group (from principal diagnosis), functional impairment level (from OASIS M1800–M1860 + M1033), comorbidity adjustment, and the LUPA visit-count threshold. Resource use is measured with a **cost-per-minute + NRS** approach built from HHA cost reports (CY2026 weights used **2022** cost report data), so therapy *minutes* still influence the statistically estimated weights across the fleet — but an individual agency cannot raise an individual period's payment by adding therapy visits.

**Where therapy volume still moves money, and only here:**
1. **Crossing the LUPA threshold.** A therapy visit that takes a period from 2 visits to 3 in a group with threshold 3 converts a per-visit payment into a full period payment. That single visit can be worth well over $1,000.
2. **The LUPA add-on.** In an initial/only LUPA period, whether the first visit is PT (1.6225), OT (1.7238), SLP (1.6696) or SN (1.7200) changes the add-on multiplier applied to that visit's per-visit rate.
3. **Outliers.** Therapy 15-minute units count toward imputed cost for outlier qualification, subject to the 32-unit/day cap.
4. **Discipline mix in a LUPA.** SLP ($210.25) vs SN ($176.96) vs HH aide ($80.12) per visit — in a LUPA, which discipline goes changes revenue by up to 2.6×.

CMS tracks "therapy only" periods (all visits PT/OT/SLP) and monitors visits per period by discipline; the CY2027 proposed rule notes HHAs "have reduced visits under PDGM in CY 2025" and that the CY2025 base rate of $2,057.35 was "approximately 34 percent more than the CY 2025 estimated 30-day period cost of $1,532.84" (91 FR 41226). Expect continued downward rate pressure justified on that gap.

---

## 8. Numbers you can hard-code vs numbers that must be reference data

### Hard-code — structural, statutory, or stable across many years

| Value | Why it's safe |
|---|---|
| 30-day payment period; 60-day certification period | 42 CFR 484.205(b)(2); 424.22(b)(1) — statutory/regulatory structure |
| 432 case-mix groups = 4 × 12 × 3 × 3 | Unchanged since CY2020; CY2027 proposes no change |
| The 12 clinical group names and their HIPPS letters A–L | Unchanged since CY2020 |
| HIPPS 5-position construction and all position value maps | MCPM Ch.10 §10.1.9; unchanged since CY2020 |
| 3 functional levels (low/medium/high) driven by OASIS M1800–M1860 + M1033 | Structure stable; the *point thresholds* are not (see below) |
| 3 comorbidity tiers (none/low/high) | Structure stable |
| Early/late definition and the **60-day gap** rule | Unchanged since CY2020 |
| Admission source = **14-day** prior inpatient window; the five facility types | Unchanged since CY2020 |
| LUPA rule: 10th percentile of visits, **floor of 2** | 83 FR 56492; unchanged since CY2019 |
| Outlier loss-sharing ratio **0.80** | Unchanged since 2010-era policy; CMS restates each year |
| Outlier national target **2.5%**; agency cap **10%** | §1895(b)(5)(A) statutory / long-standing |
| Outlier unit = **15 minutes**; **32 units (8 hrs)/day** cap | MCPM §10.1.21; long-standing |
| NOA due **5 calendar days** after SOC; penalty **1/30th per day**; no LUPA pay in the late window; provider liability | 42 CFR 484.205(j) |
| NOA is **one per admission**, not per period | 42 CFR 484.205(j)(1) |
| PEP triggers (transfer; discharge+readmit same HHA same period), **discharge status 06**, formula = service-span days ÷ 30 | 42 CFR 484.235; MCPM §10.1.15 |
| Death → full payment, no PEP | MCPM §10.1.16 |
| Transfer = condition code **47**; occurrence codes **50 / 61 / 62** | MCPM Ch.10 §40 |
| **Rate year = claim "Through" date** | R13488CP req. 14304.2 and every prior year's equivalent |
| Therapy thresholds abolished by §1895(b)(4)(B)(ii) | Statutory, CY2020 onward |
| QRP non-compliance penalty = **−2.0 percentage points** on the update | §1895(b)(3)(B)(v), statutory |

### Reference data — CMS recalibrates or re-sets these annually; version them by CY

| Value | CY2026 | Refresh source |
|---|---|---|
| National standardized 30-day period payment | $2,038.22 (QRP) / $1,998.41 (non-QRP) | Annual rule + MLN/transmittal |
| All 432 case-mix weights | 0.5364–1.9558 | `cy{YEAR}-hh-pdgm-case-mix-weights-lupa-thresholds.zip` |
| All 432 LUPA thresholds | 2–5 visits | same ZIP (CSV) |
| Per-visit (LUPA) rates by discipline | 6 values | Transmittal Tables 3–4 |
| LUPA add-on factors | SN 1.7200 / PT 1.6225 / SLP 1.6696 / OT 1.7238 | Transmittal Table 7 |
| Outlier cost-per-unit by discipline | 6 values | Transmittal Table 5 |
| Outlier FDL ratio | 0.37 | Annual rule (proposed 0.29 for CY2027) |
| Market basket %, productivity adjustment, payment update % | 3.2 / 0.8 / 2.4 | Annual rule |
| Permanent behavior adjustment | −1.023% | Annual rule (none proposed for CY2027) |
| Temporary behavior adjustment | −3.0% | Annual rule — **one-year-only by statute; never carry forward** |
| Case-mix recalibration BN factor; wage index BN factors | 1.0052 / 1.0025 / 1.0005 | Annual rule |
| Wage index values by CBSA, 5% cap, 50xxx transition county list | annual file | CY wage index file |
| Labor-related share | 74.9% | Annual rule |
| Functional impairment **point values and per-clinical-group score thresholds** | recalibrated on CY2024 data | Annual rule tables |
| Comorbidity **subgroup lists** (which ICD-10 codes, which pairs) | 20 low / 98 high | Annual rule tables + HHA Center page |
| dNPWT payment amount | $282.10 | Annual rule |

### Architectural guidance

1. **Load the CMS ZIP, don't transcribe the rule.** The 432-row CSV inside `cy{YEAR}-hh-pdgm-case-mix-weights-lupa-thresholds.zip` is the single source of truth for weights and thresholds. The Federal Register prints the same table only as a TIFF image, and — as documented in §3 — the CY2026 preamble narrative about how many thresholds changed **contradicts** the published file. Trust the file.
2. **Key every rate object by calendar year and select on the claim Through date.** A period spanning a year boundary is paid entirely at the later year's rates.
3. **Never carry a temporary behavior adjustment across years.** §1895(b)(3)(D)(iii) forbids it, and CY2027's math starts from $2,101.26 (the pre-temporary CY2026 rate), not $2,038.22. A naive year-over-year model that compounds the −3% will be wrong by ~3%.
4. **Model the LUPA threshold as a per-HIPPS integer, not a global constant.** Thresholds range 2–5 and shift group-by-group every year; ~10% of groups moved between CY2025 and CY2026.
5. **Treat the comorbidity and functional-scoring logic as an external grouper, not as in-app rules.** The lists and point values are re-derived annually from regression output. For claim-accurate results, use the CMS HH Grouper / Pricer rather than reimplementing: WebPricer at https://webpricer.cms.gov/ and Pricer source code at https://www.cms.gov/pricersourcecodesoftware (MCPM Ch. 10 §70).
6. **Expect a CY2027 final rule around November 2026** that will change every reference-data value in the table above. Build the annual refresh as a first-class operation.

---

## 9. Open items / not verified in this pass

- Appeal rights (if any) for the late-NOA payment reduction — **UNVERIFIED**.
- Explicit interaction of a PEP adjustment with a LUPA period — **UNVERIFIED**.
- The exact statutory sunset date of the rural add-on — **UNVERIFIED** (confirmed only by absence from CY2026 and CY2027 rule text).
- The precise RCD demonstration end date implied by the 2024-06-01 five-year extension — **UNVERIFIED** (CMS page states "an additional 5 years" without a date).
- CY2027 proposed per-visit rates and non-QRP 30-day rate are **[derived]** from CMS's stated factors, not read from the rule's image tables.
- CY2027 case-mix weight / LUPA threshold data file is **not yet posted** to the CMS case-mix weights page as of 2026-08-18.
- MedPAC's CY2026 home health margin analysis was not reviewed (out of scope for payment mechanics; relevant if the platform needs a margin narrative).

---

## Source index

| # | Source | URL | Date |
|---|---|---|---|
| 1 | CY2026 HH PPS Final Rule (CMS-1828-F), 90 FR 55342 | https://www.federalregister.gov/documents/2025/12/02/2025-21767 | pub. 2025-12-02, eff. 2026-01-01 |
| 2 | CMS fact sheet, CY2026 HH PPS Final Rule | https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-home-health-prospective-payment-system-final-rule-cms-1828-f | 2025-11-28 |
| 3 | CMS Transmittal R13488CP / CR 14304 (CY2026 rate tables) | https://www.cms.gov/files/document/r13488cp.pdf | 2025-11-20 |
| 4 | MLN Matters MM14304 | https://www.cms.gov/files/document/mm14304-home-health-prospective-payment-system-cy-2026-rate-update.pdf | 2025-12-11 |
| 5 | CY2026 Final HH PDGM Case-Mix Weights and LUPA Thresholds (ZIP: XLSX + CSV) | https://www.cms.gov/files/zip/cy2026-hh-pdgm-case-mix-weights-lupa-thresholds.zip | CY2026 |
| 6 | CMS HH PPS Case-Mix Weights landing page (all years) | https://www.cms.gov/medicare/payment/prospective-payment-systems/home-health-pps/home-health-pps-case-mix-weights | retrieved 2026-08-18 |
| 7 | CY2027 HH PPS Proposed Rule (CMS-1844-P), 91 FR 41216 | https://www.federalregister.gov/documents/2026/07/06/2026-13602/calendar-year-2027-home-health-prospective-payment-system-hh-pps-rate-update-requirements-for-the-hh | pub. 2026-07-06, comments close 2026-08-31 |
| 8 | CMS fact sheet, CY2027 HH PPS Proposed Rule | https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-home-health-prospective-payment-system-proposed-rule-fact-sheet-cms-1844-p | 2026-06/07 |
| 9 | Medicare Claims Processing Manual, Ch. 10 — HHA Billing | https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c10.pdf | TOC Rev. 13089, 2025-02-21 |
| 10 | 42 CFR 484.205 — Basis of payment (incl. NOA at (j)) | https://www.ecfr.gov/current/title-42/section-484.205 | current 2026-08-18 |
| 11 | 42 CFR 424.22 — Requirements for home health services (cert/recert/F2F) | https://www.ecfr.gov/current/title-42/section-424.22 | current 2026-08-18 |
| 12 | CMS Review Choice Demonstration for Home Health Services | https://www.cms.gov/data-research/monitoring-programs/medicare-fee-service-compliance-programs/prior-authorization-and-pre-claim-review-initiatives/review-choice-demonstration-home-health-services | page modified 2026-07-14 |
| 13 | CMS HHA Center | https://www.cms.gov/medicare/enrollment-renewal/providers-suppliers/home-health-agency-center | retrieved 2026-08-18 |
| 14 | CMS WebPricer / Pricer source code | https://webpricer.cms.gov/ · https://www.cms.gov/pricersourcecodesoftware | current |
