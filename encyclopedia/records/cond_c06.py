# CONDS records: Selective Mutism, Specific Phobia, Panic Disorder and Agoraphobia.
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c06.py

CONDS = [

# =====================================================================================
# 1. SELECTIVE MUTISM
# =====================================================================================
{
 "name": "Selective Mutism",
 "code": "DSM-5-TR Selective Mutism (anxiety disorders chapter; ICD-10-CM F94.0) · ICD-11 6B06 Selective mutism — verify in the ICD-11 browser before quoting",
 "neps": "3. EMOTIONAL (3.2 Anxiety) — and 1. LEARNING (1.2 Language skills)",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.2.4 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "An ANXIETY disorder: consistent failure to speak in specific social situations where speaking is expected (usually school), despite speaking in other situations (usually home) (APA, 2022, DSM-5-TR). DSM-5 (2013) moved it into the anxiety disorders chapter; ICD-11 also places it among anxiety and fear-related disorders.",
  "Criteria in outline: lasts at least ONE MONTH and is not limited to the first month of school; interferes with educational achievement or social communication; is NOT attributable to lack of knowledge of, or comfort with, the spoken language required; is not better explained by a communication disorder and does not occur exclusively during autism or a psychotic disorder (APA, 2022). Read the full criteria before quoting.",
  "The child CAN speak. Speech is blocked by anxiety at the EXPECTATION of speaking — often strongest with particular people, in particular places, or when others can hear. Johnson & Wintgens (2016) describe it as a fear of speaking to certain people, maintained like any phobia.",
  "MAINTAINING CYCLE: expectation to speak → anxiety rises → silence (or an adult answering for the child) → relief. The relief reinforces the silence (negative reinforcement). Well-meaning adults maintain it from both directions — by pressing for speech and by rescuing.",
  "Onset is usually BEFORE AGE 5, but it is often first noticed at school entry, because that is where sustained speaking to non-family adults is first expected (APA, 2022).",
  "Wide range of severity: some children whisper to one friend, nod, point or write; others freeze, avoid eye contact, and cannot eat, laugh, cough or use the toilet in school. Muris & Ollendick (2015) review the strong link with behavioural inhibition and social anxiety.",
  "The evidence-based approaches are BEHAVIOURAL and graded: stimulus fading ('sliding-in'), shaping and graded exposure, delivered in the real setting, with the pressure to speak removed (Cohan et al., 2006; Johnson & Wintgens, 2016). SLT involvement is standard practice in Ireland and the UK.",
 ],

 "what_it_is_not": [
  "NOT defiance or control. The older term 'elective mutism' implied a choice; DSM-IV (1994) renamed it 'selective' to remove that implication. Treating the silence as oppositional raises anxiety and entrenches it.",
  "NOT shyness that will pass by itself. Shy children warm up and speak when they need to; in SM the pattern persists and becomes more habitual the longer it continues (Johnson & Wintgens, 2016). 'Wait and see' is not a plan.",
  "NOT the EAL silent period. Children new to a language commonly go through a non-verbal period in that language while receptive understanding builds (Tabors, 2008). DSM-5-TR excludes mutism explained by lack of knowledge of or comfort with the language. SM is more likely where the child is ALSO silent in the home language in school (e.g., with a same-language peer or adult), or silence persists well after receptive English is established (Toppelberg et al., 2005) — check the paper for their duration guidance before quoting.",
  "NOT a language disorder — but speech and language difficulties co-occur in a substantial proportion (Kristensen, 2000), and embarrassment about speech can feed the mutism. SLT assessment still matters, often using home recordings.",
  "NOT usually caused by trauma or abuse. Reviews do not support assuming a traumatic cause (Viana et al., 2009). Do not create suspicion without basis — and do not ignore indicators either. Sudden-onset mutism is a different picture (see red flags).",
  "NOT fixed by pressure, bribes, tricks or 'I'll wait until you say it'. Pressure raises anxiety; the evidence-based approaches reduce pressure while graduating exposure (Cohan et al., 2006).",
  "NOT autism — though the two can co-occur. The question is whether silence is context-specific and fear-linked (SM) or part of a social communication difference present across settings, including home.",
 ],

 "prevalence": [
  "OVERALL: DSM-5-TR reports point prevalence from clinic and school samples of roughly 0.03%–1% (APA, 2022). Bergman, Piacentini & McCracken (2002) found about 0.7% in a US early-primary school sample. Check the current DSM-5-TR text before quoting.",
  "IRELAND: no Irish prevalence figure stated here — check before quoting. Expect most schools to meet a child with SM only occasionally, so staff experience will usually be low.",
  "EARLY YEARS 0–5: onset usually here; identification most often in preschool or junior/senior infants (APA, 2022).",
  "SCHOOL AGE 6–12: main window for referral and intervention.",
  "ADOLESCENT 13–16: new onset is uncommon; long-standing SM is harder to shift, and residual social anxiety is common (Muris & Ollendick, 2015) — rate not stated here, check.",
  "SEX RATIO: more common in girls in most studies (Viana et al., 2009) — ratio varies; check before quoting.",
  "BILINGUAL / MIGRANT CHILDREN: higher rates are reported (reviewed by Toppelberg et al., 2005) — and this is exactly where over-identification from the silent period is most likely. Hold both.",
 ],

 "cooccurring": [
  {"name": "SOCIAL ANXIETY DISORDER",
   "rate": "very high overlap — most clinical samples show it (Muris & Ollendick, 2015); rate not stated here, check",
   "presents": "fear of being watched, heard or evaluated. Often persists after speech returns — the child speaks but still avoids oral presentations and new groups. Plan for it."},
  {"name": "SPEECH, LANGUAGE AND COMMUNICATION DIFFICULTY",
   "rate": "elevated (Kristensen, 2000) — rate not stated here, check",
   "presents": "a home recording shows articulation, grammar or vocabulary difficulty. Awareness of sounding different can drive the silence. SLT assessment, using home recordings with consent."},
  {"name": "SEPARATION ANXIETY / OTHER ANXIETY",
   "rate": "elevated — rate not stated here, check",
   "presents": "distress at drop-off, clinging to a parent, somatic complaints on school mornings. Formulate the anxiety as a whole, not just the silence."},
  {"name": "AUTISM",
   "rate": "reported co-occurrence — rate not stated here, check",
   "presents": "social communication differences that are present at home as well as school. Assess both separately; do not let 'it's just SM' or 'it's just autism' close the question. Refer to CDNT for autism assessment where indicated."},
  {"name": "ELIMINATION DIFFICULTIES",
   "rate": "reported in clinical samples (Kristensen, 2000) — rate not stated here, check",
   "presents": "the child cannot ask to use the toilet, so withholds or has accidents at school. Needs a practical, non-verbal toilet plan on day one."},
  {"name": "EMOTIONALLY BASED SCHOOL AVOIDANCE (EBSA)",
   "rate": "not stated — check",
   "presents": "reluctance to attend building around days with oral demands — reading aloud, assemblies, sacramental preparation, Irish oral work, performances. Track attendance against the timetable."},
 ],

 "recommendations": [
  "REMOVE THE PRESSURE TO SPEAK. No direct questions that require a spoken reply in front of others; no 'say please'; no rewards withheld until the child asks; no 'I'll wait'. Accept nods, pointing, cards, writing and gesture as full participation (Johnson & Wintgens, 2016).",
  "TELL THE CHILD THE PRESSURE IS OFF. An agreed message from teacher and parent: 'You don't have to talk until you're ready. You can nod, point or show me.' This lowers anticipatory anxiety immediately.",
  "COMMENT, DON'T QUESTION. Use a running commentary style; ask questions the child can answer non-verbally; later, once some speech is emerging, forced-alternative questions ('red or blue?') are easier than open ones (Johnson & Wintgens, 2016).",
  "BUILD A COMMUNICATION MAP with parent and school: who the child speaks to, where, and how (speaks / whispers / gestures / nothing). It is the baseline, the plan and the outcome measure.",
  "KEYWORKER AND SMALL-STEPS PROGRAMME: one named adult, short frequent sessions, a graded hierarchy of talking targets agreed with the child. Check Johnson & Wintgens (2016) for their recommended session frequency before writing it in.",
  "SLIDING-IN (stimulus fading): the child talks to a parent in a quiet school room; the keyworker enters in stages — outside the door, in the room at a distance, closer, joining the game — while the child keeps talking; then the parent fades out. Repeat with each new person and place (Johnson & Wintgens, 2016).",
  "REACT NEUTRALLY WHEN THE CHILD SPEAKS. Respond to what was said, not to the fact of speaking. No public praise, no announcements to the class or staffroom.",
  "PRACTICAL PLAN from day one: a non-verbal toilet signal; how to show hurt, sick or needing help; answering the roll (hand up, card); alternatives for oral reading and oral assessment (e.g., a recording made at home, with consent).",
  "BRIEF EVERY ADULT: secretary, SNA, substitute teachers, coaches, bus escort. One adult who pressures can undo weeks of progress.",
  "CONTINUUM LEVEL: School Support; School Support Plus where SLT, Primary Care Psychology or CAMHS are involved, or where a reviewed plan has not shifted the communication map.",
  "REFER: SLT via GP / Primary Care (or CDNT where there are wider developmental needs) — check local SLT experience with SM. Primary Care Psychology or CAMHS where anxiety is severe, has generalised to home, or is not responding. Audiology if hearing has not been checked.",
  "DO NOT try to 'get the child talking' in your own assessment session, trick the child into speaking, or record the child without consent. Medication questions go to the doctor (PSI 2.2.2).",
 ],

 "explain_parent": [
  "'Selective mutism is an anxiety difficulty. She can talk — you hear her at home — but in school the expectation to speak sets off a freeze. It's not stubbornness and it's not something she's choosing.'",
  "'The silence works in the short term: it brings relief when she feels under pressure, so it gets stronger each time. Our job is to take the pressure away, then build confidence in very small steps.'",
  "'The approach with the best evidence starts where she's already comfortable — usually with you — and slowly brings one new person or one new place in at a time. You may be asked to come into school for short sessions at first, because you're the person she already talks to.'",
  "'Please don't promise rewards for talking or tell her she has to talk to teacher. It raises the stakes. Praise her for joining in and for the brave steps she agrees to.'",
  "'If English isn't the language at home, I'll want to know how and with whom she talks in your language. That helps us tell selective mutism apart from the normal quiet period of learning a new language.'",
  "SIGNPOST: SMIRA (Selective Mutism Information & Research Association, UK) parent materials; Johnson & Wintgens (2012) 'Can I tell you about Selective Mutism?'; the GP and Primary Care SLT route. Irish parent support groups — check what is currently active before naming one.",
 ],

 "explain_teacher": [
  "'She isn't refusing. Think of it as a phobia of being expected to talk. The more we expect it, the tighter the freeze.'",
  "'Take the pressure away: no questions that need a spoken answer in front of the class, no waiting her out. Give her ways to take part — nodding, pointing, cards, a mini-whiteboard.'",
  "'If she does speak, treat it as ordinary. Answer what she said, not the fact that she said it. A big reaction makes the next time harder.'",
  "'Consistency across adults matters most. Every adult who meets her — secretary, SNA, sub, coach — needs the same brief.'",
  "'Progress comes in small, planned steps with a keyworker. It's normal for talking to start with one person in one place and spread slowly — that's the programme working, not failing.'",
  "'Sort the practical things now: how she'll ask for the toilet, show she's hurt or unwell, and answer the roll.'",
 ],

 "explain_child": [
  "YOUNGER: 'Some children find their words get stuck at school, even though they talk lots at home. That's a worry about talking. It's not your fault, and nobody is going to make you talk. You can nod, point or show me.'",
  "OLDER: 'Selective mutism is when anxiety makes it really hard to talk in some places or to some people. Your voice works fine — it's the worry that blocks it. We'll go in tiny steps, and you get a say in every one.'",
  "DO NOT ASK WHY. Children usually cannot explain it, and the question itself is pressure. Use pointing, rating, sorting and drawing instead.",
  "ASK (answerable without speech): 'Show me on the thermometer how worried you feel at small-group time.' 'Point to who you'd most like to be able to talk to first.'",
  "OFFER CONTROL: let the child choose the first target and the pace. Control reduces fear, and a child-chosen step is far more likely to happen.",
 ],

 "analogies": [
  "THE STUCK LIFT DOORS: 'The words are there and ready to go, but the doors won't open on this floor. On the home floor they open every time. We're going to get them working on one more floor at a time.' Works with parents and children.",
  "THE SPIDER PHOBIA: 'If someone was terrified of spiders, you wouldn't hand them one and say “just hold it”. You'd start with a picture, then a spider across the room.' Works with teachers — explains graded exposure and why pressure fails, following Johnson & Wintgens' (2016) framing of SM as a fear.",
  "THE SPOTLIGHT: 'Every time someone waits for her to answer, a spotlight comes on. Our job is to switch it off so she can find her voice first where nobody's watching.' Works with teachers — explains commentary style and neutral reactions.",
  "STEPPING STONES: 'We cross the river one stone at a time, and you pick the next stone.' Works with children — explains the small-steps programme and who is in charge of the pace.",
 ],

 "language": [
  "'Selective mutism' is the current term (DSM-5-TR, ICD-11). Avoid 'elective mutism' — it implies choice and is outdated.",
  "In reports avoid 'refuses to speak', 'won't talk', 'chooses not to'. Write 'does not currently speak in…' or 'is not yet able to speak to…'. PSI 1.2.8 — interpretation must be labelled as opinion.",
  "Avoid 'shy' as the explanation, and avoid classroom labels such as 'our quiet one'.",
  "Older children and adolescents often describe it as 'freezing' or 'my words getting stuck'. Use their words back to them.",
 ],

 "red_flags": [
  "RED FLAG — SUDDEN-ONSET mutism in a child who previously spoke in school, particularly after an event or alongside other behavioural change. This is not the typical course. Consider trauma, a safeguarding concern or a medical cause. Tell your supervisor the same day; if there are indicators of abuse or neglect, follow Children First — report to Tusla as soon as practicable (telling the DLP does not discharge a mandated person's duty).",
  "RED FLAG — loss of speech across ALL settings including home, or loss of previously acquired language or skills. That is not SM. GP / paediatrics promptly.",
  "RED FLAG — an older child or adolescent with long-standing SM who is withdrawing, low in mood or self-harming. The communication barrier makes risk harder to ask about — use written or scaled methods, ask directly, and follow the risk protocol the same day.",
  "BOUNDARY — you do not diagnose SM. You describe context-specific speech, formulate, recommend and refer. Medication questions go to the doctor. PSI 2.2.2.",
  "WATCH — the EAL silent period, hearing loss, language disorder and autism. Rule each in or out before formulating.",
  "WATCH — siblings, friends or adults answering for the child. Kind, and it maintains the avoidance. Plan to fade it gently rather than stopping it abruptly.",
 ],

 "child_voice": [
  "COMMUNICATION MAP / TALKING MAP (Johnson & Wintgens, 2016) — child and parent mark who and where the child talks, whispers, gestures. Good because it is visual, needs no speech, and becomes the baseline and outcome measure.",
  "PICTURE-CARD SORTING of situations into 'easy / a bit hard / very hard' (Talking Mats-style). Good because it gathers detailed preference data with zero speech demand.",
  "WORRY THERMOMETER or SCALING by pointing. Good because it gives a repeatable, non-verbal measure across situations and shows change over time.",
  "WRITTEN OR TYPED responses, or a recording made at home with consent. Good because many older children write freely, and a home recording lets you and the SLT hear the child's actual voice and language. Agree consent, storage and deletion first (GDPR).",
  "DRAWING 'MY SCHOOL DAY' and colouring easy and hard moments. Good because it locates the difficulty in contexts rather than in the child, and gives the hierarchy its first steps.",
 ],

 "questions": [
  "Q: 'She talks non-stop at home — are you sure there's a problem?' — A: 'That's exactly the pattern. Speaking freely at home and not at school is what selective mutism looks like. It's anxiety tied to certain places and people, not an inability to talk.'",
  "Q: 'Is she doing it for attention, or to be in control?' — A: 'No. The old name, elective mutism, suggested that, and it was changed because it isn't a choice. Most children with SM would love to be able to talk at school — the worry gets there first.'",
  "Q: 'Should we just wait? She'll grow out of it.' — A: 'Some children improve, but the longer the pattern goes on, the more habitual it becomes. A gentle plan now is better than waiting and hoping.'",
  "Q: 'Can't we just reward her when she talks?' — A: 'General rewards for talking tend to raise the pressure. Rewarding small, agreed steps in a planned programme is different. And we never hold back something she needs until she asks for it.'",
  "Q: 'She's only arrived from abroad this year — is this selective mutism?' — A: 'Possibly not. Many children go through a quiet period in a new language. I'll want to know about her home language, whether she speaks it to anyone in school, and how much English she understands before drawing any conclusion.'",
  "Q: 'How will she do oral Irish or reading assessments?' — A: 'We'll plan alternatives — for example a recording made at home, or responding in writing — and make sure the arrangement is agreed and recorded, not improvised on the day.'",
  "Q: 'Did something happen to her to cause this?' — A: 'In most children, no — it's linked to an anxious, cautious temperament. If there are other worries, I'll take them seriously and we'd follow Children First, as we would for any child.'",
  "Q: 'Will she need medication?' — A: 'That's a question for her doctor, not me. The main approach is behavioural — small, planned steps with the pressure taken off.'",
 ],

 "supervision": [
  "Bring the communication map and your draft hierarchy, and ask whether the steps are small enough.",
  "For any bilingual child, discuss how the service distinguishes the silent period from SM, and whether anyone has seen the child in their home language (interpreter, home visit, recording).",
  "Ask about local SLT capacity and experience with SM — Primary Care versus CDNT — and whether your service has a keyworker model it recommends.",
  "Discuss how to assess a child who will not speak to you: non-verbal cognitive measures, pointing-response vocabulary tests, home recordings, and what cannot be concluded.",
  "Bring your own pull to 'get her to say something' in the session. Noticing it is part of the work.",
 ],

 "reflection": [
  "ON PRESSURE — Did I, even gently, ask a question that needed a spoken answer, or leave a silence waiting for one? What did the child's face and body do when I did?",
  "ON HOW I EXPLAINED IT — Did the teacher leave able to say why pressure fails, and with three specific things to do tomorrow?",
  "ON EAL — Did I establish the child's language history before concluding? Who told me — and did I use an interpreter with the family?",
  "ON MY LANGUAGE IN THE REPORT — did I write 'refuses', 'won't', 'uncooperative'? Those follow a child for years.",
  "ON THE WHOLE SYSTEM — did the plan reach the secretary, the SNA, the substitute and the coach, or only the class teacher?",
  "WHAT GOOD LOOKS LIKE: 'The teacher wanted me to get her talking in my session. I explained why I wouldn't try, completed a talking map with her mother present, and left the school with a named keyworker, a three-stage sliding-in plan and a toilet card. At review she was whispering to the keyworker.'",
  "WHAT POOR LOOKS LIKE: 'Child did not engage with the assessment.' — the mutism recorded as non-cooperation, scores reported from a verbal battery, and no plan.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "Johnson, M., & Wintgens, A. (2016). The selective mutism resource manual (2nd ed.). Speechmark. [Now distributed by Routledge — check the current edition.]",
  "Johnson, M., & Wintgens, A. (2012). Can I tell you about selective mutism? A guide for friends, family and professionals. Jessica Kingsley.",
  "Bergman, R. L., Piacentini, J., & McCracken, J. T. (2002). Prevalence and description of selective mutism in a school-based sample. Journal of the American Academy of Child & Adolescent Psychiatry, 41(8), 938–946.",
  "Cohan, S. L., Chavira, D. A., & Stein, M. B. (2006). Practitioner review: Psychosocial interventions for children with selective mutism: A critical evaluation of the literature from 1990–2005. Journal of Child Psychology and Psychiatry, 47(11), 1085–1097.",
  "Kristensen, H. (2000). Selective mutism and comorbidity with developmental disorder/delay, anxiety disorder, and elimination disorder. Journal of the American Academy of Child & Adolescent Psychiatry, 39(2), 249–256.",
  "Muris, P., & Ollendick, T. H. (2015). Children who are anxious in silence: A review on selective mutism, the new anxiety disorder in DSM-5. Clinical Child and Family Psychology Review, 18(2), 151–169.",
  "Tabors, P. O. (2008). One child, two languages: A guide for early childhood educators of children learning English as a second language (2nd ed.). Paul H. Brookes.",
  "Toppelberg, C. O., Tabors, P., Coggins, A., Lum, K., & Burger, C. (2005). Differential diagnosis of selective mutism in bilingual children. Journal of the American Academy of Child & Adolescent Psychiatry, 44(6), 592–595.",
  "Viana, A. G., Beidel, D. C., & Rabian, B. (2009). Selective mutism: A review and integration of the last 15 years. Clinical Psychology Review, 29(1), 57–67.",
 ],

 "pathway": {
  "age": "Onset is usually before age 5 (APA, 2022), but identification typically happens at school entry (junior infants) or at a transition, because that is when speaking to non-family adults becomes a daily expectation. The criteria exclude the first month of school, because initial quietness while settling is common and is not SM.",
  "who_diagnoses": "Ireland: CAMHS or Primary Care Psychology, frequently alongside SLT; a psychiatrist or clinical psychologist makes a formal diagnosis. SLTs often identify SM and lead the intervention. Where there are wider developmental needs the route may be the CDNT. Check local practice — it varies by area.",
  "who_wrote_report": "SLT (Primary Care, CDNT or private) most commonly; a CAMHS clinician; a Primary Care psychologist; a private psychologist. A school note or preschool report saying 'selective mutism' is a description, not a diagnosis. An earlier NEPS report may describe context-specific speech without naming it.",
  "refer_to": "SLT via GP / Primary Care (or CDNT if wider developmental needs) to assess speech and language — using home recordings — and to co-deliver the programme. Primary Care Psychology for anxiety-focused work; CAMHS where severe, generalised to home, or with low mood or risk. Audiology if hearing has not been checked.",
  "sooner": "'Many children with selective mutism are only noticed when school starts, because home is where they're comfortable — and a lot of families are told it's shyness. What matters is starting a gentle plan now. Earlier is easier, but it is never too late to start.'",
 },

 "differential": [
  "EAL SILENT PERIOD — new to the language; silent in English but may speak the home language with a same-language peer; receptive English building; fewer fear signs. Eases as language grows (Tabors, 2008). DSM-5-TR explicitly excludes mutism explained by lack of knowledge of the language.",
  "SHYNESS / SLOW TO WARM UP — speaks within days or weeks and speaks when it matters (to ask for help, to say they are hurt). Quiet, but not silent.",
  "LANGUAGE DISORDER or SPEECH SOUND DISORDER — difficulty is present at home too. SLT assessment.",
  "HEARING LOSS — audiology, particularly if hearing has not been checked since the newborn screen.",
  "SUDDEN-ONSET or TRAUMA-RELATED MUTISM — abrupt change in a child who previously spoke; consider safeguarding and medical causes first.",
 ],

 "next": [
  "Build the communication map with parent and school before any direct work.",
  "Brief every adult, agree a single 'no pressure' script, and put the practical plan (toilet, help, roll call) in place the same week.",
  "Set up a keyworker and sliding-in plan with SLT input; review against the communication map at an agreed date.",
  "Refer on if the anxiety has generalised, if there is low mood or risk, or if there is no movement after a reviewed plan.",
  "If risk or safeguarding emerged, none of the above — follow the protocol and tell your supervisor the same day.",
 ],

 "presentations": [
  "Speaks at home but not at school",
  "Whispers only to one friend or one adult",
  "Communicates only by nodding, pointing or writing",
  "Freezes when addressed directly",
  "Does not ask to use the toilet at school",
  "Silent period in a child new to English (not SM)",
  "Performance anxiety in oral work",
  "Reluctance to read aloud",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — onset is usually before 5; first seen in preschool or junior infants.",
   "prevalence": "Most cases begin here; band-specific rate not stated — check (DSM-5-TR range roughly 0.03–1% across samples).",
   "see": "Talks freely at home but not in preschool or junior infants; may freeze, avoid eye contact, not eat or use the toilet. Do not label settling-in quietness — the first month of school is excluded. This is the best window for intervention: sliding-in with the parent in the room works well at this age.",
   "tools": ["SDQ (2–4 version)", "BPVS-3", "Communication Matrix / AAC review",
             "Selective Mutism Questionnaire (SMQ; Bergman et al., 2008) — AGE young children, parent report (check the paper for age range) · MEASURES: frequency of speaking at school, at home and in social situations · CANNOT TELL YOU: why the child is silent, or language ability · TIME: about 10 min"],
  },
  "School Age": {
   "applies": "YES — main referral and intervention window.",
   "prevalence": "About 0.7% in one US early-primary school sample (Bergman et al., 2002); Irish rate not stated — check.",
   "see": "Silent in class, may whisper to one friend in the yard. Pressure points are reading aloud, Irish oral work, sacramental preparation, assemblies and performances. Assessment must avoid verbal demands — pointing-response vocabulary, non-verbal reasoning — and anything verbal must be reported with that limit stated.",
   "tools": ["SDQ", "RCADS", "BASC-3", "BPVS-3", "Leiter-3", "WNV (Wechsler Non-Verbal)",
             "Selective Mutism Questionnaire (SMQ; Bergman et al., 2008) — AGE primary school, parent report (check the paper for age range) · MEASURES: frequency of speaking across school, home and social settings · CANNOT TELL YOU: cause, or language ability · TIME: about 10 min",
             "SCAS (Spence Children's Anxiety Scale) — AGE roughly 8–15 child, parent version available (check) · MEASURES: anxiety symptoms by subscale, including social phobia and separation anxiety · CANNOT TELL YOU: diagnosis or risk · TIME: 10 min — the child can complete it in writing"],
  },
  "Adolescent": {
   "applies": "YES — usually long-standing rather than new; harder to shift, with social anxiety and low mood more prominent.",
   "prevalence": "New onset uncommon; residual social anxiety common (Muris & Ollendick, 2015) — rate not stated, check.",
   "see": "Transition to post-primary is both a risk and an opportunity — a fresh start where nobody knows the young person as 'the one who doesn't talk'. Plan the transition deliberately with the young person. Oral components (Irish, modern languages, CBA presentations) need planning early — check current SEC and school arrangements. Screen mood and risk in writing.",
   "tools": ["RCADS self-report", "Beck Youth Inventories-2", "MFQ (Mood and Feelings Questionnaire)", "BASC-3 SRP"],
  },
  "Young Adult": {
   "applies": "RARELY — persisting SM or residual social anxiety; adult services territory.",
   "prevalence": "Not stated — check before quoting.",
   "see": "Shows at college or work — interviews, tutorials, placements, phone calls. The EP role is transition planning and signposting: GP, adult mental health, college disability and access services. Do not hold the case.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — but check the differential especially carefully.",
   "prevalence": "Not stated — limited speech in these settings is more often language disorder, autism or intellectual disability.",
   "see": "SM is suggested where the young person has speech elsewhere (home) and the silence is context-specific and fear-linked. Start with a communication-mode review across settings, and ask the family for a recording of how the young person talks at home.",
   "tools": ["Communication Matrix / AAC review", "Vineland-3 / ABAS-3", "Functional behaviour assessment (ABC)"],
  },
 },
},

# =====================================================================================
# 2. SPECIFIC PHOBIA
# =====================================================================================
{
 "name": "Specific Phobia",
 "code": "DSM-5-TR Specific Phobia (ICD-10-CM F40.2xx — subtype codes, check before quoting) · ICD-11 6B03 Specific phobia — verify in the ICD-11 browser",
 "neps": "3. EMOTIONAL (3.2 Anxiety)",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.2.4 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Equal Status Acts 2000–2018 · Education (Welfare) Act 2000 · GDPR",

 "what_it_is": [
  "Marked fear or anxiety about a SPECIFIC object or situation that almost always provokes immediate fear, is actively avoided or endured with intense distress, is out of proportion to the actual danger, typically lasts 6 months or more, and causes significant distress or impairment (APA, 2022, DSM-5-TR).",
  "In children the fear may show as crying, tantrums, freezing or clinging (APA, 2022). Children do not need to describe it as fear or recognise it as excessive.",
  "Five specifiers (APA, 2022): ANIMAL; NATURAL ENVIRONMENT (heights, storms, water); BLOOD-INJECTION-INJURY; SITUATIONAL (lifts, planes, enclosed spaces); OTHER — in children often choking, vomiting (emetophobia), loud sounds or costumed characters.",
  "BLOOD-INJECTION-INJURY phobia is physiologically different: a rise then sudden drop in heart rate and blood pressure can cause fainting (vasovagal response). Applied tension was developed for this (Öst & Sterner, 1987). Relevant to school vaccination sessions.",
  "MAINTAINED BY AVOIDANCE. Each avoidance brings relief and prevents the child learning that the feared outcome does not happen or can be coped with. Exposure works by creating new, competing learning — the inhibitory learning account (Craske et al., 2014).",
  "EVIDENCE-BASED TREATMENT is CBT with graded exposure (James et al., 2020). Intensive one-session treatment has RCT support in young people (Ollendick et al., 2009). In Ireland this is delivered by Primary Care Psychology or CAMHS. The EP's role is formulation, school adjustments and supporting a clinician's plan.",
  "Normal fears follow a developmental sequence — separation and strangers in infancy; animals, dark and imaginary creatures in early childhood; injury and natural events in middle childhood; social and evaluative fears in adolescence (Gullone, 2000). A phobia is persistence, disproportion and impairment beyond this.",
 ],

 "what_it_is_not": [
  "NOT ordinary childhood fear. Most children fear the dark, dogs or monsters at some stage (Gullone, 2000). Diagnosis needs persistence, disproportion and impairment. Do not pathologise a developmentally normal fear.",
  "NOT helped by reassurance and avoidance alone. Both bring short-term relief and keep the fear alive. Family accommodation of anxiety is associated with greater symptom severity (Lebowitz et al., 2013).",
  "NOT exposure if it is forced. Making a child pat a dog without their agreement, or surprising them with the feared thing, is not exposure therapy — it can sensitise the child and damages trust. Exposure is graded, planned, agreed and repeated.",
  "NOT always what it looks like. Emetophobia can look like an eating difficulty or school refusal during winter bugs; choking phobia can look like food refusal; fear of hand dryers can look like a toileting problem. Always ask what the child fears will HAPPEN.",
  "NOT the same as sensory aversion in autism — though the two can sit together. A child who covers their ears at the hand dryer may be in sensory pain rather than fear. Both need a response; they need different responses.",
  "NOT usually the EP's to treat. CBT with exposure is delivered by Primary Care Psychology or CAMHS. Some EP services offer brief CBT-informed work under supervision — check your service model and your own competence (PSI 2.2.4).",
 ],

 "prevalence": [
  "OVERALL: DSM-5-TR reports approximately 5% in children and approximately 16% in 13–17-year-olds, with 12-month prevalence around 7–9% in US adult community samples (APA, 2022). Check the current text before quoting.",
  "IRELAND: no Irish phobia-specific prevalence figure stated here — check before quoting.",
  "SEX RATIO: females are affected about twice as often overall; animal, natural environment and situational types are more common in females, while blood-injection-injury is closer to equal (APA, 2022).",
  "ONSET: usually in childhood; DSM-5-TR describes onset commonly in middle childhood — check exact figures before quoting.",
  "MULTIPLE FEARS: most people with a specific phobia fear more than one object or situation, and co-occurrence with other anxiety disorders is common (APA, 2022).",
  "IMPAIRMENT IS THE THRESHOLD: high community rates in adolescence do not translate into referrals. Most phobias reaching an EP do so because they are stopping attendance, participation or eating.",
 ],

 "cooccurring": [
  {"name": "OTHER ANXIETY DISORDERS (separation, generalised, social)",
   "rate": "common (APA, 2022) — rate not stated here, check",
   "presents": "the phobia is the named fear, but worry spreads to anticipating it, to school mornings, to 'what if' questions. Formulate the whole anxiety picture, not one object."},
  {"name": "AUTISM",
   "rate": "specific phobia was among the most frequent anxiety disorders in autistic young people (van Steensel et al., 2011) — rate not stated here, check",
   "presents": "unusual or intense fears (hand dryers, balloons, particular objects), often tangled with sensory sensitivity. Adapt exposure: more visual, more predictable, and led by someone who knows autism."},
  {"name": "EMOTIONALLY BASED SCHOOL AVOIDANCE (EBSA)",
   "rate": "not stated — check",
   "presents": "avoiding school because the feared thing is on the route or in the building — a dog on the road, fire alarms, vomiting bugs going round, the school tour. Track attendance against the trigger."},
  {"name": "FEEDING DIFFICULTY / ARFID",
   "rate": "not stated — check",
   "presents": "food restriction driven by fear of choking or vomiting, not by body image. Weight, growth and energy are medical questions — GP or paediatrics."},
  {"name": "LOW MOOD (adolescence)",
   "rate": "not stated — check",
   "presents": "a narrowing life — dropping sport, trips, friends' houses — followed by withdrawal and hopelessness. Screen mood and ask directly about risk."},
 ],

 "recommendations": [
  "FORMULATE THE FEAR: the trigger, what the child predicts will happen, the avoidance and safety behaviours, and who accommodates. Write it in the report as a maintaining cycle in plain language.",
  "SCHOOL ADJUSTMENTS WITH AN EXIT PLAN: short-term accommodations (warning before fire drills, an alternative route, a named adult) are reasonable — each one written with how and when it will fade. An accommodation with no exit becomes avoidance.",
  "SUPPORT THE CLINICIAN'S EXPOSURE PLAN: where Primary Care or CAMHS have a hierarchy, school can run agreed steps (e.g., a dog topic in class, using the toilet with the dryer with an adult nearby). Coordinate — do not run a parallel programme.",
  "PRAISE APPROACH, NOT CALM: 'you stayed in the room when the dryer went on' rather than 'you weren't scared'.",
  "DON'T FORCE, DON'T AVOID: no surprises, no public confrontation with the feared thing, and no blanket exemption either.",
  "PARENT GUIDANCE: gently reduce accommodation, reward brave steps; signpost Creswell & Willetts (2019), 'Helping your child with fears and worries' — a parent-led CBT guide.",
  "BLOOD-INJECTION-INJURY FEAR AND SCHOOL VACCINATIONS: with parental consent, alert the HSE school vaccination team in advance; the child should be seated or lying down. Applied tension is taught by a clinician, not improvised.",
  "CONTINUUM LEVEL: Classroom Support for a mild, circumscribed fear; School Support where attendance or participation is affected; School Support Plus when Primary Care or CAMHS are involved.",
  "REFER: GP → Primary Care Psychology (mild–moderate) or CAMHS (severe, multiple anxieties, co-occurring low mood or risk) for CBT with exposure (James et al., 2020). GP / paediatrics if eating or weight is affected.",
  "DO NOT flood, trick or surprise the child; do not recommend permanent exemptions (swimming, tours, vaccinations) without a review date; do not advise on medication (PSI 2.2.2).",
 ],

 "explain_parent": [
  "'A phobia is a fear that has grown bigger than the danger. Her body reacts as if the dog is a real threat, even though part of her knows it probably isn't.'",
  "'Avoiding it brings relief, which is why it's so tempting — for her and for all of us. But every time we avoid it, the fear gets confirmed.'",
  "'The treatment with the best evidence is facing the fear gradually, in small steps she agrees to — that's exposure, usually as part of CBT. Some phobias improve with quite short treatment.'",
  "'Your part is to cheer on brave steps and gently cut back on the things we do to help her avoid it — not to force her.'",
  "'Lots of children have fears. What makes this one a problem is how much it's stopping her doing — and that's how we'll measure progress.'",
  "SIGNPOST: GP for referral to Primary Care Psychology or CAMHS; Creswell & Willetts (2019) 'Helping your child with fears and worries'.",
 ],

 "explain_teacher": [
  "'The fear is real even though the danger isn't. Telling her there's nothing to be afraid of won't help — her body has already decided.'",
  "'Short-term adjustments are fine — warn her before the fire drill — but each one needs a plan for how it fades, or it becomes permanent avoidance.'",
  "'Don't surprise her with the feared thing, and don't make her face it in front of the class. Small, planned, agreed steps are what work.'",
  "'If the clinician sends a step plan, school may be asked to run some steps. Ask exactly what they are and stick to them.'",
  "'Praise what she did — staying, trying, looking — not whether she looked calm.'",
 ],

 "explain_child": [
  "YOUNGER: 'Your brain has a smoke alarm to keep you safe. Yours is a bit too jumpy about dogs — it goes off loud even when it's just a little bit of burnt toast. We can teach it to calm down.'",
  "OLDER: 'A phobia is when your fear system overreacts to one thing. Avoiding it feels better straight away, but it teaches your brain the thing really was dangerous. Small steps teach it the opposite.'",
  "ASK: 'What do you think would happen if…?' The prediction is what the steps will test.",
  "BUILD A LADDER TOGETHER: the child rates each step 0–10 and chooses the first rung.",
  "NORMALISE: 'Loads of people have a fear like this — grown-ups too. It doesn't mean anything is wrong with you.'",
 ],

 "analogies": [
  "THE JUMPY SMOKE ALARM: 'It's meant to go off for a fire, but it's going off for burnt toast. The alarm isn't broken — it's too sensitive, and it can be retrained.' Works with children and parents.",
  "THE FEAR LADDER: 'We don't jump to the top. We start on a rung that's a bit scary but doable, stay there until it gets easier, then go up one.' Works with everyone — it is the treatment in one image.",
  "THE WAVE: 'Anxiety rises like a wave and falls if you stay. Leaving before it falls teaches your brain that leaving saved you.' Works with adolescents. Use loosely — inhibitory learning accounts (Craske et al., 2014) stress learning 'I can cope' over waiting for fear to drop.",
  "THE GUARD DOG: 'Your fear is a guard dog that barks at the postman every day. Every day we hide, it thinks the barking worked.' Works with parents — explains accommodation without blame.",
 ],

 "language": [
  "'Specific phobia' is the diagnostic term; with children 'fear' or 'worry' is usually better.",
  "Avoid calling the fear 'irrational' in front of the child — it feels dismissive. 'Bigger than the danger' is accurate and kinder.",
  "Avoid 'silly', 'dramatic' or 'babyish'. Children take these words as a verdict on themselves.",
  "Do not use 'phobia' loosely in reports for a normal developmental fear. PSI 1.2.8 — label opinion as opinion.",
 ],

 "red_flags": [
  "RED FLAG — food restriction with weight loss or faltering growth (fear of choking or vomiting). GP / paediatrics promptly; possible ARFID. Not a school-only plan.",
  "RED FLAG — a new, intense fear of a particular PERSON or PLACE (one adult, one house, one car). That is not a phobia until safeguarding has been considered. Tell your supervisor the same day; if there are indicators of abuse, follow Children First and report to Tusla as soon as practicable.",
  "RED FLAG — an adolescent whose world has narrowed, with low mood, self-harm or suicidal ideation. Ask directly and follow the risk protocol the same day.",
  "RED FLAG — fainting at injections or the sight of blood: first aid first, then consider blood-injection-injury phobia and alert the school health team with consent.",
  "BOUNDARY — you do not diagnose phobia and you do not deliver CBT beyond your competence. PSI 2.2.2, 2.2.4.",
  "WATCH — sensory aversion in autism, a proportionate fear after a real event (a dog bite), and developmentally normal fears. Distinguish before labelling.",
 ],

 "child_voice": [
  "FEAR LADDER built with the child. Good because the child controls the pace, and the same ladder becomes the plan and the measure.",
  "FEAR THERMOMETER ratings across situations. Good because it is quick, repeatable and gives a number for review meetings.",
  "EXTERNALISING — drawing and naming the worry (e.g., 'the worry monster'), after narrative practice (White & Epston, 1990). Good for younger children because it separates the child from the fear and makes 'bossing it back' possible.",
  "PREDICTION SPEECH BUBBLES — the child writes or draws what they think will happen. Good because it surfaces the catastrophic prediction that exposure steps will test.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) and DAY MAPPING. Good because they locate where in the school day the fear bites, which is where school adjustments go.",
 ],

 "questions": [
  "Q: 'Should we just keep her away from dogs until she grows out of it?' — A: 'Avoiding it helps today and makes it bigger over time. Some childhood fears do fade — but when a fear is stopping her doing things, gradual facing, at her pace, is what has the evidence.'",
  "Q: 'Is it my fault? I'm terrified of spiders myself.' — A: 'Children can pick up fears partly by watching the people they love, and there's an inherited part to anxiety. That's not blame. Letting her see you cope with your own fear can actually help.'",
  "Q: 'Can you do the therapy with her in school?' — A: 'The treatment for phobias is CBT with exposure, and in Ireland that comes through Primary Care Psychology or CAMHS. What I can do is help school understand it, plan adjustments that don't feed the fear, and support the steps once there's a plan.'",
  "Q: 'Should she be excused from swimming / the tour?' — A: 'Maybe for now, but only with a plan for how she builds back up to it, and a date to review. A permanent exemption usually makes the fear bigger.'",
  "Q: 'She was actually bitten by a dog. Isn't the fear reasonable?' — A: 'Being wary after a bite is completely understandable. It becomes a problem when the fear is far bigger than the risk and is stopping her walking to school. Phobias that start after a real event still respond to the same gradual approach.'",
  "Q: 'Will she need medication?' — A: 'That's a question for the doctor, not me. What I can tell you is that the treatment with the best evidence for phobias in children is CBT with exposure.'",
 ],

 "supervision": [
  "Bring any case where you are unsure whether a fear is developmentally normal or a phobia, and how you decided.",
  "Ask where the line sits in your service between EP support for graded exposure and clinical treatment that belongs with Primary Care or CAMHS.",
  "Discuss accommodations the school has already put in place that may be maintaining the fear, and how to raise that without blaming staff.",
  "Bring any feeding-related fear (choking, vomiting) and agree the medical route before any school plan.",
 ],

 "reflection": [
  "ON THE FORMULATION — Did I find out what the child predicts will happen, or did I stop at the name of the feared thing?",
  "ON ACCOMMODATIONS — Did every adjustment I recommended have an exit plan and a review date?",
  "ON MY ROLE — Did I stay within my competence, or drift into running exposure I was not trained or supervised for?",
  "ON HOW I EXPLAINED IT — Did the parent leave understanding why avoidance feels kind and keeps the fear going — without feeling blamed?",
  "ON NORMAL FEAR — Did I check the developmental norm before using the word phobia?",
  "WHAT GOOD LOOKS LIKE: 'The school had excused her from every fire drill for a year. I formulated the cycle with the teacher, and we agreed a warned-drill plan with a named adult, fading over a term, linked to the Primary Care psychologist's ladder. At review she had stayed for an unwarned drill.'",
  "WHAT POOR LOOKS LIKE: 'Anxious about fire alarms; continue to excuse from drills.' — accommodation with no exit, no formulation, no referral.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "Craske, M. G., Treanor, M., Conway, C. C., Zbozinek, T., & Vervliet, B. (2014). Maximizing exposure therapy: An inhibitory learning approach. Behaviour Research and Therapy, 58, 10–23.",
  "Creswell, C., & Willetts, L. (2019). Helping your child with fears and worries: A self-help guide for parents (2nd ed.). Robinson.",
  "Gullone, E. (2000). The development of normal fear: A century of research. Clinical Psychology Review, 20(4), 429–451.",
  "James, A. C., Reardon, T., Soler, A., James, G., & Creswell, C. (2020). Cognitive behavioural therapy for anxiety disorders in children and adolescents. Cochrane Database of Systematic Reviews, 2020(11), CD013162.",
  "Lebowitz, E. R., Woolston, J., Bar-Haim, Y., Calvocoressi, L., Dauser, C., Warnick, E., Scahill, L., Chakir, A. R., Shechner, T., Hermes, H., Vitulano, L. A., King, R. A., & Leckman, J. F. (2013). Family accommodation in pediatric anxiety disorders. Depression and Anxiety, 30(1), 47–54.",
  "Ollendick, T. H., Öst, L.-G., Reuterskiöld, L., Costa, N., Cederlund, R., Sirbu, C., Davis, T. E., III, & Jarrett, M. A. (2009). One-session treatment of specific phobias in youth: A randomized clinical trial in the United States and Sweden. Journal of Consulting and Clinical Psychology, 77(3), 504–516.",
  "Öst, L.-G., & Sterner, U. (1987). Applied tension: A specific behavioral method for treatment of blood phobia. Behaviour Research and Therapy, 25(1), 25–29.",
  "van Steensel, F. J. A., Bögels, S. M., & Perrin, S. (2011). Anxiety disorders in children and adolescents with autistic spectrum disorders: A meta-analysis. Clinical Child and Family Psychology Review, 14(3), 302–317.",
  "White, M., & Epston, D. (1990). Narrative means to therapeutic ends. W. W. Norton.",
 ],

 "pathway": {
  "age": "Usually begins in childhood (APA, 2022), but referral tends to come when the fear starts costing something visible — attendance, a school tour, swimming, eating, a vaccination session. Many circumscribed phobias never reach services at all because the feared thing can be avoided without much cost.",
  "who_diagnoses": "Ireland: Primary Care Psychology for mild–moderate presentations; CAMHS where severe, multiple or with co-occurring low mood or risk. A clinical psychologist or psychiatrist makes the diagnosis. Private clinical psychologists also assess. Check local referral criteria — they vary by area.",
  "who_wrote_report": "Primary Care psychologist; CAMHS clinician; private clinical psychologist; occasionally a paediatrician (e.g., in the context of feeding or fainting). A school note describing 'a phobia of dogs' is a description, not a diagnosis.",
  "refer_to": "GP first (also to rule out physical explanations, e.g., for fainting or food restriction) → Primary Care Psychology or CAMHS for CBT with exposure. Paediatrics / dietetics via GP if eating, weight or growth is affected. CDNT where autism is suspected and not yet assessed.",
  "sooner": "'Lots of children have strong fears, and most families quite reasonably wait to see if it passes. You came when it started getting in the way of her life — that's the right moment. Phobias respond well to treatment at any age.'",
 },

 "differential": [
  "DEVELOPMENTALLY NORMAL FEAR — typical for age (Gullone, 2000), not persistent or impairing. Reassure and monitor.",
  "SEPARATION ANXIETY — the fear is of being apart from the attachment figure, not of the object; the 'phobia' disappears when the parent is present.",
  "SOCIAL ANXIETY — the fear is of being watched or judged (e.g., vomiting in front of others), not of the object itself.",
  "OCD — avoidance driven by contamination or harm fears with rituals; ask what the child does to make it feel 'right'.",
  "SENSORY SENSITIVITY — distress from the noise, texture or light itself, often in autism; responds to sensory adjustment rather than exposure alone.",
  "PTSD / TRAUMA RESPONSE — fear linked to a traumatic event, with re-experiencing, avoidance and hyperarousal beyond the single object.",
 ],

 "next": [
  "Formulate the fear cycle with the child, parent and teacher — trigger, prediction, avoidance, accommodation.",
  "Review every current accommodation and give each an exit plan and review date.",
  "Refer via GP to Primary Care Psychology or CAMHS where impairment is significant; coordinate school steps with the clinician's plan.",
  "If eating, weight, fainting or safeguarding is involved, deal with that route first and tell your supervisor the same day.",
 ],

 "presentations": [
  "Fear of dogs affecting the walk to school",
  "Fear of vomiting (emetophobia) and school avoidance during illness outbreaks",
  "Fear of loud noises — fire alarms, hand dryers",
  "Needle fear and fainting at school vaccination",
  "Choking fear with food restriction at lunch",
  "Fear of storms or the dark",
  "Anticipatory anxiety about transitions",
  "Somatic complaints presenting at school (tummy aches, headaches)",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — but many fears are developmentally normal here; distinguish carefully.",
   "prevalence": "Band-specific rate not stated — check. Normal fears (dark, animals, noises) are very common at this age.",
   "see": "Crying, clinging, freezing or tantrums at the feared thing — dogs, loud noises, costumed characters, the dark. Diagnosis needs persistence and impairment beyond the age norm. Work is mainly with parents: reduce accommodation, model calm approach, small steps.",
   "tools": ["SDQ (2–4 version)",
             "Preschool Anxiety Scale (Spence et al., 2001) — AGE preschool, parent report (check manual) · MEASURES: anxiety symptoms including a physical injury fears subscale · CANNOT TELL YOU: whether a fear is outside the developmental norm without context · TIME: 10 min"],
  },
  "School Age": {
   "applies": "YES — common; referral comes when attendance, trips, eating or participation are affected.",
   "prevalence": "About 5% in children (APA, 2022, US data) — check current text; Irish rate not stated.",
   "see": "Avoidance of the route to school (dogs), fire drills, toilets with hand dryers, school tours, swimming, or lunch (choking). Somatic complaints before the feared event. School adjustments with exit plans, plus referral for CBT with exposure where impairing.",
   "tools": ["SDQ", "RCADS", "BASC-3",
             "SCAS (Spence Children's Anxiety Scale) — AGE roughly 8–15 child, parent version available (check) · MEASURES: anxiety symptoms by subscale, including physical injury fears · CANNOT TELL YOU: diagnosis or risk · TIME: 10 min"],
  },
  "Adolescent": {
   "applies": "YES — community rates are higher in this band; many never reach services.",
   "prevalence": "About 16% in 13–17-year-olds (APA, 2022, US data) — check current text; Irish rate not stated.",
   "see": "Often hidden and managed by avoidance — skipping science practicals (blood), school trips (flying, heights), vaccination. Look for a narrowing life and screen mood. Self-report becomes central; the young person should co-design the ladder.",
   "tools": ["RCADS self-report", "Beck Youth Inventories-2", "BASC-3 SRP", "MFQ (Mood and Feelings Questionnaire)"],
  },
  "Young Adult": {
   "applies": "YES — adult services territory.",
   "prevalence": "12-month prevalence around 7–9% in US adult samples (APA, 2022) — check.",
   "see": "Phobias affecting college placements (clinical settings for BII fear), travel for work or study, or driving. The EP role is signposting to GP and adult mental health, and supporting reasonable accommodations through college disability services.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — especially where autism is present; sensory and phobic responses often overlap.",
   "prevalence": "Not stated — check; elevated in autistic young people (van Steensel et al., 2011).",
   "see": "Intense fears of specific objects or sounds, expressed through behaviour rather than words. Use functional assessment to find the trigger, distinguish sensory pain from fear, and adapt any exposure to be visual and highly predictable.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3",
             "Anxiety Scale for Children – ASD (ASC-ASD; Rodgers et al., 2016) — AGE about 8–16, parent and child · MEASURES: anxiety in autistic young people, including uncertainty · CANNOT TELL YOU: diagnosis or risk · TIME: about 10 min — check current version"],
  },
 },
},

# =====================================================================================
# 3. PANIC DISORDER AND AGORAPHOBIA
# =====================================================================================
{
 "name": "Panic Disorder and Agoraphobia",
 "code": "DSM-5-TR Panic Disorder (ICD-10-CM F41.0) and Agoraphobia (F40.00) — separate diagnoses since DSM-5 · ICD-11 6B01 Panic disorder · 6B02 Agoraphobia — verify in the ICD-11 browser",
 "neps": "3. EMOTIONAL (3.2 Anxiety)",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.2.4 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Education (Welfare) Act 2000 · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "PANIC ATTACK: an abrupt surge of intense fear or discomfort that peaks within minutes, with four or more of thirteen symptoms — e.g., palpitations, sweating, trembling, breathlessness, choking feelings, chest pain, nausea, dizziness, chills or heat, numbness or tingling, derealisation, fear of losing control, fear of dying (APA, 2022). A panic attack is a specifier that can accompany many conditions; it is not a diagnosis on its own.",
  "PANIC DISORDER: RECURRENT, UNEXPECTED panic attacks, followed by at least one month of persistent worry about further attacks or their consequences and/or a maladaptive change in behaviour (e.g., avoiding exercise or unfamiliar places), not attributable to a substance or medical condition (APA, 2022).",
  "AGORAPHOBIA: marked fear of two or more of — public transport; open spaces; enclosed places (shops, cinemas); queues or crowds; being outside the home alone — because escape might be difficult or help unavailable if panic-like or embarrassing symptoms occur. The situations are avoided, need a companion, or are endured with intense fear; typically 6 months or more (APA, 2022).",
  "DSM-5 SEPARATED the two (they were linked in DSM-IV); either can be diagnosed without the other. They are held together here because in adolescents they often travel together, and the school picture — avoiding assembly, buses, crowded corridors, the exam hall — looks the same.",
  "COGNITIVE MODEL: Clark (1986) — panic arises from CATASTROPHIC MISINTERPRETATION of bodily sensations (racing heart → 'I'm having a heart attack'), which raises anxiety and the sensations in a vicious circle. Safety behaviours (sitting down, leaving, holding onto something, carrying water) stop the young person learning the catastrophe does not happen.",
  "EVIDENCE-BASED TREATMENT is CBT including interoceptive exposure (deliberately bringing on feared sensations) and situational exposure (Pincus et al., 2010; James et al., 2020), delivered by CAMHS, Primary Care Psychology or, for over-18s, adult mental health services. The EP's role is formulation, school adjustments, reintegration planning and consultation.",
 ],

 "what_it_is_not": [
  "NOT a single panic attack. Isolated panic attacks are relatively common in adolescence. Panic disorder requires RECURRENT UNEXPECTED attacks plus a month of worry or behaviour change (APA, 2022).",
  "NOT attention-seeking or drama. The physical symptoms are real — sympathetic arousal and often over-breathing. Staff who say 'she's putting it on' make the next attack more likely.",
  "NOT to be assumed psychological without a MEDICAL CHECK. Asthma, cardiac rhythm problems, thyroid problems, low blood sugar, caffeine or energy drinks, and substances (including cannabis) can produce similar symptoms (APA, 2022). GP first, every time.",
  "NOT the same as social anxiety or sensory overload. Ask what the young person fears will happen: 'I'll collapse, die, lose control' (panic); 'people will judge me' (social anxiety); 'it's too loud and bright' (sensory, often autism).",
  "NOT solved by always leaving, always going home, or a permanent 'exit pass'. These bring relief and maintain the belief that leaving prevented disaster (Clark, 1986). Any exit arrangement needs a return step and a fade plan.",
  "NOT school refusal in itself — but panic and agoraphobia are a common driver of emotionally based school avoidance in adolescence. An attendance plan without an anxiety formulation usually fails.",
 ],

 "prevalence": [
  "CHILDREN: panic disorder is uncommon before adolescence — DSM-5-TR reports prevalence below about 0.4% under age 14 (APA, 2022). Check the current text before quoting.",
  "ADOLESCENTS AND ADULTS: 12-month prevalence around 2–3% in US samples, rising through adolescence (APA, 2022) — check before quoting.",
  "AGORAPHOBIA: approximately 1.7% of adolescents and adults each year in DSM-5-TR data; onset commonly in late adolescence or early adulthood (APA, 2022) — check before quoting.",
  "SEX RATIO: females are affected about twice as often as males for both conditions, with the difference emerging in adolescence (APA, 2022).",
  "IRELAND: no Irish panic- or agoraphobia-specific prevalence figure stated here — check before quoting.",
  "PANIC ATTACKS (not disorder): more common than the disorder in adolescents — rate not stated here, check.",
 ],

 "cooccurring": [
  {"name": "DEPRESSION / LOW MOOD",
   "rate": "commonly co-occurs (APA, 2022) — rate not stated here, check",
   "presents": "hopelessness as life narrows — dropping sport, friends, school. Screen mood and ask directly about self-harm and suicidal thoughts."},
  {"name": "OTHER ANXIETY DISORDERS (separation, social, generalised)",
   "rate": "common — rate not stated here, check",
   "presents": "worry that extends beyond panic; childhood separation anxiety is described as a possible earlier history in some accounts — check before quoting. Formulate the anxiety as a whole."},
  {"name": "SUBSTANCE USE",
   "rate": "elevated — rate not stated here, check",
   "presents": "alcohol or cannabis used to manage anxiety; cannabis, stimulants and high-caffeine energy drinks can also trigger attacks. Ask, without judgement, and include it in the formulation."},
  {"name": "EMOTIONALLY BASED SCHOOL AVOIDANCE (EBSA)",
   "rate": "not stated — check",
   "presents": "late arrivals, leaving early, avoiding assembly, the bus or the exam hall, then whole days missed. Attendance data alongside the timetable shows where panic is concentrated."},
  {"name": "PHYSICAL HEALTH CONDITIONS (e.g., asthma)",
   "rate": "not stated — check",
   "presents": "breathlessness that is partly medical and partly panic, and each fuels the other. Needs GP or specialist input so that the school plan does not miss a medical emergency."},
 ],

 "recommendations": [
  "CONFIRM A MEDICAL CHECK FIRST. Before building a psychological plan, ask whether the GP has seen the young person about the physical symptoms. If not, recommend it.",
  "FORMULATE WITH CLARK'S CYCLE: trigger → body sensation → catastrophic thought → more anxiety → more sensation → safety behaviour. Write it in the young person's own words in the report (Clark, 1986).",
  "IN-SCHOOL PANIC PLAN, agreed with the young person: where to go, who to tell, how long, and how to RETURN to class. The aim is to stay in school, not to go home. One named adult.",
  "FADE SAFETY BEHAVIOURS WITH THE CLINICIAN: seating near the door, exit passes, a phone call home — reasonable at the start, but each needs a planned fade linked to the CAMHS or Primary Care exposure hierarchy.",
  "GRADED REINTEGRATION where attendance has dropped: a timetable of small steps, reviewed weekly, linked to the clinician's plan. Where absence reaches statutory reporting levels, the school has duties to Tusla Education Support Service (Education (Welfare) Act 2000) — check the current threshold and guidance.",
  "EXAMS: for school and State examinations, discuss arrangements with the school early — check the current SEC Reasonable Accommodations (RACE) scheme and any separate-centre provision; do not promise an accommodation you cannot confirm.",
  "PSYCHOEDUCATION for staff and young person: what panic is, that it peaks and passes, and — once medically checked — that it is not dangerous.",
  "CONTINUUM LEVEL: School Support Plus — clinical involvement (Primary Care, CAMHS or Jigsaw) is almost always needed.",
  "REFER: GP (medical check and referral); Primary Care Psychology or Jigsaw (youth mental health, roughly 12–25 — check local availability and remit) for mild–moderate presentations; CAMHS where severe, housebound, depressed or at risk; adult mental health services from 18.",
  "DO NOT deliver interoceptive exposure unless trained and supervised to do so; do not recommend home tuition as the solution without an anxiety plan — it can entrench avoidance; do not advise on medication (PSI 2.2.2).",
 ],

 "explain_parent": [
  "'A panic attack is the body's alarm system going off at full volume when there's no real danger. It's horrible, and it's real — her heart really is racing — but once the doctor has checked her over, it isn't dangerous.'",
  "'What keeps panic going is the fear of the next attack. She starts avoiding places where it might happen, and the world gets smaller.'",
  "'The treatment with the best evidence is a type of CBT that helps her learn the sensations are safe and that she can stay in the situations she's been avoiding — one step at a time.'",
  "'When she panics, the instinct is to bring her home. That brings relief today and makes school harder tomorrow. We'll agree a plan with school where she can settle and go back in.'",
  "'Please do make sure the GP has seen her about the physical symptoms. That protects her, and it also means we can all say with confidence that the sensations are not dangerous.'",
  "SIGNPOST: GP; Jigsaw (check local service); CAMHS via GP for severe presentations; HSE mental health information online — check current links before giving them.",
 ],

 "explain_teacher": [
  "'Panic attacks are real physical events — racing heart, breathlessness, dizziness — driven by a false alarm. She's not putting it on and she can't just calm down on request.'",
  "'Stay calm, use few words, and follow the agreed plan: the quiet space, the named adult, and a return to class. Our job is to help her stay, not to send her home.'",
  "'Short-term supports like sitting near the door are fine if they're part of the plan — each one has a fade date. Don't add new exits on the spot.'",
  "'If she has a medical condition such as asthma, follow the medical plan first. The panic plan never replaces a medical response.'",
  "'Crowded places — assembly, corridors at changeover, the exam hall — are often the hardest. Small adjustments there go a long way.'",
 ],

 "explain_child": [
  "YOUNGER (rare at this age): 'Sometimes our body's alarm goes off even when we're safe — your heart goes fast and you feel wobbly. It's scary, and it always passes.'",
  "OLDER: 'A panic attack is your body's alarm going off by mistake. Your heart races and you might feel you can't breathe or you're going to faint. It feels dangerous, but it isn't, and it always peaks and passes.'",
  "DRAW THE VICIOUS CIRCLE together: 'What did you notice in your body first? What did you think it meant? What did you do next?' Young people often find this a relief — it makes sense of something frightening.",
  "ASK: 'Where in school is hardest? Where is easiest?' and 'What do you do to feel safe?' The safety behaviours are what the plan will gradually test.",
  "NORMALISE WITHOUT MINIMISING: 'Lots of teenagers have panic attacks. They're really unpleasant, and they're very treatable.'",
 ],

 "analogies": [
  "THE FALSE ALARM: 'It's a smoke alarm going off with no fire. The noise is real and deafening — but there's nothing burning.' Works with young people, parents and staff.",
  "THE VICIOUS CIRCLE: 'Heart speeds up → you think “something's wrong” → that scares you → your heart speeds up more.' Clark's (1986) model in one line; works with adolescents who like to understand the mechanism.",
  "THE WAVE: 'Panic rises, peaks and falls within minutes if you let it. Leaving at the peak teaches your brain that leaving saved you.' Works with adolescents and staff; explains why the plan aims for return.",
  "THE SHRINKING MAP: 'Each place you avoid gets crossed off the map. Treatment is about colouring them back in, one at a time.' Works with parents and young people for agoraphobia.",
 ],

 "language": [
  "'Panic attack', 'panic disorder' and 'agoraphobia' are the accepted terms. In conversation, 'panic attacks' is usually enough and less alarming than the diagnostic label.",
  "Avoid 'hysterical', 'meltdown' (which has a specific meaning in autism), 'putting it on' or 'attention-seeking'.",
  "Avoid 'agoraphobic' as a description of a person; describe what they are finding hard ('finding it very hard to leave home at the moment').",
  "Do not write 'panic attack' in a report as a finding unless it has been described to you; write what was observed and reported. PSI 1.2.8.",
 ],

 "red_flags": [
  "RED FLAG — FIRST-TIME chest pain, collapse, or breathing difficulty in school: treat as a medical emergency first (school first-aid and emergency procedure). Panic is only considered once medical causes are excluded.",
  "RED FLAG — panic with low mood, hopelessness, self-harm or suicidal ideation. Ask directly and follow the same-day risk protocol; tell your supervisor the same day — supervision follows action, it does not replace it.",
  "RED FLAG — a young person who has become largely housebound. This is severe; CAMHS (or adult services if 18+), not a school-level plan alone.",
  "RED FLAG — substance use to manage panic, or panic starting after substance use. Include it in the referral; follow the risk protocol if there is danger.",
  "BOUNDARY — you do not diagnose panic disorder or agoraphobia, do not deliver interoceptive exposure beyond your competence, and do not advise on medication. PSI 2.2.2, 2.2.4.",
  "WATCH — asthma, cardiac and thyroid conditions, caffeine and energy drinks. Ask; recommend the GP check.",
 ],

 "child_voice": [
  "PANIC DIARY — when, where, first sensation, thought, what they did. Good because it reveals triggers and safety behaviours, and it is how CBT for panic usually starts — so it hands the clinician useful data.",
  "DRAWING THE VICIOUS CIRCLE together. Good because understanding the mechanism reduces fear of the sensations, and the young person owns the formulation.",
  "SCHOOL MAP — the young person colours places green, amber, red. Good because it turns vague avoidance into a precise hierarchy that school can act on.",
  "SCALING (0–10) of anxiety in specific situations. Good because it gives a repeatable measure for reintegration reviews.",
  "SOLUTION-FOCUSED questions about exceptions ('when did you expect to panic and it didn't happen?'). Good because they surface coping the young person has not noticed.",
 ],

 "questions": [
  "Q: 'Is she going to have a heart attack?' — A: 'That's exactly what panic makes people fear. It's why the GP check matters — once she's been checked, we can say with confidence that the racing heart is her alarm system, not her heart failing.'",
  "Q: 'Should we bring her home when she panics?' — A: 'It's the kindest-feeling thing, and it usually makes the next day harder. The plan is a quiet space, a named adult, and then back to class — with home as the exception, not the routine.'",
  "Q: 'Would home tuition be better until she's well?' — A: 'It can look like a solution, but it often shrinks her world further. If it's used at all, it should be short, with a planned route back. That's a decision for the whole team, including her clinician.'",
  "Q: 'Is it just hormones / exam stress?' — A: 'Adolescence is when panic often starts, and stress can trigger it. But recurrent panic that's changing what she does is worth treating properly — it doesn't usually pass on its own.'",
  "Q: 'Can she sit her exams somewhere separate?' — A: 'Possibly. It depends on the current SEC arrangements and the school's procedures, so let's raise it early and check — I won't promise something I can't confirm.'",
  "Q: 'Will she need medication?' — A: 'That's a decision for her doctor, not me. The psychological treatment with the best evidence is CBT that includes gradually facing the feared sensations and places.'",
 ],

 "supervision": [
  "Bring the formulation (Clark's cycle) and check it with your supervisor before feeding back to school.",
  "Ask where the boundary lies in your service between supporting a reintegration plan and delivering exposure-based treatment.",
  "Discuss how to raise a medical check with a family who is sure it is 'just anxiety' — or sure it is a heart problem.",
  "Bring any case where attendance has fallen to statutory reporting levels and agree who holds the Tusla link.",
  "Discuss how you asked about risk and substance use, word for word.",
 ],

 "reflection": [
  "ON THE MEDICAL QUESTION — Did I check that physical causes had been considered before I formulated anxiety?",
  "ON SAFETY BEHAVIOURS — Did my recommendations add exits without a fade plan? Would they make the world bigger or smaller in six weeks?",
  "ON RISK — Did I ask directly about mood, self-harm and substances, or did I skip it because the referral said 'anxiety'?",
  "ON MY ROLE — Did I stay in the EP role — formulation, adjustments, reintegration — or drift into therapy I was not trained or supervised for?",
  "ON HOW I EXPLAINED IT — Could the teacher describe the vicious circle after our meeting, and say what to do in the next attack?",
  "WHAT GOOD LOOKS LIKE: 'She was being sent home after every attack. I drew the vicious circle with her, confirmed the GP had seen her, and agreed a plan with the year head: quiet room, ten minutes, back to class, linked to the CAMHS clinician's hierarchy. Four weeks later she was staying full days.'",
  "WHAT POOR LOOKS LIKE: 'Experiences anxiety in school; recommend she may leave class when needed.' — no medical check, no formulation, an open-ended exit that will grow.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "Clark, D. M. (1986). A cognitive approach to panic. Behaviour Research and Therapy, 24(4), 461–470.",
  "Craske, M. G., Treanor, M., Conway, C. C., Zbozinek, T., & Vervliet, B. (2014). Maximizing exposure therapy: An inhibitory learning approach. Behaviour Research and Therapy, 58, 10–23.",
  "James, A. C., Reardon, T., Soler, A., James, G., & Creswell, C. (2020). Cognitive behavioural therapy for anxiety disorders in children and adolescents. Cochrane Database of Systematic Reviews, 2020(11), CD013162.",
  "Kearney, C. A., & Albano, A. M. (2007). When children refuse school: A cognitive-behavioral therapy approach — Therapist guide (2nd ed.). Oxford University Press.",
  "Pincus, D. B., May, J. E., Whitton, S. W., Mattis, S. G., & Barlow, D. H. (2010). Cognitive-behavioral treatment of panic disorder in adolescence. Journal of Clinical Child & Adolescent Psychology, 39(5), 638–649.",
  "Education (Welfare) Act 2000 (Ireland). https://www.irishstatutebook.ie/",
 ],

 "pathway": {
  "age": "Panic disorder usually begins in adolescence or early adulthood and is uncommon before puberty; agoraphobia commonly begins in late adolescence or early adulthood (APA, 2022). It is often identified through its consequences — falling attendance, leaving class, avoiding the bus or exam hall — rather than as panic.",
  "who_diagnoses": "Ireland: CAMHS (to 18) or Primary Care Psychology for mild–moderate presentations; Jigsaw may assess and support young people in its age range (check local remit); adult mental health services from 18. A psychiatrist or clinical psychologist makes the diagnosis. The GP rules out physical causes.",
  "who_wrote_report": "CAMHS psychiatrist or psychologist; Primary Care psychologist; Jigsaw clinician; private clinical psychologist; GP letter describing panic attacks (a description, not usually a formal diagnosis). A school incident log of 'panic attacks' is a description, not a diagnosis.",
  "refer_to": "GP first — medical check, and the route to CAMHS or Primary Care Psychology. Jigsaw for mild–moderate presentations where available (check). CAMHS where severe, housebound, with depression or risk. Adult mental health from 18. Tusla Education Support Service where statutory attendance thresholds are reached.",
  "sooner": "'Panic often starts in the teenage years and it can look like lots of other things — stress, a bug, not wanting to go to school. You've noticed the pattern, and that's the important step. It responds well to treatment.'",
 },

 "differential": [
  "MEDICAL CONDITIONS — asthma, cardiac arrhythmia, thyroid problems, hypoglycaemia; GP check first.",
  "SUBSTANCE OR CAFFEINE EFFECTS — energy drinks, cannabis, stimulants, withdrawal.",
  "SOCIAL ANXIETY DISORDER — attacks occur only in evaluative situations, and the fear is of judgement rather than of the sensations themselves.",
  "SPECIFIC PHOBIA — panic only in the presence of one feared object or situation (cued, not unexpected).",
  "SENSORY OVERLOAD IN AUTISM — distress in crowded, loud spaces driven by sensory load; may look like panic.",
  "PTSD — panic triggered by reminders of a traumatic event, with re-experiencing and hypervigilance.",
 ],

 "next": [
  "Confirm the GP has seen the young person about the physical symptoms.",
  "Formulate using Clark's cycle with the young person, and share it with school in plain language.",
  "Agree an in-school panic plan with a return step, and review every exit arrangement for a fade date.",
  "Refer to Primary Care, Jigsaw or CAMHS as severity indicates; link any reintegration plan to the clinician's hierarchy.",
  "If risk, substance use or safeguarding emerged, follow the protocol and tell your supervisor the same day.",
 ],

 "presentations": [
  "Sudden episodes of breathlessness or racing heart in class",
  "Leaving class repeatedly to the toilet or office",
  "Avoiding assembly, crowded corridors or the school bus",
  "Exam hall avoidance",
  "Test and exam anxiety",
  "Somatic complaints presenting at school (tummy aches, headaches)",
  "Anticipatory anxiety about transitions",
 ],

 "bands": {
  "Early Years": {
   "applies": "N/A — panic disorder and agoraphobia are not identified at this age.",
   "prevalence": "Not applicable — panic disorder is uncommon before adolescence (APA, 2022).",
   "see": "Sudden intense distress in a young child is far more likely to be separation anxiety, a specific fear, a sensory response or a medical problem. Formulate it as those, and involve the GP if there are physical symptoms.",
   "tools": [],
  },
  "School Age": {
   "applies": "RARELY — uncommon before puberty; consider other anxiety and medical causes first.",
   "prevalence": "Below about 0.4% under age 14 (APA, 2022) — check current text.",
   "see": "Episodes of breathlessness, dizziness or tummy pain with fear, usually in an older primary pupil approaching puberty. More often separation anxiety, generalised anxiety or a specific fear. GP check, then formulate the anxiety as a whole.",
   "tools": ["SDQ", "RCADS", "BASC-3",
             "SCAS (Spence Children's Anxiety Scale) — AGE roughly 8–15 child, parent version available (check) · MEASURES: anxiety symptoms by subscale, including panic/agoraphobia · CANNOT TELL YOU: diagnosis or risk · TIME: 10 min"],
  },
  "Adolescent": {
   "applies": "YES — the main onset window, especially after puberty and more often in girls.",
   "prevalence": "Rising through adolescence toward adult 12-month rates of around 2–3% (APA, 2022, US data) — check; Irish rate not stated.",
   "see": "Leaving class, avoiding assembly, the bus, crowded corridors or the exam hall; late arrivals and falling attendance. Self-report is essential. Ask directly about mood, self-harm and substances. Link any reintegration plan to the CAMHS or Primary Care clinician's exposure hierarchy.",
   "tools": ["RCADS self-report", "Beck Youth Inventories-2", "MFQ (Mood and Feelings Questionnaire)", "BASC-3 SRP",
             "SCAS (Spence Children's Anxiety Scale) — AGE roughly 8–15 child (check upper age), parent version available · MEASURES: anxiety symptoms by subscale, including panic/agoraphobia · CANNOT TELL YOU: diagnosis or risk · TIME: 10 min"],
  },
  "Young Adult": {
   "applies": "YES — agoraphobia commonly begins in late adolescence or early adulthood; adult services.",
   "prevalence": "Agoraphobia around 1.7% of adolescents and adults per year (APA, 2022) — check.",
   "see": "Difficulty travelling to college or work, attending lectures or exams, or leaving home alone. The EP role is signposting to GP and adult mental health, and supporting college disability-service accommodations with a view to return rather than permanent avoidance.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "RARELY — identified less often, probably under-recognised where communication is limited.",
   "prevalence": "Not stated for this population — check before quoting.",
   "see": "Panic-like episodes may appear as sudden distress, flight or aggression. Rule out medical causes and sensory overload first; use functional assessment to identify triggers, and seek clinical input for any anxiety treatment adapted to the young person's communication.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3",
             "Anxiety Scale for Children – ASD (ASC-ASD; Rodgers et al., 2016) — AGE about 8–16, parent and child · MEASURES: anxiety in autistic young people, including panic and uncertainty · CANNOT TELL YOU: diagnosis or risk · TIME: about 10 min — check current version"],
  },
 },
},

]
