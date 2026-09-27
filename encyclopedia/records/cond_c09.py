# CONDS records: Global Developmental Delay; Borderline Intellectual Functioning;
# Specific Learning Disorder with impairment in mathematics (dyscalculia).
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c09.py

CONDS = [

# =====================================================================================
# 1. GLOBAL DEVELOPMENTAL DELAY
# =====================================================================================
{
 "name": "Global Developmental Delay (GDD)",
 "code": "DSM-5-TR Global Developmental Delay (F88 — check) · ICD-11: no identically named category; nearest is 6A00.4 Disorder of intellectual development, provisional — check before quoting",
 "neps": "1. LEARNING (1.3 Comprehension and general ability)",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Disability Act 2005 (Assessment of Need) · EPSEN Act 2004 · Children First Act 2015 · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "A DSM-5-TR neurodevelopmental diagnosis RESERVED FOR CHILDREN UNDER 5 when the clinical severity of intellectual functioning cannot be reliably assessed in early childhood. The child fails to meet expected developmental milestones in several areas of intellectual functioning, and the category includes children too young to take part in standardised testing (APA, 2022).",
  "It is PROVISIONAL BY DESIGN. DSM-5-TR states that the category requires reassessment after a period of time (APA, 2022). It is a holding label that says 'development is significantly behind in several areas and we cannot yet say what that means'.",
  "The paediatric working definition is significant delay in TWO OR MORE developmental domains — gross or fine motor, speech and language, cognition, social and personal, activities of daily living (Shevell et al., 2003). 'Significant' is defined in that practice parameter against standardised norm-referenced testing — check the exact threshold in the paper before quoting it.",
  "WHY UNDER 5: early developmental measures (Bayley-4, Griffiths III) describe the present well and predict later intellectual functioning poorly. Attention, compliance, language, motor control, familiarity with the examiner and experience all move an infant or toddler score. The Reference Part D tool notes say it plainly: a low score at 18 months is a description of now, not a forecast.",
  "OUTCOMES DIVERGE. Some children with a GDD label later meet criteria for intellectual disability; others do not, and some are later identified as autistic, or with DLD, DCD or a specific genetic syndrome, or move into the typical range. Follow-up studies differ in who they sample and how they define outcome (e.g. Riou et al., 2009) — the proportion who go on to ID is not stated here; check before quoting.",
  "CAUSE: a cause is identified in some children (for example chromosomal or single-gene conditions, prenatal exposures, perinatal events, metabolic conditions) and not in many others. Aetiological investigation, including genetic testing, is a paediatric responsibility (Moeschler, Shevell & Committee on Genetics, 2014). The EP neither orders nor advises on medical tests.",
  "IRISH CONTEXT: the label almost always arrives in a CDNT, paediatric or Assessment of Need (Disability Act 2005) report. It may underpin an AIM application in ECCE pre-school, an SNA or special-class application, or the school's first plan — which is exactly why it matters that it is read as provisional.",
 ],

 "what_it_is_not": [
  "NOT a diagnosis of intellectual disability. Do not translate GDD into 'mild GLD' or any IQ band in a school record. DSM-5-TR created GDD precisely because severity could not yet be assessed (APA, 2022).",
  "NOT permanent. A school-age child whose only label is still GDD has missed a reassessment. Flag it; do not build a school-age formulation on it.",
  "NOT delay in ONE area. A child with isolated late talking or isolated motor delay does not have GDD. Several domains must be significantly affected (Shevell et al., 2003).",
  "NOT a forecast of what the child will be able to do. 'Delay' implies catching up and 'disability' implies permanence; GDD deliberately claims neither. Parents hear one or the other — correct both.",
  "NOT caused by parenting. Deprivation and neglect CAN produce delay, which is why opportunity and care history are part of the differential — but in a family doing everything right, say clearly that nothing they did caused this.",
  "NOT something the EP diagnoses. The CDNT, paediatrician or multidisciplinary Assessment of Need team makes it. The EP describes the child's functioning in the setting, contributes to reassessment, and plans for school (PSI 2.2.2).",
  "NOT an automatic route to a special school. Placement is a question of fit between the child's current needs and what a setting can provide, reviewed as the picture clarifies — not of a label made before age 5.",
 ],

 "prevalence": [
  "OVERALL: GDD is estimated to affect about 1–3% of children under 5 (Shevell et al., 2003, American Academy of Neurology practice parameter). The figure depends on how 'significant delay' is defined — cite the source when you use it.",
  "IRELAND: no Irish population prevalence study is cited here — check before quoting. CDNT caseload and Assessment of Need figures measure demand and service capacity, not prevalence.",
  "EARLY YEARS 0–5: the only band where GDD is the correct current label. Most children are identified through Public Health Nurse developmental checks, GP or paediatric review, or pre-school concern.",
  "SCHOOL AGE 6–12 AND OLDER: should not be a current label. You will meet it in the developmental history of children now described as having ID, autism, DLD or no diagnosis at all.",
  "SEX RATIO: not stated here — check before quoting.",
  "IDENTIFIED CAUSE: the proportion of children with an identified aetiology varies with the investigations done and has risen with genetic testing; figure not stated here — check Moeschler et al. (2014).",
 ],

 "cooccurring": [
  {"name": "AUTISM",
   "rate": "elevated — rate not stated here, check",
   "presents": "reduced joint attention, limited response to name and differences in play alongside delays in several domains. Do not let GDD absorb social-communication differences, and do not let an autism diagnosis explain away global delay. The CDNT assesses both."},
  {"name": "LANGUAGE AND COMMUNICATION DELAY",
   "rate": "very common — often the most delayed domain; rate not stated here, check",
   "presents": "few words, limited understanding of routine language, frustration when not understood. Communication is usually the most useful first target and the domain that most changes how the child is read by adults."},
  {"name": "MOTOR DISORDER (including cerebral palsy)",
   "rate": "elevated — rate not stated here, check",
   "presents": "delayed sitting, walking or hand use. Motor difficulty depresses scores on any cognitive or developmental item that needs manipulation, so apparent cognitive delay may be partly motor. Ask the physiotherapist or OT what the child can do physically before reading cognitive items."},
  {"name": "HEARING OR VISION IMPAIRMENT",
   "rate": "must be excluded in every case — rate not stated here, check",
   "presents": "apparent inattention, delayed language, poor response to instruction. A sensory impairment can mimic or compound global delay. Check the dates of the last audiology and ophthalmology review before interpreting anything."},
  {"name": "EPILEPSY",
   "rate": "elevated — rate not stated here, check",
   "presents": "absences mistaken for 'switching off', fluctuating performance, fatigue after seizures, medication effects. Medical — note it, ask whether it is managed, and refer via GP or paediatrics if unrecognised episodes are described."},
  {"name": "GENETIC SYNDROME (e.g. Down syndrome, fragile X)",
   "rate": "a proportion of children — figure not stated here, check",
   "presents": "a known cause with a recognisable developmental and health profile. Read the syndrome-specific literature and family organisation materials — but describe THIS child, not the syndrome average."},
  {"name": "SLEEP, FEEDING AND BEHAVIOUR DIFFICULTIES",
   "rate": "common — rate not stated here, check",
   "presents": "night waking, restricted eating, distress at transitions or self-injury. Under-asked-about, exhausting for families, and they change what any assessment session shows. Ask directly."},
 ],

 "recommendations": [
  "DESCRIBE BY DOMAIN, NOT BY LABEL. For each area — communication, play and thinking, motor, self-care, social — write what the child does now, with an example: 'uses about ten single words; follows a one-step instruction with a gesture'. That is what a pre-school room or junior infant teacher can plan from.",
  "WRITE THE REASSESSMENT INTO THE PLAN. 'GDD is a provisional label; reassessment of intellectual and adaptive functioning is recommended at or after age 5 (APA, 2022). Named service: [CDNT / NEPS]. Target: [term].' If no one owns it, it does not happen.",
  "PRE-SCHOOL: the Access and Inclusion Model (AIM) supports children with disabilities in the ECCE programme; the pre-school applies with the family. Check current AIM levels and the Better Start process before advising.",
  "SCHOOL ENTRY: plan the transition early with parents, pre-school, CDNT and school. Priorities are functional — communication, toileting and self-care, following routines, safety, play with others. Consider a later start only as a considered team decision, not by default — check current enrolment rules and entitlements.",
  "TEACH TO THE DEVELOPMENTAL LEVEL: short, predictable routines; visual timetables and objects of reference; lots of repetition in play; adult language pitched a step above the child's own; embed CDNT therapy targets in the daily routine rather than only in sessions.",
  "SNA AND PLACEMENT: SNA support is for significant CARE needs, not teaching; placement (mainstream class, special class, special school) is decided with the SENO against the child's needs. Check current NCSE criteria and application timelines — they change.",
  "CONTINUUM LEVEL: at school entry usually School Support Plus, because the CDNT is involved. Name the level and say why.",
  "REFER: CDNT (directly or through Assessment of Need — check the local route) for multidisciplinary assessment and intervention; GP / paediatrics for aetiological work-up if not done; audiology and ophthalmology if not recent.",
  "DO NOT convert a developmental quotient or early-years score into an IQ band or a GLD category, and do not write 'GDD' as a current diagnosis for a child over 5 without also recommending reassessment.",
 ],

 "explain_parent": [
  "'Global developmental delay means she's further behind than we'd expect in more than one area — for her, talking, play and getting dressed. The word \"global\" just means \"more than one area\".'",
  "'It's a label for now, for children under five. It describes where she is; it doesn't tell us where she'll be. It's meant to be looked at again once she's older and we can assess more reliably.'",
  "'Some children with this label go on to have a longer-term learning disability, some are later diagnosed with something more specific, and some make a lot of ground. I honestly can't tell you yet which it will be — and anyone who tells you for certain at this age is guessing.'",
  "'Nothing you did caused this. The doctors may look for a reason, and in lots of children no single reason is ever found.'",
  "'What makes the difference now is the same whatever the long-term picture: practising the next small step in each area, lots of times, in everyday routines.'",
  "SIGNPOST: the CDNT key worker; the HSE Assessment of Need information; Inclusion Ireland for families; the AIM / Better Start information for pre-school; the SENO for school placement questions.",
 ],

 "explain_teacher": [
  "'This is a provisional label for under-fives. Read the report for WHAT she can do in each area, not for a level. Plan from the functional description.'",
  "'Start where she is: if she's using single words, instructions need to be one word plus a gesture or picture. If she's not yet playing alongside others, sitting in a group of six is the target, not the starting point.'",
  "'Routine and repetition do most of the teaching. Same order, same visuals, same words, every day — then vary one thing at a time.'",
  "'Keep a short record of new things she does — words, skills, independence. That record is the most useful evidence for her reassessment at or after five.'",
  "'Ask the CDNT for her therapy targets and build them into the day. Two minutes of practice in the lining-up routine beats twenty minutes once a fortnight.'",
 ],

 "explain_child": [
  "YOUNGER (the child themselves, under 5): you do not explain the label. You explain what is happening: 'I'm here to play with you and see what you like and what's tricky.' Use the child's name, a favourite toy and a short sentence.",
  "YOUNGER, WHEN THEY NOTICE DIFFERENCE: 'Everybody learns things at different times. You're learning to talk more and to do your buttons. Your teacher is going to help you practise.'",
  "OLDER (a child or adolescent reading their own file later): 'When you were small, doctors wrote that you needed extra help in lots of areas. That was a word for then. Since then we've learned much more about how you learn — let's talk about now.'",
  "ASK THROUGH PLAY, NOT QUESTIONS: offer two choices ('car or blocks?'), watch what they return to, note what makes them smile or leave. Preference is voice at this age.",
  "CHECK SIBLINGS: brothers and sisters often ask 'what's wrong with her?' Give parents a sentence they can use: 'She's learning things more slowly and needs lots of practice, and that's why she gets extra help.'",
 ],

 "analogies": [
  "THE PHOTO, NOT THE FILM: 'The assessment is a photo of where he is today. We need the film — how he changes over the next year or two — before we can say what it means.' Good with parents who want an answer now.",
  "THE PROVISIONAL LICENCE: 'GDD is like a provisional licence — it's a real label, it gets you real help, but it's meant to be replaced once things are clearer.' Good with teachers and SENOs who treat it as permanent.",
  "THE WEATHER TODAY, NOT THE FORECAST: 'We can describe today's weather very accurately. Forecasting three years ahead is a different job, and at this age nobody does it well.' Good for explaining why early scores do not predict.",
  "CAUTION: avoid 'late bloomer' or 'she'll catch up' images — they promise an outcome. Avoid 'ceiling' images too. Both claim knowledge nobody has at this age.",
 ],

 "language": [
  "'Global developmental delay' is the DSM-5-TR and paediatric term (APA, 2022; Shevell et al., 2003). Use it when quoting the report, and always pair it with 'provisional' or 'for now'.",
  "Parents hear 'delay' as 'will catch up'. Say explicitly that it does not promise that, and does not rule it out.",
  "Ask the family what words they use. Many prefer 'she needs extra help with…' to any label in front of the child.",
  "Avoid 'GDD child', 'low-functioning' or 'behind' as a description of the child. Describe skills: 'is learning to…', 'does … with support'.",
  "In school records, write the child's current functional profile first and the label second, with the date it was given.",
 ],

 "red_flags": [
  "RED FLAG — LOSS OF SKILLS (regression) in language, motor, social or self-care. Not GDD. Urgent medical referral via GP / paediatrics the same day you learn of it.",
  "RED FLAG — possible neglect or abuse. Deprivation can produce delay, and disabled children are at higher risk of abuse and less able to disclose. Follow Children First: a mandated person reports to Tusla as soon as practicable; telling the DLP does not discharge that duty. Act first, then bring it to supervision.",
  "RED FLAG — episodes of staring, jerking or unexplained collapse described by staff. Possible seizures — medical referral via GP / paediatrics.",
  "RED FLAG — no hearing or vision check on file. Audiology and ophthalmology before any cognitive conclusion.",
  "BOUNDARY — you do not diagnose GDD or order investigations. You describe functioning in the setting, contribute to reassessment and plan for school (PSI 2.2.2).",
  "WATCH — a GDD label still standing at 6, 8 or 12 with no reassessment. It is now shaping expectations and resources without evidence. Recommend reassessment in writing.",
 ],

 "child_voice": [
  "STRUCTURED PLAY OBSERVATION — good because play is where a young child shows what they can do and what they choose; you record preferences, persistence and communication, not just deficits.",
  "THE MOSAIC APPROACH (Clark & Moss, 2011) — photos, tours, maps and observation to hear very young children. Good because it does not depend on the child answering questions.",
  "OBJECTS AND PHOTO CHOICE BOARDS — offer two real objects or photos and record which is chosen. Good because choice is the most basic form of voice and is reliable at this age.",
  "TALKING MATS (for children with some symbol understanding) — good because it separates having a view from being able to say it. → https://www.talkingmats.com/",
  "PARENT AND KEY-WORKER REPORT, LABELLED AS SUCH — good because they know the child best; write 'mother reports he loves…' rather than presenting it as the child's own view.",
 ],

 "questions": [
  "Q: 'Does this mean she has an intellectual disability?' — A: 'Not necessarily. This label is used under five exactly because we can't tell yet. Some children go on to have a learning disability, some don't. The plan is to look again when she's older and the assessment is more reliable.'",
  "Q: 'Will he catch up?' — A: 'I can't promise that, and I can't rule it out. What I can tell you is what will help most now, and that we'll know a great deal more in a year or two.'",
  "Q: 'Should we hold her back a year from school?' — A: 'It's worth thinking about, but it's a team decision, not an automatic one. The question is which setting will give her the most learning next year. Let's look at that with the pre-school, the CDNT and the school, and check the enrolment rules.'",
  "Q: 'Why do the doctors want genetic tests?' — A: 'That's a question for the paediatrician — it's their area, not mine. In general, doctors look for a cause because sometimes it changes medical care or family planning. Many children never have a cause found.'",
  "Q: 'Does she need a special school?' — A: 'Not because of this label. It depends on what she needs day to day and what each setting can offer. The SENO can talk you through the options, and I can describe her needs so that decision is well informed.'",
  "Q (from school): 'The report says GDD — what level do we pitch at?' — A: 'Ignore the label for planning. Use the description of what she does in each area. If the report doesn't give you that, I'll help you build it from observation in the first few weeks.'",
  "Q: 'Did I cause this?' — A: 'No. Nothing in what you've described caused this. Children develop at different rates for reasons that are mostly outside anyone's control.'",
 ],

 "supervision": [
  "Ask how your service handles children arriving at school with GDD as their only label: who owns the reassessment, and when?",
  "Bring an early-years report and ask how your supervisor reads developmental quotients — what they would and would not repeat in a school report.",
  "Ask about the local CDNT and Assessment of Need route: how referrals are made, waiting times, and what the school can do while waiting.",
  "Discuss how to answer the 'will she catch up?' question honestly without either false hope or a forecast.",
  "Bring any case where delay may relate to care or opportunity, and confirm the Children First action taken before discussing formulation.",
 ],

 "reflection": [
  "ON THE WORD 'DELAY' — What did the parent hear when I said it: catching up, or permanence? Did I check?",
  "ON PROVISIONALITY — Did my report make clear that this is a label for now, with a reassessment named and owned? Or did I repeat it as a fixed fact?",
  "ON THE DOMAINS — Did I describe what the child does in each area, or did I summarise with a score or a label?",
  "ON MY PREDICTIONS — Did I say anything about the long term that I cannot know? Did I soften honestly or reassure beyond the evidence?",
  "ON OPPORTUNITY AND CARE — Did I ask about the child's early experience and care, and if a concern arose, did I act on it before reflecting on it?",
  "WHAT GOOD LOOKS LIKE: 'I had written \"presents with GDD\" in the summary. I rewrote it as what he does in each area now, with the date of the CDNT report and a named reassessment in second term of junior infants.'",
  "WHAT POOR LOOKS LIKE: 'Child has GDD; mild GLD likely. Recommend special class.' — a provisional label treated as a diagnosis and a placement decided by category.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Global Developmental Delay.",
  "Shevell, M., Ashwal, S., Donley, D., Flint, J., Gingold, M., Hirtz, D., Majnemer, A., Noetzel, M., & Sheth, R. D. (2003). Practice parameter: Evaluation of the child with global developmental delay. Neurology, 60(3), 367–380.",
  "Moeschler, J. B., Shevell, M., & Committee on Genetics. (2014). Comprehensive evaluation of the child with intellectual disability or global developmental delays. Pediatrics, 134(3), e903–e918.",
  "Riou, E. M., Ghosh, S., Francoeur, E., & Shevell, M. I. (2009). Global developmental delay and its relationship to cognitive skills. Developmental Medicine & Child Neurology, 51(8), 600–606. (Check details before quoting.)",
  "Clark, A., & Moss, P. (2011). Listening to young children: The Mosaic approach (2nd ed.). National Children's Bureau.",
  "World Health Organization. (2019). International classification of diseases (11th rev.) — 6A00 Disorders of intellectual development.",
  "Government of Ireland. (2005). Disability Act 2005 (Part 2 — Assessment of Need).",
 ],

 "pathway": {
  "age": "Usually identified between about 1 and 4 years, through Public Health Nurse developmental checks, GP or paediatric review, or pre-school concern — when missed milestones across several areas become clear. The label is only used under 5 (APA, 2022); reassessment is expected at or after 5, often around school entry, when more reliable cognitive and adaptive assessment is possible.",
  "who_diagnoses": "Ireland: the HSE Children's Disability Network Team (CDNT) and / or a paediatrician, often through an Assessment of Need under the Disability Act 2005 (children born on or after 01/06/2002). Private multidisciplinary assessment also occurs. NEPS does not usually see children before school entry — check local arrangements.",
  "who_wrote_report": "CDNT multidisciplinary report (psychology, SLT, OT, physiotherapy); Assessment of Need report and Service Statement; paediatric or neurology letter; older early-intervention team reports. Private reports vary in scope — check which domains were actually assessed.",
  "refer_to": "CDNT for multidisciplinary assessment, intervention and reassessment (direct referral or Assessment of Need — check the local route). GP / paediatrics for medical review and aetiology. Audiology and ophthalmology if not recent. SENO for school placement and SNA questions. Tusla for any child protection concern.",
  "sooner": "'You came when you noticed, and the Public Health Nurse and pre-school noticed with you. Early help matters, and it's still early. What we do in the next year counts far more than whether it could have started a few months before.'",
 },

 "differential": [
  "ISOLATED DOMAIN DELAY (language only, motor only) — not global; different pathway (SLT, physiotherapy / OT).",
  "AUTISM — social-communication differences and restricted or repetitive behaviour; may co-occur with global delay. CDNT assesses both.",
  "HEARING OR VISION IMPAIRMENT — audiology and ophthalmology first.",
  "DEPRIVATION, NEGLECT OR LIMITED OPPORTUNITY — delay that responds quickly to enriched care; assess care history and act on any concern.",
  "REGRESSIVE OR NEUROLOGICAL CONDITION — loss of skills; urgent medical referral.",
  "EAL / LANGUAGE DIFFERENCE — language 'delay' in English only; check home-language development.",
 ],

 "next": [
  "Read the CDNT or paediatric report for the date, the domains assessed and what the child did — not just the label.",
  "Check hearing and vision dates, and ask about seizures, sleep and feeding.",
  "Observe the child in the setting and write a domain-by-domain functional description.",
  "Name the reassessment in writing: who, when, and what it should include (cognitive AND adaptive).",
  "Plan the transition to school with parents, pre-school, CDNT, school and SENO.",
 ],

 "presentations": [
  "Delayed early milestones across several areas",
  "Understanding and responding to adult direction",
  "Curriculum access at the current level",
  "Toileting, dressing and self-care skills",
  "Transition to school and school readiness",
  "Communication without speech (gesture, signs, AAC)",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — the only band where GDD is the correct current label (under 5)",
   "prevalence": "About 1–3% of children under 5 (Shevell et al., 2003) — definition-dependent; no Irish figure, check.",
   "see": "Missed milestones in several domains: few words, limited understanding, late walking or hand use, play that is younger than expected, dependence in eating, dressing and toileting. Describe by domain and by what the child does. Check hearing, vision and care history first; profiles are unstable, so plan for reassessment rather than a conclusion.",
   "tools": ["Griffiths III", "Bayley-4", "WPPSI-IV UK", "Vineland-3", "ABAS-3", "Ages & Stages Questionnaires (ASQ-3)", "Schedule of Growing Skills II"],
  },
  "School Age": {
   "applies": "RETROSPECTIVE ONLY — appears in the history; reassessment should have replaced it",
   "prevalence": "Not applicable as a current label — rate not stated here.",
   "see": "A child who arrives with 'GDD' on file at 5 or 6. The task is reassessment of intellectual AND adaptive functioning, leading to a current description (ID, a more specific diagnosis, or no diagnosis). Until then, plan from observed functioning, not from the label.",
   "tools": ["WISC-V UK", "WPPSI-IV UK", "Vineland-3", "ABAS-3", "Leiter-3", "WNV (Wechsler Non-Verbal)"],
  },
  "Adolescent": {
   "applies": "RETROSPECTIVE ONLY — a GDD label at this age means no reassessment took place",
   "prevalence": "Not applicable as a current label.",
   "see": "Only as early history. If GDD is still the only label, recommend reassessment in writing, because curriculum route (L1LP / L2LP), RACE and transition planning all depend on a current description.",
   "tools": ["WISC-V UK", "WAIS-IV UK", "ABAS-3", "Vineland-3"],
  },
  "Young Adult": {
   "applies": "RETROSPECTIVE ONLY — relevant as developmental history for adult-service eligibility",
   "prevalence": "Not applicable as a current label.",
   "see": "Early GDD in the history can support evidence of onset in the developmental period, which adult intellectual disability services need. The current question is adaptive and cognitive functioning now; refer on to adult services.",
   "tools": ["WAIS-IV UK", "ABAS-3 adult form", "Vineland-3 adult"],
  },
  "Special Setting": {
   "applies": "YES — some children enter a special class or special school with GDD as their only label",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "A young child in an early-years or infant special class whose file says GDD. Use an adaptive measure and observation against the setting curriculum; push for the reassessment so placement and expectations rest on current evidence. Check communication access (AAC, signing) is consistent across staff.",
   "tools": ["Adaptive measure in place of IQ", "Vineland-3 / ABAS-3", "Leiter-3", "Communication Matrix / AAC review"],
  },
 },
},

# =====================================================================================
# 2. BORDERLINE INTELLECTUAL FUNCTIONING
# =====================================================================================
{
 "name": "Borderline Intellectual Functioning (BIF)",
 "code": "DSM-5-TR Borderline Intellectual Functioning (R41.83; V62.89 in DSM-5, 2013 — check) · listed under 'Other Conditions That May Be a Focus of Clinical Attention' — NOT a mental disorder · ICD-11: no equivalent category — check · Irish education (historical): 'borderline mild GLD'",
 "neps": "1. LEARNING (1.3 Comprehension and general ability)",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "EPSEN Act 2004 · Equal Status Acts 2000–2018 · Children First Act 2015 · GDPR",

 "what_it_is": [
  "NOT A DISORDER. DSM-5-TR lists Borderline Intellectual Functioning in the chapter 'Other Conditions That May Be a Focus of Clinical Attention' (a V-code / Z-code style category) — something that may affect a person's care or prognosis, not a diagnosis of mental disorder (APA, 2022). Say this explicitly in reports and meetings.",
  "DSM-5-TR notes that distinguishing BIF from mild intellectual disability requires careful assessment of BOTH intellectual and adaptive functioning (APA, 2022 — check exact wording). Intellectual disability requires adaptive deficits; BIF does not.",
  "THE NUMBERS DIFFER BY SOURCE — know which one you are using: DSM-IV-TR defined BIF as IQ 71–84 (APA, 2000); DSM-5 and DSM-5-TR removed a numeric range; Irish education practice has used approximately 70–79 for 'borderline mild general learning disability', which is the band shown in the Reference Part D (FSIQ approx. 70–79). Different reports can use different bands for the same child.",
  "IRISH EDUCATION HISTORY: 'borderline mild GLD' was used as a category in Department of Education resource allocation, grouped among 'high-incidence' needs (e.g. Circular SP ED 02/05 — check wording before quoting). The 2017 special education teaching allocation model (Circulars 0013/2017 primary and 0014/2017 post-primary — check) moved allocation away from requiring a diagnosis or category, so schools can support by need. Many parents and teachers still expect a category to unlock help.",
  "MEASUREMENT: every IQ score has a confidence interval. A score of 71 and a score of 68 are not meaningfully different, yet one sits either side of the line that separates 'ID' from 'borderline'. Report ranges and describe functioning; the line is a convention, not a boundary in the child.",
  "IMPACT IS REAL. Children and young people in this range often struggle with the pace and abstraction of the curriculum, with literacy and numeracy, and with independence, and research links BIF to poorer educational, social and mental health outcomes (Peltopuro et al., 2014; Emerson et al., 2010) — check the specific findings before quoting figures.",
  "Wieland and Zitman (2016) argue that BIF has fallen between classification systems and services — too able for intellectual disability services, not 'specific' enough for learning-difficulty provision. That gap is the practical problem you will meet.",
 ],

 "what_it_is_not": [
  "NOT a diagnosis. Never write 'diagnosed with borderline intellectual functioning'. Write 'cognitive assessment indicates general ability in the [range] range' and describe what that means for learning.",
  "NOT mild intellectual disability. ID requires deficits in adaptive functioning across conceptual, social and practical domains (APA, 2022). A young person who manages everyday life independently does not have ID, whatever the score.",
  "NOT 'slow', 'weak' or 'lazy'. These words appear in referrals and follow the young person for years. The difficulty is in the pace and abstraction of learning, not in effort.",
  "NOT a specific learning difficulty — it is a general profile. BUT an SLD can co-occur: DSM-5-TR describes SLD as occurring with intellectual functioning above about 70 (± 5 for measurement error) — check the exact wording. Reading or maths far below the child's own general level suggests something additional.",
  "NOT fixed. Scores in childhood can move with schooling, language, EAL, trauma, attendance and test conditions. Treat any score as current and conditional.",
  "NOT a reason to lower expectations or narrow the curriculum by default. It is a reason to adjust pace, explicitness and practice.",
  "NOT a reason to deny support because 'there's no category'. Since 2017, Irish SET allocation is intended to follow need, not label (check the current circular).",
 ],

 "prevalence": [
  "DEFINITION-DEPENDENT. On a scale with mean 100 and SD 15, about 13.6% of scores fall between 70 and 85 — a property of the normal curve, not an epidemiological finding. A 70–79 band holds fewer. Any quoted 'prevalence' of BIF depends on which band the author used.",
  "RESEARCH ESTIMATES: vary with definition and method — see Peltopuro et al. (2014) systematic review. Figure not stated here — check before quoting.",
  "IRELAND: no Irish prevalence figure is cited here — check before quoting.",
  "SOCIOECONOMIC GRADIENT: BIF is associated with socioeconomic disadvantage (Emerson et al., 2010 — check). Be cautious about attribution: assess opportunity, attendance, language and adversity alongside ability.",
  "AGE: often noticed from middle primary, when the curriculum becomes more abstract and pace increases, and again at post-primary transition.",
  "SEX RATIO: not stated here — check before quoting.",
 ],

 "cooccurring": [
  {"name": "ADHD",
   "rate": "elevated — rate not stated here, check",
   "presents": "off-task behaviour and incomplete work. Rule out work pitched above the young person's level before attributing it to attention; then assess attention in its own right across settings."},
  {"name": "DLD / LANGUAGE DIFFICULTY",
   "rate": "elevated — rate not stated here, check",
   "presents": "low verbal scores that pull down the overall score. Ask whether the 'borderline' profile is general or mainly verbal; if mainly verbal, a language disorder may be the better description and SLT the better referral."},
  {"name": "SPECIFIC LEARNING DIFFICULTY (dyslexia, dyscalculia)",
   "rate": "can co-occur — rate not stated here, check",
   "presents": "reading, spelling or maths well below even the young person's own general level. That gap is the signal; assess and describe it separately."},
  {"name": "ANXIETY AND LOW MOOD",
   "rate": "elevated (Emerson et al., 2010 — check) — rate not stated here",
   "presents": "withdrawal, school avoidance, low self-worth ('I'm thick'). Often secondary to years of work that was too hard. Diagnostic overshadowing applies here too — distress is not part of the cognitive profile."},
  {"name": "BEHAVIOUR DIFFICULTY AND EXCLUSION",
   "rate": "elevated — rate not stated here, check",
   "presents": "disruption or refusal in lessons pitched too high, especially at post-primary. Behaviour referrals in this range often have a learning formulation underneath."},
  {"name": "SOCIAL VULNERABILITY AND EXPLOITATION",
   "rate": "elevated risk — rate not stated here, check",
   "presents": "difficulty reading others' intentions, going along with peers, online risk, and in adolescence a risk of exploitation or involvement in offending. Build explicit teaching about safety and relationships into the plan."},
 ],

 "recommendations": [
  "SAY WHAT THE RANGE MEANS FOR LEARNING, not the number: 'She learns new concepts more slowly than most of her class and needs more examples, more practice and more concrete materials before she can use an idea independently.'",
  "PITCH AND PACE: teach at the young person's current level, with fewer new ideas per lesson, more worked examples, and more time before moving on. Check mastery before the class moves.",
  "EXPLICIT, STRUCTURED INSTRUCTION: model, guided practice, independent practice; make the steps visible; teach strategies directly rather than expecting them to be discovered.",
  "REDUCE ABSTRACTION AND LOAD: concrete materials, visual organisers, pre-taught vocabulary, instructions broken into steps and checked by demonstration.",
  "LITERACY AND NUMERACY: targeted intervention at the young person's level with progress monitoring; review after a set block and adjust. Do not wait for a category.",
  "POST-PRIMARY: consider subject levels and a manageable subject load early; for some students the L2LP route may be appropriate — check NCCA eligibility guidance for L2LP before recommending it. Check current SEC RACE criteria for any exam accommodation — BIF alone is not a RACE category.",
  "INDEPENDENCE AND SAFETY: explicit teaching of organisation, money, travel, online safety and relationships, especially from 12 onwards.",
  "CONTINUUM LEVEL: usually School Support, with School Support Plus where needs are multiple or outside services are involved. Name the level and justify it.",
  "REFER: Primary Care Psychology or CAMHS if mental health needs meet their thresholds; SLT if the profile is mainly verbal; CDNT only if intellectual disability or complex needs are genuinely in question — check local criteria.",
  "DO NOT let the band decide eligibility for support, do not write BIF as a diagnosis, and do not report a single FSIQ without its confidence interval and a description of what it means.",
 ],

 "explain_parent": [
  "'Her general learning ability is below average — in what's sometimes called the borderline or low range. That isn't a diagnosis or a disability label. It's a description of how quickly she picks up new ideas compared with others her age.'",
  "'In everyday life she manages well — getting around, looking after herself, getting on with people. That's why this isn't an intellectual disability.'",
  "'What it means in school is that she needs things explained more concretely, more practice, and a bit more time before moving on. When she gets that, she learns.'",
  "'Children in this range can fall through the gaps because there's no neat label. You don't need a label for the school to help her — support in Irish schools is meant to follow need.'",
  "'Scores can change, especially in childhood. I'd rather you remember what helps her than the number.'",
  "SIGNPOST: the school's special education teacher and Student Support File; Primary Care Psychology or CAMHS if mood or anxiety are concerns; for post-primary, the guidance counsellor on subject levels and routes.",
 ],

 "explain_teacher": [
  "'This is a general profile, not a specific one. Everything new takes longer to learn, so differentiation is about pace, examples and practice, not just extra time on a test.'",
  "'Teach it explicitly — show, do it together, then let her try. Don't assume she'll work out the method from the examples.'",
  "'Check understanding by asking her to show you, not by asking if she understands. She's learned to say yes.'",
  "'There's no category, and she still qualifies for support. The allocation model is meant to follow need — put her in the Student Support File at the level her needs call for.'",
  "'Watch the gap: if her reading or maths is well below the rest of her work, tell me — that may be something additional.'",
 ],

 "explain_child": [
  "YOUNGER: 'Everyone's brain learns in its own way. Yours learns best when things are shown step by step and you get lots of practice. When that happens, you get it.'",
  "OLDER: 'Some things in school take you longer to learn than other people — that's real, and it's not about being lazy or not trying. It means you need clearer steps and more practice, and it's fair to ask for that.'",
  "DON'T GIVE A NUMBER OR A BAND. Young people repeat 'borderline' as 'nearly stupid'. Talk about how they learn and what helps.",
  "ASK: 'Which lessons make sense to you? Which ones feel too fast? What do teachers do that helps?' — then feed the answers into the plan.",
  "LISTEN FOR SELF-TALK: 'I'm thick' or 'I'm in the dumb group'. Name it gently, and challenge it with evidence of their progress.",
 ],

 "analogies": [
  "THE SLOWER DOWNLOAD: 'The information all gets there — it just takes longer to download, and if the next file starts too soon, the first one doesn't finish.' Good with teachers for explaining pace and mastery.",
  "THE STAIRS WITH SHORTER STEPS: 'She climbs the same stairs, but her steps are shorter, so she needs more of them. Missing out steps makes her fall.' Good with parents for explaining small-step teaching.",
  "THE BORDER THAT ISN'T ON THE GROUND: 'The line between \"borderline\" and \"disability\" is drawn on a map, not on the land. Children either side of it look much the same.' Good with colleagues and SENOs when a label is being used to decide support.",
  "CAUTION: avoid any image of a limit or ceiling. The analogy should explain pace, not predict an end point.",
 ],

 "language": [
  "'Borderline' is heard as 'nearly disabled' or 'nearly normal' — both unhelpful. In reports prefer 'general ability in the low / below-average range' with a description of what that means for learning.",
  "Older Irish reports say 'borderline mild general learning disability' or 'borderline mild GLD'. When you quote them, note that this is a historical allocation category, not a diagnosis.",
  "Never 'slow learner', 'weak', 'low ability pupil' or 'bottom group' as a description of a young person.",
  "DSM-5-TR's own term is 'Borderline Intellectual Functioning' — use it only when explaining the classification, and always with 'not a disorder'.",
  "Describe strengths first: practical skills, relationships, persistence, interests.",
 ],

 "red_flags": [
  "RED FLAG — social vulnerability: an adolescent being exploited, coerced or drawn into offending, or unsafe online contact. Follow Children First: report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty.",
  "RED FLAG — self-harm, suicidal ideation or marked low mood. Same-day risk route; do not wait for supervision. Refer to CAMHS / GP as your service protocol directs.",
  "RED FLAG — a falling score or loss of skills over time. Not BIF; medical review via GP.",
  "BOUNDARY — BIF is not a diagnosis and you do not diagnose ID. If adaptive functioning is also significantly affected, describe it and refer to the CDNT (PSI 2.2.2).",
  "WATCH — the label deciding the resource. If a school or service is withholding support because a score is 'only borderline', name that in writing and point to allocation by need.",
  "WATCH — EAL, interrupted schooling and trauma depress scores. Do not report a borderline score for a child assessed in a second language without stating the caution.",
 ],

 "child_voice": [
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — Irish, familiar to schools. Good because it gives structured prompts; read it aloud and simplify wording where needed. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "SCALING AND RATING LESSONS (easy / OK / too fast) — good because it needs a choice, not an explanation, and tells you directly where pace is the problem.",
  "SOLUTION-FOCUSED QUESTIONS ('When does school go well? What's different then?') — good because it locates what already helps rather than rehearsing failure.",
  "ONE-PAGE PROFILE written with the young person — good because it transfers between teachers and puts their own words about what helps in front of staff.",
  "TALKING MATS for younger or less verbal pupils — good because it reduces the language load of giving a view. → https://www.talkingmats.com/",
 ],

 "questions": [
  "Q: 'Is it a disability?' — A: 'No. It isn't a diagnosis or a disability. It describes general learning ability in the lower range. In everyday life he's managing, which is why it isn't an intellectual disability.'",
  "Q: 'So will she get any help?' — A: 'Yes, she should. Support in Irish schools is meant to be allocated by need, not by label. I'll set out exactly what she needs and at what level, so the school can plan for it.'",
  "Q: 'Is it the same as dyslexia?' — A: 'No. Dyslexia is a specific difficulty against an otherwise typical profile. This is a general profile — learning is slower across most areas. They can happen together, and I've looked at that.'",
  "Q (from school): 'She scored 72 — isn't that mild GLD?' — A: 'No. A score on its own doesn't make an intellectual disability; that also needs significant difficulty with everyday adaptive skills, which she doesn't have. And 72 has a margin of error either side. Let's plan from what she needs.'",
  "Q: 'Should he do Foundation level?' — A: 'That's a decision for later, subject by subject, with him and his teachers. What matters now is that he's taught at a pace he can keep up with. We don't close doors early.'",
  "Q: 'Will this change?' — A: 'It can, especially in childhood. Scores move with schooling, language and how things are going in a child's life. I'd use this as a picture of now, not a verdict.'",
  "Q: 'Why didn't anyone pick this up before?' — A: 'Because young people in this range often cope well enough in the early years and only struggle when the work becomes more abstract. There's no clear label, so they can go unnoticed. What matters is what we put in place now.'",
 ],

 "supervision": [
  "Ask how your service reports scores near 70 — ranges, confidence intervals, and the wording used for 'borderline'.",
  "Discuss the Irish history of 'borderline mild GLD' and how your service handles schools that still expect a category to unlock support.",
  "Bring a case where a borderline score may reflect EAL, trauma, attendance or language disorder and ask how to write the caution.",
  "Ask what your supervisor does when a young person falls between services — too able for the CDNT, below the threshold for anything else.",
  "Bring any safeguarding concern about exploitation of a young person in this range, having already taken the Children First action.",
 ],

 "reflection": [
  "ON THE WORD 'BORDERLINE' — Did I use it? What did the parent or young person hear? Could I have said the same thing with a description?",
  "ON THE LABEL AND THE RESOURCE — Did I write recommendations that stand on need, or did I lean on a category the school expects?",
  "ON ADAPTIVE FUNCTIONING — Did I establish how the young person manages everyday life before anyone raised ID, or did I let the score frame it?",
  "ON MEASUREMENT — Did I report the confidence interval and say what it means, or a single number?",
  "ON EXPECTATIONS — Did my recommendations narrow the curriculum, or adjust pace and explicitness? Whose assumption drove that?",
  "WHAT GOOD LOOKS LIKE: 'The school asked whether 74 was \"enough\" for support. I rewrote the summary to describe how she learns and what she needs at School Support, and the SET allocation followed the need, not the number.'",
  "WHAT POOR LOOKS LIKE: 'FSIQ 74 — borderline range. Not eligible for additional resources.' — a score used as a gatekeeper, no description, no plan.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Borderline Intellectual Functioning (Other Conditions That May Be a Focus of Clinical Attention).",
  "American Psychiatric Association. (2000). Diagnostic and statistical manual of mental disorders (4th ed., text rev.).",
  "Peltopuro, M., Ahonen, T., Kaartinen, J., Seppälä, H., & Närhi, V. (2014). Borderline intellectual functioning: A systematic literature review. Intellectual and Developmental Disabilities, 52(6), 419–443.",
  "Emerson, E., Einfeld, S., & Stancliffe, R. J. (2010). The mental health of young children with intellectual disabilities or borderline intellectual functioning. Social Psychiatry and Psychiatric Epidemiology, 45(5), 579–587.",
  "Wieland, J., & Zitman, F. G. (2016). It is time to bring borderline intellectual functioning back into the main fold of classification systems. BJPsych Bulletin, 40(4), 204–206.",
  "Department of Education and Skills. (2017). Circular 0013/2017: Special education teaching allocation (primary) — and Circular 0014/2017 (post-primary). Check current versions.",
  "Department of Education and Science. (2005). Circular SP ED 02/05: Organisation of teaching resources for pupils who need additional support in mainstream primary schools. Check wording before quoting.",
 ],

 "pathway": {
  "age": "Usually noticed in middle to upper primary (around 8–11), when the curriculum becomes more abstract and faster, or at post-primary transition. Earlier, the child often copes; later, the gap with peers becomes visible in attainment, independence and sometimes behaviour or mood.",
  "who_diagnoses": "No one 'diagnoses' BIF — it is not a disorder (APA, 2022). In Ireland the finding usually comes from an EP cognitive assessment (NEPS or private), sometimes from CAMHS, Primary Care Psychology or a CDNT that concluded the young person did not meet criteria for intellectual disability.",
  "who_wrote_report": "NEPS or private EP report; older reports using 'borderline mild GLD' for allocation; CAMHS or Primary Care Psychology report; a CDNT discharge letter stating ID criteria were not met. Check the date, the test, the band used and whether adaptive functioning was assessed.",
  "refer_to": "Usually no diagnostic referral is needed — plan within the school. Primary Care Psychology or CAMHS for mental health needs meeting their thresholds; SLT if the profile is mainly verbal; CDNT only if ID or complex needs are genuinely in question; Tusla for any child protection concern.",
  "sooner": "'Children in this range often manage well enough early on, and there's no clear label, so it's commonly picked up later. That's the system's gap, not yours. What we do now is what counts.'",
 },

 "differential": [
  "MILD INTELLECTUAL DISABILITY — adaptive deficits across conceptual, social and practical domains; assess with an adaptive measure.",
  "DLD / LANGUAGE DISORDER — low verbal scores lowering the overall score; compare verbal and non-verbal indices and involve SLT.",
  "EAL, INTERRUPTED SCHOOLING OR LIMITED OPPORTUNITY — scores depressed by exposure, not ability; take a history and interpret with caution.",
  "TRAUMA, ANXIETY OR LOW MOOD — performance depressed on the day or over time; assess emotional wellbeing.",
  "UNIDENTIFIED SENSORY IMPAIRMENT — check hearing and vision.",
 ],

 "next": [
  "Check whether adaptive functioning has been assessed; if ID is in question, assess it.",
  "Report ability as a range with a confidence interval and a plain description of what it means for learning.",
  "Write recommendations that stand on need, at a named Continuum level.",
  "Screen for mood, anxiety and social vulnerability, and act on any risk the same day.",
 ],

 "presentations": [
  "Cognitive profile differences (verbal, fluid, working memory, processing speed)",
  "Underachievement not meeting SLD criteria",
  "Curriculum access at the current level",
  "Understanding and responding to adult direction",
  "Interrupted or missed schooling",
  "Working memory difficulty",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — scores under 5 are unstable; describe development rather than assign a range",
   "prevalence": "Not meaningfully estimated at this age — check before quoting any figure.",
   "see": "Usually a child who is a little behind across areas but not enough for GDD. Describe the functional profile, support language and play, and review. Avoid giving a 'borderline' band at this age — the Reference notes that index gaps are less stable here than at school age.",
   "tools": ["WPPSI-IV UK", "Vineland-3", "ABAS-3", "Ages & Stages Questionnaires (ASQ-3)"],
  },
  "School Age": {
   "applies": "YES — main identification window, usually middle to upper primary",
   "prevalence": "Definition-dependent (Peltopuro et al., 2014) — figure not stated here, check.",
   "see": "A child who coped in the infant classes and now struggles with pace and abstraction across subjects: reading comprehension, problem solving, multi-step instructions. May be quiet and compliant or increasingly frustrated. Assess cognition, attainment AND adaptive functioning, and check language and opportunity.",
   "tools": ["WISC-V UK", "WIAT-III UK", "ABAS-3", "Vineland-3", "BAS-3", "WNV (Wechsler Non-Verbal)"],
  },
  "Adolescent": {
   "applies": "YES — the gap widens with abstract subject content",
   "prevalence": "Not stated here — check.",
   "see": "Difficulty with abstract subject content, independent study and the number of teachers; risk of disengagement, behaviour difficulty or low mood. Subject levels, L2LP where eligible, RACE (only on its own criteria) and social vulnerability become the practical questions.",
   "tools": ["WISC-V UK", "WAIS-IV UK", "WIAT-III UK", "ABAS-3", "Access arrangements evidence (RACE)"],
  },
  "Young Adult": {
   "applies": "YES — relevant to further education, training, employment and justice contexts",
   "prevalence": "Not stated here — check.",
   "see": "May struggle with course demands, workplace instructions, money and independent living, yet be ineligible for intellectual disability services. Functional assessment and clear, practical recommendations matter more than the score; refer on to adult and further-education supports.",
   "tools": ["WAIS-IV UK", "WRAT-5", "ABAS-3 adult form"],
  },
  "Special Setting": {
   "applies": "RARELY — most young people in this range are in mainstream; if in a special class, check why",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "A young person in a special class or school whose profile is in this range may be there for another primary need (e.g. autism, emotional or behavioural needs). Check that the curriculum is not pitched below their level and that the placement is reviewed.",
   "tools": ["WISC-V UK", "Vineland-3 / ABAS-3"],
  },
 },
},

# =====================================================================================
# 3. SPECIFIC LEARNING DISORDER WITH IMPAIRMENT IN MATHEMATICS (DYSCALCULIA)
# =====================================================================================
{
 "name": "Specific Learning Disorder with impairment in mathematics (dyscalculia)",
 "code": "DSM-5-TR Specific Learning Disorder, with impairment in mathematics (F81.2 — check) · ICD-11 6A03.2 Developmental learning disorder with impairment in mathematics — check before quoting",
 "neps": "1. LEARNING (1.5 Maths skills — concepts and computation)",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "EPSEN Act 2004 · Equal Status Acts 2000–2018 · Children First Act 2015 · GDPR",

 "what_it_is": [
  "DSM-5-TR Specific Learning Disorder specified 'with impairment in mathematics', covering four subskills: NUMBER SENSE; MEMORISATION OF ARITHMETIC FACTS; ACCURATE OR FLUENT CALCULATION; ACCURATE MATHS REASONING (APA, 2022). DSM-5-TR notes 'dyscalculia' as an alternative term for difficulties with number sense, fact learning and calculation, and says any additional difficulty (e.g. maths reasoning) should be specified.",
  "THE CRITERIA, in outline (APA, 2022 — check the full text):\n▸ difficulties have PERSISTED FOR AT LEAST 6 MONTHS DESPITE INTERVENTION targeting them;\n▸ skills are substantially and quantifiably below age expectation, confirmed by standardised achievement measures and comprehensive clinical assessment, and interfere with school, work or daily life;\n▸ onset during the school years (may not fully show until demands exceed capacity);\n▸ not better explained by intellectual disability, uncorrected vision or hearing, other mental or neurological disorder, psychosocial adversity, lack of proficiency in the language of instruction, or inadequate instruction.",
  "RESPONSE TO INTERVENTION IS BUILT IN. The 6-month criterion means the Continuum of Support record — what was taught at Classroom Support and School Support, for how long, with what progress — is part of the evidence, not background.",
  "NUMBER SENSE IS THE CORE HYPOTHESIS. Butterworth (2005) and Butterworth, Varma and Laurillard (2011) describe a core difficulty in representing and comparing numerical quantity — seen in slow dot enumeration, poor subitising and weak magnitude comparison. Others emphasise domain-general contributors (working memory, language, processing speed, visuospatial skill) and multiple routes to the same difficulty (Kaufmann et al., 2013; Geary, 2004). Hold both.",
  "THE DEVELOPMENTAL SEQUENCE (Reference, macro skill 18 — Educational interventions in numeracy): subitising → counting with one-to-one correspondence → cardinality (the last number counted is the quantity) → comparison and the mental number line → part-whole relations → derived facts and strategies → formal procedures. A child who has not secured cardinality cannot meaningfully do addition. Locate the child in this sequence before recommending anything.",
  "Severity is specified as mild, moderate or severe (APA, 2022). DSM-5 removed the IQ–achievement discrepancy requirement; SLD is described as occurring in the context of intellectual functioning above about 70 (± 5) — check wording.",
  "IRISH CONTEXT: there is no separate Irish allocation category for dyscalculia; since 2017 SET allocation does not require a diagnosis (check current circular). The maths evidence base is weaker than the literacy one, and the Reference warns against implying otherwise.",
 ],

 "what_it_is_not": [
  "NOT maths anxiety. Maths anxiety disrupts performance, particularly under time pressure, and can exist in children with typical number sense (Ashcraft, 2002). The two often co-occur. Test untimed and ask about feelings before concluding.",
  "NOT low attainment from missed teaching, absence, frequent school moves or teaching in a second language. These are exclusion criteria in DSM-5-TR (APA, 2022). Get the educational history.",
  "NOT word-problem failure caused by reading. Read the problem aloud: if the child then solves it, the barrier was reading, not maths (Reference, macro skill 18 — numeracy).",
  "NOT 'can't learn times tables' on its own. Fact-retrieval difficulty is common in dyslexia and with working-memory difficulty too. Look for number-sense difficulty underneath.",
  "NOT identified by a screener. The Dyscalculia Screener cannot give a diagnosis and does not separate anxiety from difficulty (Reference, Part D tool notes).",
  "NOT defined by a gap between IQ and maths score. The discrepancy model is not required by DSM-5-TR.",
  "NOT a reason to stop teaching maths or to drop a level by default. It is a reason to teach differently — more concretely, more explicitly, more slowly.",
 ],

 "prevalence": [
  "ALL SPECIFIC LEARNING DISORDERS: DSM-5-TR gives 5–15% of school-age children across reading, writing and mathematics, across languages and cultures (APA, 2022).",
  "MATHS SPECIFICALLY: estimates vary widely with the cut-off and the criteria used. Devine et al. (2013) showed that prevalence — and the apparent sex ratio — changed substantially depending on the diagnostic criterion applied. Figure not stated here — check the source before quoting any rate.",
  "IRELAND: no Irish prevalence study is cited here — check before quoting.",
  "SEX RATIO: depends on criteria (Devine et al., 2013) — not stated here, check.",
  "CO-OCCURRENCE WITH READING DIFFICULTY is common; many children with maths difficulty also have literacy difficulty — rate not stated here, check.",
  "AGE: usually noticed in the early-to-middle primary years, when number facts and written calculation are expected to become fluent.",
 ],

 "cooccurring": [
  {"name": "DYSLEXIA / READING DIFFICULTY",
   "rate": "common co-occurrence — rate not stated here, check",
   "presents": "word-problem failure and weak fact recall. Separate the reading load (read the problem aloud) from the calculation load, and check phonological skills separately."},
  {"name": "MATHS ANXIETY",
   "rate": "frequently co-occurs — rate not stated here, check (Ashcraft, 2002)",
   "presents": "freezing, avoidance, tears or 'I'm rubbish at maths' — worse under time pressure. Anxiety lowers performance and avoidance reduces practice, so the two feed each other. Address both."},
  {"name": "ADHD",
   "rate": "elevated — rate not stated here, check",
   "presents": "careless errors, sign mistakes and lost place in multi-step problems. Check whether errors are conceptual (consistent) or attentional (variable) through error analysis on real work."},
  {"name": "DLD / LANGUAGE DIFFICULTY",
   "rate": "elevated — rate not stated here, check",
   "presents": "confusion over maths vocabulary ('less than', 'difference', 'altogether') and word problems. The difficulty may be the language of maths rather than number itself."},
  {"name": "WORKING MEMORY DIFFICULTY",
   "rate": "commonly associated — rate not stated here, check",
   "presents": "losing track in multi-step mental calculation and carrying or borrowing errors. Reduce load with jottings, number lines and written steps, and see whether performance changes."},
  {"name": "DCD / VISUOSPATIAL DIFFICULTY",
   "rate": "elevated — rate not stated here, check",
   "presents": "misaligned columns, poorly formed digits, difficulty with shape, space and graphs. Squared paper and layout support can change results considerably."},
 ],

 "recommendations": [
  "LOCATE THE CHILD IN THE DEVELOPMENTAL SEQUENCE: state which steps are secure and which are not ('counts accurately to 20 but does not yet use the last number as the quantity'). Generic 'maths support' is not a recommendation.",
  "SEPARATE THE SOURCES OF FAILURE in the report: number sense, fact retrieval, procedural knowledge, reading, language, working memory, anxiety. Different sources need different teaching (Reference, macro skill 18 — numeracy).",
  "CONCRETE → PICTORIAL → ABSTRACT: use manipulatives (counters, Dienes, bead strings, Cuisenaire), then drawings and number lines, then symbols, and do not rush the concrete stage.",
  "EXPLICIT, SYSTEMATIC INSTRUCTION with visual representations, worked examples, the child verbalising their thinking, and a planned sequence of examples — the features Gersten et al. (2009) found most effective for students with maths learning difficulties.",
  "NUMBER SENSE WORK: subitising, magnitude comparison, number-line estimation (Siegler & Booth, 2004), part-whole relations. Build fact knowledge through derived strategies (doubles, near doubles, bridging ten), not rote drill alone.",
  "REDUCE LOAD AND TIME PRESSURE: read problems aloud, allow jottings, number lines and multiplication squares for conceptual work, and remove timed tests while anxiety is high.",
  "TARGETED INTERVENTION with a baseline, a set block (e.g. 8–10 weeks) and a review of progress; the record forms part of the SLD evidence. The numeracy intervention evidence base is modest — state its limits (Dowker, 2004).",
  "POST-PRIMARY: agree calculator and formula access for concept work in class; consider subject level with the student; check current SEC RACE criteria for maths — do not promise an accommodation.",
  "CONTINUUM LEVEL: Classroom Support for differentiation; School Support for targeted intervention; School Support Plus where needs persist despite a documented intervention or are complex. Name it.",
  "REFER: usually none for diagnosis — this is assessed within NEPS / EP practice; Primary Care Psychology or CAMHS if maths anxiety sits within wider anxiety meeting their thresholds; audiology / ophthalmology if not recent.",
  "DO NOT identify dyscalculia from a screener, recommend times-table drill for a child without secure cardinality, or omit the Continuum level.",
 ],

 "explain_parent": [
  "'Dyscalculia means his brain finds it harder to make sense of numbers — how big they are, how they relate to each other, and remembering number facts. It isn't about how clever he is or how hard he tries.'",
  "'It's specific to maths. His reading and his reasoning in other areas are where we'd expect.'",
  "'We know it's more than a slow start because he's had focused help for months and the difficulty is still there. That's part of how it's identified.'",
  "'What helps is teaching maths differently — with real objects and pictures first, lots of practice with small steps, and less pressure on speed.'",
  "'At home: play board games with dice, count real things, talk about bigger and smaller, more and less. Please don't drill times tables under a timer — it usually makes things worse.'",
  "SIGNPOST: the school's special education teacher and Student Support Plan; the NCSE's information for parents; if anxiety is high, the GP or Primary Care Psychology.",
 ],

 "explain_teacher": [
  "'Start by finding where she is in the number sequence. If she doesn't yet know that the last number counted tells you how many, practising sums won't stick.'",
  "'Keep the concrete materials out for longer than feels necessary, and move to pictures and number lines before symbols.'",
  "'Separate reading from maths: read word problems aloud. If she can do it then, the problem was the reading.'",
  "'Take the timer off. Speed tests measure anxiety as much as maths.'",
  "'Teach fact strategies — doubles, near doubles, making ten — rather than asking her to memorise a table she can't hold.'",
  "'Keep the baseline and the review. Six months of documented intervention is part of the evidence if we need to go further.'",
 ],

 "explain_child": [
  "YOUNGER: 'Some brains find numbers tricky — like knowing how many there are, or remembering adding facts. Yours is one of them. It doesn't mean you're not smart. It means we'll use blocks and pictures to help numbers make sense.'",
  "OLDER: 'Dyscalculia means your brain processes numbers differently. Lots of people have it. It's why facts don't stick and why maths can feel scary. There are ways to work around it — tools, strategies and more time.'",
  "TEACH A SELF-ADVOCACY SENTENCE: 'Can I use the number line?' or 'Can you show me with the blocks?' Practise it so asking feels normal.",
  "ASK: 'What does your body feel like in maths?' and 'What's the hardest bit — the numbers, the words, or remembering the steps?' Use a scale or pictures for younger children.",
  "NAME STRENGTHS in other subjects and in maths itself (e.g. good at shape, good at explaining).",
 ],

 "analogies": [
  "THE MISSING RULER: 'Most people have a ruler in their head for how big numbers are. Hers is blurry — 7 and 9 feel about the same. We're helping her build a clearer one.' Good with parents and teachers for number sense.",
  "THE HOUSE WITHOUT FOUNDATIONS: 'Maths is built floor by floor. If counting and \"how many\" aren't solid, every floor above wobbles, however much we practise the top floor.' Good for explaining why you go back to basics.",
  "THE FOREIGN CURRENCY: 'Imagine paying in a currency you don't know — you can follow the steps, but you've no feel for whether the price is sensible.' Good with adolescents for why estimating is hard.",
  "CAUTION: avoid 'not a maths person'. It suggests maths ability is fixed, which is the belief that feeds avoidance.",
 ],

 "language": [
  "'Specific Learning Disorder with impairment in mathematics' is the DSM-5-TR term; 'dyscalculia' is the widely used alternative that DSM-5-TR acknowledges (APA, 2022). Use 'dyscalculia' with families and define it once.",
  "Distinguish 'dyscalculia' (a specific learning disorder, criteria met) from 'maths difficulty' (a description). Use the second when criteria are not established.",
  "Avoid 'bad at maths', 'no head for figures' or 'weak in maths' in reports.",
  "Ask the young person what they call it. Some find the word 'dyscalculia' a relief; others prefer not to be labelled.",
 ],

 "red_flags": [
  "RED FLAG — distress, school avoidance or self-harm linked to maths or exams. Same-day risk route if self-harm or suicidal thinking is disclosed; do not wait for supervision.",
  "RED FLAG — a sudden drop in maths after a period of progress. Look for a change in health, home, teaching or wellbeing before assuming a learning disorder; act on any safeguarding concern through Children First.",
  "RED FLAG — vision or hearing not checked. Refer before interpreting attainment.",
  "BOUNDARY — you identify and describe the learning difficulty within your competence; you do not diagnose co-occurring anxiety disorders or ADHD. Refer where needed (PSI 2.2.2).",
  "WATCH — a 'dyscalculia' label from a screener or an online test. Ask what evidence underpins it before repeating it in a report.",
  "WATCH — EAL and interrupted schooling. Maths vocabulary and methods differ by country; check what and how the child was taught.",
 ],

 "child_voice": [
  "MATHS FEELINGS SCALE (drawn faces or a thermometer) — good because it separates how maths feels from how maths goes, which is the anxiety question.",
  "THINK-ALOUD ON A REAL TASK ('tell me what you're doing as you go') — good because it shows the child's strategy, which is more useful than the right or wrong answer.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — Irish, already in schools. Good for placing maths among the other parts of the school day. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "SOLUTION-FOCUSED QUESTIONS ('When is maths a bit better? What's different then?') — good because it finds what already works and gives the child agency.",
  "WORK SAMPLE REVIEW WITH THE CHILD — good because it lets them explain their own errors, which often reveals a consistent misconception rather than carelessness.",
 ],

 "questions": [
  "Q: 'Isn't dyscalculia just dyslexia for numbers?' — A: 'No. Dyslexia is mainly about the sounds in words. Dyscalculia is about understanding number itself — how big numbers are and how they relate. They can happen together, and that's common, but they're different.'",
  "Q: 'The online test says he has dyscalculia — is that right?' — A: 'A screener can tell us to look more closely. It can't identify dyscalculia on its own. We need his history, the help he's had, standardised testing and a look at how he actually works.'",
  "Q: 'Should she just learn her tables?' — A: 'Not yet. If she doesn't have a solid sense of what numbers mean, memorising tables won't stick. We build the understanding first, then teach facts through strategies like doubles.'",
  "Q: 'Will he get a calculator in the exams?' — A: 'Calculators are allowed in many maths papers anyway, and the State Examinations Commission decides on any extra arrangements against its own criteria. I can't promise a specific accommodation, but I can make sure the evidence is clear.'",
  "Q: 'Why did it take so long to identify?' — A: 'Part of identifying it is showing that the difficulty lasted even with good, targeted help. That takes time by design — and the help she had counts.'",
  "Q (from school): 'Is it dyscalculia or is she just anxious?' — A: 'Often both. We test untimed and calmly, we look at the kind of errors she makes, and we ask her how maths feels. That separates them enough to plan.'",
  "Q: 'Should he drop to Foundation level?' — A: 'That's a subject-by-subject decision for later, with him and his teachers. First let's get the teaching right and see how he responds.'",
 ],

 "supervision": [
  "Ask what maths measures your service holds and how it evidences the 6-month intervention criterion.",
  "Bring a work sample and do an error analysis together — what does the pattern of errors say about the child's position in the number sequence?",
  "Discuss how your supervisor separates maths anxiety from dyscalculia in practice, and how they write it.",
  "Ask how the service uses the word 'dyscalculia' in reports — when it is used, and when 'maths difficulty' is preferred.",
  "Bring a numeracy recommendation you wrote and ask whether a teacher could act on it tomorrow.",
 ],

 "reflection": [
  "ON LOCATION — Did I say where the child is in the number sequence, or only that they are behind?",
  "ON SOURCES — Did I separate reading, language, working memory, anxiety and number sense, or did I report one maths score?",
  "ON THE EVIDENCE BASE — Did I present the numeracy evidence as stronger than it is?",
  "ON THE INTERVENTION RECORD — Did I check what was taught, for how long, and with what response before concluding?",
  "ON ANXIETY — Did I ask the child how maths feels? Did my assessment conditions add pressure?",
  "WHAT GOOD LOOKS LIKE: 'I rewrote \"requires support in numeracy\" as: secure counting to 20, not yet cardinal beyond 5; recommend 10 weeks of concrete part-whole work at School Support, reviewed with a dot-enumeration and comparison check.'",
  "WHAT POOR LOOKS LIKE: 'Maths is below average. Recommend extra maths support and practice of tables at home.' — no location, no source, no Continuum level, and a recommendation likely to raise anxiety.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Specific Learning Disorder.",
  "Butterworth, B. (2005). The development of arithmetical abilities. Journal of Child Psychology and Psychiatry, 46(1), 3–18.",
  "Butterworth, B., Varma, S., & Laurillard, D. (2011). Dyscalculia: From brain to education. Science, 332(6033), 1049–1053.",
  "Gersten, R., Chard, D. J., Jayanthi, M., Baker, S. K., Morphy, P., & Flojo, J. (2009). Mathematics instruction for students with learning disabilities: A meta-analysis of instructional components. Review of Educational Research, 79(3), 1202–1242.",
  "Dowker, A. (2004). What works for children with mathematical difficulties? (Research Report RR554). Department for Education and Skills.",
  "Devine, A., Soltész, F., Nobes, A., Goswami, U., & Szűcs, D. (2013). Gender differences in developmental dyscalculia depend on diagnostic criteria. Learning and Instruction, 27, 31–39.",
  "Ashcraft, M. H. (2002). Math anxiety: Personal, educational, and cognitive consequences. Current Directions in Psychological Science, 11(5), 181–185.",
  "Geary, D. C. (2004). Mathematics and learning disabilities. Journal of Learning Disabilities, 37(1), 4–15.",
  "Kaufmann, L., Mazzocco, M. M., Dowker, A., von Aster, M., Göbel, S. M., Grabner, R. H., et al. (2013). Dyscalculia from a developmental and differential perspective. Frontiers in Psychology, 4, 516.",
  "Siegler, R. S., & Booth, J. L. (2004). Development of numerical estimation in young children. Child Development, 75(2), 428–444.",
 ],

 "pathway": {
  "age": "Usually noticed from about 7–9, when number facts and written calculation are expected to become fluent; sometimes later, at post-primary, when algebra and multi-step problems expose weak foundations. DSM-5-TR requires at least 6 months of difficulty despite targeted intervention (APA, 2022), so firm identification typically follows a documented period at School Support.",
  "who_diagnoses": "Ireland: an educational psychologist — NEPS or private — with standardised attainment testing, cognitive assessment where indicated, the intervention record and a developmental and educational history. There is no HSE diagnostic pathway for dyscalculia alone.",
  "who_wrote_report": "NEPS or private EP report; sometimes a special education teacher's screening (which is not a diagnosis); occasionally a psychologist's report written for RACE or further-education access. Check the tests used, the date, and whether an intervention record was considered.",
  "refer_to": "Usually no external referral — plan within the school. Audiology / ophthalmology if not recent; Primary Care Psychology or CAMHS where anxiety or low mood meet their thresholds; SLT if maths language difficulty sits within a wider language difficulty.",
  "sooner": "'Maths difficulties are often put down to anxiety or \"not being a maths person\", so they're commonly picked up later than reading difficulties. Part of identifying it is showing that good help wasn't enough — so the time you've spent counts.'",
 },

 "differential": [
  "MATHS ANXIETY WITHOUT NUMBER-SENSE DIFFICULTY — performance improves untimed and calm; foundational skills secure.",
  "INADEQUATE OR INTERRUPTED INSTRUCTION — gaps match missed teaching; responds quickly to teaching.",
  "GENERAL LEARNING DIFFICULTY / BIF / ID — difficulty across areas, not specific to maths.",
  "READING OR LANGUAGE DIFFICULTY — failure mainly on word problems or maths vocabulary.",
  "ATTENTION OR WORKING MEMORY DIFFICULTY — variable, careless errors; improves with reduced load.",
 ],

 "next": [
  "Gather the intervention record: what was taught, for how long, with what progress.",
  "Do an error analysis on the child's real work and locate them in the number sequence.",
  "Assess untimed maths, number sense and maths anxiety, and separate the reading load.",
  "Write a specific, level-located recommendation with a review date and Continuum level.",
 ],

 "presentations": [
  "Numeracy difficulty not meeting SLD criteria",
  "Maths anxiety",
  "Number sense and estimation",
  "Recall of number facts vs procedural method",
  "Word problems — reading as the barrier, not the maths",
  "Working memory load in multi-step calculation",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — too early to identify; describe early number development instead",
   "prevalence": "Not identified at this age — rate not stated here.",
   "see": "Difficulty with counting, one-to-one correspondence, subitising small groups or comparing quantities. Observe in play and describe; the Reference Part D notes there is no standardised maths measure to use here. Support with number games, rhymes and counting real objects.",
   "tools": [],
  },
  "School Age": {
   "applies": "YES — main identification window",
   "prevalence": "Maths-specific rate depends on criteria (Devine et al., 2013) — not stated here, check.",
   "see": "Counting on fingers long after peers, weak sense of number size, facts that do not stick, confusion with place value, errors in carrying and borrowing, avoidance or distress in maths. Separate reading from calculation, test untimed, and use error analysis on real work alongside standardised measures.",
   "tools": ["WIAT-III UK maths subtests", "Sandwell Early Numeracy Test", "Dyscalculia Screener / DysCalculiUM", "WISC-V UK", "Sigma-T (Irish standardised school maths test) — AGE: primary classes, check edition · MEASURES: group maths attainment against Irish norms · CANNOT TELL YOU: why the child is struggling or where in the number sequence they are · TIME: check the manual"],
  },
  "Adolescent": {
   "applies": "YES — sometimes first identified at post-primary",
   "prevalence": "Not stated here — check.",
   "see": "Difficulty with algebra, fractions, multi-step problems and applying maths in other subjects; reliance on calculators for basic facts; anxiety and avoidance. Subject level, calculator and formula access, and RACE (only on SEC criteria) become the practical questions.",
   "tools": ["WIAT-III UK maths subtests", "Dyscalculia Screener / DysCalculiUM", "WISC-V UK", "Access arrangements evidence (RACE)"],
  },
  "Young Adult": {
   "applies": "YES — relevant to further education, disability supports and work",
   "prevalence": "Not stated here — check.",
   "see": "Difficulty with budgeting, time, measurement, timetables and course-specific maths; anxiety about maths demands in training or work. Functional numeracy and reasonable adjustments are the focus; the EP role is usually time-limited here.",
   "tools": ["WRAT-5", "WIAT-III UK maths subtests", "WAIS-IV UK", "Dyscalculia Screener / DysCalculiUM"],
  },
  "Special Setting": {
   "applies": "RARELY — maths difficulty in special settings is usually part of a general learning profile",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Assess functional numeracy against the setting curriculum — money, time, measuring, counting in everyday tasks — rather than standardised maths scores. Practical application matters more than a label.",
   "tools": ["Adaptive measure in place of IQ", "Vineland-3 / ABAS-3"],
  },
 },
},

]
