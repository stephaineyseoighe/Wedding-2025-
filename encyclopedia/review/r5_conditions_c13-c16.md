# Review r5 — Conditions c13, c15, c16

Reviewer pass: adversarial fact-check (review_brief.txt). Files: records/cond_c13.py, records/cond_c15.py, records/cond_c16.py.
All three pass `python3 check_records.py` after edits.

## Changes

| file | entry | field | before (short) | after (short) | reason / source |
|---|---|---|---|---|---|
| cond_c16.py | Hearing impairment | prevalence | "Fortnum et al. (2001) reported about 1.07 per 1,000 at birth" | 0.91 per 1,000 at age 3 (1.07 adjusted for under-ascertainment); threshold >40 dB HL better ear | Fortnum et al. (2001) BMJ abstract (PubMed 11546698): 0.91 at age 3 → 1.65 at 9–16; adjusted 1.07 and 2.05. 1.07 is NOT a birth figure |
| cond_c16.py | Hearing impairment | prevalence | "about 1.65 per 1,000 at ages 9–16" | 1.65 per 1,000 (2.05 adjusted) | same source; added adjusted figure |
| cond_c16.py | Hearing impairment | bands › Early Years › prevalence | "About 1 per 1,000 at birth … (Fortnum)" | 0.91 per 1,000 at age 3, 1.07 adjusted | same |
| cond_c16.py | Hearing impairment | bands › School Age › prevalence | "about 1.65 per 1,000" | 1.65 per 1,000, 2.05 adjusted, >40 dB HL | same |
| cond_c16.py | Hearing impairment | what_it_is (ISL) | "check commencement" | commenced 23/12/2020 | Commencement order, Dept of Children press release / Oireachtas Seanad statements 15/12/2020; CIB news 23/12/2020 |
| cond_c16.py | Hearing impairment | citations | ISL Act, "check commencement" | ISL Act 2017 (No. 40 of 2017), commenced 23/12/2020 | same |
| cond_c16.py | Glue ear | what_it_is ×2 | NICE (2008) CG60 "check for updates" | NICE (2023) NG233, which replaced CG60 | NICE NG233 (published 30/08/2023) updates and replaces CG60 — nice.org.uk/guidance/ng233 |
| cond_c16.py | Glue ear | prevalence, cooccurring ×2, red_flags, bands › Special Setting | "(NICE, 2008)" | "(NICE, 2023)" | same |
| cond_c16.py | Glue ear | citations | NICE (2008) CG60 surgical management | NICE (2023) NG233 Otitis media with effusion in under 12s | same |
| cond_c15.py | PMDD | code | "Part D lists it within 6A70–6A7Z, the depressive-disorders block" | removed | CORRECTIONS.md already records this Reference-sheet placement as an error; ICD-11 code is GA34.41 (cross-listed under depressive disorders). Repeating the old placement risked it being quoted |
| cond_c15.py | Sleep disorders | prevalence (higher-risk groups) | "(see Gringras et al., 2017; Hiscock et al., 2015)" | flagged as treatment trials, not prevalence studies | Gringras 2017 is a melatonin RCT; Hiscock 2015 a behavioural-sleep RCT — neither supports a prevalence claim |
| cond_c15.py | Sleep disorders | bands › Special Setting › prevalence | "see Gringras et al., 2017 for autism" | noted as a melatonin treatment trial, not a prevalence source | same |
| cond_c13.py | Substance use disorders | what_it_is (severity) | "Tolerance and withdrawal from medically prescribed use do not count" | …where opioids, sedatives or stimulants are taken solely under appropriate medical supervision | DSM-5-TR limits this exclusion to those substance classes |

## Checked and confirmed correct (brief)

**c13 — addictive behaviours**
- ICD-11 6C40–6C4H (6C40 alcohol, 6C41 cannabis, 6C4A nicotine; 6C4H non-psychoactive substances); QE10 hazardous alcohol use, QE11 hazardous drug use; 6C50 gambling disorder (.0 predominantly offline, .1 predominantly online); QE21 hazardous gambling or betting; 6C51 gaming disorder (.0 predominantly online, .1 predominantly offline); QE22 hazardous gaming.
- DSM-5-TR SUD: 2 of 11 criteria in 12 months; mild 2–3, moderate 4–5, severe 6+; four criterion groups. Gambling Disorder: 4 of 9, mild 4–5, moderate 6–7, severe 8–9; manic-episode exclusion; moved from impulse control in DSM-5.
- Gaming Disorder: not a DSM-5-TR diagnosis; Internet Gaming Disorder in Section III, 5+ of 9 over 12 months. ICD-11 in effect 01/01/2022; 12-month duration, shorter if severe.
- Gambling Regulation Act 2024 (signed October 2024); Gambling Regulatory Authority of Ireland established 2025; the legal gambling age is 18. Online Safety and Media Regulation Act 2022.
- Calado, Alexandre & Griffiths (2017) J Gambl Stud 33(2) 397–424, range 0.2–12.3%; Stevens et al. (2021) ANZJP 55(6) 553–568, pooled ~3.05% (≈1.96% stringent studies).
- Citations checked: Steinberg (2008) Dev Rev 28(1); Arseneault et al. (2002) BMJ 325; Di Forti et al. (2019) Lancet Psychiatry 6(5); Faggiano et al. (2014) Cochrane CD003020; Zendle & Cairns (2018) PLOS ONE; Spicer et al. (2022) New Media & Society 24(4); Karlsson & Håkansson (2018) J Behav Addict 7(4); Aarseth et al. (2017) and Rumpf et al. (2018) J Behav Addict; Orben & Przybylski (2019) Nat Hum Behav 3(2); Przybylski et al. (2017) AJP 174(3); Mazurek & Engelhardt (2013) Pediatrics 132(2); Pontes & Griffiths (2015) CHB 45; Miller & Rollnick (2013) 3rd ed.; DoH (2017) Reducing Harm, Supporting Recovery; HSE/Tusla (2019) Hidden Harm; Children First (2017); CRAFFT (Knight et al., 1999); DSM-IV-MR-J (Fisher, 2000).
- SAOR = Support, Ask and assess, Offer assistance, Refer (HSE). DES (2002) substance use policy guidelines. Planet Youth in the West. My World Survey 2 (Dooley et al., 2019).
- Safety wording: Tusla as soon as practicable; DLP does not discharge the duty; supervision follows action. Present throughout.

**c15 — sleep, SSD/FND, PMDD**
- Insomnia disorder 3 nights/week for 3 months. ICSD-3 (2014), ICSD-3-TR (2023).
- Marcus et al. (2012) OSA "roughly 1–5%": acceptable and hedged (the technical report gives 0–5.7%). AAP recommends screening for snoring. Pediatrics 130(3) 576–584 is correct for the guideline.
- Melatonin prescription-only in Ireland: correct, and the entry already says to check HPRA status. The EP boundary is held.
- Citations checked: Carskadon (2011); Crowley et al. (2007); Chervin et al. (2002); Mindell et al. (2006); Hiscock et al. (2015) BMJ 350 h68; Dewald et al. (2010); Hale & Guan (2015); Owens et al. (2000) CSHQ (age 4–10, eight subscales); Owens & Dalzell (2005) BEARS; Gringras et al. (2017) JAACAP 56(11).
- ICD-11 6C20 Bodily distress disorder; 6B60 Dissociative neurological symptom disorder; DSM-5-TR "Functional Neurological Symptom Disorder (Conversion Disorder)"; SSD typically >6 months; stressor requirement removed in DSM-5. Espay et al. (2018) JAMA Neurol 75(9); Stone (2016) Pract Neurol 16(1); Kozlowska et al. (2007) JAACAP 46(1); Eminson (2007) CPR 27(7).
- PMDD: ICD-11 GA34.41; ICD-10-CM F32.81; ≥5 symptoms with ≥1 core symptom; prospective ratings over ≥2 cycles; DSM-5-TR 12-month prevalence 1.8–5.8% ("roughly 2–6%", hedged). RCOG Green-top Guideline No. 48 (2016), BJOG 2017 124(3) e73–e105. Yonkers et al. (2008) Lancet 371(9619); Endicott et al. (2006) DRSP. DES/HSE/DoH (2013) Well-being in post-primary schools. Pieta 1800 247 247, Samaritans 116 123, text 50808.

**c16 — hearing, vision, glue ear**
- Mitchell & Karchmer (2004) >90% of deaf children have hearing parents: correct. Sign Lang Stud 4(2) 138–163.
- Bess et al. (1998) MSHL ≈5.4% ("about 5%", hedged); Lieu (2004); Braden (1994); Fellinger et al. (2012) Lancet 379; Hall (2017) MCHJ 21(5); Jones et al. (2012) Lancet 380; Bishop et al. (2017) CATALISE-2 (hearing loss is a differentiating condition; an OME history is not). WHO (2021) hearing grades. RISLI, Chime, Irish Deaf Society, National Cochlear Implant Programme. SIFTER (Anderson, 1989).
- ICD-11 hearing loss in Chapter 10; 9D90 Vision impairment including blindness. WHO (2019) World report on vision acuity bands (6/12, 6/18, 6/60, 3/60).
- Vision Ireland (formerly NCBI, rebranded 2023): correct. Philip & Dutton (2014); Williams et al. (2021) DMCN 63(6); Rahi & Cable (2003) Lancet 362 (most have additional impairments); Tadić et al. (2010); Hatlen (1996); Dale & Salt (2007); Warren (1994). White reflex → retinoblastoma urgent.
- Rosenfeld et al. (2016) OME guideline (≈90% before school age; most resolve within 3 months, hedged); Roberts et al. (2004); Paradise et al. (2007) NEJM 356(3); Browning et al. (2010) Cochrane CD001801.

## Not resolved / for the lead
- NEPS referral category numbers (e.g., "2.2 Behaviour during break times…" used for substance use, "5.1 Vision", "5.2 Hearing", "3.6 School attendance"). These match other records, but I could not verify them against a NEPS source. The 2.2 choice for substance use reads oddly. Check against the source list.
- CORU/PSI standard numbers (e.g., PSI 2.2.4, 1.1.4, 2.3.3) were not verified.
- ISL Act 2017: I could not fetch the statute text (403). The wording "native and independent language" is widely used, but check it against s.3 before quoting. The commencement date (23/12/2020) is verified.
- Marcus et al. (2012): the 0–5.7% range comes from the companion technical report (Pediatrics 130(3) e714–e755), not the 576–584 guideline. Left as a hedged "roughly 1–5%".
