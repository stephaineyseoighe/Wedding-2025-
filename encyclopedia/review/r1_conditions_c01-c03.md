# Review r1 — Conditions c01–c03

Files: `records/cond_c01.py` (DLD, DCD, GAD) · `records/cond_c02.py` (EBSA, Separation Anxiety, Social Anxiety) · `records/cond_c03.py` (PTSD/CPTSD, RAD, DSED).
Reviewer date: 27/09/2026. All three files pass `check_records.py` after edits.

## Changes

| file | entry | field | before (short) | after (short) | reason / source |
|---|---|---|---|---|---|
| cond_c01 | DLD | recommendations | "Robust vocabulary instruction has the strongest school-level evidence base (Ebbels et al., 2019)" | Ebbels et al. set out universal/targeted/specialist tiers; don't claim "strongest" without checking | Overstated. Ebbels et al. (2019) is a pathways paper and does not rank vocabulary teaching as the strongest evidence |
| cond_c01 | DLD | recommendations | "Communication Supporting Classroom Observation Tool" | "Communication Supporting Class**rooms** Observation Tool" | Correct tool name (Dockrell et al., 2015) |
| cond_c01 | DLD | red_flags (disclosure) | "Follow Children First procedures the same day" | + report to Tusla as soon as practicable; telling the DLP does not discharge the duty; supervision follows action | Safety wording standard in the brief |
| cond_c01 | DCD | red_flags (bruising) | "…report to Tusla as soon as practicable…" | + "telling the DLP does not discharge a mandated person's duty" | Safety wording standard |
| cond_c01 | DCD | prevalence | Lingam: "under 2% … check exact figures" | 1.7% (119/6,990) DCD; further 222 (~3%) probable DCD | Checked against the Lingam et al. (2009) abstract (Europe PMC): 17 per 1,000 children |
| cond_c02 | EBSA | recommendations (REFER) | "when absence exceeds 20 days … school must report 20+ days (s.21)" | NEPS referral wording ("more than 20 days", attributed to NEPS 2023) kept separate from the statutory duty: notify EWO at an aggregate of **not less than 20** school days, s.21(4) | Two different thresholds had been merged into one. Statute: s.21(4) "not less than 20" (irishstatutebook); NEPS guide p.23 "absent more than 20 days" |
| cond_c02 | EBSA | explain_parent | "report absences **over** 20 days" | "once a child has missed 20 days **or more**" | Wrong statutory threshold. s.21(4) |
| cond_c02 | EBSA | pathway.refer_to | "once absence passes 20 days … 20+ regardless" | NEPS referral wording attributed; statutory notification at 20 or more, s.21(4) | As above |
| cond_c02 | EBSA | next | "where absence exceeds 20 days" | "where absence has reached 20 days or more in the school year" | As above |
| cond_c02 | EBSA (all) | several + citation | "NEPS, c. 2023" | "NEPS, 2023"; citation note "Guide dated 2023; check current version" | Read the gov.ie PDF: title "Managing Reluctant Attendance and School Avoidance Behaviour: A Good Practice Guide for Primary Schools". The layout is dated 10/2023 and the guide has Appendix B "My Views about School", D "My Being in School Plan" and E "Steps in a Gradual Return". It also cites West Sussex for the cycle and the Autism Good Practice Guidance (2022). All confirmed |
| cond_c03 | PTSD | prevalence | Lewis: "around 31% … around 7.8% … check" | 31.1% trauma, 7.8% PTSD by 18; only 20.6% of those with PTSD got professional help | Checked against the Lewis et al. (2019) abstract (Europe PMC) |
| cond_c03 | PTSD | prevalence (sex ratio) | "higher in girls in both Alisic (2014) and Lewis (2019)" | Alisic figures given (32.9% girls/interpersonal vs 8.4% boys/non-interpersonal); Lewis sex difference hedged "check" | The Lewis abstract gives no sex difference, so this could not be verified. The Alisic figures are from its abstract |
| cond_c03 | PTSD | cooccurring (self-harm) rate | "elevated (Lewis 2019) — rate not stated" | 48.8% self-harm, 20.1% suicide attempt among lifetime PTSD (Lewis et al., 2019) | Figures from the Lewis abstract |
| cond_c03 | PTSD | bands.Adolescent | "Around 7.8% … check before quoting" | "7.8% …" | Verified |
| cond_c03 | RAD | prevalence (overall) | "Minnis ~1.4% deprived urban … will be far lower in general population" | 1,646 children aged 6–8, 1.40% (95% CI 0.94–2.10); authors: "not rare" in this population; rate elsewhere not established | "Far lower" was unsupported speculation. The figure is correct but needed its age range |
| cond_c03 | RAD | bands.Early Years prevalence | "around 1.4% … (Minnis 2013)" | Rate for this band not stated; Minnis figure is for 6–8s | **Wrong band**: the Minnis sample was aged 6–8, not 0–5 |
| cond_c03 | RAD | bands.School Age prevalence | "Rate not stated here" | ~1.4% of 6–8s in a deprived urban UK area (Minnis 2013); not general population | Moved to the correct band |
| cond_c03 | RAD | prevalence (school age bullet) | "new first diagnoses are uncommon" | RAD can be present at 6–8 (Minnis 2013); not only an early-years question | Internal consistency with Minnis |
| cond_c03 | DSED | what_it_is | "(Kumsta et al., 2010; Rutter et al.)" | "(Kumsta et al., 2010)" | Removed a dangling, uncited "Rutter et al." |

## Checked and confirmed correct (no change)

- **Codes:** DSM-5-TR F80.2 Language Disorder; ICD-11 6A01.2 DLD (sub-codes 6A01.20–.23, already hedged). F82 / ICD-11 6A04 DCD. F41.1 / 6B00 GAD. F93.0 / 6B05 Separation Anxiety. F40.10 / 6B04 Social Anxiety. 6B40 PTSD, 6B41 CPTSD (ICD-11 only). 6B44 RAD. 6B45 DSED.
- **Statistics:**
  - Norbury et al. (2016): 7.58% DLD; 2.34% language disorder associated with ID or a medical condition (checked against the abstract).
  - Tomblin et al. (1997): 7.4%.
  - DSM-5-TR DCD: 5–6% of 5–11-year-olds.
  - Polanczyk et al. (2015): any anxiety disorder 6.5%.
  - DSM-5-TR Separation Anxiety: about 4% of children; 1.6% of adolescents; 0.9–1.9% of adults; 4-week duration; 3 of 8 criteria.
  - DSM-5-TR Social Anxiety: US 12-month prevalence about 7%; median onset 13, mostly 8–15; must occur in peer settings; "performance only" specifier.
  - DSM-5-TR GAD: 6 months; one associated symptom for children.
  - Alisic et al. (2014): 15.9% (abstract).
  - Minnis et al. (2013): 1.40% (abstract).
  - DSM-5-TR RAD: evident before 5, developmental age at least 9 months, autism excluded. DSED: at least 2 of 4 features, no before-5 criterion.
  - Tusla 2022/23: over 110,000 primary and 65,000 post-primary pupils missed 20 or more days (Tusla report; RTÉ 19/05/2025).
- **Irish law and guidance:**
  - Education (Welfare) Act 2000: compulsory attendance from age 6; home education must be registered with Tusla; s.21(4) threshold is "not less than 20".
  - Reduced school days guidelines (Department of Education, 2021).
  - Autism Good Practice Guidance for Schools (2022).
  - Jigsaw serves ages 12–25.
- **Citations checked** (author, year, journal, volume and pages):
  - DLD and DCD: Bishop 2016 PLOS ONE; Bishop 2017 JCPP; Norbury 2016; Tomblin 1997; Ebbels 2019; Conti-Ramsden & Botting 2008; Dockrell 2015; Bryan 2007; Blank 2019 DMCN; Lingam 2009; Smits-Engelsman 2013; Kirby 2010; Missiuna & Pollock 2000.
  - Anxiety: James 2020 Cochrane; Dugas 1998; Creswell 2017 Lancet Psychiatry; Lebowitz 2013 and 2020; Chorpita 2000; Spence 1998.
  - EBSA: Berg 1969; Kearney & Silverman 1990; Kearney 2002 and 2008; Egger 2003; Heyne 2019; Elliott & Place 2019.
  - Social anxiety: Clark & Wells 1995; Leigh & Clark 2018; Kagan 1984; Clauss & Blackford 2012; NICE CG159.
  - Trauma: Brewin 2017; Ehlers & Clark 2000; Maynard 2019; Anda 2020; Hobfoll 2007; Felitti 1998; Jones 2012 Lancet; Lewis 2019; NICE NG116.
  - Attachment: Zeanah & Gleason 2015; Zeanah et al. 2016; Woolgar & Baldock 2015; Granqvist 2017; Chaffin 2006; Sonuga-Barke 2017; Kumsta 2010; NICE NG26.
- **Safety wording:** the GAD, EBSA, Separation Anxiety and c03 CP_ROUTE text already met the standard (report to Tusla as soon as practicable, DLP does not discharge the duty, supervision follows action).

## Could not resolve (left as is, flagged)

- PSI / CORU clause numbers used inline: PSI 4.2.2 (DCD), 4.5.1 (RAD), 4.1.2, 2.2.1, 2.2.3; CORU 5.44, 5.45. I had no source to verify them — check them against the PSI and CORU codes.
- Norbury (2016) sex ratio and DSM-5-TR DCD sex ratio: already hedged; not verified.
- Kearney (2008) peak ages (school entry, 10–11): already hedged "check".
- Whether "My Thoughts About School" (NEPS, cited in c01/c03) is a separate current NEPS resource from "My Views about School" (Appendix B of the 2023 guide) — check the URL and title before quoting.
- Mental Health Act 2001 amendment status (GAD `law` field): already hedged.
