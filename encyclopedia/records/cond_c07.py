# CONDS records: Adjustment Disorder, Acute Stress Disorder, Prolonged Grief Disorder.
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c07.py
# All three sit in DSM-5-TR "Trauma- and Stressor-Related Disorders" and ICD-11
# "Disorders specifically associated with stress" (acute stress reaction excepted — see record 2).

CONDS = [

# =====================================================================================
# 1. ADJUSTMENT DISORDER
# =====================================================================================
{
 "name": "Adjustment Disorder",
 "code": "DSM-5-TR Adjustment Disorders (F43.2x — sub-code by specifier; check before quoting) · ICD-11 6B43 Adjustment disorder",
 "neps": "3. EMOTIONAL (3.4 Mood · 3.5 Trauma, attachment and loss) — and 2. BEHAVIOUR where the conduct specifier applies",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Equal Status Acts 2000–2018 · GDPR · Mental Health Act 2001 (context for CAMHS; check current amendments)",

 "what_it_is": [
  "Emotional or behavioural symptoms that develop in response to an IDENTIFIABLE STRESSOR (e.g. parental separation, a house move, a new school, illness, a family member's job loss) and that are out of proportion to the stressor and/or cause significant impairment (APA, 2022, DSM-5-TR).",
  "DSM-5-TR timing: symptoms begin WITHIN 3 MONTHS of the stressor, and once the stressor or its consequences have ended, they do not persist for more than a further 6 MONTHS. Specifiers: with depressed mood · with anxiety · with mixed anxiety and depressed mood · with disturbance of conduct · with mixed disturbance of emotions and conduct · unspecified. Acute (under 6 months) or persistent (APA, 2022).",
  "ICD-11 (6B43) defines it differently: a maladaptive reaction, usually emerging within ONE MONTH of the stressor, with two core features — PREOCCUPATION with the stressor (excessive worry, recurrent distressing thoughts, rumination) and FAILURE TO ADAPT, causing impairment. Symptoms typically resolve within 6 months unless the stressor persists (WHO, 2019; Maercker et al., 2013). ICD-11 dropped the DSM-style subtypes.",
  "It is a RESIDUAL category in DSM-5-TR: it is used only when the picture does not meet criteria for another disorder (e.g. major depression, PTSD) and is not simply a flare of a pre-existing one. It explicitly excludes normal bereavement and Prolonged Grief Disorder (APA, 2022).",
  "The stressor does NOT have to be traumatic. That is the key distinction from PTSD and Acute Stress Disorder, which require exposure to actual or threatened death, serious injury or sexual violence.",
  "It is one of the diagnoses most often given in child and adolescent clinical services, and one of the least researched, partly because the criteria are loose and have limited reliability (Casey & Bailey, 2011; O'Donnell et al., 2019).",
  "For school practice the useful frame is: a child who was coping, met a change, and has not yet regained their footing. The EP's work is mostly about the environment — predictability, relationships, reduced additional load — while watching for risk and for a picture that is becoming something else.",
 ],

 "what_it_is_not": [
  "NOT ordinary distress after a hard event. Upset, irritability, clinginess or a dip in schoolwork after a separation or a move is EXPECTED and usually settles with time and ordinary support. Adjustment disorder requires distress out of proportion and/or significant impairment — do not pathologise normal reactions to adversity (Masten, 2001, on resilience as 'ordinary magic').",
  "NOT 'mild' and therefore safe to ignore. Adjustment disorder in adolescents is associated with suicidal behaviour, sometimes with a short, fast suicidal process (Portzky et al., 2005). Ask about self-harm and suicidal thoughts directly.",
  "NOT a label the EP gives. Diagnosis sits with CAMHS, Primary Care Psychology or a private clinician. The EP describes the change in functioning, formulates what is keeping it going, recommends, and refers where the threshold is met (PSI 2.2.2).",
  "NOT the same as PTSD. If the event involved actual or threatened death, serious injury or sexual violence and the child has intrusions, avoidance and hyperarousal, think trauma first, not adjustment.",
  "NOT a reason to excuse the stressor. If the 'stressor' is ongoing — bullying, domestic violence, neglect, homelessness — the priority is the stressor, including child protection, not the child's 'adjustment' to it.",
  "NOT permanent. By definition it is time-limited; if difficulties persist well beyond 6 months after the stressor has ended, the formulation needs revisiting (depression, anxiety disorder, an unmet learning need, a neurodevelopmental condition surfacing under new demands).",
 ],

 "prevalence": [
  "OVERALL: child and adolescent community prevalence of adjustment disorder is poorly established — rate not stated here, check before quoting. It is frequently diagnosed in clinical and emergency settings (Casey & Bailey, 2011).",
  "IRELAND: no Irish prevalence figure for adjustment disorder in children is given here — check before quoting. Common stressors in referrals (separation, moves, homelessness, migration) are well documented in Irish services.",
  "EARLY YEARS 0–5: can be diagnosed but rarely is; reactions to change are usually understood as developmental (regression, sleep and toileting changes).",
  "SCHOOL AGE 6–12: seen after family change, school moves and illness; behavioural presentations (conduct specifier) are more likely to be referred than quiet mood change.",
  "ADOLESCENT 13–16: commonly used diagnosis in CAMHS and emergency presentations after self-harm; relationship break-ups, exam pressure and family conflict are frequent stressors (Portzky et al., 2005 — check context).",
  "SEX RATIO: not consistently reported — check before quoting.",
 ],

 "cooccurring": [
  {"name": "DEPRESSION / LOW MOOD",
   "rate": "the boundary is often blurred — rate not stated here, check",
   "presents": "low mood, withdrawal, loss of interest after a change. If criteria for major depression are met, that diagnosis takes precedence (APA, 2022). Ask about mood, sleep, appetite and hopelessness."},
  {"name": "ANXIETY",
   "rate": "common, especially the 'with anxiety' specifier — rate not stated here, check",
   "presents": "worry, reassurance-seeking, somatic complaints and clinginess that began with the change. Check whether anxiety pre-dated the stressor; if so the formulation is different."},
  {"name": "EMOTIONALLY BASED SCHOOL AVOIDANCE (EBSA)",
   "rate": "frequent pathway — rate not stated here, check",
   "presents": "late arrivals and absences starting after a move, separation or illness. Attendance data is part of the picture; early, planned re-engagement prevents a pattern setting."},
  {"name": "CONDUCT DIFFICULTY",
   "rate": "defines the 'with disturbance of conduct' specifier",
   "presents": "new rule-breaking, aggression or defiance that began after the stressor. Compare with pre-stressor behaviour reports; a long history points elsewhere."},
  {"name": "SELF-HARM AND SUICIDAL IDEATION",
   "rate": "elevated in adolescents with adjustment disorder (Portzky et al., 2005) — rate not stated here, check",
   "presents": "may appear with little warning after an acute stressor such as a break-up or a disciplinary event. Ask directly; same-day risk route if disclosed."},
  {"name": "UNDERLYING NEURODEVELOPMENTAL OR LEARNING NEED",
   "rate": "not stated — check",
   "presents": "a child with autism, ADHD or dyslexia who managed in one setting and 'falls apart' after a transition. The stressor exposed the need; the adjustment label can hide it."},
  {"name": "SUBSTANCE USE (adolescent)",
   "rate": "not stated — check",
   "presents": "new or increased drinking or cannabis use as coping after a stressor. Ask in a non-judgemental way and include it in the risk picture."},
 ],

 "recommendations": [
  "NAME THE STRESSOR AND THE CHANGE in the report: 'Since [event] on or around [date], [child] has shown…', with before-and-after evidence (attendance, attainment, teacher and parent report). This locates the difficulty in circumstance, not character.",
  "PREDICTABILITY AND ROUTINE: keep school the stable place. Advance notice of changes, a consistent key adult, a visual timetable for younger children. Reduces the uncertainty load the stressor has added.",
  "A NAMED KEY ADULT with a brief, regular check-in (e.g. 5 minutes at the start of the day). Relationship is the main protective factor available in school.",
  "TEMPORARY, TIME-LIMITED FLEXIBILITY: adjusted homework or deadlines for an agreed period with a review date — not indefinite removal of demands, which can feed avoidance.",
  "PROBLEM-SOLVING AND COPING WORK where appropriate: help the young person identify what they can and cannot control about the change. Brief solution-focused or CBT-informed work within service remit.",
  "INFORM KEY STAFF ON A NEED-TO-KNOW BASIS, with parental consent and the young person's view on who knows what. GDPR and the child's dignity both apply.",
  "MONITOR: agree a simple measure (SDQ repeated, a weekly scaling rating, attendance) and a review date at 6–8 weeks. Adjustment difficulty should be improving; if not, re-formulate.",
  "ADDRESS THE STRESSOR where the school can — bullying, a timetable clash, a difficult class placement. Sometimes the intervention is changing the environment, not the child.",
  "CONTINUUM LEVEL: Classroom Support for most; School Support for a targeted plan; School Support Plus where Primary Care, CAMHS or Tusla are involved.",
  "REFER: GP to Primary Care Psychology (mild–moderate) or CAMHS (moderate–severe, risk, or not improving); Jigsaw (12–25) where available; Rainbows Ireland for children affected by separation or loss — check local availability. Tusla if the stressor involves abuse or neglect.",
  "DO NOT write 'adjustment disorder' in an EP report unless citing a clinician's diagnosis, and do not advise on medication. Write 'difficulties adjusting to [change]'. PSI 2.2.2, 1.2.8.",
 ],

 "explain_parent": [
  "'Big changes are hard for children, and most show it for a while — clinginess, temper, sleep changes, a dip at school. That's a normal reaction, and it usually settles as things become predictable again.'",
  "'What we're seeing with him seems bigger or longer than we'd expect, and it's getting in the way of school and friends. That tells me he needs a bit more support to adjust — it doesn't mean something is wrong with him.'",
  "'The things that help most are ordinary ones done consistently: routine, one adult he trusts in school, clear information about what's happening, and being allowed to have feelings about it.'",
  "'Children often protect their parents by not saying how they feel, especially after a separation or an illness in the family. It can help to tell him directly that his feelings won't upset you.'",
  "'If at any point he talks about hurting himself or not wanting to be here, please tell us or your GP the same day. Asking about it directly doesn't put the idea in his head.'",
  "SIGNPOST: GP (Primary Care Psychology or CAMHS if needed); Rainbows Ireland for separation and loss → https://www.rainbowsireland.ie/ ; Jigsaw for 12–25 → https://jigsaw.ie/ ; Barnardos parenting supports — check local availability.",
 ],

 "explain_teacher": [
  "'This started with a change at home. The behaviour is a reaction to that change, not a new personality. That's hopeful — it usually settles with stability.'",
  "'School can be the most predictable place in her week right now. Keep routines steady, warn her about changes, and keep the same adult as her check-in.'",
  "'Temporary flexibility is fine, with an end date. Taking all demands away indefinitely tends to make it harder to come back.'",
  "'Please pass on anything she says about hurting herself or not wanting to be around — the same day, to the DLP. Don't wait to see if it passes.'",
  "'If it isn't improving in six to eight weeks, tell me. That's a sign we're missing something — sometimes the change has exposed a difficulty that was there already.'",
  "'Where the stressor is in school — a falling-out, a class move, bullying — that's something we can actually change.'",
 ],

 "explain_child": [
  "YOUNGER: 'A lot has changed for you. When lots changes, feelings get big and mixed-up — sad, cross, worried, all at once. That happens to lots of children, and it's OK. We're going to make school feel steady while things settle.'",
  "OLDER: 'When something big happens, it's normal for things to feel off for a while — sleep, concentration, mood. For you it's been hanging around longer and making school harder, so we're going to put a few things in place to help while you get your feet back under you.'",
  "ASK: 'What's changed since [event]?' and 'What's stayed the same?' — the second question often finds the protective factors.",
  "ASK: 'Which bits of this can you do something about, and which bits are out of your hands?' — separates problem-solving from acceptance.",
  "ASK ABOUT RISK DIRECTLY where age-appropriate: 'Sometimes when things are this hard, people think about hurting themselves or not wanting to be alive. Has that happened for you?' Same-day risk route if yes.",
 ],

 "analogies": [
  "MOVING HOUSE INSIDE YOUR HEAD: 'All the furniture's been moved. You keep walking into walls that didn't used to be there. It takes a while to learn the new layout.' Works with children and parents after family change.",
  "THE SNOW GLOBE: 'Something shook everything up. The snow settles if you let the globe sit still — that's what routine does.' Good with younger children and with teachers to explain why stability matters.",
  "THE SPRAINED ANKLE: 'It's a real injury, it hurts, and it heals — but it heals better with support and gradual use than by never walking on it.' Good for explaining time-limited adjustments and why not to remove all demands.",
  "THE BACKPACK: 'Everyone carries a backpack. He was coping with his. Then someone added a big rock. He needs help with the load for a while, not a lecture about walking faster.' Good with teachers.",
 ],

 "language": [
  "Use 'difficulties adjusting to…' or 'a reaction to [event]' in EP reports. 'Adjustment disorder' appears only where a clinician has diagnosed it, attributed.",
  "Avoid 'acting out', 'attention-seeking', 'manipulative' — these are interpretations. PSI 1.2.8 requires opinion to be labelled as opinion.",
  "Describe family change neutrally: 'parents have separated', not 'broken home'. Families read reports.",
  "Use the young person's own words for how they feel ('stressed', 'all over the place') in the child's-voice section.",
 ],

 "red_flags": [
  "RED FLAG — any disclosure of self-harm or suicidal ideation. Same-day risk route: inform the DLP, follow the service risk protocol, contact the parent unless doing so increases risk, and ensure a same-day GP / CAMHS / emergency response as indicated. Supervision follows action; it does not replace it.",
  "RED FLAG — the 'stressor' is abuse, neglect, domestic violence or a risk at home. Follow Children First (DCYA, 2017); report to Tusla as soon as practicable. Telling the DLP does not discharge a mandated person's duty.",
  "RED FLAG — the event was traumatic (threat to life, serious injury, sexual violence) and there are intrusions, nightmares, avoidance or hypervigilance. Consider Acute Stress Disorder or PTSD and refer accordingly.",
  "RED FLAG — no improvement, or worsening, beyond about 6 months after the stressor ended. Re-formulate; refer for clinical assessment of depression, anxiety or other conditions.",
  "BOUNDARY — you do not diagnose adjustment disorder or advise on medication. PSI 2.2.2.",
  "WATCH — the 'good' child who copes visibly and deteriorates quietly (sleep, eating, friendships). Ask parents about home as well as school.",
 ],

 "child_voice": [
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — Irish, free, familiar to staff. Good because it shows which parts of the day have become hard since the change. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "BEFORE-AND-AFTER TIMELINE — the child draws or marks 'before [event]' and 'now', then 'how I'd like it to be'. Good because it frames the difficulty as a change in circumstance and generates the child's own goal.",
  "SCALING ('how settled do you feel in school, 0–10?') repeated weekly — good because it gives a monitoring number and a solution-focused follow-up ('what would one point higher look like?').",
  "CIRCLES OF SUPPORT / ECOMAP — who is close, who has moved further away since the change. Good because it shows lost relationships (a friend left behind after a move) that adults miss.",
  "SDQ SELF-REPORT (11–17) — brief, standardised, repeatable. Good as a baseline for review, with risk asked about separately and face to face.",
 ],

 "questions": [
  "Q: 'Isn't it normal to be upset after a separation?' — A: 'Yes, completely. Most children show it for a while and settle. We're looking at whether it's much bigger or longer than expected and getting in the way of school and friendships. That's the point at which extra support makes sense.'",
  "Q: 'Is this a mental illness?' — A: 'Adjustment difficulties are a reaction to a change, and most improve as things settle. If a doctor or clinical team used the term \"adjustment disorder\", it means the reaction is significant enough to need support — and it's expected to be time-limited.'",
  "Q: 'Should we tell the school what's going on at home?' — A: 'It helps if key staff know enough to understand — they don't need details. We can agree together who needs to know and what to say, and ask him what he's comfortable with.'",
  "Q: 'Should she have time off until things calm down?' — A: 'A short break can make sense in an emergency, but staying off tends to make coming back harder. School is often the most stable part of the week. Let's plan the day around what she can manage.'",
  "Q: 'How long will this last?' — A: 'Most reactions to a change settle within months as things become predictable. We'll agree a review date. If it isn't improving, that tells us to look more closely, and I'd want to refer on.'",
  "Q: 'He's being disruptive — is this just an excuse?' — A: 'It's an explanation, not an excuse. The behaviour still needs clear boundaries. Knowing why it started helps us choose responses that settle it rather than escalate it.'",
  "Q: 'Can you diagnose this?' — A: 'No — diagnosis would come from CAMHS, Primary Care Psychology or a clinician. I can describe what's changed, what's keeping it going in school, and put a plan in place.'",
 ],

 "supervision": [
  "Ask where your service draws the line between an expected reaction to adversity and a referral — how do you avoid both pathologising and missing risk?",
  "Clarify the risk protocol step by step for a disclosure of suicidal thoughts during a session: who you phone first, what you record, and what happens if you cannot reach a parent.",
  "Bring a case where the 'stressor' may be ongoing harm at home and talk through your Children First duties as a mandated person.",
  "Discuss how to write about family circumstances in a report that both parents will read, especially after a contentious separation.",
  "Bring a case where the adjustment picture hasn't resolved and ask how your supervisor re-formulates at that point.",
 ],

 "reflection": [
  "ON HOW I EXPLAINED IT — Did I make clear that this is a reaction to circumstance, and that it is expected to improve? Did the parent leave less alarmed and with something to do?",
  "ON NORMALISING VS MINIMISING — Did I normalise distress while still asking about risk? Or did 'it's just a reaction' let me skip the self-harm question?",
  "ON THE STRESSOR — Did I check whether the stressor is still happening, and whether it is something school could change or something that needs a child protection response?",
  "ON LANGUAGE — Did my report describe the family's situation in a way both parents could read without feeling blamed?",
  "ON WHAT THE CHANGE REVEALED — Did I consider whether a learning or neurodevelopmental need was exposed by the transition, rather than caused by it?",
  "WHAT GOOD LOOKS LIKE: 'After the move, the school described him as \"a different child\". I gathered his old school's reports and attendance, which showed a settled pupil. We set up a key adult, a lunchtime club to rebuild friendships, and a six-week review. At review he had one friend and was attending fully; I closed with a note on what to watch for.'",
  "WHAT POOR LOOKS LIKE: 'Presents with adjustment difficulties. Refer to CAMHS.' — no before-and-after evidence, no risk question recorded, no school plan, and a diagnostic-sounding label used by someone who cannot diagnose.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Adjustment Disorders.",
  "World Health Organization. (2019). International classification of diseases (11th rev.) — 6B43 Adjustment disorder. https://icd.who.int/",
  "Maercker, A., Brewin, C. R., Bryant, R. A., Cloitre, M., van Ommeren, M., ... Reed, G. M. (2013). [check full author list] Diagnosis and classification of disorders specifically associated with stress: Proposals for ICD-11. World Psychiatry, 12(3), 198–206.",
  "Casey, P., & Bailey, S. (2011). Adjustment disorders: The state of the art. World Psychiatry, 10(1), 11–18.",
  "O'Donnell, M. L., Agathos, J. A., Metcalf, O., Gibson, K., & Lau, W. (2019). Adjustment disorder: Current developments and future directions. International Journal of Environmental Research and Public Health, 16(14), 2537.",
  "Portzky, G., Audenaert, K., & van Heeringen, K. (2005). Adjustment disorder and the course of the suicidal process in adolescents. Journal of Affective Disorders, 87(2–3), 265–270.",
  "Masten, A. S. (2001). Ordinary magic: Resilience processes in development. American Psychologist, 56(3), 227–238.",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government Publications.",
 ],

 "pathway": {
  "age": "Any age, because it follows a stressor rather than a developmental window. In school referrals it clusters around predictable life events — parental separation, house or school moves, transition to post-primary, illness or death in the family, migration — and in adolescence around relationship break-ups, exam pressure and disciplinary events.",
  "who_diagnoses": "Ireland: CAMHS (moderate–severe, risk, or significant impairment) or HSE Primary Care Psychology (mild–moderate), usually via GP; hospital emergency departments and liaison psychiatry after self-harm; private clinical psychologists and psychiatrists. Check local thresholds; they vary by area. The EP does not diagnose it.",
  "who_wrote_report": "CAMHS psychiatrist, psychologist or team; a hospital liaison psychiatry team after an emergency presentation; Primary Care psychologist; private clinician. A letter mentioning 'adjustment reaction' from a GP is a clinical impression, not a full assessment — ask what was done.",
  "refer_to": "GP as first point for Primary Care Psychology or CAMHS. Same-day emergency route (GP, ED, CAMHS on-call) where suicide risk is present. Jigsaw for 12–25s where available. Rainbows Ireland for separation and loss (check local groups). Tusla where the stressor involves abuse or neglect.",
  "sooner": "'Most children react to big changes and settle without needing anyone like me, so waiting to see was a reasonable thing to do. You've noticed it's lasting longer than you'd expect, and that's exactly the right time to put support in.'",
 },

 "differential": [
  "NORMAL REACTION TO ADVERSITY — distress proportionate to the event and settling over weeks. No disorder; support and monitor.",
  "ACUTE STRESS DISORDER / PTSD — the stressor meets the trauma criterion and there are intrusions, avoidance, arousal. Different pathway.",
  "MAJOR DEPRESSION — full criteria met; takes precedence over adjustment disorder (APA, 2022).",
  "PROLONGED GRIEF DISORDER / NORMAL GRIEF — where the stressor is a death, DSM-5-TR excludes adjustment disorder for normal bereavement; think grief first.",
  "PRE-EXISTING CONDITION FLARING — anxiety, ADHD, autism or a learning need that was managed and is now exposed. Get pre-stressor history.",
  "ONGOING HARM — bullying, abuse, neglect, domestic violence. This is not 'adjustment'; it is a current risk.",
 ],

 "next": [
  "Ask directly about self-harm and suicidal thoughts; act the same day if present.",
  "Establish the stressor, its timing, whether it is ongoing, and pre-stressor functioning (reports, attendance).",
  "Write a time-limited school plan: key adult, predictability, adjusted demands with an end date, review in 6–8 weeks.",
  "Refer via GP to Primary Care Psychology or CAMHS if impairment is significant or not improving; Tusla where harm is suspected.",
 ],

 "presentations": [
  "Reaction to parental separation",
  "Difficulty settling after a school or house move",
  "Transition difficulty at entry to post-primary",
  "Behaviour change after a family illness",
  "Distress after migration or displacement",
  "Low mood after a relationship break-up (adolescent)",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — reactions to change at this age are usually understood developmentally, not diagnostically",
   "prevalence": "Rate at this age not stated here — check before quoting.",
   "see": "Regression (toileting, speech, sleep), clinginess, tantrums or withdrawal after a family change or new setting. Assess through parent and setting report; frame as a reaction to change and focus on consistency of carers and routine.",
   "tools": ["SDQ (2–4 version)"],
  },
  "School Age": {
   "applies": "YES — seen after family change, moves and illness; conduct presentations more often referred",
   "prevalence": "Community rate not established — check before quoting.",
   "see": "A previously settled child becomes tearful, irritable, disruptive or withdrawn; schoolwork and friendships dip; somatic complaints and lateness begin. The before-and-after contrast is the key evidence. Keep asking what else might be going on at home.",
   "tools": ["SDQ", "RCADS", "BASC-3", "Beck Youth Inventories-2"],
  },
  "Adolescent": {
   "applies": "YES — common clinical diagnosis, including after self-harm presentations",
   "prevalence": "Frequently diagnosed in clinical and emergency settings (Casey & Bailey, 2011); community rate — check.",
   "see": "Low mood, anger, dropping grades, school avoidance, substance use or risk-taking after a break-up, family conflict, exam failure or a disciplinary event. The suicidal process can be short (Portzky et al., 2005); ask about risk at every contact.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Beck Youth Inventories-2", "SDQ"],
  },
  "Young Adult": {
   "applies": "YES — adult mental health territory; know the boundary",
   "prevalence": "Rate not stated here — check before quoting.",
   "see": "Difficulty adjusting to college, leaving home, job loss or relationship change; missed lectures, withdrawal, low mood. Refer to GP, college counselling or adult mental health services rather than hold the case.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — change is a major stressor where predictability matters; harder to identify",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Distress, self-injury, aggression or withdrawal after a change of staff, class, transport, respite or home placement. Rule out pain and illness. Rely on observation, functional assessment and informant report; restore predictability first.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3"],
  },
 },
},

# =====================================================================================
# 2. ACUTE STRESS DISORDER
# =====================================================================================
{
 "name": "Acute Stress Disorder",
 "code": "DSM-5-TR Acute Stress Disorder (F43.0 — check before quoting) · ICD-11 has NO equivalent mental disorder: acute stress reaction is QE84, in the chapter on factors influencing health status, and is treated as a normal response",
 "neps": "3. EMOTIONAL (3.5 Trauma, attachment and loss) — NEPS critical incident response where a school-level event",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "A DSM-5-TR diagnosis for trauma reactions in the FIRST MONTH: symptoms last from 3 DAYS to 1 MONTH after exposure to actual or threatened death, serious injury or sexual violence (APA, 2022).",
  "Exposure can be direct, witnessing it happen to others, LEARNING that it happened to a close family member or friend (violent or accidental in the case of death), or repeated exposure to aversive details (APA, 2022). A classmate's sudden death can qualify for some pupils.",
  "DSM-5-TR requires NINE or more of 14 symptoms across five groups: intrusion (memories, dreams, flashbacks, distress at reminders), negative mood, dissociation (altered sense of reality, amnesia for parts of the event), avoidance, and arousal (sleep, irritability, hypervigilance, concentration, startle). Check the manual for exact wording before quoting.",
  "ICD-11 took a different view: acute stress reaction (QE84) is NOT a mental disorder. It describes transient emotional, somatic, cognitive or behavioural symptoms after an extreme event, considered within the normal range and expected to subside within days (WHO, 2019; Maercker et al., 2013).",
  "The practical message from both systems: most children and adults show stress reactions after a frightening event, and most recover naturally. In a meta-analysis of child studies, PTSD prevalence roughly halved over the first months after trauma (Hiller et al., 2016 — check figures).",
  "ASD was introduced partly to identify people who would go on to develop PTSD. It does that poorly: many who develop PTSD never met ASD criteria, in adults (Bryant, 2011) and in injured children (Kassam-Adams & Winston, 2004). Monitoring over time is more useful than a one-off label.",
  "For the EP, the relevant work is almost always SYSTEMIC in the first month — supporting the school's critical incident response, psychological first aid, routine, information and monitoring — not individual assessment or trauma processing.",
 ],

 "what_it_is_not": [
  "NOT the normal first reaction. Shock, tearfulness, poor sleep, jumpiness and not wanting to talk in the first days after a frightening event are EXPECTED. Do not pathologise them (WHO, 2019, acute stress reaction).",
  "NOT a reason for individual debriefing. Single-session psychological debriefing that asks people to recount the event in detail does not prevent PTSD and may do harm (Rose et al., 2002; NICE, 2018). NEPS critical incident guidance also takes this line — check current wording.",
  "NOT PTSD. PTSD cannot be diagnosed until symptoms have lasted more than a month. If symptoms persist beyond one month, the question becomes PTSD, not ASD (APA, 2022).",
  "NOT only for the child who was physically there. A child who learned that a parent or close friend was killed or seriously hurt can meet the exposure criterion; a child who watched news coverage of strangers generally does not (media exposure counts only if work-related in DSM-5-TR — check).",
  "NOT an adjustment disorder. Adjustment disorder follows any stressor; ASD requires a trauma-level event and a specific symptom set.",
  "NOT something the EP assesses by interviewing the child about the event. The priorities are safety, calm, connection, information and monitoring (Hobfoll et al., 2007).",
 ],

 "prevalence": [
  "OVERALL: rates vary widely with the type of trauma and sample — rate not stated here, check before quoting. Interpersonal violence tends to produce higher rates than accidents.",
  "CHILDREN: studies of injured children and assault or accident survivors report ASD in a minority (e.g. Kassam-Adams & Winston, 2004) — check figures before quoting.",
  "IRELAND: no Irish child prevalence figure given here — check before quoting.",
  "EARLY YEARS 0–5: DSM-5-TR ASD has no preschool-specific criteria (unlike PTSD, which has a preschool subtype); rarely diagnosed.",
  "SCHOOL AGE AND ADOLESCENT: seen after road traffic collisions, assaults, dog attacks, house fires, sudden deaths witnessed or learned about.",
  "COURSE: natural recovery is the majority outcome in the first months (Hiller et al., 2016 — check).",
 ],

 "cooccurring": [
  {"name": "POSTTRAUMATIC STRESS DISORDER (subsequent)",
   "rate": "ASD is an imperfect predictor (Bryant, 2011; Kassam-Adams & Winston, 2004) — rate not stated here, check",
   "presents": "symptoms continuing past one month: intrusions, avoidance, negative mood and arousal still impairing. Re-assess at one month and refer for trauma-focused assessment if persisting."},
  {"name": "TRAUMATIC GRIEF",
   "rate": "common when the event involved a death — rate not stated here, check",
   "presents": "trauma symptoms tangled with grief: the child cannot think about the person without the images of how they died. Grief support alone may not be enough; flag to CAMHS or Primary Care."},
  {"name": "ANXIETY",
   "rate": "elevated — rate not stated here, check",
   "presents": "new fears linked to the event (cars, dogs, fire, being apart from a parent), clinginess, reassurance-seeking. Gentle, graded return to normal routines helps; avoidance maintains."},
  {"name": "LOW MOOD / DEPRESSION",
   "rate": "elevated — rate not stated here, check",
   "presents": "withdrawal, hopelessness, loss of interest. Ask directly about self-harm and suicidal thoughts; same-day risk route if disclosed."},
  {"name": "SLEEP DIFFICULTY",
   "rate": "very common in the first weeks",
   "presents": "nightmares, fear of the dark, wanting to sleep with a parent, tiredness in class. Expected early; persistence beyond a month is a signal to refer."},
  {"name": "EBSA",
   "rate": "possible, especially if the event happened at or near school — rate not stated here, check",
   "presents": "reluctance to return to the place, or the route, where it happened. Plan return early with a key adult; long absence makes return harder."},
  {"name": "PRE-EXISTING DIFFICULTIES",
   "rate": "prior adversity and mental health difficulty raise risk — check",
   "presents": "a child already known for anxiety, trauma history or neurodevelopmental need may react more strongly or differently. Identify these children early in a critical incident response."},
 ],

 "recommendations": [
  "SUPPORT THE SYSTEM FIRST: in a school-level event, help the school follow its Critical Incident Management Plan and the NEPS guidance (NEPS, 2016, Responding to Critical Incidents: Guidelines and Resource Materials for Schools — check for updates). Clear information to staff, pupils and parents; normal routine as far as possible.",
  "PSYCHOLOGICAL FIRST AID, not debriefing: promote a sense of SAFETY, CALMING, SELF- AND COMMUNITY EFFICACY, CONNECTEDNESS and HOPE — the five essential elements (Hobfoll et al., 2007; WHO et al., 2011).",
  "DO NOT ASK CHILDREN TO RECOUNT THE EVENT IN DETAIL. Let them talk if they want to; listen, give accurate information, correct misconceptions. Group debriefing is not recommended (Rose et al., 2002; NICE, 2018).",
  "NORMALISE REACTIONS in age-appropriate language, for pupils and parents: what is expected in the first days and weeks, and what would be a reason to seek help. NEPS handouts cover this — check current versions.",
  "IDENTIFY VULNERABLE PUPILS: those directly involved, close friends, siblings, those with previous loss or trauma, those already on the Continuum. Monitor them through a named key adult.",
  "ACTIVE MONITORING ('watchful waiting'): agree a check at about one month. NICE (2018) supports active monitoring where symptoms are mild in the first month, with referral for trauma-focused CBT where symptoms are significant — check the guideline's current wording.",
  "PRACTICAL ADJUSTMENTS for a limited period: reduced homework, a quiet space, permission to leave class, flexible exam arrangements if timing clashes. With a review date.",
  "CONTINUUM LEVEL: Classroom Support for most pupils after a school-level event; School Support for identified vulnerable pupils; School Support Plus where Primary Care or CAMHS become involved.",
  "REFER: GP to Primary Care Psychology or CAMHS if symptoms are severe, include dissociation or risk, or persist beyond one month. Same-day route for suicidal ideation or self-harm. Tusla where the event involved abuse or violence in the home.",
  "DO NOT diagnose, do not advise on medication, and do not begin trauma-processing work outside your competence and remit. PSI 2.2.2.",
 ],

 "explain_parent": [
  "'What she went through was frightening. It's normal to see nightmares, jumpiness, clinginess or not wanting to talk about it in the first days and weeks. Those are signs her mind is working through something big — not signs of damage.'",
  "'Most children settle over the following weeks with ordinary things: routine, sleep, time with people who love them, and honest, simple information about what happened.'",
  "'You don't need to make her talk about it. Let her know she can, answer questions truthfully and simply, and follow her lead.'",
  "'If things are still very hard after about a month — nightmares every night, refusing to go places, very jumpy, or she seems \"not there\" at times — that's the time to ask your GP for a referral. There are good, specific treatments for children.'",
  "'If she ever says she wants to hurt herself or not be alive, please contact your GP or the emergency services that day.'",
  "SIGNPOST: GP; NEPS critical incident handouts for parents (via the school); HSE mental health information → https://www2.hse.ie/mental-health/ — check current links.",
 ],

 "explain_teacher": [
  "'In the first few weeks, reactions like poor concentration, jumpiness, tearfulness and tiredness are expected. They are not misbehaviour and they usually ease.'",
  "'Routine is protective. Keep the day as normal as you can, with a bit of flexibility and somewhere quiet to go.'",
  "'Please don't ask the class to describe what happened or write about it in detail. Answer questions honestly and simply, and correct rumours.'",
  "'Keep an eye on the children who were closest to it and those who've had losses before. Note anything that's getting worse rather than better.'",
  "'At around a month, tell me which children are still struggling. That's when we decide who needs more than ordinary support.'",
  "'Look after yourselves too. Staff reactions are normal, and the NEPS guidance includes staff support.'",
 ],

 "explain_child": [
  "YOUNGER: 'Something scary happened. When scary things happen, our bodies and brains stay on \"alert\" for a while — bad dreams, jumpy tummies, wanting to be near grown-ups. That's your brain trying to keep you safe. It usually calms down, and grown-ups are here to help.'",
  "OLDER: 'After something like this, it's really common to have flashbacks, trouble sleeping, feel on edge or a bit unreal. It's your brain's alarm system still going. For most people it settles over a few weeks. If it doesn't, there's help that works.'",
  "GIVE CONTROL: 'You don't have to talk about what happened. If you want to, I'll listen. If you have questions, I'll answer them honestly.'",
  "ASK: 'What helps you feel calm?' and 'Who do you like having near you right now?' — builds on existing coping and connection.",
  "ASK ABOUT RISK DIRECTLY where age-appropriate and indicated: 'Sometimes after something awful, people feel so bad they think about hurting themselves. Has that happened?' Same-day risk route if yes.",
 ],

 "analogies": [
  "THE SMOKE ALARM AFTER A REAL FIRE: 'There was a real fire, so the alarm is extra sensitive for a while. It goes off at toast. Over time it resets.' Good with children and parents; explains hyperarousal and why it usually settles.",
  "THE UNFILED MEMORY: 'The memory hasn't been filed away yet, so it keeps falling off the desk — in dreams, in flashes. The brain files it over time. Sometimes it needs help to do that.' Good with older children and adolescents; explains intrusions and why referral helps if it doesn't settle.",
  "THE SNOW GLOBE (for schools): 'The event shook everyone. Routine lets the snow settle. Shaking it again — lots of talking about the details — keeps it stirred up.' Good with staff to explain why not to debrief.",
  "THE CUT THAT HEALS: 'Most cuts heal with a clean plaster and time. A few get infected and need a doctor. We watch to see which is which — we don't send everyone to hospital.' Good for explaining watchful waiting to parents and principals.",
 ],

 "language": [
  "Prefer 'stress reactions' or 'reactions to a frightening event' in school communication. 'Acute stress disorder' only where a clinician has diagnosed it, attributed.",
  "Avoid 'traumatised' as a blanket description of a class or school. Most children exposed to a frightening event are not left with a disorder, and the word can shape expectations.",
  "Avoid 'over-reacting', 'attention-seeking' or 'milking it'. Reactions vary widely and are not chosen.",
  "Use the child's words for their experience ('scared', 'weird', 'can't stop thinking about it').",
 ],

 "red_flags": [
  "RED FLAG — suicidal ideation or self-harm, including after a suicide in the school community (risk of contagion). Same-day risk route: DLP, service risk protocol, parent unless it increases risk, same-day GP / CAMHS / emergency response. Supervision follows action; it does not replace it.",
  "RED FLAG — the traumatic event was abuse or violence in the home or community, or the child is still unsafe. Follow Children First (DCYA, 2017); report to Tusla as soon as practicable. Telling the DLP does not discharge a mandated person's duty.",
  "RED FLAG — marked dissociation (appearing absent, not remembering large parts of the day), inability to function, or not eating or sleeping at all. Refer promptly via GP; do not wait a month.",
  "RED FLAG — symptoms not easing, or worsening, at one month. Refer for assessment of PTSD.",
  "BOUNDARY — you do not diagnose ASD, you do not conduct trauma-focused therapy outside your competence and remit, and you do not advise on medication. PSI 2.2.2.",
  "WATCH — your own reactions and those of school staff after a critical incident. Seek supervision and support.",
 ],

 "child_voice": [
  "CHOICE-BASED CHECK-INS — offer to talk, draw or just sit with a trusted adult. Good because control was taken away by the event; giving choice back is part of recovery.",
  "FEELINGS THERMOMETER or SCALING (0–10 for 'how worried / how jumpy today') — good because it tracks change over the first month without asking about the event itself.",
  "WORRY BOX or QUESTION BOX in class after a school-level event — good because it lets children ask questions anonymously so adults can correct misinformation and rumour.",
  "CHILDREN'S REVISED IMPACT OF EVENT SCALE (CRIES-8/13; Perrin et al., 2005) — brief self-report of intrusion and avoidance for children about 8+. Good as a monitoring screen at one month, used by or with advice from a qualified clinician — check current version and guidance.",
  "PARENT DIARY for younger children — sleep, play themes, clinginess. Good because young children show stress in play and behaviour more than words.",
 ],

 "questions": [
  "Q: 'Should we get someone in to talk to all the children about what happened?' — A: 'Not a detailed debrief — the evidence says that doesn't prevent problems and can make things worse. What helps is clear information, normal routine, and adults who are available to listen. The NEPS guidance sets out how to do that.'",
  "Q: 'Is she traumatised?' — A: 'She's been through something frightening and she's showing normal stress reactions. Most children settle over the next few weeks. We'll keep an eye on her and, if things aren't easing after a month, we'll look at a referral.'",
  "Q: 'Should I make him talk about it?' — A: 'No. Let him know he can, answer his questions honestly, and follow his lead. Some children talk through play or drawing rather than words.'",
  "Q: 'Should she stay off school?' — A: 'A day or two can make sense, but routine and friends are protective. Returning with some flexibility usually helps more than staying away.'",
  "Q: 'Can you do some therapy with her?' — A: 'If her symptoms continue, the right help is a trauma-focused approach from a clinical team — I'd refer through the GP. My role is to help school support her and to watch how she's doing.'",
  "Q: 'He wasn't even there — why is he so upset?' — A: 'Learning that something terrible happened to someone close can affect a child as strongly as being there. His reaction makes sense.'",
  "Q: 'When should we worry?' — A: 'If things are getting worse rather than better, if it's still very hard after about a month, if he seems to switch off or not be there, or if he talks about hurting himself — that last one the same day.'",
 ],

 "supervision": [
  "Ask how your service responds to critical incidents: who from NEPS attends, what the EP does in the first 24–72 hours, and where the trainee fits.",
  "Rehearse the conversation with a principal who wants 'counselling for everyone' — how to say no to debriefing and yes to what helps.",
  "Clarify when your service refers individual children at one month, and to whom.",
  "Bring your own reaction to a critical incident. Vicarious distress is expected; supervision is where it is processed.",
  "Discuss suicide postvention: safe messaging, memorials, identifying at-risk pupils, and liaison with HSE Resource Officers for Suicide Prevention — check local arrangements.",
 ],

 "reflection": [
  "ON HOW I EXPLAINED IT — Did staff and parents leave understanding that most reactions are normal and time-limited, and knowing exactly what would be a reason to refer?",
  "ON DEBRIEFING — Was I under pressure to 'do something' individually, and did I resist doing something unhelpful?",
  "ON THE VULNERABLE FEW — Did the response identify the pupils most at risk (closest, previously bereaved, already struggling), or treat everyone the same?",
  "ON RISK — After a death by suicide, did I make sure the school had thought about contagion and safe messaging?",
  "ON MY OWN RESPONSE — What did this event stir in me, and did it affect how I worked?",
  "WHAT GOOD LOOKS LIKE: 'The school wanted every class to talk through the accident. We agreed a factual statement, class teachers read it, children could ask questions, and a quiet room was staffed. We listed eleven pupils to monitor. At four weeks, two were still struggling and were referred via GP; the rest had settled.'",
  "WHAT POOR LOOKS LIKE: 'Group session held where pupils described what they saw. All pupils offered individual sessions.' — debriefing that the evidence advises against, no monitoring plan, no identification of who needs more.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Acute Stress Disorder.",
  "World Health Organization. (2019). International classification of diseases (11th rev.) — QE84 Acute stress reaction. https://icd.who.int/",
  "Bryant, R. A. (2011). Acute stress disorder as a predictor of posttraumatic stress disorder: A systematic review. Journal of Clinical Psychiatry, 72(2), 233–239.",
  "Kassam-Adams, N., & Winston, F. K. (2004). Predicting child PTSD: The relationship between acute stress disorder and PTSD in injured children. Journal of the American Academy of Child & Adolescent Psychiatry, 43(4), 403–411.",
  "Hiller, R. M., Meiser-Stedman, R., Fearon, P., Lobo, S., McKinnon, A., Fraser, A., & Halligan, S. L. (2016). Research review: Changes in the prevalence and symptom severity of child post-traumatic stress disorder in the year following trauma — a meta-analytic study. Journal of Child Psychology and Psychiatry, 57(8), 884–898.",
  "Hobfoll, S. E., Watson, P., Bell, C. C., Bryant, R. A., Brymer, M. J., Friedman, M. J., ... Ursano, R. J. (2007). Five essential elements of immediate and mid-term mass trauma intervention: Empirical evidence. Psychiatry, 70(4), 283–315.",
  "Rose, S., Bisson, J., Churchill, R., & Wessely, S. (2002). Psychological debriefing for preventing post traumatic stress disorder (PTSD). Cochrane Database of Systematic Reviews, (2), CD000560.",
  "National Institute for Health and Care Excellence. (2018). Post-traumatic stress disorder (NICE guideline NG116). NICE.",
  "National Educational Psychological Service. (2016). Responding to critical incidents: Guidelines and resource materials for schools. Department of Education and Skills. — check for updates.",
  "World Health Organization, War Trauma Foundation, & World Vision International. (2011). Psychological first aid: Guide for field workers. WHO.",
  "Perrin, S., Meiser-Stedman, R., & Smith, P. (2005). The Children's Revised Impact of Event Scale (CRIES): Validity as a screening instrument for PTSD. Behavioural and Cognitive Psychotherapy, 33(4), 487–498.",
 ],

 "pathway": {
  "age": "Any age after a traumatic event, by definition within the first month. School-age children and adolescents are the ones most likely to be described this way; DSM-5-TR has no preschool-specific ASD criteria. In practice most children are never formally diagnosed, because the month passes before any assessment, and the question becomes whether PTSD is developing.",
  "who_diagnoses": "Ireland: rarely formally diagnosed. When it is, usually by a hospital team (paediatric liaison, ED) after an injury or assault, by CAMHS, or by a private clinician. Primary Care Psychology may see children in the first month after a trauma. The EP does not diagnose it.",
  "who_wrote_report": "A hospital paediatric or liaison psychiatry team after an injury; CAMHS; a private clinical psychologist; occasionally a GP letter describing 'acute stress reaction'. A school or NEPS critical incident note is not a diagnostic report.",
  "refer_to": "GP to Primary Care Psychology or CAMHS if symptoms are severe, include dissociation or risk, or persist beyond one month. Same-day emergency route for suicide risk. NEPS critical incident support for school-level events. Tusla where abuse or violence is involved.",
  "sooner": "'In the first weeks after something like this, waiting and watching is actually the recommended approach — most children settle with support at home and school. You haven't missed anything. If it's still hard at a month, that's when we act.'",
 },

 "differential": [
  "NORMAL ACUTE STRESS REACTION — transient, expected, easing over days to weeks (ICD-11 QE84). Support and monitor.",
  "PTSD — the same kind of symptoms lasting MORE than one month (APA, 2022).",
  "ADJUSTMENT DISORDER — reaction to a non-traumatic stressor, or to a traumatic event without the ASD symptom pattern.",
  "TRAUMATIC OR COMPLICATED GRIEF — where a death is involved; grief and trauma interact.",
  "HEAD INJURY OR MEDICAL CAUSE — after an accident, confusion, memory gaps or irritability may be neurological. Medical review via GP.",
  "PRE-EXISTING ANXIETY OR TRAUMA — reactivated by the new event; get the history.",
 ],

 "next": [
  "Check immediate safety and ask about risk; same-day route if self-harm or suicidal ideation is disclosed.",
  "Support the school's critical incident response using the NEPS guidance; psychological first aid, not debriefing.",
  "List vulnerable pupils and name a key adult for each; set a one-month review.",
  "Refer via GP to Primary Care Psychology or CAMHS if symptoms are severe or persist beyond one month.",
 ],

 "presentations": [
  "Stress reaction after a critical incident in school",
  "Reaction after a road traffic collision or injury",
  "Reaction after witnessing violence",
  "Reaction to learning of a sudden death",
  "Nightmares and sleep disruption after a frightening event",
  "New fears linked to a specific event",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — DSM-5-TR ASD has no preschool-specific criteria; reactions are observed rather than diagnosed",
   "prevalence": "Rate not stated here — check before quoting.",
   "see": "Clinginess, regression, sleep disturbance, re-enacting the event in play, new fears. Support through parents and setting; routine and a calm adult are the intervention. Refer via GP if severe or persisting beyond a month (consider the PTSD preschool subtype).",
   "tools": ["SDQ (2–4 version)"],
  },
  "School Age": {
   "applies": "YES — after accidents, assaults, fires, sudden deaths witnessed or learned about",
   "prevalence": "A minority of exposed children in published samples (Kassam-Adams & Winston, 2004) — check figures.",
   "see": "Nightmares, jumpiness, poor concentration, avoidance of reminders (the road, the place, the topic), clinginess, somatic complaints, sometimes seeming 'switched off'. Monitor through the first month rather than assess the event.",
   "tools": ["SDQ", "RCADS", "Children's Revised Impact of Event Scale (CRIES-8/13; Perrin et al., 2005) — AGE about 8–18 · MEASURES: intrusion, avoidance (and arousal in the 13-item version) after a specific event · CANNOT TELL YOU: diagnosis; not valid in the first days · TIME: about 5 min — check current version and cut-off guidance"],
  },
  "Adolescent": {
   "applies": "YES — including after peer deaths, assaults and online-shared traumatic content involving people they know",
   "prevalence": "Rate not stated here — check before quoting.",
   "see": "Intrusive images, sleep loss, irritability, withdrawal, risk-taking or substance use as coping, feeling unreal. Self-report possible; ask about self-harm, especially after a suicide in the peer group.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Children's Revised Impact of Event Scale (CRIES-8/13; Perrin et al., 2005) — AGE about 8–18 · MEASURES: intrusion, avoidance (and arousal in the 13-item version) · CANNOT TELL YOU: diagnosis · TIME: about 5 min — check current version"],
  },
  "Young Adult": {
   "applies": "YES — adult mental health territory; know the boundary",
   "prevalence": "Rate not stated here — check before quoting.",
   "see": "As for adults: intrusions, dissociation, avoidance and arousal in the first month. Refer to GP, college counselling or adult mental health; psychological first aid principles apply.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — reactions happen but are harder to read where language is limited",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Change in behaviour after an event: distress, self-injury, sleep change, avoidance of places or people, regression in skills. Rule out injury and pain. Rely on observation and informant report; restore routine and familiar staff.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3"],
  },
 },
},

# =====================================================================================
# 3. PROLONGED GRIEF DISORDER
# =====================================================================================
{
 "name": "Prolonged Grief Disorder",
 "code": "DSM-5-TR Prolonged Grief Disorder (F43.81 — ICD-10-CM code in use since 01/10/2022; early DSM-5-TR printings show F43.8) · ICD-11 6B42 Prolonged grief disorder",
 "neps": "3. EMOTIONAL (3.5 Trauma, attachment and loss) — NEPS critical incident response where a death affects the school community",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "A grief response that is INTENSE, PERSISTENT and IMPAIRING well beyond what is expected in the person's social, cultural and religious context. New to both systems: ICD-11 (6B42; WHO, 2019) and DSM-5-TR (APA, 2022).",
  "DURATION DIFFERS BETWEEN SYSTEMS — hold this: DSM-5-TR requires that the death was at least 12 MONTHS ago for adults and at least 6 MONTHS ago for CHILDREN AND ADOLESCENTS. ICD-11 uses at least 6 MONTHS for all ages, with a note that this may vary with cultural and contextual norms (APA, 2022; WHO, 2019; Prigerson et al., 2021).",
  "DSM-5-TR core: intense YEARNING for the person and/or PREOCCUPATION with thoughts or memories of them (in children and adolescents, preoccupation may focus on the circumstances of the death), most days, for at least the last month; PLUS at least three of eight — identity disruption, marked disbelief, avoidance of reminders, intense emotional pain, difficulty reintegrating into life, emotional numbness, feeling life is meaningless, intense loneliness (APA, 2022 — check exact wording).",
  "ICD-11 core: persistent and pervasive LONGING for or PREOCCUPATION with the deceased, accompanied by intense emotional pain (e.g. sadness, guilt, anger, denial, difficulty accepting the death, feeling one has lost part of oneself), with significant impairment (WHO, 2019).",
  "Most bereaved children and young people do NOT develop PGD. Grief in children is normal, fluctuating and revisited at new developmental stages. In a study of youth bereaved by sudden parental death, most followed declining-grief trajectories and a minority showed persistently high grief (Melhem et al., 2011 — check proportions).",
  "Normal children's grief is often described as 'PUDDLE JUMPING': in and out of intense sadness, then playing minutes later (Winston's Wish, UK). This is not denial and not a lack of feeling.",
  "Useful models for school staff: the DUAL PROCESS MODEL — healthy grief oscillates between loss-oriented and restoration-oriented coping (Stroebe & Schut, 1999); CONTINUING BONDS — maintaining a connection to the person who died is normal, not a failure to 'let go' (Klass et al., 1996).",
 ],

 "what_it_is_not": [
  "NOT normal grief. Sadness, crying, anger, guilt, poor concentration, regression and questions about death are EXPECTED, including months later and at anniversaries, birthdays, Christmas and exam times. Do not pathologise ordinary grief (ICBN, Childhood Bereavement Care Pyramid).",
  "NOT diagnosable early. Before 6 months (child) or 12 months (adult, DSM-5-TR) it is not PGD under DSM-5-TR, however intense. Before 6 months it is not PGD under ICD-11 either. Check dates before anyone uses the term.",
  "NOT depression, although they can co-occur. PGD centres on yearning and preoccupation with the person; depression is pervasive low mood and loss of interest across life (APA, 2022).",
  "NOT something every bereaved child needs a professional for. The Irish Childhood Bereavement Care Pyramid is explicit: MOST children are supported by family and community with honest information and emotional support; SOME need extra help; a FEW need specialist support (ICBN).",
  "NOT helped by protecting children from the truth. Vague euphemisms ('gone to sleep', 'lost') confuse young children and can create fear. Honest, age-appropriate language helps (Dyregrov, 2008).",
  "NOT 'moving on' as the goal. Continuing bonds — talking about the person, keeping objects, marking anniversaries — are healthy (Klass et al., 1996). What matters is whether the young person can also re-engage with life.",
  "NOT the EP's diagnosis to make. The EP supports the school, describes, formulates and refers. PSI 2.2.2.",
 ],

 "prevalence": [
  "ADULTS: a meta-analysis estimated prolonged grief in roughly one in ten adults bereaved by natural causes (Lundorff et al., 2017 — check figure and definitions before quoting).",
  "CHILDREN AND ADOLESCENTS: rate not stated here — check before quoting. Studies using different criteria give different figures; a minority of bereaved youth show persistently high grief (Melhem et al., 2011).",
  "IRELAND: number of bereaved children in Ireland — rate not stated here, check ICBN materials before quoting.",
  "HIGHER RISK: sudden or violent deaths, suicide, death of a parent or sibling, multiple losses, a surviving parent struggling, and prior mental health difficulty — check specific sources before quoting effect sizes.",
  "EARLY YEARS 0–5: rarely diagnosed; young children's grief shows in behaviour and play.",
  "SEX RATIO: not stated here — check before quoting.",
 ],

 "cooccurring": [
  {"name": "DEPRESSION",
   "rate": "frequently co-occurs — rate not stated here, check",
   "presents": "low mood and loss of interest spreading beyond the loss itself; hopelessness about the future. Ask about suicidal thoughts directly, including thoughts of wanting to be with the person who died."},
  {"name": "PTSD / TRAUMATIC GRIEF",
   "rate": "elevated after sudden, violent or witnessed deaths — rate not stated here, check",
   "presents": "intrusive images of the death, avoidance, nightmares that block ordinary grieving. Needs trauma-informed clinical input; flag to CAMHS or Primary Care (Cohen et al., 2017)."},
  {"name": "SEPARATION ANXIETY",
   "rate": "common in younger children after a parent's death — rate not stated here, check",
   "presents": "fear that the surviving parent will die, clinging at drop-off, checking phones, refusing to go on trips. Understandable; plan reassurance and graded separation with the family."},
  {"name": "EBSA",
   "rate": "possible — rate not stated here, check",
   "presents": "not wanting to leave home, or staying close to a surviving parent. Plan a supported return; long absence isolates the child from peers and routine."},
  {"name": "SELF-HARM AND SUICIDAL IDEATION",
   "rate": "elevated after bereavement by suicide — rate not stated here, check",
   "presents": "'I want to be with Dad', giving things away, sudden calm after distress. Same-day risk route. After a suicide in the school community, NEPS guidance on identifying at-risk pupils applies."},
  {"name": "ACADEMIC DECLINE AND CONCENTRATION DIFFICULTY",
   "rate": "common in grief generally — rate not stated here, check",
   "presents": "falling grades, unfinished work, forgetfulness. Expected in early grief; persisting and worsening beyond the first year warrants review. Consider exam accommodations (check SEC criteria)."},
  {"name": "PRE-EXISTING NEURODEVELOPMENTAL NEED",
   "rate": "not stated — check",
   "presents": "an autistic child may grieve through routine disruption, questions about facts, or apparent lack of reaction. Adapt explanations to be concrete; do not read a different expression as absence of grief."},
 ],

 "recommendations": [
  "START FROM NORMAL: in most referrals, write about a bereaved child showing grief, not a disorder. Support at Classroom Support level with honest information, routine and a key adult — ICBN Pyramid 'most' level.",
  "SCHOOL-LEVEL DEATH: support the school to follow its Critical Incident Management Plan and NEPS (2016) Responding to Critical Incidents: Guidelines and Resource Materials for Schools — check for updates. Accurate information, consistent message, parental liaison, identify vulnerable pupils.",
  "A NAMED KEY ADULT and a 'time-out' card or quiet space. Grief comes in waves; a planned exit is better than a public breakdown.",
  "PLAN FOR TRIGGER DATES: anniversaries, birthdays, Mother's/Father's Day activities, Christmas, the funeral anniversary, exams. Ask the family what the child wants; offer alternatives for class activities that assume a living parent.",
  "HONEST, CONCRETE LANGUAGE: use 'died' and 'dead', not euphemisms, especially with younger children and autistic pupils (Dyregrov, 2008).",
  "ALLOW CONTINUING BONDS: a memory box, talking about the person, a photo in the pencil case. These are healthy (Klass et al., 1996).",
  "EXAMS AND WORKLOAD: temporary flexibility with review; for State examinations, consult the school on SEC procedures for bereavement — check current SEC circulars before advising.",
  "IF GRIEF IS NOT EASING after 6–12 months and is impairing — persistent yearning or preoccupation, inability to re-engage — describe it, and REFER via GP to Primary Care Psychology or CAMHS for clinical assessment. Specialist grief support: check local services (e.g. Barnardos Children's Bereavement Service; Rainbows Ireland peer support; Pieta for suicide bereavement — check eligibility and ages).",
  "CONTINUUM LEVEL: Classroom Support for most; School Support where grief is affecting learning or attendance; School Support Plus where Primary Care, CAMHS or a specialist bereavement service is involved.",
  "DO NOT offer bereavement therapy outside your competence and service remit, and do not use the term 'prolonged grief disorder' unless citing a clinician's diagnosis. PSI 2.2.2, 1.2.8.",
 ],

 "explain_parent": [
  "'Children grieve differently from adults. They can be sobbing one minute and playing the next — people call it puddle-jumping. That's normal; it's how children manage something too big to hold all at once.'",
  "'Grief often comes back at new ages. A child who was six when her dad died may grieve again at ten or fourteen, because she understands it differently. That isn't going backwards.'",
  "'Most children, with honest information and people who love them around them, find a way to carry the loss. It doesn't mean forgetting — keeping him in the family's conversations is healthy.'",
  "'What would make me want more help for her is if, a good while on, she's still consumed by missing him every day, can't take part in things, or life seems pointless to her. Then I'd suggest going to your GP for a referral.'",
  "'Please look after yourself too. Children take a lot of their cue from how the adults around them are coping, and it's fine for them to see you sad.'",
  "SIGNPOST: Irish Childhood Bereavement Network → https://www.childhoodbereavement.ie/ ; Barnardos Children's Bereavement Service; Rainbows Ireland → https://www.rainbowsireland.ie/ ; Pieta (suicide bereavement) → https://www.pieta.ie/ — check current services and eligibility.",
 ],

 "explain_teacher": [
  "'Grief in children comes in waves. Expect good days and bad days, poor concentration, and strong reactions to small things. That's normal.'",
  "'Say something. \"I'm sorry your mam died\" is far better than silence. Children notice when adults avoid them.'",
  "'Use the word \"died\". Softer words confuse younger children.'",
  "'Plan ahead for Mother's Day, Father's Day and family-tree activities. Ask the family or the child what they'd like, rather than guessing.'",
  "'Keep routine and expectations, with some flexibility. Being treated normally is a relief for many bereaved children.'",
  "'Tell the DLP the same day if a child says they want to die or to be with the person who died. Don't wait to see if it passes.'",
 ],

 "explain_child": [
  "YOUNGER: 'When someone dies, their body stops working and it can't start again. It's not your fault, and it's not because of anything you thought or said. It's OK to feel sad, cross, or even happy sometimes — all feelings are allowed.'",
  "OLDER: 'Grief doesn't go in a straight line. Some days it will hit hard out of nowhere and some days you'll feel fine, and both are normal. Missing them doesn't mean something is wrong with you.'",
  "ASK: 'What would you like people in school to know, and what would you like them not to say?' — gives the child control over their story.",
  "ASK: 'What helps on the hard days?' and 'Who can you talk to about them?' — identifies coping and connection.",
  "ASK ABOUT RISK DIRECTLY where indicated: 'Sometimes people who are grieving feel they want to be with the person who died, or don't want to be alive. Has that happened for you?' Same-day risk route if yes.",
 ],

 "analogies": [
  "PUDDLE-JUMPING: 'Children jump in and out of puddles of grief — deep sadness one minute, playing the next.' Good for parents and teachers worried a child 'doesn't care' (Winston's Wish).",
  "THE BALL IN THE BOX (widely shared analogy, source informal): 'Grief is a ball in a box with a pain button. At first the ball is huge and hits the button all the time. Over time the ball doesn't shrink so much as the box grows — it hits the button less often, but it still can.' Good with adolescents and parents; explains trigger days.",
  "GROWING AROUND GRIEF (Tonkin, 1996, Bereavement Care — check): 'The grief doesn't get smaller; life grows bigger around it.' Good with parents and older children who fear 'moving on' means forgetting.",
  "THE PENDULUM (dual process): 'Healthy grief swings between missing them and getting on with life. Getting stuck at either end is harder.' Good with staff; explains why routine and remembering both matter (Stroebe & Schut, 1999).",
 ],

 "language": [
  "Use 'died', 'death' and 'dead' clearly. Avoid 'lost', 'passed', 'gone to sleep', 'gone away' with children — especially younger and autistic children.",
  "Use 'bereaved' and 'grieving' in EP reports. 'Prolonged grief disorder' only where a clinician has diagnosed it, attributed.",
  "For suicide, say 'died by suicide', not 'committed suicide' — 'committed' implies a crime. Follow safe-messaging guidance (e.g. Headline, Ireland's media programme for mental health and suicide — check current guidance).",
  "Avoid 'she should be over it by now' and 'closure'. Grief does not have a deadline; impairment is the question.",
 ],

 "red_flags": [
  "RED FLAG — suicidal ideation, including wishing to be with the person who died, or self-harm. Same-day risk route: DLP, service risk protocol, parent unless it increases risk, same-day GP / CAMHS / emergency response. Supervision follows action; it does not replace it.",
  "RED FLAG — a death by suicide in the school community. Risk of contagion. Follow NEPS critical incident guidance, identify at-risk pupils, apply safe messaging to memorials and social media, and liaise with HSE suicide prevention services — check local arrangements.",
  "RED FLAG — the child's care is unsafe after the death (surviving carer unable to cope, substance misuse, neglect). Follow Children First (DCYA, 2017); report to Tusla as soon as practicable. Telling the DLP does not discharge a mandated person's duty.",
  "RED FLAG — traumatic intrusions about the death blocking grief. Refer for trauma-informed clinical assessment.",
  "BOUNDARY — you do not diagnose PGD, you do not provide bereavement therapy outside competence and remit, and you do not advise on medication. PSI 2.2.2.",
  "WATCH — the child who shows NO reaction and is 'fine'. Often a normal delayed or protective response; sometimes a child holding it together for a parent. Stay available and check in over months.",
 ],

 "child_voice": [
  "MEMORY BOX or MEMORY BOOK — the child collects objects, photos and stories. Good because it honours continuing bonds and gives the child something to talk through rather than about.",
  "'WHAT I WANT SCHOOL TO KNOW' one-page profile — the child decides what staff are told and what they should avoid. Good because it gives back control after an event that removed it.",
  "FEELINGS WEATHER or SCALING — 'what's the weather inside today?' tracked over weeks. Good because it shows the fluctuating pattern of normal grief versus persistent, unchanging distress.",
  "ICBN and Winston's Wish child-friendly materials — good because they are written for children and normalise mixed feelings → https://www.childhoodbereavement.ie/",
  "INVENTORY OF PROLONGED GRIEF FOR CHILDREN / ADOLESCENTS (IPG-C / IPG-A; Spuij et al., 2012) — self-report of grief intensity. Good for a clinician's assessment; the EP should know it exists rather than use it as a diagnostic tool — check availability and validation.",
 ],

 "questions": [
  "Q: 'It's been three months and she's still crying every day — is that normal?' — A: 'Three months is still early. Crying, missing him and finding it hard to concentrate are all part of normal grief at this stage. What I'd look at is whether she can also have good moments, be with friends and take part in things. If that's there, grief is doing what grief does.'",
  "Q: 'He doesn't seem upset at all — is something wrong?' — A: 'Not necessarily. Children often grieve in bursts, or hold it together to protect a parent, or show it later. Keep the door open and keep checking in.'",
  "Q: 'Should she go to the funeral?' — A: 'Children generally cope better when they're prepared, given a choice, and have a trusted adult with them. Explaining beforehand what will happen helps.' (Dyregrov, 2008)",
  "Q: 'What should we tell the class?' — A: 'Agree a short, factual statement with the family, and have class teachers share it at the same time. The NEPS critical incident guidance has templates. Answer questions honestly and correct rumours.'",
  "Q: 'When does it become a problem?' — A: 'When, well over six months to a year on, the missing and preoccupation are still intense most days and she can't take part in life — school, friends, things she enjoyed. Then I'd suggest a GP referral for a clinical assessment.'",
  "Q: 'Can you give her counselling?' — A: 'Most grieving children don't need therapy — they need honest information and people around them. If she needs more, there are specialist bereavement services and clinical teams, and I can help with that referral.'",
  "Q: 'Is it prolonged grief disorder?' — A: 'That's a clinical diagnosis and not mine to make. It also depends on time — it can't be used until at least six months after the death for a child. What I can do is describe what I'm seeing and help decide whether a referral is needed.'",
 ],

 "supervision": [
  "Ask how your service supports schools after a death, and what the trainee's role is in a critical incident response.",
  "Bring a case where you were unsure whether grief was 'normal' or needed referral, and discuss how your supervisor judges it.",
  "Clarify local bereavement services for children (Barnardos, Rainbows, Pieta, hospice services) and their eligibility, ages and waiting times — they vary.",
  "Discuss postvention after a suicide: at-risk pupils, memorials, social media, safe messaging.",
  "Bring your own grief. A child's loss can touch your own; supervision is where that is held.",
 ],

 "reflection": [
  "ON HOW I EXPLAINED IT — Did I leave the parent and teacher reassured that grief is normal, and clear on what would be a reason to seek more help?",
  "ON PATHOLOGISING — Did I treat ordinary grief as a problem to be fixed, or did I respect it as a normal response? Did I use the right timeframe before raising concern?",
  "ON LANGUAGE — Did I use the word 'died'? Did I say 'died by suicide'?",
  "ON RISK — Did I ask about suicidal thoughts, including wanting to be with the person who died? Did I act the same day if the answer was yes?",
  "ON THE CHILD'S CONTROL — Did the child decide what school was told? Did we plan for trigger dates?",
  "WHAT GOOD LOOKS LIKE: 'The school asked for a referral because a pupil was still tearful four months after his mother died. I met the family and his teacher. He was attending, playing football and had a friend he talked to. We planned for Mother's Day and the anniversary, set up a key adult, and I signposted ICBN. No referral. We agreed what would change that.'",
  "WHAT POOR LOOKS LIKE: 'Presents with prolonged grief. Referred to CAMHS for bereavement counselling.' — the term used by someone who cannot diagnose it, possibly within the time window, and ordinary grief sent to a service it does not need.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Prolonged Grief Disorder.",
  "World Health Organization. (2019). International classification of diseases (11th rev.) — 6B42 Prolonged grief disorder. https://icd.who.int/",
  "Prigerson, H. G., Boelen, P. A., Xu, J., Smith, K. V., & Maciejewski, P. K. (2021). Validation of the new DSM-5-TR criteria for prolonged grief disorder and the PG-13-Revised (PG-13-R) scale. World Psychiatry, 20(1), 96–106.",
  "Irish Childhood Bereavement Network. (n.d.). Childhood bereavement care pyramid. Irish Hospice Foundation. https://www.childhoodbereavement.ie/professionals/childhood-bereavement-care-pyramid/",
  "National Educational Psychological Service. (2016). Responding to critical incidents: Guidelines and resource materials for schools. Department of Education and Skills. — check for updates.",
  "Stroebe, M., & Schut, H. (1999). The dual process model of coping with bereavement: Rationale and description. Death Studies, 23(3), 197–224.",
  "Klass, D., Silverman, P. R., & Nickman, S. L. (Eds.). (1996). Continuing bonds: New understandings of grief. Taylor & Francis.",
  "Melhem, N. M., Porta, G., Shamseddeen, W., Walker Payne, M., & Brent, D. A. (2011). Grief in children and adolescents bereaved by sudden parental death. Archives of General Psychiatry, 68(9), 911–919.",
  "Lundorff, M., Holmgren, H., Zachariae, R., Farver-Vestergaard, I., & O'Connor, M. (2017). Prevalence of prolonged grief disorder in adult bereavement: A systematic review and meta-analysis. Journal of Affective Disorders, 212, 138–149.",
  "Dyregrov, A. (2008). Grief in children: A handbook for adults (2nd ed.). Jessica Kingsley.",
  "Cohen, J. A., Mannarino, A. P., & Deblinger, E. (2017). Treating trauma and traumatic grief in children and adolescents (2nd ed.). Guilford Press.",
 ],

 "pathway": {
  "age": "Cannot be diagnosed until at least 6 months after the death for children and adolescents (DSM-5-TR; ICD-11 uses 6 months for all ages). In school referrals, concern usually surfaces in the second half of the first year or around the first anniversary, or years later when a developmental stage (adolescence, exams, a milestone) revives the loss.",
  "who_diagnoses": "Ireland: CAMHS or HSE Primary Care Psychology via GP; private clinical psychologists and psychiatrists. Specialist bereavement services (e.g. Barnardos Children's Bereavement Service, hospice-based services) provide support and may describe complicated grief, but a formal diagnosis comes from a clinician — check local services. The EP does not diagnose it.",
  "who_wrote_report": "CAMHS or Primary Care clinician; private clinical psychologist; occasionally a hospice or specialist bereavement service summary. A bereavement counsellor's letter describes support provided; it is not a diagnostic assessment — ask what was done.",
  "refer_to": "Most children: no referral — family, school and community support (ICBN Pyramid). Some: specialist bereavement support (Barnardos, Rainbows, Pieta for suicide bereavement — check eligibility). Few: GP to Primary Care Psychology or CAMHS. Same-day route for suicide risk. NEPS for school-level deaths. Tusla if care is unsafe.",
  "sooner": "'Grief takes time and most children find their way with the people around them, so giving it time was the right thing. You've noticed it isn't easing the way you'd expect, and that's exactly when to look again.'",
 },

 "differential": [
  "NORMAL GRIEF — intense but fluctuating, with re-engagement in life; revisited at developmental milestones. Not a disorder.",
  "DEPRESSION — pervasive low mood and loss of interest beyond the loss; can co-occur.",
  "PTSD / TRAUMATIC GRIEF — intrusive images of the death and avoidance dominate, blocking grieving.",
  "SEPARATION ANXIETY — fear for the surviving carer dominates.",
  "ADJUSTMENT DISORDER — DSM-5-TR excludes it where the reaction is normal bereavement or better explained by PGD (APA, 2022).",
  "CULTURAL AND RELIGIOUS NORMS — mourning practices and timescales vary; both systems require the response to exceed the person's cultural norms.",
 ],

 "next": [
  "Check the date of death and the timeframe before anyone uses the term PGD.",
  "Ask about suicidal thoughts, including wishing to be with the person who died; same-day route if present.",
  "Support the school with a key adult, trigger-date planning and honest language; ICBN Pyramid to decide the level of support.",
  "Refer via GP to Primary Care Psychology or CAMHS where grief is intense, persistent and impairing beyond 6–12 months; signpost specialist bereavement services.",
 ],

 "presentations": [
  "Bereavement reaction (not a DSM diagnosis)",
  "Grief revisited at a developmental milestone",
  "Suicide bereavement",
  "Anniversary and trigger-date reactions",
  "Separation anxiety after the death of a parent",
  "Traumatic grief after a sudden or violent death",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — young children grieve, but the diagnosis is rarely used; support is through carers",
   "prevalence": "Rate not stated here — check before quoting.",
   "see": "Repeated questions ('when is Mammy coming back?'), searching, regression, clinginess, death themes in play. Understanding of permanence is still developing. Support the surviving carer and the setting to use honest, concrete language and keep routine.",
   "tools": ["SDQ (2–4 version)"],
  },
  "School Age": {
   "applies": "YES — after the 6-month mark, where grief is intense, persistent and impairing",
   "prevalence": "A minority of bereaved children — rate not stated here, check (Melhem et al., 2011).",
   "see": "Normal grief: puddle-jumping, concentration dips, anger, worry about the surviving parent. Concern: persistent daily yearning or preoccupation, inability to enjoy anything, withdrawal from friends, well beyond 6 months. Grief may re-surface with understanding at a new age.",
   "tools": ["SDQ", "RCADS", "Inventory of Prolonged Grief for Children (IPG-C; Spuij et al., 2012) — AGE about 8–12 · MEASURES: prolonged grief symptoms · CANNOT TELL YOU: diagnosis; for clinical use · TIME: about 10 min — check availability and validation"],
  },
  "Adolescent": {
   "applies": "YES — including peer and sibling deaths and suicide bereavement",
   "prevalence": "Rate not stated here — check before quoting.",
   "see": "Withdrawal, anger, risk-taking, falling grades, online memorialising, identity questions ('who am I now?'), meaninglessness. After a peer suicide, contagion risk. Ask about suicidal thoughts and substance use directly.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Inventory of Prolonged Grief for Adolescents (IPG-A; Spuij et al., 2012) — AGE about 13–18 · MEASURES: prolonged grief symptoms · CANNOT TELL YOU: diagnosis; for clinical use · TIME: about 10 min — check availability"],
  },
  "Young Adult": {
   "applies": "YES — note DSM-5-TR uses 12 months for adults; ICD-11 uses 6 months",
   "prevalence": "About one in ten adults bereaved by natural causes (Lundorff et al., 2017) — check before quoting.",
   "see": "Persistent yearning, identity disruption, inability to re-engage with study or work more than 12 months on (DSM-5-TR). Refer to GP, college counselling, hospice bereavement services or adult mental health.",
   "tools": ["Adult self-report measures via the service", "PG-13-R (Prigerson et al., 2021) — AGE adult · MEASURES: DSM-5-TR prolonged grief symptoms · CANNOT TELL YOU: diagnosis on its own · TIME: about 5 min — check current version"],
  },
  "Special Setting": {
   "applies": "YES — grief is often missed or misread where language or cognition is limited",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Behaviour change, searching for the person, distress at routine changes linked to the death, loss of skills. Use concrete language, visual supports and social stories to explain the death; include the child in rituals where the family agrees. Rule out pain and illness.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3"],
  },
 },
},
]
