# Review r14: presentations p5, p7 and p8

Reviewer: adversarial fact-check pass, 27/09/2026.
Files: records/pres_p5.py (20 entries), records/pres_p7.py (20), records/pres_p8.py (14).
All three pass `python3 check_records.py` after the edits.

## Changes

| file | entry | field | before (short) | after (short) | reason / source |
|---|---|---|---|---|---|
| pres_p8.py | Attendance and transitions | what_it_is[3] | Circular 0047/2021 requires notification to TESS "(and to the NCSE where the pupil has SEN)" | notify TESS only. The circular's NCSE step ended when the NCSE portal closed on 21/09/2023; TESS shares the information with the NCSE. Adds "in effect from 01/01/2022" | Out of date. Matches methods_m2.py and the r9 finding (coordinator instruction). pres_p5 and pres_p7 checked: they do not make this claim. |
| pres_p8.py | Attendance and transitions | what_it_is[3] | "notify TESS at stated absence levels" | s.21(4): absences totalling not less than 20 days in a school year | Education (Welfare) Act 2000, s.21(4) |
| pres_p5.py | EBSA | recommendations[5] | "notify Tusla Education Welfare when absences reach 20 days … check the current reporting requirements" | the principal notifies TESS (EWO) when absences total not less than 20 days in a school year (s.21(4)) | Uses the statutory wording and cites the section |
| pres_p5.py | PDA profile | what_it_is[0] | "Newson et al. (2003) first described PDA syndrome" | Newson first described it in the 1980s; Newson et al. (2003) is the first peer-reviewed journal account | Wrong attribution of priority. The 2003 Arch Dis Child paper reports work Newson began in the 1980s. |
| pres_p7.py | Medication effects | by_age[0] | "NICE (2018) advises against [stimulants] for under-5s without specialist advice" | NG87: do not offer ADHD medication to any child under 5 without a second specialist opinion from an ADHD service with expertise in young children | Restated to match the NG87 recommendation. A "second specialist opinion" is stricter than "specialist advice". |
| pres_p7.py | Chronic illness affecting school | by_age[3] | "disability supports (DSA / DARE)" | "Fund for Students with Disabilities; DARE" | DSA (Disabled Students' Allowance) is a UK scheme. Ireland uses the Fund for Students with Disabilities. |
| pres_p7.py | AIM level | what_it_is[2] + citations[0] | Government of Ireland (2016) … Inter-Departmental Group | (2015) … Report of the Inter-Departmental Group | The IDG report came out in November 2015 (aim.gov.ie PDF "Inter-Departmental-Group-Report-launched-Nov-2015"). AIM itself began in 2016. |
| pres_p8.py | RACE | what_it_is[1] | the psych-report, professional-report and cognitive-score statements cited to "section 4.1" | "sections 4.1(b) and 9.1" | The r8 reviewer read the SEC 2026 Instructions in full: psych-report and professional-report points are in s.9.1; no cognitive scores or diagnosis is s.4.1(b) |
| pres_p8.py | Continuum implemented? | what_it_is[2] | Durlak & DuPre (2008) "showed … programmes delivered with fidelity produced effects two to three times larger" | Reviewed 500+ studies. The "two to three times higher" figure comes from some of the meta-analyses they reviewed and compares careful implementation with serious implementation problems, in prevention and promotion programmes; check before quoting | Overstated. The paper reports the figure from earlier meta-analyses, not as its own finding about "fidelity", and not for school SEN support. |
| pres_p8.py | Attendance and transitions | assess[3] + citations[3] | NEPS (2023) Managing reluctant attendance … | (n.d.), check the year on gov.ie | Title confirmed (assets.gov.ie/83467 and the post-primary PDF on cypsc.ie). The 2023 date could not be confirmed and the gov.ie asset number suggests an earlier year. Hedged. |
| pres_p5.py | Truancy, Late arrival, Bullying | red_flags | "report to Tusla" | adds "as soon as practicable (telling the DLP does not discharge a mandated person's duty; supervision follows action)" | Safety standard in the brief |
| pres_p7.py | Multiple disabilities; Delayed milestones; AIM; Transition to primary; Parenting capacity (assess + red_flags); Family functioning; Housing | red_flags / assess | "Children First procedures; report to Tusla." / "Children First procedures apply." | same safety wording added | Safety standard in the brief |

## Checked and confirmed (brief)

**Irish law, circulars and policy**
- Education (Welfare) Act 2000:
  - s.21(4), "not less than 20 days".
  - Compulsory school age is 6.
- Circular 0047/2021: reduced school days, in effect 01/01/2022, notify TESS.
- Circulars 0013/2017 (primary) and 0014/2017 (post-primary): SET allocation by school profile.
- Circular 0030/2014: SNA scheme, care needs.
- NCSE (2018) Comprehensive Review of the SNA scheme.
- DES (2017) Guidelines for Primary Schools on supporting pupils with SEN.
- NEPS Continuum of Support:
  - Primary: 2007 (Guidelines for Teachers).
  - Post-primary: 2010. The "(check title and date)" hedge is harmless; the title and date are correct.
- Bí Cineálta (2024):
  - The definition paraphrase is accurate: targeted, online or offline, harm, repeated over time, imbalance of power.
  - It replaced the Anti-Bullying Procedures (2013).
- Cineáltas: Action Plan on Bullying (December 2022).
- Coco's Law is the Harassment, Harmful Communications and Related Offences Act 2020.
- Domestic Violence Act 2018 created the coercive control offence.
- Children First (DCYA, 2017):
  - Lists exposure to domestic violence as an example of emotional abuse.
  - Children with disabilities are at greater risk.
- Children First Act 2015: mandated person duty and joint report.
- Child Protection Procedures for Primary and Post-Primary Schools: 2017, revised 2023.
- Child Care (Amendment) Act 2015: aftercare needs assessment and plan.
- Traveller ethnicity was recognised in 2017.
- Equal Status Acts: nine grounds.
- AIM:
  - Seven levels (1–3 universal; 4 Better Start; 5 equipment and minor alterations; 6 therapy; 7 additional capacity).
  - LINC; needs-based; ECCE from 2 years 8 months.
- Mo Scéal (NCCA, 2018); O'Kane (2016) NCCA Research Report No. 19; First 5 (2018); HSE perinatal model of care (2017).
- DEIS Plan 2017; Wellbeing Policy Statement (2018, revised 2019); NEWB code of behaviour guidelines (2008); Primary Curriculum Framework (2023); Framework for Junior Cycle (2015); Aistear (2009); Cosán (2016); Oide (2023).
- REALT (Regional Education and Language Teams).

**RACE, against the r8 reading of the SEC 2026 Instructions**
- Scribe only in very exceptional circumstances (s.5.1).
- Trauma and adversity are outside scope (s.5.6).
- Junior Cycle scribe expected to move to a word processor or recording device (s.4.1(a)).
- Appeals to the Independent Appeals Committee, then the Ombudsman or Ombudsman for Children (s.4.1(h)).
- NEPS role (s.4.1(c)).

**Attendance and PDA frameworks**
- Heyne et al. (2019): four categories (school refusal, truancy, school withdrawal, school exclusion).
- School withdrawal is parent-driven absence.
- Berg et al. (1969) criteria.
- Kearney & Silverman (1990): four functions.
- SRAS-R (Kearney, 2002).
- Kearney & Graczyk (2014): RTI model.
- Maynard et al. (2018): attendance improved; anxiety effect unclear.
- PDA:
  - Not in DSM-5-TR or ICD-11; framed as a profile, not a diagnosis, throughout.
  - Green et al. (2018); Kildahl et al. (2021); O'Nions et al. (2014) EDA-Q.

**Clinical and DSM**
- DSM-5-TR:
  - Irritable mood can substitute for depressed mood in young people.
  - Anhedonia is one of the two core MDE symptoms.
- DSM-5-TR Z codes named correctly: relational problems; housing and economic problems; acculturation difficulty; social exclusion or rejection; target of (perceived) adverse discrimination or persecution. Codes are left as "check".
- ICD-11 codes: 6B41 CPTSD; 6B42 PGD.
- NICE guidelines: NG134 (2019); NG206 (2021), including the warning against fixed incremental graded exercise; NG217 (2022).

**Citations (author, year, journal, volume, pages) verified**
- Evans 1997; Leonard 1990; Boyer & Liénard 2006; Hume 2009; Angold 1995; Dazzi 2014; Thapar 2012; Ryan & Deci 2000; Martell 2010.
- Asendorpf 1990; Rubin 2009; Frederickson & Turner 2003; Stringaris 2018; Vidal-Ribas 2016; Leibenluft & Stoddard 2013.
- Bath 2008; Cook 2005; van der Kolk 2005; Felitti 1998; Hughes 2017; Anda 2020; Lacey & Minnis 2020.
- Klass 1996; Stroebe & Schut 1999; Worden 1996; Fazel 2012; Hobfoll 2007; Cummins 2008; Maynard 2019; Gottman 1996; SAMHSA 2014.
- Egger 2003; Kearney 2008; Pinquart & Teubert 2012; Shaw & McCabe 2008; Crowley 2007; Gottfried 2014; Heyne & Rollings 2002.
- Newson 2003; Coie 1982; Parker & Asher 1987; Olweus 1993; Salmivalli 2010; Arseneault 2010; Gaffney 2019; Schalock 2021; ABAS-3; Vineland-3.
- Bellamy 2010; Imray & Hinchcliffe 2014; Lum 2017; Pinquart & Shen 2011; Varni 2002; Loring & Meador 2004; Prevatt 2000; Ylvisaker 2001.
- Fraiberg 1975; Zeanah 2019; Powell 2014; Guralnick 2011; Shevell 2003; ASQ-3; Bellman 2013; Dockett & Perry 2007.
- Sebba 2015; Darmody 2013 (OCO); Holt 2008; Callaghan 2018; Cleaver 2011; Donald & Jureidini 2004; Carr 2012; Epstein 1978; Berry 1997; Atkinson 2002; Sloper 2004.
- Barrett 2015; Fisher 2014; Shield & Dockrell 2003; Frederickson & Cline 2015; Gickling & Armstrong 1978; Haring 1978; Rosenshine 2012; Sweller 1988; Evangelou 2008.
- Zabala 2005; Phillips & Zhao 1993; Wood 2018; Webster 2016; Sylva 2004; Melhuish 2008; Desforges & Abouchaar 2003; Bronfenbrenner 1979; Wagner 2000; Fixsen 2005; Joyce & Showers 2002; Guskey 2002.

**Boundaries and safety**
- No entry diagnoses or advises on medication.
- EBSA, low mood and irritability entries give same-day risk routes.
- The child protection entry has the full mandated-person wording.

## Unresolved

- **Rose et al. (2015), emotion coaching:** cited in the text of p5 "Complex trauma" and "Trauma-informed classroom practice" but missing from their reference lists. I was not certain enough of the journal details to add it. Next reviewer: add the full reference (Rose, Gilbert & McGuire-Snieckus, 2015) after checking.
- **Stallard et al. (2012), Kuyken et al. (2022) and Ttofi & Farrington (2011):** also cited in text without references. All three are real studies.
- **NEPS "Managing reluctant attendance…" year:** I could not open the PDF metadata. Now "n.d."; confirm the year on gov.ie.
- **Children First Act 2015, Schedule 2 wording for psychologists:** the entries assume the EP is a mandated person. That is consistent with the rest of the workbook, but the exact Schedule 2 wording was not re-checked here.
- **Durlak & DuPre (2008), "two to three times":** hedged from memory of the paper's text; confirm against the full text if the figure is to be quoted.
