# Review r9: Part H methods (m1–m3)

Files: records/methods_m1.py, records/methods_m2.py, records/methods_m3.py. All three pass `check_records.py` after the edits.
Reviewed 27/09/2026.

## Changes

| file | entry | field | before (short) | after (short) | reason / source |
|---|---|---|---|---|---|
| m2 | Graduated return (EBSA) | need_before | "Circular 0047/2021 requires notification to TESS, and to the NCSE where SEN" | TESS only. The NCSE portal closed 21/09/2023 and TESS now shares the information with the NCSE | Out of date. Source: NCSE / INTO summaries of Circular 0047/2021 |
| m2 | Graduated return (EBSA) | risk | "notified to TESS (and the NCSE where the pupil has SEN)" | TESS, which passes the information to the NCSE since 21/09/2023 | Same as above |
| m2 | Graduated return (EBSA) | next | "notified to TESS (and the NCSE where SEN)" | TESS is the single route since 21/09/2023 | Same as above |
| m2 | module docstring | — | "notify TESS, and NCSE where SEN" | Adds the note that the NCSE portal closed on 21/09/2023 | Same as above |
| m2 | Graduated return (EBSA) | need_before | "misses 20 school days… check exact wording of s.21" | s.21(4): the aggregate reaches 20 days or more. The NEPS guide's "more than 20" is not the statutory threshold | Education (Welfare) Act 2000 s.21(4) |
| m2 | Graduated return (EBSA) | history, frameworks, citations | "Hunt et al., 2022" with named authors | West Sussex County Council EPS (2018; updated 2022), corporate author | Could not verify the author list. The 2018 original and the 2022 update are confirmed |
| m2 | Graduated return (EBSA) | citations | NEPS guide "(2023)" | "(n.d.; PDF on gov.ie created 10/2023 — check for an earlier edition)" | The PDF's XMP CreateDate is 24/10/2023. The gov.ie asset ID suggests an earlier original. No confirmed publication year |
| m1 | Teacher consultation | history | Caplan's types given as "client-, consultee-, programme-centred and administrative" | The four correct types: client-centred case, consultee-centred case, programme-centred administrative, consultee-centred administrative | Caplan (1970) |
| m1 | Teacher consultation | history | CBC "(1992; 2nd ed. 2008)" | 1992 paper; Sheridan, Kratochwill & Bergan manual 1996; 2nd ed. 2008 | The 1st edition of the book is 1996, not 1992 |
| m1 | ABC functional analysis | theory | "Motivating operations… (Michael, 1982)" | Michael (1982) coined "establishing operation". "Motivating operation" came from Laraway et al. (2003) | Attribution |
| m1 | ABC functional analysis | frameworks | "CARR (2015) 5 Ps" | "4 Ps (predisposing, precipitating, perpetuating, protective)" | Carr's model has 4 Ps. Also contradicted m2 ("Carr's 4 Ps") |
| m1 | ABC functional analysis | how | "review in 4–6 weeks" | Adds "a working default, not a policy requirement — check your service's cycle" | A review-cycle default was presented without a hedge |
| m3 | Group intervention | evidence, why_this | Werner-Seidler: "somewhat larger for targeted than universal" | Targeted beat universal for depression specifically. Small effects overall | Werner-Seidler et al. (2017) abstract |

## Checked and confirmed (no change)

- **Classroom observation:**
  - Barker & Wright (1951); Barker (1968)
  - Bijou, Peterson & Ault (1968) JABA 1(2)
  - Powell, Martindale & Kulp (1975) JABA 8(4), including the direction of bias for partial-interval, whole-interval and momentary time sampling
  - Hintze (2005) SPR 34(4), 507–519
  - Volpe et al. (2005): seven coding schemes
  - Shapiro (2011) workbook; Cooper et al. (2020)
  - Frederickson & Cline (2015)
  - Monsen & Frederickson (2008); Gameson & Rhydderch (2008)
  - Bronfenbrenner & Morris (2006)
  - NEPS BESD Continuum (2010)
  - Circulars 0013/2017 and 0014/2017 (SET model)
- **Teacher consultation:**
  - Bergan (1977); Bergan & Kratochwill (1990), four stages
  - Bergan & Tombari (1976) J School Psych 14(1), 3–14. The finding is that problem identification predicts plan implementation and outcome
  - Schein (1969/1999)
  - Wagner (2000) EPiP 16(1), 9–18; Wagner (2008) chapter
  - Sheridan, Welch & Orme (1996) RASE 17(6), already hedged
  - Noell et al. (2005) SPR 34(1)
  - Nolan & Moreland (2014)
  - Kelly (1955); Bandura (1977)
  - The review default of 6–8 weeks is already hedged as a service choice
- **ABC functional analysis:**
  - Skinner (1953)
  - Iwata et al. (1982, reprinted JABA 1994, 27(2), 197–209), with the four conditions
  - Carr & Durand (1985)
  - O'Neill et al. (1990; 3rd ed. 2015); Carr et al. (2002); Gore et al. (2013)
  - Hanley, Iwata & McCord (2003)
  - Thompson & Iwata (2007)
  - Durand & Crimmins (1988)
  - Gresham, Watson & Skinner (2001)
  - Touchette et al. (1985)
  - NEWB Code of Behaviour guidelines (2008)
- **Parent feedback:**
  - Baile et al. (2000) SPIKES; Buckman (1992)
  - Finn & Tonsager (1992, 1997); Finn (2007)
  - Kessels (2003), where the recall percentage is already hedged
  - Poston & Hanson (2010)
  - Olshansky (1962)
  - Weiner (1985)
- **Report writing:**
  - Klopfer (1960)
  - Tallent: "Aunt Fanny" (1958); 4th ed. 1993
  - Meehl (1956) Barnum; Forer (1949)
  - Harvey (1997, 2006)
  - Pelco et al. (2009)
  - Groth-Marnat & Horvath (2006)
  - Mastoras et al. (2011)
  - Lichtenberger et al. (2004)
  - GDPR Art. 15; FOI Act 2014
- **EBSA:**
  - Broadwin (1932); Johnson et al. (1941)
  - Berg et al. (1969), criteria and citation
  - The Kearney–Silverman four functions; SRAS-R (2002); Kearney (2008) CPR 28(3)
  - Heyne et al. (2019), four-way typology; Heyne et al. (2002); King et al. (1998)
  - Maynard et al. (2018) Campbell: attendance improved, anxiety effect not clear
  - Elliott & Place (2019)
  - Mowrer (1947); Wolpe (1958)
  - Circular 0047/2021 in effect from 01/01/2022
- **Group intervention:**
  - Yalom (1970; 6th ed. 2020)
  - Tuckman (1965); Tuckman & Jensen (1977)
  - Boxall nurture groups, ILEA 1969–70
  - Newton, Taylor & Wilson (1996); Frederickson & Turner (2003)
  - Durlak et al. (2011), 213 programmes; Durlak & DuPre (2008)
  - Stallard et al. (2014), PACES: health-led beat school-led
  - **MYRIAD** (Kuyken et al., 2022, EBMH 25(3), 99–109): not superior to usual provision, ages 11–16. Correct as written
  - Dishion et al. (1999)
  - Gresham, Sugai & Horner (2001)
  - Clarke, Bunting & Barry (2014) HER 29(5)
  - Wellbeing Policy Statement (2018; revised 2019)
  - Well-Being guidelines (2013 post-primary, 2015 primary)
- **Staff training:**
  - Caplan (1970)
  - **Joyce & Showers** (1980s; 3rd ed. 2002, ASCD). The transfer percentages are appropriately hedged
  - **Kirkpatrick** (1959; Kirkpatrick & Kirkpatrick 2006, 3rd ed.), four levels
  - Guskey (2000), five levels
  - Desimone (2009); Kennedy (2016) RER 86(4)
  - Sims et al. (2021) EEF, four mechanism groups; EEF PD guidance (2021)
  - Fixsen et al. (2005)
  - Knowles (1980)
  - Gathercole & Alloway (2008)
  - Hickey et al. (2017)
  - **Oide** established 2023 (01/09/2023)
  - **AIM Level 3** (training, e.g. LINC). Aistear updated 2024 is already hedged
- **Transition planning:**
  - Bronfenbrenner (1979)
  - Rimm-Kaufman & Pianta (2000)
  - Smyth, McCoy & Darmody (2004), ESRI Moving Up
  - Evangelou et al. (2008) DCSF-RR019
  - Kohler (1996; 2.0 2016); Test et al. (2009)
  - McGuckin et al. (2013), NCSE Research Report No. 14
  - Eccles et al. (1993)
  - Mo Scéal (2018)
  - **Education Passport:** optional from 2013/14 and required from 2014/15 under Circular 0045/2014, so "from 2014" is acceptable
  - HSE New Directions (2012)
  - Education (Admission to Schools) Act 2018
  - ADMA 2015, commenced 26/04/2023
  - Compulsory school age 6
  - Early intervention classes for ages 3–5
  - **AIM:** universal Levels 1–3 and targeted Levels 4–7, as described
  - **DARE 2026:**
    - under 23 on 01/01/2026
    - CAO by 01/02/2026
    - for dyslexia, two scores at or below the 10th percentile (SS 81 or below) from tests on or after 01/02/2024
    - a psychological report of any age
    - no IQ requirement
  - **EPSEN 2004:** the IEP and transition sections are not commenced. Correct and hedged

## Unresolved / for the next reviewer

- **NEPS "Managing Reluctant Attendance…" guide:** I could not confirm the original publication year. The citation is now hedged.
- **NEPS guide internals:** not checked against the PDF. This covers the appendix letters (A, B, D, F, H, I), the Step 2 key adult, the sample steps and the Step 4 CAMHS advice. The PDF could not be text-extracted in this container.
- **CORU/PSI standard numbers:** not checked against the standards text. This covers PSI 1.2.10, 3.1.8, 3.3.7 and 4.2.3, and CORU 5.38 "individual, group and organisational". It is an internal cross-reference to Reference Part B.
- **Clarke, Bunting & Barry (2014):** the actual outcomes are not summarised in the file. The file already says "read before citing".
- **Nolan & Moreland (2014):** the characterisation is reasonable but was not checked against the abstract.
- **DARE document deadline:** stated only as "a March deadline". Check the exact date in the 2026/2027 handbook.
