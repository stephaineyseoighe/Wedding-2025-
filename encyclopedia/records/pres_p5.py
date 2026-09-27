# PRES batch 5 — descriptive (non-diagnostic) presentations.
# Context: Reference Part D, column N.
#   Item 1      sits under 3. EMOTIONAL (3.3 Obsessive-compulsive and related) — Part D: "check autism first"
#   Items 2–5   sit under 3. EMOTIONAL (3.4 Mood)
#   Items 6–10  sit under 3. EMOTIONAL (3.5 Trauma, attachment and loss)
#   Items 11–16 sit under 3. EMOTIONAL (3.6 School attendance) — Part D: "None. Everything here is a presentation."
#   Items 17–20 sit under 4. SOCIAL (4.1 Friendships and social skills)
# at every UCD Table 3 band. Part D routes:
#   3.3 → Primary Care | CAMHS (severe) | NEPS
#   3.4 → Primary Care (mild–mod) | CAMHS (mod–severe) | NEPS
#   3.5 → Primary Care (milder) | CAMHS (severe) | NEPS critical incident response | NEPS | community services
#   3.6 → NEPS | Primary Care | Educational Welfare (Tusla) | Paediatrics | NEPS for school supports
#   4.1 → CDNT | NEPS for school supports | NEPS with SLT | whole-school policy support

NEPS_33 = "3. EMOTIONAL (3.3 Obsessive-compulsive and related)"
NEPS_34 = "3. EMOTIONAL (3.4 Mood)"
NEPS_35 = "3. EMOTIONAL (3.5 Trauma, attachment and loss)"
NEPS_36 = "3. EMOTIONAL (3.6 School attendance)"
NEPS_41 = "4. SOCIAL (4.1 Friendships and social skills)"

PRES = []

# ---------------------------------------------------------------- 1
PRES.append({
 "name": "Ritual at transitions",
 "neps": NEPS_33,
 "related_to": ["Autism", "Obsessive-Compulsive Disorder", "Separation Anxiety Disorder", "Generalised Anxiety Disorder", "Tourette's Disorder"],
 "what_it_is": [
  "A description of a fixed sequence the child must carry out at a change point — touching the door frame on the way in, lining up in the same place, saying goodbye in exactly the same words, re-packing the bag in a set order before leaving the room. The transition cannot proceed until the sequence is done, and interrupting it produces distress out of proportion to the task.",
  "Ritualised behaviour is developmentally ordinary. Evans et al. (1997) found parent-reported 'just right' and routine behaviours are common in the preschool years and become less frequent in the early school years; Leonard et al. (1990) compared the childhood rituals of children with and without OCD and found considerable overlap in early ritual behaviour — check the paper before quoting detail. At this band the question is intensity, rigidity and cost — not presence.",
  "Transitions are where rituals cluster because they are the moments of highest uncertainty: leaving the known activity, not yet in the next. Boyer and Liénard (2006) frame ritual as a response to perceived potential threat — the sequence imposes predictability where the environment offers little.",
  "Part D places this under 3.3 with the flag 'check autism first'. The same observable ritual can serve three different functions — autistic need for sameness and predictability, anxiety reduction, or an OCD compulsion driven by an intrusive thought — and the function, not the behaviour, decides the response.",
 ],
 "what_it_is_not": [
  "NOT OCD by default. A compulsion in OCD is performed to neutralise an unwanted intrusive thought or feared outcome ('if I don't touch it three times, Mum will die'), and the child usually experiences it as unwanted. An autistic routine is usually experienced as right and comforting, and the distress comes when it is blocked. Ask what would happen if it were not done.",
  "NOT defiance or delay tactics. The child who must finish the sequence before lining up is not choosing to hold up the class. Treating it as non-compliance increases the uncertainty the ritual was managing.",
  "NOT something to eliminate by blocking it. Abrupt removal of a ritual usually raises distress and often produces a substitute ritual. The target is flexibility and reduced cost, not zero ritual.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: bedtime sequences, insisting on the same cup, the same route into preschool, the same goodbye. Mostly typical (Evans et al., 1997). Part D: rarely identified at this age — parent report; routines are developmentally normal here.",
  "SCHOOL AGE 6–12: rituals that persist or intensify after 6–7, that take more than a few minutes, or that the child hides or is embarrassed by warrant a closer look. Watch the start of the day, yard-to-class, and home time.",
  "ADOLESCENT 13–16: post-primary multiplies transitions (eight or more room changes a day). Rituals may move out of sight — mental counting, re-checking lockers, arriving late to avoid a crowded corridor. Self-report emerges; ask directly and privately.",
  "YOUNG ADULT 17–26: rituals around leaving home, starting a lecture or shift. Adult services lead; your role is describing the functional cost in the course or workplace.",
  "SPECIAL SETTING: Part D — distinguish autistic routine from compulsion; the function differs. In a child with limited speech, a ritual may be the only way of signalling 'I don't know what's coming next'.",
 ],
 "assess": [
  "Map the transitions: which ones trigger a ritual, how long it takes, what happens if it is interrupted, and which transitions pass with none. The ones that pass are as informative as the ones that don't.",
  "Ask the function directly, at the child's level: 'What would happen if you didn't do it?' A feared catastrophe points towards anxiety or OCD; 'it wouldn't feel right' or 'I'd not know what to do next' points towards predictability needs.",
  "Parent and teacher interview on onset and course: gradual since early childhood (more consistent with an autistic profile) versus sudden onset or rapid escalation (warrants GP review; Part D route is Primary Care, CAMHS if severe).",
  "Look for the wider pattern without diagnosing: social communication, sensory responses, other repetitive behaviours (SRS-2 parent and teacher), and anxiety across settings (RCADS, SDQ). CY-BOCS is administered by clinical services, not NEPS (Part D).",
 ],
 "recommendations": [
  "MAKE THE TRANSITION PREDICTABLE so the ritual has less work to do: visual timetable, a 'now / next' board, a warning before the change (e.g., two-minute signal), the same adult at the door. Visual structure and work systems support independence for autistic pupils (Hume et al., 2009).",
  "BUILD THE RITUAL IN rather than fight it where it is short and harmless: time allowed at the start of the line-up, a designated spot. Then agree small, planned variations with the child — never an unannounced removal.",
  "REDUCE THE TRANSITION LOAD in the plan: fewer unnecessary room changes, leaving class a minute early at post-primary to avoid the crowd, a consistent route.",
  "RECORD IN THE STUDENT SUPPORT FILE which transitions, which supports, and a review measure (e.g., minutes from bell to seated; number of interrupted transitions per week). CONTINUUM LEVEL: Classroom Support to School Support; School Support Plus where CAMHS or CDNT is involved.",
  "REFER — via GP to Primary Care or CAMHS where rituals are driven by intrusive feared thoughts, take up significant time, or have escalated quickly; to CDNT where a wider autism question has not been explored. DO NOT label the behaviour 'OCD' or 'autistic' in the report; describe it and its function.",
 ],
 "explain_parent": [
  "'A lot of children her age have little routines at changeover times. It's how she makes the change feel safe. What we're looking at is how much time it takes and how upset she gets if it's interrupted.'",
  "'The goal isn't to stop it. It's to make the changes around her more predictable so she needs the routine less, and to stretch it gently with her agreement.'",
  "'If it ever sounds like she's doing it to stop something bad happening — to you, to her — tell me or your GP, because that's a different thing and there's good help for it.'",
 ],
 "explain_teacher": [
  "'When he stops at the door to do his sequence, he isn't stalling you. The change is the hard bit; the routine is how he gets through it.'",
  "'A two-minute warning and a picture of what's next will cut most of the delay. Blocking the routine usually makes the next transition worse.'",
  "'Keep a quick tally of which changes set it off. That's the most useful thing you can bring to the next review.'",
 ],
 "explain_child": [
  "YOUNGER: 'Lots of people have a special way of doing things when something changes. Let's make a picture list so you know what's coming, and see if your special way gets easier.'",
  "OLDER: 'Changeovers seem to be the hard part for you. Is the routine something that feels right, or something you feel you have to do in case something bad happens? Either answer's okay — it helps me know what will help.'",
  "ASK: 'Which change in the day is the worst one? Which one is easiest?' — the child's ranking gives you the order to work in.",
 ],
 "red_flags": [
  "WATCH — rapid onset of rituals, intrusive thoughts or new tics, especially after an infection: refer to the GP promptly; this is a medical question, not a classroom one.",
  "WATCH — rituals taking so long that the child is late, missing lessons or avoiding school: link to the attendance presentations (3.6) and review the plan.",
  "BOUNDARY — you describe and formulate. Whether it is OCD, autism or anxiety is a diagnostic question for CAMHS, Primary Care or the CDNT.",
 ],
 "questions": [
  "Q: 'Is this OCD?' A: 'Routines at transitions are common and often not OCD. What matters is why she does it and what it costs her. If she is doing it to stop something bad happening, I'd suggest the GP, who can refer on.'",
  "Q: 'Should we just not let him do it?' A: 'Stopping it suddenly usually makes things harder and he may swap in a new routine. We make the change more predictable first, then stretch the routine with him.'",
  "Q: 'She's fine at home — why only at school?' A: 'Home has far fewer unplanned changes. School has dozens a day, set by other people. That's where the routine is working hardest.'",
  "Q: 'Will she grow out of it?' A: 'Many children do, and the research shows these routines usually fade after the early years (Evans et al., 1997). If it's growing rather than fading, that's the signal to look further.'",
 ],
 "supervision": [
  "Bring your function hypothesis: what did the child say when asked 'what would happen if you didn't?' — and how confident are you in the distinction between routine, anxiety and compulsion?",
  "Discuss whether a wider autism question has been missed, and how to raise it with parents without leading.",
 ],
 "citations": [
  "Evans, D. W., Leckman, J. F., Carter, A., Reznick, J. S., Henshaw, D., King, R. A., & Pauls, D. (1997). Ritual, habit, and perfectionism: The prevalence and development of compulsive-like behavior in normal young children. Child Development, 68(1), 58–68.",
  "Leonard, H. L., Goldberger, E. L., Rapoport, J. L., Cheslow, D. L., & Swedo, S. E. (1990). Childhood rituals: Normal development or obsessive-compulsive symptoms? Journal of the American Academy of Child and Adolescent Psychiatry, 29(1), 17–23.",
  "Boyer, P., & Liénard, P. (2006). Why ritualized behavior? Precaution systems and action parsing in developmental, pathological and cultural rituals. Behavioral and Brain Sciences, 29(6), 595–613.",
  "Hume, K., Loftin, R., & Lantz, J. (2009). Increasing independence in autism spectrum disorders: A review of three focused interventions. Journal of Autism and Developmental Disorders, 39(9), 1329–1338.",
 ],
})

# ---------------------------------------------------------------- 2
PRES.append({
 "name": "Low mood without diagnostic threshold",
 "neps": NEPS_34,
 "related_to": ["Major Depressive Disorder", "Persistent Depressive Disorder (dysthymia)", "Adjustment Disorder", "Generalised Anxiety Disorder", "Prolonged Grief Disorder"],
 "what_it_is": [
  "A description of a child or young person who is persistently sadder, flatter or more negative about themselves than usual, affecting how they engage in school, but where no one has made — and you should not imply — a diagnosis of depression.",
  "Subthreshold depressive symptoms are common and matter in their own right: they are associated with later depressive disorder and with current impairment (Thapar et al., 2012). NICE NG134 (2019, check for updates) uses the language of 'mild' versus 'moderate to severe' depression and recommends watchful waiting and low-intensity support for milder presentations.",
  "In the Irish context, the My World Survey (Dooley & Fitzgerald, 2012; Dooley et al., 2019) reported substantial levels of depressive symptoms among Irish adolescents — exact rates not stated here; check before quoting.",
  "Part D routes: Primary Care (mild–mod), CAMHS (mod–severe), NEPS. At School Age Part D notes that 'low mood often presents as irritability or refusal rather than sadness' — see the irritability entry.",
 ],
 "what_it_is_not": [
  "NOT ordinary sadness after a clear, recent event that is easing with time and support. Proportionate, time-limited low mood after a loss or disappointment is a normal response; watch the trajectory before you escalate.",
  "NOT 'just a phase' or 'teenagers are moody' when it persists for weeks and is changing how the young person functions. Dismissal is the most common reason low mood goes unsupported.",
  "NOT something an EP diagnoses. You describe mood, its duration and its impact, screen for risk, and signpost. Whether it reaches the threshold of a depressive disorder is for Primary Care, the GP or CAMHS.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: rarely framed as low mood; shows as less play, less pleasure, clinginess, sleep and appetite change. Part D: not assessed at this age — parent report on mood and play, refer.",
  "SCHOOL AGE 6–12: tearfulness, 'I'm stupid' or 'nobody likes me', somatic complaints, irritability, reduced effort. Parent and teacher report plus pupil interview; the MFQ is named in Part D.",
  "ADOLESCENT 13–16: withdrawal, sleep change, falling grades, loss of interest, harsh self-criticism, more time online. Self-report (MFQ, Beck Youth Inventories-2) becomes central. Part D: always screen for risk — see 3.7.",
  "YOUNG ADULT 17–26: disengagement from course or work, missed deadlines. Adult services lead; college counselling services are often the first stop.",
  "SPECIAL SETTING: mood against the setting baseline; staff who know the pupil best notice change in behaviour, sleep, eating and engagement before any self-report is possible.",
 ],
 "assess": [
  "Establish DURATION, PERVASIVENESS and CHANGE from baseline: how long, in which settings, and what the young person was like before. Collect parent, teacher and pupil accounts separately.",
  "Self-report screen at an appropriate age: MFQ (Mood and Feelings Questionnaire; Angold et al., 1995) or Beck Youth Inventories-2; check the manual or source for cut-offs before quoting any.",
  "ASK ABOUT SELF-HARM AND SUICIDAL THOUGHTS directly in every assessment of low mood in an adolescent. Asking does not plant the idea (Dazzi et al., 2014). Know the school's procedure before you ask.",
  "Look for the maintaining factors you can influence: bullying, learning difficulty, sleep, social isolation, family stressors, a recent loss.",
 ],
 "recommendations": [
  "NAME ONE KEY ADULT who checks in briefly and regularly — consistent with the emphasis on relationships and school connectedness in the Wellbeing Policy Statement and Framework for Practice (Department of Education, 2019 — check current version).",
  "ACTIVITY, NOT JUST TALK: agree small, achievable activities the young person used to value (a club, a role, time with a friend) — the logic of behavioural activation (Martell et al., 2010).",
  "ADDRESS THE MAINTAINING FACTOR you found: bullying response, learning support, reasonable adjustment of workload for a defined period with a review date.",
  "SIGNPOST: GP; Jigsaw (youth mental health, 12–25, check local availability); for parents, the SPHE and wellbeing supports in school. Primary Care Psychology for mild–moderate; CAMHS for moderate–severe (via GP).",
  "CONTINUUM LEVEL: Classroom Support for mild, transient low mood; School Support where a plan is needed; School Support Plus when outside agencies are involved. Review in 4–6 weeks — if not improving, escalate.",
  "DO NOT recommend universal classroom CBT or mindfulness as the response to one young person's low mood; trials of school-wide programmes have not shown benefit over usual provision (Stallard et al., 2012; Kuyken et al., 2022).",
 ],
 "explain_parent": [
  "'What we're seeing is low mood — she's been flatter and harder on herself for a few weeks. That isn't a diagnosis. It's something to take seriously and to watch.'",
  "'The things that help most are ordinary: one adult in school she trusts, keeping up small things she used to enjoy, sleep, and sorting out anything that's weighing on her.'",
  "'If it gets worse, lasts beyond a few more weeks, or she says anything about not wanting to be here, go to the GP — and tell us, the same day.'",
 ],
 "explain_teacher": [
  "'He's not being lazy. Low mood drains energy and makes everything feel pointless. A brief, warm check-in from you does more than a talk about effort.'",
  "'Notice and tell someone if anything changes — especially if he mentions hurting himself or not being around. Follow the school procedure the same day.'",
 ],
 "explain_child": [
  "YOUNGER: 'Sometimes our feelings get stuck on sad or grumpy for a long time. That happens to lots of people. Let's find some small things that help and a grown-up you can tell.'",
  "OLDER: 'It sounds like things have felt heavy for a while. That's real, and it's not your fault. Doing small things you used to like can help even before you feel like doing them.'",
  "ASK: 'On a scale of 0–10, how's your mood most days? What would make it one point better?' — and always: 'Have you had thoughts of hurting yourself or not wanting to be alive?'",
 ],
 "red_flags": [
  "RED FLAG — any disclosure of suicidal thoughts, plans or self-harm: follow the school's suicide/self-harm and child safeguarding procedures the same day; do not leave the young person alone if at immediate risk; contact parents unless doing so increases risk; GP or emergency services as indicated. Supervision follows the action.",
  "RED FLAG — disclosure of abuse or neglect: Children First route; report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's own duty (Children First Act 2015).",
  "WATCH — low mood with marked change in eating, weight, or sleep, or with unusual beliefs or experiences: GP review.",
 ],
 "questions": [
  "Q: 'Is she depressed?' A: 'I can describe what I'm seeing — low mood for several weeks affecting school. Whether it meets the threshold for depression is for the GP or a mental health service to judge.'",
  "Q: 'Won't asking about suicide put the idea in his head?' A: 'No. Research consistently finds asking does not increase risk, and it often brings relief (Dazzi et al., 2014).'",
  "Q: 'Should she take time off?' A: 'Usually staying connected helps more than withdrawing. We can lighten the load for a few weeks with a plan and a review date.'",
  "Q: 'When should we go to the GP?' A: 'If it's lasted more than a couple of weeks and is getting in the way, go now. If there's any talk of self-harm, the same day.'",
 ],
 "supervision": [
  "Bring every case where you asked about self-harm — what you asked, the answer, and what you did. Supervision follows action; it never replaces it.",
  "Discuss how you word low mood in a report so it is taken seriously without implying a diagnosis.",
 ],
 "citations": [
  "Angold, A., Costello, E. J., Messer, S. C., Pickles, A., Winder, F., & Silver, D. (1995). The development of a short questionnaire for use in epidemiological studies of depression in children and adolescents. International Journal of Methods in Psychiatric Research, 5, 237–249.",
  "Dazzi, T., Gribble, R., Wessely, S., & Fear, N. T. (2014). Does asking about suicide and related behaviours induce suicidal ideation? What is the evidence? Psychological Medicine, 44(16), 3361–3363.",
  "Dooley, B., & Fitzgerald, A. (2012). My World Survey: National study of youth mental health in Ireland. Headstrong and UCD School of Psychology.",
  "National Institute for Health and Care Excellence. (2019). Depression in children and young people: Identification and management (NICE Guideline NG134). NICE.",
  "Thapar, A., Collishaw, S., Pine, D. S., & Thapar, A. K. (2012). Depression in adolescence. The Lancet, 379(9820), 1056–1067.",
 ],
})

# ---------------------------------------------------------------- 3
PRES.append({
 "name": "Loss of interest in school activities previously enjoyed",
 "neps": NEPS_34,
 "related_to": ["Major Depressive Disorder", "Persistent Depressive Disorder (dysthymia)", "Adjustment Disorder", "Substance use disorders", "Autism"],
 "what_it_is": [
  "A description of a CHANGE: the pupil who used to love hurling, choir, art or a particular subject has stopped going, stopped trying or says it's 'boring' — and the change is noticed by adults who knew them before.",
  "Loss of interest or pleasure (anhedonia) is one of the two core symptoms of a major depressive episode in DSM-5-TR (American Psychiatric Association, 2022) — but on its own it is a presentation with several possible explanations, not a symptom checklist item to tick.",
  "It is often noticed before sadness is. Young people may not say they feel low; they say things are pointless, they're tired, or they 'just don't want to'. The before/after contrast is the finding.",
  "Part D places it under 3.4 Mood; the referral routes are Primary Care (mild–mod), CAMHS (mod–severe) and NEPS.",
 ],
 "what_it_is_not": [
  "NOT the normal shifting of interests as young people grow. Dropping football for music at 14 is development; dropping everything and replacing it with nothing is the concern.",
  "NOT necessarily mood. A pupil who quits the team after a new coach, a humiliating incident or bullying in the changing room has a reason — find it. Self-determination theory (Ryan & Deci, 2000) reminds us that loss of autonomy, competence or relatedness in an activity reduces motivation without any mood disorder.",
  "NOT 'laziness'. Anhedonia reduces the anticipated reward of effort; exhortation to try harder rarely shifts it.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: less play, less curiosity, flat response to favourite things. Rare, and needs a GP and developmental view; think illness, hearing, and changes at home first.",
  "SCHOOL AGE 6–12: no longer wants to go to the club, stops drawing, doesn't join yard games. Teachers notice 'he used to light up at…'. Check for bullying and learning pressures.",
  "ADOLESCENT 13–16: drops out of sport, music or Transition Year activities; stops caring about grades. Also consider substance use, sleep, and online life. Self-report is informative — ask what it used to feel like.",
  "YOUNG ADULT 17–26: stops attending societies, lectures, work shifts. College counselling or GP; adult mental health services if moderate–severe.",
  "SPECIAL SETTING: staff notice withdrawal from preferred activities, reduced response to usual reinforcers, or regression in skills. Always rule out pain and illness in pupils who cannot report them.",
 ],
 "assess": [
  "Build a BEFORE / NOW timeline with parent, pupil and a teacher who knew the pupil earlier: which activities, when the change began, what else changed around then.",
  "Pupil interview: 'What was it like when you enjoyed it? What's different now — the activity, the people, or how you feel?' The answer separates an activity-specific reason from a general loss of pleasure.",
  "Screen mood (MFQ, Beck Youth Inventories-2 at adolescence) and ask about self-harm and suicidal thoughts.",
  "Check the alternative explanations: bullying, a change of coach/teacher, injury, sleep, substance use, learning difficulty making the activity harder, family change.",
 ],
 "recommendations": [
  "RECONNECT WITH ONE VALUED ACTIVITY in a small, low-pressure form — attending training without playing, helping at the club, one art session a week. Scheduling valued activity is the core of behavioural activation (Martell et al., 2010).",
  "REMOVE THE SPECIFIC BARRIER where there is one: bullying response, a changed role on the team, a different group.",
  "AGREE EXPECTATIONS FOR A DEFINED PERIOD: reduce pressure to perform while keeping connection; review in 4–6 weeks.",
  "CONTINUUM LEVEL: Classroom Support where the cause is local and resolving; School Support where a plan and key adult are needed; School Support Plus if Primary Care or CAMHS is involved.",
  "REFER via GP where loss of interest is broad (across most activities), persistent (more than a couple of weeks) and accompanied by other mood signs — Primary Care for mild–moderate, CAMHS for moderate–severe.",
 ],
 "explain_parent": [
  "'The important thing here is the change. He used to love hurling and now he doesn't want to go. That's worth understanding, not forcing.'",
  "'Sometimes there's a specific reason — something happened at the club. Sometimes it's a sign that mood is low overall. We'll try to find out which.'",
  "'Keeping a small connection — going to watch, helping out — is better than all-or-nothing.'",
 ],
 "explain_teacher": [
  "'You knew her before. Your description of what she was like then is the most useful evidence we have.'",
  "'Try a smaller role in the activity rather than full participation — the aim is connection, not performance.'",
 ],
 "explain_child": [
  "YOUNGER: 'You used to really like art. It seems like it's not fun right now. Can you tell me what's different?'",
  "OLDER: 'Sometimes when things feel flat, nothing seems worth doing — even things you used to love. That's a known thing and it can change. Doing a small bit often comes before feeling like it.'",
 ],
 "red_flags": [
  "RED FLAG — loss of interest alongside hopelessness or talk of not wanting to be alive: follow the school's suicide/self-harm procedure the same day; GP or emergency services as indicated.",
  "WATCH — sudden change with signs of substance use, new peer group, or unexplained money/possessions: consider safeguarding and the substance-use route.",
  "WATCH — loss of interest with loss of skills, weight change or physical symptoms: GP review.",
 ],
 "questions": [
  "Q: 'Isn't this just a teenager changing?' A: 'Changing interests is normal. Losing interest in everything and not replacing it is different, and that's what we're seeing.'",
  "Q: 'Should we make him go back to the club?' A: 'Forcing it tends to backfire. A smaller step — going along, helping — keeps the connection without the pressure.'",
  "Q: 'Does this mean she's depressed?' A: 'It can be part of low mood, but there are other reasons too. I'd look at the whole picture, and the GP is the person to decide about depression.'",
 ],
 "supervision": [
  "Bring the before/now timeline — does the pattern point to an activity-specific cause or a general loss of pleasure?",
  "Discuss how you asked about self-harm, what you would have done with a 'yes', and how you'd follow up at review.",
 ],
 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). American Psychiatric Publishing.",
  "Martell, C. R., Dimidjian, S., & Herman-Dunn, R. (2010). Behavioral activation for depression: A clinician's guide. Guilford Press.",
  "Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. American Psychologist, 55(1), 68–78.",
  "Thapar, A., Collishaw, S., Pine, D. S., & Thapar, A. K. (2012). Depression in adolescence. The Lancet, 379(9820), 1056–1067.",
 ],
})

# ---------------------------------------------------------------- 4
PRES.append({
 "name": "Withdrawal from peers",
 "neps": NEPS_34,
 "related_to": ["Major Depressive Disorder", "Social Anxiety Disorder (social phobia)", "Autism", "Selective mutism", "Posttraumatic Stress Disorder"],
 "what_it_is": [
  "A description of a child or young person who spends less time with peers than before, or less than is typical for their age — eating alone, staying in at break, leaving group chats, turning down invitations.",
  "Rubin, Coplan and Bowker (2009) distinguish social withdrawal (the child removes themselves from peer interaction) from active peer exclusion (peers remove the child). They look similar from the staffroom window and need different responses.",
  "Asendorpf (1990) separated three motivations: SHYNESS (wants to join, but anxious), UNSOCIABILITY (content alone, low desire to join) and AVOIDANCE (wants to be away from peers). Research summarised by Rubin et al. (2009) suggests unsociability on its own carries less risk than shyness or avoidance — check before quoting detail.",
  "Part D lists it under 3.4 Mood because withdrawal is a common behavioural sign of low mood — but it also sits on the 4.1 social presentations list in spirit. The formulation question is: is this a change, and what is driving it?",
 ],
 "what_it_is_not": [
  "NOT introversion. A child who has always preferred one friend and quiet activities, and is content, is not presenting with withdrawal. Change from baseline and distress are the signals.",
  "NOT always the child's choice. Check whether the pupil has been pushed out (bullying, relational aggression, a friendship group split) before concluding they have pulled back.",
  "NOT fixed by instructing the child to 'go and play'. Anxious or low children who are pushed into groups without support often have a worse experience and withdraw further.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: watching rather than joining is typical in new settings. Persistent, distressed solitary play, or no interest in peers at all, may warrant a CDNT developmental view.",
  "SCHOOL AGE 6–12: alone at yard, staying with adults, no party invitations. Yard observation shows whether the child approaches and is rebuffed, or doesn't approach.",
  "ADOLESCENT 13–16: leaving the lunch group, spending break in the library, disengaging online. Low mood, social anxiety and bullying (including online) are the main hypotheses. Ask privately.",
  "YOUNG ADULT 17–26: not joining societies, isolating in accommodation. Loneliness in college is a known risk; college counselling and GP.",
  "SPECIAL SETTING: interpret against the child's usual interaction style and the peer group actually available; withdrawal may reflect sensory overload in a busy room rather than mood.",
 ],
 "assess": [
  "Establish baseline and change: was the child previously sociable? When did it change, and what else changed then?",
  "Structured yard observation over at least two sessions: who initiates, what happens to the child's approaches, where the child positions themselves.",
  "Pupil interview on motivation: 'Would you like to be with others more, less or about the same?' — separates shyness, unsociability and avoidance (Asendorpf, 1990).",
  "Mood and anxiety screens (MFQ, RCADS, SDQ peer problems scale) and ask directly about bullying, online and offline.",
 ],
 "recommendations": [
  "STRUCTURED SOCIAL OPPORTUNITIES rather than open yard: lunchtime club, a buddy role, a job with a peer. Structure removes the need to initiate.",
  "WORK WITH THE PEER GROUP where exclusion is part of it — Circle of Friends has evidence for improving peer acceptance (Frederickson & Turner, 2003).",
  "KEY ADULT CHECK-IN to monitor mood and give the child a place to say what's happening.",
  "ADDRESS THE DRIVER: bullying response under the school's anti-bullying procedures; anxiety-focused support; mood support and signposting.",
  "CONTINUUM LEVEL: Classroom Support to School Support; School Support Plus where CAMHS, Primary Care or CDNT is involved. Review with an observable measure (e.g., number of breaks spent with a peer).",
 ],
 "explain_parent": [
  "'Some children like their own company and that's fine. What's different here is that she used to be with friends and has pulled back, and she doesn't seem happy about it.'",
  "'We want to find out whether she's pulling away or being left out, because the help is different.'",
 ],
 "explain_teacher": [
  "'Watch the first minute of yard. Does he try to join and get turned away, or not try at all? That tells us where to put the support.'",
  "'A small job with one other child at break is easier than being told to go and play.'",
 ],
 "explain_child": [
  "YOUNGER: 'I noticed you've been playing on your own a lot. Is that what you like, or would you like someone to play with?'",
  "OLDER: 'Some people like time alone. Some people want to be around others but it's hard right now. Which is closer for you?'",
 ],
 "red_flags": [
  "RED FLAG — withdrawal with hopelessness, self-harm or talk of not wanting to be alive: same-day school procedure; GP/emergency services as indicated.",
  "WATCH — withdrawal following a specific event, new fearfulness of particular people, or changes suggesting abuse: Children First; report to Tusla as soon as practicable.",
  "WATCH — withdrawal into online contact with unknown adults: safeguarding concern.",
 ],
 "questions": [
  "Q: 'Isn't she just shy?' A: 'Shyness is one explanation. The change from before is what makes me want to understand it more.'",
  "Q: 'Should we make him join in?' A: 'Pushing tends to backfire. Small, structured chances to be with others work better.'",
  "Q: 'Could it be bullying?' A: 'It could. We'll ask him directly and watch the yard, and if it is, the school's anti-bullying procedure applies.'",
 ],
 "supervision": [
  "Bring the yard observation — did the pattern suggest withdrawal or exclusion, and what would change your mind?",
  "Discuss how to ask about bullying and low mood in the same interview without overwhelming the child.",
 ],
 "citations": [
  "Asendorpf, J. B. (1990). Beyond social withdrawal: Shyness, unsociability, and peer avoidance. Human Development, 33(4–5), 250–259.",
  "Frederickson, N., & Turner, J. (2003). Utilizing the classroom peer group to address children's social needs: An evaluation of the Circle of Friends intervention approach. The Journal of Special Education, 36(4), 234–245.",
  "Rubin, K. H., Coplan, R. J., & Bowker, J. C. (2009). Social withdrawal in childhood. Annual Review of Psychology, 60, 141–171.",
 ],
})

# ---------------------------------------------------------------- 5
PRES.append({
 "name": "Irritability as the presentation of low mood in young people",
 "neps": NEPS_34,
 "related_to": ["Major Depressive Disorder", "Disruptive Mood Dysregulation Disorder", "Oppositional Defiant Disorder", "Generalised Anxiety Disorder", "ADHD"],
 "what_it_is": [
  "A description of a child or young person whose low mood shows mainly as irritability — snapping, quick anger, low frustration tolerance, sulking — rather than sadness or tearfulness.",
  "DSM-5-TR (American Psychiatric Association, 2022) allows irritable mood to stand in for depressed mood in children and adolescents for a major depressive episode. Part D (School Age) notes that low mood often presents as irritability or refusal rather than sadness.",
  "Stringaris et al. (2018) define irritability as an increased proneness to anger relative to peers, and note it is one of the commonest reasons young people are referred to mental health services — and one of the least specific.",
  "The danger in school is that irritability is read as behaviour and responded to with sanctions, while the mood underneath goes unseen.",
 ],
 "what_it_is_not": [
  "NOT the same as oppositional behaviour. Irritability is about mood (how easily angered); oppositionality is about behaviour towards authority. They co-occur but have different trajectories — irritability is more linked to later depression and anxiety (Vidal-Ribas et al., 2016).",
  "NOT Disruptive Mood Dysregulation Disorder unless diagnosed. DMDD is a specific DSM-5-TR diagnosis made by clinicians; do not use the term descriptively.",
  "NOT simply 'hormonal' or 'a phase' when it is persistent, pervasive across settings and a change from before.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: tantrums are developmentally expected. Persistent, severe irritability across settings warrants a GP or developmental view, not a mood label.",
  "SCHOOL AGE 6–12: short fuse, quick to tears of anger, 'everything's unfair', fights at yard. Ask about sleep, bullying, learning difficulty and home before concluding mood.",
  "ADOLESCENT 13–16: sharpness with teachers, conflict at home, slammed doors, withdrawal after outbursts. Self-report often reveals low mood the adults haven't seen. Screen for risk.",
  "YOUNG ADULT 17–26: irritability in relationships and work; adult services.",
  "SPECIAL SETTING: irritability may signal pain, illness, sensory overload or a communication breakdown — rule these out first, especially in pupils with limited speech.",
 ],
 "assess": [
  "Distinguish TONIC irritability (persistently cranky mood between outbursts) from PHASIC outbursts (Stringaris et al., 2018) — ask parents and teachers about both.",
  "Change from baseline, pervasiveness across settings, and duration.",
  "Pupil self-report on mood (MFQ, Beck Youth Inventories-2) — young people often report sadness adults haven't noticed. Always ask about self-harm and suicidal thoughts.",
  "Look for maintaining factors: sleep deprivation, bullying, unrecognised learning difficulty, ADHD, anxiety, family conflict, substance use.",
 ],
 "recommendations": [
  "REFRAME FOR STAFF: describe the irritability as a sign of how the pupil is feeling, not only as behaviour; ensure the behaviour plan includes a mood-support element.",
  "CALM, PREDICTABLE RESPONSES to outbursts: reduce audience, give time, return to the issue later. Avoid escalating power struggles.",
  "KEY ADULT who checks in on mood, not only behaviour.",
  "ADDRESS SLEEP AND OTHER MAINTAINERS through the parent conversation.",
  "CONTINUUM LEVEL: School Support; School Support Plus if external services involved. REFER via GP to Primary Care (mild–moderate) or CAMHS (moderate–severe) where irritability is persistent, pervasive and accompanied by other mood signs.",
  "DO NOT rely on escalating sanctions alone; they do not address the mood driving the behaviour.",
 ],
 "explain_parent": [
  "'In young people, low mood often comes out as crankiness rather than sadness. So the snapping might be telling us something about how he's feeling.'",
  "'That doesn't mean ignoring the behaviour — it means we also look after the mood.'",
 ],
 "explain_teacher": [
  "'Her short fuse may be the way low mood shows in her. Sanctions alone won't reach that.'",
  "'Give space in the moment, and have the conversation later when she's calm.'",
  "'Keep a note of when the outbursts happen — time of day, lesson, what came just before. Mornings after poor sleep and Mondays are common patterns.'",
 ],
 "explain_child": [
  "YOUNGER: 'Sometimes when we feel sad inside, it comes out as cross. Does that happen to you?'",
  "OLDER: 'You've been getting annoyed a lot lately. Sometimes that's what feeling low looks like from the outside. How have you actually been feeling?'",
 ],
 "red_flags": [
  "RED FLAG — irritability with hopelessness, self-harm or suicidal talk: same-day procedure; GP/emergency services as indicated.",
  "WATCH — irritability with elevated mood, reduced need for sleep or unusual ideas: GP/CAMHS review.",
  "WATCH — irritability with substance use or new risky behaviour: consider the substance-use and safeguarding routes.",
 ],
 "questions": [
  "Q: 'He's just cheeky — why are you talking about mood?' A: 'In young people, low mood often comes out as irritability. It's worth checking before we only treat it as behaviour.'",
  "Q: 'Is this DMDD?' A: 'That's a diagnosis a clinician would make. I can describe what we see and help decide whether a referral makes sense.'",
  "Q: 'What should we do when she explodes?' A: 'Stay calm, reduce the audience, give time, and talk later.'",
 ],
 "supervision": [
  "Bring a case where behaviour was the referral and mood emerged in interview — how did you rebalance the plan?",
  "Discuss how to present mood-driven behaviour to a school focused on sanctions.",
 ],
 "citations": [
  "Leibenluft, E., & Stoddard, J. (2013). The developmental psychopathology of irritability. Development and Psychopathology, 25(4 Pt 2), 1473–1487.",
  "Stringaris, A., Vidal-Ribas, P., Brotman, M. A., & Leibenluft, E. (2018). Practitioner review: Definition, recognition, and treatment challenges of irritability in young people. Journal of Child Psychology and Psychiatry, 59(7), 721–739.",
  "Vidal-Ribas, P., Brotman, M. A., Valdivieso, I., Leibenluft, E., & Stringaris, A. (2016). The status of irritability in psychiatry: A conceptual and quantitative review. Journal of the American Academy of Child and Adolescent Psychiatry, 55(7), 556–570.",
 ],
})

# ---------------------------------------------------------------- 6
PRES.append({
 "name": "Complex or developmental trauma",
 "neps": NEPS_35,
 "related_to": ["Complex PTSD", "Posttraumatic Stress Disorder", "Reactive Attachment Disorder", "Disinhibited Social Engagement Disorder", "ADHD", "Foetal Alcohol Spectrum Disorder"],
 "what_it_is": [
  "A description of the effects of repeated, prolonged, interpersonal harm — usually abuse, neglect or exposure to violence — occurring within a caregiving relationship during development. Cook et al. (2005) describe impact across attachment, biology, emotion regulation, dissociation, behavioural control, cognition and self-concept.",
  "van der Kolk (2005) proposed 'developmental trauma disorder' to capture this pattern; it was NOT adopted into DSM-5 or DSM-5-TR. Part D labels it 'Not a DSM diagnosis'. ICD-11 includes Complex PTSD (6B41), which requires PTSD symptoms plus disturbances in self-organisation — that is a clinical diagnosis, not what this entry describes.",
  "In school it is recognised by pattern and history, not a checklist: hypervigilance, rapid escalation, difficulty trusting adults, shame, controlling behaviour, difficulty with transitions and endings, and learning affected by chronic stress.",
  "Part D routes: Primary Care (milder), CAMHS (severe), NEPS, community services. At School Age: consultation on trauma-informed practice — do not conduct trauma interviews.",
 ],
 "what_it_is_not": [
  "NOT a diagnosis you can make or imply. Write 'the history and presentation are consistent with the effects of adverse early experience' — not 'he has developmental trauma'.",
  "NOT a reason to lower expectations or remove boundaries. Structure, predictability and warm limits are part of what helps (Bath, 2008).",
  "NOT the only explanation for attention and behaviour difficulty in a care-experienced child. ADHD, FASD, language disorder and learning difficulty are all more common in this group and are easily missed when everything is attributed to trauma.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: indiscriminate approach to adults or no approach at all, extreme distress at separation or none, sleep and feeding difficulty. Part D: parent and setting report only — do not screen a preschooler for trauma; refer.",
  "SCHOOL AGE 6–12: 'fight or flight' in class, controlling play, difficulty with praise, stealing or hoarding food, sabotage before holidays or endings.",
  "ADOLESCENT 13–16: risk-taking, self-harm, substance use, exploitation risk, volatile relationships with staff. Part D: self-report only where safe and the young person has chosen to speak — supervision first; CAMHS pathway.",
  "YOUNG ADULT 17–26: aftercare transitions (Tusla aftercare), unstable accommodation, disengagement from education. Adult services.",
  "SPECIAL SETTING: Part D — setting stability and staff consistency as the intervention; watch for staff turnover and placement moves.",
 ],
 "assess": [
  "Gather history from records and professionals (social worker, foster carer, Tusla) with consent — do NOT ask the child to recount traumatic events.",
  "Describe current functioning across settings: regulation, relationships with adults and peers, learning, triggers and what calms.",
  "Screen for the conditions easily overshadowed: language (CELF-5 UK / SLT), attention (Conners-4, BRIEF-2), learning attainments, and whether an FASD question has been raised.",
  "SDQ and BASC-3 can describe breadth of difficulty; they do not assess trauma. Trauma-specific assessment belongs to CAMHS or specialist services.",
 ],
 "recommendations": [
  "SAFETY, CONNECTION, REGULATION FIRST — Bath's (2008) three pillars: predictable routine, a named key adult, and co-regulation before expectations of self-regulation.",
  "PLAN FOR TRANSITIONS AND ENDINGS: advance notice of staff absence, holidays and changes; a planned goodbye rather than a sudden one.",
  "RELATIONAL RESPONSE TO BEHAVIOUR: repair after incidents; clear limits delivered without shaming. Consider emotion coaching (Gottman et al., 1996; Rose et al., 2015).",
  "CONTINUUM LEVEL: School Support Plus usually — multiple agencies (Tusla social work, CAMHS, CDNT) should be coordinated through one plan.",
  "REFER via GP to CAMHS where severe symptoms, self-harm or dissociation are present; Primary Care for milder presentations. Ensure Tusla social work is involved where the child is in care or known to services.",
  "DO NOT recommend reduced timetables or exclusion as behaviour management without a planned return — for this group, rejection experiences compound the problem.",
 ],
 "explain_parent": [
  "'Children who've had frightening or unpredictable early experiences often stay on high alert. What looks like bad behaviour is often his body reacting as though he's still unsafe.'",
  "'The things that help are ordinary but hard to keep up: predictability, one trusted adult, and staying calm when he isn't.'",
  "'This is not about blame. It's about what his brain learned to expect, and it can learn something new.'",
 ],
 "explain_teacher": [
  "'Her reaction is fast because her alarm system is set high. Lowering your voice and giving space works better than raising the stakes.'",
  "'Tell her in advance if you'll be absent. Unannounced changes of adult are among the hardest things for her.'",
  "'Structure and limits still matter — delivered warmly, with repair afterwards.'",
 ],
 "explain_child": [
  "YOUNGER: 'Some children's bodies go into \"danger mode\" really quickly, even when they're safe. We're going to help your body learn school is a safe place.'",
  "OLDER: 'Your reactions make sense given what you've been through. They're not who you are. We want to find what helps you stay steady here.'",
  "ASK: 'Who in school do you feel safe with? What helps when things get too much?' — do NOT ask about the traumatic events themselves.",
 ],
 "red_flags": [
  "RED FLAG — any new disclosure or indicator of abuse or neglect: Children First route; report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty.",
  "RED FLAG — self-harm, suicidal ideation, or signs of exploitation: same-day risk procedure.",
  "BOUNDARY — you do not conduct trauma therapy or trauma interviews. Consult with CAMHS or specialist services on therapeutic needs.",
 ],
 "questions": [
  "Q: 'Does she have developmental trauma?' A: 'That's not a formal diagnosis. I can describe how her experiences seem to be affecting her in school and what helps.'",
  "Q: 'Should we go easy on the rules?' A: 'No — predictability and clear limits help. How we deliver them matters: calmly, without shame, and with repair afterwards.'",
  "Q: 'Could it be ADHD instead?' A: 'It could be both, or either. Children with difficult early histories also have higher rates of ADHD and language difficulty. That's why I'd keep those questions open.'",
  "Q: 'Should we ask him what happened?' A: 'No. If he chooses to tell you, listen and follow the child protection procedure. Don't go looking.'",
 ],
 "supervision": [
  "Bring any case where you felt pulled into rescuing or into anger — trauma presentations evoke strong reactions in staff and in you.",
  "Discuss how to write the formulation so it doesn't imply a diagnosis and doesn't close off other explanations.",
 ],
 "citations": [
  "Bath, H. (2008). The three pillars of trauma-informed care. Reclaiming Children and Youth, 17(3), 17–21.",
  "Cook, A., Spinazzola, J., Ford, J., Lanktree, C., Blaustein, M., Cloitre, M., DeRosa, R., Hubbard, R., Kagan, R., Liautaud, J., Mallah, K., Olafson, E., & van der Kolk, B. (2005). Complex trauma in children and adolescents. Psychiatric Annals, 35(5), 390–398.",
  "van der Kolk, B. A. (2005). Developmental trauma disorder: Toward a rational diagnosis for children with complex trauma histories. Psychiatric Annals, 35(5), 401–408.",
  "World Health Organization. (2019). International classification of diseases for mortality and morbidity statistics (11th rev.). https://icd.who.int/",
 ],
})

# ---------------------------------------------------------------- 7
PRES.append({
 "name": "Adverse Childhood Experiences (ACEs)",
 "neps": NEPS_35,
 "related_to": ["Posttraumatic Stress Disorder", "Complex PTSD", "Major Depressive Disorder", "Substance use disorders", "Conduct Disorder"],
 "what_it_is": [
  "A research framework, not a presentation in the child. The original ACE Study (Felitti et al., 1998) counted exposure to categories of abuse, neglect and household dysfunction (e.g., parental mental illness, substance use, domestic violence, incarceration, separation) and found a dose–response relationship between the number of categories and later adult health outcomes.",
  "Hughes et al. (2017) meta-analysis confirmed the association between multiple ACEs and a wide range of later outcomes, strongest for problematic substance use, mental ill-health and interpersonal violence.",
  "The ACE score is a population-level risk indicator. Anda, Porter and Brown (2020) — authors of the original study — warn explicitly against using it to screen or predict outcomes for an individual.",
  "Part D lists ACEs as 'Not a DSM diagnosis' under 3.5. In EP practice it is useful as a language for systemic conversations and for understanding cumulative adversity — not for scoring a child.",
 ],
 "what_it_is_not": [
  "NOT an individual screening tool. Lacey and Minnis (2020) review the limitations: the score treats very different experiences as equal, ignores timing, severity and protective factors, and has poor individual predictive accuracy.",
  "NOT destiny. Most children with high ACE counts do not develop the outcomes associated at population level; relationships, school connectedness and supportive adults buffer risk.",
  "NOT a label for a child. 'He's a high-ACE child' is stigmatising and inaccurate. Describe the needs and the protective factors.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: adversity at this age affects language, regulation and attachment most visibly. Work through the parent, the preschool and public health nurse; AIM and Tusla family support where relevant.",
  "SCHOOL AGE 6–12: difficulty with regulation, attention and relationships; attainment gaps. School can be the stable adult-rich environment the child lacks.",
  "ADOLESCENT 13–16: risk-taking, substance use, self-harm, early school leaving. Connectedness to school is a protective factor to protect.",
  "YOUNG ADULT 17–26: aftercare, further education access, employment. Adult services and community supports.",
  "SPECIAL SETTING: adversity and disability compound each other; children with disabilities are at increased risk of abuse — rate not stated here, check before quoting.",
 ],
 "assess": [
  "DO NOT administer an ACE questionnaire to a child or parent as part of an EP assessment. It is not validated for individual decision-making and can cause distress without a service to respond.",
  "Gather relevant history from appropriate sources with consent (social worker, GP, school records), focused on what is needed to understand current functioning.",
  "Map PROTECTIVE FACTORS as carefully as risks: key adults, interests, strengths, belonging.",
  "Describe current needs across learning, regulation and relationships with standard measures (SDQ, BASC-3, attainment) and observation.",
 ],
 "recommendations": [
  "BUILD PROTECTIVE FACTORS deliberately: a named key adult, a sense of belonging (clubs, roles), predictable routines.",
  "WHOLE-SCHOOL LENS: use ACE awareness to support trauma-informed practice across the school rather than to identify individual children.",
  "LINK WITH FAMILY SUPPORT: Tusla Prevention, Partnership and Family Support (PPFS) and Meitheal (check local arrangements) where families need wider support.",
  "CONTINUUM LEVEL: Classroom Support for whole-class practice; School Support or Support Plus for identified children with individual needs.",
  "DO NOT write ACE scores in reports.",
 ],
 "explain_parent": [
  "'Research shows that hard things happening in childhood can add up and affect how children feel and learn. But it's not a prediction — the right support makes a big difference.'",
  "'What matters most now is having steady adults around him, at home and at school. That's what we're building.'",
 ],
 "explain_teacher": [
  "'ACE research tells us about populations, not individual children. Don't count a child's ACEs — look at what they need and what's going well.'",
  "'Your relationship with her is one of the protective factors the research talks about.'",
 ],
 "explain_child": [
  "YOUNGER: (not usually discussed directly) 'Everybody has some things that are hard. School is a place where grown-ups want to help.'",
  "OLDER: 'Some things that have happened aren't your fault and aren't your whole story. We want to make sure you have people and things in school that help.'",
 ],
 "red_flags": [
  "RED FLAG — if gathering history reveals current abuse or neglect: Children First; report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's own duty.",
  "BOUNDARY — do not use ACE scores to determine eligibility, placement or prognosis.",
  "WATCH — schools using ACE checklists to 'identify' children: raise it in consultation and recommend a universal, trauma-informed approach instead.",
 ],
 "questions": [
  "Q: 'Should we screen all our pupils for ACEs?' A: 'No — the ACE score wasn't designed for individual screening and its own authors advise against it (Anda et al., 2020). A trauma-informed whole-school approach helps everyone.'",
  "Q: 'She's had so much happen — is it too late?' A: 'No. Relationships and school connection are protective at every age.'",
  "Q: 'Does a high ACE score mean he'll have problems later?' A: 'It raises the average risk across a population. It doesn't predict any one child's future.'",
 ],
 "supervision": [
  "Bring any report where adversity is described — does the language describe need and strength, or does it label?",
  "Discuss how to respond when a school wants to use an ACE checklist, and how you would explain the population-versus-individual distinction to staff.",
 ],
 "citations": [
  "Anda, R. F., Porter, L. E., & Brown, D. W. (2020). Inside the adverse childhood experience score: Strengths, limitations, and misapplications. American Journal of Preventive Medicine, 59(2), 293–295.",
  "Felitti, V. J., Anda, R. F., Nordenberg, D., Williamson, D. F., Spitz, A. M., Edwards, V., Koss, M. P., & Marks, J. S. (1998). Relationship of childhood abuse and household dysfunction to many of the leading causes of death in adults: The Adverse Childhood Experiences (ACE) Study. American Journal of Preventive Medicine, 14(4), 245–258.",
  "Hughes, K., Bellis, M. A., Hardcastle, K. A., Sethi, D., Butchart, A., Mikton, C., Jones, L., & Dunne, M. P. (2017). The effect of multiple adverse childhood experiences on health: A systematic review and meta-analysis. The Lancet Public Health, 2(8), e356–e366.",
  "Lacey, R. E., & Minnis, H. (2020). Practitioner review: Twenty years of research with adverse childhood experience scores – Advantages, disadvantages and applications to practice. Journal of Child Psychology and Psychiatry, 61(2), 116–130.",
 ],
})

# ---------------------------------------------------------------- 8
PRES.append({
 "name": "Bereavement reaction",
 "neps": NEPS_35,
 "related_to": ["Prolonged Grief Disorder", "Adjustment Disorder", "Posttraumatic Stress Disorder", "Major Depressive Disorder", "Separation Anxiety Disorder"],
 "what_it_is": [
  "A description of a child or young person's response to the death of someone important — parent, sibling, grandparent, friend, classmate, teacher. Grief is a normal response to loss, not a disorder (Part D: 'Not a DSM diagnosis').",
  "Children's grief is often intermittent — 'puddle jumping', a phrase used by UK child bereavement charities: intense one moment, playing the next. Adults can misread this as not caring. Worden (1996) found that most bereaved children in the Harvard Child Bereavement Study adapted over time, with a minority showing persistent difficulties.",
  "Grief is re-experienced at developmental milestones (First Communion, Confirmation, exams, debs) as the child understands the loss in new ways.",
  "Models useful in schools: the dual process model (Stroebe & Schut, 1999) — oscillation between loss and restoration is healthy; continuing bonds (Klass et al., 1996) — maintaining a connection with the person who died is normal and helpful.",
 ],
 "what_it_is_not": [
  "NOT something to 'get over' on a timetable. Grief changes shape rather than ending.",
  "NOT Prolonged Grief Disorder. PGD is a diagnosis (ICD-11 6B42; DSM-5-TR) made by clinicians when grief is persistent, pervasive and impairing beyond expected cultural norms, with duration criteria that differ between systems and by age — check current criteria before quoting.",
  "NOT a reason to avoid mentioning the person who died. Children usually want their loss acknowledged; silence can feel like the adults have forgotten.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: limited understanding of permanence; may ask repeatedly when the person is coming back; regression, clinginess, sleep difficulty. Use concrete language ('died', not 'gone to sleep').",
  "SCHOOL AGE 6–12: growing understanding of permanence and universality; may fear other people dying; concentration and learning dip; somatic complaints.",
  "ADOLESCENT 13–16: may grieve privately or with peers rather than adults; risk-taking, anger, withdrawal; peer deaths (including by suicide) need critical incident response.",
  "YOUNG ADULT 17–26: grief alongside major transitions; may take on family responsibilities.",
  "SPECIAL SETTING: understanding of death depends on developmental level; use concrete, consistent language and visual supports; watch behaviour change as communication of grief.",
 ],
 "assess": [
  "Usually NO formal assessment is needed — grief is normal. Consultation with parents and teachers on how the child is coping is the main activity.",
  "Establish the circumstances: expected or sudden; by suicide, accident or violence (traumatic bereavement needs a different response); the child's relationship to the person.",
  "Monitor over time: functioning at home and school, sleep, mood, whether distress is easing or intensifying.",
  "Refer for clinical assessment where grief is complicated by trauma symptoms, persistent severe impairment, or risk.",
 ],
 "recommendations": [
  "ACKNOWLEDGE THE LOSS: a named adult speaks to the child soon after return; agree with the child what classmates will be told.",
  "FLEXIBILITY WITH A PLAN: a 'time-out' card or quiet space; flexibility around homework and assessments for a period, with review.",
  "PLAN FOR ANNIVERSARIES AND MILESTONES: note the date in the Student Support File; alert new teachers at transition.",
  "SIGNPOST: Irish Childhood Bereavement Network (resources for families and schools); Barnardos and Rainbows Ireland programmes (check local availability); GP if concerned.",
  "CRITICAL INCIDENT: where a death affects the school community, follow the school's critical incident plan with NEPS support (NEPS, Responding to Critical Incidents guidelines — check current version).",
  "CONTINUUM LEVEL: Classroom Support in most cases; School Support where a plan is needed; School Support Plus with Primary Care or CAMHS if complicated.",
 ],
 "explain_parent": [
  "'It's normal for children to grieve in bursts — upset one minute, playing the next. That doesn't mean they don't care.'",
  "'Use clear words like \"died\". Phrases like \"lost\" or \"gone to sleep\" can confuse or frighten young children.'",
  "'Grief often comes back at milestones. That's not a setback; it's her understanding it in a new way.'",
 ],
 "explain_teacher": [
  "'Say something. \"I'm sorry your dad died\" is better than saying nothing.'",
  "'Ask him how he wants the class to know, and give him a way to step out if it gets too much.'",
  "'Note anniversaries and let next year's teacher know.'",
 ],
 "explain_child": [
  "YOUNGER: 'When someone dies, their body stops working and they can't come back. It's okay to feel sad, cross or even happy sometimes. All feelings are okay.'",
  "OLDER: 'There's no right way to grieve. Some days will be harder. It's okay to keep remembering them and talking about them.'",
  "ASK: 'Who can you talk to when you're missing them? What helps on the hard days?'",
 ],
 "red_flags": [
  "RED FLAG — talk of wanting to die to be with the person, self-harm, or suicidal ideation: same-day procedure; GP/emergency services as indicated.",
  "RED FLAG — bereavement by suicide in the school community: critical incident response with NEPS; heightened monitoring of vulnerable peers.",
  "WATCH — traumatic bereavement with intrusive images, avoidance, hyperarousal: refer via GP to CAMHS or Primary Care.",
 ],
 "questions": [
  "Q: 'Should he come to the funeral?' A: 'Children often cope better when they're included and prepared for what they'll see. It's a family decision — let him know what to expect.'",
  "Q: 'She seems fine — should I worry?' A: 'Children often grieve in bursts. Keep an eye out, let her know she can talk, and watch for changes over the coming months.'",
  "Q: 'When should we get professional help?' A: 'If his grief isn't easing over time, is stopping him living his life, or if there's any talk of self-harm, talk to the GP.'",
 ],
 "supervision": [
  "Bring your own reactions — bereavement work touches personal loss, and supervision is the place to notice it before it shapes your advice.",
  "Discuss how to distinguish normal grief from complicated or traumatic grief without pathologising, and what would make you recommend a GP referral.",
 ],
 "citations": [
  "Klass, D., Silverman, P. R., & Nickman, S. L. (Eds.). (1996). Continuing bonds: New understandings of grief. Taylor & Francis.",
  "Stroebe, M., & Schut, H. (1999). The dual process model of coping with bereavement: Rationale and description. Death Studies, 23(3), 197–224.",
  "Worden, J. W. (1996). Children and grief: When a parent dies. Guilford Press.",
  "National Educational Psychological Service. (2016). Responding to critical incidents: Guidelines and resource materials for schools. Department of Education and Skills.",
 ],
})

# ---------------------------------------------------------------- 9
PRES.append({
 "name": "Displacement, asylum and resettlement",
 "neps": NEPS_35,
 "related_to": ["Posttraumatic Stress Disorder", "Adjustment Disorder", "Prolonged Grief Disorder", "Major Depressive Disorder", "Separation Anxiety Disorder"],
 "what_it_is": [
  "A description of the educational and wellbeing needs of children and young people who have been forced to leave their home country — international protection applicants, programme refugees, those under temporary protection, separated children seeking international protection — and are settling in Ireland.",
  "Fazel et al. (2012) organise risk and protective factors in three phases: PRE-MIGRATION (exposure to violence, loss), MIGRATION (journey, separation from family) and POST-MIGRATION (housing instability, uncertainty about status, discrimination, school belonging). Post-migration factors are the ones school can change.",
  "Most displaced children are resilient; many will not need specialist mental health input, but most will benefit from school stability, language support and belonging.",
  "Part D places it under 3.5 (added). Routes: NEPS, Primary Care, CAMHS if severe, community services. In Ireland: International Protection Accommodation Services (IPAS) centres, Tusla Separated Children Seeking International Protection team, and Department of Education Regional Education and Language Teams (REALT) — check current arrangements.",
 ],
 "what_it_is_not": [
  "NOT the same as trauma. Many displaced children have experienced frightening events; not all are traumatised, and not all distress is trauma. Avoid assuming.",
  "NOT a learning difficulty. Limited English and interrupted schooling are not SEN. Cummins' distinction between conversational and academic language (Cummins, 2008) warns that fluent playground English can mask limited academic language.",
  "NOT something the child needs to talk about to heal. Pushing for the story can cause harm; many children need safety and routine first.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: regression, separation anxiety, sleep difficulty; parents' stress affects the child most directly. Support the parent.",
  "SCHOOL AGE 6–12: adjusting to a new language and school culture; may be the family interpreter; learning gaps from interrupted schooling.",
  "ADOLESCENT 13–16: age-appropriate class placement with language and curricular gaps; identity and belonging; separated minors have particular vulnerability.",
  "YOUNG ADULT 17–26: access to further education, employment, and status uncertainty; adult services.",
  "SPECIAL SETTING: children with disabilities may have had no prior assessment or schooling; assessment needs interpreters and culturally appropriate tools.",
 ],
 "assess": [
  "Use a qualified interpreter (not a family member, especially not a child) for parent consultation.",
  "Gather educational history: years of schooling, language(s) of instruction, literacy in first language.",
  "Be cautious with standardised tools: norms do not reflect this population; non-verbal tools (WNV, Leiter-3) reduce but do not remove bias. Dynamic assessment and curriculum-based observation over time are more informative.",
  "Screen wellbeing through observation and consultation (SDQ in the family's language if available and validated — check). Do not conduct trauma interviews.",
 ],
 "recommendations": [
  "BELONGING AND SAFETY FIRST: buddy system, a named adult, visual timetables, predictable routine (Hobfoll et al., 2007: safety, calm, connectedness, self-efficacy, hope).",
  "LANGUAGE SUPPORT: English as an Additional Language (EAL) support; value and maintain the home language.",
  "INTERPRETED COMMUNICATION WITH FAMILIES; recognise parents' own stress and uncertainty.",
  "LINK WITH SERVICES: Tusla (separated children); community organisations and NGOs supporting refugees (check local availability); GP registration.",
  "CONTINUUM LEVEL: Classroom Support for most; School Support for identified needs; School Support Plus if CAMHS or Tusla involved.",
  "DO NOT assess for SEN until the child has had sufficient time and language support — the right interval depends on the child; document why you are or are not assessing.",
 ],
 "explain_parent": [
  "(Through an interpreter) 'Many children who've moved countries take time to settle. School will help her feel safe and learn English, while keeping her own language strong.'",
  "'Your own wellbeing matters too. If you're finding things hard, please talk to your GP.'",
 ],
 "explain_teacher": [
  "'He may speak English in the yard but still need support with academic language — that takes years, not months (Cummins, 2008).'",
  "'Don't ask him about what happened before he came. Focus on making him feel safe and belonging here.'",
 ],
 "explain_child": [
  "YOUNGER: 'This is your school. [Name] is your buddy. If you need help, go to [adult].'",
  "OLDER: 'Moving to a new country is a big change. It's normal to miss home and to feel lots of things. Here's who you can talk to.'",
 ],
 "red_flags": [
  "RED FLAG — signs of trafficking, exploitation or abuse (especially separated minors): Children First; report to Tusla as soon as practicable.",
  "RED FLAG — self-harm, suicidal ideation: same-day procedure.",
  "WATCH — persistent re-experiencing, avoidance, hyperarousal affecting daily life: refer via GP to Primary Care or CAMHS.",
 ],
 "questions": [
  "Q: 'Should we get her assessed for learning difficulties?' A: 'Not yet — she needs time and language support first. We'll monitor and review.'",
  "Q: 'Should we ask him about the war?' A: 'No. If he wants to talk, listen. Focus on safety and belonging now.'",
  "Q: 'Can her older brother interpret at the meeting?' A: 'Please use a professional interpreter — it's fairer to him and more accurate.'",
 ],
 "supervision": [
  "Bring your assessment decisions — how did you avoid over- or under-identifying SEN, and what evidence would change your decision at review?",
  "Discuss your own cultural assumptions, how you brief and work with interpreters, and how you would respond if a family asked you to help with their protection application.",
 ],
 "citations": [
  "Cummins, J. (2008). BICS and CALP: Empirical and theoretical status of the distinction. In B. Street & N. H. Hornberger (Eds.), Encyclopedia of language and education (2nd ed., Vol. 2, pp. 71–83). Springer.",
  "Fazel, M., Reed, R. V., Panter-Brick, C., & Stein, A. (2012). Mental health of displaced and refugee children resettled in high-income countries: Risk and protective factors. The Lancet, 379(9812), 266–282.",
  "Hobfoll, S. E., Watson, P., Bell, C. C., Bryant, R. A., Brymer, M. J., Friedman, M. J., Friedman, M., Gersons, B. P. R., de Jong, J. T. V. M., Layne, C. M., Maguen, S., Neria, Y., Norwood, A. E., Pynoos, R. S., Reissman, D., Ruzek, J. I., Shalev, A. Y., Solomon, Z., Steinberg, A. M., & Ursano, R. J. (2007). Five essential elements of immediate and mid-term mass trauma intervention: Empirical evidence. Psychiatry, 70(4), 283–315.",
 ],
})

# ---------------------------------------------------------------- 10
PRES.append({
 "name": "Trauma-informed classroom practice",
 "neps": NEPS_35,
 "related_to": ["Posttraumatic Stress Disorder", "Complex PTSD", "Reactive Attachment Disorder", "Adjustment Disorder", "ADHD"],
 "what_it_is": [
  "The systemic response (Part D: 'the systemic response'). A whole-class and whole-school approach that assumes some pupils have experienced adversity, and organises routine, relationships and responses to behaviour so that they help rather than retraumatise — without needing to know which pupils.",
  "SAMHSA (2014) describes four Rs: REALISE the impact of trauma, RECOGNISE the signs, RESPOND by integrating knowledge into practice, and RESIST re-traumatisation. Six principles: safety; trustworthiness and transparency; peer support; collaboration; empowerment and choice; cultural, historical and gender issues.",
  "Classroom translation: predictable routines, calm adult responses, co-regulation before consequences, repair after conflict, and adult attunement (Bath, 2008).",
  "Evidence caution: Maynard et al. (2019) Campbell review found no studies meeting inclusion criteria to evaluate trauma-informed approaches in schools. The principles are well-grounded, but specific packages lack outcome evidence.",
 ],
 "what_it_is_not": [
  "NOT 'no consequences'. Structure and boundaries are part of safety.",
  "NOT therapy. Teachers are not being asked to treat trauma or to ask about it.",
  "NOT a branded programme you need to buy. The core practices are relational and low-cost.",
  "NOT a way to identify 'trauma children'. It is universal by design; singling pupils out undermines the principle of safety and transparency.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: key-person approach, predictable routines, co-regulation, and supporting parents' regulation.",
  "SCHOOL AGE 6–12: calm corners, emotion coaching, visual routines, restorative conversations; staff consistency across the day.",
  "ADOLESCENT 13–16: consistency across many subject teachers is hard — a key adult and shared plan; restorative practice; avoid public shaming.",
  "YOUNG ADULT 17–26: trauma-informed approaches in FE and third-level supports; adult services.",
  "SPECIAL SETTING: Part D — setting stability and staff consistency as the intervention.",
 ],
 "assess": [
  "Consult at whole-school or class level: map routines, transitions, responses to behaviour, and staff confidence.",
  "Observe a class with a focus on adult responses: tone, predictability, repair.",
  "Use staff and pupil voice (surveys, focus groups) to identify what feels safe and what doesn't.",
  "Review the code of behaviour against SAMHSA principles.",
 ],
 "recommendations": [
  "PREDICTABILITY: visual timetables, advance notice of change, consistent routines for start of day and transitions.",
  "CO-REGULATION BEFORE CONSEQUENCE: calm adult voice, reduced audience, time to settle — then the conversation.",
  "REPAIR AFTER CONFLICT: restorative conversation; the relationship is restored, not ended.",
  "STAFF WELLBEING: trauma-informed practice depends on regulated staff; support and supervision for staff are part of it.",
  "EMOTION COACHING as a teachable staff skill (Gottman et al., 1996; Rose et al., 2015).",
  "CONTINUUM LEVEL: Classroom Support (universal); integrate with NEPS Wellbeing framework and the school's SSE process.",
 ],
 "explain_parent": [
  "'The school is making its routines more predictable and its responses calmer. That helps every child, especially those who've had a hard time.'",
  "'It doesn't mean there are no rules — it means the rules are delivered calmly and relationships are repaired afterwards.'",
 ],
 "explain_teacher": [
  "'You don't need to know who has experienced trauma. Predictable routines, calm responses and repair help everyone.'",
  "'Regulate yourself first. A calm adult is the most powerful intervention in the room.'",
  "'Consequences still happen — after the child is calm, and with a way back.'",
 ],
 "explain_child": [
  "YOUNGER: 'In our class, we always know what's next, and if something goes wrong, we fix it together.'",
  "OLDER: 'If you're having a hard time, you can use the quiet space. We'll talk when you're ready.'",
 ],
 "red_flags": [
  "RED FLAG — disclosure of abuse or neglect: Children First; report to Tusla as soon as practicable.",
  "WATCH — trauma-informed language being used to avoid addressing unsafe behaviour or to avoid referral.",
  "WATCH — staff burnout and secondary trauma: consult with the principal on staff support.",
 ],
 "questions": [
  "Q: 'Isn't this just being soft?' A: 'No — it's about delivering structure calmly and repairing relationships. The rules stay.'",
  "Q: 'Is there evidence?' A: 'The principles are well-grounded, but specific school packages haven't been well tested (Maynard et al., 2019). We focus on the practices with the strongest rationale.'",
  "Q: 'Do we need to know which children have trauma?' A: 'No — the approach works for everyone.'",
 ],
 "supervision": [
  "Bring a consultation where staff were resistant — what concern sat underneath (workload, fairness, fear of losing control)?",
  "Discuss how to present the evidence honestly (Maynard et al., 2019) without undermining the approach, and how you'd evaluate change in one school.",
 ],
 "citations": [
  "Bath, H. (2008). The three pillars of trauma-informed care. Reclaiming Children and Youth, 17(3), 17–21.",
  "Gottman, J. M., Katz, L. F., & Hooven, C. (1996). Parental meta-emotion philosophy and the emotional life of families: Theoretical models and preliminary data. Journal of Family Psychology, 10(3), 243–268.",
  "Maynard, B. R., Farina, A., Dell, N. A., & Kelly, M. S. (2019). Effects of trauma-informed approaches in schools: A systematic review. Campbell Systematic Reviews, 15(1–2), e1018.",
  "Substance Abuse and Mental Health Services Administration. (2014). SAMHSA's concept of trauma and guidance for a trauma-informed approach (HHS Publication No. SMA 14-4884). SAMHSA.",
 ],
})

# ---------------------------------------------------------------- 11
PRES.append({
 "name": "Emotionally Based School Avoidance (school refusal)",
 "neps": NEPS_36,
 "related_to": ["Separation Anxiety Disorder", "Social Anxiety Disorder (social phobia)", "Generalised Anxiety Disorder", "Major Depressive Disorder", "Autism", "Somatic Symptom Disorder"],
 "what_it_is": [
  "A description of a child or young person who has severe difficulty attending school because of emotional distress, usually anxiety, where the parents know about the absence and have generally tried to get the child to school. Berg et al. (1969) set out the classic criteria that still frame 'school refusal' today; Heyne et al. (2019) update them and place school refusal alongside truancy, school withdrawal and school exclusion as four distinct attendance problems.",
  "EBSA is the UK and Irish educational-psychology term (West Sussex Educational Psychology Service, 2018) — it places the emphasis on emotional drivers and deliberately avoids implying wilfulness.",
  "Kearney and Silverman (1990) proposed four FUNCTIONS that maintain school refusal behaviour: avoiding school-related stimuli that provoke negative feelings; escaping aversive social or evaluative situations; seeking attention (often from a parent); and pursuing tangible rewards outside school. The first two are negatively reinforced; the last two positively. Function guides intervention.",
  "Part D: 'None. Everything here is a presentation.' — there is no diagnosis of EBSA. Routes: NEPS, Primary Care, Educational Welfare (Tusla), Paediatrics. At School Age, Part D names attendance data, separate parent/pupil/teacher accounts, the West EBSA framework and school-based risk factors; at Adolescence it is flagged as a core development area for you.",
  "A full CONDITION entry for EBSA exists elsewhere in the workbook; this row is the presentation-level summary to use at the referral stage.",
 ],
 "what_it_is_not": [
  "NOT truancy. In truancy the young person usually conceals the absence from parents, is not at home, and does not show marked anxiety about school itself (Berg et al., 1969; Heyne et al., 2019). The formulation and response differ — see the next entry.",
  "NOT 'a parenting problem'. Parents of children with EBSA are frequently exhausted from trying; blaming them closes the partnership you need for any return.",
  "NOT solved by waiting until the child 'feels ready'. Avoidance reduces anxiety in the short term and maintains it in the long term; the longer the absence, the harder the return (Kearney, 2008). Early, planned, graded return is the principle.",
  "NOT only anxiety. Egger et al. (2003) found both anxiety and depression associated with anxious school refusal in a community sample; unmet learning needs, autism and bullying are common contributors.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: preschool attendance is not compulsory — Part D says frame accordingly. Separation distress at drop-off is common and usually brief; persistent, escalating distress warrants a conversation with parents and the setting.",
  "SCHOOL AGE 6–12: tummy aches and headaches on school mornings that ease by mid-morning at home or at weekends; clinging at the gate; Sunday-night and end-of-holiday distress. Separation anxiety is prominent in younger children.",
  "ADOLESCENT 13–16: often begins or escalates at primary-to-post-primary transition or around exam years. Social evaluative fears, academic pressure, bullying (including online) and low mood are common drivers. Part D: pupil interview, EBSA framework, graded return plan, Tusla Educational Welfare involvement.",
  "YOUNG ADULT 17–26: Part D: course attendance and engagement. Disengagement from FE or college; supports through disability/access and counselling services.",
  "SPECIAL SETTING: Part D — attendance into and within the setting; transport as a factor. Sensory load, changes of staff and the bus journey itself can be the trigger.",
 ],
 "assess": [
  "ATTENDANCE DATA first: days attended out of days possible, pattern by weekday, lesson and time of year (Part D: Form 2 asks for days out of days). Partial attendance and late arrivals count.",
  "SEPARATE ACCOUNTS from parent, pupil and teacher — Part D notes they usually differ, and the difference is data. Use the West Sussex (2018) EBSA framework prompts or a structured interview.",
  "FUNCTION: School Refusal Assessment Scale–Revised (Kearney, 2002) child and parent versions to generate hypotheses about function — check licensing and norms before use.",
  "SCREEN ANXIETY AND MOOD (RCADS; MFQ in adolescence) and ASK ABOUT BULLYING, learning difficulty and self-harm.",
  "SCHOOL-BASED FACTORS: specific lessons, teachers, peers, spaces (canteen, corridors), transitions, exam pressure. Ask the pupil to rate parts of the school day.",
 ],
 "recommendations": [
  "EARLY RESPONSE: act on emerging patterns rather than waiting for chronic absence. Kearney and Graczyk (2014) propose a tiered, response-to-intervention approach that maps onto the Continuum of Support.",
  "GRADED RETURN PLAN agreed with the young person: small, specific steps (e.g., arrive and go to base room; one preferred lesson; build up) with a clear timeline and review dates. See the Return-to-school planning entry.",
  "ADDRESS THE FUNCTION: anxiety-management skills and graded exposure for avoidance/escape functions; a consistent morning routine and handover plan for separation; engagement in school-based positives where out-of-school rewards compete.",
  "KEY ADULT AND SAFE BASE in school; a meet-and-greet at arrival; an agreed exit card for overwhelm with a return-to-class expectation.",
  "CONTINUUM LEVEL: School Support for emerging EBSA; School Support Plus where absence is significant or CAMHS/Primary Care/Tusla Education Support Service is involved.",
  "REFER — via GP to Primary Care or CAMHS where anxiety or mood is moderate–severe; paediatrics where somatic complaints need medical review. Schools must notify Tusla Education Welfare when a pupil's absences reach 20 days in a school year (Education (Welfare) Act 2000 — check the current reporting requirements). DO NOT recommend home tuition or long-term reduced timetables as the plan — they tend to maintain avoidance.",
 ],
 "explain_parent": [
  "'This is not him being bold, and it's not your fault. His worry about school has grown to the point where avoiding it feels like the only way to cope.'",
  "'Staying home makes the worry go down today, but it makes tomorrow harder. We want to plan small, doable steps back, together.'",
  "'You'll get a plan with a named person in school, a clear first step, and a date we check how it's going.'",
 ],
 "explain_teacher": [
  "'When she comes in, a warm, low-key greeting matters more than any comment about being away.'",
  "'Tell us which lessons or moments seem hardest. That shapes the order of the return plan.'",
  "'Don't ask where she's been in front of the class. Agree with her what to say if other pupils ask.'",
 ],
 "explain_child": [
  "YOUNGER: 'Sometimes worries get really big about school and it feels safest to stay home. We're going to make a plan with small steps so school feels okay again.'",
  "OLDER: 'Avoiding school makes sense when it feels awful — it does make the anxiety drop, for a bit. But it tends to grow back bigger. What's the smallest step you think you could manage?'",
  "ASK: 'Rate each part of the school day 0–10 for how hard it is.' The ratings become the steps of the plan.",
 ],
 "red_flags": [
  "RED FLAG — self-harm or suicidal ideation: same-day procedure.",
  "RED FLAG — absence concealing abuse, neglect, young carer burden or exploitation: Children First; report to Tusla as soon as practicable.",
  "WATCH — somatic complaints without medical review: recommend GP/paediatric review before assuming they are anxiety-based.",
  "BOUNDARY — you formulate and plan the school response; anxiety disorders are diagnosed and treated by Primary Care or CAMHS.",
 ],
 "questions": [
  "Q: 'Should we just make her come in?' A: 'Force without a plan usually makes things worse. A graded return, with her agreement and clear steps, works better — and it still means coming in.'",
  "Q: 'Should he get home tuition?' A: 'Home tuition can maintain avoidance. We'd want a return plan first, with home tuition only if there's a clear medical reason.'",
  "Q: 'Is it anxiety or is he just being difficult?' A: 'The pattern — distress on school mornings, relief at weekends — points to anxiety. We'll look at what's driving it.'",
  "Q: 'Will Tusla get involved?' A: 'Schools notify Tusla Education Welfare when absences reach a set number of days. That's a support as much as a check, and it's routine.'",
 ],
 "supervision": [
  "Bring your function hypothesis and the evidence for it — how did the different accounts from parent, pupil and teacher shape it?",
  "Discuss how you balance urgency (early return) with the young person's agreement to the plan.",
 ],
 "citations": [
  "Berg, I., Nichols, K., & Pritchard, C. (1969). School phobia—Its classification and relationship to dependency. Journal of Child Psychology and Psychiatry, 10(2), 123–141.",
  "Heyne, D., Gren-Landell, M., Melvin, G., & Gentle-Genitty, C. (2019). Differentiation between school attendance problems: Why and how? Cognitive and Behavioral Practice, 26(1), 8–34.",
  "Kearney, C. A. (2008). School absenteeism and school refusal behavior in youth: A contemporary review. Clinical Psychology Review, 28(3), 451–471.",
  "Kearney, C. A., & Silverman, W. K. (1990). A preliminary analysis of a functional model of assessment and treatment for school refusal behavior. Behavior Modification, 14(3), 340–366.",
  "West Sussex Educational Psychology Service. (2018). Emotionally based school avoidance: Good practice guidance for schools and support agencies. West Sussex County Council.",
 ],
})

# ---------------------------------------------------------------- 12
PRES.append({
 "name": "Truancy distinguished from EBSA",
 "neps": NEPS_36,
 "related_to": ["Conduct Disorder", "Oppositional Defiant Disorder", "Substance use disorders", "Major Depressive Disorder", "ADHD"],
 "what_it_is": [
  "A description of absence where the young person is out of school WITHOUT their parents' knowledge or against their wishes, usually NOT at home, and without the marked anxiety about school that characterises EBSA (Berg et al., 1969; Heyne et al., 2019).",
  "Part D: 'different formulation, different response'. Truancy is more often associated with disengagement, conduct difficulties, peer influence and substance use; Egger et al. (2003) found truancy associated with conduct disorder and depression in a community sample.",
  "Truancy and EBSA can co-occur or shift over time — a young person avoiding a feared situation may begin to spend the time with peers. Heyne et al. (2019) recommend classifying the attendance problem explicitly because the interventions differ.",
  "Truancy is also a signal of unmet need: learning difficulty, bullying, low school connectedness, or problems at home can all sit underneath.",
 ],
 "what_it_is_not": [
  "NOT EBSA. The key distinguishing questions: do the parents know? Where is the young person? Is there distress about attending? Getting this wrong means applying graded exposure to a disengaged young person, or sanctions to an anxious one.",
  "NOT simply 'bad behaviour'. Truancy is linked to disengagement and unmet needs; enforcement without engagement rarely works long-term.",
  "NOT always without anxiety. Some young people who truant are avoiding a specific feared situation (an exam, a bully) — ask.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: not applicable — young children do not truant; absence is a parental decision (see Parentally condoned absence).",
  "SCHOOL AGE 6–12: rare in primary; leaving the school grounds is more often a safety and supervision issue.",
  "ADOLESCENT 13–16: the main band — skipping specific lessons, leaving at lunch, not arriving. Peer group, substance use and exploitation risk rise.",
  "YOUNG ADULT 17–26: non-attendance in FE/training; linked to disengagement and competing demands (work, caring).",
  "SPECIAL SETTING: absconding from the setting is a safety issue first; consider communication, sensory and anxiety drivers.",
 ],
 "assess": [
  "CLASSIFY the attendance problem using Heyne et al. (2019): parental knowledge, location during absence, emotional distress, parent effort to get the young person to school.",
  "ATTENDANCE DATA by lesson and time — patterns (e.g., only after lunch, only certain subjects) reveal drivers.",
  "PUPIL INTERVIEW on engagement: 'What's the point of school for you right now? Which parts are worth it?' — and on where they go and with whom.",
  "SCREEN for learning difficulty (literacy/attainment), mood, and substance use.",
 ],
 "recommendations": [
  "ENGAGEMENT BEFORE ENFORCEMENT: a key adult, a mentor, an interest-based hook (practical subjects, a role, work experience).",
  "ADDRESS THE UNDERLYING NEED: learning support; response to bullying; family support through Tusla Education Support Service or Home School Community Liaison (HSCL) where the school has one.",
  "CLEAR, CONSISTENT CONSEQUENCES alongside engagement — same-day parent contact on absence.",
  "CONTINUUM LEVEL: School Support; School Support Plus with Tusla Educational Welfare involvement where absence is persistent.",
  "REFER where conduct, substance use or exploitation concerns are present: CAMHS (with GP), addiction services, Tusla.",
 ],
 "explain_parent": [
  "'It sounds like he's leaving school without you knowing, and he's not worried about school so much as switched off from it. That needs a different plan to a child who's too anxious to go in.'",
  "'We'd like to work together — same-day contact if he's missing, and something in school that gives him a reason to be there.'",
 ],
 "explain_teacher": [
  "'Is she skipping because she's anxious, or because she's disengaged? The answer changes everything we do.'",
  "'Look at which lessons she misses — that pattern often tells us where the problem is.'",
  "'Same-day contact home when she's missing matters more than the size of the sanction. And when she is in, notice it.'",
 ],
 "explain_child": [
  "OLDER: 'I'm not here to give out. I want to understand what's going on when you're not in school, and what would make being here worth it.'",
  "ASK: 'Where do you go? Who with? Is there anything in school that you're avoiding?'",
 ],
 "red_flags": [
  "RED FLAG — signs of exploitation (criminal or sexual), including new possessions, older associates, or unexplained money: Children First; report to Tusla; Gardaí where there is immediate risk.",
  "RED FLAG — substance use with risk to safety: same-day procedure.",
  "WATCH — truancy masking anxiety or bullying: ask directly.",
 ],
 "questions": [
  "Q: 'Isn't truancy just the same as school refusal?' A: 'No. In school refusal, parents know and the child is anxious. In truancy, parents often don't know and the young person is disengaged. They need different plans.'",
  "Q: 'Should we just suspend him?' A: 'Suspension gives him more time out of school. Engagement and consequences together work better.'",
  "Q: 'What does Tusla do?' A: 'The Educational Welfare Service works with families and schools on attendance; it's a support and, in the end, has legal powers — check the current process.'",
 ],
 "supervision": [
  "Bring your classification — what evidence placed this as truancy rather than EBSA, and what would change your mind?",
  "Discuss how to hold engagement and safeguarding together when a young person is out of school and at risk.",
 ],
 "citations": [
  "Berg, I., Nichols, K., & Pritchard, C. (1969). School phobia—Its classification and relationship to dependency. Journal of Child Psychology and Psychiatry, 10(2), 123–141.",
  "Egger, H. L., Costello, E. J., & Angold, A. (2003). School refusal and psychiatric disorders: A community study. Journal of the American Academy of Child and Adolescent Psychiatry, 42(7), 797–807.",
  "Heyne, D., Gren-Landell, M., Melvin, G., & Gentle-Genitty, C. (2019). Differentiation between school attendance problems: Why and how? Cognitive and Behavioral Practice, 26(1), 8–34.",
 ],
})

# ---------------------------------------------------------------- 13
PRES.append({
 "name": "Parentally condoned absence",
 "neps": NEPS_36,
 "related_to": ["Separation Anxiety Disorder", "Relational problems (parent-child, sibling, upbringing away from parents)", "Somatic Symptom Disorder / Illness Anxiety", "Autism", "Major Depressive Disorder"],
 "what_it_is": [
  "A description of absence where the parent keeps the child at home, or knowingly permits absence, for reasons that are not a recognised, legitimate cause — to help at home, for company, because of the parent's own anxiety or illness, for holidays in term time, or because the parent does not see school as important.",
  "Heyne et al. (2019) call this 'school withdrawal' and list it as one of four distinct attendance problems (with school refusal, truancy and school exclusion). The defining feature is that the parent, not the child, is the main driver of the absence.",
  "It sits on a spectrum. At one end: a parent who is exhausted by a child's distress and has stopped trying (which is closer to EBSA). At the other: a parent who needs the child at home for their own reasons. The school's response depends on where the family is on that spectrum.",
  "Part D routes: NEPS for school supports, Primary Care, Educational Welfare (Tusla). Parents have a legal duty in relation to school attendance under the Education (Welfare) Act 2000 — check current provisions before quoting specific sections.",
 ],
 "what_it_is_not": [
  "NOT automatically neglect. Many families who keep children at home are struggling with illness, disability, poverty, mental health or caring responsibilities. Understand first.",
  "NOT EBSA, even when the child says they are anxious. Ask: who is driving the absence? A parent who fears for the child's safety in school (after bullying, say) is a different case from a parent who needs the child's company.",
  "NOT a reason for the EP to stand back as 'a Tusla matter'. The EP's contribution is formulation of the family's position and a school plan that makes attendance possible.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: preschool attendance is not compulsory; frame conversations as benefit, not duty.",
  "SCHOOL AGE 6–12: the parent is most in control of attendance at this age; young children can't get themselves to school. Watch for siblings with similar patterns.",
  "ADOLESCENT 13–16: may involve a young carer role (caring for a parent or siblings) — a hidden form; or parental agreement to avoid a conflict with an older child.",
  "YOUNG ADULT 17–26: less relevant — the young person decides; family demands may still compete with course attendance.",
  "SPECIAL SETTING: parents may keep a child home because of worry about care, transport, or a previous incident; build trust with the setting.",
 ],
 "assess": [
  "ATTENDANCE PATTERN across siblings and over time; the reasons given for absences, and whether they are consistent.",
  "PARENT CONSULTATION — non-judgemental, curious: 'What makes it hard to get him to school?' 'What would need to be different?'",
  "EXPLORE PARENT FACTORS with sensitivity: parent physical or mental health, caring load, previous negative school experience, belief about education, fear for the child's safety.",
  "PUPIL VOICE: 'What happens on the days you're at home? Would you rather be here?' — the child's own wish is important information and can reveal young caring roles.",
 ],
 "recommendations": [
  "BUILD THE RELATIONSHIP WITH THE PARENT: a named school contact; HSCL coordinator where the school has one; practical problem-solving (breakfast club, transport, morning routine).",
  "ADDRESS PARENT NEEDS through appropriate routes: GP for parent health; Tusla Family Support or Meitheal (check local arrangements); young carer supports.",
  "MAKE ATTENDANCE WORTH IT: the child's positive connection to school — a role, a friend, a club — is a lever the parent can see.",
  "CONTINUUM LEVEL: School Support Plus usually, with Tusla Education Support Service involvement once absence reaches the notification threshold.",
  "REFER — Tusla (Children First) where absence is part of a pattern of neglect or a child is being kept from school to conceal harm.",
 ],
 "explain_parent": [
  "'We can see it's been hard to get her in. We're not here to blame — we want to understand what's getting in the way and help with it.'",
  "'Every day she's here, she's building friendships and learning that are harder to catch up on later. What would make mornings easier?'",
  "'The school does have to let Tusla know when absences reach a certain level. That's routine, and they can often help.'",
 ],
 "explain_teacher": [
  "'This is the parent's decision more than the child's. Don't put the child in the middle — keep welcoming him warmly when he's here.'",
  "'A reason to come — a role, a friend, a job — sometimes helps the parent see the point of the effort.'",
 ],
 "explain_child": [
  "YOUNGER: 'We're really glad when you're here. We miss you when you're not.'",
  "OLDER: 'I know it's not always your decision whether you come in. What would you like to happen? Is there anything at home that makes it hard to get here?'",
 ],
 "red_flags": [
  "RED FLAG — absence concealing injuries, neglect or abuse: Children First; report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty.",
  "WATCH — young carer role: link with supports and consider welfare needs.",
  "WATCH — family travel or extended absence abroad with no return date: check the school's procedures for removal from the register and Tusla notification.",
 ],
 "questions": [
  "Q: 'Is it illegal to keep him home?' A: 'Parents do have legal responsibilities around attendance, and the school must notify Tusla after a certain number of absences. But the first step is understanding and helping.'",
  "Q: 'She's only missing a day here and there — does it matter?' A: 'It adds up quickly across a year, and it's harder to keep up with friendships and learning. Let's look at the pattern together.'",
  "Q: 'What if the parent won't engage?' A: 'Keep trying through the HSCL or a trusted staff member. If there are welfare concerns, Tusla must be informed.'",
 ],
 "supervision": [
  "Bring your formulation of the parent's position — where on the spectrum from 'exhausted' to 'withdrawing' is this family, and what evidence places them there?",
  "Discuss the line between supporting a family and a child protection concern, and when you'd cross it.",
 ],
 "citations": [
  "Heyne, D., Gren-Landell, M., Melvin, G., & Gentle-Genitty, C. (2019). Differentiation between school attendance problems: Why and how? Cognitive and Behavioral Practice, 26(1), 8–34.",
  "Kearney, C. A. (2008). School absenteeism and school refusal behavior in youth: A contemporary review. Clinical Psychology Review, 28(3), 451–471.",
  "Education (Welfare) Act 2000 (Ireland). https://www.irishstatutebook.ie/",
 ],
})

# ---------------------------------------------------------------- 14
PRES.append({
 "name": "Absence due to chronic illness",
 "neps": NEPS_36,
 "related_to": ["Epilepsy and its educational impact", "Somatic Symptom Disorder / Illness Anxiety / Conversion Disorder", "Major Depressive Disorder", "Separation Anxiety Disorder", "Acquired brain injury"],
 "what_it_is": [
  "A description of repeated or prolonged absence caused by a long-term health condition — asthma, diabetes, epilepsy, inflammatory bowel disease, cystic fibrosis, sickle cell disease, cancer treatment, ME/CFS, chronic pain, and others.",
  "Pinquart and Teubert (2012) meta-analysis found children with chronic physical illness had, on average, somewhat lower academic functioning and more absence than healthy peers, with differences varying by condition — effect sizes not stated here, check before quoting.",
  "The educational impact is often from the absence itself (missed teaching, disrupted friendships) plus the condition's direct effects (fatigue, pain, medication effects, cognitive effects of some conditions and treatments).",
  "Part D routes: Paediatrics, Primary Care, NEPS for school supports. The medical team leads on the condition; school and EP lead on access to learning and belonging.",
 ],
 "what_it_is_not": [
  "NOT EBSA — although the two can overlap. A child with a real illness may also develop anxiety about returning; a child with anxiety may present with physical symptoms. Medical review first, then psychological formulation.",
  "NOT for the EP to question the medical diagnosis or advise on treatment. Your role is educational access and wellbeing (PSI 2.2.2).",
  "NOT only a physical matter. Children with chronic illness have elevated rates of emotional difficulty — rate not stated here, check — and may face isolation and reduced self-esteem.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: frequent hospital stays can interrupt early learning and preschool friendships; parents' anxiety is high.",
  "SCHOOL AGE 6–12: missed foundational teaching (literacy, number), gaps that compound; peers may not understand the illness.",
  "ADOLESCENT 13–16: exam years; identity and independence (managing own condition); risk of disengagement; treatment adherence can become a conflict area.",
  "YOUNG ADULT 17–26: transition from paediatric to adult health services is a known risk point; college disability services and reasonable accommodations.",
  "SPECIAL SETTING: complex medical needs may require nursing support and care plans; attendance may be limited by health, not choice.",
 ],
 "assess": [
  "ATTENDANCE PATTERN in relation to medical events: hospital admissions, treatment cycles, flares.",
  "LIAISE WITH THE MEDICAL TEAM (with consent): what to expect, fatigue, cognitive effects, any restrictions.",
  "ATTAINMENT CHECK to find gaps from missed teaching; curriculum-based assessment is often more useful than standardised tests.",
  "WELLBEING — mood, anxiety, peer relationships, self-perception (Piers-Harris 3, SDQ).",
 ],
 "recommendations": [
  "INDIVIDUAL HEALTHCARE PLAN with the school, parents and medical team — check current Department of Education guidance on managing medical conditions in schools.",
  "FLEXIBLE ACCESS: work sent home, a named contact, online links where possible, catch-up teaching on return. Home Tuition Scheme may be available on medical grounds — check the current Department of Education scheme and eligibility.",
  "MAINTAIN BELONGING: keep the child connected to classmates during absence (cards, video calls, visits).",
  "STATE EXAMS: consider Reasonable Accommodations at Certificate Examinations (RACE) where the condition affects performance — check SEC criteria.",
  "CONTINUUM LEVEL: School Support; School Support Plus where multiple agencies are involved. DO NOT recommend reduced timetables without medical advice and a review date.",
 ],
 "explain_parent": [
  "'Our job is making sure his illness doesn't close doors to learning or friendships. The hospital team leads on his health; we lead on school.'",
  "'Let's agree how work gets to him when he's out, and how we'll help him catch up when he's back.'",
 ],
 "explain_teacher": [
  "'Her fatigue is real, not motivational. Short tasks and flexible deadlines help.'",
  "'Keep her connected to the class when she's out — it makes coming back much easier.'",
  "'Tell us what she has missed in your subject in a short list — core topics, not every worksheet — so the catch-up is manageable.'",
 ],
 "explain_child": [
  "YOUNGER: 'When you're in hospital, your class still thinks about you. We'll help you catch up when you're back.'",
  "OLDER: 'Your illness is part of your life, not all of it. Let's work out what helps you keep up with school and friends.'",
 ],
 "red_flags": [
  "WATCH — absence exceeding what the medical picture suggests: explore anxiety or EBSA sensitively, with medical input.",
  "WATCH — low mood, isolation, or non-adherence to treatment in adolescence: GP/medical team.",
  "BOUNDARY — do not advise on medication or treatment; refer questions to the medical team.",
 ],
 "questions": [
  "Q: 'Should she do exams?' A: 'That depends on her health and the medical advice. Reasonable accommodations may help — the SEC has a process.'",
  "Q: 'How do we stop him falling behind?' A: 'A plan for work at home, catch-up on return, and keeping him connected socially.'",
  "Q: 'Is it anxiety or is he really sick?' A: 'His medical team is best placed to judge. We can support both — health and any worry about coming back.'",
 ],
 "supervision": [
  "Bring your liaison with medical teams — what information did you need, and how did you obtain consent?",
  "Discuss how you'd respond when a school suspects illness is being used to avoid school.",
 ],
 "citations": [
  "Pinquart, M., & Teubert, D. (2012). Academic, physical, and social functioning of children and adolescents with chronic physical illness: A meta-analysis. Journal of Pediatric Psychology, 37(4), 376–389.",
  "Shaw, S. R., & McCabe, P. C. (2008). Hospital-to-school transition for children with chronic illness: Meeting the new challenges of an evolving health care system. Psychology in the Schools, 45(1), 74–87.",
 ],
})

# ---------------------------------------------------------------- 15
PRES.append({
 "name": "Late arrival and partial attendance",
 "neps": NEPS_36,
 "related_to": ["Separation Anxiety Disorder", "Sleep disorders", "Major Depressive Disorder", "ADHD", "Autism"],
 "what_it_is": [
  "A description of a pupil who is marked present but misses part of the school day: arriving late (often daily), leaving early, missing specific lessons, spending long periods in the office, toilet or base room, or attending a reduced timetable.",
  "It is frequently an EARLY SIGN of an emerging attendance problem. Kearney (2008) describes absenteeism as a continuum from morning difficulties and tardiness through partial absence to full non-attendance — intervening at the tardy end is easier.",
  "Late arrival can hide in the data because the pupil is technically 'present'. Gottfried (2014) found chronic absenteeism associated with lower academic and socioemotional outcomes; the effect of partial absence specifically is less studied — check before quoting.",
  "Part D places it under 3.6. Common drivers: morning anxiety, sleep problems (including adolescent delayed sleep phase — Crowley et al., 2007), caring responsibilities, family routines, avoidance of a particular first lesson, or transport difficulties.",
 ],
 "what_it_is_not": [
  "NOT trivial because the pupil 'gets in eventually'. Missing the first lesson every day adds up across a year, and the arrival itself — into a class already settled — can be socially and emotionally costly.",
  "NOT only a discipline matter. Detention for lateness can deepen avoidance in a pupil whose lateness is anxiety-driven.",
  "NOT the same as a planned reduced timetable. A reduced day agreed as part of a return plan is a support; an informal, open-ended one is an attendance problem — Department of Education guidance on reduced school days (2021, check current version and Tusla notification requirements) applies.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: late arrival usually reflects family routine; frame supportively.",
  "SCHOOL AGE 6–12: lateness is mostly within the parent's control; separation difficulty at the gate, sibling logistics, morning routines, or a first lesson the child dreads.",
  "ADOLESCENT 13–16: delayed sleep phase is common (Crowley et al., 2007); night-time phone use; avoiding first-period subjects or a crowded arrival; hiding in toilets; leaving before a particular lesson.",
  "YOUNG ADULT 17–26: missing morning lectures; partial engagement; work shifts competing.",
  "SPECIAL SETTING: transport timing, medical routines, sensory difficulties at busy arrival times; a quieter staggered entry may help.",
 ],
 "assess": [
  "DATA BY PERIOD, NOT BY DAY: which lessons, which days, how late, how often. Look for patterns (e.g., always Monday, always PE).",
  "MORNING ROUTINE INTERVIEW with parent and pupil: wake time, sleep time, phone use, who does what, where it breaks down.",
  "PUPIL VIEW: 'What's the hardest part of getting to school?' 'What happens when you arrive late?' — the arrival itself may be the feared moment.",
  "SCREEN for anxiety, mood, sleep and caring responsibilities.",
 ],
 "recommendations": [
  "MAKE ARRIVAL EASY: a meet-and-greet at a side door; arrival to a base before class; a job on arrival; no public comment about lateness.",
  "SLEEP: sleep hygiene conversation with parent and young person; GP if persistent sleep difficulty.",
  "TARGET THE SPECIFIC LESSON if avoidance is lesson-specific: find out why (teacher, peers, content, public performance) and adjust.",
  "REDUCED DAYS ONLY AS PART OF A PLAN with a return date, reviewed regularly and notified as required by Department of Education guidance — check current requirements.",
  "CONTINUUM LEVEL: Classroom Support for occasional lateness; School Support for patterns; School Support Plus with Tusla where it forms part of a wider attendance concern.",
 ],
 "explain_parent": [
  "'Coming in late seems small, but it adds up and often it's an early sign that something's getting harder. Let's look at mornings together.'",
  "'Is there a particular point where things get stuck — waking, getting dressed, leaving the house, or at the gate?'",
 ],
 "explain_teacher": [
  "'Please don't comment on his lateness in front of the class. A quiet \"good to see you\" helps him come in rather than stay out.'",
  "'If he's always missing your lesson, that's a clue — not a criticism. Let's work out what's happening.'",
 ],
 "explain_child": [
  "YOUNGER: 'Mornings seem hard. Let's make a picture list of what you do each morning, and see what helps.'",
  "OLDER: 'Coming in late can be because it's hard to sleep, or because walking into a full class is awful, or something else. What's it like for you?'",
 ],
 "red_flags": [
  "WATCH — lateness due to caring responsibilities or chaotic home circumstances: consider welfare needs and Tusla Family Support.",
  "WATCH — lateness progressing to full absence: act early; see the EBSA entry.",
  "RED FLAG — lateness concealing injuries or neglect: Children First; report to Tusla.",
 ],
 "questions": [
  "Q: 'She gets in eventually — why worry?' A: 'Because lateness is often the first step toward bigger attendance problems, and she's missing a lot of learning.'",
  "Q: 'Should we give detentions for lateness?' A: 'If the lateness is driven by anxiety, detention can make it worse. Let's find out why first.'",
  "Q: 'Can we let him start later each day?' A: 'Only as part of a plan with a clear return date and a review. Open-ended reduced days tend to become permanent.'",
 ],
 "supervision": [
  "Bring the period-by-period attendance pattern — what hypotheses did it generate, and how did you test them with the pupil?",
  "Discuss when a reduced timetable is a support and when it becomes part of the problem.",
 ],
 "citations": [
  "Crowley, S. J., Acebo, C., & Carskadon, M. A. (2007). Sleep, circadian rhythms, and delayed phase in adolescence. Sleep Medicine, 8(6), 602–612.",
  "Gottfried, M. A. (2014). Chronic absenteeism and its effects on students' academic and socioemotional outcomes. Journal of Education for Students Placed at Risk, 19(2), 53–75.",
  "Kearney, C. A. (2008). School absenteeism and school refusal behavior in youth: A contemporary review. Clinical Psychology Review, 28(3), 451–471.",
 ],
})

# ---------------------------------------------------------------- 16
PRES.append({
 "name": "Return-to-school planning after extended absence",
 "neps": NEPS_36,
 "related_to": ["Separation Anxiety Disorder", "Social Anxiety Disorder (social phobia)", "Major Depressive Disorder", "Autism", "Acquired brain injury"],
 "what_it_is": [
  "The planned, graded process of bringing a pupil back into school after a long absence — whether from EBSA, illness, exclusion, bereavement, hospitalisation or a family crisis.",
  "The principle, from school-refusal intervention research (Heyne & Rollings, 2002; Kearney, 2008), is graded exposure within a supportive plan: small, agreed steps with increasing time and demand, reinforced, and not reversed without review.",
  "Maynard et al. (2018) meta-analysis found psychosocial interventions for school refusal (largely CBT with exposure) improved attendance relative to comparison conditions, though evidence on anxiety reduction was less clear — effect sizes not stated here, check before quoting.",
  "Part D: at Adolescence, 'graduated return plan' and 'Tusla Educational Welfare involvement'. The EP typically coordinates the plan with the school, family, young person and any clinical service.",
 ],
 "what_it_is_not": [
  "NOT 'come back when you feel ready'. Waiting for anxiety to go away before returning tends to maintain it.",
  "NOT a full-time return on day one for a pupil who has been out for months — this frequently fails and makes the next attempt harder.",
  "NOT an open-ended reduced timetable. Every step needs a date and a review.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: re-entry to preschool after illness or family crisis; a settling-in approach with a key person.",
  "SCHOOL AGE 6–12: parent involvement in the plan is central; a handover routine at the door; building up time and activities.",
  "ADOLESCENT 13–16: the young person's own agreement is essential; subject-by-subject reintroduction; managing peers' questions; exam-year pressures.",
  "YOUNG ADULT 17–26: return to course with disability/access office support; phased workload.",
  "SPECIAL SETTING: transport, staff consistency and sensory adjustments; a visual plan for the return.",
 ],
 "assess": [
  "UNDERSTAND WHY the absence happened and what maintains it now — the return plan must address the maintaining factors, not only the original cause.",
  "BUILD A HIERARCHY with the young person: rate each part of the school day (arrival, lessons, break, lunch) for difficulty; the hierarchy becomes the plan.",
  "IDENTIFY RESOURCES: key adult, safe base, preferred lessons, trusted friends.",
  "CLARIFY OTHER SERVICES: CAMHS, Primary Care, medical team, Tusla — who does what.",
 ],
 "recommendations": [
  "WRITE THE PLAN with specific steps (e.g., Week 1: arrive 9:00, 30 minutes in base with key adult; Week 2: add first lesson...), review dates, and who is responsible.",
  "PREPARE THE ENVIRONMENT: agree what classmates are told; brief teachers; prepare a safe base and exit card.",
  "PLAN FOR SETBACKS: a set-back is expected; agree in advance what happens (return to previous step, not to full absence).",
  "REINFORCE PROGRESS: specific praise; celebrating steps achieved, not only the final goal.",
  "CONTINUUM LEVEL: School Support Plus usually. DO NOT recommend home tuition as a replacement for return unless medically indicated.",
 ],
 "explain_parent": [
  "'We'll plan small steps back, with dates. It'll feel slow, but it's much more likely to stick than trying to go straight back full-time.'",
  "'There will be hard days. We've planned for them — a hard day means going back one step, not stopping.'",
 ],
 "explain_teacher": [
  "'He's coming back gradually. Please welcome him without drawing attention and don't comment on the time he's been away.'",
  "'If he needs to use the exit card, let him, and expect him to come back — that's part of the plan.'",
 ],
 "explain_child": [
  "YOUNGER: 'We're going to come back a little bit at a time. First, you'll come to [base] with [adult]. When that feels okay, we'll add something else.'",
  "OLDER: 'You set the steps with us. The plan moves forward when you've managed a step, and if something's too hard, we adjust — we don't give up.'",
 ],
 "red_flags": [
  "RED FLAG — self-harm, suicidal ideation, or disclosure of harm during the return process: same-day procedure; Children First where relevant.",
  "WATCH — repeated failure at the same step: review the plan and the formulation; consider clinical referral.",
  "WATCH — the plan stalling at a reduced day: set a review date and escalate.",
 ],
 "questions": [
  "Q: 'Why not just full-time straight away?' A: 'After a long absence, a full return usually overwhelms and fails. Small steps build confidence and stick.'",
  "Q: 'What if she has a bad day?' A: 'We've planned for that — go back one step, not back to full absence.'",
  "Q: 'How long will it take?' A: 'It depends on the young person, but the plan has dates and we'll review regularly.'",
 ],
 "supervision": [
  "Bring the draft plan — are the steps small enough, specific enough, and agreed with the young person?",
  "Discuss how you coordinate roles when CAMHS, Tusla and the school are all involved.",
 ],
 "citations": [
  "Heyne, D., & Rollings, S. (2002). School refusal. BPS Blackwell.",
  "Kearney, C. A. (2008). School absenteeism and school refusal behavior in youth: A contemporary review. Clinical Psychology Review, 28(3), 451–471.",
  "Maynard, B. R., Heyne, D., Brendel, K. E., Bulanda, J. J., Thompson, A. M., & Pigott, T. D. (2018). Treatment for school refusal among children and adolescents: A systematic review and meta-analysis. Research on Social Work Practice, 28(1), 56–67.",
 ],
})

# ---------------------------------------------------------------- 17
PRES.append({
 "name": "Pathological Demand Avoidance (PDA) profile",
 "neps": NEPS_41,
 "related_to": ["Autism", "Oppositional Defiant Disorder", "Generalised Anxiety Disorder", "ADHD", "Conduct Disorder"],
 "what_it_is": [
  "A description of a pattern of extreme avoidance of everyday demands and expectations, often using social strategies (distraction, excuses, negotiation, role play, withdrawal into fantasy) and, when pressure increases, meltdown or aggression. Newson et al. (2003) first described 'pathological demand avoidance syndrome' as a distinct pervasive developmental disorder.",
  "PDA is NOT a diagnosis in DSM-5-TR or ICD-11 (Part D: 'Not a DSM diagnosis'). It is used in the UK, and increasingly in Ireland, as a PROFILE description, usually within autism. Some clinicians and many families find it a helpful way of explaining the pattern; others question its validity.",
  "The evidence base is limited and contested. Green et al. (2018) argue PDA describes a set of symptoms seen across conditions, not a separate syndrome; Kildahl et al. (2021) systematic review found the research base small and methodologically limited. The EDA-Q (O'Nions et al., 2014) is a research questionnaire, not a diagnostic tool.",
  "Current thinking frames the avoidance as anxiety-driven and linked to a strong need for control and autonomy. That framing is what makes it useful for school planning, regardless of the diagnostic debate.",
 ],
 "what_it_is_not": [
  "NOT a diagnosis you can make or confirm. Describe the pattern ('an extreme, anxiety-driven avoidance of demands'); do not write 'has PDA'.",
  "NOT the same as oppositional defiance. The PDA description emphasises anxiety and a need for control rather than hostility towards authority, and a better response to indirect, flexible approaches than to firmer boundaries — but the overlap is real and the distinction contested.",
  "NOT a reason to remove all expectations. Approaches recommended in PDA literature reduce and reframe demands; they do not abandon learning or safety.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: refusal of ordinary routines (dressing, eating, toileting) with unusual social strategies to avoid them; intense need to control play.",
  "SCHOOL AGE 6–12: task refusal escalating as demands increase; excuses, distraction, role-play as a way out; meltdowns under pressure; relationships with peers marked by control.",
  "ADOLESCENT 13–16: school avoidance (EBSA) is common; masking at school with explosive release at home; conflict with authority.",
  "YOUNG ADULT 17–26: difficulties with workplace or course expectations; self-employment or high-autonomy roles may suit; adult services.",
  "SPECIAL SETTING: rigid routines can escalate avoidance for this profile; flexible, choice-based approaches may work better — observe carefully.",
 ],
 "assess": [
  "DESCRIBE THE PATTERN: which demands, how the pupil avoids them, what happens as pressure increases, what reduces avoidance.",
  "SEPARATE ACCOUNTS from home and school — PDA descriptions often feature large differences (masking at school, release at home).",
  "SCREEN for autism characteristics (SRS-2, SCQ) and anxiety (RCADS); refer to CDNT for diagnostic assessment if not already assessed.",
  "FUNCTIONAL ASSESSMENT of avoidance: what the avoidance achieves (escape, control, anxiety reduction).",
 ],
 "recommendations": [
  "REDUCE AND REFRAME DEMANDS: indirect language ('I wonder if...', 'Let's see if...'), choices within limits, collaborative problem-solving.",
  "PRIORITISE: agree the few non-negotiables (safety) and flex the rest.",
  "ANXIETY SUPPORT: predictability where helpful, but with flexibility; a trusted adult; a safe space.",
  "CONSISTENCY BETWEEN HOME AND SCHOOL in approach; a shared one-page profile of what helps and what escalates, written with the pupil where possible.",
  "CONTINUUM LEVEL: School Support Plus usually, with CDNT involvement. DO NOT use the PDA label in reports as if it were a diagnosis.",
 ],
 "explain_parent": [
  "'The pattern you're describing — avoiding even ordinary requests, with a lot of anxiety underneath — is sometimes called a PDA profile. It's not a formal diagnosis, but it can help us plan.'",
  "'What often helps is fewer direct demands, more choices, and a calm, flexible approach. That's what we'll try in school.'",
 ],
 "explain_teacher": [
  "'Direct instructions seem to trigger his anxiety. Try indirect language and choices: \"Would you like to start with the maths or the reading?\"'",
  "'Decide on the few things that really matter and be flexible on the rest. Pick your battles.'",
 ],
 "explain_child": [
  "YOUNGER: 'Sometimes when people ask you to do things, it feels really hard. Let's find ways that feel easier.'",
  "OLDER: 'It sounds like being told what to do makes you feel really uncomfortable. That's okay — let's work out together how school can work for you.'",
 ],
 "red_flags": [
  "RED FLAG — aggression causing injury, or self-harm: safety plan and risk procedure.",
  "WATCH — escalating school avoidance: see the EBSA entry.",
  "BOUNDARY — PDA is not a diagnosis. Diagnostic questions go to the CDNT or CAMHS.",
 ],
 "questions": [
  "Q: 'Does she have PDA?' A: 'PDA isn't a formal diagnosis. The pattern you describe is real and I can describe it and plan for it. If there's a question about autism, that's for the CDNT.'",
  "Q: 'Aren't we just giving in to him?' A: 'No — we're reducing the anxiety that drives the avoidance, and keeping the things that really matter.'",
  "Q: 'Is there research?' A: 'There's some, but it's limited and debated. We focus on approaches that make sense for anxiety-driven avoidance.'",
 ],
 "supervision": [
  "Bring the debate — how do you use PDA language with families who value it without implying a diagnosis?",
  "Discuss your formulation: anxiety, autism, ODD, or a mix — and what evidence each hypothesis rests on.",
 ],
 "citations": [
  "Green, J., Absoud, M., Grahame, V., Malik, O., Simonoff, E., Le Couteur, A., & Baird, G. (2018). Pathological demand avoidance: Symptoms but not a syndrome. The Lancet Child & Adolescent Health, 2(6), 455–464.",
  "Kildahl, A. N., Helverschou, S. B., Rysstad, A. L., Wigaard, E., Hellerud, J. M., Ludvigsen, L. B., & Howlin, P. (2021). Pathological demand avoidance in children and adolescents: A systematic review. Autism, 25(8), 2162–2176.",
  "Newson, E., Le Maréchal, K., & David, C. (2003). Pathological demand avoidance syndrome: A necessary distinction within the pervasive developmental disorders. Archives of Disease in Childhood, 88(7), 595–600.",
  "O'Nions, E., Christie, P., Gould, J., Viding, E., & Happé, F. (2014). Development of the 'Extreme Demand Avoidance Questionnaire' (EDA-Q): Preliminary observations on a trait measure for pathological demand avoidance. Journal of Child Psychology and Psychiatry, 55(7), 758–768.",
 ],
})

# ---------------------------------------------------------------- 18
PRES.append({
 "name": "Peer relationship difficulties and social isolation",
 "neps": NEPS_41,
 "related_to": ["Autism", "Social (Pragmatic) Communication Disorder", "ADHD", "Social Anxiety Disorder (social phobia)", "DLD"],
 "what_it_is": [
  "A description of a child or young person who has difficulty making or keeping friends, is rejected or ignored by peers, or is isolated — whether or not they want more social contact.",
  "Parker and Asher (1987) reviewed longitudinal evidence that low peer acceptance predicts later difficulties including early school leaving and criminality; the link to later mental health is also documented but varies by study.",
  "Sociometric research distinguishes REJECTED children (actively disliked) from NEGLECTED children (overlooked) — Coie et al. (1982). Rejection is more predictive of later difficulty; neglect is often more transient.",
  "Part D lists it under 4.1 as 'Not a DSM diagnosis'. Routes: NEPS for school supports, NEPS with SLT, CDNT, whole-school policy support. Part D at School Age: yard and classroom observation, SRS-2, sociometric mapping, friendship interview.",
 ],
 "what_it_is_not": [
  "NOT the same as preferring solitude. Some children are content with few interactions; the concern is distress or exclusion.",
  "NOT only the child's 'social skills'. Peer group dynamics, class culture and adult structures shape who is included. Interventions that work only on the child's skills have more limited effects than those that also involve peers.",
  "NOT a diagnosis. Social difficulty is common across autism, ADHD, DLD and anxiety — describe it without implying one.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: difficulty joining play, turn-taking, reading others' cues; the adult's role in scaffolding play is large.",
  "SCHOOL AGE 6–12: not picked for teams, alone at yard, not invited to parties; rejection becomes stable across years.",
  "ADOLESCENT 13–16: friendship groups become more complex and online; exclusion, relational aggression; social demands of post-primary are different (Part D) — assess those.",
  "YOUNG ADULT 17–26: isolation in college or work; loneliness and mental health.",
  "SPECIAL SETTING: peer group may be small; opportunities for integration and shared activity matter (Part D).",
 ],
 "assess": [
  "YARD AND CLASSROOM OBSERVATION: approaches, responses, positions, who plays with whom.",
  "SOCIOMETRIC MAPPING (class-level, handled sensitively and ethically; many schools prefer less intrusive approaches — check local policy).",
  "SRS-2 parent and teacher (Part D names this as a named development area); SDQ peer problems scale.",
  "FRIENDSHIP INTERVIEW with the pupil: 'Who do you play with? Who would you like to? What happens when you try?'",
 ],
 "recommendations": [
  "PEER-MEDIATED APPROACHES: Circle of Friends (Frederickson & Turner, 2003); buddy systems; structured cooperative learning.",
  "STRUCTURED BREAK OPTIONS: lunchtime clubs, games, library; roles that bring the child into contact with peers.",
  "TEACH SPECIFIC SKILLS in context if needed (joining, turn-taking, repair) — practised in real settings with peer support.",
  "CLASS CULTURE: seating, grouping and teacher modelling of inclusion.",
  "CONTINUUM LEVEL: Classroom Support to School Support; School Support Plus with CDNT or SLT involvement.",
 ],
 "explain_parent": [
  "'He wants friends, but at the moment his attempts to join in aren't working. We'll work on it with him and with the other children.'",
  "'Friendships depend on the group too, not only on him. We'll look at both.'",
 ],
 "explain_teacher": [
  "'Where you seat her and who you group her with makes a big difference. A structured task with one kind peer is a good start.'",
  "'Watch the first minutes of yard — does she approach and get rejected, or not approach at all?'",
 ],
 "explain_child": [
  "YOUNGER: 'Making friends can be tricky. Let's find some games you like and someone to play them with.'",
  "OLDER: 'Some people find friendships easier than others. What's going on for you? What would you like to be different?'",
 ],
 "red_flags": [
  "RED FLAG — isolation with low mood, self-harm or suicidal ideation: same-day procedure.",
  "WATCH — isolation caused by bullying: school anti-bullying procedure.",
  "WATCH — vulnerability to exploitation by peers or adults offering friendship: safeguarding.",
 ],
 "questions": [
  "Q: 'Can you teach him social skills?' A: 'We can, but it works best alongside changes in the peer group and class. It's not all on him.'",
  "Q: 'Is it autism?' A: 'Social difficulty can be part of autism, but also other things. If there's a wider question, the CDNT is the route.'",
  "Q: 'Should we force her to join in?' A: 'Structured chances with support work better than pushing.'",
 ],
 "supervision": [
  "Bring your observation — rejected or neglected (Coie et al., 1982)? What evidence, and what would a second observation need to show to change your view?",
  "Discuss the ethics of sociometric methods in a class: consent, how results are stored, and the risk that naming exercises harm the child you are trying to help.",
 ],
 "citations": [
  "Coie, J. D., Dodge, K. A., & Coppotelli, H. (1982). Dimensions and types of social status: A cross-age perspective. Developmental Psychology, 18(4), 557–570.",
  "Frederickson, N., & Turner, J. (2003). Utilizing the classroom peer group to address children's social needs: An evaluation of the Circle of Friends intervention approach. The Journal of Special Education, 36(4), 234–245.",
  "Parker, J. G., & Asher, S. R. (1987). Peer relations and later personal adjustment: Are low-accepted children at risk? Psychological Bulletin, 102(3), 357–389.",
 ],
})

# ---------------------------------------------------------------- 19
PRES.append({
 "name": "Bullying",
 "neps": NEPS_41,
 "related_to": ["Social Anxiety Disorder (social phobia)", "Major Depressive Disorder", "Autism", "Posttraumatic Stress Disorder", "ADHD"],
 "what_it_is": [
  "Olweus (1993) defined bullying as repeated negative actions by one or more people towards another, where there is an imbalance of power. The Irish definition in Bí Cineálta (Department of Education, 2024 — check current version) describes bullying as targeted behaviour, online or offline, that causes harm, repeated over time, involving an imbalance of power; check the exact wording before quoting.",
  "Forms: physical, verbal, relational (exclusion, rumours), and online (cyberbullying). Identity-based bullying (homophobic, transphobic, racist, disablist) is named specifically in Irish guidance.",
  "Salmivalli (2010) shows bullying is a group process: bystanders, assistants, reinforcers and defenders shape whether it continues. Interventions that target the peer group are more effective than those that target only the individual.",
  "Part D lists bullying under 4.1 as 'Not a DSM diagnosis'. Route: whole-school policy support. Irish schools must have an anti-bullying policy; Bí Cineálta procedures replaced the Anti-Bullying Procedures (2013) — check implementation timeline.",
 ],
 "what_it_is_not": [
  "NOT the same as a single conflict or falling-out between equals. Repetition and power imbalance are the key features (though a single serious incident may still need action under the school's procedures).",
  "NOT 'just part of growing up'. Bullying is associated with lasting mental health effects for victims — Arseneault et al. (2010) reviewed the evidence.",
  "NOT only about the victim's vulnerability. Characteristics of the victim should never be used to explain away the behaviour of those doing the bullying.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: repeated exclusion or aggression in play; adults frame as behaviour to manage rather than 'bullying' at this age.",
  "SCHOOL AGE 6–12: name-calling, exclusion, physical bullying; online bullying emerges with phone ownership.",
  "ADOLESCENT 13–16: relational and online bullying peak; identity-based bullying; image-based abuse is a crime under the Harassment, Harmful Communications and Related Offences Act 2020 (Coco's Law).",
  "YOUNG ADULT 17–26: workplace and college bullying; adult policies apply.",
  "SPECIAL SETTING: pupils with SEN are at higher risk of being bullied — rate not stated here, check before quoting; communication difficulties may prevent reporting.",
 ],
 "assess": [
  "LISTEN to the child's account; record factually; follow the school's anti-bullying procedure.",
  "SCREEN the impact: mood, anxiety, attendance, sleep, self-harm.",
  "CONSULT with the school on the group dynamics (Salmivalli, 2010): who is involved, who is watching, who could defend.",
  "CHECK THE SCHOOL POLICY is being implemented, and consider the whole-school climate.",
 ],
 "recommendations": [
  "FOLLOW THE SCHOOL'S ANTI-BULLYING PROCEDURES (Bí Cineálta) — the EP role is consultation, not investigation.",
  "WHOLE-SCHOOL APPROACHES are more effective than individual ones (Gaffney et al., 2019; Ttofi & Farrington, 2011).",
  "SUPPORT FOR THE TARGET: key adult, safe spaces, peer support; monitor impact on mood and attendance.",
  "WORK WITH THOSE DOING THE BULLYING: understand their needs; restorative approaches where appropriate.",
  "CONTINUUM LEVEL: Classroom Support to School Support; whole-school policy support at systemic level.",
 ],
 "explain_parent": [
  "'What your child has told us is serious and we're taking it seriously. The school has a procedure and it will be followed.'",
  "'We'll also keep an eye on how she's feeling — her mood, sleep, and wanting to come to school.'",
 ],
 "explain_teacher": [
  "'Bullying is a group process. Bystanders who step in or tell an adult make the biggest difference.'",
  "'Record what you see factually, and follow the school procedure. Don't try to resolve it with a quick handshake.'",
 ],
 "explain_child": [
  "YOUNGER: 'Thank you for telling me. It's not your fault. We're going to help make it stop.'",
  "OLDER: 'What's been happening isn't okay and it's not because of anything wrong with you. Let's talk about what you'd like to happen next.'",
 ],
 "red_flags": [
  "RED FLAG — self-harm or suicidal ideation linked to bullying: same-day procedure.",
  "RED FLAG — sexual harassment, image-based abuse, or bullying involving adults: Children First; report to Tusla; Gardaí as appropriate.",
  "WATCH — school avoidance following bullying: see the EBSA entry.",
 ],
 "questions": [
  "Q: 'Isn't it just kids being kids?' A: 'No. Repeated targeting with a power imbalance is bullying, and it can affect children for years.'",
  "Q: 'Should she just ignore it?' A: 'That puts the burden on her. Adults need to act.'",
  "Q: 'What will happen to the other child?' A: 'The school will follow its procedure. We'll also look at what's going on for them.'",
 ],
 "supervision": [
  "Bring a case where you felt pulled into investigating — where's the line between consultation and investigation?",
  "Discuss how to support the school's systemic response under Bí Cineálta without taking over the school's own responsibility.",
 ],
 "citations": [
  "Arseneault, L., Bowes, L., & Shakoor, S. (2010). Bullying victimization in youths and mental health problems: 'Much ado about nothing'? Psychological Medicine, 40(5), 717–729.",
  "Department of Education. (2024). Bí Cineálta: Procedures to prevent and address bullying behaviour for primary and post-primary schools. Government of Ireland.",
  "Gaffney, H., Ttofi, M. M., & Farrington, D. P. (2019). Evaluating the effectiveness of school-bullying prevention programs: An updated meta-analytical review. Aggression and Violent Behavior, 45, 111–133.",
  "Olweus, D. (1993). Bullying at school: What we know and what we can do. Blackwell.",
  "Salmivalli, C. (2010). Bullying and the peer group: A review. Aggression and Violent Behavior, 15(2), 112–120.",
 ],
})

# ---------------------------------------------------------------- 20
PRES.append({
 "name": "Social adaptive skills",
 "neps": NEPS_41,
 "related_to": ["Intellectual Disability", "Autism", "Global Developmental Delay", "Social (Pragmatic) Communication Disorder", "Genetic syndromes"],
 "what_it_is": [
  "The everyday social skills a person uses to get along with others and function in social settings — interpersonal relationships, play and leisure, coping, following social rules, and responsibility. They form one of the three domains of adaptive behaviour (conceptual, social, practical) in the AAIDD framework (Schalock et al., 2021) and in DSM-5-TR.",
  "Adaptive behaviour is what a person TYPICALLY does, not what they CAN do under ideal conditions. A pupil who can describe how to greet someone in a test setting may not do it spontaneously in the yard.",
  "Social adaptive skills are measured with standardised rating scales — Vineland-3 (Sparrow et al., 2016) and ABAS-3 (Harrison & Oakland, 2015) — completed by parents, teachers or through interview. Both are in the tool catalogue.",
  "Part D lists it under 4.1 as 'Not a DSM diagnosis'. It is essential to the assessment of intellectual disability (adaptive deficits are a diagnostic requirement) and to planning in special settings.",
 ],
 "what_it_is_not": [
  "NOT the same as social skills knowledge. Adaptive behaviour is about typical performance in real life; low scores may reflect lack of opportunity, not lack of ability.",
  "NOT a diagnosis. A low social adaptive score describes current functioning; it supports but does not make a diagnosis of ID or autism.",
  "NOT fixed. Adaptive skills can be taught, and scores change with intervention and opportunity.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: responding to others, sharing, simple play rules; Vineland-3 and ABAS-3 have early-childhood forms.",
  "SCHOOL AGE 6–12: friendships, following class and yard rules, managing conflict, coping with change.",
  "ADOLESCENT 13–16: more complex social rules; independence; online social behaviour.",
  "YOUNG ADULT 17–26: work, community, relationships — ABAS-3 adult form, Vineland-3 adult.",
  "SPECIAL SETTING: adaptive measures often replace IQ as the central measure; planning is built on them (Part D: adaptive measure in place of IQ).",
 ],
 "assess": [
  "Vineland-3 or ABAS-3 social domain from at least two informants (home and school). Differences between raters are data about setting demands and opportunity.",
  "OBSERVATION of social behaviour in natural settings — yard, lunch, group work.",
  "PUPIL AND PARENT INTERVIEW on social routines, independence and opportunities.",
  "INTERPRET in the context of cognitive ability, language, culture and opportunity — check the manual for score interpretation rules.",
 ],
 "recommendations": [
  "TEACH SPECIFIC SKILLS in real settings: greeting, joining, asking for help, turn-taking — with visual supports and practice.",
  "CREATE OPPORTUNITIES: structured peer activities, roles, clubs.",
  "GENERALISE: coordinate targets between home and school.",
  "LINK TO PLANNING: set one or two specific adaptive targets in the Student Support Plan (e.g., asks a peer to join a game at yard twice a week) and review them each term.",
  "CONSIDER SLT input where pragmatic language underlies the difficulty (Part D: NEPS with SLT).",
  "CONTINUUM LEVEL: School Support to School Support Plus; CDNT involvement for children with disabilities.",
 ],
 "explain_parent": [
  "'Adaptive skills are the everyday things we do to get along with people. We looked at what she usually does, not only what she knows.'",
  "'These skills can be taught and practised. Let's pick a couple to work on together at home and in school.'",
 ],
 "explain_teacher": [
  "'He may know the rule but not use it without support. Practise it in the yard, not only in a lesson.'",
  "'Your rating and the parent's may differ — that tells us about different settings, not that one is wrong.'",
 ],
 "explain_child": [
  "YOUNGER: 'We're going to practise saying hello and asking to join a game.'",
  "OLDER: 'Some social things are tricky for everyone. Let's pick one you'd like to get better at.'",
  "ASK: 'Which social situations feel easy, and which feel hard?' — use the answer to choose the first target.",
 ],
 "red_flags": [
  "WATCH — regression in adaptive skills: GP/paediatric review.",
  "WATCH — social naivety increasing vulnerability to exploitation: safeguarding.",
  "BOUNDARY — adaptive scores contribute to but do not make diagnoses; ID and autism are diagnosed by the CDNT or appropriate service.",
 ],
 "questions": [
  "Q: 'Why do you need a questionnaire about what he does every day?' A: 'Because what he does every day matters more for planning than what he can do in a test.'",
  "Q: 'Her scores are different at home and school — which is right?' A: 'Both. They tell us about different demands and supports.'",
  "Q: 'Can adaptive skills improve?' A: 'Yes, with teaching, practice and opportunity.'",
 ],
 "supervision": [
  "Bring an adaptive profile — how did you interpret differences between home and school raters, and what did they say about setting demands?",
  "Discuss how to distinguish a skill deficit from an opportunity or performance deficit, and how that changes the recommendation.",
 ],
 "citations": [
  "Harrison, P. L., & Oakland, T. (2015). Adaptive Behavior Assessment System (3rd ed.). Western Psychological Services.",
  "Schalock, R. L., Luckasson, R., & Tassé, M. J. (2021). Intellectual disability: Definition, diagnosis, classification, and systems of supports (12th ed.). American Association on Intellectual and Developmental Disabilities.",
  "Sparrow, S. S., Cicchetti, D. V., & Saulnier, C. A. (2016). Vineland Adaptive Behavior Scales (3rd ed.). Pearson.",
 ],
})
