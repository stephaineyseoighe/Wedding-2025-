# R6 review: records/cond_c17.py, cond_c18.py, cond_c20.py

Reviewer: adversarial fact-check pass, 27/09/2026. All three files pass `python3 check_records.py`.

## Changes

| file | entry | field | before (short) | after (short) | reason / source |
|---|---|---|---|---|---|
| cond_c17 | Epilepsy | code | "ICD-11 code — check (Chapter 08)" | ICD-11 8A60–8A6Z (Chapter 08), verify subtype | ICD-11 MMS block "Epilepsy or seizures" |
| cond_c17 | Epilepsy | prevalence | "over 45,000 … check; no Irish child figure" | over 45,000 incl. approx. 10,000 children (Epilepsy Ireland, estimate) | epilepsy.ie (figure confirmed, child estimate added) |
| cond_c17 | Cerebral palsy | code | "ICD-11 code — check" | 8D2 block; 8D20 spastic, 8D20.0 unilateral, 8D20.1 bilateral | ICD-11 MMS |
| cond_c17 | Cerebral palsy | prevalence (RISK) | multiple births attributed to Oskoui 2013 | Oskoui for preterm/LBW only; multiple births "register data — check" | Oskoui 2013 reports by GA/BW; multiple-birth attribution not verified |
| cond_c17 | Cerebral palsy | red_flags (safeguarding) | "to the DLP and Tusla the same day" | report to Tusla as soon as practicable + inform DLP; supervision follows action | Brief's safety wording / Children First 2015 |
| cond_c17 | Spina bifida | code | "may place it in Chapter 20 … verify" | ICD-11 LA02 Spina bifida, Chapter 20 (NOT Ch 08 as Part D lists) | ICD-11 MMS LA02 |
| cond_c17 | Spina bifida | red_flags (safeguarding) | "DLP and Tusla the same day" | Tusla as soon as practicable + DLP; supervision follows action | Brief's safety wording |
| cond_c17 | Spina bifida | what_it_is | "Primary prevention is folic acid (MRC 1991)" | folic acid reduces risk (MRC 1991, trial in women with a previous affected pregnancy) | MRC trial was of recurrence (secondary) prevention |
| cond_c18 | Muscular dystrophy | what_it_is | "Most boys are within the typical range" | many in typical range; distribution shifted down; substantial minority ID | Mean FSIQ ≈1 SD below mean (Cotton et al., 2001) makes "most in typical range" an overstatement |
| cond_c18 | Muscular dystrophy | cooccurring (SpLD) | "(Hinton et al., 2004; Ricotti …)" | "(Ricotti et al., 2016)" | Hinton 2004 not in reference list — dangling citation removed |
| cond_c18 | Muscular dystrophy | red_flags (abuse) | no "supervision follows" | + "Act first; supervision follows." | Brief's safety wording |
| cond_c18 | Muscular dystrophy | in-text + citations | Birnkrant 2018a / 2018c | 2018a / 2018b; "(Check author list)" removed | APA 7 letters run a, b across the list; author lists for Parts 1 and 3 verified |
| cond_c18 | ABI | prevalence (Ireland) | "service-level estimates … check" | about 450 children/yr moderate–severe TBI (CHI et al., 2023 — estimate) | CHI/NRH/ABII/BTI strategic direction paper, 2023 |
| cond_c18 | ABI | citations | CHI et al. 2023 "(Check exact title and authorship)" | title confirmed, publisher/URL added, author order flagged | childrenshealthireland.ie news page and PDF |
| cond_c20 | Relational problems | what_it_is | "Other Conditions and Problems That May Be…" | "Other Conditions That May Be a Focus of Clinical Attention" | DSM-5-TR chapter title; matched the code field |

## Checked and confirmed correct (no change)

- Epilepsy: Fisher 2014 (ILAE definition; Epilepsia 55(4) 475–482); Fisher 2017 and Scheffer 2017 (Epilepsia 58(4)); **Fiest et al. 2017 active epilepsy 6.4/1,000** (Neurology 88(3) 296–303); Aaberg 2017 (~0.66% at age 10; Pediatrics 139(5)); Reilly 2014 (80% ≥1 comorbidity; Pediatrics 133(6)); Masur 2013; Binnie 2003; NICE NG217 (2022); **Circular 0030/2014 = SNA scheme circular**; learner-driver age 17; RSA medical fitness.
- CP: Rosenbaum 2007 definition quote and DMCN Suppl 109; Palisano 1997; Eliasson 2006; Hidecker 2011; **Oskoui 2013 2.11/1,000 live births**; **Novak 2012 proportions (ID ~1 in 2; epilepsy ~1 in 4; pain ~3 in 4; blind 1 in 10 vs deaf 1 in 25)**; Novak 2017 (<6 months corrected age, MRI/GMA/HINE); Rosenbaum & Gorter 2012; Jones et al. 2012 Lancet.
- Spina bifida: Copp 2015; Dennis & Barnes 2010; Dennis et al. 2006; Adzick 2011 (MOMS — reduced shunting); MRC 1991 citation details.
- DMD: **Mendell 2012 1 in 5,017 male births** (Ann Neurol 71(3)); **Cotton 2001 mean FSIQ ~1 SD below, VIQ<PIQ**; Hinton 2000; Banihani 2015; Ricotti 2016; Colvin 2018; Mercuri 2019; ICD-10 G71.0; non-progressive cognitive profile; newborn screening not routine in Ireland.
- ABI: Anderson 2005 / 2011; Ylvisaker 2005 / 2007; Babikian & Asarnow 2009; **Patricios 2023 (Amsterdam): most children recover within 4 weeks, 24–48 h relative rest, return-to-learn before full return to sport**; ICD-11 Chapter 22.
- FASD: **SIGN 156 (2019) categories (with / without sentinel facial features; "at risk") and ≥3 severely impaired domains**; **DSM-5-TR ND-PAE in Section III, recordable as Other Specified Neurodevelopmental Disorder (F88)**; **Lange 2017 7.7/1,000, Europe highest**; Lange 2013; Popova 2017; Cook 2016; Kable 2016; Streissguth 2004 (protective factors); NICE QS204 (2022).
- Children in care: **Child Care Act 1991 s.4 voluntary care, s.13 ECO, s.17 ICO, s.18 care order (Tusla has parent-like control and may consent to medical/psychiatric examination and assessment), s.19 supervision order**; **Child Care (Amendment) Act 2007 (s.43A enhanced authority for long-term foster carers)**; **Child Care (Amendment) Act 2015 (aftercare)**; Foster Care Regulations 1995; DSM-5-TR relational Z62.x codes; ICD-11 Chapter 24; Sebba 2015 authors/findings; McGilloway 2012; Tusla–DES joint protocol 2017; Virtual School Heads under Children and Families Act 2014 (England).
- Psychosis: DSM-5-TR duration criteria; schizophrenia lifetime 0.3–0.7%; ICD-11 6A20/6A23/6A24; NICE CG155 (2013, updated 2016); **Kelleher 2012 medians 17% (9–12) / 7.5% (13–18)**; Kelleher 2013 JAMA Psychiatry; Fusar-Poli 2012; Marshall 2005; Moore 2007; Di Forti 2019; Kapur 2003; Romme & Escher 1989; **HSE EIP Model of Care (2019)** (still hedged on exact title/age range).
- Bipolar: mania ≥7 days, hypomania ≥4 days, cyclothymia 2 years / 1 year in youth; **DSM-5-TR 12-month Bipolar I 0.6% US, Bipolar II 0.8% US; mean onset ~18**; ICD-11 6A60/6A61/6A62; Van Meter 2011 1.8%; **Moreno 2007 ~40-fold rise**; Leibenluft 2011; Kowatch 2005 (FIND); Geller 2002; Birmaher 2009; NICE CG185; DMDD cannot be diagnosed alongside bipolar disorder.
- Safety wording: epilepsy, ABI, FASD, relational (CP_ROUTE), psychosis and bipolar already compliant.

## Unresolved / left hedged

- CHI et al. (2023): author order on the cover not confirmed.
- Photosensitive epilepsy proportion, CP sex ratio, NTD rates in Ireland, DMD ID proportion: hedged in the file, left as they are.
- "Malbin (2002)" and "Eight Magic Keys": already flagged "check source"; plausible, not verified.
- PSI 4.1.2 / CORU 5.45 mapping in c20 supervision: outside what this pass could verify.
