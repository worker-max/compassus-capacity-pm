# Capacity and Scheduling Platform: Total Cost of Ownership

Three-year cost model, low / base / high
Prepared 21 August 2026

---

## 1. Purpose and how to read this document

This is the cost side of the business case only. It does not estimate benefit.

It is written on the assumption that the benefit case has already been built and that the risk in this decision is not that the benefit is overstated but that the cost is understated. Enterprise healthcare software business cases routinely present the software licence as though it were the cost of the programme. In the model below, the licence is approximately one tenth of the three-year cost in every scenario.

Two conventions are used throughout:

- Where a figure comes from a published source, the source is named and linked.
- Where a figure is an estimate, it is labelled "Estimate" and the basis is stated. No estimate is presented as though it were a quoted price.

Much enterprise healthcare pricing is genuinely not public. Vendors in this segment sell under NDA, price by negotiation, and vary quoted rates by an order of magnitude depending on the buyer's size and urgency. Where that is the case, this document says so and gives a range with the reasoning, rather than a single number that would imply a precision that does not exist.

### Organisation parameters used

| Parameter | Value | Note |
|---|---|---|
| Annual home health revenue | $549M | Given |
| Field clinicians | ~3,000 | Given |
| Schedulers | ~300 | Given |
| Branches | ~100 | Given |
| System of record | Homecare Homebase (HCHB) | Given |
| Intake / referral | Commure | Given |
| HR system | Workday | Given |
| Vendors under evaluation | 6 to 7 | Given |
| Derived: revenue per clinician | ~$183,000 / yr | $549M / 3,000 |
| Derived: revenue per clinician-week | ~$3,812 | 48 productive weeks |

---

## 2. Headline numbers

Three-year total cost of ownership, all in, including internal labour and transition productivity loss.

| Scenario | Year 1 | Year 2 | Year 3 | Three-year total |
|---|---|---|---|---|
| Low | $3.16M | $3.19M | $2.05M | $8.4M |
| Base | $8.21M | $8.04M | $5.48M | $21.7M |
| High | $20.07M | $17.77M | $11.41M | $49.3M |

Five structural findings, which matter more than the totals:

1. Software licensing is approximately one tenth of three-year cost in every scenario: 10.7% low, 10.1% base, 9.9% high. The vendor selection decision, which is where the evaluation effort is currently concentrated, is not where the money is.
2. The single largest line in all three scenarios is internal programme labour, at 42% of base-case three-year cost, which is four times the licence. It is also the line least visible to vendors and therefore the one most often omitted from vendor-led business cases.
3. The spread between low and high is $40.9M, and 72% of it sits in four lines: internal programme labour (31%), change management (16%), implementation and integration (15%), and data readiness (10%).
4. Two of the four spread drivers are operating-model decisions the organisation controls and can settle now, before any contract: whether the capacity steward function is net-new headcount, and how much branch champion time is real.
5. The most dangerous cost is not in the model. It is the schedule risk attached to integrating with a system-of-record vendor that sells a competing scheduling product, has no public integration surface, confirms that integration fees exist, and faces no substitution pressure. Section 4.2 sets out the evidence. A six-month integration delay costs approximately $2.2M in carrying cost alone at base.

Before the totals are used: this is a cost model, not a decision. It should be read against the benefit case, and specifically against the fact that base-case cost is front-loaded while benefit ramps with the branch waves. The years in which this programme is cash-negative are Years 1 and 2, and the case for it is made in Years 3 through 5, not inside the three-year window shown here.

---

## 3. Software licensing

### 3.1 How this category actually prices

There is no single pricing convention in healthcare workforce and scheduling software. Five structures are in active use:

| Structure | Where it is used | Implication at this scale |
|---|---|---|
| Per employee per month (PEPM) | Workforce management suites, HCM-adjacent products | Most common; predictable; scales linearly with headcount |
| Per user per month, named or concurrent | Clinical and scheduling point solutions | Cheaper if only schedulers are licensed, far more if clinicians are |
| Per site / per branch | Multi-site operators | Punitive at 100+ branches unless tiered |
| Per episode / per admission / per visit | Home health specific analytics and optimisation vendors | Couples cost directly to volume; unpopular with finance |
| Flat enterprise subscription with tiers | Capacity optimisation vendors selling to health systems | Opaque; negotiated; typically the structure at 3,000-seat scale |

For an enterprise deal of this size the realistic outcome is a negotiated flat or banded enterprise subscription, with the vendor's internal model built on a PEPM or per-clinician rate that is then discounted. That means the useful analytical exercise is to establish a defensible PEPM band and then apply an enterprise discount, rather than to hunt for a list price that will not apply.

### 3.2 The hardest available anchor: a disclosed public contract at almost exactly this seat count

The City of Houston's February 2025 council packet for its UKG Kronos contract extension is the single most useful public document found, because it discloses line-item annual cost alongside explicit user counts, which almost nothing else in this market does.

| Line | Users | Annual cost | Derived PEPM |
|---|---|---|---|
| Telestaff, Houston Police Department | 3,400 | $349,524, flat FY26 to FY30 | $8.57 |
| Telestaff, Houston Airports | 1,200 | $101,506 rising to $123,497 by FY30 | $7.05 rising to $8.58 |
| UKG Pro Workforce Management | City-wide | $1,208,405 in FY26 | Not derivable; headcount not disclosed |
| Professional services | | $130,000/yr plus $48,372/yr | Separate line |

Total contract value $21.2M over five years. The contractual escalator is exactly 4.00% a year on every escalating line, which independently corroborates a reported cooperative-contract cap at 4%.

Source: [City of Houston, Kronos contract extension packet, 5 February 2025](https://www.houstontx.gov/council/committees/govtops/20250205/Kronos-Contract-Extension.pdf)

Why this matters: a 3,400-user shift-scheduling deployment at $8.57 PEPM is the closest public analogue to a 3,000-clinician scheduling deployment that exists in the public record. It is a real signed price at a real seat count, not a directory estimate.

Two caveats on using it directly. It is a public-sector cooperative-contract price, which is typically keener than a private negotiated one. And Telestaff is shift scheduling for uniformed services, which does not carry credential and licensure validation, acuity-based matching, visit routing, or geographic optimisation. It therefore sets a hard floor rather than a target.

### 3.3 Other published and derived pricing signals

| Signal | Value | Source and reliability |
|---|---|---|
| UKG Ready, time and attendance module alone | ~$7 PEPM | ([OutSail](https://www.outsail.co/post/how-much-does-ukg-cost), [CheckThat.ai](https://checkthat.ai/brands/ukg/pricing)) Reliability: moderate. Notable because it triangulates independently with the Houston actuals from a different methodology. |
| UKG Ready, mid-market suite | $20 to $27 PEPM | Same sources. Reliability: moderate. |
| UKG Pro, enterprise | $26 to $41 PEPM, second source $27 to $37 | Same sources. Reliability: moderate. |
| Full HCM plus advanced workforce management | $32 to $40+ PEPM | Same sources. Reliability: moderate. Brackets the top of the range. |
| Volume discount at ~3,000 seats | $30 to $36 PEPM versus $32 to $41 at 1,000 seats, i.e. 10% to 15% off | ([CheckThat.ai](https://checkthat.ai/brands/ukg/pricing)) Reliability: moderate, and more credible than generic SaaS discount guidance because it is vendor-specific. 3,000 seats is mid-size for a tier-one workforce vendor, not a trophy account. |
| Generic enterprise SaaS discounting | 15% to 30% off list on 2 to 3 year commitments; 30% to 60% on the largest competitive deals | ([Vendr](https://www.vendr.com/marketplace/vendr), [VendorBenchmark](https://vendorbenchmark.com/guides/saas-pricing-benchmark-by-company-size)) Reliability: moderate. Reserve the upper band for a genuinely competitive process with a credible displacement threat. |
| Federal awards, Kronos/UKG | $11.88M over 2024-08 to 2026-07, i.e. $5.94M/yr; $8.14M over 2023-10 to 2026-09, i.e. $2.71M/yr | USAspending, queried directly. Reliability: high on dollars, but seat counts are not disclosed, so no PEPM can be derived. |
| Federal awards, QGenda physician scheduling, VA | $364,407/yr; $356,299/yr; $261,170/yr across three separate VA awards | USAspending. Reliability: high on dollars. Useful as an absolute annual-contract-value band for clinician scheduling at network scale. |
| Workday at a large university | $5.7M annual licensing fee within a $265M seven-year programme; implementation services alone $47M at a comparable institution | ([Student Life](https://www.studlife.com/news/2025/12/10/breaking-down-workdays-265-million-cost), [Tone Madison](https://tonemadison.com/articles/workday-and-the-excesses-of-higher-ed-efficiency-consultants/)) Reliability: high. The $5.7M against an estimated 17,000 to 19,000 employees implies roughly $25 to $28 PEPM, consistent with the published UKG Pro band. Headcount is an estimate. |
| LeanTaaS, capacity optimisation | Approaching $150M annual contract value; nearly 200 health systems; 1,000+ hospitals and centres | ([LeanTaaS](https://leantaas.com/press-releases/leantaas-races-towards-150-million-in-annual-contract-value-cementing-its-market-leadership/), [Becker's](https://www.beckershospitalreview.com/hospital-management-administration/leantaas-races-towards-150-million-in-annual-contract-value-cementing-its-market-leadership/), [BusinessWire](https://www.businesswire.com/news/home/20240814354788/en/LeanTaaS-Races-Towards-$150-Million-in-Annual-Contract-Value-Cementing-its-Market-Leadership)) Reliability: high; a company disclosure of aggregate ACV against disclosed customer counts. |
| Derived: LeanTaaS ACV per customer | ~$750,000 per health system, or ~$150,000 per hospital or centre | Estimate. Basis: $150M divided by ~200 health systems, and separately by 1,000+ sites. Both derivations are given because the denominator changes the answer by 5x, and a multi-branch provider organisation is structurally closer to the health-system denominator than the site denominator. |
| Homecare Homebase platform | "Starts at $100 per user per month"; tier upgrades $500 to $2,000/month | ([SaaSworthy](https://www.saasworthy.com/product/homecare-homebase/pricing), [itQlick](https://www.itqlick.com/homecare-homebase/pricing)) Reliability: LOW. Directory aggregators that do not disclose methodology. Order-of-magnitude sanity check only. |
| AlayaCare, WellSky Home Health directory listings | "From $899 per user per month"; the same product also appears elsewhere at $50 per user per month | ([SoftwareFinder](https://softwarefinder.com/emr-software/alayacare/pricing), [Software Advice](https://www.softwareadvice.com/product/67949-WellSky-Home-Health/)) Reliability: VERY LOW. A 16x scatter on the same product is the tell. $899 per clinician per month at 3,000 clinicians would be $32M a year, which is not a real price. These are census-tier floors that directories have mislabelled into a per-user field. Included here specifically to warn against citing them. |

### 3.4 A structural finding that changes the shape of the model

Home health software is generally not sold per seat. It is sold per census, per episode, or by visit-volume tier.

This is the explanation for the directory scatter above: review sites have a per-user field, home health vendors do not price per user, and the resulting numbers are data-entry artefacts rather than prices.

The consequence for this evaluation is practical. If some candidate vendors price per clinician and others price per census or per episode, the proposals are not directly comparable and the cheapest-looking one may be the most expensive at this organisation's volume. Two protections are worth building into the process:

- Require every vendor to quote in their own native structure and also to restate that quote as an effective cost per clinician per month at the organisation's actual volumes. The restatement is the comparable figure.
- Build a parallel per-census or per-episode model alongside the PEPM model in this document and reconcile the two. A per-episode structure couples cost directly to admissions volume, which is attractive when volume falls and punitive when the growth case the programme is meant to enable actually lands.

### 3.5 What is genuinely opaque, and why

Four things could not be established and should be treated as open questions for the vendor process rather than modelled certainties:

1. No competitively awarded public contract for a home-health-specific capacity or scheduling platform was located. Public procurement disclosure works for hospital and municipal workforce management; home health is overwhelmingly private and for-profit, so the disclosure route does not exist.
2. No candidate vendor in this segment is a standalone public company with segment-level revenue disclosure. LeanTaaS, UKG and WellSky are privately held. HCHB is owned by Hearst Health and not reported separately. No SEC filing yields a per-seat rate for this category. HealthStream, which historically disclosed revenue per contracted subscriber, has stopped publishing that metric; the last public values date to 2015 and cover learning management rather than scheduling, so they are not a usable comparator.
3. KLAS and Gartner publish vendor performance scores, not prices.
4. No public price exists for the incumbent system of record's own scheduling module, which is the most relevant comparator of all. See section 3.6.

The practical consequence: the licence line in this model is a reasoned band, not a quote. Replace it with actual vendor proposals as soon as they exist. Do not re-baseline the rest of the model on the licence figure, because the licence is not what drives the total.

### 3.6 The comparator that is missing from the evaluation

Six or seven vendors are under evaluation. The system of record already sells a scheduling optimiser, HCHB Smart Scheduling, as a paid extension. Its price is not public and could not be established.

That option is materially cheaper on every line in this model except licence, and possibly on licence too:

| Line item | Third-party vendor | HCHB Smart Scheduling |
|---|---|---|
| Licence | Unknown, modelled $317K to $1.51M a year | Unknown, likely lower per seat as an extension to an existing contract |
| HCHB integration | $180K to $1.10M plus schedule risk | None required |
| Interface schedule risk | Six weeks to twelve months, HCHB-gated | None |
| Data extraction for the tool itself | Required | Native |
| Commercial friction with system of record | Structural | None |
| Data readiness | Still required for measurement and baselining | Still required for measurement and baselining |
| Internal programme labour | Full | Full |
| Change management | Full | Full |

The point is not that Smart Scheduling is the right answer. The internal evaluation already identifies real limitations in it, including that it is architecturally a controller that auto-decides and can override manual scheduling, which collides with a governance posture that wants human judgement retained in specific places, and that it has effectively no patient-facing coordination or communication capability.

The point is that a cost analysis which prices six third-party options and does not price the incumbent's own module is incomplete, and that roughly $1M of integration cost and the entire schedule risk in section 4.2 are avoidable in one of the available scenarios. Obtain a Smart Scheduling quote and include it as a costed comparator, even if it is expected to lose on capability. If it loses, the evaluation is stronger for having shown its price.

### 3.7 Modelled licence cost

Licensed population is assumed to be clinicians plus schedulers. The high case adds branch leadership and operations users.

| Input | Low | Base | High |
|---|---|---|---|
| Licensed seats | 3,300 | 3,300 | 3,600 |
| PEPM applied | $8 | $18 | $35 |
| Annual list-equivalent | $317K | $713K | $1.51M |
| Year 1 ramp waiver | 3 months | 1 month | none |
| Annual escalation Y2, Y3 | 3% | 5% | 7% |

| Licence cost | Year 1 | Year 2 | Year 3 | Three-year |
|---|---|---|---|---|
| Low | $238K | $326K | $336K | $900K |
| Base | $653K | $748K | $786K | $2.19M |
| High | $1.51M | $1.62M | $1.73M | $4.86M |

Basis for the PEPM selections:

- Low, $8: essentially the Houston Telestaff actual of $8.57 PEPM at 3,400 seats, rounded down slightly. This is the hardest number in the model. It assumes a narrow-scope scheduling tool at a public-sector-equivalent price with no healthcare premium, which is optimistic but not fictional.
- Base, $18: roughly double the Houston floor. The uplift is deliberate and is the healthcare and home health premium: credential and licensure validation, acuity-to-skill matching, visit routing and drive-time optimisation, per-diem and float management, and a clinical decision surface. None of that exists in municipal shift scheduling. Two independent checks support the level. First, $18 sits well below the $26 to $41 enterprise HCM band, which is correct because this is a point solution rather than a suite. Second, the resulting $713K annual figure lands within 5% of the $750K derived LeanTaaS average annual contract value per health system, which is the closest available real-world analogue for a capacity optimisation platform bought by a large provider organisation.
- High, $35: full enterprise-HCM-equivalent rate applied to a wider licensed population, on the assumption that the winning vendor prices to clinician count, concedes only the 10% to 15% discount typical at 3,000 seats rather than a competitive-deal discount, and the organisation licenses beyond the core two populations.

Three structural warnings on this line:

- Licence normally starts at contract signature, not at go-live. A 100-branch waved rollout will not have all seats in production until well into Year 2, but most vendors will bill for them from Year 1. The model reflects this. Business cases that assume licence begins at first go-live understate Year 1 by roughly a full year of licence.
- Escalation compounds. Over a realistic five to seven year platform life, a 7% escalator roughly doubles the licence. A 4% cap is demonstrably achievable: it is the contractual escalator across every escalating line in the Houston agreement. Treat 4% as the target and anything above 5% as a concession that needs justifying. Capping the escalator is usually more winnable in negotiation than moving the headline rate, and it is worth more.
- Expect roughly 10% to 15% off list at this seat count, not the 30% to 60% that generic SaaS negotiation guidance promises. Three thousand seats is mid-size for a tier-one workforce vendor. The larger discount is available only in a genuinely competitive process with a credible incumbent-displacement threat, which is worth engineering deliberately if the timeline allows.

---

## 4. Implementation and integration

### 4.1 Implementation-to-licence ratio

The services-to-software ratio in enterprise healthcare software is consistently and substantially above 1:1. The canonical evidence is EHR implementation, where the services and internal cost dwarf the software:

| Anchor | Figure | Source |
|---|---|---|
| Wake Forest Baptist, Epic go-live | $8M in Epic-related implementation expense, plus $26.6M in lost margin from volume disruption | Reported implementation and margin impact ([Becker's / industry reporting summarised at healthcareitnews.com](https://www.healthcareitnews.com/news/go-live-gone-wrong)) |
| MD Anderson, Epic implementation | Attributed a 77% drop in adjusted income to the Epic implementation period | ([Becker's Hospital Review](https://www.beckershospitalreview.com/finance/md-anderson-points-to-epic-implementation-for-77-drop-in-adjusted-income/)) |
| UKG Pro implementation | 40% to 70% of annual subscription; UKG Ready 20% to 40% | ([OutSail](https://www.outsail.co/post/how-much-does-ukg-cost), [CheckThat.ai](https://checkthat.ai/brands/ukg/pricing)) Two independent sources agree. Reliability: moderate to high. |
| UKG implementation, absolute, at 1,000+ employees | $350,000 to $1,000,000+ one-time | Same sources |
| City of Houston, professional services alongside the UKG contract | $130,000/yr plus $48,372/yr, as separate recurring lines | [Houston council packet](https://www.houstontx.gov/council/committees/govtops/20250205/Kronos-Contract-Extension.pdf) Note that professional services here are recurring, not one-time. |
| Workday implementation services at a large university | $47M against a $5.7M annual licence | ([Tone Madison](https://tonemadison.com/articles/workday-and-the-excesses-of-higher-ed-efficiency-consultants/)) Reliability: high. An extreme case, but a real one, and a reminder that the ratio has no natural ceiling. |
| Home health software, first-year total | Approximately 2x to 3x annualised subscription once implementation, migration, training and interfaces are counted | Estimate consolidated from multiple home health vendor sources. Reliability: moderate. Implies implementation alone at roughly 1x to 2x licence. |
| Typical healthcare enterprise software | Services commonly 1x to 3x first-year licence | Estimate. Basis: consistent pattern across published EHR, ERP and workforce implementation reporting; the ratio rises with number of sites, number of interfaces, and degree of process change. |

For this programme the ratio should be modelled toward the upper half of that band, for three specific reasons: 100+ branches means a waved rollout with repeated site-level effort; the integration target is a system of record that is not designed for external optimisation and sells a competing product; and the process being changed is the daily operating rhythm of 3,300 people, not a back-office function.

Modelled: 0.75x licence (low), 1.5x (base), 2.5x (high) for vendor-delivered implementation, plus separately priced integration and a separately priced advisory or systems-integration partner.

Reconciliation against the benchmark, base case: vendor implementation of $1.07M against a first-year licence of $653K is 1.6x, which sits inside the 1x to 2x band implied by the home health rule of thumb and above the 40% to 70% UKG figure, which is correct because a workforce management deployment does not carry an EHR integration or a 100-site clinical rollout. Adding the HCHB integration, the Commure and Workday interfaces, and the advisory partner brings total implementation and integration to $2.42M, or 3.4x first-year licence. That is above the general benchmark, and deliberately so. The integration and advisory lines are what the general benchmark does not contain.

### 4.2 Integrating with Homecare Homebase

This is the highest-uncertainty and highest-consequence item in the implementation category, and it deserves to be treated as a named programme risk rather than a line in a services estimate.

Answer to the direct question: yes, HCHB should be flagged as a difficult and costly integration partner. Not because of any single published fact, but because five independently verifiable conditions stack in the same direction.

#### Condition 1: there is no self-serve integration surface

HCHB has no public developer portal, no published API reference, no OpenAPI specification, and no sandbox. Its productised integration offering is branded HCHB Connect, with a third-party lane called Business Connect covering roughly sixteen functional areas including EVV, GL export, payroll and revenue cycle ([hchb.com/partners/business-connect](https://hchb.com/partners/business-connect/), [hchb.com/hchb-connect](https://hchb.com/hchb-connect)). No transport, schema or fee detail is published anywhere.

The best hard technical evidence of what an HCHB integration actually looks like is the ONC Electronic Medical Documentation Interoperability pilot with a large national home health provider. That connection used HL7 v2 ADT bidirectional messaging and HL7 CCD outbound, over SFTP inside a TCP/IP VPN tunnel. It was not a REST API. ([ONC project tracker](https://oncprojectracking.healthit.gov/wiki/pages/viewpage.action?pageId=179830829))

REST endpoints appear to exist but are thinly evidenced: a 2023 LinkedIn post attributed to HCHB's interoperability services manager references HCHB APIs and a forthcoming Epic integration, with no specification published. No evidence was found that HCHB holds ONC certification under 170.315(g)(10), the FHIR API criterion. Home health and hospice sit outside the certification mandate, so this is expected, but the consequence matters: no regulatory floor obliges HCHB to expose a standards-based FHIR API. That is strong inference rather than a verified fact, and it should be tested directly with HCHB.

One integration vendor states publicly that integrating with HCHB is notoriously difficult ([airplatform.io](https://www.airplatform.io/2023/09/06/hchb-integration/)).

#### Condition 2: integration fees exist, and the discount is a partner privilege

HCHB operates a curated recommended-partner list rather than an open marketplace. Its own page describes the benefits of partner status as including roadmap collaboration, solutions built into HCHB workflows, beta-adopter access, reduced integration fees and enhanced support ([hchb.com/hchb-recommended-partner-solutions](https://hchb.com/hchb-recommended-partner-solutions/)).

Reduced integration fees is the load-bearing phrase. It is first-party confirmation that integration fees exist as a baseline, charged to non-partners at full rate. The amount is not published anywhere. This is the single most important commercial fact in this section and the reason the high case on HCHB integration is six times the low case.

Named vendors with public HCHB integrations include Medalogix and Forcura (now merged into Mosai, so treat them as one relationship rather than two), nVoq, Swift Medical, MedBridge, Corridor, Trella Health, WorldView and Enquire CRM. Of these, only Mosai publishes a timeline: six to eight weeks from planning to go-live, with the partner's own team doing the technical work ([mosai.com/ehr-integrations](https://mosai.com/ehr-integrations)).

#### Condition 3: HCHB sells the product this programme is buying

HCHB Smart Scheduling is a paid extension in the HCHB Intelligence suite. HCHB claims it automates up to 95% of visit types and 64% of workflow tasks, with nightly optimisation plus real-time re-optimisation for admissions, reassignments and declines, and guardrails for licensure, productivity standards, territory and mileage, patient preference and continuity ([hchb.com HCHB Smart Scheduling](https://hchb.com/our-solutions/hchb-intelligence/hchb-smart-scheduling/)). The vendor product overview held internally describes the same engine with claimed coverage of 99% of home health and 97% of hospice visits, optimising labour, overtime and mileage cost against a weighted continuity score (HCHB Smart Scheduling Product Overview, November 2024).

Any third-party capacity and scheduling optimiser under evaluation is therefore a direct substitute for a revenue-generating HCHB module. Integration cooperation, data access terms, interface pricing and roadmap alignment are all being negotiated with a party whose commercial interest is served by the competing product performing poorly.

This is an inference, and it should be labelled as one: no public evidence was found of HCHB either refusing or obstructing a competitor integration. But the structure is clear. A curated partner list whose stated benefit is reduced fees, combined with a competing first-party module, makes standard-rate pricing, no roadmap access and no in-workflow embedding the realistic planning assumption. The Medalogix-style embed directly inside the clinician application is a partner privilege, and a scheduling competitor is unlikely to receive it.

This is the most reliable way for this programme to become expensive without anyone deciding to spend more money, and it is a reason to open the HCHB commercial conversation before vendor shortlisting rather than after.

#### Condition 4: HCHB has no substitution pressure

HCHB reported 351 customers, more than 418,000 users, over one million patients daily and 121.9 million annual visits, with 97.6% retention and an average customer relationship of 7.3 years, as of May 2025 ([hchb.com company profile](https://hchb.com/hchb-company-profile/)). A 2025 release claims a 44% share of the Medicare home health market ([hchb.com](https://hchb.com/homecare-homebase-releases-impact-model-and-dashboards-to-support-agency-strategy/)). Hearst acquired an 85% stake in December 2013; terms were undisclosed ([hearst.com](https://www.hearst.com/-/hearst-corporation-agrees-to-acquire-an-85-stake-in-homecare-homebase-llc)).

KLAS characterises HCHB's position bluntly: retention is very high largely because no alternative offers comparable functionality at large-organisation scale, while customers report a below-average experience relative to cost and the lowest support ratings in the segment ([KLAS vendor page](https://klasresearch.com/vendor-ratings/homecare-homebase/61511), summarised in [TechTarget](https://www.techtarget.com/searchhealthit/news/366579268/Epic-Systems-Among-the-Leading-Home-Care-EHR-Vendors)). Full KLAS scores are paywalled and could not be retrieved.

The negotiating implication: the organisation has no credible threat to leave, and HCHB knows it.

#### Condition 5: the read path is workable, but it is the customer's problem

There is a pragmatic route to HCHB data. An HCHB consultancy describes helping agencies that already have, or need to set up, an HCHB log-shipping database, positioned as the way to centralise HCHB data with other systems ([dccforme.com](https://www.dccforme.com/hchb-analytics)). That is SQL Server transaction-log shipping into a customer-controlled read-only replica, which gives near-real-time direct SQL access to the schema. It is the cheapest high-fidelity extraction path available and should be the assumed design.

No public pricing, setup fee, or contractual eligibility information for log shipping was found. The packaged alternative is HCHB Analytics, a premium add-on with tiered viewer, analyst and builder roles ([hchb.com/hchb-analytics](https://hchb.com/hchb-analytics/)); its list price is also not public.

#### Cost estimate for the integration

Practical consequences to price for:

| Item | Basis | Low | Base | High |
|---|---|---|---|---|
| HCHB interface build, log-shipping replica, HCHB-side fees and certification | Estimate. Basis: general healthcare interface build cost of $48K to $58K per interface plus hidden maintenance ([enter.health](https://www.enter.health/post/hl7-fees-explained-expensive-costs-how-to-avoid)), multiplied for a multi-domain bidirectional integration covering visits, roster, capacity and status write-back; scaled up for confirmed but unpublished HCHB integration fees at non-partner rate, HL7 v2 and SFTP era transport rather than REST, and a vendor with pricing power and no substitution pressure. Third-party implementation estimates for HCHB range $5K to $50K+ ([itqlick](https://www.itqlick.com/homecare-homebase/pricing)) and $30K to $500K setup ([enzo.health](https://www.enzo.health/resource/homecare-homebase)); both are SEO-derived extrapolations, not HCHB rates, and are used only to bound the order of magnitude | $180K | $450K | $1.10M |
| Commure and Workday interfaces | Estimate. Basis: two further interfaces at the same per-interface benchmark, with Workday the simpler of the two | $90K | $200K | $420K |
| Vendor implementation services | 0.75x / 1.5x / 2.5x first-year licence | $238K | $1.07M | $3.78M |
| Advisory or systems-integration partner | Estimate. Basis: independent partner for process design, branch rollout and vendor management across a 100-branch waved deployment | $250K | $700K | $1.60M |
| Total implementation and integration | | $758K | $2.42M | $6.90M |

Phasing used: 70% Year 1, 25% Year 2, 5% Year 3, reflecting a waved rollout across roughly 100 branches rather than a single go-live.

#### Schedule risk, which is the larger exposure

The ONC pilot cited above was estimated at several months of work for a single developer, but ran roughly a year in elapsed time. The gap between effort and elapsed time is the whole risk. Where HCHB development or interoperability resources sit on the critical path, the constraint is their queue, not the work.

Plan on six to eight weeks as the best case, which is the only published partner figure, and twelve months or more as the realistic worst case if HCHB resources gate the build.

A six-month integration delay does not merely postpone benefit. It holds the internal programme team, the change team and the vendor implementation team in place while they wait, and it does so while the licence clock runs. Year 1 base-case burn is $8.21M, or roughly $684,000 a month. Not all of that is exposed to a delay, but the carrying cost of the internal team, change team and licence alone is approximately $370,000 a month at base, so a six-month slip is a $2.2M event before any benefit deferral is counted. That is larger than the entire modelled HCHB integration cost in the high case, which is why the schedule question in the list below matters more than the fee question.

#### Five questions to force into the process before signature

1. What does HCHB charge a non-partner third party for an interface, per connection and per transaction, and does that fee escalate?
2. Can the organisation obtain or already hold an HCHB log-shipping replica, at what cost, and under what contractual terms on use of the data?
3. Does any HCHB contract term restrict third-party use of extracted data for competing optimisation? This is a contractual question, not a technical one, and it is far cheaper to answer now.
4. What is HCHB's committed lead time for third-party interface work, and will it commit to a date?
5. Is the candidate vendor an HCHB recommended partner? If it is, it gets reduced fees, workflow embedding and roadmap access. If it is not, it does not. That distinction is worth real money and should be a scored criterion in the evaluation.

Note on evidence quality: no HCHB fee schedule, developer portal, sandbox, partner certification document or log-shipping price is public. Extensive searching, including practitioner forums, returned nothing. That absence is itself the finding. Integration terms here will be established bilaterally and privately, which removes the buyer's ability to benchmark, and it is why the high case on this line is six times the low case rather than the two-to-three times that a normal interface estimate would carry.

---

## 5. Data readiness

### 5.1 The problem being priced

The organisation's own material describes three conditions that make optimisation impossible until they are fixed:

- Systems are not real-time.
- The clinician application runs on Citrix with manual synchronisation.
- Productivity data must be exported to Excel before it is usable.

Each of these is a distinct cost, and they are cumulative rather than alternative.

One clarification worth making before pricing, because it changes what can be fixed and what cannot. External evidence indicates that the Citrix dependency and the sync latency are two separate problems in two separate places:

- The HCHB back office, which is where scheduling, billing and reporting are done, is delivered through a Citrix thin client hosted by HCHB. This is confirmed by HCHB's own scheduling documentation, which describes the browser-based Web Scheduling console as a read-and-surface layer only, with schedulers continuing to act in the legacy Citrix consoles, and it is corroborated by current user reviews and vendor infrastructure reporting.
- PointCare, the clinician field application, is a native mobile application rather than a Citrix-delivered one, and its offline model is store-and-forward: the device holds the record locally and synchronises on reconnect ([Google Play listing](https://play.google.com/store/apps/details?id=com.hchb.pc.ui), [hchb.com FAQs](https://hchb.com/faqs/)).

If the organisation's own material describes the clinician application as running on Citrix, that is worth verifying internally before design begins. It may reflect a locally chosen deployment, a legacy configuration, or loose language for the sync behaviour. The distinction matters because a Citrix dependency in the back office is an architectural property of the system of record that no third-party vendor can remove, whereas sync latency in the field application is a measurable number that can be characterised, designed around, and in part improved.

Either way the consequence for a capacity platform is the same and it is severe. Optimisation requires knowing, during the day, which scheduled visits have actually been completed. Field-captured data is not available server-side until it syncs, so any integration reading visit data inherits that latency. If completion status only becomes visible after a delay, the optimiser is planning against a schedule rather than against reality, and a schedule counts visits that will never happen. This is precisely the gap the platform exists to close, and it cannot be closed by the platform alone.

The first analytical task of this programme, before any vendor is selected, is to measure the actual distribution of the gap between visit completion and system visibility. That measurement determines whether the product being bought is an intraday capacity instrument or a next-day reporting tool, and those are different products at different prices with different benefit cases.

### 5.2 What has to be built

| Workstream | What it is | Why it cannot be skipped |
|---|---|---|
| Extraction layer | Reliable, scheduled extraction from HCHB at visit grain, plus roster from Workday and referral from Commure | Excel export is not a data source; it has no lineage, no schedule and no reconciliation |
| Cloud data platform | Warehouse or lakehouse, ingestion tooling, orchestration, monitoring | Nothing downstream is repeatable without it |
| Visit-grain fact model | One row per visit with status, weight, discipline, geography, timestamps | Capacity maths is meaningless above visit grain; branch-level rollups hide the variance that the programme exists to manage |
| Status latency remediation | Closing or measuring the gap between visit completion and system visibility | Determines whether the platform can operate intraday or only next-day. This single decision changes the product's value proposition |
| Reference and geospatial data | Postal geography, drive-time or distance API, territory definitions | Route and travel modelling is a large share of home health capacity; without real distance the optimiser produces plausible-looking nonsense |
| Data quality remediation and historical backfill | Cleaning roster, FTE, discipline, territory and status fields; backfilling history for baselining | Without a clean baseline, benefit cannot be measured, and an unmeasurable benefit is an unrenewed contract |

### 5.3 Modelled data readiness cost

| Input | Low | Base | High |
|---|---|---|---|
| Data engineers (FTE) | 3.0 | 5.0 | 7.0 |
| Build duration (years) | 0.75 | 1.0 | 1.5 |
| Fully loaded data engineer cost | $195,000 | $195,000 | $195,000 |
| Cloud platform, tooling, geospatial APIs (annual) | $120K | $260K | $520K |
| One-off remediation and backfill | $100K | $300K | $750K |
| Steady-state run FTE from Year 2 | 1.2 | 2.0 | 2.8 |

Fully loaded data engineer cost is an Estimate. Basis: US senior data engineer base salary in the $135K to $155K range, multiplied by a 1.3x loading for benefits, payroll tax, equipment and overhead, which is the standard convention for internal cost accounting.

| Data readiness | Year 1 | Year 2 | Year 3 | Three-year |
|---|---|---|---|---|
| Low | $507K | $512K | $366K | $1.38M |
| Base | $1.18M | $1.02M | $676K | $2.87M |
| High | $2.55M | $1.86M | $1.12M | $5.53M |

Sequencing warning: this work is a prerequisite, not a parallel workstream. A vendor selection that assumes the data is ready will produce a Year 1 plan that cannot execute. If the choice is made to run data readiness concurrently with vendor implementation, expect the implementation to extend and the vendor to bill for the delay.

---

## 6. Internal cost to run the programme

This is the largest cost category in every scenario and the one most often left out of vendor-led business cases entirely, because the vendor has no visibility of it and no incentive to raise it.

### 6.1 Loaded internal rates used

All figures are fully loaded: base salary plus benefits, payroll taxes and allocated overhead at approximately 1.3x base, which is the standard internal cost-accounting convention.

Every figure in this table is an Estimate. The basis in each case is a mid-to-senior US market base salary for the role multiplied by 1.3. Worked example: a clinical informaticist at roughly $138,000 base becomes $180,000 loaded.

Replace these with the organisation's own loaded-rate table, which finance will already hold and which will be more accurate than any external benchmark. If the actual loading multiplier differs materially from 1.3, this entire category scales with it, and it is the largest category in the model.

| Role | Fully loaded annual cost |
|---|---|
| Programme director | $265,000 |
| Product owner / business analyst | $175,000 |
| Clinical informaticist | $180,000 |
| Analytics and reporting analyst | $165,000 |
| Trainer / instructional designer | $145,000 |
| IT, security and interface support | $190,000 |
| Branch champion (clinical manager time) | $135,000 |
| Capacity steward (net new operating role) | $140,000 |

### 6.2 FTE by scenario

| Role | Low | Base | High |
|---|---|---|---|
| Programme director | 0.5 | 1.0 | 1.0 |
| Product owner / BA | 1.0 | 2.0 | 3.0 |
| Clinical informatics | 1.0 | 2.0 | 3.0 |
| Analytics / reporting | 1.0 | 2.0 | 3.0 |
| Training / instructional design | 1.0 | 2.0 | 4.0 |
| IT / security / interfaces | 0.5 | 1.0 | 2.0 |
| Core team annual cost | $893K | $1.79M | $2.79M |
| Branch champion FTE per branch | 0.05 | 0.10 | 0.20 |
| Branch champions, 100 branches, annual | $675K | $1.35M | $2.70M |
| Capacity stewards, net new, from Year 2 | 0 | 6 | 14 |
| Capacity steward annual cost | $0 | $840K | $1.96M |

| Internal programme labour | Year 1 | Year 2 | Year 3 | Three-year |
|---|---|---|---|---|
| Low | $1.30M | $1.57M | $1.01M | $3.87M |
| Base | $2.60M | $3.64M | $2.86M | $9.09M |
| High | $4.41M | $6.66M | $5.52M | $16.59M |

### 6.3 The two lines that are usually missing

Branch champions. A 100-branch rollout requires a named person at each branch who owns adoption locally. At 0.10 FTE of a clinical manager, that is $1.35M a year at base. Organisations almost always assume this is absorbed. It is not absorbed; it is displaced, and what it displaces is branch clinical supervision. If the intention is genuinely that it be absorbed at zero cost, that assumption should be stated explicitly in the business case so that it can be challenged, rather than left implicit.

The capacity steward. A capacity and scheduling platform does not remove the need for judgement; it relocates it. Someone has to own the capacity picture at a level above the branch, maintain the rules, arbitrate between branches, and act on what the system surfaces. In the low case this is assumed to be absorbed into existing scheduling supervision at zero net cost. In the base case it is six net-new FTE, roughly one per sixteen branches. In the high case it is fourteen. The decision between those three is a real operating-model decision, not a modelling assumption, and it is worth $1.96M a year at the top end. It should be resolved before signature, not after go-live.

---

## 7. Change management

### 7.1 Benchmark

| Anchor | Figure | Source |
|---|---|---|
| Most common change management allocation | 10% of total project budget | ([Prosci](https://www.prosci.com/blog/how-to-budget-for-change-management)) |
| Projects over $10M budget | Approximately $2.5M on change management | ([Prosci](https://www.prosci.com/blog/how-to-budget-for-change-management)) |
| Typical dedicated change resource | Approximately 4.6 full-time people | ([Prosci](https://www.prosci.com/blog/how-to-budget-for-change-management)) |
| Correlation with success | Projects with effective change management are approximately 7x more likely to meet objectives; 88% met or exceeded objectives; 81% came in on or under budget | ([Prosci](https://www.prosci.com/blog/the-correlation-between-change-management-and-project-success)) |

### 7.2 Why 10% is the wrong number here

A prior scheduling pilot at this organisation failed for change-management reasons. That fact changes the calculation in three ways, and each of them costs money:

1. The population being asked to change has already been asked once and has already learned that the change did not hold. The starting position is not neutral; it is negative. Rebuilding credibility costs more than establishing it.
2. Field clinician and scheduler behaviour in home health is driven by autonomy, territory, earnings and trust in coverage. A scheduling optimiser touches all four simultaneously. This is not a systems change with a training component; it is an operating-model change with a systems component.
3. The organisation's own stakeholder analysis identifies clinician archetypes whose drivers are fixed rather than shapeable. Where a driver is fixed, the system must be designed to work around it. That is design cost and configuration cost, incurred before training begins.

The model therefore prices change management at 10% in the low case, which is the Prosci baseline, and at 16% base and 22% high, treating it as the critical path rather than a supporting workstream.

The percentage is applied to licence, implementation, data and internal labour, with a 1.15x weighting in Year 1 to reflect front-loaded readiness work and 0.55x in Year 3 as the programme moves to sustainment.

| Change management | Year 1 | Year 2 | Year 3 | Three-year |
|---|---|---|---|---|
| Low (10%) | $296K | $259K | $96K | $651K |
| Base (16%) | $1.13M | $961K | $391K | $2.48M |
| High (22%) | $3.36M | $2.61M | $1.05M | $7.03M |

A useful cross-check: the base case lands at $2.48M over three years, which is within 1% of Prosci's observed figure of approximately $2.5M spent on change management by organisations running projects with budgets over $10M. The percentage was raised for programme-specific reasons, but the resulting absolute number is exactly what comparable organisations actually spend on comparable programmes. That is reassuring in both directions: it suggests 16% is not inflated, and it suggests the 10% benchmark is being read against smaller projects than this one.

What that money buys, at base: a dedicated change lead, roughly four to five change and communications practitioners, which matches Prosci's observed average of about 4.6 dedicated people, plus role-based training design and delivery for approximately 3,300 people, at-the-elbow support during each branch wave, an adoption measurement capability, and the branch champion network costed separately in section 6.

The cheapest place to lose this programme is here, and the second-cheapest is to fund it at 10% because that is what the benchmark says, when the benchmark does not know about the prior failed pilot.

---

## 8. Ongoing run cost

Costs that persist after go-live, over and above the licence and its escalation.

| Component | Basis | Low | Base | High |
|---|---|---|---|---|
| Premium support and service-level uplift | Estimate. Basis: premium support tiers commonly add 15% to 25% of base platform cost in healthcare integration and platform contracts ([Redox pricing analysis, tactionsoft.com](https://www.tactionsoft.com/blog/redox-integration/)) | 10% of licence | 18% of licence | 25% of licence |
| Payer-rules library maintenance | Estimate. Basis: a large multi-branch home health provider carries a substantial book of payer contracts, each with authorisation, visit-frequency and coverage rules that change on renegotiation. Rules must be re-encoded in the platform on each change or the optimiser schedules non-reimbursable work | 0.5 FTE at $160K | 1.5 FTE | 3.0 FTE |
| Annual CMS reference-data refresh | Estimate. Basis: CMS recalibrates PDGM case-mix weights, LUPA thresholds, functional impairment levels and comorbidity subgroups annually, across 432 payment groups, in each calendar-year Home Health PPS final rule ([CMS CY2026 final rule fact sheet](https://cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-home-health-prospective-payment-system-final-rule-cms-1828-f), [CY2027 proposed rule fact sheet](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-home-health-prospective-payment-system-proposed-rule-cms-1844-p)). This is a guaranteed annual event with a fixed deadline, not a contingency | $35K | $90K | $190K |
| Version upgrades and regression testing | Estimate. Basis: two to four vendor releases a year, each requiring regression testing of the HCHB interface and of any configured rules | $40K | $120K | $300K |

| Ongoing run | Year 1 | Year 2 | Year 3 | Three-year |
|---|---|---|---|---|
| Low | $86K | $188K | $189K | $462K |
| Base | $298K | $585K | $591K | $1.47M |
| High | $766K | $1.37M | $1.40M | $3.54M |

Year 1 is weighted at 40% because most of these costs begin at go-live rather than at contract signature.

The payer-rules line is the one that surprises people. It is not a project cost; it is a permanent operating obligation created by the decision to automate scheduling. Before automation, a payer rule change is absorbed by schedulers applying judgement. After automation, it is a configuration change that must be made correctly and on time, in a system, by someone accountable for it. The obligation does not go away, it becomes explicit and it acquires a headcount.

---

## 9. Productivity dip during transition

### 9.1 Documented magnitude and duration

| Anchor | Figure | Source |
|---|---|---|
| Clinical productivity, first 90 days post-go-live | Drops 20% to 50% | Industry implementation guidance ([billingparadise.com](https://www.billingparadise.com/blog/epic-ehr-adoption-trends-2026/), [clindcast.com](https://www.clindcast.com/epic-go-live-checklist-and-what-healthcare-organizations-often-miss/)) Reliability: moderate; consistent across multiple independent implementation advisories |
| Physician productivity, first 3 to 6 months | Drops 20% to 30% | Same sources |
| Time to return to baseline | 6 to 12 weeks for most units; 4 to 6 weeks fastest; 8 to 14 weeks for ambulatory and specialty | Same sources |
| Wake Forest Baptist, Epic | $8M implementation expense plus $26.6M lost margin from interim volume disruption | ([healthcareitnews.com](https://www.healthcareitnews.com/news/go-live-gone-wrong)) Reliability: high; a named organisation with a disclosed financial figure |
| MD Anderson, Epic | 77% drop in adjusted income attributed to the implementation | ([Becker's Hospital Review](https://www.beckershospitalreview.com/finance/md-anderson-points-to-epic-implementation-for-77-drop-in-adjusted-income/)) Reliability: high; organisation's own attribution |

### 9.2 Adjusting the benchmark to this programme

The EHR benchmarks above describe a full clinical documentation system replacement. A capacity and scheduling platform is a narrower change: the clinician's documentation workflow is largely untouched, but the assignment, routing and daily plan change substantially, and the scheduler's job changes completely.

The model therefore uses a reduced magnitude and a shorter duration than the EHR benchmark, applied per branch wave rather than to the whole organisation at once.

| Input | Low | Base | High |
|---|---|---|---|
| Productivity dip | 4% | 8% | 15% |
| Duration per wave | 4 weeks | 6 weeks | 10 weeks |
| Gross revenue exposed | $1.83M | $5.49M | $17.16M |
| Contribution margin on marginal visit | 40% | 40% | 40% |
| Proportion of visits recovered by rescheduling | 50% | 45% | 30% |
| Net margin impact | $366K | $1.21M | $4.80M |

Calculation: 3,000 clinicians x duration in weeks x $3,812 revenue per clinician-week x dip percentage, converted to margin at 40% and reduced by the recovery proportion. Contribution margin and recovery proportion are Estimates; the basis is that home health visits deferred within an episode are often recoverable, whereas visits lost to missed windows and referral turn-down are not.

| Productivity loss (net margin) | Year 1 | Year 2 | Year 3 | Three-year |
|---|---|---|---|---|
| Low | $201K | $146K | $18K | $366K |
| Base | $664K | $483K | $60K | $1.21M |
| High | $2.64M | $1.92M | $240K | $4.80M |

Phased 55% Year 1, 40% Year 2, 5% Year 3 across the branch waves.

Two things this line does not capture, and which should be watched rather than modelled: referral turn-down during the dip, which is lost admissions rather than deferred visits and is therefore not recoverable at all; and LUPA exposure, where a visit-frequency disruption pushes an episode below its threshold and converts a full episode payment into a per-visit payment. Both are real, both are plausible during a scheduling transition, and neither can be estimated responsibly without the organisation's own baseline data.

---

## 10. The cost of failure at eighteen months

The scenario: the programme is halted at month 18, having gone live in some branches but not achieved the operating change.

| Scenario | Spent by month 18 | Recoverable | Written off |
|---|---|---|---|
| Low | $4.75M | $418K | $4.33M |
| Base | $12.2M | $1.00M | $11.2M |
| High | $29.0M | $2.25M | $26.7M |

Recovery assumptions: 45% of data platform and pipeline investment is reusable by a successor programme or for general analytics; 12% of integration investment survives, principally interface plumbing that a different vendor could reuse. Everything else is sunk. These are Estimates; the basis is that data infrastructure is vendor-neutral and therefore retains value, whereas vendor-specific configuration, training, change management and internal programme labour do not.

What is unrecoverable, specifically:

- Licence paid to date. Enterprise SaaS agreements at this size are typically multi-year with limited or no termination-for-convenience refund. If any portion is prepaid, assume it is gone.
- All implementation services. These are consumed on delivery.
- All change management and training. This is the largest single unrecoverable block after internal labour, and its value is entirely contingent on the change holding.
- All internal programme labour. Roughly $3.9M by month 18 in the base case.
- The productivity dip already incurred. Approximately $0.9M of margin in the base case, spent on a transition that did not complete.

What does not appear in the table, and matters more than what does:

This would be the second failed scheduling initiative at this organisation. The first failure has already raised the cost of the second, which is why change management is priced at 16% rather than 10% in section 7. A second failure would raise the cost of the third by considerably more, and would plausibly remove the option entirely for several years. That cost is real, it is large, and it cannot be put in a table. It is the strongest available argument for funding section 7 properly rather than trimming it, because change management is both the cheapest line to cut and the one whose absence caused the prior failure.

A useful framing for the investment committee: the difference between the base case and the low case in change management is $1.83M over three years. The unrecoverable write-off in the base failure case is $11.2M. Change management funded at benchmark rather than at risk-adjusted level is a $1.83M saving against an $11.2M exposure.

---

## 11. Three-year total cost of ownership

### Low case

| Line item | Year 1 | Year 2 | Year 3 | Total |
|---|---|---|---|---|
| Software licensing | $237,600 | $326,304 | $336,093 | $900,000 |
| Implementation and integration | $530,320 | $189,400 | $37,880 | $757,600 |
| Data readiness and engineering | $507,125 | $511,625 | $366,000 | $1,384,750 |
| Internal programme labour | $1,297,500 | $1,567,500 | $1,008,000 | $3,873,000 |
| Change management | $295,843 | $259,483 | $96,139 | $651,465 |
| Ongoing run and maintenance | $85,760 | $187,630 | $188,609 | $461,999 |
| Transition productivity loss | $201,300 | $146,400 | $18,300 | $366,000 |
| Total | $3,155,448 | $3,188,342 | $2,051,021 | $8,394,811 |

### Base case

| Line item | Year 1 | Year 2 | Year 3 | Total |
|---|---|---|---|---|
| Software licensing | $653,400 | $748,440 | $785,862 | $2,187,702 |
| Implementation and integration | $1,693,440 | $604,800 | $120,960 | $2,419,200 |
| Data readiness and engineering | $1,182,500 | $1,015,500 | $676,000 | $2,874,000 |
| Internal programme labour | $2,595,000 | $3,639,000 | $2,856,000 | $9,090,000 |
| Change management | $1,126,879 | $961,238 | $390,616 | $2,478,733 |
| Ongoing run and maintenance | $297,612 | $584,719 | $591,455 | $1,473,786 |
| Transition productivity loss | $664,290 | $483,120 | $60,390 | $1,207,800 |
| Total | $8,213,121 | $8,036,817 | $5,481,283 | $21,731,221 |

### High case

| Line item | Year 1 | Year 2 | Year 3 | Total |
|---|---|---|---|---|
| Software licensing | $1,512,000 | $1,617,840 | $1,731,089 | $4,860,929 |
| Implementation and integration | $4,830,000 | $1,725,000 | $345,000 | $6,900,000 |
| Data readiness and engineering | $2,553,250 | $1,856,250 | $1,118,000 | $5,527,500 |
| Internal programme labour | $4,405,000 | $6,661,000 | $5,521,000 | $16,587,000 |
| Change management | $3,364,963 | $2,609,220 | $1,054,526 | $7,028,709 |
| Ongoing run and maintenance | $766,000 | $1,374,460 | $1,402,772 | $3,543,232 |
| Transition productivity loss | $2,642,062 | $1,921,500 | $240,188 | $4,803,750 |
| Total | $20,073,275 | $17,765,270 | $11,412,575 | $49,251,120 |

### Cumulative spend

| Scenario | End of Year 1 | End of Year 2 | End of Year 3 |
|---|---|---|---|
| Low | $3.16M | $6.34M | $8.39M |
| Base | $8.21M | $16.25M | $21.73M |
| High | $20.07M | $37.84M | $49.25M |

The shape matters as much as the total. In the base case, 75% of the three-year cost is incurred in the first two years, before the branch network is fully live and before the benefit case can materially land. Any funding approval that treats this as an evenly spread three-year commitment will hit a cash problem in Year 2, which is also the year the programme is most vulnerable to being cut.

### Per-unit reference points, base case

| Measure | Value |
|---|---|
| Three-year cost per clinician | $7,244 |
| Three-year cost per branch | $217,312 |
| Three-year cost as a share of one year's revenue | 4.0% |
| Annualised cost as a share of annual revenue | 1.3% |
| Software licence as a share of three-year TCO | 10.1% |

---

## 12. What drives the spread

Total spread between low and high, three-year: $40.9M.

| Line item | Contribution to spread | Share |
|---|---|---|
| Internal programme labour | $12.71M | 31.1% |
| Change management | $6.38M | 15.6% |
| Implementation and integration | $6.14M | 15.0% |
| Transition productivity loss | $4.44M | 10.9% |
| Data readiness and engineering | $4.14M | 10.1% |
| Software licensing | $3.96M | 9.7% |
| Ongoing run and maintenance | $3.08M | 7.5% |

The four decisions that move the number most, in order:

1. Whether the capacity steward function is net-new headcount or absorbed. Worth up to $1.96M a year, and it is an operating-model choice rather than an estimate. Resolve it before signature.
2. How much branch champion time is real. At 0.05 versus 0.20 FTE per branch across 100 branches, this is a $2.0M annual swing, and it is the line most likely to be assumed away.
3. Whether change management is funded at the 10% benchmark or at a level that reflects the prior failed pilot. A $6.4M three-year swing, and the line with the highest correlation to whether the programme succeeds at all.
4. What HCHB charges for integration and what it permits. A $920K swing on the integration line alone, and an unbounded one on schedule if cooperation is slow. This is the least controllable item in the model and the one with the weakest public evidence base.

Note that software licensing is sixth of seven as a driver of the spread. The vendor selection decision, which is where most of the evaluation effort is currently going, is not where most of the cost variance lives.

---

## 13. Assumptions register

Every material assumption, in one place, so that each can be challenged individually.

| # | Assumption | Value used | Type |
|---|---|---|---|
| 1 | Licensed population is clinicians plus schedulers | 3,300 seats; 3,600 in high case | Estimate |
| 2 | PEPM band for an enterprise capacity and scheduling platform | $8 / $18 / $35 | Low is near-hard data (Houston, $8.57 at 3,400 seats). Base and high are Estimates, triangulated against LeanTaaS derived ACV and published enterprise HCM bands |
| 3 | Licence begins at contract signature, not go-live | Yes | Convention; verify in contract |
| 4 | Annual licence escalation | 3% / 5% / 7% | Estimate. A 4% contractual cap is demonstrably achievable (Houston). Holding base at 4% rather than 5% reduces three-year base licence by roughly $30K, so this matters far more over a five to seven year life than inside this window |
| 5 | Vendor implementation as multiple of first-year licence | 0.75x / 1.5x / 2.5x | Estimate; healthcare services-to-software convention |
| 6 | HCHB integration cost | $180K / $450K / $1.10M | Estimate; no public benchmark exists |
| 7 | Fully loaded internal labour multiplier | 1.3x base salary | Convention |
| 8 | Branch champion effort | 0.05 / 0.10 / 0.20 FTE per branch | Estimate |
| 9 | Net-new capacity steward FTE | 0 / 6 / 14 | Operating-model decision, not an estimate |
| 10 | Change management as share of programme cost | 10% / 16% / 22% | Prosci benchmark, adjusted upward for prior pilot failure |
| 11 | Productivity dip magnitude | 4% / 8% / 15% | Estimate; EHR benchmark scaled down for narrower scope |
| 12 | Productivity dip duration per wave | 4 / 6 / 10 weeks | Estimate; below the 6 to 12 week EHR benchmark |
| 13 | Contribution margin on marginal visit | 40% | Estimate; replace with actual |
| 14 | Visits recovered by rescheduling | 50% / 45% / 30% | Estimate; replace with actual |
| 15 | Productive weeks per clinician per year | 48 | Convention |
| 16 | Rollout phasing across branches | 55% / 40% / 5% of transition impact by year | Estimate |
| 17 | Recoverable share on failure: data 45%, integration 12% | As stated | Estimate |

The five figures most worth replacing with the organisation's own data, in priority order: contribution margin per visit, revenue per clinician, current scheduler-to-clinician ratio, actual branch count and size distribution, and the historical cost of the prior failed pilot.

---

## 14. Recommendations for the vendor process

These follow directly from the cost structure above and are intended to reduce the spread rather than the base.

1. Score HCHB recommended-partner status as an explicit evaluation criterion. HCHB states that partner status carries reduced integration fees, in-workflow embedding and roadmap access. A vendor that has it and a vendor that does not are not comparable on integration cost or schedule, and the difference is not visible in either vendor's proposal.
2. Require every vendor to quote implementation and integration as a fixed fee, not time and materials, and to name the HCHB integration approach explicitly, including the transport used, whether a log-shipping replica is assumed, and whether they have delivered it before and for whom.
3. Ask each vendor for two reference customers running on HCHB at more than 50 branches. If none can produce one, this is a first-of-type integration and should be priced and scheduled as such.
4. Negotiate the escalation cap before the headline rate. A 3% cap is worth more over the platform's life than a 10% discount at signature.
5. Tie licence commencement to go-live by branch wave, not to signature. This is a Year 1 cash item worth several hundred thousand dollars at base.
6. Open a separate, parallel commercial conversation with HCHB about data access, log-shipping terms and interface fees, before vendor shortlisting rather than after. The answer determines the data readiness cost, the integration cost, the schedule, and which vendors are viable. It is the highest-value unanswered question in the whole evaluation.
7. Measure the sync-latency distribution before selection. Whether the platform can operate intraday or only next-day is a product-definition question, and it is currently unanswered.
8. Fund and staff change management before the platform is selected. The prior pilot failed on change, and the work that matters most, understanding which clinician and scheduler behaviours are fixed and which are shapeable, does not depend on which vendor wins.
9. Decide the capacity steward operating model as a governance decision at the outset. It is the largest single controllable line in the model.

---

## 15. Sources

Pricing and market signals
- City of Houston, UKG Kronos contract extension packet, February 2025, with disclosed seat counts, annual line-item costs and the 4% escalator: https://www.houstontx.gov/council/committees/govtops/20250205/Kronos-Contract-Extension.pdf
- Federal contract awards for UKG/Kronos and QGenda, queried directly: https://api.usaspending.gov/
- UKG pricing analysis, PEPM bands and implementation ratios: https://www.outsail.co/post/how-much-does-ukg-cost
- UKG pricing, second independent source, including the volume-discount curve by employee count: https://checkthat.ai/brands/ukg/pricing
- Enterprise SaaS pricing benchmark by company size: https://vendorbenchmark.com/guides/saas-pricing-benchmark-by-company-size
- SaaS negotiation and discount benchmarks: https://www.vendr.com/marketplace/vendr
- Workday total programme cost at a large university, including annual licence fee: https://www.studlife.com/news/2025/12/10/breaking-down-workdays-265-million-cost
- Workday implementation services cost at a comparable institution: https://tonemadison.com/articles/workday-and-the-excesses-of-higher-ed-efficiency-consultants/
- LeanTaaS annual contract value and customer count: https://leantaas.com/press-releases/leantaas-races-towards-150-million-in-annual-contract-value-cementing-its-market-leadership/
- Same, secondary reporting: https://www.beckershospitalreview.com/hospital-management-administration/leantaas-races-towards-150-million-in-annual-contract-value-cementing-its-market-leadership/
- Same, primary wire release: https://www.businesswire.com/news/home/20240814354788/en/LeanTaaS-Races-Towards-$150-Million-in-Annual-Contract-Value-Cementing-its-Market-Leadership
- Healthcare workforce management PEPM band: https://vendorbenchmark.com/vendors/ukg-pro-ultimate-kronos-pricing
- HR and workforce platform pricing by company size: https://harmonyhr.org/blog/hr-software-pricing-comparison-2025.html
- Homecare Homebase directory pricing (low reliability): https://www.saasworthy.com/product/homecare-homebase/pricing
- Homecare Homebase cost analysis (low reliability): https://www.itqlick.com/homecare-homebase/pricing
- AlayaCare directory pricing (very low reliability): https://softwarefinder.com/emr-software/alayacare/pricing
- WellSky Home Health directory listing (very low reliability): https://www.softwareadvice.com/product/67949-WellSky-Home-Health/

Homecare Homebase: integration surface, partner programme, market position
- HCHB Connect overview: https://hchb.com/hchb-connect
- HCHB Business Connect, third-party vendor lane: https://hchb.com/partners/business-connect/
- HCHB recommended partner solutions, including the reduced integration fees benefit: https://hchb.com/hchb-recommended-partner-solutions/
- HCHB partner ecosystem: https://hchb.com/our-solutions/hchb-connect/hchb-partner-ecosystem/
- ONC EMDI pilot, documenting HL7 v2 ADT, CCD, SFTP over VPN and the project timeline: https://oncprojectracking.healthit.gov/wiki/pages/viewpage.action?pageId=179830829
- HCHB Smart Scheduling product page: https://hchb.com/our-solutions/hchb-intelligence/hchb-smart-scheduling/
- HCHB Analytics: https://hchb.com/hchb-analytics/
- HCHB company profile and scale figures, May 2025: https://hchb.com/hchb-company-profile/
- HCHB Medicare home health market share claim: https://hchb.com/homecare-homebase-releases-impact-model-and-dashboards-to-support-agency-strategy/
- Hearst acquisition of 85% stake, December 2013: https://www.hearst.com/-/hearst-corporation-agrees-to-acquire-an-85-stake-in-homecare-homebase-llc
- KLAS vendor rating page: https://klasresearch.com/vendor-ratings/homecare-homebase/61511
- KLAS findings summarised: https://www.techtarget.com/searchhealthit/news/366579268/Epic-Systems-Among-the-Leading-Home-Care-EHR-Vendors
- Third-party integrator commentary on HCHB integration difficulty: https://www.airplatform.io/2023/09/06/hchb-integration/
- HCHB log-shipping database, described by an HCHB consultancy: https://www.dccforme.com/hchb-analytics
- Partner integration timeline, six to eight weeks: https://mosai.com/ehr-integrations
- PointCare mobile application listing: https://play.google.com/store/apps/details?id=com.hchb.pc.ui
- HCHB FAQs, store-and-forward sync claims: https://hchb.com/faqs/
- HCHB implementation and setup cost extrapolation (low reliability): https://www.enzo.health/resource/homecare-homebase

Integration cost
- HL7 interface build and maintenance cost: https://www.enter.health/post/hl7-fees-explained-expensive-costs-how-to-avoid
- Redox pricing, contract value bands and premium support uplift: https://www.tactionsoft.com/blog/redox-integration/
- Redox marketplace pricing: https://www.vendr.com/marketplace/redox

Change management
- Prosci, how to budget for change management: https://www.prosci.com/blog/how-to-budget-for-change-management
- Prosci, correlation between change management and project success: https://www.prosci.com/blog/the-correlation-between-change-management-and-project-success
- Prosci, change management in healthcare: https://www.prosci.com/change-management-in-healthcare

Go-live productivity impact
- MD Anderson, 77% drop in adjusted income attributed to Epic implementation: https://www.beckershospitalreview.com/finance/md-anderson-points-to-epic-implementation-for-77-drop-in-adjusted-income/
- Go-live disruption, including Wake Forest Baptist figures: https://www.healthcareitnews.com/news/go-live-gone-wrong
- Go-live productivity decline and recovery timelines: https://www.clindcast.com/epic-go-live-checklist-and-what-healthcare-organizations-often-miss/
- Epic adoption and productivity impact: https://www.billingparadise.com/blog/epic-ehr-adoption-trends-2026/
- Epic go-live staffing and at-the-elbow support: https://www.trustedtalent.com/epic-staffing-strategy/

Regulatory reference data
- CMS CY2026 Home Health PPS final rule fact sheet: https://cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-home-health-prospective-payment-system-final-rule-cms-1828-f
- CMS CY2027 Home Health PPS proposed rule fact sheet: https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2027-home-health-prospective-payment-system-proposed-rule-cms-1844-p
- CY2026 final rule, Federal Register: https://www.federalregister.gov/documents/2025/12/02/2025-21767/medicare-and-medicaid-programs-calendar-year-2026-home-health-prospective-payment-system-hh-pps-rate

Vendor documents held internally
- HCHB Smart Scheduling Product Overview, November 2024
- HCHB Web Scheduling User Guide, KB0025451 v10

---

Model file: model.py in this directory. All tables regenerate from it.
