# PRES batch 4 — descriptive (non-diagnostic) presentations.
# Context: Reference Part D, column N.
#   Items 1–5   sit under 2. BEHAVIOUR (2.2 Behaviour during break times and around the school)
#   Items 6–12  sit under 3. EMOTIONAL (3.1 Confidence and self-esteem) — Part D: "0 dx", referred to NEPS
#   Items 13–18 sit under 3. EMOTIONAL (3.2 Anxiety)
#   Items 19–20 sit under 3. EMOTIONAL (3.3 Obsessive-compulsive and related)
# at every UCD Table 3 band. Part D routes: 2.2 → NEPS | CAMHS | Addiction services | Tusla;
# 3.1 → NEPS; 3.2 → Primary Care (mild–mod) | CAMHS (severe) | NEPS | GP to rule out;
# 3.3 → Primary Care | CAMHS (severe) | NEPS.

NEPS_22 = "2. BEHAVIOUR (2.2 Behaviour during break times and around the school)"
NEPS_31 = "3. EMOTIONAL (3.1 Confidence and self-esteem)"
NEPS_32 = "3. EMOTIONAL (3.2 Anxiety)"
NEPS_33 = "3. EMOTIONAL (3.3 Obsessive-compulsive and related)"

PRES = []

# ---------------------------------------------------------------- 1
PRES.append({
 "name": "Adolescent substance misuse / dual diagnosis",
 "neps": NEPS_22,
 "related_to": ["Substance use disorders (alcohol, cannabis, opioid, stimulant, tobacco, inhalant, sedative, hallucinogen)", "Conduct Disorder", "ADHD", "Major Depressive Disorder", "Post-Traumatic Stress Disorder", "Gambling Disorder"],
 "what_it_is": [
  "A description of a young person's use of alcohol, cannabis, nicotine/vapes or other drugs that is affecting school, relationships, safety or health. Part D lists it as 'Not a standalone diagnosis' — a Substance Use Disorder is diagnosed by CAMHS or addiction services, never by the EP.",
  "'DUAL DIAGNOSIS' means a mental health difficulty and a substance use difficulty occurring together. Each tends to worsen the other, and young people often fall between mental health and addiction services — which is why it is named separately.",
  "Hawkins, Catalano and Miller (1992) set out the risk and protective factors framework still used in prevention: early conduct problems, school failure, low commitment to school, peer use and family conflict raise risk; attachment to school and a warm adult lower it. Several of these are things a school can move.",
  "For the EP the question is rarely 'is this addiction?' It is: what is the use DOING for this young person (coping, belonging, sleep, numbing), what is it costing in school, and is anyone at risk right now?",
 ],
 "what_it_is_not": [
  "NOT NEPS work to screen, assess or treat. Part D (Adolescent, 2.2): 'substance screening is not NEPS work — refer.' Your role is to notice, describe school impact, hold the safeguarding line and connect the family to the right service.",
  "NOT simply a behaviour problem to be handled by the code of behaviour. Suspension alone can remove the one protective factor (attachment to school) the young person still has; the evidence on school connectedness points the other way.",
  "NOT confidential between you and the student when there is risk. Use by a child is a welfare matter; significant harm triggers Children First (DCYA, 2017) and the Tusla route regardless of what was promised.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: not a presentation of the child. What you may see is the impact of a PARENT's substance use — neglect indicators, missed appointments, chaotic drop-off. That is a child protection matter (Children First; Tusla), not this presentation.",
  "SCHOOL AGE 6–12: use by the child is rare and is ALWAYS a welfare concern — ask who supplied it and who is supervising. Older siblings, exploitation and access at home are the usual routes. Tusla consultation, same day.",
  "ADOLESCENT 13–16: the core band. Watch for a drop in attendance, a new peer group, lateness after lunch, sleep in class, money problems, and grades that fall across all subjects at once rather than one.",
  "YOUNG ADULT 17–26: usually adult addiction or mental health services; in further education, the EP's role is signposting and supporting course retention. Part D: 'Not typically a NEPS referral at this band.'",
  "SPECIAL SETTING: young people with intellectual disability or autism may be targeted or exploited to carry or use substances; treat any indication as a safeguarding concern first.",
 ],
 "assess": [
  "Gather the SCHOOL picture, not a drug history: attendance pattern by day and period, incident record, year-head notes, change in attainment across subjects, who the young person is with at break (Part D: corridor and break observation where possible · pupil interview · school incident record).",
  "Pupil interview using a motivational interviewing stance (Miller & Rollnick, 2013): curiosity, not interrogation. 'What does it do for you? What does it cost you?' The young person's own account of the function is the most useful formulation data.",
  "Screen for what sits underneath: low mood, trauma, anxiety, ADHD, an unidentified learning need. RCADS self-report or MFQ can describe mood; they do not assess substance use.",
  "Establish RISK before anything else: self-harm, suicidal ideation, overdose, driving, exploitation, debt to dealers, sexual risk. Any one of these moves you to the same-day route.",
 ],
 "recommendations": [
  "RISK FIRST: where there is immediate risk — overdose, suicidal ideation, exploitation, abuse — the same-day risk / child protection route applies. Report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's own duty (Children First Act 2015). Supervision follows the action; it does not replace it.",
  "REFER through the family to the GP and to local HSE youth drug and alcohol / adolescent addiction services; for a co-occurring mental health difficulty, CAMHS. Service names and thresholds vary by CHO area — check locally before naming one in a report.",
  "KEEP THE YOUNG PERSON IN SCHOOL: recommend the school weighs any sanction against the protective value of attendance and a trusted adult. A named key adult and a regular brief check-in are School Support Plus-level actions.",
  "ADDRESS THE FUNCTION: if use is managing anxiety, sleep or low mood, recommend that the underlying need is supported in school (counselling, SPHE, student support team) while the specialist service works on the use.",
  "CONTINUUM LEVEL: School Support Plus — outside agencies involved, a coordinated plan held by the student support team, with parents.",
  "DO NOT give advice on medication or withdrawal, and do not agree to 'keep it between us'. DO NOT recommend drug-testing in school — that is outside the EP role and outside NEPS work.",
 ],
 "explain_parent": [
  "'What we're seeing in school — the missed afternoons, the tiredness, the grades dropping everywhere at once — fits with what you've told me about the cannabis. I'm not the person who assesses the drug use itself, but I can help you get to the service that does.'",
  "'Often the drug is doing a job for a young person — helping them sleep, or switching off worry. The service will look at both, and school will look at what's making the day hard.'",
  "SIGNPOST: GP; local HSE youth drug and alcohol service; Local or Regional Drug and Alcohol Task Force for family supports; CAMHS if mood or risk is a concern. Check current local names before giving them.",
 ],
 "explain_teacher": [
  "'Sanctions on their own tend to push him further out of school, which removes the thing that protects him most. A named adult he checks in with each morning will do more.'",
  "'Don't try to assess the drug use — pass on what you see (dates, times, who with) to the DLP and the year head. Your observation is evidence; your judgement about \"how much\" isn't needed.'",
  "'If he tells you something about risk, you can't promise to keep it secret. Tell him that before he goes further, if you can.'",
 ],
 "explain_child": [
  "OLDER (the only relevant band): 'I'm not here to catch you out or to test you. I'm interested in what it does for you and what it's costing you in school.'",
  "'If you tell me something that means you or someone else isn't safe, I can't keep that to myself — I'd tell you first what I was going to do.'",
  "ASK: 'On a scale of 0 to 10, how much is this getting in the way of the things you want?' The answer tells you whether there is readiness to talk to a service.",
 ],
 "red_flags": [
  "RED FLAG — overdose, loss of consciousness, drug use combined with suicidal talk or self-harm: emergency or same-day route; do not wait for a scheduled meeting.",
  "RED FLAG — signs of criminal or sexual exploitation (unexplained money, older 'friends', carrying for others, going missing): child protection route to Tusla; Gardaí where there is immediate danger.",
  "RED FLAG — a child under 13 using substances, or a parent's use leaving a child unsupervised or unsafe: Tusla, as soon as practicable.",
  "BOUNDARY — no drug screening, no diagnosis of substance use disorder, no medication or withdrawal advice (PSI 2.2.2). Describe, refer, safeguard.",
 ],
 "questions": [
  "Q: 'Should we suspend him?' A: 'That's a decision for the school under its code of behaviour. From a psychological view, staying connected to school is one of the strongest protective factors we know of (Hawkins et al., 1992). If there is a sanction, plan the return and the key adult at the same time.'",
  "Q: 'Is it just cannabis — isn't that harmless?' A: 'Heavy adolescent use is linked with poorer school outcomes and mental health risks (Hall & Degenhardt, 2009). I'm not the person to assess how much harm it's doing him — the youth service is.'",
  "Q: 'Can you not just talk to him about it?' A: 'I can help him think about what it's doing for him, and help school support what's underneath. The drug use itself needs a specialist service, and I'll help get him there.'",
  "Q: 'Do we have to tell his parents?' A: 'For a child, yes as a rule — unless telling them would put him at greater risk, in which case that is itself a Tusla matter. Talk to the DLP today.'",
 ],
 "supervision": [
  "Bring any case where you are unsure whether the threshold for a Tusla report is met — after you have taken the immediate action, not instead of it.",
  "Ask what the local referral routes actually are in your area (youth drug and alcohol service, Drug and Alcohol Task Force family supports, CAMHS thresholds for dual diagnosis) and how long they take.",
  "Reflect on your own assumptions about drug use and class, and whether they shaped how you read the young person.",
 ],
 "citations": [
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government Publications.",
  "Department of Health. (2017). Reducing harm, supporting recovery: A health-led response to drug and alcohol use in Ireland 2017–2025. Department of Health.",
  "Hall, W., & Degenhardt, L. (2009). Adverse health effects of non-medical cannabis use. The Lancet, 374(9698), 1383–1391.",
  "Hawkins, J. D., Catalano, R. F., & Miller, J. Y. (1992). Risk and protective factors for alcohol and other drug problems in adolescence and early adulthood: Implications for substance abuse prevention. Psychological Bulletin, 112(1), 64–105.",
  "Miller, W. R., & Rollnick, S. (2013). Motivational interviewing: Helping people change (3rd ed.). Guilford Press.",
 ],
})

# ---------------------------------------------------------------- 2
PRES.append({
 "name": "Unstructured time",
 "neps": NEPS_22,
 "related_to": ["ADHD", "Autism", "Developmental Coordination Disorder (dyspraxia)", "Developmental Language Disorder (DLD)", "Social Anxiety Disorder (social phobia)", "Conduct Disorder"],
 "what_it_is": [
  "A pupil who copes in the structured classroom but whose difficulties cluster in UNSTRUCTURED time — yard, lunch, corridors, lining up, changing rooms, the bus queue. Part D names it 'Unstructured time — yard and corridor as the difficulty'.",
  "The difficulty sits in the INTERACTION between the child and the demands of that time: no adult direction, fluid rules, noise and space, fast-moving peer negotiation, and less supervision. Blatchford (1998) showed breaktime is where much of children's social life — and conflict — happens.",
  "The key finding is the CONTRAST: Part D (School Age, 2.2) — 'compare classroom vs yard — the difference is the finding.' A child who is fine at 10:45 and in trouble at 11:05 is telling you about the setting, not only about themselves.",
  "Often the first place a social communication difficulty, a motor difficulty or anxiety shows, because the classroom scaffolds had been hiding it.",
 ],
 "what_it_is_not": [
  "NOT evidence that the child is 'fine really and just choosing to misbehave at break'. The classroom supplies structure the child may rely on; its absence is the variable.",
  "NOT solved by removing yard time. Keeping a child in removes exercise, peer contact and the chance to learn the skills; Baines and Blatchford (2019) report breaktimes have already been shortened in many schools — check your school's current times before assuming.",
  "NOT automatically bullying — but check. Unstructured time is where bullying most often happens (Olweus, 1993), and a child reacting to provocation can look like the aggressor.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: free play and outdoor time in preschool. Snatching, running off and difficulty joining play are developmentally common — Part D: 'describe rather than classify'.",
  "SCHOOL AGE 6–12: the peak referral band. Games with shifting rules (tag, football), lining up, and the return to class after yard are the hot spots. Watch the first five minutes back in the room.",
  "ADOLESCENT 13–16: corridors between classes, lunch, the canteen, toilets and the walk to and from school. More movement, less supervision, larger peer groups and online spill-over.",
  "YOUNG ADULT 17–26: canteen, common rooms and gaps in a college timetable; isolation is more common than conflict. Rarely a NEPS referral at this band.",
  "SPECIAL SETTING: Part D — 'Break-time structure in the setting · supported vs unsupported time · staffing at transitions.' Compare the child in supported versus unsupported time.",
 ],
 "assess": [
  "Yard observation with event or frequency recording (Part D, School Age): what happens, where, with whom, how long into break, and what the adult on duty did. Observe more than one break — Monday and Friday differ.",
  "A simple map of the yard or corridor with incidents plotted on it. Clusters by location (behind the shed, the stairwell) or by time point to setting changes.",
  "Pupil interview with a map: 'Show me where break is good. Show me where it goes wrong.' Friendship mapping or a sociogram at School Age (Part D).",
  "SDQ peer problems subscale (teacher and parent) for the social picture; incident log analysed by time of day and period.",
  "Check for an unmet need the yard exposes: social communication (autism assessment route), motor skill in games (DCD route), language for negotiating rules (DLD), or anxiety.",
 ],
 "recommendations": [
  "ADD STRUCTURE TO THE TIME, NOT THE CHILD: structured games or a games leader for part of break, a choice of a quieter zone (library, club, garden), a clear 'start and end' routine for yard.",
  "PRE-CORRECTION AND ACTIVE SUPERVISION: a brief rule reminder before going out, and supervising adults who move, scan and interact. Lewis, Colvin and Sugai (2000) found pre-correction plus active supervision reduced problem behaviour at recess.",
  "PLANNED TRANSITION BACK: a calm-down routine or a job on the way back into class; a key adult who meets the pupil at the door after lunch.",
  "SKILL-TEACHING WHERE THE GAP IS: teach the specific game rules, joining-in phrases or conflict scripts in a quiet moment, then practise them with adult support in the yard.",
  "CONTINUUM LEVEL: Classroom Support / School Support for most; School Support Plus if incidents involve injury or outside agencies. Put the break-time plan in the Student Support File, including who is on duty.",
  "DO NOT recommend loss of yard as a standing sanction; if a quiet alternative is offered, it is a CHOICE with a planned return, reviewed after 4–6 weeks.",
 ],
 "explain_parent": [
  "'In class, the teacher is running the show and he knows what's expected. At break the rules change every few minutes, and that's where he struggles. It's the setting, not a sign he's a bad child.'",
  "'We're going to add some structure to his break rather than take break away. He needs the run-around and the practice with other children.'",
 ],
 "explain_teacher": [
  "'Look at the incident log by time — nearly everything is at lunch or straight after. That tells us where to put the support.'",
  "'He doesn't know how to join a game that's already started. Teaching him one phrase and having the yard adult help him use it is worth more than another sanction.'",
  "'The five minutes after yard are when it spills over. A job to do on the way in gives him a landing strip.'",
 ],
 "explain_child": [
  "YOUNGER: 'Some children find the yard tricky because the games keep changing. Let's make a plan for what you can do at break.'",
  "OLDER: 'Loads of people find the corridors and lunch harder than class — no one's telling you what to do and it's loud. Where's the easiest place for you to be?'",
  "ASK: 'If break was perfect, what would you be doing, and who with?'",
 ],
 "red_flags": [
  "RED FLAG — injury, a pattern of being targeted, or a child who is afraid to go out: anti-bullying procedures (Bí Cineálta, Department of Education, 2024 — check for updates) and, where harm is significant, child protection.",
  "WATCH — a child who is always alone and says they prefer it may be content, or may be isolated and low. Ask; do not assume either.",
  "WATCH — sudden change in yard behaviour: ask what changed at home, online or in the peer group.",
 ],
 "questions": [
  "Q: 'He's fine in class — why is he like this at yard?' A: 'Class gives him structure he relies on. Yard takes it away. The difference between the two is actually the most useful thing we know about him.'",
  "Q: 'Can he not just stay in at lunch?' A: 'As a choice with a plan, sometimes yes. As a punishment, it removes the exercise and the practice he needs, and the problem is still there next week.'",
  "Q: 'Is it bullying?' A: 'Sometimes. Unstructured times are where most bullying happens, so we'll check who's involved before deciding who started it.'",
 ],
 "supervision": [
  "Bring your yard observation data and discuss whether you are formulating the child or the setting — and whether your recommendations reflect that.",
  "Discuss how to raise supervision arrangements with a principal without it landing as criticism of staff.",
 ],
 "citations": [
  "Baines, E., & Blatchford, P. (2019). School break and lunch times and young people's social lives: A follow-up national study. Final report. UCL Institute of Education / Nuffield Foundation.",
  "Blatchford, P. (1998). Social life in school: Pupils' experiences of breaktime and recess from 7 to 16 years. Falmer Press.",
  "Lewis, T. J., Colvin, G., & Sugai, G. (2000). The effects of pre-correction and active supervision on the recess behavior of elementary students. Education and Treatment of Children, 23(2), 109–121.",
  "Olweus, D. (1993). Bullying at school: What we know and what we can do. Blackwell.",
  "Department of Education. (2024). Bí Cineálta: Procedures to prevent and address bullying behaviour for primary and post-primary schools. Department of Education. (Check for updates.)",
 ],
})

# ---------------------------------------------------------------- 3
PRES.append({
 "name": "Supervision ratio and yard layout",
 "neps": NEPS_22,
 "related_to": ["ADHD", "Autism", "Conduct Disorder", "Oppositional Defiant Disorder", "Developmental Coordination Disorder (dyspraxia)"],
 "what_it_is": [
  "A SYSTEMIC presentation: the difficulty is located in how break time is staffed and how the physical space is laid out, rather than in one pupil. Part D lists it under 2.2 so that the EP asks the question before formulating a child.",
  "Covers: how many adults are on duty and where they stand; blind spots (behind buildings, toilets, bike shed, stairwells); crowding at pinch points (doors, the tuck shop, the one football pitch); whether zones exist for different activities; and how pupils line up and return.",
  "Colvin, Sugai, Good and Lee (1997) showed ACTIVE supervision (moving, scanning, interacting) and pre-correction reduced problem behaviour at transitions — how adults supervise matters, not only how many there are.",
  "It often explains why several unrelated referrals from one school all mention lunchtime.",
 ],
 "what_it_is_not": [
  "NOT a criticism of the staff on duty. Supervision is usually a rota squeezed between other duties; the EP's job is to help the school see the pattern, not to allocate blame.",
  "NOT a matter with a single 'correct' ratio. No national yard supervision ratio is stated here — schools set supervision under their own policy and Board of Management arrangements. Check the school's policy rather than quoting a figure.",
  "NOT a replacement for looking at the individual child. A systemic fix may resolve most incidents; a pupil who still struggles in a well-supervised yard needs their own formulation.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: preschool ratios are set by regulation for the setting as a whole (check current Tusla early years regulations before quoting); outdoor layout — bikes crossing the sandpit — matters as much as numbers.",
  "SCHOOL AGE 6–12: infants and senior classes sharing one yard; a single football pitch; lining up at one door. Staggered breaks and zoned yards are the common changes.",
  "ADOLESCENT 13–16: corridors, stairwells, locker areas and off-site lunch. Supervision is thinner and movement constant; toilets and the space between buildings are typical blind spots.",
  "YOUNG ADULT 17–26: supervision is not the model; the issue becomes access to quiet spaces and social hubs. Rarely a NEPS question.",
  "SPECIAL SETTING: Part D — 'supported vs unsupported time · staffing at transitions'. SNA deployment at break (often when SNAs take their own breaks) is frequently the gap.",
 ],
 "assess": [
  "Walk the yard WITH a staff member during break and after it. Sketch the layout: entrances, zones, where adults stand, where incidents cluster.",
  "Plot the school's incident log onto the map by location and time. Three incidents in the same corner are a layout finding.",
  "Ask pupils (a class group or pupil council): 'Where is the yard good? Where do you avoid? Where do adults never go?' They know the blind spots.",
  "Look at the rota: who is on duty, where, for how long, and what they are asked to do (e.g., also covering the canteen, also on their own lunch).",
 ],
 "recommendations": [
  "ZONE THE SPACE: separate areas for ball games, quiet play and structured games; rotate pitch access by class. Make the rules of each zone visible.",
  "ACTIVE SUPERVISION: duty adults move on a route that covers the blind spots, scan, and interact positively; brief all duty staff on the pre-corrections for the hot spots (Colvin et al., 1997).",
  "STAGGER AND SPREAD: staggered breaks or staggered lining up where pinch points are the problem; a second door in use at the end of break.",
  "WHOLE-SCHOOL LEVEL: this is a whole-school recommendation, made in consultation with the principal and staff — frame it within the school's code of behaviour and anti-bullying procedures (Bí Cineálta, 2024).",
  "INDIVIDUAL PLANS SIT ON TOP: for a pupil still struggling, a School Support plan names where they are, with whom, and which adult is nearby.",
  "DO NOT quote a supervision ratio or a regulation you have not checked; DO NOT recommend CCTV or other surveillance — that is a Board of Management and data-protection question, not a psychological one.",
 ],
 "explain_parent": [
  "'Most of the difficulties happen in one corner of the yard where adults can't easily see. The school is looking at how the yard is set up, which should help him and other children too.'",
  "'This doesn't mean nothing is being done for him individually — we'll still plan for his break times specifically.'",
 ],
 "explain_teacher": [
  "'When I put the incident log onto a map of the yard, nearly all of it was behind the prefab and at the back door when lining up. That's a layout problem we can fix more easily than a child problem.'",
  "'Moving around and chatting to groups on duty seems to prevent more than standing at the door and responding — that's what the research on active supervision shows.'",
 ],
 "explain_child": [
  "YOUNGER: 'Show me on this picture of the yard where you like to play, and where things go wrong.'",
  "OLDER: 'If you were in charge of the yard, what would you change so fewer fights happen?'",
  "ASK: 'Where do the teachers never go?' — the most useful single question in this presentation.",
 ],
 "red_flags": [
  "RED FLAG — repeated injury, sexualised behaviour, or bullying in an identified blind spot: this is a safeguarding and anti-bullying matter for the principal and DLP, not only a layout issue.",
  "WATCH — children with physical or sensory needs in a crowded yard (a wheelchair user at a pinch point; a child with visual impairment near ball games): risk assessment by the school.",
  "BOUNDARY — the EP advises; staffing decisions, rotas and physical changes belong to the principal and Board of Management.",
 ],
 "questions": [
  "Q: 'How many teachers should be on yard?' A: 'I can't give you a standard number with confidence — check the school's policy and your management body's guidance. What I can say is where the adults are standing and how they supervise seems to matter as much as how many.'",
  "Q: 'Why are you looking at the yard when we referred a child?' A: 'Because three of the referrals from this school mention lunchtime. If the yard is part of the problem, fixing it helps all of them.'",
  "Q: 'We don't have space to zone.' A: 'Zoning can be done by time as well as space — pitch on alternate days, quiet corner with cones, games leader for the first 15 minutes.'",
 ],
 "supervision": [
  "Discuss how to present a systemic observation to a principal in a way that is heard — what to put in writing and what to say in person.",
  "Reflect on whether, when you get an individual referral, you routinely check the setting first. What made you do it here?",
 ],
 "citations": [
  "Colvin, G., Sugai, G., Good, R. H., & Lee, Y.-Y. (1997). Using active supervision and precorrection to improve transition behaviors in an elementary school. School Psychology Quarterly, 12(4), 344–363.",
  "Lewis, T. J., Colvin, G., & Sugai, G. (2000). The effects of pre-correction and active supervision on the recess behavior of elementary students. Education and Treatment of Children, 23(2), 109–121.",
  "Blatchford, P. (1998). Social life in school: Pupils' experiences of breaktime and recess from 7 to 16 years. Falmer Press.",
  "Department of Education. (2024). Bí Cineálta: Procedures to prevent and address bullying behaviour for primary and post-primary schools. Department of Education. (Check for updates.)",
 ],
})

# ---------------------------------------------------------------- 4
PRES.append({
 "name": "Group dynamics and peer influence",
 "neps": NEPS_22,
 "related_to": ["Conduct Disorder", "ADHD", "Oppositional Defiant Disorder", "Substance use disorders (alcohol, cannabis, opioid, stimulant, tobacco, inhalant, sedative, hallucinogen)", "Social Anxiety Disorder (social phobia)"],
 "what_it_is": [
  "Behaviour that is best understood at the level of the GROUP rather than the individual: a pupil who behaves differently depending on who they are with, a class or friendship group that escalates together, a role the pupil holds in the group (clown, enforcer, follower, scapegoat).",
  "Salmivalli et al. (1996) showed bullying is a group process with participant roles — bully, assistant, reinforcer, outsider, defender, victim. Most children in a bullying episode are not the bully or the victim, and their roles can be changed.",
  "Peer influence is strongest in adolescence: Gardner and Steinberg (2005) found adolescents took more risks in a driving task when peers were present, and the peer effect was larger for adolescents than for adults.",
  "Dishion, McCord and Poulin (1999) showed that grouping young people with conduct problems together can INCREASE problem behaviour ('deviancy training') — directly relevant when schools set up behaviour groups.",
 ],
 "what_it_is_not": [
  "NOT a reason to stop at 'he's easily led'. Ask what the group gives him — belonging, protection, status — and what he would lose by stepping out.",
  "NOT only negative. Peer influence also drives prosocial behaviour; defenders, buddies and peer mentoring use the same process.",
  "NOT solved by splitting everyone up without a plan. Separating a group without giving each member somewhere to belong often reforms the group elsewhere.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: play groups form and change quickly; copying is how young children learn. Describe; do not attribute intent.",
  "SCHOOL AGE 6–12: stable friendship groups from middle primary; exclusion and 'ganging up' appear, especially among the older classes. Friendship mapping is informative (Part D, School Age).",
  "ADOLESCENT 13–16: the peak. Status, reputation and online groups (group chats) shape behaviour in and out of school; risk-taking rises in the presence of peers (Gardner & Steinberg, 2005).",
  "YOUNG ADULT 17–26: peer norms in college, work and social life; relevant mainly for substance use, risk and belonging. Rarely a NEPS referral at this band.",
  "SPECIAL SETTING: small class groups mean one relationship can dominate the dynamic; pupils with social communication difficulties may be set up by peers to break rules without realising.",
 ],
 "assess": [
  "Observe the pupil with different groups (class, yard, a structured group task). Record who initiates, who reinforces (laughs, films, watches), and who withdraws.",
  "Sociometric or friendship mapping (Part D, School Age) — handled ethically and privately; never displayed. At adolescence, a pupil interview about who they spend time with and why.",
  "Incident log analysed by WHO WITH, not only what and when.",
  "Pupil voice: 'Who are you when you're with them? Who are you on your own?' Adolescents can often describe the role they hold.",
 ],
 "recommendations": [
  "CHANGE THE ROLES, NOT JUST THE PERSON: work with bystanders and potential defenders — whole-class work on how to respond when something happens (Salmivalli et al., 1996).",
  "AVOID AGGREGATION: DO NOT recommend putting several pupils with conduct difficulties together in a group intervention without prosocial peers; mixed groups reduce the deviancy-training risk (Dishion et al., 1999).",
  "OFFER ANOTHER PLACE TO BELONG: a club, team, role or responsibility that gives status without the risk behaviour.",
  "SEATING, GROUPING AND TIMETABLE: planned class groupings and seating plans; staggered movement where one group escalates in corridors.",
  "CONTINUUM LEVEL: Classroom Support (grouping, seating) through to whole-school work; School Support for an individual plan where the pupil's role is entrenched.",
  "Where group behaviour involves bullying, apply the school's anti-bullying procedures (Bí Cineálta, 2024 — check for updates).",
 ],
 "explain_parent": [
  "'On his own he's thoughtful and polite. With those three lads he takes on a different role — he's the one who does the dare. It's the group we need to work with as much as him.'",
  "'Rather than just telling him to stay away from them, we're looking for somewhere else he can belong. That tends to work better.'",
 ],
 "explain_teacher": [
  "'Check who laughs and who films. The audience is what keeps it going; working with them is often more effective than targeting the one in the middle.'",
  "'Please don't put all four of them in one behaviour group — the research shows that can make it worse. Mix them with pupils who model the behaviour you want.'",
 ],
 "explain_child": [
  "YOUNGER: 'Sometimes we act differently with different friends. Who do you feel most like yourself with?'",
  "OLDER: 'Everyone plays a part in a group. What part do you end up playing? Is it one you chose?'",
  "ASK: 'What would happen if you said no to them?' — the answer tells you what the group is protecting him from, or giving him.",
 ],
 "red_flags": [
  "RED FLAG — group involvement in exploitation, weapons, sexual harm, or image-sharing: child protection route; Tusla; Gardaí where there is immediate danger.",
  "RED FLAG — a pupil being scapegoated or coerced by the group: treat as bullying and potential harm, not as mutual conflict.",
  "WATCH — a sudden change in friendship group alongside falling attendance or grades: consider substance use, grooming, or an event at home.",
 ],
 "questions": [
  "Q: 'Should we separate them?' A: 'Sometimes, in class. But on its own it moves the group somewhere else. Give each of them another place to belong at the same time.'",
  "Q: 'He's just easily led.' A: 'He is influenced by them — but it's worth asking what he gets from the group. If it's protection or status, that need doesn't go away when they're separated.'",
  "Q: 'Should we run a behaviour group for the lads?' A: 'Only if you mix them with other pupils. Groups of pupils who all have behaviour difficulties can make it worse (Dishion et al., 1999).'",
 ],
 "supervision": [
  "Discuss how to recommend grouping changes without implying the school's existing intervention made things worse.",
  "Reflect on the ethics of sociometric data — who sees it, where it is stored, how children are protected from it.",
 ],
 "citations": [
  "Dishion, T. J., McCord, J., & Poulin, F. (1999). When interventions harm: Peer groups and problem behavior. American Psychologist, 54(9), 755–764.",
  "Gardner, M., & Steinberg, L. (2005). Peer influence on risk taking, risk preference, and risky decision making in adolescence and adulthood: An experimental study. Developmental Psychology, 41(4), 625–635.",
  "Salmivalli, C., Lagerspetz, K., Björkqvist, K., Österman, K., & Kaukiainen, A. (1996). Bullying as a group process: Participant roles and their relations to social status within the group. Aggressive Behavior, 22(1), 1–15.",
  "Department of Education. (2024). Bí Cineálta: Procedures to prevent and address bullying behaviour for primary and post-primary schools. Department of Education. (Check for updates.)",
 ],
})

# ---------------------------------------------------------------- 5
PRES.append({
 "name": "Risk-taking without a diagnosis attached",
 "neps": NEPS_22,
 "related_to": ["ADHD", "Conduct Disorder", "Substance use disorders (alcohol, cannabis, opioid, stimulant, tobacco, inhalant, sedative, hallucinogen)", "Post-Traumatic Stress Disorder", "Major Depressive Disorder"],
 "what_it_is": [
  "Behaviour that puts the young person or others at risk of harm — climbing, running from school, dares, unsafe online contact, sexual risk, vaping, fire-setting, road risk — where no diagnosis explains it and none may be needed.",
  "Risk-taking rises in adolescence for everyone. Steinberg (2008) describes a developmental imbalance: reward sensitivity increases at puberty before self-regulation fully matures, and peers amplify it (Gardner & Steinberg, 2005). Casey, Jones and Hare (2008) give a similar account.",
  "Moffitt (1993) distinguished adolescence-limited from life-course-persistent antisocial behaviour: much adolescent risk-taking is time-limited and normative. The EP's job is to tell the difference — early onset, pervasiveness and severity matter.",
  "Risk-taking also has a FUNCTION: excitement, status, escape, self-punishment, or proof of worth. Ask what it does.",
 ],
 "what_it_is_not": [
  "NOT automatically ADHD, Conduct Disorder or a sign of trauma — although each can present this way. 'Without a diagnosis attached' means describe first; refer only if the wider pattern points there.",
  "NOT to be confused with self-harm or suicidal behaviour. Some 'risk-taking' (walking on train tracks, deliberately unsafe acts) is self-harm by another name — ask directly.",
  "NOT reduced by fear messages alone. Ellis et al. (2012) argue risk-taking serves developmental goals (status, independence); interventions that offer those goals safely work better than ones that only warn.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: climbing, running off, no sense of danger. Mostly developmental; persistent absence of danger awareness with other signs may warrant a developmental review (GP / paediatrics).",
  "SCHOOL AGE 6–12: absconding from class or school, climbing on roofs or walls, dares in the yard, fire play. Absconding is a safety issue for the school's plan today, whatever the cause.",
  "ADOLESCENT 13–16: the core band — alcohol, vaping, sexual risk, online contact with strangers, road risk, dares filmed for social media. Ask what happens in the group, not only in the individual.",
  "YOUNG ADULT 17–26: driving, substances, gambling, sexual health; adult services. Rarely a NEPS referral at this band.",
  "SPECIAL SETTING: absconding and lack of danger awareness in children with intellectual disability or autism are a safety-planning priority; the behaviour may be sensory-seeking or escape from overload.",
 ],
 "assess": [
  "Functional analysis (ABC): what precedes the risk behaviour, what it achieves (escape, attention, sensation, status), and what follows. Functional behaviour assessment is the Special Setting tool in Part D.",
  "Pupil interview: 'What goes through your head just before? What does it feel like during? What happens afterwards?' Listen for thrill, numbness, or 'I don't care what happens to me'.",
  "Ask DIRECTLY about self-harm and suicidal thinking. Asking does not increase risk; not asking can miss it.",
  "Across settings: parent report of risk at home and in the community; any Garda, Tusla or youth service involvement; online activity.",
  "Screen what sits underneath: mood (RCADS self-report, MFQ), trauma history, attention difficulty, an unmet learning need.",
 ],
 "recommendations": [
  "SAFETY PLAN FIRST where the risk is immediate (absconding, climbing, road risk): who notices, who responds, what happens next, parents' contact — agreed with the school before other work.",
  "OFFER THE FUNCTION SAFELY: sport, outdoor pursuits, performance, leadership roles — status and excitement without the harm (Ellis et al., 2012).",
  "TEACH RISK IN CONTEXT: SPHE and RSE work on peer pressure and decision-making, delivered by the school; for the individual, rehearse 'how to get out of it' scripts that save face.",
  "KEY ADULT AND CHECK-IN: a named adult who knows the young person's pattern, particularly on known high-risk days (Fridays, after conflict at home).",
  "CONTINUUM LEVEL: School Support; School Support Plus when outside agencies are involved or the risk is significant.",
  "REFER: CAMHS where risk-taking sits with low mood, self-harm or a suspected diagnosis; Tusla where there are welfare concerns. DO NOT label the young person with a diagnosis in the report.",
 ],
 "explain_parent": [
  "'A lot of teenagers take more risks — it's partly how the brain develops at this age, and friends make it stronger. What worries me more is the pattern and how far he goes, so we're going to plan for that.'",
  "'I asked him about whether he's ever wanted to hurt himself. That's a standard question and it doesn't put the idea in his head.'",
 ],
 "explain_teacher": [
  "'Look at what he gets from it — the lads cheering, a laugh, getting out of class. If we can offer that some other way, the risk-taking has less of a job to do.'",
  "'If he runs, the safety plan is the priority — don't chase; follow the agreed steps and ring home.'",
 ],
 "explain_child": [
  "OLDER: 'Loads of people your age like the buzz of doing something risky — that's normal. I'm interested in when it goes too far and what's going on for you then.'",
  "YOUNGER: 'When you climb up high or run out of school, what does it feel like? What makes you want to do it?'",
  "ASK: 'Have you ever done something risky because you didn't care if you got hurt?' — the direct question that separates thrill from self-harm.",
 ],
 "red_flags": [
  "RED FLAG — risk-taking that is really self-harm, or any suicidal ideation: same-day risk route; inform parents unless unsafe to do so; Tusla where abuse is suspected.",
  "RED FLAG — sexual risk, older contacts, exploitation, online grooming: child protection; report to Tusla as soon as practicable.",
  "WATCH — a sudden rise in risk-taking after a loss, a family change or bullying: formulate around the event.",
 ],
 "questions": [
  "Q: 'Is it ADHD?' A: 'Impulsive risk-taking can be part of ADHD, but lots of teenagers take risks without it. If it's been there since he was small, across school and home, that's worth raising with your GP — I can't make that call.'",
  "Q: 'Will he grow out of it?' A: 'Many young people do — risk-taking tends to peak in adolescence (Steinberg, 2008). Our job is to keep him safe until then and notice if it's more than that.'",
  "Q: 'Should we scare him with the consequences?' A: 'Fear messages on their own don't work well for teenagers. Giving him other ways to get the buzz and the status works better.'",
 ],
 "supervision": [
  "Bring any case where you are unsure whether behaviour is thrill-seeking or self-harm — after the immediate risk action has been taken.",
  "Discuss how you balance a young person's growing autonomy against safety in your recommendations, and how you word that in a report.",
  "Reflect on your own tolerance of risk and how it shapes your formulation.",
 ],
 "citations": [
  "Casey, B. J., Jones, R. M., & Hare, T. A. (2008). The adolescent brain. Annals of the New York Academy of Sciences, 1124, 111–126.",
  "Ellis, B. J., Del Giudice, M., Dishion, T. J., Figueredo, A. J., Gray, P., Griskevicius, V., Hawley, P. H., Jacobs, W. J., James, J., Volk, A. A., & Wilson, D. S. (2012). The evolutionary basis of risky adolescent behavior: Implications for science, policy, and practice. Developmental Psychology, 48(3), 598–623.",
  "Gardner, M., & Steinberg, L. (2005). Peer influence on risk taking, risk preference, and risky decision making in adolescence and adulthood: An experimental study. Developmental Psychology, 41(4), 625–635.",
  "Moffitt, T. E. (1993). Adolescence-limited and life-course-persistent antisocial behavior: A developmental taxonomy. Psychological Review, 100(4), 674–701.",
  "Steinberg, L. (2008). A social neuroscience perspective on adolescent risk-taking. Developmental Review, 28(1), 78–106.",
 ],
})

# ---------------------------------------------------------------- 6
PRES.append({
 "name": "Low confidence and self-esteem",
 "neps": NEPS_31,
 "related_to": ["Specific Learning Disorder with impairment in reading (dyslexia)", "Developmental Language Disorder (DLD)", "Major Depressive Disorder", "Social Anxiety Disorder (social phobia)", "Developmental Coordination Disorder (dyspraxia)"],
 "what_it_is": [
  "A description of how a pupil VALUES themselves (self-esteem) and how sure they feel they can do things (confidence). Part D: 'Not a DSM diagnosis'; 3.1 carries no diagnoses at all — referral is to NEPS.",
  "Rosenberg (1965) defined self-esteem as a global positive or negative attitude toward the self. Harter (2012) showed children's self-evaluations become differentiated with age — by middle childhood they judge themselves separately on school work, sport, looks, friendships and behaviour.",
  "Self-esteem typically dips in early adolescence and recovers through adolescence and adulthood (Orth & Robins, 2014). A Transition Year pupil and a first-year pupil are on different parts of that curve.",
  "Low self-esteem is a risk factor for later depression (Sowislo & Orth, 2013) — reason enough to take it seriously and to look beneath it.",
 ],
 "what_it_is_not": [
  "NOT the cause of poor attainment in most cases. Baumeister et al. (2003) reviewed the evidence and found self-esteem is at best weakly causal for performance; success tends to raise self-esteem more than the reverse. Build skills and success, not just 'boost self-esteem'.",
  "NOT fixed by generic praise. Unconditional praise for easy work can signal low expectations; praise that is specific and earned carries more weight (see also Mueller & Dweck, 1998).",
  "NOT the same as low mood. Persistent sadness, withdrawal, loss of interest or talk of worthlessness need a mood screen and possibly a referral, not a self-esteem programme.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: young children usually rate themselves very positively. Low confidence shows as reluctance to try, clinging, or 'I can't'. Part D: 'Adult report only · structured play and comment · no self-report measure is valid at this age.'",
  "SCHOOL AGE 6–12: social comparison begins — 'I'm in the bottom group'. Part D: My Thoughts About School (NEPS Continuum of Support) · Piers-Harris 3 · drawing and sentence-completion · teacher and parent report.",
  "ADOLESCENT 13–16: appearance, peers and online comparison join school work. Part D: 'Self-report measures become the primary source · Piers-Harris 3 · BASC-3 SRP · solution-focused interview · watch for low mood underneath.'",
  "YOUNG ADULT 17–26: course and work identity; less likely a NEPS referral (Part D).",
  "SPECIAL SETTING: Part D — 'Self-concept relative to the setting peer group, not the mainstream one.' A pupil may feel more capable in a special class than they did in mainstream.",
 ],
 "assess": [
  "Ask WHICH DOMAIN is low — school work, friendships, sport, appearance, behaviour — using Piers-Harris 3 domain scores or Harter-style questions. A single global score hides the picture.",
  "My Thoughts About School (NEPS Continuum of Support resource) at School Age; sentence completion ('I am good at…', 'I wish I…'); drawing 'me at school'.",
  "Teacher and parent report: when does the pupil give up, hide work, refuse to try, or put themselves down?",
  "Screen for low mood (RCADS, MFQ at adolescence) and check for an unidentified learning need — the two most common things underneath.",
 ],
 "recommendations": [
  "BUILD REAL SUCCESS: tasks pitched so the pupil succeeds with effort, and that success made visible (progress charts against their own previous best, not peers).",
  "SPECIFIC, EARNED FEEDBACK: name the strategy or effort ('you checked your answer with the number line'), not the person ('you're so clever').",
  "A ROLE WITH STATUS: a responsibility that uses a real strength — buddy for a younger pupil, class job, team role.",
  "ADDRESS THE CAUSE: if a literacy, language or motor need is driving it, the intervention for that need IS the self-esteem intervention.",
  "CONTINUUM LEVEL: Classroom Support in most cases; School Support for a targeted plan (e.g., small-group social and emotional programme) with a review date.",
  "REFER: where low mood, self-harm or hopelessness is present, to GP / Primary Care Psychology / CAMHS as the level of need requires. DO NOT describe low self-esteem as a diagnosis.",
 ],
 "explain_parent": [
  "'She's not low in herself across the board — she feels good about friends and swimming. It's school work where she thinks she's no good, and that's because reading has been hard for a long time.'",
  "'Telling her she's great won't shift it on its own. What shifts it is her seeing herself get better at something, so that's where the plan starts.'",
 ],
 "explain_teacher": [
  "'Compare her with herself, not the class — a chart of her own scores going up will do more than any sticker.'",
  "'When you praise, name what she did. \"You kept going when it got hard\" lands; \"good girl\" doesn't.'",
  "'Give her a job that uses what she's good at — she's brilliant with the younger ones.'",
 ],
 "explain_child": [
  "YOUNGER: 'Let's make a list of things you're good at and things that are tricky. Everyone has both.'",
  "OLDER: 'Lots of people feel rubbish about one part of their life and fine about the rest. Which bits feel OK for you?'",
  "ASK: 'When did you last feel proud of yourself? What were you doing?'",
 ],
 "red_flags": [
  "RED FLAG — talk of being worthless, a burden, or better off gone: ask directly about suicidal thoughts; same-day risk route.",
  "WATCH — persistent low self-worth with sleep, appetite or interest changes: mood screen and GP/CAMHS referral via parents.",
  "WATCH — a sudden drop in confidence: ask about bullying, online events, or change at home.",
 ],
 "questions": [
  "Q: 'If we boost his self-esteem, will his grades go up?' A: 'Probably not on its own — the research suggests success raises self-esteem more than the other way round (Baumeister et al., 2003). So we start with helping him succeed.'",
  "Q: 'Should I tell her she's brilliant all the time?' A: 'Specific praise about what she did works better than general praise. Children can tell when it's not earned.'",
  "Q: 'Is this depression?' A: 'Low self-esteem isn't the same as depression, but it can be a risk for it. I've checked her mood today and I'll tell you what I found.'",
 ],
 "supervision": [
  "Bring any case where self-esteem was the referral reason — check together whether a learning need or low mood has been ruled out.",
  "Discuss how you word self-esteem findings so they describe the domain and the context rather than labelling the child.",
 ],
 "citations": [
  "Baumeister, R. F., Campbell, J. D., Krueger, J. I., & Vohs, K. D. (2003). Does high self-esteem cause better performance, interpersonal success, happiness, or healthier lifestyles? Psychological Science in the Public Interest, 4(1), 1–44.",
  "Harter, S. (2012). The construction of the self: Developmental and sociocultural foundations (2nd ed.). Guilford Press.",
  "Orth, U., & Robins, R. W. (2014). The development of self-esteem. Current Directions in Psychological Science, 23(5), 381–387.",
  "Rosenberg, M. (1965). Society and the adolescent self-image. Princeton University Press.",
  "Sowislo, J. F., & Orth, U. (2013). Does low self-esteem predict depression and anxiety? A meta-analysis of longitudinal studies. Psychological Bulletin, 139(1), 213–240.",
 ],
})

# ---------------------------------------------------------------- 7
PRES.append({
 "name": "Learned helplessness",
 "neps": NEPS_31,
 "related_to": ["Specific Learning Disorder with impairment in reading (dyslexia)", "Specific Learning Disorder with impairment in mathematics (dyscalculia)", "Major Depressive Disorder", "Intellectual Disability — mild", "ADHD"],
 "what_it_is": [
  "A pattern where a pupil has come to believe that what they do makes no difference to the outcome, so they stop trying — even when success is now within reach. Part D: 'Not a DSM diagnosis.'",
  "The term comes from Seligman and Maier (1967). Abramson, Seligman and Teasdale (1978) reformulated it for humans around ATTRIBUTIONS: helplessness is worse when failure is explained as internal ('it's me'), stable ('always') and global ('at everything').",
  "Diener and Dweck (1978) showed the classroom version: after failure, 'helpless' children's strategies deteriorated and they blamed their ability, while 'mastery-oriented' children with the same skills kept using good strategies.",
  "Maier and Seligman (2016) revised the theory: passivity may be the default response to uncontrollable adversity, and what is LEARNED is that one has control. The practical message is the same — the child needs repeated experience that their effort changes outcomes.",
 ],
 "what_it_is_not": [
  "NOT laziness. The child who puts their head down before reading the question is protecting themselves from another failure, not choosing to avoid effort.",
  "NOT a fixed trait. It is learned from experience and can be unlearned from experience — but only if the tasks and feedback actually change.",
  "NOT the same as depression, though it overlaps with it: helplessness was proposed as a model of depression. If hopelessness extends beyond school work, screen mood.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: rare as a pattern; watch for a young child who has stopped attempting tasks, often after repeated overwhelming demands. Adult report only.",
  "SCHOOL AGE 6–12: 'I can't do it' before trying; waiting for help; copying; blank pages; tears when asked to start alone. Common in children with an unidentified literacy or maths difficulty after years of failure.",
  "ADOLESCENT 13–16: 'What's the point?' — refusing to attempt exams, choosing lower levels, disengaging from whole subjects. Can look like indifference or defiance.",
  "YOUNG ADULT 17–26: avoidance of courses or jobs that involve the old failure area; less likely a NEPS referral.",
  "SPECIAL SETTING: high adult support can inadvertently teach helplessness (prompt dependence). Check how quickly adults step in.",
 ],
 "assess": [
  "Observe the FIRST 60 SECONDS of an independent task: does the pupil start, look around, wait, or give up? Time to first attempt is a useful measure.",
  "Give a task you know the pupil CAN do, framed as new. If they still say 'I can't', the belief is running ahead of the skill — that is the helplessness signature.",
  "Attribution interview: 'When you got that one wrong, why do you think it happened?' Listen for internal-stable-global explanations ('I'm thick').",
  "Establish the skill level objectively (e.g., WIAT-III UK) — you need to know whether the task is genuinely too hard before calling it helplessness.",
 ],
 "recommendations": [
  "ENGINEER CONTROLLABLE SUCCESS: tasks broken into steps the pupil can complete, with the link between their action and the outcome made explicit ('you used the strategy, and look — it worked').",
  "ATTRIBUTION RETRAINING: consistently attribute success to effort and strategy, and failure to strategy or effort that can change — not to ability (Abramson et al., 1978; Dweck & Leggett, 1988).",
  "FADE ADULT HELP ON PURPOSE: wait-time before prompting; least-to-most prompting; a 'try it first, then ask' card.",
  "TEACH THE MISSING SKILL: if there is a literacy or maths gap, targeted teaching is non-negotiable — without it, the new 'experience of control' never arrives.",
  "CONTINUUM LEVEL: Classroom Support to School Support; the plan should include a measure such as independent starts per lesson.",
  "WATCH MOOD: if hopelessness generalises beyond school, screen mood and refer via GP or CAMHS as needed.",
 ],
 "explain_parent": [
  "'He's had so many experiences of trying hard and still getting it wrong that he's decided trying doesn't work. That's a sensible conclusion from what he's lived — but it's no longer true, because the work is now pitched at his level.'",
  "'Every time he does something and it works, point to what he did. He needs to see the connection over and over.'",
 ],
 "explain_teacher": [
  "'Give him ten seconds before you step in. If you help as soon as he looks up, he learns that looking up is the strategy.'",
  "'When he gets it right, tell him why — \"you sounded it out and it worked\". He still thinks success is luck.'",
 ],
 "explain_child": [
  "YOUNGER: 'Sometimes when things have been hard for a long time, our brain says \"don't bother\". Let's catch your brain being wrong.'",
  "OLDER: 'It makes sense you stopped trying — it didn't seem to work. What's different now is the work is set up so your effort pays off. Let's test it.'",
  "ASK: 'Is there anything you used to be bad at and now you're good at? How did that happen?'",
 ],
 "red_flags": [
  "WATCH — helplessness spreading to everything ('nothing I do matters'), with low mood or withdrawal: mood screen; ask about self-harm; refer via parents to GP/CAMHS.",
  "WATCH — adult over-support as the maintaining factor in special settings or with SNA support: raise it tactfully.",
  "BOUNDARY — do not describe the child as 'depressed' in a report; describe the pattern and refer.",
 ],
 "questions": [
  "Q: 'He won't even try — isn't that just attitude?' A: 'It looks like attitude, but when I gave him something he could do, he still said he couldn't. That's a belief learned from years of failure, and it needs a plan, not a sanction.'",
  "Q: 'Should the SNA sit with him all day?' A: 'Constant help can keep the pattern going. Planned support that steps back as he succeeds is better.'",
  "Q: 'How long will it take?' A: 'It took years to learn; expect weeks to months to shift. Measure small signs — how fast he starts, how often he tries before asking.'",
 ],
 "supervision": [
  "Discuss how to observe and measure 'trying' in a way that stands up in a report.",
  "Reflect on how adult help — including your own during testing — can reinforce helplessness, and what that means for how you administer tests.",
 ],
 "citations": [
  "Abramson, L. Y., Seligman, M. E. P., & Teasdale, J. D. (1978). Learned helplessness in humans: Critique and reformulation. Journal of Abnormal Psychology, 87(1), 49–74.",
  "Diener, C. I., & Dweck, C. S. (1978). An analysis of learned helplessness: Continuous changes in performance, strategy, and achievement cognitions following failure. Journal of Personality and Social Psychology, 36(5), 451–462.",
  "Dweck, C. S., & Leggett, E. L. (1988). A social-cognitive approach to motivation and personality. Psychological Review, 95(2), 256–273.",
  "Maier, S. F., & Seligman, M. E. P. (2016). Learned helplessness at fifty: Insights from neuroscience. Psychological Review, 123(4), 349–367.",
  "Seligman, M. E. P., & Maier, S. F. (1967). Failure to escape traumatic shock. Journal of Experimental Psychology, 74(1), 1–9.",
 ],
})

# ---------------------------------------------------------------- 8
PRES.append({
 "name": "Academic self-concept vs global self-esteem",
 "neps": NEPS_31,
 "related_to": ["Specific Learning Disorder with impairment in reading (dyslexia)", "Developmental Language Disorder (DLD)", "Borderline Intellectual Functioning", "Giftedness / exceptional ability", "ADHD"],
 "what_it_is": [
  "The distinction between how a pupil sees themselves AS A LEARNER (academic self-concept) and how they feel about themselves OVERALL (global self-esteem). They are related but separate, and they can go in different directions.",
  "Shavelson, Hubner and Stanton (1976) proposed a hierarchical, multidimensional model: global self-concept at the top, academic and non-academic self-concepts beneath it, and subject-specific self-concepts (maths, English) below that.",
  "Marsh and Craven (2006) report reciprocal effects: academic self-concept and achievement each influence the other over time. Unlike global self-esteem (Baumeister et al., 2003), SUBJECT-specific self-concept is linked to performance in that subject.",
  "Marsh (1987) described the big-fish-little-pond effect: the same pupil has a lower academic self-concept in a high-achieving class than in an average one. Comparison group matters.",
 ],
 "what_it_is_not": [
  "NOT interchangeable terms. A report that says 'low self-esteem' when the data show low MATHS self-concept and healthy global self-esteem misleads the reader and the recommendation.",
  "NOT fixed across subjects. A pupil can see themselves as good at English and hopeless at maths (Marsh's internal/external frame of reference model) — check each.",
  "NOT only about ability. Academic self-concept is shaped by comparison, feedback and grouping — things the school controls.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: self-concept is positive and undifferentiated; not meaningfully separable at this age. Adult report only (Part D).",
  "SCHOOL AGE 6–12: domains separate by middle childhood (Harter, 2012); ability grouping and visible comparison (reading groups, table names) start to shape academic self-concept.",
  "ADOLESCENT 13–16: subject self-concepts drive choices of level (Higher/Ordinary) and subject. Global self-esteem is more tied to peers and appearance.",
  "YOUNG ADULT 17–26: course and career identity; academic self-concept affects persistence in further or higher education.",
  "SPECIAL SETTING: Part D — 'Self-concept relative to the setting peer group, not the mainstream one.' Moving setting can raise academic self-concept (a big-fish effect) — useful to know when advising on placement.",
 ],
 "assess": [
  "Piers-Harris 3 domain scores (e.g., the intellectual and school status domain) alongside the total — check the manual for current domain names and interpretation.",
  "Ask domain-by-domain: 'How good are you at reading / maths / sport / making friends? How much does it matter to you?' Harter (2012) emphasises that a low self-rating hurts most in domains the child values.",
  "Compare the pupil's view with attainment data. A low academic self-concept with average attainment points to comparison or feedback; a matching low points to skill.",
  "Look at the grouping and feedback context: ability groups, public results, which class they are in.",
 ],
 "recommendations": [
  "REPORT PRECISELY: name the domain — 'low academic self-concept in reading, with positive global self-esteem' — so the recommendation targets the right thing.",
  "SUBJECT-SPECIFIC SUCCESS + FEEDBACK: because academic self-concept and achievement are reciprocal (Marsh & Craven, 2006), combine skill teaching with feedback that makes progress visible in that subject.",
  "REDUCE PUBLIC COMPARISON: flexible grouping, self-referenced progress measures, private feedback.",
  "PROTECT WHAT IS HEALTHY: where global self-esteem is good, name the strengths that sustain it (sport, friends, music) and do not remove them for extra tuition.",
  "CONTINUUM LEVEL: Classroom Support; School Support where a targeted learning plan is in place.",
  "DO NOT recommend a generic self-esteem programme where the difficulty is subject-specific.",
 ],
 "explain_parent": [
  "'She feels good about herself as a person — friends, hurling, family. It's as a reader that she thinks she's no good. That's actually good news: the fix is more specific.'",
  "'Keep the hurling. It's part of what keeps her feeling good about herself while reading catches up.'",
 ],
 "explain_teacher": [
  "'Her problem isn't self-esteem in general — it's how she sees herself in reading. Seeing her own reading improve will do more than a confidence programme.'",
  "'Being in the lowest reading group, where everyone knows it's the lowest, is feeding it. Can the groups be more flexible?'",
 ],
 "explain_child": [
  "YOUNGER: 'You can be great at some things and still learning others. Let's draw a picture with all the different bits of you.'",
  "OLDER: 'How you feel about yourself as a person and how you feel about maths are two different things. One can be fine while the other's low.'",
  "ASK: 'Which subject makes you feel smartest? Which makes you feel least smart? Why?'",
 ],
 "red_flags": [
  "WATCH — low academic self-concept spreading to global worthlessness ('I'm stupid, I'm useless'): check mood; ask about self-harm if indicated.",
  "WATCH — a highly able pupil in a selective setting with collapsing academic self-concept (big-fish-little-pond): may present as anxiety or disengagement.",
 ],
 "questions": [
  "Q: 'The report says she has good self-esteem — so why is she upset about school?' A: 'Feeling good about yourself overall and feeling good about yourself as a learner are different. Hers is the second.'",
  "Q: 'Would moving her to a smaller class help?' A: 'It can raise how she sees herself as a learner, because she's comparing with different peers. That's one factor to weigh, not the only one.'",
  "Q: 'Does self-esteem matter for results?' A: 'General self-esteem not much; how she sees herself in a particular subject does, and the two feed each other (Marsh & Craven, 2006).'",
 ],
 "supervision": [
  "Check your report drafts for the words 'self-esteem' and ask whether you meant self-esteem or self-concept in a domain.",
  "Discuss placement cases where the big-fish-little-pond effect is relevant.",
 ],
 "citations": [
  "Harter, S. (2012). The construction of the self: Developmental and sociocultural foundations (2nd ed.). Guilford Press.",
  "Marsh, H. W. (1987). The big-fish-little-pond effect on academic self-concept. Journal of Educational Psychology, 79(3), 280–295.",
  "Marsh, H. W., & Craven, R. G. (2006). Reciprocal effects of self-concept and performance from a multidimensional perspective: Beyond seductive pleasure and unidimensional perspectives. Perspectives on Psychological Science, 1(2), 133–163.",
  "Shavelson, R. J., Hubner, J. J., & Stanton, G. C. (1976). Self-concept: Validation of construct interpretations. Review of Educational Research, 46(3), 407–441.",
  "Baumeister, R. F., Campbell, J. D., Krueger, J. I., & Vohs, K. D. (2003). Does high self-esteem cause better performance, interpersonal success, happiness, or healthier lifestyles? Psychological Science in the Public Interest, 4(1), 1–44.",
 ],
})

# ---------------------------------------------------------------- 9
PRES.append({
 "name": "Attribution style",
 "neps": NEPS_31,
 "related_to": ["Specific Learning Disorder with impairment in reading (dyslexia)", "ADHD", "Major Depressive Disorder", "Giftedness / exceptional ability"],
 "what_it_is": [
  "How a pupil EXPLAINS their successes and failures. Part D frames it as 'effort vs ability': does the pupil think they did well because they tried and used a good strategy, or because they are (or aren't) 'smart'?",
  "Weiner (1985) described attributions along three dimensions — locus (internal/external), stability (stable/unstable) and controllability. Effort is internal, unstable and controllable; ability is internal, stable and uncontrollable. The dimensions predict emotion and persistence.",
  "Attributing failure to low ability (stable, uncontrollable) leads to shame and giving up; attributing it to effort or strategy (changeable) leads to trying again (Weiner, 1985; Dweck & Leggett, 1988).",
  "Adults shape attributions through feedback. Mueller and Dweck (1998) found children praised for intelligence were more likely to avoid challenge and to perform worse after failure than children praised for effort.",
 ],
 "what_it_is_not": [
  "NOT the same as 'growth mindset' posters. Sisk et al. (2018) found small average effects of mindset interventions on achievement; Yeager et al. (2019) found effects concentrated among lower-achieving students in supportive schools. Attributional feedback in daily teaching matters more than a one-off intervention.",
  "NOT always wrong to attribute to ability. For a pupil with a specific learning difficulty, some tasks really are harder; the useful attribution is 'this is hard for me AND the right strategy helps', not 'try harder'.",
  "NOT only about failure. A pupil who explains success as luck ('the test was easy') gains nothing from succeeding.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: young children tend to see effort and ability as the same thing; not a meaningful assessment target. Adult language is the thing to note.",
  "SCHOOL AGE 6–12: by later primary children begin to separate effort from ability; 'I'm just not smart' can appear. My Thoughts About School and sentence completion reveal it (Part D).",
  "ADOLESCENT 13–16: attributions stabilise and drive level choices, homework effort and exam avoidance. Self-report interview is the main source.",
  "YOUNG ADULT 17–26: attributions shape persistence in courses and work; less likely a NEPS referral.",
  "SPECIAL SETTING: pupils may attribute success to adult help ('Miss did it'). Make the pupil's own contribution explicit.",
 ],
 "assess": [
  "After a task, ask: 'You got that one right — why do you think?' and 'That one went wrong — why?' Code the answers: effort, ability, strategy, luck, task difficulty, other people.",
  "Sentence completion: 'When I do badly in a test it's because…', 'People who are good at maths are…'.",
  "Listen to adult feedback in the classroom during observation: is praise about the person or the process?",
  "Cross-check with attainment and cognitive profile — an attribution of 'I'm bad at spelling' may be accurate and still unhelpful.",
 ],
 "recommendations": [
  "PROCESS FEEDBACK AS ROUTINE: praise effort, strategy, persistence and improvement; avoid 'you're so smart' (Mueller & Dweck, 1998).",
  "MAKE STRATEGY VISIBLE: after success, name the strategy that worked; after failure, name the next strategy to try. This gives a controllable explanation.",
  "AVOID 'JUST TRY HARDER' for a pupil who already tries: attribute to strategy, not effort, or the pupil concludes that maximum effort still fails — which confirms low ability.",
  "WHOLE-CLASS: a shared language of 'not yet' and 'what strategy could you use?' costs nothing and benefits everyone.",
  "CONTINUUM LEVEL: Classroom Support; School Support where attribution retraining is part of an individual plan.",
  "DO NOT rely on a stand-alone mindset programme as the intervention (Sisk et al., 2018).",
 ],
 "explain_parent": [
  "'When she gets something wrong, she tells herself it's because she's stupid. That makes her stop trying. We're going to help her see that the strategy is what went wrong, and strategies can change.'",
  "'At home, try praising how she did something — \"you kept checking\" — rather than \"you're so clever\". It sounds small but it makes a difference.'",
 ],
 "explain_teacher": [
  "'He tries hard already. \"Try harder\" tells him that his best isn't good enough. \"Try this way\" gives him somewhere to go.'",
  "'When he gets it right, ask him why. If he says \"luck\", tell him what he actually did.'",
 ],
 "explain_child": [
  "YOUNGER: 'Your brain is like a muscle — it gets stronger when you practise the right way.'",
  "OLDER: 'When something goes wrong, there are two stories: \"I'm no good\" or \"that strategy didn't work\". Only one of them lets you do anything about it.'",
  "ASK: 'Think of someone who's really good at something. How did they get good?'",
 ],
 "red_flags": [
  "WATCH — pervasive self-blame ('everything bad is my fault') beyond school: screen for low mood (Abramson et al., 1978 link attribution style to depression).",
  "WATCH — a highly able pupil who attributes all success to 'being smart' and avoids any challenge: can present as anxiety or perfectionism in adolescence.",
 ],
 "questions": [
  "Q: 'Should we do growth mindset with the class?' A: 'The research shows small effects on average from mindset programmes (Sisk et al., 2018). The bigger lever is how feedback is given every day.'",
  "Q: 'Isn't it true he finds it harder?' A: 'Yes, for spelling it is. The helpful message isn't \"it's not hard\" — it's \"it's hard, and this strategy helps\".'",
  "Q: 'Is praising her for being clever bad?' A: 'It can make children avoid hard work to protect the label (Mueller & Dweck, 1998). Praise the effort and the strategy instead.'",
 ],
 "supervision": [
  "Listen back to (or reflect on) your own feedback during an assessment session — did you praise the child or the process?",
  "Discuss how to present attribution findings to teachers without it sounding like 'you're praising wrong'.",
 ],
 "citations": [
  "Dweck, C. S., & Leggett, E. L. (1988). A social-cognitive approach to motivation and personality. Psychological Review, 95(2), 256–273.",
  "Mueller, C. M., & Dweck, C. S. (1998). Praise for intelligence can undermine children's motivation and performance. Journal of Personality and Social Psychology, 75(1), 33–52.",
  "Sisk, V. F., Burgoyne, A. P., Sun, J., Butler, J. L., & Macnamara, B. N. (2018). To what extent and under which circumstances are growth mind-sets important to academic achievement? Two meta-analyses. Psychological Science, 29(4), 549–571.",
  "Weiner, B. (1985). An attributional theory of achievement motivation and emotion. Psychological Review, 92(4), 548–573.",
  "Yeager, D. S., Hanselman, P., Walton, G. M., et al. (2019). A national experiment reveals where a growth mindset improves achievement. Nature, 573(7774), 364–369.",
 ],
})

# ---------------------------------------------------------------- 10
PRES.append({
 "name": "Response to failure and setback",
 "neps": NEPS_31,
 "related_to": ["ADHD", "Autism", "Generalised Anxiety Disorder", "Disruptive Mood Dysregulation Disorder", "Specific Learning Disorder with impairment in reading (dyslexia)"],
 "what_it_is": [
  "How a pupil REACTS when something goes wrong — a wrong answer, a poor mark, losing a game, being corrected. Part D notes this item uses Form 2 survey wording; check the form in use for the exact phrasing.",
  "Reactions range from recovering and trying again, to withdrawal, tears, anger, tearing up work, or refusing the next task. The EP describes the pattern: what triggers it, how big the reaction is, and how long recovery takes.",
  "Martin and Marsh (2008) describe ACADEMIC BUOYANCY — the capacity to deal with everyday setbacks (a poor grade, a bad day) — as distinct from resilience in the face of major adversity. Most school referrals are about buoyancy.",
  "Diener and Dweck (1978) showed that after failure some children keep strategies intact ('mastery-oriented') and some deteriorate ('helpless'), even with equal skills — the reaction is itself a learned pattern.",
 ],
 "what_it_is_not": [
  "NOT simply 'a bad loser' or 'too sensitive'. A strong reaction to failure is information about how the pupil understands mistakes and what they fear it means.",
  "NOT always emotional regulation difficulty in general. Some pupils regulate well elsewhere and react only to academic failure — that is a specific pattern.",
  "NOT helped by removing all failure. Pupils need small, safe setbacks with support to learn to recover; protecting them from every mistake removes the practice.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: frustration and tantrums when something doesn't work are developmentally expected; watch for recovery with adult help.",
  "SCHOOL AGE 6–12: tearing up work, meltdowns at losing, refusing to try again after a wrong answer. Correction in front of peers is a common trigger.",
  "ADOLESCENT 13–16: shutting down after a poor test result, dropping a subject level, not handing in work to avoid a grade, or anger at a teacher's feedback.",
  "YOUNG ADULT 17–26: withdrawal from a course after a failed exam or placement; less likely a NEPS referral.",
  "SPECIAL SETTING: rigid expectations of 'right' (sometimes linked to autism) can make any mistake intolerable — check the function before targeting the behaviour.",
 ],
 "assess": [
  "Observe or ask about specific setbacks: what happened, what the pupil did, how long until they re-engaged, what helped them recover.",
  "Pupil interview: 'What goes through your head when you get something wrong?' The answer ('I'm stupid', 'everyone will laugh', 'Mam will be cross') gives you the formulation.",
  "Teacher and parent report on reactions at home vs school and in academic vs non-academic settings (sport, games).",
  "Screen for anxiety (RCADS), perfectionism and an unidentified learning need — each can drive intense reactions to failure.",
 ],
 "recommendations": [
  "NORMALISE MISTAKES: teacher models making and fixing mistakes; 'favourite mistake' discussions; marking that shows how to improve, not just what is wrong.",
  "PRIVATE CORRECTION: feedback given quietly and with a next step; avoid public correction for this pupil.",
  "RECOVERY ROUTINE: a planned response to a setback — a short break, a calming strategy, then a smaller version of the task to regain success.",
  "GRADED EXPOSURE TO SETBACK: low-stakes games and tasks where losing is likely and supported, gradually increasing.",
  "CONTINUUM LEVEL: Classroom Support; School Support with a plan and a review measure (e.g., time to re-engage after a setback).",
  "REFER if reactions include self-harm, extreme distress or are part of wider anxiety or mood difficulty (Primary Care / CAMHS).",
 ],
 "explain_parent": [
  "'When she gets something wrong, it feels to her like proof she's no good, so the reaction is big. We're going to help her practise getting things wrong in small, safe ways, and bouncing back.'",
  "'At home, let her see you make mistakes and fix them. That's more powerful than telling her mistakes are OK.'",
 ],
 "explain_teacher": [
  "'Correcting him in front of the class is what sets it off. A quiet word and a next step keeps him in the lesson.'",
  "'When it happens, give him a couple of minutes, then a smaller version of the task so he gets a win straight away.'",
 ],
 "explain_child": [
  "YOUNGER: 'Mistakes are how our brain learns. Let's find a mistake today and see what it taught us.'",
  "OLDER: 'Everyone gets things wrong. What matters is what you do next. What's helped you bounce back before?'",
  "ASK: 'When you get something wrong, what do you think other people think?'",
 ],
 "red_flags": [
  "RED FLAG — self-harm or statements of worthlessness after failure: same-day risk route.",
  "WATCH — an extreme reaction to minor setbacks in multiple settings: consider anxiety, mood or a neurodevelopmental difference, and refer as appropriate.",
  "WATCH — exam-time withdrawal in adolescence: screen for anxiety and perfectionism.",
 ],
 "questions": [
  "Q: 'Should we let her win so she doesn't get upset?' A: 'Sometimes, while she's learning. But she needs safe practice at losing too, with support, or it never gets easier.'",
  "Q: 'Why does he react so badly to a small mistake?' A: 'To him it isn't small — it's evidence that he's stupid. We're working on that belief.'",
  "Q: 'Is it anxiety?' A: 'It can be part of anxiety. I've screened for that and I'll tell you what I found.'",
 ],
 "supervision": [
  "Bring an example of a pupil's reaction to failure during your own assessment — how did you handle it, and would you change anything?",
  "Discuss the difference between buoyancy and resilience and how you would word each in a report.",
 ],
 "citations": [
  "Diener, C. I., & Dweck, C. S. (1978). An analysis of learned helplessness: Continuous changes in performance, strategy, and achievement cognitions following failure. Journal of Personality and Social Psychology, 36(5), 451–462.",
  "Dweck, C. S., & Leggett, E. L. (1988). A social-cognitive approach to motivation and personality. Psychological Review, 95(2), 256–273.",
  "Martin, A. J., & Marsh, H. W. (2008). Academic buoyancy: Towards an understanding of students' everyday academic resilience. Journal of School Psychology, 46(1), 53–83.",
 ],
})

# ---------------------------------------------------------------- 11
PRES.append({
 "name": "Perfectionism and fear of getting it wrong",
 "neps": NEPS_31,
 "related_to": ["Generalised Anxiety Disorder", "Obsessive-Compulsive Disorder", "Autism", "Anorexia Nervosa", "Giftedness / exceptional ability"],
 "what_it_is": [
  "Setting excessively high standards for oneself and judging oneself harshly for falling short, with fear of mistakes driving behaviour: rewriting, not handing in, avoiding new tasks, distress at anything less than full marks.",
  "Frost et al. (1990) identified dimensions including concern over mistakes, doubts about actions, personal standards and parental expectations. Hewitt and Flett (1991) distinguished self-oriented, other-oriented and socially prescribed perfectionism (believing others demand perfection).",
  "Stoeber and Otto (2006) separate perfectionistic STRIVINGS (high standards — often adaptive) from perfectionistic CONCERNS (fear of mistakes, self-criticism — consistently linked to distress). The concerns, not the standards, are the target.",
  "Curran and Hill (2019) found perfectionism scores in young people increased across birth cohorts between 1989 and 2016 (US, Canadian and UK samples) — it is becoming more common, not less.",
 ],
 "what_it_is_not": [
  "NOT the same as being conscientious or high-achieving. A pupil with high standards who recovers from mistakes and enjoys work is not the concern; a pupil whose self-worth depends on flawless work is.",
  "NOT OCD — though they overlap. Perfectionism is about standards and self-worth; OCD involves intrusive thoughts and compulsions to neutralise anxiety. If there are rituals the pupil feels driven to perform, check (see 'Repeated checking of work').",
  "NOT only found in high achievers. Pupils with learning difficulties can be perfectionistic too, and it often shows as refusal to attempt anything they might get wrong.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: distress at a drawing that 'isn't right', refusing to try unfamiliar things. Often temperament; describe and watch.",
  "SCHOOL AGE 6–12: rubbing out repeatedly, tearing pages, very slow work, tears at a single error, avoiding reading aloud. My Thoughts About School and sentence completion help (Part D).",
  "ADOLESCENT 13–16: all-nighters, not submitting coursework until 'perfect', procrastination, exam distress, social media comparison. Egan, Wade and Shafran (2011) describe perfectionism as a transdiagnostic process across anxiety, depression and eating disorders — watch for these.",
  "YOUNG ADULT 17–26: missed deadlines, dropping out after a single poor grade, burnout. Less likely a NEPS referral.",
  "SPECIAL SETTING: in autistic pupils, 'getting it right' may reflect a need for predictability or a literal reading of instructions rather than self-worth — explore the function.",
 ],
 "assess": [
  "Interview: 'What happens if it's not perfect? What would that mean about you?' The meaning attached to mistakes separates strivings from concerns.",
  "Observe work: rubbings-out, time spent, uncompleted pieces, reaction to an error. Look at the work-sample record over a term.",
  "Parent and teacher report: where it shows (homework, sport, music), and whether adults' expectations or praise feed it.",
  "Screen for anxiety and mood (RCADS; MFQ at adolescence). At adolescence, be alert to eating and body-image concerns.",
 ],
 "recommendations": [
  "SEPARATE WORK FROM WORTH: feedback on the work, never on the person; celebrate 'good enough' and completion.",
  "TIME AND DRAFT LIMITS: 'first draft only', a timer for rewriting, a set number of rubbing-outs; submit on time and improve later.",
  "PLANNED IMPERFECTION: low-stakes tasks where mistakes are expected (brainstorms, sketches, quizzes that don't count) — graded exposure to getting it wrong.",
  "ADULT MODELLING: teachers and parents talk openly about their own mistakes and how they coped; reduce public ranking of results.",
  "CONTINUUM LEVEL: Classroom Support; School Support where distress is significant. REFER to Primary Care Psychology or CAMHS if perfectionism is part of anxiety, OCD, depression or an eating difficulty — CBT approaches to perfectionism are delivered by clinical services (Shafran, Cooper & Fairburn, 2002).",
  "DO NOT recommend 'just relax' or 'it doesn't matter' — the pupil hears that you don't understand.",
 ],
 "explain_parent": [
  "'Her standards are high, which can be a strength. The problem is that she feels like a failure if anything isn't perfect, and that's making her exhausted and anxious.'",
  "'Try praising finishing, not the result: \"You got it done — well done.\" And tell her about something you got wrong this week.'",
 ],
 "explain_teacher": [
  "'She's not being slow on purpose — she's rubbing out anything that isn't perfect. A first-draft-only rule for some tasks will help a lot.'",
  "'If she hands in something with mistakes, praise that she handed it in. That's the hard part for her.'",
 ],
 "explain_child": [
  "YOUNGER: 'Mistakes are how our brains learn. Let's have a \"mistake of the day\" and see if anything bad actually happens.'",
  "OLDER: 'Having high standards is fine. The problem is when getting something wrong feels like you are wrong. They're not the same thing.'",
  "ASK: 'What would happen if you handed it in with one mistake? What's the worst that could happen, and how likely is it?'",
 ],
 "red_flags": [
  "RED FLAG — restricted eating, rapid weight change or intense body focus with perfectionism: GP referral via parents, promptly; eating disorders are medical and psychiatric matters.",
  "RED FLAG — self-harm or hopelessness after perceived failure: same-day risk route.",
  "WATCH — rituals or checking the pupil feels compelled to do: consider OCD; refer via GP to Primary Care / CAMHS.",
 ],
 "questions": [
  "Q: 'Isn't it good that she wants to do well?' A: 'High standards are good. What's hurting her is the fear of mistakes and feeling she's a failure — that's the part we're working on.'",
  "Q: 'Where does it come from?' A: 'Usually a mix of temperament and experience. Sometimes pressure — even gentle — from adults or school plays a part. It's not about blame; it's about what we can change now.'",
  "Q: 'Should we lower expectations?' A: 'Not lower — broaden. Value finishing, trying new things and learning from mistakes as much as the marks.'",
 ],
 "supervision": [
  "Discuss where the line sits between perfectionism you can support in school and anxiety or OCD that needs a clinical referral.",
  "Reflect on your own perfectionism and how it might shape your reports or your reaction to the pupil.",
 ],
 "citations": [
  "Curran, T., & Hill, A. P. (2019). Perfectionism is increasing over time: A meta-analysis of birth cohort differences from 1989 to 2016. Psychological Bulletin, 145(4), 410–429.",
  "Egan, S. J., Wade, T. D., & Shafran, R. (2011). Perfectionism as a transdiagnostic process: A clinical review. Clinical Psychology Review, 31(2), 203–212.",
  "Frost, R. O., Marten, P., Lahart, C., & Rosenblate, R. (1990). The dimensions of perfectionism. Cognitive Therapy and Research, 14(5), 449–468.",
  "Hewitt, P. L., & Flett, G. L. (1991). Perfectionism in the self and social contexts: Conceptualization, assessment, and association with psychopathology. Journal of Personality and Social Psychology, 60(3), 456–470.",
  "Stoeber, J., & Otto, K. (2006). Positive conceptions of perfectionism: Approaches, evidence, challenges. Personality and Social Psychology Review, 10(4), 295–319.",
 ],
})

# ---------------------------------------------------------------- 12
PRES.append({
 "name": "Self-esteem as a consequence of unidentified SLD",
 "neps": NEPS_31,
 "related_to": ["Specific Learning Disorder with impairment in reading (dyslexia)", "Specific Learning Disorder with impairment in written expression (dysgraphia)", "Specific Learning Disorder with impairment in mathematics (dyscalculia)", "Developmental Language Disorder (DLD)", "Major Depressive Disorder"],
 "what_it_is": [
  "Low self-esteem or academic self-concept that has DEVELOPED because a specific learning difficulty went unrecognised: years of trying and failing without an explanation lead the pupil (and sometimes adults) to conclude they are 'stupid' or 'lazy'.",
  "Part D adds 'check the sequence': the formulation depends on WHICH CAME FIRST. If the learning difficulty preceded the emotional difficulty, the self-esteem problem is likely secondary, and addressing the learning need is central to addressing it.",
  "Burden (2008) reviewed the evidence and concluded dyslexia is not NECESSARILY associated with negative self-worth; it depends on how the difficulty is understood and supported. Humphrey and Mullins (2002) found children with dyslexia were more likely to attribute failure to low intelligence.",
  "Maughan et al. (2003) found an association between reading problems and depressed mood in boys — one reason to take the emotional consequences seriously.",
 ],
 "what_it_is_not": [
  "NOT a reason to treat the self-esteem first and the learning later. If the need is unidentified, the failure continues and so does the damage.",
  "NOT proof that a SLD is present. Low self-esteem has many causes; this presentation applies only once the learning profile has been assessed.",
  "NOT the inevitable outcome of an SLD. Many pupils with dyslexia have healthy self-esteem, especially with early identification, understanding and support (Burden, 2008).",
 ],
 "by_age": [
  "EARLY YEARS 0–5: not applicable in the usual sense — SLDs are not identified at this age. Part D (1.4 Early Years): 'do not assess for dyslexia at this age — describe the precursors.'",
  "SCHOOL AGE 6–12: the child notices they are behind peers by middle primary; comments like 'I'm thick', avoiding reading, disruptive behaviour to hide difficulty. Often the first point of identification.",
  "ADOLESCENT 13–16: years of unexplained difficulty; may present as disengagement, behaviour difficulty or anxiety. Late identification can bring relief ('so I'm not stupid') and anger ('why did no one notice?').",
  "YOUNG ADULT 17–26: identification in further or higher education; the explanation often reframes a lifetime of self-blame.",
  "SPECIAL SETTING: a pupil in a special class for another reason may have an unidentified SLD overlaid — check literacy and numeracy profiles against their cognitive profile.",
 ],
 "assess": [
  "ESTABLISH THE SEQUENCE: developmental and school history — when did literacy or maths concerns first appear (school records, standardised tests over years), and when did the emotional change appear?",
  "Assess the learning profile fully: WIAT-III UK, phonological processing (PhAB2), cognitive profile (WISC-V UK) as indicated.",
  "Self-concept by domain (Piers-Harris 3), attributions ('Why do you find reading hard?'), and mood screening (RCADS / MFQ).",
  "Pupil voice: 'What have you thought about why reading is hard?' — the pupil's own theory tells you how much damage has been done.",
 ],
 "recommendations": [
  "NAME IT: explaining the learning difficulty clearly and positively to the pupil is itself an intervention — 'your brain processes sounds in words differently; it's not about being clever'.",
  "TARGETED TEACHING for the SLD at School Support or School Support Plus level, with review; assistive technology and reasonable accommodations (including state exam arrangements via RACE at post-primary — check current SEC rules).",
  "REBUILD ATTRIBUTIONS: make progress visible; attribute success to effort and strategy; reframe past failure as 'the teaching didn't fit how you learn'.",
  "PROTECT STRENGTHS: ensure time in areas of strength is not replaced entirely by support sessions.",
  "CONTINUUM LEVEL: School Support to School Support Plus depending on severity.",
  "REFER if low mood persists after the learning need is addressed, or if there is self-harm (GP / Primary Care / CAMHS).",
 ],
 "explain_parent": [
  "'He's been working really hard for years and it hasn't worked, because the reading difficulty wasn't picked up. He decided that meant he wasn't clever. It doesn't — it means his brain needed a different kind of teaching.'",
  "'It's natural to feel guilty or angry that it wasn't spotted earlier. What matters now is he knows why, and the right support starts.'",
 ],
 "explain_teacher": [
  "'Her behaviour in English makes sense now — she's been hiding a reading difficulty. Getting the right support in place will probably help the behaviour more than a behaviour plan.'",
  "'Tell her explicitly that reading is hard because of how her brain processes sounds — not because she's not bright. She needs to hear it from you too.'",
 ],
 "explain_child": [
  "YOUNGER: 'Your brain is really good at lots of things, and reading is tricky for it. That's not because you're not smart. Lots of clever people find reading hard.'",
  "OLDER: 'You've been told — or told yourself — you're lazy or thick. The testing shows that isn't true. Your brain works differently with words, and there are ways around it.'",
  "ASK: 'What have you thought about why school work is hard? What do you think now?'",
 ],
 "red_flags": [
  "RED FLAG — hopelessness, self-harm or suicidal thoughts: same-day risk route.",
  "WATCH — anger at late identification directed at the school or parents: acknowledge it; it may need space in a feedback meeting.",
  "BOUNDARY — you describe the learning profile; any formal SLD label follows the NEPS / DSM-5-TR framework and your service's policy — check local practice.",
 ],
 "questions": [
  "Q: 'Why wasn't it picked up earlier?' A: 'Sometimes children compensate for years, or the difficulty looks like behaviour or not trying. What matters now is we know, and we can act.'",
  "Q: 'Will her confidence come back?' A: 'For many children it improves once they understand why and the support is right. We'll keep an eye on her mood as well.'",
  "Q: 'Should she see a counsellor?' A: 'If her mood doesn't lift once the learning support is in place, yes, and I'd help with that route. But first, she needs the learning need addressed.'",
 ],
 "supervision": [
  "Bring your sequencing evidence (school records, test history) and discuss how confident you can be about which came first.",
  "Discuss how to handle parents' guilt or anger at late identification in feedback.",
 ],
 "citations": [
  "Burden, R. (2008). Is dyslexia necessarily associated with negative feelings of self-worth? A review and implications for future research. Dyslexia, 14(3), 188–196.",
  "Humphrey, N., & Mullins, P. M. (2002). Personal constructs and attribution for academic success and failure in dyslexia. British Journal of Special Education, 29(4), 196–203.",
  "Maughan, B., Rowe, R., Loeber, R., & Stouthamer-Loeber, M. (2003). Reading problems and depressed mood. Journal of Abnormal Child Psychology, 31(2), 219–229.",
 ],
})

# ---------------------------------------------------------------- 13
PRES.append({
 "name": "School anxiety presentations (not a standalone diagnosis)",
 "neps": NEPS_32,
 "related_to": ["Separation Anxiety Disorder", "Social Anxiety Disorder (social phobia)", "Generalised Anxiety Disorder", "Specific Phobia", "Selective mutism", "Autism"],
 "what_it_is": [
  "An umbrella for anxiety that SHOWS AT SCHOOL — worry about school work, separation at the gate, fear of teachers or peers, distress in particular lessons, avoidance of school. Part D: 'Not a DSM diagnosis.' 'School anxiety' or 'school phobia' is not a diagnostic category.",
  "The EP describes WHAT the anxiety is about and WHEN it happens. Anxiety disorders (separation, social, generalised, specific phobia) are diagnosed by Primary Care Psychology or CAMHS — Part D routes: Primary Care (mild–moderate), CAMHS (severe), GP to rule out physical causes.",
  "Kearney and Silverman (1990) proposed that school refusal is maintained by one or more functions: avoiding school-related distress, escaping aversive social or evaluative situations, gaining attention, or pursuing tangible rewards outside school. The School Refusal Assessment Scale (revised: Kearney, 2002) assesses these.",
  "Anxiety and attendance travel together — Part D (Adolescent): 'school attendance data alongside — anxiety and EBSA travel together.'",
 ],
 "what_it_is_not": [
  "NOT truancy. Truancy usually involves concealment from parents and no marked anxiety; anxious non-attenders are usually at home with parents' knowledge.",
  "NOT a diagnosis to put in a report. Write 'anxiety presenting in school around X' — not 'school phobia'.",
  "NOT helped by long-term avoidance. Accommodations that remove the pupil from all anxiety-provoking situations can maintain the anxiety; graded, supported exposure is usually needed.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: separation at drop-off is the common presentation (Part D). Usually developmental; persistent or extreme distress may merit Primary Care referral rather than NEPS.",
  "SCHOOL AGE 6–12: tummy aches on school mornings, clinginess, tears at the door, worry about tests or specific teachers. Part D: RCADS parent and child · SCAS · pupil interview using drawing or scaling · observation at the anxious moment.",
  "ADOLESCENT 13–16: social and performance anxiety, exam worry, avoidance of particular classes, panic in crowded corridors. Part D: RCADS self-report · SCAS-A · Beck Youth Inventories · direct interview · attendance data.",
  "YOUNG ADULT 17–26: course and workplace anxiety; Part D: 'refer to adult mental health rather than hold.'",
  "SPECIAL SETTING: anxiety about the setting or transition out of it; staff report on where and when (Part D). In autistic pupils, check sensory and predictability triggers.",
 ],
 "assess": [
  "Map the anxiety: where, when, with whom, about what. Observe at the anxious moment, not a random one (Part D).",
  "RCADS (parent and child; self-report at adolescence) to describe anxiety types; SCAS or SCAS-A as alternatives — check versions and norms.",
  "Function: ask what the pupil avoids, what they get, and what happens at home on non-school days (Kearney & Silverman, 1990). Attendance pattern by day and lesson.",
  "Rule out: bullying, a learning need, a physical cause (GP), and events at home.",
 ],
 "recommendations": [
  "NAMED KEY ADULT and a morning meet-and-greet routine; a quiet safe base; predictable start to the day.",
  "GRADED EXPOSURE with support: small steps back into the feared situation, planned with the pupil, rather than avoidance.",
  "TEACH COPING SKILLS: recognising anxiety, breathing and grounding, challenging worries — in school where appropriate; school-delivered CBT-informed programmes may be available (check what is used locally).",
  "PARENT GUIDANCE: calm, confident and consistent responses in the morning; Creswell and Willetts (2019) give a parent-led CBT approach.",
  "CONTINUUM LEVEL: School Support; School Support Plus if attendance is falling and outside agencies are involved.",
  "REFER to Primary Care Psychology (mild–moderate) or CAMHS (severe) via GP; GP to rule out physical causes. DO NOT diagnose an anxiety disorder or advise on medication.",
 ],
 "explain_parent": [
  "'Her anxiety is real, and it's mostly about separating from you in the morning. It's not a diagnosis in itself — we're describing what's happening so we can plan.'",
  "'Keeping her at home makes tomorrow harder. We'll plan small steps with lots of support.'",
  "SIGNPOST: GP; Primary Care Psychology; CAMHS if severe. Creswell and Willetts (2019) for parents.",
 ],
 "explain_teacher": [
  "'The first ten minutes are the hardest. A familiar face at the door and a job to do helps him get through them.'",
  "'Please don't let him skip the lessons he's anxious about — let's plan small steps back in instead.'",
 ],
 "explain_child": [
  "YOUNGER: 'Worry is like an alarm in your body. Yours goes off at the school gate even though you're safe. We can help it calm down.'",
  "OLDER: 'Anxiety tries to protect you by telling you to avoid things. But the more you avoid, the bigger it gets. We'll take small steps together.'",
  "ASK: 'On a scale of 1 to 10, how worried are you at the gate? In class? At lunch?'",
 ],
 "red_flags": [
  "RED FLAG — self-harm, suicidal thoughts or panic attacks: same-day risk route; refer to CAMHS.",
  "RED FLAG — anxiety that could be a response to abuse, bullying or something at home: child protection route; Tusla as soon as practicable.",
  "WATCH — attendance falling rapidly: act early; long absences are harder to reverse.",
 ],
 "questions": [
  "Q: 'Does she have school phobia?' A: 'That's not a diagnosis. She has anxiety that shows at school, mostly around separating from you. If it's severe, the GP can refer to a service that can assess an anxiety disorder.'",
  "Q: 'Should we keep him home until he feels better?' A: 'Staying off usually makes it harder to return. Small, supported steps are better.'",
  "Q: 'Will he grow out of it?' A: 'Some children do, but anxiety often responds well to support, so it's worth acting now rather than waiting.'",
 ],
 "supervision": [
  "Bring cases where attendance is falling and discuss thresholds for referral to Primary Care or CAMHS.",
  "Reflect on how you balance the parent's distress with the need for graded exposure.",
 ],
 "citations": [
  "Creswell, C., & Willetts, L. (2019). Helping your child with fears and worries: A self-help guide for parents (2nd ed.). Robinson.",
  "Kearney, C. A. (2002). Identifying the function of school refusal behavior: A revision of the School Refusal Assessment Scale. Journal of Psychopathology and Behavioral Assessment, 24(4), 235–245.",
  "Kearney, C. A., & Silverman, W. K. (1990). A preliminary analysis of a functional model of assessment and treatment for school refusal behavior. Behavior Modification, 14(3), 340–366.",
 ],
})

# ---------------------------------------------------------------- 14
PRES.append({
 "name": "Test and exam anxiety",
 "neps": NEPS_32,
 "related_to": ["Generalised Anxiety Disorder", "Social Anxiety Disorder (social phobia)", "Panic Disorder", "Specific Learning Disorder with impairment in reading (dyslexia)", "ADHD"],
 "what_it_is": [
  "Anxiety specifically triggered by tests and exams — worry, physical symptoms and avoidance before and during assessment — that impairs performance below what the pupil knows.",
  "Zeidner (1998) describes test anxiety as having cognitive (worry), emotional (tension, physical arousal) and behavioural (avoidance, procrastination) components. Worry — not arousal — is most strongly related to poorer performance (Hembree, 1988).",
  "Attentional control theory (Eysenck et al., 2007) explains the mechanism: anxiety uses working memory and attention, leaving less capacity for the task.",
  "von der Embse et al. (2018) meta-analysis found test anxiety is negatively associated with performance across ages; Putwain (2008) discusses the construct in UK secondary schools. Irish state exams (Junior Cycle, Leaving Certificate) are the key pressure points.",
 ],
 "what_it_is_not": [
  "NOT the same as normal pre-exam nerves. Some arousal is typical and can help; test anxiety is when worry impairs performance or leads to avoidance.",
  "NOT always a sign of generalised anxiety — it can be specific. But check for broader anxiety.",
  "NOT a reason on its own for reasonable accommodations in state exams. Eligibility for RACE is decided by SEC rules — check current guidance before advising.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: not applicable — no formal testing.",
  "SCHOOL AGE 6–12: standardised tests (e.g., end-of-year), spelling tests, maths tables. Look for stomach aches on test days and a gap between class work and test results.",
  "ADOLESCENT 13–16: Junior Cycle and class tests; Christmas and summer exams. Avoidance, going blank, panic, and 'I know it but I can't write it'.",
  "YOUNG ADULT 17–26: Leaving Certificate, further and higher education exams; less likely a NEPS referral but may seek documentation.",
  "SPECIAL SETTING: formal testing is less common; watch for anxiety in assessment situations generally, including your own assessment.",
 ],
 "assess": [
  "Compare performance: class work vs test results; timed vs untimed; familiar vs new formats. A large gap suggests anxiety is involved.",
  "Interview: 'What happens in your head and body before and during a test?' Listen for worry thoughts ('I'll fail', 'everyone will know').",
  "RCADS self-report or Beck Youth Inventories-2 at adolescence to check for broader anxiety; test-specific scales exist — check availability and norms before using.",
  "Check for an underlying learning need, processing speed difficulty or attention difficulty — each can masquerade as test anxiety or add to it.",
 ],
 "recommendations": [
  "PREPARATION AND FAMILIARITY: practice under exam-like conditions, graded; familiarise the pupil with the exam hall and format.",
  "WORRY STRATEGIES: brief expressive writing about worries before a test has some evidence (Ramirez & Beilock, 2011); breathing and grounding techniques; challenging catastrophic thoughts.",
  "REDUCE PUBLIC PRESSURE: avoid announcing results publicly; emphasise learning over grades.",
  "ACCOMMODATIONS: consider school-based arrangements (separate room, rest breaks) for in-house exams; for state exams, check SEC/RACE eligibility carefully — anxiety alone may not qualify.",
  "CONTINUUM LEVEL: Classroom Support; School Support where it is significant and affecting outcomes.",
  "REFER if anxiety is broader or severe (GP / Primary Care Psychology / CAMHS).",
 ],
 "explain_parent": [
  "'He knows the work — his class results show that. But in exams, the worry takes up the space he needs to think. We're going to help him practise and manage the worry.'",
  "'Try not to add pressure by talking about results. Focus on effort and preparation.'",
 ],
 "explain_teacher": [
  "'She freezes in tests but her class work is strong. Practice under exam conditions, low stakes first, will help.'",
  "'A couple of minutes to write down her worries before a test might help — there's some evidence behind it.'",
 ],
 "explain_child": [
  "YOUNGER: 'Tests can make your tummy feel funny. That's your body getting ready. We can teach it to calm down.'",
  "OLDER: 'When you're anxious in an exam, the worry takes up space in your brain. There are ways to free up that space.'",
  "ASK: 'What goes through your head when you turn over the paper?'",
 ],
 "red_flags": [
  "RED FLAG — panic attacks, self-harm or suicidal ideation around exams: same-day risk route.",
  "WATCH — exam avoidance (missing exams, not submitting coursework): address early.",
  "WATCH — anxiety spreading beyond exams: consider referral.",
 ],
 "questions": [
  "Q: 'Can she get a separate room for the Leaving Cert?' A: 'That depends on SEC rules for reasonable accommodations. Anxiety alone may not qualify — the school's RACE coordinator will know current rules.'",
  "Q: 'Is it just nerves?' A: 'A bit of nerves is normal. When it stops him showing what he knows, it's worth addressing.'",
  "Q: 'Should he do more past papers?' A: 'Practice helps, but graded — start with low-stakes, build up. Too much at once can increase anxiety.'",
 ],
 "supervision": [
  "Discuss how to advise on RACE and SEC accommodations without overstepping — what evidence is needed and who decides.",
  "Reflect on your own experience of exams and how it affects your advice.",
 ],
 "citations": [
  "Eysenck, M. W., Derakshan, N., Santos, R., & Calvo, M. G. (2007). Anxiety and cognitive performance: Attentional control theory. Emotion, 7(2), 336–353.",
  "Hembree, R. (1988). Correlates, causes, effects, and treatment of test anxiety. Review of Educational Research, 58(1), 47–77.",
  "Putwain, D. W. (2008). Deconstructing test anxiety. Emotional and Behavioural Difficulties, 13(2), 141–155.",
  "Ramirez, G., & Beilock, S. L. (2011). Writing about testing worries boosts exam performance in the classroom. Science, 331(6014), 211–213.",
  "von der Embse, N., Jester, D., Roy, D., & Post, J. (2018). Test anxiety effects, predictors, and correlates: A 30-year meta-analytic review. Journal of Affective Disorders, 227, 483–493.",
 ],
})

# ---------------------------------------------------------------- 15
PRES.append({
 "name": "Performance anxiety in oral work",
 "neps": NEPS_32,
 "related_to": ["Social Anxiety Disorder (social phobia)", "Selective mutism", "Childhood-Onset Fluency Disorder (stuttering)", "Developmental Language Disorder (DLD)", "Autism"],
 "what_it_is": [
  "Anxiety specifically around speaking in front of others — reading aloud, answering questions, presentations, oral exams (including Irish and modern language orals) — that leads to avoidance, freezing, or physical symptoms.",
  "Clark and Wells (1995) describe a cognitive model of social anxiety: fear of negative evaluation, heightened self-focus (monitoring how one looks and sounds), and safety behaviours (speaking quietly, avoiding eye contact, rehearsing every word) that maintain the anxiety because the pupil never learns the feared outcome would not have happened. Rapee and Heimberg (1997) give a similar account centred on the imagined audience.",
  "Links to 'Participation in oral work and classroom talk' (Part D, 1.2) — the same observable behaviour can be language-driven or anxiety-driven. Distinguish them.",
  "Oral assessments are part of Junior Cycle (Classroom-Based Assessments) and Leaving Certificate languages; anxiety here has real consequences.",
 ],
 "what_it_is_not": [
  "NOT selective mutism — though it may overlap. Selective mutism is a consistent failure to speak in specific social situations despite speaking in others; it is diagnosed by clinical services. If the pupil does not speak at all in school, consider that route.",
  "NOT shyness alone. Shy pupils may be quiet but participate when asked; performance anxiety causes distress and avoidance that affects learning or assessment.",
  "NOT always anxiety. A language difficulty, stammer or word-finding difficulty can make speaking aloud hard — the anxiety may be secondary to that.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: reluctance to speak in groups is common; persistent silence in preschool while speaking at home needs Part D's 1.2 selective mutism route.",
  "SCHOOL AGE 6–12: reading aloud, answering in class, show-and-tell, school plays. Watch for tummy aches on days with oral tasks.",
  "ADOLESCENT 13–16: presentations, oral exams, Irish orals, group discussions. Fear of peer judgment peaks; avoidance can affect grades.",
  "YOUNG ADULT 17–26: presentations in college, job interviews; less likely a NEPS referral.",
  "SPECIAL SETTING: consider communication differences and AAC use; performance anxiety can present differently in pupils with social communication differences.",
 ],
 "assess": [
  "Observe in speaking and non-speaking situations: is the pupil fluent and relaxed in small groups or one-to-one, but anxious in front of the class?",
  "Rule out language (CELF-5 UK, SLT input), fluency and word-finding difficulties as primary causes.",
  "RCADS social anxiety subscale (parent and child) or self-report at adolescence.",
  "Interview: 'What goes through your mind when it's your turn to read aloud?' Listen for evaluation fears ('they'll laugh', 'I'll go red').",
 ],
 "recommendations": [
  "GRADED PARTICIPATION: start with low-exposure options (paired talk, small group, recorded presentation), building to larger audiences.",
  "PREPARE AND REHEARSE: give questions or reading passages in advance; allow rehearsal with a trusted adult.",
  "REDUCE SAFETY BEHAVIOURS GENTLY: encourage the pupil to try without them in small steps, with praise for trying.",
  "ASSESSMENT ACCOMMODATIONS: for school-based orals, consider alternative formats (recorded, smaller audience); for state exams, check SEC rules.",
  "CONTINUUM LEVEL: Classroom Support; School Support if it significantly affects participation or assessment.",
  "REFER if social anxiety is broader or selective mutism is suspected (GP / Primary Care / CAMHS; SLT if language or fluency involved).",
 ],
 "explain_parent": [
  "'She's anxious about speaking in front of the class — she worries people are judging her. We're going to start with small steps so she can build up.'",
  "'At home, let her practise reading aloud to you or recording herself. It builds confidence.'",
 ],
 "explain_teacher": [
  "'Please don't call on him cold. Tell him the question in advance, and let him answer to a partner first.'",
  "'Reading aloud in front of the class is the hardest thing for her right now. Can she read to you privately while we build up?'",
 ],
 "explain_child": [
  "YOUNGER: 'Some children feel scared talking in front of lots of people. We'll practise with just a few people first.'",
  "OLDER: 'When you're speaking, your brain is busy checking how you look and sound. That makes it harder. We'll practise so it gets easier.'",
  "ASK: 'Who is easiest to talk in front of? Who is hardest?'",
 ],
 "red_flags": [
  "RED FLAG — consistent silence in school despite speaking at home: consider selective mutism; refer to clinical services.",
  "WATCH — avoidance of school on days with oral tasks: address early.",
  "WATCH — anxiety spreading to other social situations: consider referral.",
 ],
 "questions": [
  "Q: 'Should we just excuse her from speaking?' A: 'Short-term, maybe. Long-term, avoidance makes it worse. Small, supported steps are better.'",
  "Q: 'Is it selective mutism?' A: 'She does speak in class in small groups, so it doesn't look like it. If she stopped speaking altogether in school, we'd look at that.'",
  "Q: 'Can he get an accommodation for the Irish oral?' A: 'For school orals, yes, we can adapt. For state exams, it depends on SEC rules — check with the school.'",
 ],
 "supervision": [
  "Discuss how to distinguish language-driven from anxiety-driven difficulty in oral work.",
  "Reflect on how you set up your own assessment so the speaking demands do not become the anxious event.",
 ],
 "citations": [
  "Clark, D. M., & Wells, A. (1995). A cognitive model of social phobia. In R. G. Heimberg, M. R. Liebowitz, D. A. Hope, & F. R. Schneier (Eds.), Social phobia: Diagnosis, assessment, and treatment (pp. 69–93). Guilford Press.",
  "Rapee, R. M., & Heimberg, R. G. (1997). A cognitive-behavioral model of anxiety in social phobia. Behaviour Research and Therapy, 35(8), 741–756.",
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). American Psychiatric Publishing.",
 ],
})

# ---------------------------------------------------------------- 16
PRES.append({
 "name": "Anticipatory anxiety about transitions",
 "neps": NEPS_32,
 "related_to": ["Separation Anxiety Disorder", "Generalised Anxiety Disorder", "Autism", "Specific Phobia", "ADHD"],
 "what_it_is": [
  "Worry that builds in the days, weeks or months BEFORE a change — starting school, moving class or teacher, primary to post-primary, a new special class, returning after a long absence, leaving school. The anxiety is about what is coming, not what is happening now.",
  "Characteristically: questions repeated about the change, sleep difficulty as the date approaches, clinginess, irritability, stomach aches, and a sudden deterioration in the term before a move that 'comes from nowhere' unless you look at the calendar.",
  "Evangelou et al. (2008) identified what makes primary to secondary transition successful for most pupils: new friendships and confidence, settling into routines, interest in school, and continuity of curriculum. The pupils most at risk were those with SEN and those with prior anxiety or bullying.",
  "In Ireland, Smyth (2016) drew on ESRI longitudinal research on post-primary students to argue that how first year is organised (induction, class allocation, support) shapes adjustment. The NCCA Education Passport carries information between primary and post-primary — check what it contains for this pupil.",
 ],
 "what_it_is_not": [
  "NOT the same as difficulty with moment-to-moment transitions between activities or classes — that sits under 2.1 in Part D ('Transitions between activities and between classes'). This presentation is about the approach of a larger change.",
  "NOT a reason to delay the transition by default. Holding a pupil back a year because of anxiety about moving rarely removes the anxiety; preparation usually does more.",
  "NOT only an autism presentation. Many pupils without any diagnosis become anxious before a move; autistic pupils may need more, and earlier, preparation because of intolerance of uncertainty (Boulter et al., 2014).",
 ],
 "by_age": [
  "EARLY YEARS 0–5: starting preschool or primary. Separation distress in the weeks before is common (Part D: separation at drop-off is the common presentation). Visits, photos and a named adult help.",
  "SCHOOL AGE 6–12: moving teacher or class in September; the move to post-primary in 6th class, often peaking between the offer of a place and the first weeks of first year.",
  "ADOLESCENT 13–16: moving into senior cycle, Transition Year, change of school, returning after a period of non-attendance. The return after the summer or midterm is a recurring pinch point.",
  "YOUNG ADULT 17–26: leaving school, starting further/higher education or work, moving from child to adult services. Part D: refer to adult mental health rather than hold.",
  "SPECIAL SETTING: Part D — 'anxiety about the setting or about transition out of it.' Leaving a special class or school for post-school options can be a major source of worry for pupils and parents alike.",
 ],
 "assess": [
  "TIMELINE: plot the pupil's behaviour and attendance against the school calendar and known upcoming changes. A rise before each holiday return or before the move is the signature.",
  "Ask the pupil what they imagine about the new setting: 'What do you think it will be like? What's the worst bit?' Often the fear is specific and fixable (getting lost, lockers, lunch, a rumour about a teacher).",
  "RCADS (parent and child) for separation, generalised and social anxiety components; check for intolerance of uncertainty in autistic pupils.",
  "Speak to the receiving setting: what induction they offer, who the contact is, whether information is passed on (Education Passport).",
 ],
 "recommendations": [
  "PREPARE EARLY AND CONCRETELY: extra visits, a photo book or video of the new setting, a map, the timetable, names and photos of key adults; practise the journey.",
  "A NAMED LINK PERSON in the receiving setting who meets the pupil before the move and on the first day.",
  "TRANSITION PLAN in the Student Support File, shared (with consent) with the receiving setting: triggers, what helps, strengths. Do not rely on the Education Passport alone for a pupil with significant needs.",
  "COUNTDOWN AND PREDICTABILITY: a visual countdown for younger or autistic pupils; for others, a planned conversation schedule rather than constant reassurance, which can maintain worry.",
  "CONTINUUM LEVEL: Classroom Support for most; School Support where anxiety is significant; School Support Plus where outside agencies are involved.",
  "REFER if anxiety is severe, persistent after the transition, or accompanied by self-harm (Primary Care / CAMHS via GP).",
 ],
 "explain_parent": [
  "'The closer it gets to September, the more his worry grows — that's anticipatory anxiety. It usually settles once he's there and knows what it's like, so the plan is to make the new school as familiar as possible before he starts.'",
  "'Answering the same question over and over can keep the worry going. Agree a time each evening to talk about the move, and gently hold to it.'",
 ],
 "explain_teacher": [
  "'The behaviour change in May lines up with the move to secondary, not with anything in your room. Her worry about next year is spilling into this one.'",
  "'Could you give her an extra visit and let her meet her year head before June? Specific information shrinks the worry.'",
 ],
 "explain_child": [
  "YOUNGER: 'New things can feel scary before they happen. Let's look at pictures of your new classroom so your brain knows what to expect.'",
  "OLDER: 'Worrying before something new is really normal. What's the one thing you're most worried about? Let's find out the real answer.'",
  "ASK: 'What would you want to know about the new school that nobody has told you yet?'",
 ],
 "red_flags": [
  "RED FLAG — self-harm, suicidal talk or refusal to attend linked to the upcoming change: same-day risk route.",
  "WATCH — anxiety that does not settle within the first half-term after the transition: reassess; consider bullying, a learning need, or a broader anxiety difficulty.",
  "WATCH — a pupil for whom transition means losing a key relationship (SNA, teacher): plan the ending explicitly.",
 ],
 "questions": [
  "Q: 'Should we hold him back a year?' A: 'Usually the anxiety moves with him. Good preparation and a named person in the new school tend to help more.'",
  "Q: 'She keeps asking the same questions — should I keep answering?' A: 'Answer them properly once, write the answers down, then gently point to the list. Constant reassurance can keep the worry going.'",
  "Q: 'Will it get better once he's there?' A: 'For most children, yes, within the first few weeks. We'll check in after midterm to be sure.'",
 ],
 "supervision": [
  "Discuss how to write a transition plan that is useful to a receiving school, and what information needs consent to share.",
  "Reflect on cases where a transition was delayed — was the outcome what was hoped?",
 ],
 "citations": [
  "Boulter, C., Freeston, M., South, M., & Rodgers, J. (2014). Intolerance of uncertainty as a framework for understanding anxiety in children and adolescents with autism spectrum disorders. Journal of Autism and Developmental Disorders, 44(6), 1391–1402.",
  "Evangelou, M., Taggart, B., Sylva, K., Melhuish, E., Sammons, P., & Siraj-Blatchford, I. (2008). What makes a successful transition from primary to secondary school? (Research Report DCSF-RR019). Department for Children, Schools and Families.",
  "Smyth, E. (2016). Students' experiences and perspectives on secondary education: Institutions, transitions and policy. Palgrave Macmillan.",
 ],
})

# ---------------------------------------------------------------- 17
PRES.append({
 "name": "Somatic complaints presenting at school (tummy aches, headaches)",
 "neps": NEPS_32,
 "related_to": ["Somatic Symptom Disorder / Illness Anxiety / Conversion Disorder", "Separation Anxiety Disorder", "Generalised Anxiety Disorder", "Major Depressive Disorder", "Specific Learning Disorder with impairment in reading (dyslexia)"],
 "what_it_is": [
  "Physical complaints — tummy aches, headaches, nausea, tiredness, feeling faint — that recur at school, often on particular days or before particular lessons, and lead to visits to the office, calls home or missed school.",
  "Egger et al. (1999) found that stomach aches, headaches and musculoskeletal pains in children and adolescents were associated with anxiety and depressive disorders — the body is often where young children first show emotional distress.",
  "Functional abdominal pain (no identified organic cause) is common in childhood and is recognised in the Rome IV criteria for paediatric functional gastrointestinal disorders (Hyams et al., 2016) — diagnosed by a doctor, not by the EP.",
  "The pain is REAL. 'Functional' or 'anxiety-related' does not mean imagined; the brain and gut are closely linked, and worry can produce genuine pain.",
 ],
 "what_it_is_not": [
  "NOT something the EP can attribute to anxiety without medical review. Part D's route includes 'GP to rule out' — a physical cause must be excluded by a doctor first (coeliac disease, migraine, constipation, infections and others).",
  "NOT 'faking' or 'putting it on'. Suggesting a child is lying about pain damages trust and does not reduce the symptom.",
  "NOT to be confused with Somatic Symptom Disorder, which is a clinical diagnosis for persistent, distressing symptoms with excessive thoughts and behaviours about them — diagnosed by CAMHS or paediatrics.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: tummy aches at drop-off, often linked to separation; wetting or soiling may also appear under stress (elimination disorders sit with medical services).",
  "SCHOOL AGE 6–12: the classic presentation — Monday-morning tummy aches, headaches before tests, repeated trips to the office. Map it against the timetable.",
  "ADOLESCENT 13–16: headaches, fatigue, nausea, fainting; may link to exams, social worry, bullying, low mood, sleep or disordered eating. Watch for patterns of leaving school early.",
  "YOUNG ADULT 17–26: headaches and fatigue linked to course or work stress; GP-led.",
  "SPECIAL SETTING: pupils with limited verbal communication may show pain through behaviour (hitting the head, holding the stomach, withdrawal). Always check for a medical cause first — pain is under-recognised in this group.",
 ],
 "assess": [
  "CONFIRM MEDICAL REVIEW: ask the parent whether the GP has seen the child for these symptoms and what was found. If not, recommend it before any psychological formulation.",
  "PATTERN MAP: from office records, list each complaint by day, time, lesson and what happened next (sent home, rested, returned). Is it Monday, maths, PE, lunchtime, a particular teacher?",
  "Pupil interview using a body map: 'Where do you feel it? When does it come? What makes it better?' Then 'What else is going on at those times?'",
  "RCADS (parent and child) and check for bullying, a learning need in the triggering lessons, and events at home.",
 ],
 "recommendations": [
  "MEDICAL REVIEW FIRST via the GP; the school follows any medical advice about the specific symptom.",
  "A CONSISTENT RESPONSE PLAN: brief, kind attention; a short rest in a quiet place with a time limit; return to class as the default rather than going home — agreed with parents and GP.",
  "ADDRESS THE TRIGGER: if pain clusters around a lesson or time, look at what is hard there (learning demand, peers, test) and adjust.",
  "TEACH BODY-MIND LINK and coping: simple explanations of how worry affects the tummy; breathing and relaxation strategies.",
  "CONTINUUM LEVEL: Classroom Support to School Support, with the plan recorded in the Student Support File and reviewed with parents.",
  "REFER: GP for medical review; Primary Care Psychology or CAMHS if anxiety or low mood is significant. DO NOT tell a parent the pain is 'just anxiety' before medical review.",
 ],
 "explain_parent": [
  "'The pain is real — I'm not saying she's making it up. Worry can cause real tummy pain. It's important the GP checks her first, so we know nothing physical is being missed.'",
  "'If the GP is happy, the plan is to help her manage the pain at school and look at what's worrying her, rather than coming home each time — coming home can make the next morning harder.'",
 ],
 "explain_teacher": [
  "'His headaches are nearly always before Irish. It might be worth looking at what's hard for him there.'",
  "'Please don't say he's putting it on. Ten minutes in the quiet room, then back to class, is the agreed plan.'",
 ],
 "explain_child": [
  "YOUNGER: 'Sometimes when we're worried, our tummy hurts. That's real. Let's find out what might be worrying your tummy.'",
  "OLDER: 'Your body and brain are connected. Stress can cause real headaches. Let's look at when they happen and what might help.'",
  "ASK: 'If your tummy ache could talk, what would it say?'",
 ],
 "red_flags": [
  "RED FLAG — weight loss, vomiting, night waking with pain, blood, fever, severe or worsening headaches: urgent GP review — these are medical warning signs, not EP territory.",
  "RED FLAG — somatic complaints alongside disclosures or signs of abuse, or fear of going home: child protection route; Tusla.",
  "WATCH — increasing absence due to symptoms: act early; long absences reinforce the cycle.",
 ],
 "questions": [
  "Q: 'Is she making it up?' A: 'No. Worry can cause real pain. The GP needs to check first, then we'll look at what might be worrying her.'",
  "Q: 'Should I keep him home when he's sick?' A: 'Follow the GP's advice on genuine illness. If the GP is satisfied there's no medical cause, going home usually makes it harder to go back.'",
  "Q: 'Is this a diagnosis?' A: 'No — I'm describing what's happening. If the pain is very persistent, the GP may refer to a paediatrician.'",
 ],
 "supervision": [
  "Discuss how you raise the anxiety hypothesis with a parent who is convinced there is a medical cause — and how you keep medical review in place.",
  "Bring cases where the pattern map was striking and discuss what to recommend at school level.",
 ],
 "citations": [
  "Egger, H. L., Costello, E. J., Erkanli, A., & Angold, A. (1999). Somatic complaints and psychopathology in children and adolescents: Stomach aches, musculoskeletal pains, and headaches. Journal of the American Academy of Child & Adolescent Psychiatry, 38(7), 852–860.",
  "Hyams, J. S., Di Lorenzo, C., Saps, M., Shulman, R. J., Staiano, A., & van Tilburg, M. (2016). Functional disorders: Children and adolescents. Gastroenterology, 150(6), 1456–1468.",
  "Campo, J. V., & Fritsch, S. L. (1994). Somatization in children and adolescents. Journal of the American Academy of Child & Adolescent Psychiatry, 33(9), 1223–1235.",
 ],
})

# ---------------------------------------------------------------- 18
PRES.append({
 "name": "Anxiety secondary to an unmet learning need",
 "neps": NEPS_32,
 "related_to": ["Specific Learning Disorder with impairment in reading (dyslexia)", "Specific Learning Disorder with impairment in mathematics (dyscalculia)", "Developmental Language Disorder (DLD)", "ADHD", "Generalised Anxiety Disorder"],
 "what_it_is": [
  "Anxiety that ARISES FROM an unrecognised or unsupported learning difficulty: the pupil is anxious because the work is persistently too hard, failure is public, and they cannot explain why. Remove or support the learning need and the anxiety often reduces.",
  "Nelson and Harwood (2011) meta-analysis found students with learning disabilities had higher anxiety than peers — rate not stated here, check the paper before quoting a figure.",
  "Typical signature: anxiety concentrated in specific lessons (English, Irish, maths), on specific tasks (reading aloud, tests, copying from the board) and less or absent elsewhere (sport, art, practical subjects).",
  "Part D's parallel item under Behaviour — 'Behaviour as communication of an unmet learning need — always test this hypothesis' — applies equally here: always test whether a learning need sits beneath the anxiety.",
 ],
 "what_it_is_not": [
  "NOT a primary anxiety disorder to be referred straight to CAMHS. If the anxiety is secondary, the priority is assessing and supporting the learning need.",
  "NOT the same as 'Self-esteem as a consequence of unidentified SLD', though they often co-occur: this item concerns worry, fear and avoidance; that one concerns how the pupil values themselves.",
  "NOT excluded by a pupil being 'bright'. Twice-exceptional pupils may mask a learning difficulty for years, with anxiety the only visible sign.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: rarely identified this way; watch for distress around early literacy or number activities alongside language delay.",
  "SCHOOL AGE 6–12: anxiety in literacy or maths lessons, avoidance of reading aloud, stomach aches before spelling tests. Often picked up when the gap with peers widens in middle primary.",
  "ADOLESCENT 13–16: anxiety about subjects, exams and homework; avoidance of classes; can escalate into attendance difficulty (EBSA). Many subjects with heavy reading load amplify it.",
  "YOUNG ADULT 17–26: late identification in further/higher education; anxiety about reading-heavy courses.",
  "SPECIAL SETTING: check whether the curriculum is pitched at the right level; anxiety may be the sign of a mismatch.",
 ],
 "assess": [
  "MAP ANXIETY TO TASKS: which lessons and tasks trigger it and which don't. A clear link to literacy or maths demand is the key finding.",
  "Assess the learning profile: WIAT-III UK, phonological processing (PhAB2), language (CELF-5 UK or SLT), cognitive profile (WISC-V UK) as indicated.",
  "RCADS to describe the anxiety pattern; compare with attainment and history.",
  "History: when did anxiety appear relative to the learning difficulty? (See 'check the sequence' in the self-esteem item.)",
 ],
 "recommendations": [
  "TREAT THE LEARNING NEED: targeted intervention for the literacy, maths or language need at School Support or School Support Plus level.",
  "REDUCE ANXIETY-PROVOKING DEMANDS while skills build: no cold reading aloud; alternative ways to record work; assistive technology; extra time for tests.",
  "EXPLAIN IT TO THE PUPIL: understanding why the work is hard reduces anxiety about it.",
  "MONITOR BOTH: review both learning progress and anxiety at the plan review. If anxiety persists after the learning need is supported, reconsider the formulation.",
  "CONTINUUM LEVEL: School Support to School Support Plus.",
  "REFER for anxiety only if it persists after the learning need is addressed or is severe (GP / Primary Care / CAMHS).",
 ],
 "explain_parent": [
  "'His anxiety makes sense — he's been struggling with reading and not knowing why. When the reading support is in place, I expect the anxiety to ease. We'll check that it does.'",
  "'The anxiety is real, but the root is the reading. That's where we're starting.'",
 ],
 "explain_teacher": [
  "'Her anxiety is almost entirely in English and Irish — where the reading load is. In PE and art she's fine. That points to the reading, not a general anxiety.'",
  "'While the reading support gets going, please don't ask her to read aloud cold. Give her the passage in advance.'",
 ],
 "explain_child": [
  "YOUNGER: 'Reading is tricky for your brain, and that makes you worried in class. We're going to help with the reading, and that should help the worry too.'",
  "OLDER: 'It makes sense you're anxious in English — the work has been harder for you than for others, and nobody explained why. Now we know, and we can do something.'",
  "ASK: 'Which lessons do you feel most worried in? Which do you feel OK in?'",
 ],
 "red_flags": [
  "RED FLAG — self-harm or suicidal ideation: same-day risk route.",
  "WATCH — anxiety leading to non-attendance: act quickly with both learning and attendance support.",
  "WATCH — anxiety persisting after the learning need is supported: reconsider the formulation; refer if needed.",
 ],
 "questions": [
  "Q: 'Should she see a counsellor for the anxiety?' A: 'The anxiety seems to be coming from the reading difficulty. Let's put reading support in first and see if the anxiety lifts. If it doesn't, we'll look at counselling or a referral.'",
  "Q: 'Is it anxiety or dyslexia?' A: 'It looks like both — the reading difficulty is causing the anxiety. Treating the reading is the first step.'",
  "Q: 'Why is he anxious in some lessons and not others?' A: 'The lessons he's anxious in are the ones with lots of reading. That's the clue.'",
 ],
 "supervision": [
  "Discuss how confident you can be that anxiety is secondary, and what evidence would change your mind.",
  "Plan the review: what would tell you the formulation is right (anxiety falling as skills rise)?",
 ],
 "citations": [
  "Nelson, J. M., & Harwood, H. (2011). Learning disabilities and anxiety: A meta-analysis. Journal of Learning Disabilities, 44(1), 3–17.",
  "Maughan, B., Rowe, R., Loeber, R., & Stouthamer-Loeber, M. (2003). Reading problems and depressed mood. Journal of Abnormal Child Psychology, 31(2), 219–229.",
 ],
})

# ---------------------------------------------------------------- 19
PRES.append({
 "name": "Rigidity and routine that is not OCD",
 "neps": NEPS_33,
 "related_to": ["Autism", "Obsessive-Compulsive Disorder", "Generalised Anxiety Disorder", "ADHD", "Foetal Alcohol Spectrum Disorder"],
 "what_it_is": [
  "A strong need for sameness, routine or rules — distress when plans change, insistence on doing things a particular way, difficulty switching tasks — that is NOT driven by the intrusive thoughts and neutralising compulsions of OCD.",
  "Part D: 'check autism first.' Insistence on sameness and restricted, repetitive behaviours are part of the autism diagnostic criteria (DSM-5-TR). Leekam, Prior and Uljarevic (2011) review restricted and repetitive behaviours in autism.",
  "Evans et al. (1997) found ritualistic and 'just right' behaviours are common and developmentally normal in young children, peaking around ages 2–4. Part D (Early Years): 'routines are developmentally normal here.'",
  "Rigidity can also reflect anxiety and intolerance of uncertainty (Boulter et al., 2014): routine reduces unpredictability. Rodgers et al. (2012) found anxiety and repetitive behaviour linked in autistic children.",
 ],
 "what_it_is_not": [
  "NOT OCD. In OCD, compulsions are performed to reduce anxiety from intrusive, unwanted thoughts, and the person often recognises them as excessive. Autistic routines are often experienced as comforting or preferred, not unwanted (Part D, Special Setting: 'Distinguish autistic routine from compulsion — the function differs').",
  "NOT stubbornness or defiance. Distress at change is usually genuine and linked to predictability, anxiety or cognitive flexibility.",
  "NOT to be removed by force. Rigid behaviour often serves a regulating function; removing it without addressing the need increases distress.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: routines and 'just right' behaviours are developmentally normal (Evans et al., 1997). Intense distress at change alongside social communication differences may warrant a developmental review (CDNT).",
  "SCHOOL AGE 6–12: distress at a substitute teacher, change of timetable, a different route; insistence on rules; difficulty with open-ended tasks. Part D: describe school impact and refer.",
  "ADOLESCENT 13–16: rigidity about timetables, subject rules, moral rules; difficulty with the many changes in post-primary. May increase with stress.",
  "YOUNG ADULT 17–26: rigidity in work or study routines; adult services.",
  "SPECIAL SETTING: Part D — 'Distinguish autistic routine from compulsion — the function differs.' Functional behaviour assessment helps identify the function.",
 ],
 "assess": [
  "FUNCTION: ask 'What happens if the routine is broken? How does it feel?' Comfort and predictability suggest autistic routine or anxiety; intrusive unwanted thoughts and neutralising suggest OCD.",
  "Check the social communication profile — SRS-2, SCQ, developmental history — and whether an autism assessment has been considered (CDNT or CAMHS depending on area).",
  "Functional behaviour assessment (ABC) around changes: what precedes distress, what reduces it.",
  "RCADS for anxiety; parent and teacher report on flexibility (e.g., BRIEF-2 Shift scale).",
 ],
 "recommendations": [
  "PREDICTABILITY: visual timetables, advance warning of changes, 'change cards' or 'surprise' symbols to prepare for the unexpected.",
  "GRADED FLEXIBILITY: small planned changes in low-stakes situations, with support and praise, building tolerance gradually.",
  "RESPECT FUNCTION: allow routines that are regulating and harmless; focus change efforts only where rigidity impairs learning or wellbeing.",
  "TRANSITIONS: plan for known changes (substitute teachers, trips, timetable changes) and give information in advance.",
  "CONTINUUM LEVEL: Classroom Support; School Support where rigidity significantly affects learning or participation.",
  "REFER: autism assessment via CDNT or CAMHS as locally appropriate; Primary Care / CAMHS if OCD is suspected. DO NOT diagnose autism or OCD.",
 ],
 "explain_parent": [
  "'His need for routine isn't OCD — it's about feeling safe when things are predictable. That's often linked with how autistic children experience the world, so it's worth exploring an autism assessment.'",
  "'We'll help him cope with small changes, step by step, while respecting the routines that help him feel calm.'",
 ],
 "explain_teacher": [
  "'He's not being difficult when he gets upset about the substitute — the change is genuinely distressing. A heads-up the day before makes a big difference.'",
  "'Let him keep his routines where they don't get in the way. Pick your battles to the ones that affect learning.'",
 ],
 "explain_child": [
  "YOUNGER: 'You like things to be the same — that makes you feel safe. Sometimes things change, and we'll help you know what's happening.'",
  "OLDER: 'Some people's brains like routine and find change hard. That's OK. We can find ways to make changes less stressful.'",
  "ASK: 'What happens in your head when plans change suddenly?'",
 ],
 "red_flags": [
  "WATCH — distress so severe it leads to meltdowns, self-injury or school avoidance: plan urgently; refer as needed.",
  "WATCH — rituals that seem driven by intrusive thoughts or 'bad things will happen' fears: consider OCD; refer via GP.",
  "BOUNDARY — do not diagnose autism or OCD; describe and refer.",
 ],
 "questions": [
  "Q: 'Is it OCD?' A: 'From what I've seen, it looks more like needing predictability than OCD. OCD usually involves unwanted thoughts that the rituals try to cancel out. If you notice that, tell the GP.'",
  "Q: 'Should we stop his routines?' A: 'Only where they get in the way. Many routines help him feel calm, so we'll work gently on flexibility where it matters.'",
  "Q: 'Is he autistic?' A: 'Rigidity is one of the things that can go with autism, but it's not enough on its own. An assessment would look at the whole picture.'",
 ],
 "supervision": [
  "Discuss the distinction between autistic routine, anxiety-driven rigidity and OCD — and how you would evidence each.",
  "Reflect on local routes for autism assessment and waiting times.",
 ],
 "citations": [
  "Evans, D. W., Leckman, J. F., Carter, A., Reznick, J. S., Henshaw, D., King, R. A., & Pauls, D. (1997). Ritual, habit, and perfectionism: The prevalence and development of compulsive-like behavior in normal young children. Child Development, 68(1), 58–68.",
  "Leekam, S. R., Prior, M. R., & Uljarevic, M. (2011). Restricted and repetitive behaviors in autism spectrum disorders: A review of research in the last decade. Psychological Bulletin, 137(4), 562–593.",
  "Boulter, C., Freeston, M., South, M., & Rodgers, J. (2014). Intolerance of uncertainty as a framework for understanding anxiety in children and adolescents with autism spectrum disorders. Journal of Autism and Developmental Disorders, 44(6), 1391–1402.",
  "Rodgers, J., Glod, M., Connolly, B., & McConachie, H. (2012). The relationship between anxiety and repetitive behaviours in autism spectrum disorder. Journal of Autism and Developmental Disorders, 42(11), 2404–2409.",
 ],
})

# ---------------------------------------------------------------- 20
PRES.append({
 "name": "Repeated checking of work",
 "neps": NEPS_33,
 "related_to": ["Obsessive-Compulsive Disorder", "Generalised Anxiety Disorder", "Autism", "ADHD", "Specific Learning Disorder with impairment in reading (dyslexia)"],
 "what_it_is": [
  "A pupil who checks, re-reads, re-does or rubs out work repeatedly — checking the same answer many times, re-reading instructions, asking the teacher 'Is this right?' again and again — to the point where it slows or stops work.",
  "Salkovskis (1985) and Rachman (2002) give cognitive accounts: checking is driven by an inflated sense of responsibility for preventing harm or error, and it is maintained because it briefly reduces anxiety.",
  "van den Hout and Kindt (2003) showed experimentally that repeated checking INCREASES memory distrust — the more you check, the less sure you feel — which keeps the cycle going.",
  "Can be part of OCD, perfectionism, generalised anxiety, or a reasonable strategy for a pupil with a learning difficulty who genuinely makes more errors. The function decides which.",
 ],
 "what_it_is_not": [
  "NOT always OCD. A pupil with dyslexia checking spelling, or a pupil with ADHD taught to check work, may be using a reasonable strategy. The question is whether it is excessive, distressing and hard to stop.",
  "NOT helped by reassurance. Answering 'Yes, that's right' every time maintains the checking; reassurance-seeking is itself a form of checking.",
  "NOT to be ignored when it slows work drastically — incomplete work can be misread as laziness or low ability.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: rarely seen; asking repeatedly for reassurance is common and usually developmental.",
  "SCHOOL AGE 6–12: re-reading, rubbing out, asking 'Is this right?' repeatedly; very slow work. Part D (School Age, 3.3): parent and teacher report; describe school impact and refer.",
  "ADOLESCENT 13–16: checking exam answers repeatedly and running out of time; re-reading notes; checking locks, bags, emails. Part D: describe impact on work completion and attendance.",
  "YOUNG ADULT 17–26: checking at work or in study; adult services.",
  "SPECIAL SETTING: distinguish autistic routine (preferred, comforting) from compulsion (unwanted, anxiety-reducing) — Part D.",
 ],
 "assess": [
  "Observe and count: how often does the pupil check, re-do or ask for reassurance in a task? How long does it add?",
  "Interview: 'What would happen if you didn't check? How do you feel if you stop yourself?' Intense anxiety and feared consequences suggest OCD; mild discomfort suggests habit or strategy.",
  "Check the learning profile — if the pupil genuinely makes many errors, checking may be reasonable.",
  "RCADS OCD subscale (parent and child); if OCD is suspected, the CY-BOCS is administered by clinical services, not NEPS (Part D).",
 ],
 "recommendations": [
  "LIMIT CHECKING GENTLY: agree one check per task, or a checklist to use once; praise stopping.",
  "REDUCE REASSURANCE: teachers answer once, then refer to the agreed checklist or say 'You've checked — trust it.'",
  "TIME SUPPORT: in tests, a strategy for moving on and returning ('mark it, move on, come back once'); weigh extra time carefully, as it may simply give more room to check.",
  "PROVIDE STRATEGIES where there is a genuine learning need (spell-checkers, structured proof-reading).",
  "CONTINUUM LEVEL: Classroom Support; School Support where checking significantly affects work.",
  "REFER if OCD is suspected — via GP to Primary Care Psychology or CAMHS. NICE (2005) recommends CBT including exposure and response prevention for OCD in young people, delivered by clinical services. DO NOT attempt exposure-response prevention yourself.",
 ],
 "explain_parent": [
  "'She checks her work many times because she worries it isn't right. The checking makes her feel better for a moment, but then she doubts again. We want to help her trust her first check.'",
  "'When she asks \"Is this right?\" again and again, answer once, then gently say \"You've checked.\" Reassurance keeps the checking going.'",
 ],
 "explain_teacher": [
  "'He's not slow — he's checking each answer many times. One agreed check per question will help him get more done.'",
  "'When he asks for reassurance, answer once and then point to his checklist.'",
  "'If his work comes back with holes rubbed in the page, that is the checking, not carelessness. Record how long each task takes so we can see whether the plan is working.'",
 ],
 "explain_child": [
  "YOUNGER: 'Checking once is good. Checking again and again can make your worry bigger. Let's practise checking once and trusting it.'",
  "OLDER: 'The more you check, the less sure you feel — research shows that. Let's try one check and see what happens.'",
  "ASK: 'What would happen if you only checked once?'",
 ],
 "red_flags": [
  "WATCH — checking extending beyond school work (locks, doors, safety) with distress: consider OCD; refer via GP.",
  "WATCH — checking so time-consuming that work is never finished: address promptly.",
  "BOUNDARY — do not diagnose OCD or deliver exposure-response prevention; describe and refer.",
 ],
 "questions": [
  "Q: 'Is it OCD?' A: 'It might be part of OCD, or of anxiety or perfectionism. If it's causing a lot of distress, the GP can refer for an assessment.'",
  "Q: 'Should I keep reassuring her?' A: 'Reassurance helps for a moment but keeps the checking going. Answer once, then encourage her to trust herself.'",
  "Q: 'Should he get extra time in exams?' A: 'Possibly — but extra time can also give more room for checking rather than answering. Decide with the school's RACE coordinator, and with clinical advice if he is attending a service.'",
 ],
 "supervision": [
  "Discuss the line between supporting checking at school and needing a clinical OCD referral.",
  "Reflect on how to explain reassurance-seeking to teachers and parents without it sounding unkind — and notice whether you gave reassurance yourself during testing.",
 ],
 "citations": [
  "National Institute for Health and Care Excellence. (2005). Obsessive-compulsive disorder and body dysmorphic disorder: Treatment (Clinical Guideline CG31). NICE. (Check for updates.)",
  "Rachman, S. (2002). A cognitive theory of compulsive checking. Behaviour Research and Therapy, 40(6), 625–639.",
  "Salkovskis, P. M. (1985). Obsessional-compulsive problems: A cognitive-behavioural analysis. Behaviour Research and Therapy, 23(5), 571–583.",
  "van den Hout, M., & Kindt, M. (2003). Repeated checking causes memory distrust. Behaviour Research and Therapy, 41(3), 301–316.",
 ],
})
