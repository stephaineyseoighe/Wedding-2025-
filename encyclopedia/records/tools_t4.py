"""Part G tool teaching records — batch t4 (seven tools).

Written to agree with src/tool_catalogue.json and Reference Part D (rows 507-650):
WAIS-IV at 16:0+ and Young Adult; WRAT-5 adult norms and RACE literacy evidence;
MFQ and Beck Youth Inventories for low mood with 'always screen for risk';
AQ-10 / adult screening at Young Adult; RACE evidence at Adolescent;
Communication Matrix / AAC review in special settings.
No norms, cut-offs, reliability figures or eligibility thresholds are stated as fact;
where they matter the entry says 'check the manual' or 'check the current SEC Instructions'.
RACE content checked against SEC (2025) Reasonable Accommodations at the 2026
Certificate Examinations: Instructions for Schools, read 27/09/2026. The 2027
Instructions had not been located on that date — check whether they have issued.
"""

TOOLS = [
# ---------------------------------------------------------------- WAIS-IV UK
{
 "name": "WAIS-IV UK",
 "before": [
  "Know where it sits. WAIS-IV UK covers 16:0–90:11 (Wechsler, 2010, UK adaptation of the 2008 US edition); WISC-V UK runs to 16:11, so at 16:0–16:11 either is defensible (tool catalogue). As a rule of thumb, a 16-year-old still in school with a question about learning is often better served by WISC-V (child-oriented items, comparison with school-age peers); a school leaver or a question about third-level or adult services points to WAIS-IV. Whichever you choose, say why in the report.",
  "Check the edition in the cupboard. WAIS-5 was published in the US in 2024 — check whether a UK-normed edition is available to your service and which one current good practice expects you to use. Norms age, and an older standardisation can inflate scores; if you use WAIS-IV, know when its UK norms were collected (check the technical manual).",
  "Write the referral question first. In Irish EP practice the WAIS-IV usually answers questions about a young person at post-primary, in Youthreach or preparing for further/higher education (e.g. evidence for DARE or college disability supports), or about eligibility for adult disability services (Reference Part D, Adolescent and Young Adult). None of these is answered by an IQ alone — plan the attainment, adaptive and functional measures that go beside it.",
  "Rule out the confounds before the session: vision and hearing, first language and years of English-medium schooling, medication, sleep, substance use, current mental state, and whether they have had a Wechsler battery in the past year (practice effects). A young adult who is exhausted, low in mood or has been up all night gives you a result about today, not about their ability.",
  "Know the structure: four indices — Verbal Comprehension, Perceptual Reasoning, Working Memory, Processing Speed — plus FSIQ and GAI, built from ten core subtests with supplementary subtests available. Some supplementary subtests are only normed for part of the age range; check which composites need which subtests in the manual before you pack the kit.",
 ],
 "administer": [
  "Follow the script verbatim, including the adult start points, reversal and discontinue rules — they differ from WISC-V, and trainees who learned WISC-V first carry WISC habits across. Build a separate one-page crib for WAIS-IV.",
  "Talk to a young adult as an adult. Explain the purpose, who will see the results and what they can and cannot be used for, and get their own consent (at 16+ their view carries weight; at 18+ it is their consent, not their parent's). Record it.",
  "Record verbatim responses, queries (Q) and prompts (P), and the clinical half: approach to difficulty, persistence, self-talk, reaction to timed items, anxiety about 'being tested', and fatigue. Many young adults referred at this age have years of experience of failing tests — note what that looks like.",
  "Record every departure from standard procedure (split sessions, breaks, a reader for printed instructions, a motor or sensory adaptation) and interpret the affected subtests with that caution.",
 ],
 "score": [
  "Calculate age in years, months and days twice; the adult age bands are wide but a wrong band still changes scaled scores.",
  "Report each index with its 95% confidence interval and percentile rank, not only the standard score. Percentile is what a college disability officer or adult service can use.",
  "Before calling any index a strength or weakness, check the subtest splits within it and the index differences against the critical values and base rates in the manual. A statistically significant difference can still be common in the standardisation sample.",
  "Decide between FSIQ and GAI on the pattern, not on which looks better, and say in the report why you used the one you used (see WISC-V UK entry for the workbook's working rule on scatter).",
 ],
 "interpret": [
  "Normative and ipsative are different questions. A young adult's attainment and daily functioning are what matter to the course or service — the WAIS-IV tells you about reasoning, verbal knowledge, working memory and speed on the day, not about how they will manage a lecture, a placement or a job (tool catalogue: functional capacity needs functional assessment too).",
  "Verbal Comprehension depends on schooling and language exposure. For a young person with interrupted schooling, EAL or long absence (EBSA, illness), a low VCI is first a statement about opportunity.",
  "Processing Speed and Working Memory are often the lowest indices in young people referred for exam or course accommodations. Link them to specific demands — timed exams, note-taking, multi-step instructions — and to concrete supports, not to a label.",
  "An FSIQ in the range associated with intellectual disability is not a diagnosis. It needs an adaptive measure (ABAS-3 adult form or Vineland-3), developmental history and evidence of onset in the developmental period. Adult service eligibility criteria vary — check them with the service rather than implying eligibility in your report.",
  "State what the WAIS-IV cannot establish: it does not diagnose ADHD, autism, a specific learning difficulty or a mental health condition. It contributes to a formulation and to recommendations; diagnosis stays with the relevant service (PSI 2.2.2).",
 ],
 "errors": [
  "Using WAIS-IV at 16 without saying why WISC-V was not chosen.",
  "Applying WISC-V start or discontinue rules from habit.",
  "Taking consent from a parent for an 18-year-old instead of from the young adult.",
  "Implying eligibility for an adult service or college support from an IQ score alone.",
  "Interpreting a low VCI without reference to language and schooling history.",
 ],
 "read": [
  "Wechsler, D. (2010). Wechsler Adult Intelligence Scale–Fourth UK Edition (WAIS-IV UK): Administration and scoring manual; Technical and interpretive manual. Pearson. — administration chapters first.",
  "Lichtenberger, E. O., & Kaufman, A. S. (2013). Essentials of WAIS-IV assessment (2nd ed.). Wiley.",
  "Weiss, L. G., Saklofske, D. H., Coalson, D. L., & Raiford, S. E. (Eds.). (2010). WAIS-IV clinical use and interpretation: Scientist-practitioner perspectives. Academic Press.",
 ],
},

# ---------------------------------------------------------------- WRAT-5
{
 "name": "WRAT-5",
 "before": [
  "Know what it is: the Wide Range Achievement Test, fifth edition (Wilkinson & Robertson, 2017), a brief individually administered attainment test from 5 to 85+ with four subtests — Word Reading, Sentence Comprehension, Spelling and Math Computation — and a Reading Composite. It has two parallel forms (check the names in your kit), which helps with retesting.",
  "Know its place in Irish practice. The SEC's RACE Instructions list the WRAT-5 among the tests schools may use, individually administered, for a standard score in single-word reading and in spelling (SEC, 2025, section 9.1). So a post-primary pupil may already have a recent school-administered WRAT-5 — ask before you test, and do not repeat it within a short interval.",
  "Know its limits before choosing it (tool catalogue: brief means less information). It has no reading fluency, no phonological or decoding-of-nonwords measure, no oral language and no written expression. For a question about why a pupil cannot read, WIAT-III, a phonological battery (PhAB2, CTOPP-2) or a reading-comprehension test (YARC) tells you more; WRAT-5 is strongest as a quick, repeatable description of level.",
  "Check the norms. The WRAT-5 standardisation is US; check the manual for the sample and whether your service applies any UK/Irish guidance. Spelling and word lists reflect US conventions in places — note this when interpreting borderline spelling scores.",
 ],
 "administer": [
  "Administer individually, in a quiet room, with the record form and response booklet ready. Some subtests can be given to groups in other settings, but for RACE purposes only individual administration is accepted (SEC, 2025) — and individual administration is better practice for an EP anyway.",
  "Math Computation and parts of Spelling have time limits and different entry points by age; read the rules for each subtest in the manual before the session. Watch Math Computation closely — note whether errors are procedural, fact-retrieval or reading-the-sign errors.",
  "For Word Reading, record every error phonetically. The pattern (visual approximations, regularisation of irregular words, guessing from the first letter) is more useful to the teacher than the standard score.",
  "Record behaviour: self-correction, sub-vocalising, finger-pointing, avoidance, fatigue. In adolescents, note visible embarrassment — it tells you about the classroom as well as the test.",
 ],
 "score": [
  "Score as the manual directs, converting raw scores to standard scores, percentiles and confidence intervals by age (or grade, if your service uses grade norms — say which). Check each conversion twice.",
  "Grade equivalents and age equivalents are available but are easily misread; if you report them at all, explain them. Standard scores with confidence intervals and percentile ranks are what the school, the SENO and the SEC process can use.",
  "If a score is being used as RACE evidence, record the date of administration and the test form — the SEC sets a time window for acceptable attainment scores (check the current Instructions for Schools).",
 ],
 "interpret": [
  "Describe level, then pattern: Word Reading versus Sentence Comprehension (decoding versus understanding in context), Spelling versus Word Reading (a spelling score well below reading is a common profile in pupils who have compensated for decoding difficulty).",
  "Compare with instruction and history. A low Word Reading score after years of structured intervention is a different finding from one in a pupil who arrived recently or missed school. Always ask what has been taught.",
  "Do not over-read a brief test. One WRAT-5 subtest is a small sample of behaviour; before concluding a specific learning difficulty, corroborate with classwork, a fuller attainment measure and phonological evidence (Reference Part A, 'Phonological and literacy measures').",
  "For adults and older adolescents (Reference Part D, Young Adult), WRAT-5 adult norms are useful for describing functional literacy for a course or workplace; frame recommendations in terms of the demands of that setting.",
  "Write the limitations sentence: what the WRAT-5 could not tell you — fluency, comprehension of connected text, written composition, exam performance under time pressure.",
 ],
 "errors": [
  "Re-testing a pupil the school assessed on WRAT-5 a few months earlier.",
  "Reporting a grade equivalent without explanation.",
  "Concluding dyslexia from Word Reading and Spelling alone.",
  "Group-administering a subtest and then offering the score as RACE evidence.",
  "Ignoring the error pattern and reporting only the standard score.",
 ],
 "read": [
  "Wilkinson, G. S., & Robertson, G. J. (2017). Wide Range Achievement Test (5th ed.): Manual. Pearson. — administration rules for each subtest and the norms chapter.",
  "State Examinations Commission. (2025). Reasonable accommodations at the 2026 certificate examinations: Instructions for schools. SEC. — section 9.1 on attainment tests; check for the current year's edition.",
  "Snowling, M. J., & Hulme, C. (2011). Evidence-based interventions for reading and language difficulties: Creating a virtuous circle. British Journal of Educational Psychology, 81(1), 1–23.",
 ],
},

# ---------------------------------------------------------------- MFQ
{
 "name": "MFQ (Mood and Feelings Questionnaire)",
 "before": [
  "Know what it is: a questionnaire of depressive symptoms over the past two weeks, developed by Angold, Costello and colleagues (Angold et al., 1995) for children and young people roughly 8–18 (tool catalogue), with child self-report and parent versions, a long form and a 13-item short form (SMFQ). It is free to use from its developers' current source (Duke University Center for Developmental Epidemiology at the time of writing — check). Check which form your service uses; the long and short forms are scored and interpreted differently.",
  "Read every item before you use it. The long MFQ includes items on thoughts of death, on being better off dead or on killing oneself — check exactly which items are in the version you hold. You are therefore running a risk screen whether you intend to or not.",
  "Plan the risk step before the session, not after. Know your service's same-day risk procedure, who the DLP is and that they are on site, how to reach the young person's parent, the GP and out-of-hours options, and that you are a mandated person under the Children First Act 2015. Book time after the questionnaire — never give it at the end of a session with no time to follow up.",
  "Decide why you are using it. It describes severity of low mood and tracks change; it does not diagnose depression (tool catalogue). Use it inside a consultation and interview, not instead of them, and have parent and teacher accounts alongside (Reference Part D: low mood often presents as irritability or refusal rather than sadness).",
 ],
 "administer": [
  "Introduce it honestly: 'These are questions about how you have been feeling over the last two weeks. There are no right answers. I will read it with you before you go. If anything you tell me makes me worried you are not safe, I will need to talk to someone about keeping you safe — and I will tell you first.' That is informed assent, not a threat.",
  "Stay in the room. Read items aloud for younger children and weak readers and record that you did. Watch for hesitation, crossed-out answers and items skipped — a skipped item on death or self-harm is not a 'no'.",
  "Read the completed form before the young person leaves. Any endorsement of an item on death, self-harm or suicide is followed up then, in person, with direct, calm questions about thoughts, plans, means, past attempts and protective factors. Asking directly does not put the idea into their head.",
  "If there is risk: follow the same-day risk route — keep the young person safe and supervised, inform the DLP and the parent (unless doing so would increase risk), and arrange urgent assessment via GP, CAMHS or the emergency department as your procedure sets out. Where there is a child protection concern, report to Tusla as soon as practicable; telling the DLP does not discharge your own duty as a mandated person. Supervision follows the action, never replaces it.",
  "Give the parent version separately. Parent and young-person reports of low mood often disagree, in either direction; the disagreement is information (De Los Reyes & Kazdin, 2005).",
 ],
 "score": [
  "Items are rated on a three-point scale (not true / sometimes / true) and summed. Score both the total and — separately — every risk item, which you report by content, not only as part of a number.",
  "Cut-offs for the SMFQ and long MFQ are published but vary by version, informant and sample (compare Angold et al., 1995; Thabrew et al., 2018). Do not quote one from memory; check the current scoring guidance for the version you used and say which you applied.",
  "Record missing items and whether items were read aloud. A total with risk items missing cannot be interpreted as low risk.",
 ],
 "interpret": [
  "A raised score entitles you to say 'reports depressive symptoms at a level that warrants further assessment', and to recommend referral: Primary Care Psychology or a youth mental health service (e.g. Jigsaw, for 12–25, where available) for mild to moderate difficulty; via the GP to CAMHS where severity, risk or impairment is high. Check current local pathways and waiting times. The EP does not diagnose depression and does not advise on medication (PSI 2.2.2).",
  "A low score is not reassurance. Young people mask, and low mood in children often shows as irritability, withdrawal, school refusal or somatic complaints rather than sadness. Where parent, teacher or your own observation say otherwise, act on that.",
  "Formulate, do not only measure. Ask what is maintaining low mood — bullying, bereavement, family stress, exam pressure, unmet learning need, social isolation in autism — and link recommendations to it at the right Continuum level: Classroom Support (named adult, check-ins, reduced pressure), School Support (small-group wellbeing or CBT-informed programme where staff are trained), School Support Plus (EP casework, referral).",
  "Use it to track change. Re-administer after intervention or at review, with the same form, and report direction of change with caution.",
 ],
 "errors": [
  "Letting the young person leave before you have read the risk items.",
  "Treating a skipped suicide item as a 'no'.",
  "Informing the DLP and assuming your own Tusla reporting duty is discharged.",
  "Writing 'has depression' or 'meets criteria' from a questionnaire.",
  "Quoting a cut-off from memory, or from the wrong version.",
 ],
 "read": [
  "Angold, A., Costello, E. J., Messer, S. C., Pickles, A., Winder, F., & Silver, D. (1995). Development of a short questionnaire for use in epidemiological studies of depression in children and adolescents. International Journal of Methods in Psychiatric Research, 5(4), 237–249. — plus the current MFQ scoring guidance from the developers.",
  "Thabrew, H., Stasiak, K., Bavin, L. M., Frampton, C., & Merry, S. (2018). Validation of the Mood and Feelings Questionnaire (MFQ) and Short Mood and Feelings Questionnaire (SMFQ) in New Zealand help-seeking adolescents. International Journal of Methods in Psychiatric Research, 27(3), e1610.",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government of Ireland. — mandated-person sections; check for updates.",
  "National Institute for Health and Care Excellence. (2019). Depression in children and young people: Identification and management (NICE Guideline NG134). NICE. — UK guidance; check for updates and for Irish HSE equivalents.",
 ],
},

# ---------------------------------------------------------------- BYI-2
{
 "name": "Beck Youth Inventories-2",
 "before": [
  "Know what it is: the Beck Youth Inventories, second edition (Beck, Beck, Jolly & Steer, 2005), five short self-report inventories for 7–18 (tool catalogue) — Self-Concept, Anxiety, Depression, Anger and Disruptive Behaviour. Each can be used alone or together. They are US-normed; there are no Irish norms.",
  "Choose the inventories the question needs. For low mood, Depression plus Self-Concept; for EBSA and worry, Anxiety (Reference Part D, Adolescent); for behaviour referrals, Anger and Disruptive Behaviour alongside the pupil's own account. Giving all five by default adds time and dilutes the conversation.",
  "Read every item first. The Depression Inventory includes content on hopelessness and self-harm, and the Disruptive Behaviour Inventory asks about behaviours a young person may be disclosing for the first time. Check the exact items in your copy — you are running a risk screen.",
  "Plan the risk step before the session: know the same-day risk procedure, that the DLP is available, how to contact the parent and GP, and that you are a mandated person under the Children First Act 2015. Leave time after completion to read and follow up.",
 ],
 "administer": [
  "Explain purpose, confidentiality and its limits in plain words before starting: who sees the answers, and that if they tell you something that means they or someone else is not safe, you will have to act — and will tell them first.",
  "For younger children and weak readers, read items aloud and record that you did. Stay in the room; note hesitation, changed answers, skipped items and speed.",
  "Read the Depression Inventory (and any item that suggests harm to self or others, or harm by others) before the young person leaves. Any endorsement touching self-harm or suicidal thoughts is followed up then, directly and calmly: thoughts, plans, means, past attempts, protective factors.",
  "If there is risk or a disclosure of abuse or neglect: follow the same-day risk and child protection route — keep the young person safe, inform the DLP and parent (unless that would increase risk), arrange urgent assessment via GP, CAMHS or ED as your procedure requires, and report to Tusla as soon as practicable. Telling the DLP does not discharge your own duty as a mandated person. Supervision follows the action, never replaces it.",
 ],
 "score": [
  "Each item is rated on a four-point frequency scale (never / sometimes / often / always). Sum each inventory and convert to T-scores using the age and sex tables in the manual; check which tables apply and do not quote severity thresholds from memory.",
  "Report each inventory separately, and report risk items by content. A total that looks mild can contain one item that needs same-day action.",
  "Record omitted items and any read-aloud adaptation; check the manual on pro-rating before you do it.",
 ],
 "interpret": [
  "Nothing on the BYI-2 stands without corroboration (tool catalogue). Set each elevation against parent and teacher report, attendance data and your interview. The inventories have no validity scales — your observation of how they were completed is the check.",
  "Read the pattern: raised Anger and Disruptive Behaviour with low Self-Concept and raised Depression is a common picture in adolescents whose low mood shows as behaviour. The formulation should say what drives the behaviour, not only describe it.",
  "It is a description of self-reported feeling and behaviour, not a diagnosis of depression, anxiety, conduct disorder or ODD. Recommend referral where severity, risk or impairment warrants — Primary Care Psychology, a youth mental health service, or via the GP to CAMHS — and keep within PSI 2.2.2.",
  "Link recommendations to the Continuum of Support: Classroom Support (predictable routines, named adult, de-escalation plan), School Support (targeted programme), School Support Plus (EP casework, multi-agency). Re-administer the same inventories at review to track change.",
 ],
 "errors": [
  "Not reading the Depression Inventory before the young person leaves.",
  "Giving all five inventories when two answer the question.",
  "Reporting a T-score as a diagnosis.",
  "Treating the DLP conversation as the end of your own reporting duty.",
  "Interpreting self-report without parent, teacher or observational corroboration.",
 ],
 "read": [
  "Beck, J. S., Beck, A. T., Jolly, J. B., & Steer, R. A. (2005). Beck Youth Inventories–Second Edition for children and adolescents: Manual. Harcourt Assessment / PsychCorp.",
  "De Los Reyes, A., & Kazdin, A. E. (2005). Informant discrepancies in the assessment of childhood psychopathology. Psychological Bulletin, 131(4), 483–509.",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government of Ireland. — check for updates.",
 ],
},

# ---------------------------------------------------------------- AQ-10 / AQ-50
{
 "name": "AQ-10 / AQ-50",
 "before": [
  "Know what they are. The Autism-Spectrum Quotient (AQ-50; Baron-Cohen et al., 2001) is a 50-item self-report questionnaire of autistic traits for adults of average intelligence, 16+. The AQ-10 (Allison et al., 2012) is a 10-item short form intended as a quick 'red flag' screen. Separate adolescent (parent-report) and child versions exist — check which fits the young person's age and who is completing it.",
  "They are screens, not diagnostic tools (tool catalogue). A score above threshold is a reason to consider referral for comprehensive assessment; a score below it does not rule autism out. In a study of adults referred for diagnostic assessment, the AQ had limited ability to discriminate those who received a diagnosis from those who did not, with many false negatives (Ashwood et al., 2016).",
  "Know when they are appropriate. They assume the person can reflect on and report their own social experience and read the items independently; they are not suitable for someone with a moderate or severe intellectual disability, and are less reliable where insight, literacy or English is limited. NICE CG142 recommends the AQ-10 as an aid to deciding on referral in adults without moderate or severe intellectual disability (NICE, 2012, updated 2021) — check the current wording and any threshold there rather than quoting it from memory.",
  "Know the route in Ireland before you use it. For an adult, diagnostic assessment is usually accessed via the GP to adult mental health or specialist services, or privately; pathways are limited and vary by area — check what exists locally before you raise expectations. For a young person still under 18, the CDNT (if disability-related needs) or CAMHS (if a mental health presentation) route may apply.",
 ],
 "administer": [
  "Explain what it is and what it is not: 'This is a short questionnaire about how you think and what you like. It cannot tell us whether you are autistic — it helps decide whether a full assessment would be useful.' Get the young adult's own consent and agree who will see the result.",
  "Let them complete it themselves, but offer to read items aloud and record if you did. Some items are double-negatives or idiomatic; note any they queried or found ambiguous — that is information about language processing and literal interpretation.",
  "Ask afterwards about two or three items they agreed with strongly, and how much effort their social life takes. Masking or camouflaging — effortful compensation that hides difficulty — can lower self-report scores, and has been described particularly in autistic women (Hull et al., 2017).",
 ],
 "score": [
  "Score with the published key: on both forms, items are scored in the direction of autistic traits, with some items reverse-keyed. Check the key for the version you used; hand-scoring errors on reverse items are common.",
  "Report the score, the version and the referral threshold you applied with its source. Do not state a threshold from memory — thresholds differ between AQ-50 and AQ-10 and between published studies.",
 ],
 "interpret": [
  "Write it as a screening result: 'On a self-report screening questionnaire, X reported a number of experiences associated with autism. This is not a diagnosis. I recommend referral to … for comprehensive assessment.' The EP does not diagnose autism in this context (PSI 2.2.2).",
  "High scores are not specific to autism. Social anxiety, depression, ADHD and some personality presentations raise AQ scores; low scores occur in autistic people who mask or lack insight. Set the result beside developmental history (ideally from a parent), school records and observation.",
  "Whatever the score, act on the functional need you can see now (Reference Part D, Young Adult): the social demands of the course or workplace, reasonable accommodations, self-advocacy. A young person does not need a diagnosis to be supported.",
  "Be alert to co-occurring mental health risk. Autistic adolescents and adults have elevated rates of anxiety, depression and suicidality (rate not stated here — check before quoting). If distress or self-harm comes up, follow the same-day risk route; for under-18s, report to Tusla as soon as practicable where there is a child protection concern.",
 ],
 "errors": [
  "Reporting an AQ score as a diagnosis, or a low score as ruling autism out.",
  "Using it with someone who lacks the literacy, language or insight to self-report.",
  "Quoting a cut-off from memory without naming the version and source.",
  "Recommending referral without knowing whether a local adult pathway exists.",
  "Ignoring masking, especially in girls and women.",
 ],
 "read": [
  "Baron-Cohen, S., Wheelwright, S., Skinner, R., Martin, J., & Clubley, E. (2001). The Autism-Spectrum Quotient (AQ): Evidence from Asperger syndrome/high-functioning autism, males and females, scientists and mathematicians. Journal of Autism and Developmental Disorders, 31(1), 5–17.",
  "Allison, C., Auyeung, B., & Baron-Cohen, S. (2012). Toward brief 'red flags' for autism screening: The short Autism Spectrum Quotient and the short Quantitative Checklist in 1,000 cases and 3,000 controls. Journal of the American Academy of Child & Adolescent Psychiatry, 51(2), 202–212.",
  "Ashwood, K. L., Gillan, N., Horder, J., Hayward, H., Woodhouse, E., McEwen, F. S., Findon, J., Eklund, H., Spain, D., Wilson, C. E., Cadman, T., Young, S., Stoencheva, V., Murphy, C. M., Robertson, D., Charman, T., Bolton, P., Glaser, K., Asherson, P., … Murphy, D. G. (2016). Predictive validity of the Autism Spectrum Quotient (AQ) as a screening instrument for adults with ASD. Psychological Medicine, 46(12), 2595–2604. — check author list against source.",
  "National Institute for Health and Care Excellence. (2012, updated 2021). Autism spectrum disorder in adults: Diagnosis and management (Clinical Guideline CG142). NICE. — UK guidance; check for updates. Also Hull, L., Petrides, K. V., Allison, C., Smith, P., Baron-Cohen, S., Lai, M.-C., & Mandy, W. (2017). 'Putting on my best normal': Social camouflaging in adults with autism spectrum conditions. Journal of Autism and Developmental Disorders, 47(8), 2519–2534.",
 ],
},

# ---------------------------------------------------------------- Communication Matrix
{
 "name": "Communication Matrix / AAC review",
 "before": [
  "Know what the Communication Matrix is: an assessment of expressive communication for people at the earliest stages of communication, of any age, including those with severe or multiple disabilities and those using AAC (Rowland, 2011). It is free online (communicationmatrix.org — check the current site). It maps communication across seven levels, from pre-intentional behaviour to language, and four reasons to communicate: to refuse, to obtain, to engage socially and to seek or give information. It counts every mode — body movement, sounds, facial expression, gesture, objects, pictures, signs, speech, devices.",
  "Know whose tool it is. AAC assessment and system selection are SLT-led (in Ireland usually the CDNT or school-linked SLT). The EP's contribution is different: how the pupil communicates across the day, whether staff respond consistently, how communication links to behaviour and learning, and whether the system is actually available and used (tool catalogue: whether the system suits the pupil needs SLT). Contact the SLT before you start.",
  "Gather what exists: the SLT's current AAC plan and targets, the pupil's communication passport, the device or book itself, the Student Support File, and any behaviour support plan. In a special school or special class, ask who programmed the device, when it was last updated and who is responsible for it.",
  "Decide who completes the Matrix. It is completed by someone who knows the person well — parent, class teacher, SNA, SLT — ideally more than one. Differences between informants are one of the most useful things it produces.",
 ],
 "administer": [
  "Observe before you rate: at least two contrasting times of day (a structured task and an unstructured one such as break or lunch), noting each communicative act, its form, its function (refuse / obtain / social / information), and how the adult responded. Behaviour that challenges is often the most effective 'refuse' message the pupil has.",
  "Complete the Matrix with the informant rather than handing it over. Use the questions and examples on the site; ask 'show me' or 'tell me the last time' for each behaviour rated as mastered.",
  "Run the AAC review alongside: Is the system with the pupil all day, including yard, bus and home? Does it contain vocabulary for refusing, feelings, pain, toileting and body parts, not only requests? Do adults model on it (aided language modelling) or only prompt? Does every adult respond the same way?",
 ],
 "score": [
  "The Matrix is not a norm-referenced test and has no standard scores. The online version generates a profile showing which skills are emerging or mastered at each level and for each reason; print it and date it.",
  "Record informant, date and settings for each profile, and keep them. Their value is in change over time and in agreement between home and school.",
 ],
 "interpret": [
  "Read the profile for the next step, not the level: the most useful target is usually a function the pupil does not yet have a reliable way to express (often refusing or seeking attention appropriately), in a mode they can already use.",
  "Connect communication and behaviour. Where challenging behaviour serves a communicative function, the recommendation is a taught, equally effective alternative plus consistent adult response — build it into the behaviour support plan with the SLT and class team.",
  "Name the consistency finding plainly: if the SNA responds to a gesture the teacher ignores, the pupil is learning that communication works only sometimes. Recommend shared staff guidance and, where relevant, whole-school AAC training.",
  "Answer common myths with evidence: AAC does not stop speech developing — the evidence suggests it does not hinder, and may support, speech (Millar et al., 2006). Adults modelling on the device supports its use (Sennott et al., 2016).",
  "Safeguarding: pupils with limited communication are more vulnerable to abuse and less able to disclose it. Check that the system lets them say 'no', 'stop', 'hurt' and name body parts and people. Any concern goes through the child protection route: report to Tusla as soon as practicable — telling the DLP does not discharge a mandated person's own duty.",
 ],
 "errors": [
  "Recommending a change to the AAC system without the SLT.",
  "Rating from one informant only and treating it as the pupil's profile.",
  "Treating the Matrix as a standardised test with a 'level' to report as an age or score.",
  "Reviewing a device that only contains request vocabulary and not saying so.",
  "Writing a behaviour plan without identifying the communicative function of the behaviour.",
 ],
 "read": [
  "Rowland, C. (2011). Using the Communication Matrix to assess expressive skills in early communicators. Communication Disorders Quarterly, 32(3), 190–201. — plus the current Communication Matrix website and handbook.",
  "Millar, D. C., Light, J. C., & Schlosser, R. W. (2006). The impact of augmentative and alternative communication intervention on the speech production of individuals with developmental disabilities: A research review. Journal of Speech, Language, and Hearing Research, 49(2), 248–264.",
  "Sennott, S. C., Light, J. C., & McNaughton, D. (2016). AAC modeling intervention research review. Research and Practice for Persons with Severe Disabilities, 41(2), 101–115.",
  "Light, J. (1989). Toward a definition of communicative competence for individuals using augmentative and alternative communication systems. Augmentative and Alternative Communication, 5(2), 137–144.",
 ],
},

# ---------------------------------------------------------------- RACE
{
 "name": "Access arrangements evidence (RACE)",
 "before": [
  "Know what this is: not a test but the assembly of evidence for the State Examinations Commission's Reasonable Accommodations at Certificate Examinations (RACE) scheme (tool catalogue: an application, not an assessment). The SEC publishes Instructions for Schools each year; the latest verified here is for the 2026 examinations (SEC, 2025). Check whether the Instructions for the current exam year have issued (they have usually come out in the autumn) and work from those, not from this entry.",
  "Know who does what. The school authority makes the application and, for learning-difficulty grounds, carries out the required testing itself; the SEC decides. The 2026 Instructions state that a psychological report is not required for RACE, that a professional report's recommendation is treated as a recommendation to the school and does not confer eligibility, and that error-rate evidence can only come from the school's own assessment. NEPS's stated role is training, advice to schools (especially complex cases), quality assurance and complex-case referrals on learning grounds (SEC, 2025, section 4.1).",
  "Know the scheme is needs-based and being reviewed. Since the move to a needs-based model, cognitive ability scores are no longer needed and no diagnosis is required for learning-difficulty grounds (SEC, 2025, section 4.1). The SEC has a system-wide review under way and has piloted additional-time changes — check the SEC website for the current position before advising anyone on extra time.",
  "Do not state eligibility thresholds. The criteria for each accommodation (history of difficulty, school intervention, error rates, attainment scores, time windows for evidence) are set out in section 9 of the Instructions and change — read them there, in the current year's edition, every time.",
 ],
 "administer": [
  "Start with the pupil's normal way of working. The Instructions stress that accommodations should reflect how the pupil works in school and that it is rarely in a candidate's interest to be given an accommodation they are not used to (SEC, 2025). So the evidence begins with the Student Support File: history of difficulty, interventions provided and their effect, and how the pupil is accommodated in class and house exams.",
  "Know the accommodation families so you can advise the school on what to trial: reading support (reading assistance, exam reading pen, individual reader), writing support (word processor, recording device, and a scribe only in very exceptional circumstances), a spelling, grammar and punctuation waiver in language subjects, special centres, rest breaks and, on other grounds, supports for hearing, visual and physical difficulty (SEC, 2025, section 5.1). Check the current list.",
  "Your useful contribution is usually in the gaps the scheme leaves: a trial of a reading pen or word processor with a record of what happened, a formulation of why a pupil is struggling, and advice to the school on complex cases. Where you have tested (e.g. WIAT-III, WRAT-5, DASH), give dates and standard scores clearly so the school can check them against the SEC's time window and test list.",
  "Know what the scheme does not cover. The SEC states that trauma and life adversity are outside RACE's scope; arrangements then are limited to things like special centres, rest breaks and deferred examinations where eligible, and NEPS supports schools in crises during the exams (SEC, 2025, section 5.6). Mental health grounds are considered under the physical-difficulty category — check the current wording.",
 ],
 "score": [
  "There is no score. What is 'scored' is evidence against criteria, and the school must retain it for SEC and NEPS quality assurance until the candidate completes the Leaving Certificate (SEC, 2025, section 9.1).",
  "Keep your own record of what you contributed, the dates of any tests you administered, and what you told the school, pupil and family — especially if you advised that an accommodation was not appropriate.",
 ],
 "interpret": [
  "Never promise an accommodation (tool catalogue). Say: 'The school applies and the SEC decides, using criteria set out each year. What I can do is help the school understand the need and try out supports now.'",
  "Think of Leaving Certificate early. Junior Cycle accommodations are generally reactivated at Leaving Certificate on the school's confirmation of continuing need, and the SEC expects scribes at Junior Cycle to move toward word processors or recording devices through senior-cycle intervention (SEC, 2025, section 4.1). So the recommendation that matters at 13–15 is often keyboard or recording-device training.",
  "Families need the appeal route. Decisions can be appealed to an Independent Appeals Committee, and after appeal a complaint can be made to the Ombudsman (18+) or the Ombudsman for Children (under 18); closing dates are strictly applied (SEC, 2025, section 4.1). Check the current dates.",
  "Keep equity in view: a pupil whose school tested late, or who attends an Irish-medium school (alternative criteria available from the SEC on request — SEC, 2025, section 9.1.5), may need your advocacy on process rather than more testing.",
 ],
 "errors": [
  "Telling a family a pupil 'will get a reader' or 'will get extra time'.",
  "Quoting eligibility thresholds from memory or from an old year's Instructions.",
  "Implying a psychological report is required, or will secure an accommodation.",
  "Recommending an accommodation the pupil has never used in school.",
  "Missing the closing date because nobody told the school your testing was relevant.",
 ],
 "read": [
  "State Examinations Commission. (2025). Reasonable accommodations at the 2026 certificate examinations: Instructions for schools. SEC. — sections 4, 5, 6 and 9; check examinations.ie for the current year's edition and the RACE Review page.",
  "Department of Education. (2023). Circular Letter 0001/2023 — standardised tests approved for use in post-primary schools (referred to by the SEC as Circular Letter 01/2023). Check the exact title and number, and the current annual list.",
  "SEC and NEPS webinar: An overview of the RACE scheme — held each October via Education Support Centres and published on the SEC website (SEC, 2025). Check the current recording.",
 ],
},
]
