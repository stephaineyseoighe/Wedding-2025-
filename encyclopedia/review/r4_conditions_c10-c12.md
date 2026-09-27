# Review r4: conditions c10–c12

Files: `records/cond_c10.py` (written expression SLD, tic disorders / Tourette's, Stereotypic Movement Disorder), `records/cond_c11.py` (OCD, BDD, trichotillomania / excoriation), `records/cond_c12.py` (Hoarding, IED, pyromania / kleptomania).
All three pass `python3 check_records.py` after the edits.

## Changes

| File | Entry | Field | Before (short) | After (short) | Reason / source |
|---|---|---|---|---|---|
| cond_c10 | SLD written expression | neps (and header comment) | "1.3 Literacy" | "1.4 Literacy" | In Reference Part D, 1.3 is Comprehension and general ability and 1.4 is Literacy (see cond_c08 and the other records) |
| cond_c10 | SLD written expression | what_it_is[1] | "DSM-5-TR does not treat poor handwriting on its own as SLD" | handwriting not listed, so alone it does not fit the specifier; "an inference … not a sentence to quote from the manual" | DSM-5-TR lists three sub-skills (spelling, grammar/punctuation, clarity/organisation). It does not say "handwriting alone is not SLD", so the claim was over-attributed |
| cond_c10 | SLD written expression | differential[0] | "DSM-5-TR does not class handwriting alone as SLD" | "handwriting is not one of the DSM-5-TR written-expression sub-skills" | Same reason |
| cond_c10 | Tic disorders | code | "ICD-11 8A05 Primary tics or tic disorders (8A05.00 Tourette syndrome)" | "8A05 Tic disorders (8A05.0 Primary tics or tic disorders: 8A05.00 Tourette · .01 chronic motor · .02 chronic phonic · .03 transient motor)" | 8A05 is "Tic disorders". "Primary tics or tic disorders" is 8A05.0 (ICD-11 MMS browser, confirmed via findacode ICD-11 listing) |
| cond_c10 | Tic disorders | explain_parent SIGNPOST | TSAI "has been the long-standing Irish charity" | "was the older Irish charity but current activity is not confirmed" | No current activity for TSAI found. Tourette's Support NI & ROI (tourettessupportni.org) is the active all-island charity. The older Tourette Support Ireland Facebook page appears inactive |
| cond_c10 | Stereotypic Movement Disorder | code | "(note: the workbook's Reference sheet currently lists 6A04 …)" | "(6A04 is DCD, not SMD)" | The note was stale: CORRECTIONS.md / fix_base.py already corrects the Reference sheet to 6A04 → 6A06. A code field someone may quote should not describe a workbook bug |
| cond_c10 | Stereotypic Movement Disorder | red_flags[3] | "…report to Tusla as soon as practicable if … reasonable grounds. Do not let…" | adds "telling the DLP does not discharge a mandated person's own duty; supervision follows action" | Brief safety standard |
| cond_c11 | OCD | neps | "3. EMOTIONAL (3.2 Anxiety) — Obsessive-compulsive and related" | "3. EMOTIONAL (3.3 Obsessive-compulsive and related) — and 3.2 Anxiety" | Part D has 3.3 Obsessive-compulsive and related (used in cond_c12 and pres_p5). The two files disagreed |
| cond_c11 | BDD | neps | "(3.2 Anxiety; 3.3 Mood)" | "(3.3 Obsessive-compulsive and related) — and 3.2 Anxiety · 3.4 Mood" | Mood is 3.4, not 3.3 (cond_c04/c05/pres_p5) |
| cond_c11 | Trich / Excoriation | neps | "(3.2 Anxiety) — Obsessive-compulsive and related" | "(3.3 Obsessive-compulsive and related) — and 3.2 Anxiety" | As OCD |
| cond_c11 | Trich / Excoriation | what_it_is[3] | "Most young people do both (Flessner et al., 2008)" | "Most people who pull do both (Flessner et al., 2008 — adult sample)" | Flessner et al. (2008) studied adults. The paediatric data are MIST-C (2007) |
| cond_c11 | Trich / Excoriation | prevalence[0] | excoriation "about 1.4% or somewhat higher lifetime … (APA, 2022)" | DSM-5 (2013) 1.4%+; Grant & Chamberlain (2020) 3.1% lifetime / 2.1% current; "check which figure DSM-5-TR uses" | 1.4% is the DSM-5 (2013) wording (OCD-UK quotes DSM-5). Secondary sources say DSM-5-TR reports 3.1% lifetime from the later US survey. I could not see the TR text, so it is hedged |
| cond_c11 | Trich / Excoriation | bands Young Adult prevalence | "excoriation about 1.4% or higher (APA, 2022)" | "1.4% or higher (DSM-5) to 3.1% (Grant & Chamberlain, 2020)" | Same |
| cond_c11 | Trich / Excoriation | citations | — | + Grant & Chamberlain (2020), J Psychiatr Res, 130, 57–60 | Verified on PMC7115927 |

cond_c12: no changes needed. Every checked claim is listed below.

## Claims checked and confirmed

**Codes.** All confirmed:
- F81.81 and ICD-11 6A03.1 (written expression)
- F95.2 / F95.1 / F95.0 and 8A05.00 (tics)
- F98.4 and 6A06 / 6A06.0 / 6A06.1 (SMD)
- F42.2 and 6B20 (OCD)
- F45.22 and 6B21 (BDD)
- F63.3 and L98.1, 6B25.0 / 6B25.1 (trich / excoriation)
- F42.3 and 6B24 (hoarding)
- F63.81 and 6C73 (IED)
- F63.1 / F63.2 and 6C70 / 6C71 (pyromania / kleptomania)

**DSM-5-TR criteria.** All confirmed:
- SLD: 6-month persistence despite intervention; 5–15% SLD prevalence; the three written-expression sub-skills.
- Tics: onset before 18, the more-than-1-year rule, and provisional under 1 year.
- SMD: severity specifiers; autism + SMD rule.
- OCD: the 1 hour/day example; insight and tic-related specifiers.
- BDD: muscle dysmorphia and insight specifiers.
- Hoarding: excessive acquisition specifier; brain injury / cerebrovascular / Prader-Willi exclusions.
- IED:
  - Criterion A frequency (twice weekly for 3 months, OR 3 damaging or injurious outbursts in 12 months)
  - age 6 or more
  - adjustment disorder exclusion for ages 6–18
  - DMDD cannot coexist with IED
  - 2.7% one-year prevalence (narrow definition)
  - onset after 40 rare
- Pyromania: criterion E exclusions including impaired judgement / ID; "very rare"; juvenile fire-setting usually with CD / ADHD / adjustment disorder.
- Kleptomania: 0.3–0.6% prevalence; about 3:1 female.

**Epidemiology citations.** All confirmed:
- Knight et al. (2012) Pediatr Neurol 47(2) 77–90: 0.77% Tourette's in children.
- Scharf et al. (2015) Mov Disord 30(2).
- Hirschtritt et al. (2015) JAMA Psychiatry 72(4) 325–333: about 86% any comorbidity; ADHD 54%, OCD 50%, so "roughly half each" is right.
- Leckman et al. (1998) Pediatrics 102(1).
- Heyman et al. (2001) BJP 179: 0.25% of 5–15s.
- Ruscio et al. (2010) Mol Psychiatry 15(1): 2.3% lifetime.
- Veale et al. (2016) Body Image 18: about 2% adolescents and adults.
- Postlethwaite et al. (2019) J Affect Disord 256: 2.5%.
- McLaughlin et al. (2012) Arch Gen Psychiatry 69(11): 7.8% lifetime, DSM-IV / broad definition.
- Grisham et al. (2006).

**Guidelines and trials.** All confirmed:
- Pringsheim et al. (2019) Neurology 92(19) 896–906 (CBIT as an initial option).
- Andrén et al. (2022) ECAP 31(3).
- Piacentini et al. (2010) JAMA 303(19).
- NICE CG31 (2005): OCD and BDD, still CG31.
- POTS (2004) JAMA 292(16).
- Mataix-Cols et al. (2015) JAACAP 54(11).
- Franklin et al. (2011) JAACAP 50(8).
- Azrin & Nunn (1973) BRT 11(4).
- Tolin et al. (2015) Depress Anxiety 32(3).
- Sukhodolsky et al. (2004).
- McCloskey et al. (2008).
- Coccaro (2012) AJP 169(6).

**Other citations.** All real, with correct pairings:
- Writing: Berninger et al. (2002); Graham et al. (2012); Santangelo & Graham (2016); Connelly et al. (2005); Dockrell et al. (2009); Berninger & Wolf (2016); DASH (2007).
- Tics and stereotypies: Heyman, Liang & Hedderly (2021); Pringsheim et al. (2021); Harris et al. (2008); Singer (2009); Oliver & Richards (2015); Hanley et al. (2003); Kapp et al. (2019).
- OCD, BDD and BFRBs: Evans et al. (1997); Lebowitz et al. (2016); Geller et al. (1998); Angelakis et al. (2016); Phillips (2007) Prim Psychiatry 14(12) 58–66; Bjornsson et al. (2013); Flessner et al. (2008).
- Hoarding: Frost & Hartl (1996); Storch et al. (2007); Tolin et al. (2008); Tolin & Villavicencio (2011).
- Behaviour, fire-setting and kleptomania: Hollo et al. (2014); Lambie & Randell (2011); Kolko (2002); Gannon & Pina (2010); Grant & Odlaug (2008).

**Irish documents.**
- NEPS (2007) Continuum of Support and NEPS (2010) BESD continuum: titles and years correct.
- DES (2017) primary guidelines: correct.
- Children First (2017): correct.
- DE Guidelines on Reduced School Days (2021), with notification to TESS: correct.

**Irish law.**
- Children Act 2001: Part 4 is the Diversion Programme. The age of criminal responsibility is 12, with exceptions from 10 for murder, manslaughter, rape and aggravated sexual assault (s.52 as substituted by Criminal Justice Act 2006, s.129). Correct.
- Criminal Damage Act 1991: damage by fire is charged as arson (s.2(4)). Correct.
- Criminal Justice (Theft and Fraud Offences) Act 2001: correct.

**Safety wording.** Present in OCD, BDD, trich, hoarding, IED and pyromania / kleptomania: report to Tusla as soon as practicable; telling the DLP does not discharge the duty; supervision follows action. It has now been added to SMD.

**Other.** Emergency numbers 999/112, Jigsaw 12–25, and Spence PAS / SCAS age ranges with OCD subscales are correct.

## Unresolved (hedged, not changed)
- DSM-5-TR excoriation prevalence wording (1.4% vs 3.1%): hedged, see above.
- Which Irish Tourette's organisation is currently active: Tourette's Support NI & ROI is confirmed active; TSAI status is unknown.
- Andrén et al. (2022) is cited for "tics worsen with stress / after school". The claim is plausible, but that guideline is Part II (interventions), so I could not confirm the exact location. Left as "e.g." with its existing hedge.
- NEPS category for tics (1.6 Co-ordination) is a questionable choice but not a factual error; left as is.
- CIT_ICD in cond_c12 uses "(2019/2022)" rather than a single APA year. This is minor and was left.
