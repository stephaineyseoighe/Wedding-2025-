# CONDS batch c05 — disruptive behaviour and mood-dysregulation diagnoses.
# 1 Oppositional Defiant Disorder · 2 Conduct Disorder · 3 Disruptive Mood Dysregulation Disorder
# Context: Reference Part D, 2. BEHAVIOUR (2.1 / 2.2) and 3. EMOTIONAL (3.4 Mood), all bands.
# Stance throughout: formulate before labelling. The EP does not diagnose (PSI 2.2.2).

NEPS_BEH = "2. BEHAVIOUR (2.1 Behaviour in class · 2.2 Behaviour during break times and around the school)"
CORU = "3.1 · 3.2 · 3.4 · 3.10 · 3.12 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32 · 5.34"
PSI = "2.2.2 · 2.2.4 · 2.3.1 · 1.3.1 · 1.2.8 · 1.1.4"
LAW = ("Children First Act 2015 · Children First National Guidance (2017) · EPSEN Act 2004 · "
       "Education Act 1998 (s.29 appeals) · Education (Welfare) Act 2000 · Equal Status Acts 2000–2018 · "
       "Children Act 2001 · GDPR / Data Protection Act 2018")

CIT_DSM = ("American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders "
           "(5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787")
CIT_NICE = ("National Institute for Health and Care Excellence. (2013, updated 2017). Antisocial behaviour and "
            "conduct disorders in children and young people: Recognition and management (Clinical Guideline "
            "CG158). NICE. [Check nice.org.uk for updates before quoting.]")
CIT_HOLLO = ("Hollo, A., Wehby, J. H., & Oliver, R. M. (2014). Unidentified language deficits in children with "
             "emotional and behavioral disorders: A meta-analysis. Exceptional Children, 80(2), 169–186.")
CIT_NEPS = ("National Educational Psychological Service. (2010). Behavioural, emotional and social difficulties: "
            "A continuum of support — Guidelines for teachers. Department of Education and Skills.")
CIT_IFF = ("Frederickson, N., & Cline, T. (2015). Special educational needs, inclusion and diversity (3rd ed.). "
           "Open University Press.")
CIT_MCG = ("McGilloway, S., Ní Mháille, G., Bywater, T., Furlong, M., Leckey, Y., Kelly, P., Comiskey, C., & "
           "Donnelly, M. (2012). A parenting intervention for childhood behavioral problems: A randomized "
           "controlled trial in disadvantaged community-based settings. Journal of Consulting and Clinical "
           "Psychology, 80(1), 116–127.")
CIT_POL15 = ("Polanczyk, G. V., Salum, G. A., Sugaya, L. S., Caye, A., & Rohde, L. A. (2015). Annual research "
             "review: A meta-analysis of the worldwide prevalence of mental disorders in children and "
             "adolescents. Journal of Child Psychology and Psychiatry, 56(3), 345–365.")
CIT_STR09 = ("Stringaris, A., & Goodman, R. (2009). Three dimensions of oppositionality in youth. Journal of Child "
             "Psychology and Psychiatry, 50(3), 216–223.")
CIT_GREENE = "Greene, R. W. (2014). The explosive child (5th ed.). Harper. [Check for the current edition.]"

EP_REPORT = ("Psychological report — formulation first, diagnosis (if any) reported as someone else's finding, "
             "with its source and date")

CONDS = []

# ============================================================================ 1 · ODD
CONDS.append({
 "name": "Oppositional Defiant Disorder (ODD)",
 "code": "DSM-5-TR Oppositional Defiant Disorder (ICD-10-CM F91.3) · ICD-11 6C90 Oppositional defiant disorder (qualifier: with / without chronic irritability-anger — check subcodes before quoting)",
 "neps": NEPS_BEH + " — and 3. EMOTIONAL (3.4 Mood) where irritability dominates",
 "coru": CORU,
 "psi": PSI,
 "law": LAW,

 "what_it_is": [
  "A DSM-5-TR diagnosis in the 'Disruptive, Impulse-Control, and Conduct Disorders' chapter: a frequent, persistent pattern of ANGRY/IRRITABLE MOOD, ARGUMENTATIVE/DEFIANT BEHAVIOUR, or VINDICTIVENESS lasting at least six months (American Psychiatric Association [APA], 2022).",
  "Criteria require at least four of eight listed symptoms across the three groupings, shown with at least one person who is not a sibling. Frequency guide: under 5 years, most days; 5 and over, at least once a week — unless otherwise stated in the criterion (APA, 2022). Verify wording against the DSM-5-TR text before quoting any criterion.",
  "SEVERITY is defined by SETTINGS, not intensity: mild = one setting; moderate = some symptoms in at least two settings; severe = some symptoms in three or more settings (APA, 2022). An 'ODD — mild' report may describe a child who is only oppositional at home.",
  "Stringaris and Goodman (2009) showed the symptoms split into IRRITABLE, HEADSTRONG and HURTFUL dimensions. The irritable dimension predicts later anxiety and depression; the headstrong and hurtful dimensions predict later conduct problems. ICD-11 builds this in with a 'chronic irritability-anger' qualifier.",
  "It is a DESCRIPTION of a pattern in relationships, not an explanation of it. The diagnosis tells you what is happening between the child and adults; it does not tell you why. That is the formulation — and that is the EP's job.",
  "The pattern is INTERACTIONAL. Patterson's (1982) coercion model: demand → escalation → adult withdraws the demand → escalation is reinforced for the child, and withdrawal is reinforced for the adult. Both sides learn. This is why parenting programmes work and why 'fixing the child' alone does not.",
  "DSM-5-TR states ODD should not be diagnosed where criteria for Disruptive Mood Dysregulation Disorder are met (DMDD takes precedence), and that symptoms must not occur exclusively during a psychotic, substance use, depressive or bipolar disorder (APA, 2022).",
 ],
 "what_it_is_not": [
  "NOT a character judgement. 'Oppositional' and 'defiant' are clinical labels for a pattern; in a school report they read as moral verdicts. PSI 1.2.8 requires discretion so information is not used to a child's detriment — describe behaviour and context instead.",
  "NOT a sufficient explanation. Behaviour that looks like defiance is very often an unmet need: Hollo, Wehby and Oliver (2014) meta-analysed studies of children with emotional and behavioural disorders and found that a large majority had language deficits that had never been identified. 'Won't' is frequently 'can't understand' or 'can't do'.",
  "NOT the same as ADHD, though they often co-occur. In ADHD, non-compliance is typically forgetting, losing track or acting before thinking; in ODD the pattern is directed at adults and has an angry or vindictive quality. Untreated ADHD plus years of correction commonly produces an oppositional pattern on top.",
  "NOT a trauma response mislabelled — but it can be. Hypervigilance, controlling behaviour and rapid threat-based escalation after adversity can meet ODD criteria on paper. Ask about adversity before accepting a behavioural formulation.",
  "NOT anxiety-free. Refusal is one of the commonest faces of anxiety — the child who refuses to read aloud or go into the hall may be avoiding fear, not authority. The irritable dimension of ODD is itself linked to later emotional disorder (Stringaris & Goodman, 2009).",
  "NOT 'Pathological Demand Avoidance'. PDA is a profile described by Newson, Le Maréchal and David (2003); it is not a diagnosis in DSM-5-TR or ICD-11. Some families and clinicians use it to describe an anxiety-driven, extreme avoidance of everyday demands, often in autistic children; the evidence base and its status are debated. Record the term if a family uses it, describe the behaviour, and do not confirm or dismiss it.",
  "NOT a life sentence. Many children with an ODD diagnosis do not go on to conduct disorder; the headstrong/hurtful dimension, early onset, and adversity raise that risk (Stringaris & Goodman, 2009; Burke et al., 2002).",
 ],
 "prevalence": [
  "OVERALL: Polanczyk et al. (2015) pooled worldwide prevalence of ODD in children and adolescents at about 3.6% (disruptive behaviour disorders overall about 5.7%). DSM-5-TR reports prevalence estimates ranging roughly 1–11% depending on sample and method — check the text before quoting a single figure.",
  "IRELAND: no national ODD prevalence figure is stated here — check before quoting. Growing Up in Ireland reports SDQ conduct-problem data, which is a screening measure, not a diagnostic rate.",
  "EARLY YEARS 0–5: oppositional behaviour is developmentally normal in toddlers; DSM-5-TR sets a higher frequency threshold under 5 (most days) for that reason. Diagnosis at this age should be rare and cautious.",
  "SCHOOL AGE 6–12: typical period of first identification in school; symptoms usually first appear in the preschool years and rarely begin after early adolescence (APA, 2022).",
  "ADOLESCENT 13–16: some continuity; a subgroup progresses to conduct disorder, and the irritable subgroup to anxiety or depression.",
  "SEX RATIO: DSM-5-TR reports a modest male predominance before adolescence (about 1.4:1), not consistently found in adolescence or adulthood (APA, 2022) — check current text before quoting.",
 ],
 "cooccurring": [
  {"name": "ADHD", "rate": "commonly co-occurs — substantial overlap in clinic samples; rate not stated here, check before quoting",
   "presents": "non-compliance that is forgetting, impulsivity and task avoidance, compounded by years of correction. Assess ADHD in its own right; treatment of ADHD often reduces the oppositional layer."},
  {"name": "DEVELOPMENTAL LANGUAGE DISORDER (DLD) / UNIDENTIFIED LANGUAGE NEED", "rate": "elevated — Hollo et al. (2014) found most children with EBD had unidentified language deficits; check figure before quoting",
   "presents": "'ignoring' instructions, arguing over what was said, walking off during verbal reprimands. Language screening (CELF-5 UK via SLT) belongs in every behaviour referral."},
  {"name": "SPECIFIC LEARNING DIFFICULTY", "rate": "elevated — rate not stated here, check",
   "presents": "defiance clustering around literacy or maths tasks. Escape from work that cannot be done looks like refusal. Assess attainment before accepting a behavioural account."},
  {"name": "ANXIETY DISORDERS", "rate": "elevated, especially where irritability dominates — rate not stated here, check",
   "presents": "refusal of specific situations (reading aloud, PE, the hall, transitions), controlling behaviour, meltdowns at predictable points. Refusal is avoidance, not challenge to authority."},
  {"name": "AUTISM", "rate": "elevated — rate not stated here, check",
   "presents": "rigidity, rule disputes and distress at change that adults read as defiance. Where demand avoidance is extreme, families may use the term PDA — describe, do not adjudicate."},
  {"name": "TRAUMA AND ADVERSITY", "rate": "elevated — rate not stated here, check",
   "presents": "hypervigilance, threat-based escalation, controlling behaviour with adults, poor response to punitive systems. Ask about adversity and follow Children First if concerns emerge."},
  {"name": "DEPRESSION", "rate": "elevated over time, particularly after an irritable ODD pattern (Stringaris & Goodman, 2009) — rate not stated here",
   "presents": "irritability in young people is often how low mood shows. Ask about mood, sleep and hopelessness, not only behaviour."},
  {"name": "CONDUCT DISORDER", "rate": "a minority progress — rate not stated here, check",
   "presents": "escalation from arguing and defying to aggression, theft, destruction or serious rule-breaking. Early onset and adversity raise the risk."},
 ],
 "recommendations": [
  "FORMULATE BEFORE YOU NAME. Use the Interactive Factors Framework (Frederickson & Cline, 2015) or Monsen: map learning, language, attention, emotional, family and school-system factors. Write the formulation first; any diagnosis goes after, attributed to whoever made it.",
  "FUNCTIONAL ASSESSMENT. ABC recording across at least a week, in more than one lesson. Identify what the behaviour gets or avoids. Recommendations must fit the function — a child escaping unreadable work needs readable work, not a sanction.",
  "RULE OUT THE UNMET NEED. Recommend (or complete) attainment assessment and a language screen. Refer to SLT where comprehension is in doubt. This is the most frequently skipped step in behaviour referrals.",
  "RELATIONSHIP BEFORE COMPLIANCE. A named key adult; planned daily positive contact; high ratio of specific praise to correction. NEPS (2010) BESD Continuum guidelines give classroom-level strategies.",
  "REDUCE THE COERCIVE CYCLE. Calm, brief, private instructions; two acceptable choices rather than an ultimatum; a planned 'take-up time'; never a public stand-off. Avoid escalating sanctions that remove the child from the relationships that help.",
  "COLLABORATIVE PROBLEM-SOLVING for recurring flashpoints (Greene, 2014): identify the unsolved problem, hear the child's concern first, then solve it together. Works best with older children and with staff who can hold a non-punitive stance.",
  "PARENTING PROGRAMME (recommend the family be offered one; do not deliver unless trained). NICE CG158 (2013, updated 2017 — check for updates) recommends group parent-training for children aged 3–11 with or at risk of conduct problems. In Ireland: Incredible Years (Irish RCT, McGilloway et al., 2012), Parents Plus (Irish-developed), and Triple P in some counties — availability varies by HSE area and Tusla Family Resource Centre; check locally.",
  "CONTINUUM LEVEL: School Support with a behaviour support plan; School Support Plus where outside services are involved or behaviour persists despite a reviewed plan. Review dates on the plan, not 'ongoing'.",
  "REFER: GP / Primary Care Psychology for mild–moderate; CAMHS where there is a moderate–severe mental health difficulty (e.g. co-occurring ADHD, depression, risk) — check the current HSE CAMHS Operational Guideline, as behaviour difficulty alone is often not accepted. Tusla Family Support / Meitheal where family stress is part of the picture.",
  "DO NOT recommend reduced timetables, exclusion or sanctions as intervention. Where a reduced school day is used it must follow the Department of Education guidelines on reduced school days (2021 — check current circular), including notification to Tusla Education Support Service. DO NOT write 'defiant', 'manipulative' or 'attention-seeking' in the report.",
 ],
 "explain_parent": [
  "'The diagnosis describes a pattern — lots of arguments, temper, and saying no to adults — that's been going on for a while and is getting in the way. It describes what's happening. My job is to work out why.'",
  "'In my experience, and in the research, behaviour like this very often has something underneath it: work that's too hard, language that's harder than it looks, attention difficulties, worry, or hard things that have happened. We check all of those before we settle on an explanation.'",
  "'It isn't your fault, and it isn't his either. It's a cycle that everyone gets caught in — he pushes back, the adult pushes harder or gives in, and both sides learn to do it again. The good news is cycles can be changed from either side.'",
  "'The things with the best evidence are parenting programmes — not because your parenting caused this, but because they give you tools that change the cycle. Incredible Years and Parents Plus both run in Ireland; I'll check what's available near you.'",
  "'At school we'll be looking at what he's avoiding, what sets things off, and who he gets on with — because the plan has to fit him.'",
  "SIGNPOST: GP for Primary Care Psychology referral; local HSE / Tusla Family Resource Centre for parenting programmes; Parentline (check current number) for support between sessions.",
 ],
 "explain_teacher": [
  "'Think of the defiance as a signal, not the problem. The question is: what is he getting away from, or getting, when this happens? The ABC sheet will tell us that within a week.'",
  "'Before we build a behaviour plan, I want to rule out the boring explanations — can he read the page, does he understand the instruction, can he hold three steps in mind? Those account for a lot of \"won't\".'",
  "'Private, calm, short. Two choices, both acceptable. Walk away and give him take-up time. The audience is often what makes backing down impossible.'",
  "'Five specific positives for every correction is the target — not because he deserves a reward, but because the relationship is the intervention. Name exactly what he did well.'",
  "'After an incident, repair rather than retribution. A short, calm conversation later: what happened, what was hard, what we'll try next time.'",
  "'Please don't write \"defiant\" or \"refused\" on the log. Write what he did and what came just before. It's more useful to us and fairer to him.'",
 ],
 "explain_child": [
  "YOUNGER: 'Some days it feels like grown-ups are always telling you what to do, and your body says NO before you've even decided. That happens to lots of children. We're going to work out which times are the hardest, and make them easier.'",
  "OLDER: 'It sounds like school's been a lot of arguments lately, and you get the blame even when it isn't all you. I'm not here to give out. I want to understand what's hard, from your side.'",
  "ASK: 'When do you get on best with teachers?' and 'What's the one thing adults do that makes you most annoyed?' The answers are often the recommendation.",
  "ASK: 'Is there any work that feels too hard or boring before you even start?' — this surfaces unmet learning needs faster than any test.",
  "DO NOT use the diagnostic label with the child unless the family has; if they have, say: 'It's a name for a pattern, not a name for you.'",
 ],
 "analogies": [
  "THE TUG-OF-WAR: 'Both ends are pulling, and the harder one side pulls the harder the other does. Someone has to put the rope down first — and it works best if that's the adult.' Patterson's coercion cycle in plain terms; good with parents and teachers.",
  "THE SMOKE ALARM: 'The alarm isn't the fire. If we only take the battery out, we never find out what's burning.' For staff who want the behaviour stopped before anything else is understood.",
  "THE SHOE THAT PINCHES: 'If a child keeps kicking off his shoe, you could punish the kicking — or check the shoe.' For unmet learning or language need beneath 'refusal'; good with parents and principals.",
  "THE ARMOUR: 'Arguing can be armour. If you're sure you'll fail or be caught out, it's safer to refuse first.' For anxiety- or failure-driven opposition; works with older children too.",
 ],
 "language": [
  "In reports, describe behaviour and context: 'When asked to write independently, X left his seat on 6 of 8 observed occasions' — not 'X is defiant'. PSI 1.1.4 and 1.2.8 both apply.",
  "'Oppositional Defiant Disorder' is the diagnostic name; when citing it, attribute it: 'X was diagnosed with ODD by [service], [DD/MM/YYYY].' Do not use the acronym as an adjective ('an ODD child').",
  "Avoid: 'manipulative', 'attention-seeking', 'naughty', 'refuses', 'chooses not to', 'bold' (common in Irish school usage). Prefer: 'connection-seeking', 'finds X difficult', 'did not complete', 'left the task'.",
  "PDA: if a family uses the term, record it as their description ('the family describe a demand-avoidant profile') and describe the behaviour; do not present it as a diagnosis.",
  "'Behaviour that challenges' is widely used and places the difficulty in the interaction rather than the child.",
 ],
 "red_flags": [
  "RED FLAG — disclosure of harm, unexplained injuries, hunger, or sexualised behaviour beyond developmental expectation. Children First route the same day: DLP, and as a mandated person you report to Tusla as soon as practicable — telling the DLP does not discharge your own duty. Supervision follows action.",
  "RED FLAG — irritability with low mood, withdrawal, talk of death or self-harm. Same-day risk protocol; do not let the behaviour label hide an emotional emergency.",
  "RED FLAG — escalation to serious aggression, weapons, cruelty to animals or fire-setting. Now outside ODD; consider conduct disorder, risk assessment and CAMHS / Tusla as indicated.",
  "BOUNDARY — you do not diagnose ODD and you do not advise on medication (PSI 2.2.2). You formulate, recommend, and refer.",
  "WATCH — a school asking for a diagnosis to support exclusion or a reduced timetable. Name the purpose; your role is to meet need, not to supply grounds for removal.",
  "WATCH — sudden onset in a previously settled child. ODD develops gradually; sudden change suggests an event — bereavement, bullying, abuse, family change, illness.",
 ],
 "child_voice": [
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — Irish, free, familiar to schools. Good because it lets the child rate lessons and relationships rather than justify behaviour. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "DAY MAPPING (green / amber / red timetable) — good because it locates difficulty in times and tasks, turning 'he's always defiant' into 'Tuesday after lunch, Irish writing'.",
  "DRAWING THE IDEAL SCHOOL (Williams & Hanke, 2007, adapted from Moran's Drawing the Ideal Self) — good because the 'non-ideal' school gives children a safe, indirect way to describe what hurts without being asked about their behaviour.",
  "SCALING WITH A KEY ADULT ('how well did today go, 1–10?') — good because it gives the child a legitimate voice in the plan and builds the relationship that is itself the intervention.",
  "SOLUTION-FOCUSED EXCEPTIONS: 'Tell me about a time a teacher asked you to do something and it went fine.' — good because children with a behaviour label rarely get asked about success.",
 ],
 "questions": [
  "Q: 'Is ODD a real diagnosis or just a label for bold children?' — A: 'It's a real diagnosis in the DSM, describing a persistent pattern. But it describes rather than explains — so the useful question is what's driving the pattern for this child.'",
  "Q: 'Is it my parenting?' — A: 'No single thing causes it. Temperament, attention, language, stress and relationships all play a part. Parenting programmes help because they change the cycle, not because parents are to blame.'",
  "Q: 'Will he grow out of it?' — A: 'Many children do improve, especially with support at home and school. A smaller group go on to more serious difficulty, which is why we act now.'",
  "Q: 'Is there medication for ODD?' — A: 'That's a medical question and not one I can advise on. What I can say is that the recommended first steps in guidelines are parenting and school-based approaches.'",
  "Q: 'She's been described as PDA — is that the same thing?' — A: 'PDA isn't a diagnosis in the current manuals, though some families and professionals find the description helpful. What matters for school is the pattern of demands she finds hard, and that's what I'll describe.'",
  "Q (principal): 'Can we put him on a reduced timetable until the diagnosis comes?' — A: 'A reduced day should be a short-term, reviewed measure under the Department's guidelines, with Tusla Education Support Service notified. It doesn't treat the need, and a diagnosis wouldn't change that.'",
  "Q: 'He's fine at home — so it must be the school?' — A: 'It tells us the pattern depends on context, which is useful. Let's look at what's different between the two settings.'",
 ],
 "supervision": [
  "Bring your formulation BEFORE the diagnostic question: what hypotheses did you test (language, learning, attention, anxiety, adversity) and what did you find?",
  "Ask how your service handles requests for a diagnosis that appear linked to exclusion or reduced timetables.",
  "Rehearse word-for-word how you explain the coercive cycle to a parent without implying blame.",
  "Ask which parenting programmes actually run locally, who refers, and the waiting time — so you do not recommend something that does not exist.",
  "Discuss your own reaction to a child who has been hostile towards you. Countertransference in behaviour work is real and it shows in report language.",
 ],
 "reflection": [
  "ON FORMULATION — Did I test the unmet-need hypotheses, or did the referral label decide my conclusion before I arrived?",
  "ON LANGUAGE — Count the words 'refuses', 'defiant', 'won't' in my report. Each one is an interpretation; did I label it as such?",
  "ON POWER — Whose account dominated: the school's, the parent's, or the child's? Did the child's voice change anything in my recommendations?",
  "ON THE CYCLE — Did I describe the adult side of the interaction as well as the child's, without blaming?",
  "ON PURPOSE — Was my involvement being used to support removal of the child? Did I name that?",
  "WHAT GOOD LOOKS LIKE: 'The referral said \"defiant in class\". The ABC showed incidents clustered in independent writing; the WIAT showed spelling well below expectation; SLT screening flagged comprehension. The plan targeted literacy and instruction language, and incidents fell. The word \"defiant\" is not in my report.'",
  "WHAT POOR LOOKS LIKE: 'Presentation consistent with ODD. Recommend behaviour chart and referral to CAMHS.' — no formulation, no function, no unmet need tested, and a referral likely to be declined.",
 ],
 "citations": [
  CIT_DSM,
  CIT_POL15,
  CIT_STR09,
  "Burke, J. D., Loeber, R., & Birmaher, B. (2002). Oppositional defiant disorder and conduct disorder: A review of the past 10 years, part II. Journal of the American Academy of Child & Adolescent Psychiatry, 41(11), 1275–1293.",
  "Patterson, G. R. (1982). Coercive family process. Castalia.",
  CIT_HOLLO,
  "Newson, E., Le Maréchal, K., & David, C. (2003). Pathological demand avoidance syndrome: A necessary distinction within the pervasive developmental disorders. Archives of Disease in Childhood, 88(7), 595–600.",
  CIT_NICE,
  CIT_MCG,
  CIT_NEPS,
 ],

 "pathway": {
  "age": "Usually named in the school-age years (6–12). Oppositional symptoms typically appear in the preschool years, but a diagnosis is held back then because opposition is developmentally normal in toddlers. It becomes visible in school when compliance with non-parental adults is demanded all day.",
  "who_diagnoses": "Ireland: CAMHS psychiatrist or clinical psychologist, Primary Care Psychology, or a private clinical psychologist or psychiatrist. It is commonly given alongside ADHD by the same team. The EP does not diagnose it.",
  "who_wrote_report": "CAMHS (often within an ADHD assessment), Primary Care Psychology, a private clinical psychologist or psychiatrist, or occasionally a paediatrician. An SDQ or BASC-3 conduct score from school is screening data, not a diagnosis.",
  "refer_to": "GP / Primary Care Psychology for mild–moderate; CAMHS where co-occurring ADHD, mood difficulty or risk (check current CAMHS acceptance criteria); SLT for language; HSE / Tusla Family Resource Centre or Parents Plus / Incredible Years provider for parenting programmes; Tusla (Children First) where there is a welfare concern.",
  "sooner": "'Behaviour like this usually builds slowly, and it's very hard to know in the early years what's normal toddler pushback and what's a pattern. You're here now, and the things that help — at home and in school — work at this age.'",
 },
 "differential": [
  "ADHD — impulsive or forgetful non-compliance rather than angry opposition; needs its own assessment.",
  "UNIDENTIFIED LANGUAGE OR LEARNING NEED — refusal clustered around specific tasks; test attainment and language before concluding.",
  "ANXIETY — refusal of specific feared situations; controlling behaviour that reduces with reassurance and predictability.",
  "AUTISM — rule disputes, rigidity and distress at change, not a hostile stance to authority; extreme demand avoidance may be described as PDA by families.",
  "TRAUMA / ADVERSITY — threat-based escalation, hypervigilance, poor response to punitive systems.",
  "DMDD — persistent irritable mood between outbursts plus severe, frequent outbursts; if DMDD criteria are met, DSM-5-TR says ODD is not diagnosed.",
  "DEPRESSION — irritability as the main sign of low mood in children and adolescents.",
 ],
 "next": [
  "Proceed to FORMULATION with a named framework (Interactive Factors, Monsen, COMOIRA) — behaviour, learning, language, emotion, family and system.",
  "Complete or recommend attainment and language assessment before finalising any behavioural account.",
  "Agree a function-based support plan at School Support, with a review date and measurable targets.",
  "If risk or safeguarding emerged, none of the above first — follow the protocol and tell your supervisor the same day.",
 ],
 "presentations": [
  "Behaviour that challenges",
  "Behaviour function (ABC analysis, trigger-behaviour-consequence)",
  "Emotion regulation in the classroom",
  "Response to correction and repair after an incident",
  "Transitions between activities and between classes",
  "Escalation and de-escalation pattern",
  "Behaviour as communication of an unmet learning need",
  "Pathological Demand Avoidance (PDA) profile",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — opposition is developmentally normal; DSM-5-TR sets a higher frequency threshold under 5",
   "prevalence": "Not reliably estimated at this age here — check before quoting; frame as developmental.",
   "see": "Tantrums, 'no' to routine requests, hitting when frustrated — mostly typical. Concern is frequency, intensity, and whether it happens across settings and with several adults. Language delay is a frequent driver; describe rather than classify, and support the parent-child relationship.",
   "tools": ["SDQ (2–4 version)", "Conners EC", "Ages & Stages Questionnaires (ASQ-3)", "Preschool Language Scales-5 (PLS-5)", "Functional behaviour assessment (ABC)"],
  },
  "School Age": {
   "applies": "YES — typical period of first identification",
   "prevalence": "Pooled ODD prevalence about 3.6% in children and adolescents (Polanczyk et al., 2015); no Irish figure stated here.",
   "see": "Arguing with teachers, refusal clustered around certain tasks or adults, blaming others, temper after correction. Test the unmet-need hypotheses (language, literacy, attention, anxiety) with attainment, language screening and a week of ABC data. Parent–teacher disagreement tells you about context.",
   "tools": ["SDQ", "BASC-3", "Conners-4", "BRIEF-2", "Functional behaviour assessment (ABC)", "CELF-5 UK", "WIAT-III UK", "RCADS", "Piers-Harris 3"],
  },
  "Adolescent": {
   "applies": "YES — continuing or first identified; watch for mood and conduct trajectories",
   "prevalence": "Broadly similar to school age; male predominance less consistent after adolescence (APA, 2022) — check before quoting.",
   "see": "Conflict with specific teachers, walking out, suspensions accumulating. The irritable dimension may now be depression; the hurtful dimension may be moving toward conduct problems. Self-report becomes essential, and the young person's account of fairness matters more than ever.",
   "tools": ["SDQ", "BASC-3 SRP", "Conners-4 self-report", "RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "CELF-5 UK", "WIAT-III UK", "Functional behaviour assessment (ABC)"],
  },
  "Young Adult": {
   "applies": "RETROSPECTIVE ONLY — rarely a new diagnosis in education settings at this age",
   "prevalence": "Not stated here — check before quoting; adult ODD is recognised in DSM-5-TR but rarely diagnosed in Irish services.",
   "see": "Appears as a history in files: 'ODD at age 8'. Ask what has changed and what the diagnosis now adds. Relevant in Youthreach, further education and disability support settings, where the history may still shape how staff read the young person.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — but check the label; communication and sensory needs often explain 'defiance'",
   "prevalence": "Rate not stated here — check before quoting.",
   "see": "Refusal and aggression in pupils with intellectual disability, autism or limited communication are usually communication of need, pain, or sensory overload. Functional assessment and communication review come before any behavioural diagnosis; adaptive functioning sets the developmental expectation.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3", "Communication Matrix / AAC review", "Adaptive measure in place of IQ"],
  },
 },
})

# ============================================================================ 2 · CD
CONDS.append({
 "name": "Conduct Disorder (CD)",
 "code": "DSM-5-TR Conduct Disorder (ICD-10-CM F91.1 childhood-onset · F91.2 adolescent-onset · F91.9 unspecified onset) · ICD-11 6C91 Conduct-dissocial disorder (childhood / adolescent onset; limited prosocial emotions qualifier — check subcodes before quoting)",
 "neps": NEPS_BEH + " — and 3. EMOTIONAL (3.5 Trauma, attachment and loss · 3.7 Risk and safeguarding) where relevant",
 "coru": CORU,
 "psi": PSI,
 "law": LAW,

 "what_it_is": [
  "A DSM-5-TR diagnosis: a repetitive and persistent pattern of behaviour that violates the basic rights of others or major age-appropriate societal norms or rules (APA, 2022).",
  "Criteria require at least three of fifteen behaviours in the past 12 months, at least one in the past 6 months, across four groups: AGGRESSION to people and animals; DESTRUCTION OF PROPERTY; DECEITFULNESS OR THEFT; SERIOUS VIOLATIONS OF RULES (e.g. truancy beginning before age 13). Verify the full list against DSM-5-TR before quoting.",
  "ONSET SPECIFIERS: childhood-onset (at least one symptom before age 10), adolescent-onset (none before 10), unspecified (APA, 2022). The distinction matters because the outcomes differ.",
  "Moffitt's (1993) developmental taxonomy: a small LIFE-COURSE-PERSISTENT group, with early onset and neurodevelopmental and family adversity, and a larger ADOLESCENCE-LIMITED group whose antisocial behaviour is more social and more often desists. Later follow-ups have complicated this, but it remains the most useful frame for a school conversation.",
  "'WITH LIMITED PROSOCIAL EMOTIONS' specifier: at least two of lack of remorse or guilt; callous lack of empathy; unconcern about performance; shallow or deficient affect — persistently, over 12 months, across relationships and settings (APA, 2022). This maps to research on callous-unemotional traits (Frick et al., 2014). It is a small subgroup and must never be inferred from a single incident.",
  "Severity (mild / moderate / severe) is based on the number of problems and the harm caused (APA, 2022).",
  "It is heavily shaped by CONTEXT: poverty, harsh or inconsistent parenting, abuse and neglect, peer groups, school exclusion. The behaviour is real and harmful; the causes are rarely in the child alone.",
 ],
 "what_it_is_not": [
  "NOT 'a bad kid'. The diagnosis describes behaviour over 12 months; it is not a prediction of adult criminality. Most young people with conduct problems do not go on to antisocial personality disorder (Moffitt, 1993; APA, 2022).",
  "NOT the same as delinquency or offending. Offending is a legal category; CD is a clinical description of a pattern with impairment. A single serious incident does not make a diagnosis.",
  "NOT 'psychopathy'. Callous-unemotional traits are a narrow, research-defined dimension (Frick et al., 2014). Do not use 'psychopath', 'no conscience' or similar in any report or conversation.",
  "NOT separate from harm done to the child. Many children with conduct problems have experienced abuse, neglect, domestic violence, or exploitation. Cruelty to animals, fire-setting and sexualised aggression can be indicators of the child's own victimisation.",
  "NOT untreatable. NICE CG158 (2013, updated 2017) recommends parent training for younger children, child-focused social and cognitive problem-solving programmes for older children, and multimodal interventions (e.g. multisystemic therapy) for adolescents — check for updates.",
  "NOT solved by exclusion. Removing a young person from school removes structure, adult relationships and supervision, and exposes them to peers and exploitation. Exclusion is a risk factor, not an intervention.",
 ],
 "prevalence": [
  "OVERALL: Polanczyk et al. (2015) pooled worldwide prevalence of CD in children and adolescents at about 2.1%. DSM-5 reports one-year population prevalence estimates from about 2% to over 10%, median about 4% — check the DSM-5-TR text before quoting.",
  "IRELAND: no national CD prevalence figure is stated here — check before quoting.",
  "EARLY YEARS 0–5: not meaningfully diagnosed; aggression at this age is common and developmental.",
  "SCHOOL AGE 6–12: childhood-onset cases are identified here; this is the group Moffitt (1993) links to persistent difficulty.",
  "ADOLESCENT 13–16: prevalence rises; most new cases are adolescent-onset (APA, 2022).",
  "SEX RATIO: more common in males in DSM-5-TR; DSM-5-TR notes females are more likely than males to show lying, truancy, running away and substance use rather than physical aggression (APA, 2022) — check current text before quoting a ratio.",
 ],
 "cooccurring": [
  {"name": "ADHD", "rate": "commonly co-occurs, especially in childhood-onset CD — rate not stated here, check",
   "presents": "impulsive aggression and rule-breaking. ADHD plus early conduct problems is the profile most linked to persistence; assess both."},
  {"name": "ODD", "rate": "often precedes childhood-onset CD — rate not stated here",
   "presents": "a history of arguing and defiance before the more serious behaviours. DSM-5-TR allows both diagnoses where criteria are met."},
  {"name": "DEVELOPMENTAL LANGUAGE DISORDER / LITERACY DIFFICULTY", "rate": "elevated — unidentified language need common in EBD samples (Hollo et al., 2014); check figure",
   "presents": "poor verbal problem-solving, misreading of adult intentions, failure and shame in reading. Language screening is essential and often reveals needs never identified."},
  {"name": "TRAUMA, ABUSE AND NEGLECT", "rate": "elevated — rate not stated here, check",
   "presents": "aggression, hypervigilance, running away, fire-setting, sexualised behaviour. Children First applies whenever there is reasonable concern."},
  {"name": "DEPRESSION AND ANXIETY", "rate": "elevated — rate not stated here, check",
   "presents": "irritability, risk-taking, self-destructive behaviour. Emotional need is easily hidden behind conduct behaviour."},
  {"name": "SUBSTANCE USE", "rate": "elevated in adolescence — rate not stated here, check",
   "presents": "theft, truancy and aggression linked to use or debt. Ask; consider local youth drug and alcohol services and possible exploitation."},
  {"name": "INTELLECTUAL DISABILITY / LEARNING DIFFICULTY", "rate": "elevated — rate not stated here, check",
   "presents": "suggestibility, being used by older peers, not understanding consequences. Adaptive and cognitive assessment changes how behaviour should be read."},
 ],
 "recommendations": [
  "FORMULATE THE WHOLE SYSTEM. Interactive Factors (Frederickson & Cline, 2015) across child, family, peers, school and community. Name protective factors — a teacher, a sport, a grandparent — as carefully as risks.",
  "SAFETY FIRST, THEN FORMULATION. If behaviour poses risk to the young person or others, the school's risk and safeguarding procedures come before any assessment plan.",
  "KEEP THEM IN SCHOOL. Recommend a named key adult, a daily check-in, and a timetable with success built in. Challenge exclusion and prolonged reduced timetables; where a reduced day is used, it must follow Department of Education guidelines on reduced school days (2021 — check current circular), with Tusla Education Support Service notified.",
  "TEST THE UNMET LEARNING AND LANGUAGE NEED. Attainment (WIAT-III UK) and language screening; many young people with conduct problems have unidentified literacy and language difficulties (Hollo et al., 2014).",
  "STRUCTURE AND SUPERVISION in unstructured time — yard, corridors, lunch. Most serious incidents happen where adult presence is lowest.",
  "SOCIAL AND COGNITIVE PROBLEM-SOLVING for older children (NICE CG158 recommends group programmes for ages 9–14 — check for updates); restorative approaches for repair after harm.",
  "PARENTING / FAMILY: recommend referral for a parenting programme for younger children (Incredible Years, Parents Plus, Triple P where available — check locally); for adolescents, NICE recommends multimodal family-based intervention — availability in Ireland is limited and varies; check with CAMHS and Tusla.",
  "CONTINUUM LEVEL: School Support Plus in almost all cases, with a multi-agency plan and named coordinator.",
  "REFER: CAMHS where there is co-occurring mental health difficulty or risk (check acceptance criteria); Tusla (Children First) for welfare concerns; Tusla Family Support / Meitheal; Garda Youth Diversion Project or Juvenile Liaison Officer where offending is involved (school or family would usually link); youth drug and alcohol services.",
  "DO NOT diagnose, predict criminality, or use 'psychopathic', 'callous' or 'dangerous' in reports. DO NOT recommend 'scared straight', boot-camp or purely punitive approaches — the evidence does not support them.",
 ],
 "explain_parent": [
  "'The diagnosis describes a pattern of behaviour over the last year that's been causing real harm or breaking serious rules. It describes the behaviour. It doesn't say who he is or who he'll become.'",
  "'Most young people with these difficulties do not go on to have them as adults — especially when they stay connected to school and to adults who are on their side.'",
  "'There are usually several things feeding in — school getting harder, friends, things at home, sometimes things that have happened to him. We look at all of them, and at what's going right, so the plan has something to build on.'",
  "'The best-supported help involves the whole family, not just him. That isn't blame — it's because you're the people with the most influence.'",
  "'I'll be honest: some of the services that work best are hard to get quickly. I'll tell you what's available here and what I'm asking for.'",
  "SIGNPOST: GP; CAMHS via GP where there's a mental health concern; Tusla Family Resource Centre; local parenting programme providers; Parentline (check current number).",
 ],
 "explain_teacher": [
  "'This is a young person in trouble, not just a young person causing trouble. Both are true, and the plan has to hold both.'",
  "'Keeping him in school is the single most protective thing we can do. Exclusion hands him to the street and to older peers.'",
  "'Can he read the textbook? Let's check before we decide his behaviour in history is about history.'",
  "'He needs one adult who is reliably glad to see him. Not a mentor programme on paper — a person, every day, for two minutes.'",
  "'Watch the unstructured times. Most of the serious incidents come from yard, corridors and lunch.'",
  "'If anything he says or does makes you worried about his own safety or someone else's, it goes to the DLP that day — and if you're a mandated person, your own duty to report to Tusla still stands.'",
 ],
 "explain_child": [
  "YOUNGER: 'Some of the things that have happened have hurt people, and I think some things have hurt you too. I'm here to help work out what's going wrong and what would help.'",
  "OLDER: 'I'm not the guards and I'm not the principal. I'm trying to understand what school is like for you, so the adults can do things differently. You don't have to tell me anything you don't want to.'",
  "BE CLEAR ABOUT CONFIDENTIALITY at the start: 'If you tell me something that means you or someone else might be hurt, I'd have to tell someone to keep you safe. I'd tell you first.'",
  "ASK: 'Who's the one adult in school you'd go to if something was wrong?' and 'What are you good at that school doesn't see?'",
  "ASK about fairness: 'What happens in school that feels unfair?' Young people with conduct difficulties often have a strong, and sometimes accurate, sense of injustice.",
 ],
 "analogies": [
  "THE FORK IN THE ROAD: 'Two roads start in the same place — one for a few difficult teenage years, one that goes on longer. What makes the difference is mostly what's around the young person, and that's what we can change.' Moffitt's taxonomy for parents and staff.",
  "THE ANCHOR: 'School is the anchor. Pull it up and the boat drifts toward whatever current is strongest.' For principals weighing exclusion.",
  "THE ICEBERG: 'The incident is the tip. Underneath: reading, language, home, friends, what's happened to him.' For staff meetings where only the incident is discussed.",
  "THE REPUTATION TRAP: 'Once everyone expects trouble, every small thing proves it, and he starts to live up to it.' Good with adolescents themselves — it names the process without blaming them.",
 ],
 "language": [
  "Describe what happened, when, and with whom: 'On 3 occasions in 4 weeks, X hit a peer during yard' — not 'X is violent'.",
  "Attribute any diagnosis: 'X was diagnosed with Conduct Disorder by [service], [DD/MM/YYYY].' Never 'a CD child'.",
  "Avoid: 'psychopath', 'callous', 'evil', 'thug', 'dangerous', 'no conscience', 'criminal'. These follow a young person into other files and services. PSI 1.1.4 and 1.2.8.",
  "Where the limited-prosocial-emotions specifier appears in a clinical report, quote it exactly and attribute it; do not paraphrase it into everyday language.",
  "'Young person' is generally preferred to 'offender' or 'delinquent' in Irish youth justice and education contexts.",
 ],
 "red_flags": [
  "RED FLAG — disclosure or signs of abuse, neglect, domestic violence or exploitation (including being used to carry drugs or money, or unexplained money, phones or new 'friends'). Children First route the same day; as a mandated person, report to Tusla as soon as practicable — telling the DLP does not discharge your duty.",
  "RED FLAG — threats to harm others, weapons, specific plans, or fire-setting. Immediate safety response via the principal and school procedures; Gardaí where there is imminent danger. Supervision follows action.",
  "RED FLAG — self-harm, suicidal talk, or reckless risk-taking. Same-day risk protocol; conduct behaviour and suicide risk co-exist.",
  "RED FLAG — sexually harmful behaviour. This needs a specialist response (Tusla and specialist services); do not investigate yourself.",
  "BOUNDARY — you do not diagnose CD, predict offending, or conduct forensic risk assessment. PSI 2.2.2, 2.2.4.",
  "WATCH — a school building a file toward expulsion. Your report may be used; write it knowing that, and name needs clearly. Expulsion or suspensions totalling 20 school days in a year can be appealed under s.29 of the Education Act 1998 — check current provisions.",
 ],
 "child_voice": [
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — good because it asks about school rather than about behaviour, lowering defensiveness. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "PERSONAL CONSTRUCT PSYCHOLOGY — Drawing the Ideal Self (Moran, 2001) — good because it allows a young person to describe who they don't want to become, which is often the most honest thing they say.",
  "TIMELINE / LIFE MAPPING — good because it lets the young person place turning points (moves, losses, exclusions) themselves, which often reframes the referral.",
  "MOTIVATIONAL INTERVIEWING-STYLE CONVERSATION — good for adolescents because it respects autonomy and avoids the lecture they are expecting.",
  "RESTORATIVE CONFERENCE NOTES (with consent) — good because they capture how the young person understands harm and repair in their own words.",
 ],
 "questions": [
  "Q: 'Is he going to end up in prison?' — A: 'Most young people with these difficulties don't. What makes a difference is staying in school, having adults on side, and getting help early — which is what we're doing.'",
  "Q (principal): 'Doesn't the diagnosis mean he needs a special school or a unit?' — A: 'The diagnosis describes behaviour; it doesn't determine placement. Any change of placement goes through the SENO and NCSE process, and first we need to know what has and hasn't been tried here.'",
  "Q: 'Is this because of what happened at home?' — A: 'Hard experiences can be part of it, and if there's anything that worries us about safety we have to act on that. But there's usually more than one cause, and some of them we can change in school.'",
  "Q: 'He shows no remorse — does that mean he's a psychopath?' — A: 'No. Lack of visible remorse can be shame, defensiveness or not having the words. Clinicians use a specific, careful definition, and it isn't something to conclude from how a meeting went.'",
  "Q: 'Will medication help?' — A: 'That's a medical question and outside my role. If he has ADHD as well, that's for his doctor to discuss. The main recommended help for conduct difficulties is family and school-based.'",
  "Q: 'Why should we keep him when he's hurting other children?' — A: 'Everyone's safety comes first, and the plan has to protect other pupils. Keeping him connected to school, with the right structure, is also the thing most likely to reduce the harm over time.'",
 ],
 "supervision": [
  "Bring any case with a safeguarding thread the same day, and record what you did before discussing what it means.",
  "Ask how your service works with Tusla, Gardaí (Juvenile Liaison Officers) and youth diversion projects, and where the EP role stops.",
  "Discuss how to write a report that is honest about harm without writing a young person's future for them.",
  "Ask for help with your own reactions — fear, anger or protectiveness — after meeting a young person who has hurt others.",
  "Bring your language: read a paragraph of your report aloud and ask whether it would harm the young person if read in five years' time by another agency.",
 ],
 "reflection": [
  "ON FORMULATION — Did I find the protective factors, or only the risks?",
  "ON SAFEGUARDING — Did I ask about harm to the young person, not just harm by them?",
  "ON THE UNMET NEED — Did I test reading and language, or assume a young person with conduct difficulties 'just won't'?",
  "ON LANGUAGE AND FUTURE READERS — Who will read this report in five years, and what will it do for or to this young person?",
  "ON THE SYSTEM — Was I asked to help, or to legitimise exclusion? Did I say so?",
  "WHAT GOOD LOOKS LIKE: 'The referral was framed as expulsion-imminent. I mapped incidents: nearly all in yard and in two lessons with heavy reading. WIAT showed reading well below age expectation. We agreed yard supervision changes, a key adult, adapted texts and a parenting referral. I raised one welfare concern with the DLP that day and reported to Tusla.'",
  "WHAT POOR LOOKS LIKE: 'Presents with conduct difficulties and limited empathy. Recommend alternative placement.' — no formulation, no safeguarding question, stigmatising language, and a recommendation outside the EP's evidence.",
 ],
 "citations": [
  CIT_DSM,
  "Moffitt, T. E. (1993). Adolescence-limited and life-course-persistent antisocial behavior: A developmental taxonomy. Psychological Review, 100(4), 674–701.",
  "Frick, P. J., Ray, J. V., Thornton, L. C., & Kahn, R. E. (2014). Can callous-unemotional traits enhance the understanding, diagnosis, and treatment of serious conduct problems in children and adolescents? A comprehensive review. Psychological Bulletin, 140(1), 1–57.",
  CIT_POL15,
  CIT_NICE,
  CIT_HOLLO,
  CIT_MCG,
  CIT_IFF,
  "Moran, H. (2001). Who do you think you are? Drawing the ideal self: A technique to explore a child's sense of self. Clinical Child Psychology and Psychiatry, 6(4), 599–604.",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government Publications.",
 ],

 "pathway": {
  "age": "Childhood-onset CD is identified in the primary years, often after a history of ODD and ADHD. Adolescent-onset CD appears from about 13 onwards, when peer influence, independence and unsupervised time increase. Identification often follows a crisis — a serious incident, suspension, or Garda contact.",
  "who_diagnoses": "Ireland: CAMHS psychiatrist or clinical psychologist, or a private psychiatrist or clinical psychologist. Some young people are assessed through youth justice routes (e.g. assessment linked to Oberstown Children Detention Campus or court reports). The EP does not diagnose it.",
  "who_wrote_report": "CAMHS; a private clinical psychologist or psychiatrist; a forensic or court-ordered assessment; occasionally Tusla-commissioned assessment for a child in care. Check whether the report was written for a clinical, legal or care purpose — it shapes what it says.",
  "refer_to": "CAMHS via GP where there is co-occurring mental health difficulty or risk (check current acceptance criteria); Tusla (Children First) for welfare concerns; Tusla Family Support / Meitheal; Garda Youth Diversion Projects (usually via JLO); youth drug and alcohol services; SLT for language; NCSE / SENO where placement or supports are being reviewed.",
  "sooner": "'Difficulties like these often build up over years, and the signs early on can look like ordinary behaviour problems. What matters now is that the right people are around him — and that's what we're setting up.'",
 },
 "differential": [
  "ODD — arguing and defiance without serious aggression, theft, destruction or rule violation.",
  "ADHD — impulsive rule-breaking without the persistent violation of others' rights; often co-occurs.",
  "TRAUMA / PTSD / ATTACHMENT DIFFICULTY — aggression and running away as threat response; check history and safeguarding.",
  "DEPRESSION OR BIPOLAR DISORDER — irritability and reckless behaviour limited to mood episodes; needs medical assessment.",
  "ADOLESCENT PEER-GROUP OR CONTEXTUAL BEHAVIOUR — antisocial acts within a peer group or exploitation, without a persistent individual pattern.",
  "LEARNING DISABILITY / UNIDENTIFIED LANGUAGE NEED — behaviour arising from misunderstanding, suggestibility or failure.",
 ],
 "next": [
  "Check safeguarding first — any concern goes the same day to the DLP and to Tusla as a mandated person.",
  "Formulate with a named framework, including protective factors, and test learning and language needs.",
  "Convene a multi-agency School Support Plus plan with a named coordinator and review date.",
  "Tell your supervisor the same day about any risk concern; supervision follows action.",
 ],
 "presentations": [
  "Behaviour that challenges",
  "Harmful or sexualised behaviour in children",
  "Adolescent substance misuse / dual diagnosis",
  "Risk-taking without a diagnosis attached",
  "Group dynamics and peer influence",
  "Unstructured time — yard and corridor as the difficulty",
  "Behaviour as communication of an unmet learning need",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — aggression at this age is common and developmental; not a meaningful diagnosis",
   "prevalence": "Not meaningfully estimated at this age — check before quoting.",
   "see": "Hitting, biting and snatching are typical early behaviours. Concern is persistence, severity, cruelty to animals or other children, and signs of harm to the child. Frame as developmental and relational; ask about the home environment and language.",
   "tools": ["SDQ (2–4 version)", "Ages & Stages Questionnaires (ASQ-3)", "Functional behaviour assessment (ABC)"],
  },
  "School Age": {
   "applies": "YES — childhood-onset CD (symptom before age 10) is identified here, usually after ODD/ADHD",
   "prevalence": "Pooled CD prevalence about 2.1% across children and adolescents (Polanczyk et al., 2015); lower in younger children — no Irish figure stated here.",
   "see": "Physical aggression, stealing, lying, destruction of property, bullying. Usually a history of ODD and often ADHD. Literacy and language difficulty is common and frequently unidentified. Ask about home, safety and adversity.",
   "tools": ["SDQ", "BASC-3", "Conners-4", "Functional behaviour assessment (ABC)", "WIAT-III UK", "CELF-5 UK", "Piers-Harris 3"],
  },
  "Adolescent": {
   "applies": "YES — peak prevalence; adolescent-onset cases first appear here",
   "prevalence": "Rises in adolescence (APA, 2022) — no single figure stated here; check before quoting.",
   "see": "Truancy, staying out, theft, fights, substance use, Garda contact, suspensions accumulating. Distinguish persistent individual pattern from peer-group behaviour. Screen mood and risk; consider exploitation.",
   "tools": ["SDQ", "BASC-3 SRP", "Conners-4 self-report", "RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "WIAT-III UK", "CELF-5 UK"],
  },
  "Young Adult": {
   "applies": "RARELY — CD may be diagnosed after 18 only where antisocial personality disorder criteria are not met (APA, 2022); usually retrospective in education settings",
   "prevalence": "Not stated here — check before quoting.",
   "see": "Appears in files from Youthreach, further education, probation or Oberstown. Ask what the history means now; many young adults have desisted. Unidentified literacy and learning needs are often still present and still actionable.",
   "tools": ["Adult self-report measures via the service", "WRAT-5"],
  },
  "Special Setting": {
   "applies": "YES — but read behaviour through communication, cognition and trauma first",
   "prevalence": "Rate not stated here — check before quoting.",
   "see": "Special schools and classes may hold young people with conduct difficulties alongside intellectual disability or autism. Suggestibility and exploitation are real risks. Functional assessment and adaptive functioning come before any behavioural label.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3", "Adaptive measure in place of IQ"],
  },
 },
})

# ============================================================================ 3 · DMDD
CONDS.append({
 "name": "Disruptive Mood Dysregulation Disorder (DMDD)",
 "code": "DSM-5-TR Disruptive Mood Dysregulation Disorder (ICD-10-CM F34.81), in the Depressive Disorders chapter · ICD-11: no equivalent category — nearest is 6C90.0 ODD with chronic irritability-anger (check before quoting; Part D lists 6A70–6A7Z, the depressive-disorders block)",
 "neps": "3. EMOTIONAL (3.4 Mood) — and " + NEPS_BEH,
 "coru": CORU,
 "psi": PSI,
 "law": LAW,

 "what_it_is": [
  "A DSM-5 diagnosis introduced in 2013 and retained in DSM-5-TR, placed in the DEPRESSIVE DISORDERS chapter — not with the behaviour disorders (APA, 2022). It is a MOOD diagnosis whose most visible sign is behaviour.",
  "Core features: severe, recurrent TEMPER OUTBURSTS (verbal and/or behavioural) grossly out of proportion to the situation and inconsistent with developmental level, on average three or more times a week; PLUS persistently IRRITABLE OR ANGRY MOOD between outbursts, most of the day, nearly every day, observable by others (APA, 2022).",
  "Duration and settings: present for 12 months or more without a break of three or more consecutive months; present in at least two of three settings (home, school, peers) and severe in at least one (APA, 2022).",
  "AGE RULES (verify wording against DSM-5-TR before quoting): the diagnosis should not be made for the first time before age 6 or after age 18; by history or observation, onset of the criteria is before age 10 (APA, 2022). So DMDD is a school-age-onset diagnosis — onset is before 10, first diagnosis between 6 and 18.",
  "Why it exists: to address the rise in bipolar disorder diagnoses in children in the United States, many of whom had chronic, non-episodic irritability rather than distinct manic episodes. Research on 'severe mood dysregulation' showed these children tended to develop depression and anxiety, not bipolar disorder (Leibenluft, 2011).",
  "Exclusions: it cannot co-exist with ODD, Intermittent Explosive Disorder or bipolar disorder; if DMDD criteria are met, ODD is not diagnosed. There must never have been a distinct period of more than one day meeting criteria for mania or hypomania (APA, 2022).",
  "It is DSM-only. ICD-11 chose not to include it and instead added a 'with chronic irritability-anger' qualifier to ODD. A child could be described differently depending on which system the clinician used.",
 ],
 "what_it_is_not": [
  "NOT 'tantrums'. Tantrums are normal and episodic. DMDD requires frequent, severe outbursts PLUS an irritable mood that persists between them, for a year, across settings.",
  "NOT childhood bipolar disorder. The irritability is chronic, not episodic; there are no distinct manic episodes. Leibenluft (2011) summarises the evidence that these young people are more likely to develop depression and anxiety than bipolar disorder.",
  "NOT ODD with a new name. It sits in the depressive disorders chapter because the underlying problem is mood. Recommendations should address emotional regulation and wellbeing, not only compliance.",
  "NOT a diagnosis for under-6s. Irritability in preschoolers can be significant and deserve support, but DSM-5-TR says DMDD is not diagnosed for the first time before 6.",
  "NOT uncontroversial. Critics have questioned its distinctiveness from severe ODD and its stability over time; ICD-11 did not adopt it (Stringaris et al., 2018 review the debate). Hold it lightly and focus on the child's actual pattern.",
  "NOT explained by the diagnosis alone. As with ODD, test for unmet learning and language need, ADHD, anxiety, autism, sleep difficulty and adversity — all of which can drive chronic irritability.",
 ],
 "prevalence": [
  "OVERALL: DSM-5-TR estimates 6-month to 1-year prevalence among children and adolescents in the range of about 2–5%, with higher rates in males and school-age children than in females and adolescents (APA, 2022) — check current text before quoting.",
  "Copeland et al. (2013) applied DMDD criteria retrospectively to three US community samples and found rates of roughly 1–3% in the preschool-to-adolescent range, with very high co-occurrence with other disorders — check figures before quoting.",
  "IRELAND: no Irish figure stated here — check before quoting. DMDD is used less often in Irish and UK services than in the US; many Irish reports will describe the same child as ODD, ADHD with emotional dysregulation, or anxiety.",
  "EARLY YEARS 0–5: not diagnosed (APA, 2022).",
  "SCHOOL AGE 6–12: the band where onset must occur (before 10) and where most first diagnoses are made.",
  "ADOLESCENT 13–16: can be first diagnosed up to 18; outbursts may lessen while irritability and risk of depression and anxiety continue (Stringaris et al., 2018).",
 ],
 "cooccurring": [
  {"name": "ADHD", "rate": "very high co-occurrence reported — rate not stated here, check",
   "presents": "impulsive outbursts plus inattention; distinguishing ADHD-related emotional dysregulation from DMDD is a clinical judgement. Assess ADHD in its own right."},
  {"name": "ANXIETY DISORDERS", "rate": "elevated — rate not stated here, check",
   "presents": "outbursts at predictable feared points (transitions, performance, separation) with irritable, tense mood between. Treat the anxiety and irritability often reduces."},
  {"name": "DEPRESSION", "rate": "elevated concurrently and over time (Leibenluft, 2011) — rate not stated here",
   "presents": "irritability, low enjoyment, sleep change, negative self-talk. DMDD and major depression can both be diagnosed. Always ask about mood and self-harm."},
  {"name": "AUTISM", "rate": "elevated — rate not stated here, check",
   "presents": "meltdowns from sensory overload or unpredictability that look like outbursts; irritability from chronic stress. Clinicians must decide whether outbursts are better explained by autism."},
  {"name": "DLD / UNIDENTIFIED LANGUAGE NEED", "rate": "elevated in EBD samples (Hollo et al., 2014) — check figure",
   "presents": "outbursts when language demands exceed skill; frustration at not being understood; difficulty labelling feelings."},
  {"name": "TRAUMA AND ADVERSITY", "rate": "elevated — rate not stated here, check",
   "presents": "chronic irritability and explosive reactions as threat responses. Ask about adversity; follow Children First where concerns arise."},
  {"name": "SLEEP DIFFICULTY", "rate": "common and bidirectional — rate not stated here",
   "presents": "chronic irritability and low frustration tolerance worsened by poor sleep. Always ask."},
 ],
 "recommendations": [
  "FORMULATE THE MOOD, NOT ONLY THE BEHAVIOUR. Interactive Factors (Frederickson & Cline, 2015) with emotional wellbeing central: what keeps this child irritable most of the time — anxiety, sleep, pain, unmet learning need, peer difficulty, adversity?",
  "MAP THE OUTBURSTS. ABC over two weeks with time of day, setting, preceding demand and recovery time. Look for predictable escalation points and for early warning signs staff can learn to read.",
  "PREVENT, DON'T ONLY RESPOND. Predictable routine, advance warning of transitions, reduced demands on bad days, a planned calm space the child can access before, not after, an outburst.",
  "CO-REGULATION FIRST. During escalation: fewer words, lower voice, reduce audience, keep everyone safe. Teaching and consequences happen later, when calm. NEPS (2010) BESD Continuum guidance applies.",
  "BUILD EMOTIONAL VOCABULARY AND REGULATION SKILLS when calm — feelings scales, body-cue work, problem-solving for known triggers. Link to SPHE and school wellbeing programmes.",
  "TEST THE UNMET NEED: attainment and language screening; hearing and sleep history; anxiety screen (RCADS); mood screen (MFQ) for older children.",
  "PARENT SUPPORT: parenting programmes that address irritability and outbursts (Incredible Years, Parents Plus, Triple P — check local availability). DMDD is not covered by NICE CG158; clinical treatment decisions belong to CAMHS.",
  "CONTINUUM LEVEL: School Support Plus where a DMDD diagnosis exists or outbursts are severe across settings; a safety plan for outbursts must be agreed with parents and reviewed.",
  "REFER: CAMHS via GP — DMDD is a mood diagnosis and chronic irritability with low mood or risk meets the moderate–severe threshold more often than behaviour alone (check current criteria); Primary Care Psychology for milder presentations; SLT where language is in doubt.",
  "DO NOT advise on medication, suggest bipolar disorder, or describe the child as 'explosive' or 'volatile' in reports. DO NOT use seclusion or restraint as a plan; any physical intervention must follow school policy and current Department of Education guidance (check current status).",
 ],
 "explain_parent": [
  "'DMDD describes a child who is irritable or angry most of the day, most days, with big outbursts several times a week, going on for at least a year. It's in the same part of the manual as depression, because the underlying difficulty is mood.'",
  "'It was added partly to stop children being diagnosed with bipolar disorder when they didn't have it. Children with this pattern are more likely to have difficulties with worry and low mood later than with bipolar disorder — which is why we keep an eye on mood.'",
  "'Being irritable all the time is exhausting for the child as well as for you. It usually isn't something he's choosing, and punishments on their own don't tend to change it.'",
  "'We'll look for what keeps the irritability high — sleep, worry, school being too hard, friendships — and build a plan around the times of day that go wrong.'",
  "'Decisions about treatment, including anything medical, are for his doctor or CAMHS. What I can do is make school a calmer, more predictable place for him.'",
  "SIGNPOST: GP for CAMHS or Primary Care referral; local parenting programmes; Parentline (check current number); Jigsaw for young people aged 12–25 where available (check eligibility).",
 ],
 "explain_teacher": [
  "'This is a mood difficulty that shows up as behaviour. The outbursts are the tip; the everyday irritability is the bigger part.'",
  "'The irritability means his fuse is short most of the time. Small things — a changed plan, a correction in front of others — can tip him over.'",
  "'Look for the build-up. Most outbursts have warning signs; if we can spot them, a quiet task, a job or a break can prevent the explosion.'",
  "'During an outburst: fewer words, lower voice, fewer people. Keep everyone safe and wait. Talking it through happens later.'",
  "'Notice mood, not only behaviour. If he seems flat, withdrawn or says things like \"I hate myself\", tell the DLP the same day.'",
  "'Keep a simple log: time, what came before, how long it lasted, what helped. It's the most useful thing you can give me.'",
 ],
 "explain_child": [
  "YOUNGER: 'Some children feel cross or grumpy lots of the time, and then little things feel really big and the anger comes out all at once. That's not you being bad. We're going to find ways to help the cross feeling get smaller.'",
  "OLDER: 'It sounds like you feel wound up most of the time, and then something small sets you off. That's really tiring. I want to understand what makes it worse and what makes it better.'",
  "USE A FEELINGS THERMOMETER or 5-point scale: 'Where are you now? Where were you just before it happened?' This builds the awareness that regulation depends on.",
  "ASK: 'How are you sleeping?', 'Is there anything you're worried about?' and 'Do you ever feel sad or fed up as well as angry?' — irritability often hides worry or low mood.",
  "ASK: 'What's the first sign in your body that you're getting annoyed?' — this gives the child a role in noticing and preventing outbursts.",
 ],
 "analogies": [
  "THE KETTLE ALREADY NEAR THE BOIL: 'Most children start the day with cold water. He starts with it nearly boiling, so it takes very little to boil over.' Explains chronic irritability plus outbursts; works with parents and staff.",
  "THE SUNBURN: 'Touch that wouldn't bother anyone else really hurts on sunburn. His mood is like that most of the time — small things hurt more.' Good with teachers who say 'it was nothing'.",
  "THE WEATHER AND THE STORMS: 'The storms are the outbursts, but the weather is grey most days. We need to work on the weather, not just the storms.' Separates mood from outbursts; good with children and families.",
  "THE SMOKE DETECTOR TOO SENSITIVE: 'It goes off for toast. The alarm works — it's just set too sensitive. We turn it down with sleep, calm, predictability and less stress.' Good with older children.",
 ],
 "language": [
  "Attribute any diagnosis: 'X was diagnosed with DMDD by [service], [DD/MM/YYYY].' Note that it is a DSM-5-TR diagnosis without an ICD-11 equivalent, if relevant to other services.",
  "Describe outbursts factually: frequency, duration, setting, trigger, recovery. Avoid: 'explosive', 'volatile', 'rage', 'meltdown' as characterisations of the child.",
  "'Irritability' is the clinical term; in conversation, 'short fuse', 'wound up' or 'cross a lot of the time' is often clearer for families and children.",
  "Do not use 'bipolar' in any school conversation unless quoting a medical report; it is frightening and, for most of these children, not accurate.",
 ],
 "red_flags": [
  "RED FLAG — irritability with low mood, hopelessness, self-harm or talk of death. Same-day risk protocol; DMDD is a mood diagnosis and depression commonly co-occurs.",
  "RED FLAG — outbursts causing injury to the child or others, or requiring physical intervention. Immediate safety planning with the principal and parents; school physical-intervention policy; supervision follows action.",
  "RED FLAG — distinct periods of elevated mood, reduced need for sleep, grandiosity or racing speech. Not DMDD; urgent medical assessment via GP / CAMHS.",
  "RED FLAG — disclosure or signs of abuse, neglect or domestic violence. Children First route the same day; report to Tusla as a mandated person — telling the DLP does not discharge your duty.",
  "BOUNDARY — you do not diagnose DMDD, distinguish it from bipolar disorder, or advise on medication. PSI 2.2.2, 2.2.4.",
  "WATCH — irritability after a clear change (illness, bereavement, family breakdown, bullying). DMDD requires a year's duration and onset before 10; recent onset suggests something else.",
 ],
 "child_voice": [
  "FEELINGS THERMOMETER / 5-POINT SCALE — good because it gives the child a concrete, shared language for mood and lets staff see the build-up the child feels.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — good because it locates the difficult times and relationships from the child's side. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "BODY MAPPING — the child marks where anger and worry show in their body. Good because it builds interoceptive awareness and often surfaces anxiety beneath irritability.",
  "MOOD DIARY (older children, with a key adult) — good because it shows patterns (sleep, days, lessons) the child can use to plan, and it gives them ownership.",
  "DRAWING THE IDEAL SCHOOL (Williams & Hanke, 2007, adapted from Moran's Drawing the Ideal Self) — good because it allows the child to describe what school feels like without being asked directly about outbursts.",
 ],
 "questions": [
  "Q: 'Is DMDD just a new word for tantrums?' — A: 'No. It needs frequent, severe outbursts and an irritable mood most of the time, for at least a year and in more than one place. Ordinary tantrums don't meet that.'",
  "Q: 'Does this mean she'll get bipolar disorder?' — A: 'The research suggests children with this pattern are more likely to have worry or low mood later than bipolar disorder. If anyone has a concern about bipolar disorder, that's a medical question for her doctor.'",
  "Q: 'Why is it with depression in the manual when the problem is behaviour?' — A: 'Because the underlying difficulty is mood — the irritability — and the outbursts are how it shows. That's why support needs to target feelings as well as behaviour.'",
  "Q: 'The report from abroad says DMDD but the Irish service says ODD — which is right?' — A: 'The two systems handle this differently: DSM has DMDD, ICD-11 describes ODD with chronic irritability. The label differs; the child and the support needed are the same.'",
  "Q: 'He's 4 and has huge outbursts — could it be DMDD?' — A: 'The manual says it isn't diagnosed for the first time before 6. We can still support him now, and look at language, sleep and what's going on around the outbursts.'",
  "Q: 'Will medication fix it?' — A: 'That's a decision for his doctor, not me. What I can help with is making school predictable, spotting the build-up, and teaching regulation skills.'",
 ],
 "supervision": [
  "Bring any mood or self-harm concern the same day, and record the action you took first.",
  "Discuss how you distinguish, in your own report, irritability as mood from irritability as response to an environment that does not fit the child.",
  "Ask how your local CAMHS responds to DMDD, ODD and emotional dysregulation — whether terminology affects acceptance.",
  "Rehearse how you explain the DSM / ICD difference to a family holding a report from another jurisdiction.",
  "Reflect on safety planning: who holds it, how physical intervention is governed, and where the EP role stops.",
 ],
 "reflection": [
  "ON MOOD — Did I ask about sadness, worry, sleep and self-harm, or did the outbursts take up the whole assessment?",
  "ON FORMULATION — What keeps this child's irritability high? Did I test learning, language, sensory, anxiety and adversity hypotheses?",
  "ON LANGUAGE — Did my report describe outbursts factually, or did I use 'explosive', 'volatile', 'rage'?",
  "ON THE LABEL — Did I treat DMDD as an explanation, or as a description that still needs formulating?",
  "ON SAFETY — Is there an agreed, reviewed plan for outbursts, and does it protect the child's dignity as well as others' safety?",
  "WHAT GOOD LOOKS LIKE: 'The log showed outbursts clustered on Mondays and after yard. Parents described poor sleep at weekends and a worry about a sibling's illness. RCADS was raised on anxiety. We agreed Monday check-ins, a calm space before yard ends, a feelings scale, and GP referral to CAMHS for mood. Outbursts reduced.'",
  "WHAT POOR LOOKS LIKE: 'Child has DMDD; recommend behaviour plan and reward chart.' — no mood assessment, no formulation, and a compliance-only plan for a mood difficulty.",
 ],
 "citations": [
  CIT_DSM,
  "Leibenluft, E. (2011). Severe mood dysregulation, irritability, and the diagnostic boundaries of bipolar disorder in youths. American Journal of Psychiatry, 168(2), 129–142.",
  "Copeland, W. E., Angold, A., Costello, E. J., & Egger, H. (2013). Prevalence, comorbidity, and correlates of DSM-5 proposed disruptive mood dysregulation disorder. American Journal of Psychiatry, 170(2), 173–179.",
  "Stringaris, A., Vidal-Ribas, P., Brotman, M. A., & Leibenluft, E. (2018). Practitioner review: Definition, recognition, and treatment challenges of irritability in young people. Journal of Child Psychology and Psychiatry, 59(7), 721–739.",
  CIT_STR09,
  "World Health Organization. (2022). ICD-11: International classification of diseases (11th revision). https://icd.who.int/",
  CIT_HOLLO,
  CIT_NEPS,
 ],

 "pathway": {
  "age": "Onset of the criteria must be before age 10, and the diagnosis is not made for the first time before 6 or after 18 (APA, 2022 — verify wording). In practice it is usually named between 6 and 12, after a year or more of daily irritability and frequent outbursts across home and school.",
  "who_diagnoses": "Ireland: CAMHS psychiatrist or clinical psychologist, or a private psychiatrist. It is used less often in Irish services than in the US; the same child may be described as ODD (with chronic irritability-anger under ICD-11), ADHD with emotional dysregulation, or anxiety. The EP does not diagnose it.",
  "who_wrote_report": "CAMHS; a private psychiatrist or clinical psychologist; often a report from the US or another DSM-using jurisdiction for families who have moved. Check which system (DSM or ICD) the clinician used.",
  "refer_to": "CAMHS via GP where irritability, low mood or risk are significant (check current criteria); Primary Care Psychology for milder presentations; SLT where language may be driving frustration; Tusla (Children First) where there is a welfare concern; parenting programme providers for the family.",
  "sooner": "'It's very hard to tell early on whether a child's temper is a phase or something more lasting — the diagnosis itself needs a year of the pattern before it can be made. What matters now is understanding his mood and making the days more manageable.'",
 },
 "differential": [
  "ODD — defiance and anger without the persistent, severe mood component; if DMDD criteria are met, DSM-5-TR says ODD is not diagnosed.",
  "BIPOLAR DISORDER — distinct episodes of elevated mood; DMDD irritability is chronic, not episodic. Medical assessment.",
  "INTERMITTENT EXPLOSIVE DISORDER — outbursts without persistent irritable mood between them.",
  "ADHD WITH EMOTIONAL DYSREGULATION — outbursts linked to impulsivity and frustration; often co-occurs.",
  "AUTISM — meltdowns from sensory overload, change or unpredictability; clinicians consider whether autism better explains the outbursts.",
  "ANXIETY OR DEPRESSION — irritability as the presenting sign of worry or low mood.",
  "ADVERSITY / TRAUMA / RECENT LIFE EVENT — irritability of recent onset or clearly linked to events.",
 ],
 "next": [
  "Screen mood and risk (MFQ, RCADS as age-appropriate) and act the same day on any risk.",
  "Formulate with a named framework; test learning, language, sleep, anxiety and adversity hypotheses.",
  "Agree a School Support Plus plan with preventive, co-regulation and safety elements and a review date.",
  "Refer to CAMHS via GP where mood or risk is significant; tell your supervisor the same day about any risk.",
 ],
 "presentations": [
  "Emotion regulation in the classroom",
  "Escalation and de-escalation pattern",
  "Behaviour that challenges",
  "Response to correction and repair after an incident",
  "Transitions between activities and between classes",
  "Behaviour as communication of an unmet learning need",
 ],

 "bands": {
  "Early Years": {
   "applies": "N/A — DSM-5-TR says DMDD is not diagnosed for the first time before age 6",
   "prevalence": "Not applicable as a diagnosis at this age (APA, 2022).",
   "see": "Frequent, severe tantrums and irritability in preschoolers can be significant and deserve support, but are framed developmentally. Look at language, sleep, sensory needs and the home context; support the parent–child relationship.",
   "tools": ["SDQ (2–4 version)", "Ages & Stages Questionnaires (ASQ-3)", "Preschool Language Scales-5 (PLS-5)", "Functional behaviour assessment (ABC)"],
  },
  "School Age": {
   "applies": "YES — onset must be before 10; most first diagnoses are made in this band",
   "prevalence": "DSM-5-TR estimates about 2–5% in children and adolescents, higher in school-age males (APA, 2022) — check before quoting; no Irish figure stated here.",
   "see": "Daily irritability visible to staff, plus outbursts several times a week that are out of proportion to the trigger. Often co-occurs with ADHD and anxiety. Map outbursts, screen mood and anxiety, and test language and learning needs.",
   "tools": ["SDQ", "BASC-3", "Conners-4", "RCADS", "BRIEF-2", "Functional behaviour assessment (ABC)", "CELF-5 UK", "WIAT-III UK"],
  },
  "Adolescent": {
   "applies": "YES — can be first diagnosed up to 18, but onset must have been before 10",
   "prevalence": "Lower than in school age (APA, 2022) — no figure stated here; check before quoting.",
   "see": "Outbursts may lessen while irritability continues; depression and anxiety become more likely (Leibenluft, 2011). Self-report of mood is essential. A first presentation of irritability in adolescence with no childhood history is not DMDD — look for mood disorder or life events.",
   "tools": ["SDQ", "BASC-3 SRP", "RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Beck Youth Inventories-2", "Conners-4 self-report"],
  },
  "Young Adult": {
   "applies": "RETROSPECTIVE ONLY — DSM-5-TR says DMDD is not diagnosed for the first time after 18",
   "prevalence": "Not applicable as a new diagnosis (APA, 2022).",
   "see": "Appears as a childhood diagnosis in files. Ask about current mood: irritability in adolescence is linked to later depression and anxiety (Stringaris et al., 2018). Signpost to adult or youth mental health services (e.g. Jigsaw, GP) where mood difficulty continues.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "RARELY — outbursts in pupils with ID, autism or limited communication are usually better explained by those needs",
   "prevalence": "Rate not stated here — check before quoting.",
   "see": "Frequent distress and outbursts are common in special settings and usually reflect communication, sensory, pain or environmental factors. Functional assessment, communication review and health checks come first; a mood diagnosis is a clinical decision made cautiously.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3", "Communication Matrix / AAC review"],
  },
 },
})
