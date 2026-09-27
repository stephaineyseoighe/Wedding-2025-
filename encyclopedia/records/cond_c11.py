# CONDS records: Obsessive-Compulsive Disorder, Body Dysmorphic Disorder,
# Trichotillomania and Excoriation (skin-picking) Disorder.
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c11.py

CONDS = [

# =====================================================================================
# 1. OBSESSIVE-COMPULSIVE DISORDER
# =====================================================================================
{
 "name": "Obsessive-Compulsive Disorder",
 "code": "DSM-5-TR Obsessive-Compulsive Disorder (F42.2) · ICD-11 6B20 Obsessive-compulsive disorder — check codes before quoting",
 "neps": "3. EMOTIONAL (3.3 Obsessive-compulsive and related) — and 3.2 Anxiety",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Equal Status Acts 2000–2018 · GDPR · Mental Health Act 2001 (context of CAMHS; check current amendments)",

 "what_it_is": [
  "OBSESSIONS — recurrent, intrusive, unwanted thoughts, images or urges that cause marked anxiety or disgust (e.g. contamination, harm coming to a parent, things not being 'just right', unwanted violent, sexual or religious thoughts) — and/or COMPULSIONS — repetitive behaviours or mental acts the person feels driven to perform to reduce the distress or prevent a feared outcome (APA, 2022, DSM-5-TR).",
  "DSM-5-TR requires that the obsessions or compulsions are time-consuming (the manual gives more than one hour a day as an example) or cause clinically significant distress or impairment. Specifiers record INSIGHT (good or fair / poor / absent) and whether there is a current or past TIC disorder. Children often have limited insight — they do not need to see the thoughts as excessive for the diagnosis (APA, 2022).",
  "THE CYCLE: intrusive thought → anxiety or 'not right' feeling → compulsion or avoidance → brief relief → the brain learns the ritual 'worked' → the thought returns stronger. The same cycle applies to REASSURANCE-SEEKING, which is a compulsion in its own right.",
  "Compulsions can be visible (washing, checking, ordering, repeating, re-reading, rewriting, touching, counting aloud) or MENTAL (counting, praying, reviewing, 'cancelling' a bad thought with a good one). Mental compulsions are easily missed in school — the child simply looks slow or distracted.",
  "FAMILY ACCOMMODATION — parents and staff joining in rituals, answering the same question repeatedly, changing routines or allowing avoidance — is very common and is associated with greater severity (Lebowitz et al., 2016). It is done out of love, and it keeps the cycle going.",
  "The first-line treatment for children and young people is CBT including EXPOSURE AND RESPONSE PREVENTION (ERP), with the family involved (NICE, 2005, CG31 — check for updates). The Pediatric OCD Treatment Study found CBT, sertraline and their combination all effective, with the combination strongest (POTS Team, 2004). Medication is a medical decision.",
  "In Ireland, assessment and treatment sit with CAMHS (or a private clinician). The EP's job is to recognise it, describe it in school, stop school unintentionally feeding it, and refer.",
 ],

 "what_it_is_not": [
  "NOT 'being a bit OCD' about tidiness. The everyday phrase trivialises a condition that can consume hours a day and cause great distress. OCD is defined by distress, time and impairment, not by liking things neat.",
  "NOT ordinary childhood ritual. Young children commonly have strong preferences for sameness, bedtime rituals and 'just right' routines, which peak in the preschool years and fade (Evans et al., 1997). These are developmentally typical and are not distressing or impairing.",
  "NOT autistic routine or repetitive behaviour. Autistic routines and interests are usually experienced as comforting, predictable or enjoyable; OCD compulsions are usually driven by an unwanted thought and a feared outcome, and the child wishes they could stop. Both can co-occur — the question to ask is 'what would happen if you didn't?'",
  "NOT a sign that the child is dangerous or 'bad'. Intrusive thoughts about harm, sex or blasphemy are the OPPOSITE of what the child wants — that is why they are so distressing. Having the thought is not the wish. Do not respond with alarm.",
  "NOT helped by reassurance. Reassurance is a compulsion done by someone else. It brings relief for minutes and strengthens the cycle. The same applies to letting the child avoid triggers indefinitely.",
  "NOT a diagnosis the EP makes. CAMHS (or a private psychiatrist or clinical psychologist) diagnoses and treats. The EP describes, formulates in school terms, recommends and refers (PSI 2.2.2).",
  "NOT generalised worry. GAD worry is about real-life concerns and feels reasonable to the child; OCD obsessions are intrusive, often feel senseless or 'sticky', and are linked to rituals.",
 ],

 "prevalence": [
  "OVERALL (CHILDREN): the British nationwide child mental health survey found OCD in about 0.25% of 5–15-year-olds (Heyman et al., 2001) — a figure from a single national survey, likely an underestimate because children hide symptoms. Other studies report higher rates — check before quoting a single figure.",
  "ADULT: lifetime prevalence in the US National Comorbidity Survey Replication was about 2.3% (Ruscio et al., 2010) — check before quoting.",
  "AGE OF ONSET: onset is often described as bimodal — one peak in childhood (around late primary) and another in late adolescence or early adulthood (Geller et al., 1998). A substantial share of adults report onset before 18 — exact proportion not stated here, check.",
  "IRELAND: no national diagnostic prevalence figure for childhood OCD is stated here — check before quoting.",
  "SEX RATIO: childhood-onset OCD is more common in boys; the ratio evens out by adolescence and adulthood (Geller et al., 1998) — exact ratio not stated here, check.",
  "DELAY: children and families commonly hide OCD for a long time because of shame about the thoughts. Identification in school is often years after onset.",
 ],

 "cooccurring": [
  {"name": "TIC DISORDERS / TOURETTE SYNDROME",
   "rate": "elevated, especially in childhood-onset OCD in boys — rate not stated here, check",
   "presents": "Repetitive movements or sounds alongside rituals. The distinction matters: a tic is preceded by a physical urge; a compulsion is preceded by a thought or feared outcome. DSM-5-TR has a tic-related specifier. Paediatric neurology or CAMHS."},
  {"name": "OTHER ANXIETY DISORDERS",
   "rate": "common — rate not stated here, check",
   "presents": "Broad worry, separation fears or social fears alongside obsessions. Name each focus in the referral; the ERP plan and the anxiety plan overlap but are not identical."},
  {"name": "DEPRESSION / LOW MOOD",
   "rate": "elevated, particularly in adolescence and with severe OCD — rate not stated here, check",
   "presents": "Hopelessness about ever being free of the thoughts, withdrawal, exhaustion from rituals. Ask directly about self-harm and suicidal thoughts — asking does not increase risk."},
  {"name": "AUTISM",
   "rate": "elevated — rate not stated here, check",
   "presents": "Rigid routines, sameness and repetitive behaviour that may or may not be OCD. Ask whether the behaviour is wanted and comforting (autism) or unwanted and driven by a feared outcome (OCD). ERP needs adapting for autistic young people; CDNT and CAMHS may both be involved."},
  {"name": "ADHD",
   "rate": "elevated — rate not stated here, check",
   "presents": "Inattention that is actually mental rituals, or genuine ADHD alongside OCD. Ask what is happening in the child's head when they 'switch off'."},
  {"name": "EATING DIFFICULTIES",
   "rate": "elevated in adolescence — rate not stated here, check",
   "presents": "Food rituals, contamination fears around eating, or rigid rules about food. Distinguish OCD contamination fear from weight and shape concern; any weight loss → GP the same week."},
  {"name": "EMOTIONALLY BASED SCHOOL AVOIDANCE (EBSA)",
   "rate": "frequent pathway — rate not stated here, check",
   "presents": "Late arrival because morning rituals take hours, avoidance of toilets or shared equipment, then partial attendance. Attendance and lateness data are part of the assessment."},
  {"name": "BODY DYSMORPHIC DISORDER / BODY-FOCUSED REPETITIVE BEHAVIOURS",
   "rate": "elevated — rate not stated here, check",
   "presents": "Mirror checking, appearance rituals, hair-pulling or skin-picking alongside OCD. DSM-5-TR groups these in the same chapter; each needs its own description in the referral."},
 ],

 "recommendations": [
  "FORMULATE THE OCD CYCLE in the report: trigger → intrusive thought → anxiety or 'not right' feeling → ritual, avoidance or reassurance-seeking → brief relief → cycle strengthens. Name what school does, kindly, that feeds it (e.g. answering the same question repeatedly, allowing rewriting until perfect).",
  "DON'T PROVIDE REASSURANCE LOOPS AT SCHOOL. Agree ONE brief, consistent, warm response across staff to repeated questions: 'That sounds like the OCD asking. I've answered it once — let's get on with the next bit.' Coordinate with the CAMHS plan so school and home respond the same way.",
  "REDUCE ACCOMMODATION GRADUALLY, NOT ABRUPTLY. Do not remove accommodations in one go or set school-based exposure tasks without the treating clinician's plan — that is treatment, and it belongs to CAMHS. School's role is to support the steps the young person and clinician have agreed.",
  "PRACTICAL ADJUSTMENTS WHILE TREATMENT RUNS: extra time or reduced volume where rituals slow work (e.g. re-reading, rewriting); permission to hand in work that is 'not perfect'; typing in place of handwriting if erasing and rewriting is a ritual; discreet toilet access; a quiet base when distress is high. Review each adjustment — the aim is to protect learning, not to build avoidance.",
  "EXAMS: rituals (checking, re-reading, rewriting) can cause incomplete papers. Consider Reasonable Accommodations in State Examinations (RACE) evidence early — check current SEC criteria and deadlines.",
  "PSYCHOEDUCATION FOR KEY STAFF: OCD thoughts are unwanted and are not wishes; responding with alarm or discipline to disclosure of a 'bad thought' increases shame.",
  "MONITOR: an agreed simple measure (time lost to rituals per day, RCADS OCD subscale repeated, attendance and lateness) and a review date.",
  "CONTINUUM LEVEL: School Support for a coordinated staff response and adjustments; School Support Plus where CAMHS is involved and the plan is joint.",
  "REFER: via GP to CAMHS for assessment and CBT with ERP (NICE, 2005, CG31 — check for updates). Primary Care Psychology may see milder cases — check local criteria. Private clinical psychologists trained in ERP are an option for some families.",
  "DO NOT advise on medication (PSI 2.2.2); do not run ERP yourself unless your service offers it and you are trained and supervised; do not describe normal routines or autistic sameness as OCD in a report.",
 ],

 "explain_parent": [
  "'OCD is a bit like a false alarm in the brain. A thought pops in — something bad might happen, or things aren't right — and it comes with a huge feeling of anxiety. The rituals are her way of switching the alarm off.'",
  "'The thoughts are the opposite of what she wants. That's exactly why they upset her so much. Having a thought is not the same as wanting it.'",
  "'When we answer the same question again, or join in with a ritual, it helps for a few minutes and makes the OCD stronger over time. Nearly every parent does this — it's what love looks like. The treatment helps you step back gradually, with support.'",
  "'The treatment with the best evidence is a type of CBT called exposure and response prevention. She learns, step by step, that she can face the fear without doing the ritual, and the anxiety comes down on its own. Parents are usually part of it.'",
  "'This is very treatable. Getting it named is the first step.'",
  "SIGNPOST: GP for CAMHS referral; OCD Ireland (support groups — check current services) → https://www.ocdireland.org/; Derisley et al. (2008), Breaking Free from OCD; Huebner (2007), What to Do When Your Brain Gets Stuck (younger children).",
 ],

 "explain_teacher": [
  "'He's not being difficult or slow on purpose. When he re-reads a line five times or rubs out a letter, the OCD is telling him something bad will happen if it's not right.'",
  "'Answering the same question again feels kind, but it's reassurance, and reassurance feeds OCD. One calm answer, then \"that sounds like the OCD — let's move on\".'",
  "'If he tells you about a frightening thought — harming someone, something rude or religious — please stay calm. These thoughts are unwanted and very common in OCD. Pass it on to the DLP only if there is a real safeguarding concern, not because of the thought itself.'",
  "'We'll follow the CAMHS plan. Please don't set him challenges to face his fears on your own — the treatment steps are planned with his clinician.'",
  "'Good enough is the goal. Praise finishing, not perfection.'",
 ],

 "explain_child": [
  "YOUNGER: 'Sometimes your brain has a worry bully that says \"wash again or something bad will happen\". It's a trick — the bully gets stronger every time you do what it says. We're going to help you learn to boss it back.' (Externalising — March & Mulle, 1998.)",
  "OLDER: 'OCD sends thoughts that feel urgent and scary. The rituals make the anxiety drop for a bit, so your brain thinks they worked. Treatment helps you learn that the anxiety comes down on its own if you don't do the ritual. It's hard work, and it works.'",
  "NAME IT: 'If OCD was a character, what would you call it? What does it tell you to do?' Separates the young person from the OCD and makes it easier to talk about thoughts they are ashamed of.",
  "ASK: 'Are there things you have to do, or thoughts that keep coming back, that you'd rather not have?' 'What do you think would happen if you didn't do it?' 'How long does it take each day?' The second question separates OCD from autistic routine.",
  "ASK ABOUT RISK DIRECTLY where age-appropriate: 'Sometimes when OCD gets really heavy people feel hopeless or think about hurting themselves. Has that happened for you?' Same-day risk route if yes.",
 ],

 "analogies": [
  "THE FALSE ALARM: 'A fire alarm that goes off when there's no fire. The ritual turns it off for a minute — but the alarm learns to ring louder next time.' Works with parents, teachers and children.",
  "THE BULLY THAT KEEPS ASKING: 'OCD is like a bully — every time you give it what it wants, it comes back and asks for more.' Good with 7–12s; explains why rituals and reassurance backfire (March & Mulle, 1998).",
  "THE STUCK RECORD / BRAIN HICCUP: 'The thought gets stuck and replays — like a scratched record.' Good for younger children and for reducing shame about the content of thoughts.",
  "THE COLD SWIMMING POOL: 'You get used to the cold by staying in, not by jumping out every time.' Good for explaining exposure and response prevention to parents and adolescents.",
 ],

 "language": [
  "Use 'OCD' or 'obsessive-compulsive difficulties' only where diagnosed or where you are describing a referral concern; otherwise describe the behaviour ('repeated checking', 'intrusive thoughts', 'rituals').",
  "Avoid 'a bit OCD', 'obsessive' or 'fussy' in reports and conversation — they trivialise and mislabel. PSI 1.2.8.",
  "'The OCD' (externalised) is helpful language with children and families; it separates the young person from the condition.",
  "Do not repeat the specific content of taboo intrusive thoughts in a report unless necessary; describe them as 'unwanted intrusive thoughts of harm' or similar — the content is highly shaming and the report will be read by others.",
 ],

 "red_flags": [
  "RED FLAG — suicidal thoughts, self-harm or hopelessness. Same-day risk route: inform the DLP, follow the service risk protocol, contact the parent unless doing so raises risk, and arrange a same-day GP / CAMHS / emergency response as indicated. Supervision follows action; it does not replace it.",
  "RED FLAG — SUDDEN, dramatic onset of OCD symptoms (overnight or over days), especially with other changes (eating restriction, tics, bedwetting, handwriting deterioration). Urgent medical review via GP / paediatrics. PANS/PANDAS is debated in the literature — it is not the EP's diagnosis; the action is medical review.",
  "RED FLAG — weight loss or food restriction, or not drinking because of contamination fears. GP the same week.",
  "RED FLAG — do not confuse unwanted intrusive thoughts with intent. A child disclosing a feared thought of harming someone is usually describing OCD, not risk to others. Do not ignore it either: record, consult, and let the clinician assess. If there is any separate indication of real risk or harm to the child, follow Children First; report to Tusla as soon as practicable — telling the DLP does not discharge a mandated person's duty.",
  "BOUNDARY — you do not diagnose OCD, do not deliver ERP outside your service's remit and competence, and do not advise on medication. PSI 2.2.2.",
  "WATCH — school well-meaning accommodation (repeated reassurance, rewriting permitted indefinitely, avoidance of toilets or equipment) quietly increasing over the year.",
  "WATCH — skin damage from excessive handwashing (cracked, bleeding hands). GP.",
 ],

 "child_voice": [
  "EXTERNALISING CONVERSATION ('What would you call your OCD? What does it make you do?') — good because it lets a child talk about thoughts they are ashamed of without owning them (March & Mulle, 1998).",
  "OCD MAP / 'WHERE OCD WINS AND WHERE I WIN' drawing — good because it shows which parts of the school day the OCD controls and gives a baseline for the review.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — Irish and free; good because it surfaces difficult parts of the day (toilets, shared equipment, handwriting) without leading. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "RCADS SELF-REPORT (includes an OCD subscale) — standardised; good as a structured way to report symptoms the child may not say aloud. It is a screen, not a diagnosis; ask about risk separately, face to face.",
  "SCALING the time lost to rituals ('how much of your morning does OCD take?') — good because it gives a concrete monitoring number the child owns.",
 ],

 "questions": [
  "Q: 'Isn't she just a perfectionist?' — A: 'Perfectionism is about wanting to do well. OCD is different — it's about a feared outcome or an unbearable \"not right\" feeling, and she can't stop even when she wants to. The question to ask is what she thinks would happen if she didn't redo it.'",
  "Q: 'He's autistic — isn't this just his routines?' — A: 'It might be. Routines that he likes and that calm him are usually autism. Rituals he wishes he could stop, driven by fear something bad will happen, sound more like OCD. Both can be true. That's worth raising with his team.'",
  "Q: 'Should I keep reassuring her?' — A: 'It's natural, and it helps for a few minutes. With OCD, reassurance works like a ritual and keeps it going. The CAMHS team will help you step back gradually — not all at once.'",
  "Q: 'He told me he has thoughts of hurting his brother. Should I be worried?' — A: 'Intrusive thoughts of harm are common in OCD, and they upset children precisely because they don't want to act on them. I'll record it and make sure the clinician knows. If anything else suggests real risk, we act on that straight away.'",
  "Q: 'Will she need medication?' — A: 'That's a medical decision for her doctor, not mine. What I can say is that the first-line treatment for children is a type of CBT called exposure and response prevention, and it works well.'",
  "Q: 'Can you diagnose OCD?' — A: 'No. CAMHS would assess and diagnose. I can describe what's happening in school, help school respond in a way that doesn't feed it, and refer.'",
  "Q: 'Did we cause this?' — A: 'No. OCD comes from a mix of genes, brain and experience. Families often end up joining in with rituals out of love — that doesn't cause OCD, and it's one of the things treatment helps with.'",
 ],

 "supervision": [
  "Bring a case where a child's rituals could be autistic routine or OCD, and talk through the questions that separate them.",
  "Ask how to handle a disclosure of a violent or sexual intrusive thought — what to record, whom to tell, and how to avoid both over-reacting and under-reacting.",
  "Clarify local CAMHS acceptance criteria for OCD and whether any clinician locally offers ERP for children; what to tell families about waiting times.",
  "Discuss where the line sits between school supporting the CAMHS plan and the EP delivering exposure work — what the service offers and what your competence covers.",
  "Bring your own reaction — did the family's distress pull you towards reassuring them in the same way the child seeks reassurance?",
 ],

 "reflection": [
  "ON DISTINGUISHING — Did I ask 'what would happen if you didn't?' before calling a routine OCD, or did I label on the surface behaviour?",
  "ON REASSURANCE — Did any of my recommendations build a reassurance loop into the school day?",
  "ON SHAME — Did the child get the message that their thoughts were unwanted, common and treatable — or did my reaction add to the shame?",
  "ON ROLE — Did I stay within formulation, school adjustments and referral, or did I drift into running exposure tasks?",
  "ON RISK — Did I ask about mood and self-harm directly, and act the same day if needed?",
  "WHAT GOOD LOOKS LIKE: 'Teacher described \"endless checking\". The girl told me she re-read each line until it \"felt right\" or her mum would get sick. We agreed one consistent staff response, typed work to reduce rewriting, and a GP letter for CAMHS. At review, the school plan matched the CAMHS ERP plan.'",
  "WHAT POOR LOOKS LIKE: 'Child presents as a bit OCD. Teacher to reassure when anxious. Allow extra time for rewriting.' — no formulation, reassurance and rewriting recommended as support, no referral.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). American Psychiatric Publishing.",
  "National Institute for Health and Care Excellence. (2005). Obsessive-compulsive disorder and body dysmorphic disorder: Treatment (Clinical Guideline CG31). NICE. [Check for updates.]",
  "Pediatric OCD Treatment Study (POTS) Team. (2004). Cognitive-behavior therapy, sertraline, and their combination for children and adolescents with obsessive-compulsive disorder: The Pediatric OCD Treatment Study (POTS) randomized controlled trial. JAMA, 292(16), 1969–1976.",
  "Heyman, I., Fombonne, E., Simmons, H., Ford, T., Meltzer, H., & Goodman, R. (2001). Prevalence of obsessive-compulsive disorder in the British nationwide survey of child mental health. British Journal of Psychiatry, 179(4), 324–329.",
  "Geller, D., Biederman, J., Jones, J., Park, K., Schwartz, S., Shapiro, S., & Coffey, B. (1998). Is juvenile obsessive-compulsive disorder a developmental subtype of the disorder? A review of the pediatric literature. Journal of the American Academy of Child & Adolescent Psychiatry, 37(4), 420–427.",
  "Ruscio, A. M., Stein, D. J., Chiu, W. T., & Kessler, R. C. (2010). The epidemiology of obsessive-compulsive disorder in the National Comorbidity Survey Replication. Molecular Psychiatry, 15(1), 53–63.",
  "Evans, D. W., Leckman, J. F., Carter, A., Reznick, J. S., Henshaw, D., King, R. A., & Pauls, D. (1997). Ritual, habit, and perfectionism: The prevalence and development of compulsive-like behavior in normal young children. Child Development, 68(1), 58–68.",
  "Lebowitz, E. R., Panza, K. E., & Bloch, M. H. (2016). Family accommodation in obsessive-compulsive and anxiety disorders: A five-year update. Expert Review of Neurotherapeutics, 16(1), 45–53.",
  "March, J. S., & Mulle, K. (1998). OCD in children and adolescents: A cognitive-behavioral treatment manual. Guilford Press.",
  "Derisley, J., Heyman, I., Robinson, S., & Turner, C. (2008). Breaking free from OCD: A CBT guide for young people and their families. Jessica Kingsley.",
 ],

 "pathway": {
  "age": "Often first noticed in late primary (childhood-onset peak) or in mid–late adolescence (second peak) (Geller et al., 1998). Identification is frequently delayed by years because children hide intrusive thoughts out of shame, rituals are mistaken for fussiness or perfectionism, and families accommodate without realising. School often notices lateness, slowness, rewriting or toilet avoidance before anyone names OCD.",
  "who_diagnoses": "Ireland: CAMHS (psychiatrist, clinical psychologist or MDT), usually via GP referral; private psychiatrist or clinical psychologist. Primary Care Psychology may see milder presentations — check local criteria. Medication, if considered, is prescribed by a psychiatrist (or GP on specialist advice), never a psychologist. Waiting times and ERP availability vary by CHO — check before advising families.",
  "who_wrote_report": "CAMHS consultant psychiatrist, clinical psychologist or MDT; private psychiatrist or clinical psychologist. A CY-BOCS score (Scahill et al., 1997) will usually come from a clinician. An RCADS OCD subscale score in an EP report is a screen, not a diagnosis.",
  "refer_to": "GP for CAMHS referral (check whether local CAMHS accepts other referrers). GP / paediatrics urgently if onset is sudden or accompanied by food restriction or neurological change. Same-day emergency route for acute suicide risk. Tusla if abuse or neglect is suspected. CDNT if autism is a live question.",
  "sooner": "'OCD is one of the most hidden conditions in childhood — children often keep the thoughts secret because they're ashamed of them, and families naturally adapt around the rituals. It's very common for it to be named only after a long time. It's treatable at any age, and you've noticed now.'",
 },

 "differential": [
  "AUTISTIC ROUTINES, SAMENESS AND REPETITIVE BEHAVIOUR — wanted and comforting rather than driven by feared outcomes; check autism first where there are social communication features.",
  "ORDINARY CHILDHOOD RITUALS — preschool 'just right' and bedtime routines are developmentally typical and fade (Evans et al., 1997).",
  "TIC DISORDER — preceded by a physical urge, not a thought; may co-occur.",
  "GENERALISED ANXIETY — real-life worries that feel reasonable to the child, without rituals.",
  "EATING DISORDER — food rules driven by weight and shape rather than contamination or 'just right'.",
  "PSYCHOSIS — rare; beliefs held with conviction and not experienced as one's own intrusive thoughts. Clinician's judgement; urgent CAMHS if suspected.",
  "SUDDEN-ONSET PRESENTATION — medical review via GP / paediatrics.",
 ],

 "next": [
  "Ask the child what would happen if they didn't do the ritual, and how long it takes; ask directly about mood and self-harm.",
  "Map the cycle and school's accommodations with the teacher and parent; gather attendance and lateness data.",
  "Check for autism, tics and learning needs before formulating OCD alone.",
  "Write a school plan: one consistent response to reassurance-seeking, adjustments to protect learning, review date and measure.",
  "Refer via GP to CAMHS for assessment and CBT with ERP (NICE CG31, 2005 — check for updates).",
 ],

 "presentations": [
  "Rigidity and routine that is not OCD",
  "Repeated checking of work",
  "Ritual at transitions",
  "Repeated reassurance-seeking",
  "Rewriting and erasing until 'just right'",
  "Contamination avoidance (toilets, shared equipment)",
  "Unwanted intrusive thoughts",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — preschool rituals are usually developmentally typical",
   "prevalence": "Diagnosis at this age uncommon — rate not stated here, check before quoting.",
   "see": "Bedtime rituals, 'just right' ordering and sameness are common and peak in the preschool years (Evans et al., 1997). Concern only if rituals cause marked distress, take a lot of time, or are driven by a feared outcome. Refer via GP/Primary Care; check autism where social communication differences are present.",
   "tools": ["SDQ (2–4 version)", "Preschool Anxiety Scale (Spence et al., 2001) — AGE about 2.5–6.5, parent report · MEASURES: includes an obsessive-compulsive subscale alongside other anxiety areas · CANNOT TELL YOU: diagnosis · TIME: about 10 min — check current version"],
  },
  "School Age": {
   "applies": "YES — first onset peak; often hidden or misread as perfectionism",
   "prevalence": "About 0.25% of 5–15s in the British national survey (Heyman et al., 2001) — likely an underestimate; check before quoting.",
   "see": "Rewriting and erasing, re-reading, slowness, lateness from morning rituals, repeated questions, avoidance of toilets or shared equipment, distress when routines are interrupted. Mental rituals look like daydreaming. Ask about the feared outcome to separate it from autistic routine.",
   "tools": ["RCADS", "RCADS self-report", "SDQ", "Spence Children's Anxiety Scale (SCAS; Spence, 1998) — AGE about 8–15 child report, parent version available · MEASURES: includes an obsessive-compulsive subscale · CANNOT TELL YOU: diagnosis or risk · TIME: about 10 min — check current version and norms"],
  },
  "Adolescent": {
   "applies": "YES — second onset peak; taboo intrusive thoughts and mood difficulties more common",
   "prevalence": "Rate for this band not stated here — check before quoting.",
   "see": "Hidden mental rituals, reassurance-seeking by text, intrusive sexual, violent or religious thoughts causing shame, exam papers incomplete because of checking, exhaustion, low mood. Self-report is essential; ask about mood and self-harm directly.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Beck Youth Inventories-2", "Access arrangements evidence (RACE)"],
  },
  "Young Adult": {
   "applies": "YES — onset still possible; adult mental health services hold the case",
   "prevalence": "Adult lifetime about 2.3% (Ruscio et al., 2010) — check before quoting.",
   "see": "Checking and rituals interfering with study, deadlines or placements; avoidance of shared accommodation or facilities. Refer to GP, college counselling or adult mental health; know the boundary of the EP role.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — but very hard to separate from autistic repetitive behaviour where language is limited",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Repetitive behaviour with distress when blocked may be OCD, autistic sameness, sensory regulation or anxiety. Without self-report, rely on observation of distress versus comfort, functional assessment and informant report; joint working with CDNT and CAMHS.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3"],
  },
 },
},

# =====================================================================================
# 2. BODY DYSMORPHIC DISORDER
# =====================================================================================
{
 "name": "Body Dysmorphic Disorder",
 "code": "DSM-5-TR Body Dysmorphic Disorder (F45.22) · ICD-11 6B21 Body dysmorphic disorder — check codes before quoting",
 "neps": "3. EMOTIONAL (3.3 Obsessive-compulsive and related) — and 3.2 Anxiety · 3.4 Mood",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Equal Status Acts 2000–2018 · GDPR · Mental Health Act 2001 (context of CAMHS; check current amendments)",

 "what_it_is": [
  "A PREOCCUPATION with one or more perceived defects or flaws in physical appearance that are NOT observable, or appear slight, to others — plus REPETITIVE BEHAVIOURS or mental acts in response (mirror checking, excessive grooming, skin picking, reassurance-seeking, comparing with others), causing significant distress or impairment (APA, 2022, DSM-5-TR).",
  "Common foci: skin (acne, scars), nose, hair, teeth, face shape, body build. DSM-5-TR has a MUSCLE DYSMORPHIA specifier (belief that one's body is too small or insufficiently muscular) — more often seen in boys and young men — and an INSIGHT specifier; insight is often poor, and some young people are completely convinced (APA, 2022).",
  "It is classified with OCD in both DSM-5-TR and ICD-11 (6B21) because of the obsession–ritual structure. It is NOT vanity: the young person usually experiences the flaw as shameful and the preoccupation as tormenting.",
  "ONSET is most commonly in ADOLESCENCE (Bjornsson et al., 2013), when appearance, peer comparison and — for many young people — image-based social media become central.",
  "RISK: suicidal ideation and suicide attempts are markedly elevated in BDD compared with the general population (Phillips, 2007; Angelakis et al., 2016). Every BDD concern is a risk conversation.",
  "Treatment is CBT with exposure and response prevention adapted for BDD, and specialist referral; NICE CG31 covers BDD alongside OCD (NICE, 2005 — check for updates). A pilot RCT supports CBT for adolescents with BDD (Mataix-Cols et al., 2015). Cosmetic procedures rarely relieve the preoccupation and are not a treatment.",
 ],

 "what_it_is_not": [
  "NOT ordinary teenage self-consciousness. Most adolescents dislike aspects of their appearance. BDD is preoccupation lasting hours a day, with rituals, avoidance and real impairment — missing school, avoiding photos, unable to leave the house.",
  "NOT vanity or attention-seeking. The young person is usually ashamed, and many hide the preoccupation completely.",
  "NOT helped by reassurance about appearance. 'You look fine' is heard as untrue or kind lying, and it feeds the checking cycle. Do not argue about the flaw either — acknowledge the distress instead.",
  "NOT an eating disorder, though they overlap. If the concern is mainly about weight or body fat and eating is restricted, consider an eating disorder first — and both can co-occur.",
  "NOT gender dysphoria. Distress about sex characteristics related to gender identity is a separate matter and should not be labelled BDD. Keep the two distinct and non-pathologising.",
  "NOT fixed by cosmetic, dermatological or dental procedures when the 'defect' is slight — the preoccupation usually moves or persists. Young people may seek fillers, tanning or supplements; this needs medical, not cosmetic, attention.",
  "NOT caused by social media alone. Associations between image-focused social media use and appearance concerns are reported, but most evidence is correlational — say 'may contribute' rather than 'causes' (check current evidence before stating more).",
  "NOT a diagnosis the EP makes. CAMHS or a specialist clinician diagnoses. The EP recognises, asks about risk, supports school, and refers.",
 ],

 "prevalence": [
  "OVERALL: a systematic review estimated weighted prevalence of about 2% in adolescents and about 2% in community adults (Veale et al., 2016) — check exact figures before quoting.",
  "HIGHER in dermatology and cosmetic-surgery settings (Veale et al., 2016) — relevant when a young person is already seeking treatment for appearance.",
  "AGE OF ONSET: most commonly adolescence (Bjornsson et al., 2013) — exact mean age not stated here, check.",
  "IRELAND: no national prevalence figure for BDD in young people stated here — check before quoting.",
  "SEX RATIO: occurs in both sexes; muscle dysmorphia more common in males — exact ratio not stated here, check.",
  "UNDER-IDENTIFICATION: shame and secrecy mean BDD is frequently missed or seen only as depression or social anxiety.",
 ],

 "cooccurring": [
  {"name": "DEPRESSION",
   "rate": "very common — rate not stated here, check",
   "presents": "Low mood, hopelessness and withdrawal alongside appearance preoccupation. Depression plus BDD raises suicide risk; ask directly and act the same day."},
  {"name": "SOCIAL ANXIETY",
   "rate": "common — rate not stated here, check",
   "presents": "Avoidance of being seen, photographed or looked at. Ask whether the fear is of being judged generally or specifically of the 'flaw' being noticed — the latter points to BDD."},
  {"name": "OCD",
   "rate": "elevated — rate not stated here, check",
   "presents": "Checking, rituals and intrusive thoughts beyond appearance. Describe both in the referral; treatment overlaps."},
  {"name": "EATING DISORDERS",
   "rate": "overlap is recognised — rate not stated here, check",
   "presents": "Concern with weight or shape plus restriction, bingeing or compensatory behaviour. Weight loss or restriction → GP the same week."},
  {"name": "SKIN-PICKING (EXCORIATION)",
   "rate": "common in BDD — rate not stated here, check",
   "presents": "Picking at perceived blemishes to 'fix' them, causing real damage that then feeds the preoccupation. Dermatological harm → GP."},
  {"name": "SELF-HARM AND SUICIDAL IDEATION",
   "rate": "markedly elevated (Angelakis et al., 2016) — rate not stated here, check",
   "presents": "Hopelessness about appearance, 'I can't live looking like this', withdrawal, giving things away. Same-day risk route."},
  {"name": "SUBSTANCE USE / STEROID USE (muscle dysmorphia)",
   "rate": "reported in muscle dysmorphia — rate not stated here, check",
   "presents": "Excessive gym use, supplements, anabolic steroid use in older adolescents. Medical risk — GP; do not treat as a fitness hobby."},
 ],

 "recommendations": [
  "ASK ABOUT RISK FIRST, EVERY TIME. Ask directly about hopelessness, self-harm and suicidal thoughts. If present, same-day risk route. Record that you asked and what was said.",
  "FORMULATE THE CYCLE: perceived flaw → shame and anxiety → checking, camouflaging, comparing, reassurance-seeking or avoidance → brief relief → preoccupation grows. Name school triggers (mirrors in toilets, PE changing, photographs, presentations).",
  "DON'T REASSURE ABOUT APPEARANCE, and don't argue about the flaw. Agree a staff response that validates the distress without engaging the content: 'I can see how much this is upsetting you. Let's think about what would help you get through this class.'",
  "PRACTICAL ADJUSTMENTS WHILE TREATMENT RUNS: flexibility about PE changing, class photographs and being filmed; seating that doesn't face peers; alternatives to presenting at the front. Each time-limited and reviewed — the aim is attendance and learning, not permanent avoidance.",
  "PHONE AND SOCIAL MEDIA: support the family and young person to notice how image-focused social media and camera or filter use affect the checking cycle — a conversation, not a ban, and coordinated with the clinician's plan.",
  "ATTENDANCE: monitor lateness and absence closely — hours of grooming or camouflaging often cause late arrival, and BDD can escalate into complete avoidance.",
  "CONTINUUM LEVEL: School Support Plus — BDD needs specialist input, and the school plan should be joint with CAMHS.",
  "REFER: via GP to CAMHS for assessment and CBT with ERP adapted for BDD (NICE, 2005, CG31 — check for updates); SAME-DAY route (GP / CAMHS / emergency department) if suicidal thoughts or self-harm are present. Jigsaw (12–25) for support where available, not as a substitute for CAMHS where risk or severity is high.",
  "DO NOT advise on medication, cosmetic or dermatological procedures (PSI 2.2.2); do not reassure about appearance; do not describe gender-related body distress as BDD.",
 ],

 "explain_parent": [
  "'Body dysmorphic disorder means her brain is locked onto something about her appearance that others barely notice or can't see at all, and it causes her real torment. It's not vanity — she's ashamed of it.'",
  "'Telling her she looks fine won't help, even though it's the natural thing to say. It gets heard as kind lying and she'll need to ask again. Instead, try: \"I can see how upset you are. I'm not going to argue about how you look — let's think about what would help today.\"'",
  "'Young people with BDD can feel very hopeless. I asked her directly about thoughts of hurting herself — it's important you know that, and that asking is safe. If you ever have concerns about her safety, contact your GP or go to the emergency department the same day.'",
  "'There is specialist treatment — a form of CBT — and it works. Cosmetic treatments don't usually help, because the worry tends to move to another feature.'",
  "SIGNPOST: GP for CAMHS referral; Veale, Willson & Clarke (2009), Overcoming Body Image Problems including Body Dysmorphic Disorder; BDD Foundation (UK) → https://bddfoundation.org/ (check Irish availability); Jigsaw (12–25) → https://jigsaw.ie/; emergency: 999/112 or ED.",
 ],

 "explain_teacher": [
  "'She's not being difficult about photos or PE — she believes something about how she looks is so bad that people will stare. It's a recognised condition and it's frightening for her.'",
  "'Please don't reassure her about how she looks, and don't argue with her about it. Acknowledge that she's upset and move on to the task.'",
  "'Lateness may be because it takes her hours to get ready. Please pass on patterns rather than just recording lates.'",
  "'Any comment about not wanting to be here, or feeling hopeless, goes to the DLP immediately and we follow the risk procedure the same day.'",
  "'Mirrors, photos, filming and changing rooms are the hot spots. We have a short-term plan for each; it'll be reviewed with her clinician.'",
 ],

 "explain_child": [
  "YOUNGER (rare — late primary): 'Sometimes our brain gets stuck on one thing about how we look and won't let go, even when other people don't notice it. That can feel really awful. There are people who know how to help with that.'",
  "OLDER: 'BDD is when your brain zooms in on part of how you look and turns the volume right up. The checking and hiding make sense — they bring a bit of relief — but they keep the zoom stuck on. There's a type of therapy that helps turn it down. I'm not going to argue with you about how you look; I believe you that it feels this bad.'",
  "ASK: 'How much of the day do you spend thinking about it?' 'What do you do to check or hide it?' 'What have you stopped doing because of it?' These map the rituals and avoidance without debating the flaw.",
  "ASK ABOUT RISK DIRECTLY: 'When people feel this bad about how they look, sometimes they think about hurting themselves or not wanting to be alive. Has that happened for you?' Same-day risk route if yes.",
  "ASK ABOUT ONLINE LIFE neutrally: 'How do you find social media and photos these days?' — opens the conversation without blame.",
 ],

 "analogies": [
  "THE ZOOM LENS: 'Her brain has zoomed right in on one spot, so it fills the whole picture. Everyone else sees the whole face.' Works with parents, teachers and adolescents; avoids arguing about the flaw.",
  "THE FUNHOUSE MIRROR: 'It's like looking in a distorting mirror — what she sees is real to her, but the mirror is bent.' Good for parents; explains why reassurance doesn't land.",
  "THE ITCH YOU SCRATCH: 'Checking the mirror is like scratching an itch — relief for a moment, then it itches more.' Good with adolescents for explaining why rituals backfire.",
 ],

 "language": [
  "Use 'body dysmorphic disorder' only where diagnosed; otherwise 'significant appearance-related distress' or 'appearance preoccupation'.",
  "Avoid 'vain', 'obsessed with her looks', 'attention-seeking' in reports and conversation. PSI 1.2.8.",
  "Do not describe the perceived flaw in detail in a report — the young person may read it, and naming the feature can increase shame. 'Preoccupation with an aspect of facial appearance' is enough.",
  "Keep gender-related body distress separate and use the young person's own terms; do not fold it into BDD language.",
 ],

 "red_flags": [
  "RED FLAG — suicidal thoughts, self-harm or hopelessness ('I can't live like this'). Same-day risk route: inform the DLP, follow the service risk protocol, contact the parent unless doing so raises risk, and arrange a same-day GP / CAMHS / emergency response. Supervision follows action; it does not replace it.",
  "RED FLAG — self-inflicted 'corrections' (cutting, picking, DIY procedures), anabolic steroid use or severe food restriction. Medical review via GP the same day or week depending on severity.",
  "RED FLAG — complete school avoidance or not leaving the house. Escalate the referral; this is severe BDD or severe depression until shown otherwise.",
  "RED FLAG — appearance-related bullying, online harassment or image-based abuse (sharing of intimate images). Follow the anti-bullying procedure; for image-based abuse or any sexual exploitation, follow Children First and report to Tusla as soon as practicable — telling the DLP does not discharge a mandated person's duty. Consider An Garda Síochána where the law may have been broken (check current legislation).",
  "BOUNDARY — you do not diagnose BDD, do not advise on medication, cosmetic or dermatological treatment, and do not deliver specialist CBT outside your service's remit. PSI 2.2.2.",
  "WATCH — increasing lateness, absence from PE, avoidance of photographs and heavy make-up, hats or hoods worn to hide a feature.",
 ],

 "child_voice": [
  "SCALING DISTRESS AND TIME ('How much of today did it take up, 0–10?') — good because it maps impact without discussing the flaw itself.",
  "'A DAY IN MY LIFE' timeline — the young person marks where appearance worry is loudest (mirrors, PE, photos, social media). Good because it locates school triggers for the plan.",
  "WHAT I'VE STOPPED DOING list — good because it shows impairment in the young person's own words and gives a baseline for recovery goals.",
  "RCADS SELF-REPORT or MFQ — standardised screens for anxiety and mood that often sit with BDD. Good as a structured way to report low mood; they do not measure BDD and do not replace the face-to-face risk question.",
 ],

 "questions": [
  "Q: 'Shouldn't I just tell her she's beautiful?' — A: 'It's the most natural thing to say. With BDD it tends not to land — she hears it as kindness, not truth, and needs to ask again. Acknowledging how upset she is, without arguing about her looks, usually helps more.'",
  "Q: 'Would paying for the procedure fix it?' — A: 'That's not a decision for me, and her doctor should be involved. What's known is that with BDD, cosmetic treatments often don't relieve the distress — the worry commonly moves to another feature. Treatment for the BDD itself is the recommended route.'",
  "Q: 'Is this from social media?' — A: 'Social media and photo filters can feed appearance worries, and it's worth looking at together. But BDD usually has several causes — it isn't just the phone, and taking it away won't fix it on its own.'",
  "Q: 'Is she at risk?' — A: 'Young people with BDD can feel very hopeless, so I always ask directly. [State what she said.] If you're ever worried about her safety, contact the GP or go to the emergency department that day.'",
  "Q: 'Isn't this just being a teenager?' — A: 'Most teenagers dislike something about how they look. What we're seeing is different: hours a day, rituals, avoiding school and photos, and a lot of distress. That's what makes it a clinical concern.'",
  "Q: 'Can you diagnose BDD?' — A: 'No — CAMHS would assess that. I can describe what's happening in school, make sure the risk is being handled, put a school plan in place and refer.'",
 ],

 "supervision": [
  "Talk through the risk conversation for BDD before you have it — the wording, what counts as acting the same day, and whom you phone first.",
  "Bring a case where the question is BDD, eating disorder or gender-related distress, and discuss how to keep each distinct and non-pathologising.",
  "Clarify local CAMHS pathways and whether there is any specialist BDD expertise available to young people in the area.",
  "Discuss how to advise on social media and phone use without moralising or blaming the young person or family.",
 ],

 "reflection": [
  "ON RISK — Did I ask directly about suicidal thoughts and self-harm, and did I act on the answer the same day?",
  "ON REASSURANCE — Did I find myself saying 'but you look fine'? What did I do with the urge?",
  "ON LANGUAGE — Does my report describe distress and impairment, or does it describe the young person's appearance?",
  "ON DIFFERENTIAL — Did I consider eating disorder, depression, social anxiety and gender-related distress, and keep each distinct?",
  "ON MY OWN ASSUMPTIONS — Did I underestimate the severity because appearance concern is 'normal' in adolescence?",
  "WHAT GOOD LOOKS LIKE: 'The referral said \"refusing PE and photos\". She told me she spent three hours a day on her skin and felt hopeless. I asked about suicidal thoughts; she had passive thoughts, no plan. Same-day DLP, parent and GP contact; CAMHS referral; a short-term school plan for PE, photos and presentations, reviewed jointly.'",
  "WHAT POOR LOOKS LIKE: 'Student has low self-esteem about appearance. Staff to offer positive comments on her appearance.' — no risk question, reassurance recommended as the intervention, no referral.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). American Psychiatric Publishing.",
  "National Institute for Health and Care Excellence. (2005). Obsessive-compulsive disorder and body dysmorphic disorder: Treatment (Clinical Guideline CG31). NICE. [Check for updates.]",
  "Phillips, K. A. (2007). Suicidality in body dysmorphic disorder. Primary Psychiatry, 14(12), 58–66. [Check volume and pages before quoting.]",
  "Angelakis, I., Gooding, P. A., & Panagioti, M. (2016). Suicidality in body dysmorphic disorder (BDD): A systematic review with meta-analysis. Clinical Psychology Review, 49, 55–66.",
  "Veale, D., Gledhill, L. J., Christodoulou, P., & Hodsoll, J. (2016). Body dysmorphic disorder in different settings: A systematic review and estimated weighted prevalence. Body Image, 18, 168–186.",
  "Bjornsson, A. S., Didie, E. R., Grant, J. E., Menard, W., Stalker, E., & Phillips, K. A. (2013). Age at onset and clinical correlates in body dysmorphic disorder. Comprehensive Psychiatry, 54(7), 893–903.",
  "Mataix-Cols, D., Fernández de la Cruz, L., Isomura, K., Anson, M., Turner, C., Monzani, B., Cadman, J., Bowyer, L., Heyman, I., Veale, D., & Krebs, G. (2015) [check full author list]. A pilot randomized controlled trial of cognitive-behavioral therapy for adolescents with body dysmorphic disorder. Journal of the American Academy of Child & Adolescent Psychiatry, 54(11), 895–904.",
  "Veale, D., Willson, R., & Clarke, A. (2009). Overcoming body image problems including body dysmorphic disorder. Robinson.",
 ],

 "pathway": {
  "age": "Most often begins in adolescence (Bjornsson et al., 2013), when appearance, peer comparison and image-based social media become central. Identification is frequently delayed by years: young people hide it out of shame, and adults read it as ordinary teenage self-consciousness, low self-esteem, depression or social anxiety. Late arrival, PE and photo avoidance and heavy camouflaging are often the first things school sees.",
  "who_diagnoses": "Ireland: CAMHS (psychiatrist, clinical psychologist or MDT) via GP referral; private psychiatrist or clinical psychologist; adult mental health services from 18. Specialist BDD expertise is limited — check what is available locally. Medication, if considered, is a psychiatric decision. Emergency department / on-call CAMHS for acute risk.",
  "who_wrote_report": "CAMHS psychiatrist, clinical psychologist or MDT; private psychiatrist or clinical psychologist. A dermatologist or GP may have noted appearance concern but would usually refer on for diagnosis. A BDD questionnaire score in a school report is a screen, not a diagnosis.",
  "refer_to": "SAME-DAY GP / CAMHS / emergency department if suicidal ideation or self-harm. Otherwise GP for CAMHS referral. GP for dermatological harm from picking or DIY procedures. Tusla (and Gardaí where relevant) for image-based abuse or exploitation. Jigsaw (12–25) for support where available.",
  "sooner": "'BDD is one of the most hidden conditions there is — young people are usually too ashamed to say what they're thinking, and appearance worries are easy to put down to being a teenager. You've noticed now, and there is specific treatment that helps.'",
 },

 "differential": [
  "ORDINARY ADOLESCENT APPEARANCE CONCERN — present in most teenagers, without hours of preoccupation, rituals or impairment.",
  "EATING DISORDER — concern mainly with weight and shape plus disordered eating; assess and refer via GP; may co-occur.",
  "GENDER DYSPHORIA — distress related to gender identity and sex characteristics; not BDD; separate, non-pathologising pathway.",
  "SOCIAL ANXIETY — fear of general negative evaluation rather than of a specific perceived flaw.",
  "DEPRESSION — low self-worth including about appearance, without the specific preoccupation and rituals.",
  "PSYCHOSIS / DELUSIONAL BELIEFS — BDD with absent insight can look delusional; the clinician decides. Urgent CAMHS if other psychotic features are present.",
  "A GENUINE, OBSERVABLE CONDITION (e.g. acne, scarring, a visible difference) — then distress may be understandable and dermatological or medical input may help; BDD applies when concern is markedly excessive.",
 ],

 "next": [
  "Ask directly about suicidal thoughts and self-harm; act the same day if present.",
  "Map the rituals, avoidance and school triggers with the young person, without debating the flaw.",
  "Consider eating disorder, depression, social anxiety and gender-related distress; keep them distinct.",
  "Agree a short-term school plan (PE, photos, presentations, staff response without reassurance) with a review date.",
  "Refer via GP to CAMHS; same-day route if risk is present.",
 ],

 "presentations": [
  "Appearance preoccupation and mirror checking",
  "Avoidance of PE changing, photographs or presentations",
  "Late arrival linked to grooming or camouflaging",
  "Reassurance-seeking about appearance",
  "Excessive exercise and supplement use (muscle concern)",
 ],

 "bands": {
  "Early Years": {
   "applies": "N/A — BDD is not a presentation of early childhood",
   "prevalence": "Not applicable at this band — no figure.",
   "see": "Young children may be distressed by teasing about a visible difference or by others' comments, but this is not BDD. Address teasing and any visible-difference support needs; refer medically if there is a real condition of concern.",
   "tools": [],
  },
  "School Age": {
   "applies": "RARELY — onset can occur in late primary, but it is uncommon",
   "prevalence": "Rate at this age not stated here — check before quoting.",
   "see": "Late primary: persistent distress about one feature, reluctance to be photographed, repeated questions about looks, hiding under hoods or hair. Differentiate from teasing, a visible difference, or early eating concerns. Ask about mood and safety.",
   "tools": ["RCADS", "RCADS self-report", "SDQ"],
  },
  "Adolescent": {
   "applies": "YES — the peak onset period",
   "prevalence": "About 2% of adolescents in a systematic review (Veale et al., 2016) — check before quoting.",
   "see": "Hours of mirror checking or avoiding mirrors, heavy make-up or camouflaging, lateness, PE and photo avoidance, comparing with peers and online images, picking at skin, seeking cosmetic treatments, excessive gym use, low mood, hopelessness. Ask about suicidal thoughts every time.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Beck Youth Inventories-2", "Body Dysmorphic Disorder Questionnaire (BDDQ; Phillips) — AGE adolescent/adult versions reported · MEASURES: brief self-report screen for appearance preoccupation and impact · CANNOT TELL YOU: diagnosis or risk · TIME: about 5 min — check which version is validated for adolescents before use"],
  },
  "Young Adult": {
   "applies": "YES — onset and persistence continue; adult mental health holds the case",
   "prevalence": "About 2% in community adults (Veale et al., 2016) — check before quoting.",
   "see": "Avoidance of lectures, placements or work because of appearance; seeking cosmetic procedures; social withdrawal; depression. Refer to GP, college counselling or adult mental health; same-day route for risk.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "RARELY — may be present but hard to identify where language is limited",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Persistent distress about a body part, repeated touching or checking, and avoidance of mirrors or photos may occur, but alternative explanations (sensory, autistic routine, medical discomfort) are more common. Observe, gather informant report and involve the CDNT and GP.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3"],
  },
 },
},

# =====================================================================================
# 3. TRICHOTILLOMANIA AND EXCORIATION (SKIN-PICKING) DISORDER
# =====================================================================================
{
 "name": "Trichotillomania and Excoriation (skin-picking) Disorder",
 "code": "DSM-5-TR Trichotillomania (F63.3) · Excoriation Disorder (L98.1) · ICD-11 6B25.0 Trichotillomania · 6B25.1 Excoriation disorder (under 6B25 Body-focused repetitive behaviour disorders) — check codes before quoting",
 "neps": "3. EMOTIONAL (3.3 Obsessive-compulsive and related) — and 3.2 Anxiety",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "TRICHOTILLOMANIA — recurrent pulling out of one's own hair (scalp, eyebrows, eyelashes or elsewhere) resulting in hair loss, with repeated attempts to reduce or stop, causing significant distress or impairment (APA, 2022, DSM-5-TR).",
  "EXCORIATION (SKIN-PICKING) DISORDER — recurrent skin picking resulting in skin lesions, with repeated attempts to stop, causing distress or impairment, and not better explained by a skin condition, substance or another mental disorder (APA, 2022).",
  "Together they are called BODY-FOCUSED REPETITIVE BEHAVIOURS (BFRBs). DSM-5-TR places them in the obsessive-compulsive and related chapter; ICD-11 groups them under 6B25 Body-focused repetitive behaviour disorders (WHO, 2019). Unlike OCD, they are not usually driven by an obsessional thought.",
  "Pulling and picking can be AUTOMATIC (outside awareness — while reading, watching screens, lying in bed) or FOCUSED (deliberate, in response to an urge, tension, boredom, a 'wrong' feeling hair or skin, or strong emotion). Most people who pull do both (Flessner et al., 2008 — adult sample). This matters for the plan.",
  "The behaviour is often REGULATING — it soothes, relieves tension or stimulates — which is why willpower and telling off do not work. Shame is typical and the behaviour is usually hidden.",
  "The best-evidenced treatment is HABIT REVERSAL TRAINING (HRT) — awareness training, a competing response and social support (Azrin & Nunn, 1973) — often within a broader behavioural or CBT approach. An RCT found behaviour therapy effective for paediatric trichotillomania (Franklin et al., 2011). It is delivered by trained clinicians.",
 ],

 "what_it_is_not": [
  "NOT self-harm in the usual sense. The aim is usually soothing or regulating, not injury, and treating it as self-harm can increase shame. But ask about self-harm separately — both can be present.",
  "NOT a 'bad habit' the child could stop if they tried. Most young people have tried repeatedly. Punishment, nagging and public comment increase tension and hiding and usually make it worse.",
  "NOT OCD, though related. There is usually no obsessional thought or feared outcome driving it; the driver is an urge, a sensation or an emotional state.",
  "NOT attention-seeking. Most children go to great lengths to hide bald patches or scabs.",
  "NOT always a disorder in young children. Hair-pulling that starts in the toddler and preschool years is often associated with soothing and frequently resolves — rate not stated here, check before quoting.",
  "NOT alopecia, a skin condition or a medical problem to be assumed away — hair loss and skin lesions need a GP to rule out medical causes (e.g. alopecia areata, eczema, scabies) before behavioural explanations are assumed.",
  "NOT a diagnosis the EP makes. GP, dermatology, CAMHS or a clinical psychologist diagnoses. The EP describes, supports the school response and refers.",
 ],

 "prevalence": [
  "ADULT: DSM-5-TR states a 12-month prevalence of about 1–2% for trichotillomania in adults and adolescents (APA, 2022). EXCORIATION: DSM-5 (2013) gave adult lifetime prevalence of 1.4% or somewhat higher; a later US survey of 10,169 adults found 3.1% lifetime and 2.1% current (Grant & Chamberlain, 2020) — check which figure the DSM-5-TR text uses before quoting.",
  "CHILDREN: rate for school-age children not stated here — check before quoting.",
  "AGE OF ONSET: trichotillomania most commonly begins around puberty; excoriation most commonly in adolescence, often with acne (APA, 2022) — check before quoting.",
  "IRELAND: no national prevalence figure stated here — check before quoting.",
  "SEX RATIO: in adolescence and adulthood more females than males are identified; in early childhood the ratio is closer to even (APA, 2022) — exact ratio not stated here, check.",
  "UNDER-IDENTIFICATION: shame and hiding (hats, hair styles, make-up, long sleeves) mean many young people are never identified.",
 ],

 "cooccurring": [
  {"name": "ANXIETY",
   "rate": "common — rate not stated here, check",
   "presents": "Pulling or picking increases under stress, before exams, or at bedtime. Map the emotional triggers; anxiety support and HRT work together."},
  {"name": "DEPRESSION / LOW MOOD",
   "rate": "elevated — rate not stated here, check",
   "presents": "Shame, hiding, withdrawal and hopelessness about stopping. Ask about mood and about self-harm directly."},
  {"name": "OCD",
   "rate": "elevated — rate not stated here, check",
   "presents": "Pulling or picking linked to 'just right' feelings plus other obsessions and compulsions. Describe both in the referral."},
  {"name": "BODY DYSMORPHIC DISORDER",
   "rate": "skin-picking is common in BDD — rate not stated here, check",
   "presents": "Picking to 'fix' a perceived flaw in appearance. If appearance preoccupation is the driver, the concern is BDD and the risk questions for BDD apply."},
  {"name": "ADHD",
   "rate": "elevated — rate not stated here, check",
   "presents": "Automatic pulling or picking during sustained seated tasks, alongside fidgeting. Fidget tools can double as competing responses."},
  {"name": "AUTISM",
   "rate": "elevated — rate not stated here, check",
   "presents": "Picking or pulling as sensory regulation. Consider sensory-based alternatives with OT input; distinguish from self-injury in special settings."},
  {"name": "OTHER BFRBs (nail-biting, cheek-biting, lip-picking)",
   "rate": "commonly co-occur — rate not stated here, check",
   "presents": "Several body-focused behaviours at once. The HRT approach is the same; list them all."},
 ],

 "recommendations": [
  "DON'T PUNISH OR DRAW ATTENTION. No public comment, no telling off, no 'hands down'. Agree with the young person a private, pre-arranged cue if they want one — or none at all. Protect them from peer comment and bullying about bald patches or marks.",
  "DESCRIBE THE PATTERN (not the young person): when, where, during which activities, and whether automatic or focused. A simple self- or teacher-kept log for two weeks, agreed with the young person, gives the baseline.",
  "KEEP HANDS BUSY IN HIGH-RISK SITUATIONS: fidget items, putty, a textured object, doodling during listening tasks — offered to everyone or discreetly, so the young person is not singled out. These support competing responses; they are not treatment on their own.",
  "HABIT REVERSAL VIA TRAINED CLINICIANS: HRT (awareness training, competing response, social support; Azrin & Nunn, 1973) and related behavioural approaches are delivered by trained clinicians — refer via GP to CAMHS or Primary Care Psychology, or signpost a private clinician with BFRB training. School supports the plan; school does not run it.",
  "HEADWEAR AND UNIFORM: permit a hat, scarf or hairstyle that conceals hair loss, and long sleeves or plasters for skin lesions, where the young person wants this — check school uniform policy and apply it flexibly (Equal Status Acts considerations — check).",
  "EMOTIONAL REGULATION AND STRESS: where triggers are emotional (exams, transitions), build in the anxiety plan and regulation strategies.",
  "CONTINUUM LEVEL: Classroom Support for mild, well-hidden cases with low impact; School Support where there is distress or peer difficulty; School Support Plus where clinical services are involved.",
  "REFER: GP for any dermatological harm (infection, bleeding, open wounds, scarring), for hair loss (to rule out medical causes) and for swallowing hair (trichophagia) — URGENT if abdominal pain, vomiting or weight loss. GP to CAMHS or Primary Care Psychology for behavioural treatment — check local criteria.",
  "DO NOT advise on medication or topical treatments (PSI 2.2.2); do not recommend punishment, reward charts for 'not pulling' without clinical guidance, or physical barriers imposed without the young person's agreement.",
 ],

 "explain_parent": [
  "'Hair-pulling and skin-picking are called body-focused repetitive behaviours. They're much more common than people think, and they usually happen because they soothe or relieve tension — often without her noticing.'",
  "'It's not a bad habit she could stop by trying harder. She almost certainly has tried. Telling her off or pointing it out usually makes the tension, and the pulling, worse.'",
  "'The treatment with the best evidence is called habit reversal. A trained clinician helps her notice when it's about to happen and do something else with her hands. Your part is support, not policing.'",
  "'Please get the GP to look at her scalp or skin — partly to rule out other causes, and partly because picked skin can get infected. If she swallows hair and has tummy pain or vomiting, see the GP straight away.'",
  "SIGNPOST: GP; The TLC Foundation for BFRBs (US, online resources) → https://www.bfrb.org/; Trichotillomania Support (UK) — check current services; CAMHS or Primary Care Psychology via GP.",
 ],

 "explain_teacher": [
  "'He's not doing it on purpose and he's not doing it for attention. Most of the time he doesn't know he's doing it.'",
  "'Please don't comment on it in class or tell him to stop. That makes it worse and it tells the class. If he wants a private signal, we'll agree one with him.'",
  "'Fidget items and something to do with his hands during listening tasks help — offer them to the whole group if you can.'",
  "'Watch for teasing about his hair or skin. Treat it as bullying.'",
  "'If you notice open wounds, bleeding or signs of infection, tell his parents so the GP can see it.'",
 ],

 "explain_child": [
  "YOUNGER: 'Lots of people have a thing their hands do that helps them feel calm — twirling hair, picking, biting nails. Sometimes it gets stuck on and is hard to stop. That's not your fault. There are tricks that can help your hands do something else.'",
  "OLDER: 'Pulling and picking are really common — they usually happen because they take the edge off tension or boredom, often without you noticing. It's not about willpower. There's a method called habit reversal where you learn to notice the moment before and do something else. It works for a lot of people.'",
  "ASK: 'When does it happen most — what are you doing, where are you, how are you feeling?' 'Do you notice it at the time or only afterwards?' 'What have you tried?' These separate automatic from focused pulling and show what they have already attempted.",
  "ASK: 'Does anyone say things about your hair or skin?' — peer comment is common and hidden.",
  "ASK ABOUT MOOD AND SELF-HARM separately and directly where age-appropriate; act the same day if there is risk.",
 ],

 "analogies": [
  "THE AUTOPILOT: 'Your hands go on autopilot when your brain is busy — like driving a familiar road and not remembering the journey. Habit reversal teaches you to notice when autopilot switches on.' Good with adolescents and parents; explains automatic pulling.",
  "THE PRESSURE VALVE: 'Picking lets off a bit of steam — that's why it feels good for a second. We want other ways to let the steam out.' Good with parents and teachers; explains why punishment backfires.",
  "THE ITCH THAT ISN'T THERE: 'It's like an itch — scratching feels right for a moment and then makes the itch come back.' Good with younger children.",
 ],

 "language": [
  "'Hair-pulling', 'skin-picking' and 'body-focused repetitive behaviours (BFRBs)' are accepted, neutral terms. Use 'trichotillomania' or 'excoriation disorder' only where diagnosed.",
  "Avoid 'bad habit', 'nervous habit', 'self-mutilation' or 'attention-seeking' in reports and conversation. PSI 1.2.8.",
  "Do not describe bald patches or lesions in detail in a report beyond what is needed for the referral; the young person may read it.",
  "Use the young person's own word for it ('my picking', 'the pulling') in the child's-voice section.",
 ],

 "red_flags": [
  "RED FLAG — swallowing hair (trichophagia) with abdominal pain, vomiting, loss of appetite or weight loss: risk of a hairball (trichobezoar). URGENT GP / emergency medical review the same day.",
  "RED FLAG — infected, bleeding or deep skin lesions, or picking near the eyes. GP the same day or week depending on severity; dermatology via GP.",
  "RED FLAG — self-harm with intent to injure, suicidal thoughts or hopelessness alongside picking or pulling. Same-day risk route: DLP, service risk protocol, parent (unless doing so raises risk), same-day GP / CAMHS / emergency response. Supervision follows action; it does not replace it.",
  "RED FLAG — sudden onset linked to a stressor at home or unexplained injuries. Consider abuse or neglect; follow Children First; report to Tusla as soon as practicable — telling the DLP does not discharge a mandated person's duty.",
  "BOUNDARY — you do not diagnose, do not deliver habit reversal outside your service's remit and training, and do not advise on medication or topical treatments. PSI 2.2.2.",
  "WATCH — peer teasing, hats and hoods, refusal of PE or swimming, long sleeves in warm weather.",
 ],

 "child_voice": [
  "'WHEN AND WHERE' MAP — the young person marks times, places and activities when pulling or picking is most likely. Good because it builds awareness (the first step of HRT) and gives the school plan its targets.",
  "SCALING urge strength and awareness ('how much did you notice it today?') — good because it tracks the thing HRT changes, not just the behaviour count.",
  "WHAT HELPS / WHAT MAKES IT WORSE list — good because it puts the young person in charge of which adjustments and which cues (if any) they want, and protects them from well-meant but shaming responses.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — good for surfacing stress points and peer comment without leading. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
 ],

 "questions": [
  "Q: 'Should I tell her to stop every time I see her do it?' — A: 'It's the natural thing to do, and it usually backfires — it adds tension and shame, and she'll hide it more. Agree with her whether she wants a private signal at all. The treatment works by building her own awareness, not by others policing it.'",
  "Q: 'Is this self-harm?' — A: 'Usually not in the sense of wanting to hurt herself — it tends to be soothing. I've asked her separately about self-harm and her mood, because both can be present, and we'll act on that if needed.'",
  "Q: 'Will she grow out of it?' — A: 'Hair-pulling that starts very young often settles. When it starts around puberty it can last longer without help. Habit reversal with a trained clinician works for many young people, so it's worth getting a referral.'",
  "Q: 'Can he wear a hat in class?' — A: 'I'd recommend the school allows it while he's getting help. Being able to hide the hair loss reduces a lot of stress, and less stress usually means less pulling. I'll put that in the plan.'",
  "Q: 'Is it dangerous?' — A: 'Mostly not, but two things need a doctor: skin that's infected or bleeding, and swallowing hair — if there's tummy pain or vomiting, see the GP straight away.'",
  "Q: 'Can you diagnose it?' — A: 'No — the GP, a dermatologist, CAMHS or a clinical psychologist would. I can describe the pattern, help school respond without shaming, and refer.'",
 ],

 "supervision": [
  "Ask where local families can access habit reversal from a trained clinician — CAMHS, Primary Care Psychology, private — and what the waiting times are.",
  "Bring a case where picking could be self-harm, a BFRB, BDD or sensory regulation, and talk through the questions that separate them.",
  "Discuss how to advise on uniform flexibility (hats, sleeves) and bullying prevention without singling the young person out.",
  "Clarify when a dermatological concern crosses from 'mention to parents' into 'same-day GP' in your service's protocol.",
 ],

 "reflection": [
  "ON TONE — Did my recommendations protect the young person from attention and shame, or did they build in public prompts and monitoring?",
  "ON ROLE — Did I leave habit reversal to a trained clinician and write a supportive school plan, or did I slip into delivering treatment?",
  "ON MEDICAL — Did I make sure a GP had seen the hair loss or skin before assuming a behavioural explanation?",
  "ON RISK — Did I ask separately about self-harm and mood, and about swallowing hair?",
  "ON VOICE — Did the young person decide which adjustments and cues they wanted?",
  "WHAT GOOD LOOKS LIKE: 'The teacher had been saying \"hands down\" in class. The girl mapped her pulling to silent reading and bedtime. We stopped public prompts, offered fidget items to the whole group, allowed a headband, and wrote to the GP for referral to a clinician trained in habit reversal. At review she said the class had stopped noticing.'",
  "WHAT POOR LOOKS LIKE: 'Child has a nervous habit of pulling hair. Teacher to remind her to stop and use a reward chart.' — public attention, no GP check, no referral, no child's voice.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). American Psychiatric Publishing.",
  "World Health Organization. (2019). International classification of diseases for mortality and morbidity statistics (11th rev.). WHO.",
  "Azrin, N. H., & Nunn, R. G. (1973). Habit-reversal: A method of eliminating nervous habits and tics. Behaviour Research and Therapy, 11(4), 619–628.",
  "Franklin, M. E., Edson, A. L., Ledley, D. A., & Cahill, S. P. (2011). Behavior therapy for pediatric trichotillomania: A randomized controlled trial. Journal of the American Academy of Child & Adolescent Psychiatry, 50(8), 763–771.",
  "Flessner, C. A., Conelea, C. A., Woods, D. W., Franklin, M. E., Keuthen, N. J., & Cashin, S. E. (2008). Styles of pulling in trichotillomania: Exploring differences in symptom severity, phenomenology, and functional impact. Behaviour Research and Therapy, 46(3), 345–357. [Check author list and pages before quoting.]",
  "Grant, J. E., & Chamberlain, S. R. (2020). Prevalence of skin picking (excoriation) disorder. Journal of Psychiatric Research, 130, 57–60.",
  "Woods, D. W., & Twohig, M. P. (2008). Trichotillomania: An ACT-enhanced behavior therapy approach. Therapist guide. Oxford University Press.",
 ],

 "pathway": {
  "age": "Trichotillomania most commonly begins around puberty; excoriation most commonly in adolescence, often starting with acne (APA, 2022 — check). Very early hair-pulling (toddler and preschool years) is often soothing and may resolve. Identification is delayed because young people hide patches and lesions; school may first notice hats, hoods, gaps in eyebrows or lashes, marks on arms or face, or teasing.",
  "who_diagnoses": "Ireland: GP (first point, and to rule out medical causes), dermatology via GP, CAMHS or Primary Care Psychology via GP, or a private clinical psychologist or psychiatrist. Clinicians trained in habit reversal for BFRBs are limited — check local availability before advising families. Medication or topical treatment is a medical decision.",
  "who_wrote_report": "GP, dermatologist, CAMHS clinician, Primary Care or private clinical psychologist. A dermatology letter may describe the physical findings and suggest a behavioural cause without a psychological assessment.",
  "refer_to": "GP for all hair loss and skin damage (same day if infected or if hair-swallowing with abdominal symptoms). GP to CAMHS or Primary Care Psychology for behavioural treatment — check local criteria. OT (via CDNT or Primary Care) where sensory regulation is a driver. Same-day risk route if self-harm or suicidal ideation. Tusla if abuse or neglect is suspected.",
  "sooner": "'Hair-pulling and skin-picking are usually hidden very well — young people are embarrassed and families often think it's a habit that will pass. It's very common for it to go on for a while before anyone asks for help, and help works at any stage.'",
 },

 "differential": [
  "MEDICAL HAIR LOSS OR SKIN CONDITION — alopecia areata, tinea, eczema, scabies, acne; GP review first.",
  "SELF-HARM — injury with intent to hurt, often to manage overwhelming emotion; assess risk separately; may co-occur.",
  "BODY DYSMORPHIC DISORDER — picking to correct a perceived appearance flaw; BDD risk questions apply.",
  "OCD — pulling or picking driven by obsessional thoughts or 'just right' rituals with other OCD features.",
  "SENSORY REGULATION / AUTISM — repetitive self-stimulation; OT and CDNT input.",
  "TIC DISORDER — preceded by a physical urge but not usually producing hair loss or lesions.",
 ],

 "next": [
  "Ask the young person when and where it happens, whether they notice it, and what they have tried; ask separately about mood, self-harm and hair-swallowing.",
  "Stop any public prompting or punishment; agree private supports and uniform flexibility with the young person.",
  "Recommend GP review for hair loss or skin damage; urgent if infection or abdominal symptoms.",
  "Refer via GP for habit reversal with a trained clinician (CAMHS, Primary Care Psychology or private); set a review date.",
 ],

 "presentations": [
  "Hair-pulling (not diagnosed)",
  "Skin-picking (not diagnosed)",
  "Nail-biting and other body-focused repetitive behaviours",
  "Fidgeting and self-soothing repetitive behaviour",
  "Visible hair loss or skin lesions noticed in school",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — early hair-pulling is often soothing and transient",
   "prevalence": "Rate at this age not stated here — check before quoting.",
   "see": "Hair-twirling and pulling at sleep time, when tired or with a comfort object; often resolves. Concern if hair loss is marked, if hair is swallowed, or if skin is damaged. GP first; support parents to respond calmly and substitute soothing activities.",
   "tools": ["SDQ (2–4 version)"],
  },
  "School Age": {
   "applies": "YES — onset rises towards puberty",
   "prevalence": "Rate for this band not stated here — check before quoting.",
   "see": "Pulling or picking during reading, listening or screen time; eyebrow or eyelash gaps; hats and hair styles hiding patches; scabs on fingers or arms; peer teasing. Map when and where; stop public prompts; GP review; referral for habit reversal.",
   "tools": ["SDQ", "RCADS", "Milwaukee Inventory for Styles of Trichotillomania–Child Version (MIST-C; Flessner et al., 2007) — AGE about 10–17 self-report · MEASURES: automatic and focused pulling styles · CANNOT TELL YOU: diagnosis, severity alone or risk · TIME: about 5–10 min — check version and availability before use"],
  },
  "Adolescent": {
   "applies": "YES — the peak onset period, especially excoriation with acne",
   "prevalence": "12-month trichotillomania about 1–2% in adults and adolescents (APA, 2022) — check before quoting.",
   "see": "Hidden pulling or picking, heavy make-up or long sleeves, avoidance of PE, swimming or photos, shame and low mood. Distinguish from BDD (picking to fix appearance) and from self-harm. Ask about mood and self-harm directly.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Beck Youth Inventories-2"],
  },
  "Young Adult": {
   "applies": "YES — often persistent; adult services hold the case",
   "prevalence": "Adult 12-month trichotillomania about 1–2% (APA, 2022); excoriation lifetime 1.4% or higher (DSM-5) to 3.1% (Grant & Chamberlain, 2020) — check before quoting.",
   "see": "Pulling or picking during study or screen work, avoidance of social situations and relationships because of appearance, shame. Refer to GP, college counselling or adult psychology.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — but repetitive skin and hair behaviours often have sensory or communicative functions here",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Picking or pulling may be self-stimulation, a response to pain or discomfort (check medical causes), communication of distress, or self-injury. Functional assessment, OT input via CDNT, and GP review for skin damage come before a BFRB formulation.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3"],
  },
 },
},
]
