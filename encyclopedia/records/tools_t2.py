"""Part G tool teaching records — batch t2 (ten tools).

Written to agree with src/tool_catalogue.json (variants RCADS self-report,
BASC-3 SRP, ADOS-2 Toddler/Module 1-4 and Vineland-3 adult are covered inside
their parent entries) and Reference Part D (rows 507-650).
No norms, cut-offs, reliability figures or item counts are stated as fact
unless widely documented and attributed; otherwise 'check the manual'.
"""

TOOLS = [
# ---------------------------------------------------------------- RCADS
{
 "name": "RCADS",
 "before": [
  "Know what it is: the Revised Child Anxiety and Depression Scale (Chorpita et al., 2000) is a questionnaire mapped onto DSM-IV anxiety and depression categories — separation anxiety, social phobia, generalised anxiety, panic, obsessive-compulsive and major depression subscales. It is free to use; download it and the scoring program from the authors' current source and check you have the latest version.",
  "Choose the forms. There is a child/young person self-report and a parent version (RCADS-P; Ebesutani et al., 2010) covering roughly 8–18 (tool catalogue: 'RCADS self-report' is the same instrument). A shorter 25-item version exists; check which your service uses and do not mix scoring programs between them.",
  "Plan the risk step before you hand it over. The depression subscale asks about low mood and hopelessness, and a young person may disclose thoughts of death or self-harm on paper that they never said aloud. Know your service's same-day risk procedure and who the DLP is before the session, not after.",
  "Check reading level and language. If the child reads below the item level, or has EAL, read the items aloud in a neutral voice and record that you did — it is a procedural adaptation and goes in the report.",
  "Norms are from US school-grade samples and are split by sex and grade (Chorpita et al., 2000); there are no Irish norms. Check which norm tables your scoring program applies and translate Irish class to the appropriate grade with care.",
 ],
 "administer": [
  "Introduce it as 'questions about how you feel and what worries you — there are no right answers, and I will look at it with you before you go'. Tell the young person who will see the answers and what you would have to do if they told you they were unsafe — that is informed assent, not a threat.",
  "Stay in the room while it is completed. You are watching for hesitation, rubbed-out answers, questions about wording, and speed — a pupil who ticks 'never' down the column in ninety seconds is telling you something about engagement.",
  "Read the completed form before the young person leaves. Any endorsement on a depression item that touches on death, worthlessness or not wanting to be here is followed up then, in person, with direct questions. If there is risk: same-day risk route, DLP informed, and a report to Tusla as soon as practicable where there is a child protection concern — telling the DLP does not discharge your own duty as a mandated person (Children First Act 2015). Supervision follows the action; it does not replace it.",
  "Give the parent form separately and ask the parent to complete it alone. Parent and child ratings of anxiety commonly disagree; the disagreement is data (De Los Reyes & Kazdin, 2005).",
 ],
 "score": [
  "Items are rated on a four-point frequency scale (never / sometimes / often / always). Use the authors' scoring program or spreadsheet for T-scores by sex and grade; hand-summing is fine for raw scores but not for conversion.",
  "Report each subscale plus the total anxiety and total anxiety-and-depression scores, not only the total. Thresholds for 'borderline' and 'clinical' T-scores are set in the scoring guidance — check the manual rather than quoting from memory.",
  "Record missing items. Pro-rating rules for omitted items differ by version; check before you pro-rate, and say in the report if you did.",
 ],
 "interpret": [
  "It is a screen and a severity description, not a diagnosis (tool catalogue). A clinical-range subscale entitles you to write 'reports anxiety at a level that warrants further assessment' and to recommend referral — to Primary Care Psychology or, where severity, risk or impairment is high, via the GP to CAMHS.",
  "Look at the shape. Social anxiety elevated with separation anxiety low points toward class-based and peer demands; separation anxiety high in an 8-year-old points toward the morning drop-off and home–school transition. Link the shape to the EBSA picture and attendance data (Reference Part D).",
  "Read depression elevations as a risk question first and a planning question second. A raised depression subscale always gets a direct conversation about safety, whatever the anxiety scores show.",
  "Consider what else raises scores: bullying, bereavement, family stress, autism (social anxiety items overlap with social communication difficulty), and a pupil telling you what they think you want to hear. The RCADS has no validity scale; your observations are the check.",
  "Write the plan at the right Continuum level: Classroom Support (predictable routines, a named adult, planned check-ins), School Support (a small-group or individual CBT-informed programme, where the school has trained staff), School Support Plus (EP casework, referral). Re-administer after intervention to track change.",
 ],
 "errors": [
  "Letting a young person leave before you have read the depression items.",
  "Writing 'meets criteria for generalised anxiety disorder' from a questionnaire.",
  "Reporting only the total score and losing the subscale shape.",
  "Treating a low self-report as reassurance when the parent and teacher describe marked anxiety.",
  "Reading items aloud without recording that you did.",
 ],
 "read": [
  "Chorpita, B. F., Yim, L., Moffitt, C., Umemoto, L. A., & Francis, S. E. (2000). Assessment of symptoms of DSM-IV anxiety and depression in children: A revised child anxiety and depression scale. Behaviour Research and Therapy, 38(8), 835–855. — plus the current RCADS user's guide from the authors.",
  "Ebesutani, C., Bernstein, A., Nakamura, B. J., Chorpita, B. F., & Weisz, J. R. (2010). A psychometric analysis of the Revised Child Anxiety and Depression Scale—Parent Version in a clinical sample. Journal of Abnormal Child Psychology, 38(2), 249–260.",
  "De Los Reyes, A., & Kazdin, A. E. (2005). Informant discrepancies in the assessment of childhood psychopathology. Psychological Bulletin, 131(4), 483–509.",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government Publications. — the mandated-person sections.",
 ],
},

# ---------------------------------------------------------------- BASC-3
{
 "name": "BASC-3",
 "before": [
  "Know the family of forms (Reynolds & Kamphaus, 2015): Teacher Rating Scales (TRS) and Parent Rating Scales (PRS) at preschool, child and adolescent levels; Self-Report of Personality (SRP) at child, adolescent and college levels, with an interview version for younger children; plus the Structured Developmental History and the Student Observation System. The catalogue's 'BASC-3 SRP' is part of this entry. Check the exact age bands for each form in the manual before you choose.",
  "Decide why you want it. The BASC-3 is broad — externalising, internalising, school problems and adaptive skills in one instrument. That breadth suits a referral where you do not yet know what is driving the behaviour; for a narrow question (attention only, anxiety only) a focused measure is quicker and the Reference sheet (Part A, 'Behavioural and emotional rating scales') suggests the SDQ as a general first screen.",
  "Get at least a parent and a teacher form; at post-primary add the SRP and more than one subject teacher (Reference Part D, Adolescent). Is it all classes or some? That question often matters more than the scores.",
  "Norms are US. There are general and clinical norm groups, and combined-sex and sex-specific options — decide which you will use before scoring and state it in the report.",
 ],
 "administer": [
  "It is a rating scale, so administration is instruction: the time frame (recent months — check the form wording), rate what you see rather than what you think causes it, answer every item. Raters who have known the child only a few weeks are rating a stranger.",
  "For the SRP, stay with the young person, check reading level, read items aloud if needed and record it. Tell them in advance who will see it.",
  "Check the form for omissions before the rater leaves; too many omitted items invalidate a scale, and the threshold is in the manual.",
  "Look at critical items on the SRP and PRS the same day. Some items concern self-harm, hopelessness or feeling unsafe; an endorsement goes to the risk route that day, not to the report next week.",
 ],
 "score": [
  "Score through Q-global or by hand with the manual. Scores are T-scores with percentiles; clinical and adaptive scales run in opposite directions (high is concerning on clinical scales, low on adaptive scales). Check the classification bands in the manual before you label anything 'at risk' or 'clinically significant'.",
  "Check the validity indexes first — they flag inconsistent, overly negative or overly positive responding (the SRP has additional indexes). A 'caution' or 'extreme caution' flag changes how much weight you put on everything else.",
  "Report composites and the scales beneath them, rater by rater, in a table that lets the reader compare home, school and self side by side.",
 ],
 "interpret": [
  "It describes the pattern and leaves the formulation to you (tool catalogue). 'Elevated hyperactivity at school but not at home' is a finding; why is your hypothesis, to be tested with observation and interview.",
  "Treat rater differences as information about settings and demands, not as someone being wrong (De Los Reyes & Kazdin, 2005). Lay them out and ask each rater what the child is like when it goes well.",
  "Adaptive scales matter for planning: social skills, functional communication and study skills are what you build the intervention on. Do not leave them out because the clinical scales are more dramatic.",
  "Elevated attention, anxiety or depression scales are reasons to refer or investigate, not diagnoses. ADHD goes to CAMHS or paediatrics; persistent low mood with impairment goes via the GP. You describe and recommend (PSI 2.2.2).",
  "Pitch recommendations at the Continuum level: a whole-class behaviour approach at Classroom Support, a targeted plan with a named adult at School Support, a functional behaviour assessment and multi-agency plan at School Support Plus.",
 ],
 "errors": [
  "Skipping the validity indexes.",
  "Reading high adaptive scores as a problem, or low clinical scores as reassurance, because the directions were confused.",
  "Finding a critical item on the SRP after the young person has gone home.",
  "Writing 'has ADHD' or 'is depressed' from rating-scale elevations.",
  "Not stating that the norms are US and which norm group was used.",
 ],
 "read": [
  "Reynolds, C. R., & Kamphaus, R. W. (2015). BASC-3: Behavior Assessment System for Children (3rd ed.) manual. Pearson. — the chapters on validity indexes and interpretation.",
  "De Los Reyes, A., & Kazdin, A. E. (2005). Informant discrepancies in the assessment of childhood psychopathology. Psychological Bulletin, 131(4), 483–509.",
  "Achenbach, T. M., McConaughy, S. H., & Howell, C. T. (1987). Child/adolescent behavioral and emotional problems: Implications of cross-informant correlations for situational specificity. Psychological Bulletin, 101(2), 213–232.",
 ],
},

# ---------------------------------------------------------------- ADOS-2
{
 "name": "ADOS-2",
 "before": [
  "Know what it is: the Autism Diagnostic Observation Schedule, Second Edition (Lord et al., 2012) is a standardised, semi-structured observation of social communication, play and restricted/repetitive behaviour. There is a Toddler Module and Modules 1–4, chosen by expressive language level and age, not age alone — pre-verbal or single words (Toddler, Module 1), phrase speech (Module 2), fluent speech in children and younger adolescents (Module 3), fluent speech in older adolescents and adults (Module 4). The catalogue's 'ADOS-2 Toddler / Module 1', 'Module 2/3' and 'Module 3/4' are all this entry.",
  "Know who administers it. The ADOS-2 requires specific training — a recognised clinical training course and supervised practice — and is normally used within a multidisciplinary diagnostic process. In Ireland that is usually the HSE CDNT, CAMHS or a specialist assessment service (including Assessment of Need pathways under the Disability Act 2005), or a private diagnostic team. Check the publisher's and your service's current training requirement; a trainee EP on a school placement will almost never administer it.",
  "What the EP does with an ADOS-2 report: read it for what the child did in that structured hour — eye contact, gesture, reciprocal conversation, play, sensory interests — and set it beside what you see in class and yard. Use the observations (not the classification) to plan: where the child needs visual structure, explicit social teaching, predictable transitions, and adaptations to language demands.",
  "What the EP must not do: administer it without the training; re-score or re-run the algorithm from a report; tell a parent or school 'the ADOS shows autism' or 'the ADOS rules out autism'; treat a classification as the diagnosis; or use it as a school screening tool. Diagnosis is made by the team against DSM-5-TR or ICD-11 criteria, integrating history (e.g. ADI-R), observation and other information (NICE, 2011/2017).",
 ],
 "administer": [
  "If you are not trained, you do not administer it — say so plainly if a school or parent asks. What you can contribute to the diagnostic team is the school picture: structured classroom and yard observation, teacher information, SRS-2 or SCQ where appropriate, and your own account of the child across settings (Reference Part D).",
  "If you observe a trained colleague, watch how the activities create 'presses' for social communication — a pause for the child to initiate, an unexpected event, a request for help — and how the examiner keeps them standard while keeping the child engaged. The skill is in the presses, not the materials.",
  "Ask what the session was like for the child: new room, strangers, time of day, medication, anxiety. One hour in a clinic is a small sample; school observation over several settings complements it.",
 ],
 "score": [
  "Coding and the algorithm (Social Affect and Restricted and Repetitive Behaviour domains, with a module-specific classification) are done by the trained examiner. Calibrated severity scores are available for some modules (Gotham et al., 2009) — check the report for what was used.",
  "When quoting a report, quote the author's name, role and date and the narrative observations, not only the classification. If something in the report looks inconsistent, contact the author rather than reinterpreting it.",
 ],
 "interpret": [
  "An ADOS-2 classification is one piece of evidence. Masking, anxiety, a good day, or a very structured examiner can lower scores in a verbally able child — often a girl — while language disorder, severe anxiety, attachment difficulty or low cognitive level can raise them. That is why it is team-used, not stand-alone (tool catalogue).",
  "If the ADOS-2 report and school observations disagree, the difference is information about setting and demand. Raise it with the CDNT keyworker or the diagnostic team in writing, not by contradicting their conclusion in your report.",
  "Translate for the school: each observation becomes a practical adjustment and a Continuum level — visual timetable and explicit transition warnings at Classroom Support; social communication teaching and a key adult at School Support; individual plan, NCSE/SENO involvement or special class consideration at School Support Plus.",
  "Your report says, for example: 'The CDNT assessment (ADOS-2 among other measures) noted…; in school I observed…; this suggests…' It does not restate or revise a diagnosis.",
 ],
 "errors": [
  "Administering or scoring the ADOS-2 without the required training.",
  "Writing 'the ADOS-2 confirmed autism' as if the observation made the diagnosis.",
  "Treating a non-spectrum classification as a rule-out in a masking child.",
  "Quoting the classification and ignoring the narrative observations that actually guide teaching.",
  "Contradicting a team diagnosis in an EP report instead of raising the discrepancy with the team.",
 ],
 "read": [
  "Lord, C., Rutter, M., DiLavore, P. C., Risi, S., Gotham, K., & Bishop, S. L. (2012). Autism Diagnostic Observation Schedule, Second Edition (ADOS-2) manual. Western Psychological Services. — the introduction and the interpretation chapter.",
  "National Institute for Health and Care Excellence. (2011, updated 2017). Autism spectrum disorder in under 19s: Recognition, referral and diagnosis (CG128). NICE.",
  "Gotham, K., Pickles, A., & Lord, C. (2009). Standardizing ADOS scores for a measure of severity in autism spectrum disorders. Journal of Autism and Developmental Disorders, 39(5), 693–705.",
  "Current HSE and PSI guidance on autism assessment in Ireland (Reference Part A cites PSI Autism Guidelines, 2022) — check title and version before citing.",
 ],
},

# ---------------------------------------------------------------- SCQ
{
 "name": "SCQ (Social Communication Questionnaire)",
 "before": [
  "Know where it comes from: the SCQ (Rutter et al., 2003; developed by Berument et al., 1999) is a short parent-completed yes/no questionnaire built from ADI-R items. It is for children aged 4 and over with a mental age above about 2 (tool catalogue). It is a screen — its job is to say 'worth a fuller look' or 'probably not', not to diagnose.",
  "Choose the form. The Lifetime form asks about the child's whole developmental history and is the one used for screening and referral; the Current form asks about the recent period and is more useful for describing present functioning and planning. Check the manual for the exact time frames.",
  "Know its weak spots before you rely on it: it depends on parental recall and knowledge of development; it is less sensitive in younger children and in verbally able children, particularly girls who mask (tool catalogue); and it is parent-report only, so it cannot tell you about school.",
  "Pair it with something from school — observation, teacher consultation, SRS-2 teacher form (Reference Part D, School Age) — and with a developmental history taken in conversation.",
 ],
 "administer": [
  "Explain to the parent what it is for, that it is a questionnaire not a test of the child, and that you will talk it through with them. Offer to read it with them if literacy, language or time is a barrier, and record that you did.",
  "Several items ask about behaviour at a specific earlier age. Parents often struggle with these; tell them to answer as best they can and note which items they were unsure about.",
  "Go through it together afterwards. 'You said yes to this one — can you tell me what that looked like?' turns a tick into history and catches misreadings.",
 ],
 "score": [
  "Score according to the manual — items are scored so that a higher total means more autism-related features, and some items are reverse-keyed. Check the scoring key rather than counting 'yes' answers.",
  "Compare the total with the manual's screening threshold. Check the manual for the figure and its basis before you quote it; do not quote a cut-off from memory in a report.",
 ],
 "interpret": [
  "A score above the threshold means refer for a full assessment — to the CDNT or through the Assessment of Need route, or via the GP — not 'likely autistic'. Say so in those words.",
  "A score below the threshold does not rule out autism, particularly in a verbally able child or a child whose parent has little comparison (tool catalogue; Chandler et al., 2007). If school or parent concern persists, the concern stands.",
  "Consider what else raises SCQ scores: language disorder, intellectual disability, significant anxiety, attachment difficulties and hearing impairment. Name the alternatives you considered in the report.",
  "Use the item content for planning even without a diagnosis — social communication needs described by the parent can go into a School Support plan now, while referral proceeds.",
 ],
 "errors": [
  "Writing 'the SCQ indicates autism'.",
  "Treating a below-threshold score as a rule-out.",
  "Using the Current form for a screening decision that needs the Lifetime form.",
  "Handing the form over without discussing the answers with the parent.",
 ],
 "read": [
  "Rutter, M., Bailey, A., & Lord, C. (2003). The Social Communication Questionnaire manual. Western Psychological Services.",
  "Berument, S. K., Rutter, M., Lord, C., Pickles, A., & Bailey, A. (1999). Autism screening questionnaire: Diagnostic validity. British Journal of Psychiatry, 175(5), 444–451.",
  "Chandler, S., Charman, T., Baird, G., Simonoff, E., Loucas, T., Meldrum, D., Scott, M., & Pickles, A. (2007). Validation of the Social Communication Questionnaire in a population cohort study of autism spectrum disorders. Journal of the American Academy of Child and Adolescent Psychiatry, 46(10), 1324–1332.",
 ],
},

# ---------------------------------------------------------------- Vineland-3
{
 "name": "Vineland-3",
 "before": [
  "Like the ABAS-3, it measures what the person usually does, not what they can do when asked. The Vineland-3 (Sparrow et al., 2016) covers Communication, Daily Living Skills and Socialization, with optional Motor Skills (younger ages — check the manual) and Maladaptive Behavior sections, summarised as an Adaptive Behavior Composite.",
  "Choose the format: the Interview Form (a semi-structured interview with a parent or caregiver), the Parent/Caregiver Form (a rating form) and the Teacher Form, each in comprehensive and shorter domain-level versions. The age range runs from birth into late adulthood (tool catalogue: birth–90; 'Vineland-3 adult' is this entry) but the Teacher Form covers school ages only — check the ranges.",
  "The Interview Form is the Vineland's strength and needs practice: you ask open questions about the area and score the items from what you hear, rather than reading items aloud. Rehearse it with your supervisor before using it with a family.",
  "If intellectual disability is in question you need both an adaptive and a cognitive measure (Reference Part D, School Age; AAIDD definition). In special settings it is often more useful than an IQ score for planning (Reference Part D, Special Setting).",
 ],
 "administer": [
  "For the interview, start broad ('Tell me about how she gets dressed in the morning'), then narrow to the items you still need. Record what the parent said as well as your score — it is the evidence behind the rating.",
  "Keep the distinction between 'can' and 'does' in front of the parent: 'Does he usually do it without being reminded?' A skill done only with prompting scores differently from one done independently; check the scoring rules.",
  "For rating forms, sit with the rater or at least explain the response options, and check for 'don't know' or estimated items before they leave.",
 ],
 "score": [
  "Score with the manual or Q-global. Domain and composite standard scores, subdomain v-scale scores, and age equivalents are available; basal and ceiling rules apply on the comprehensive interview — check them.",
  "Look at subdomains, not just the composite. A flat profile and a spiky one (e.g. strong daily living, weak interpersonal relationships) lead to different plans.",
  "Norms are US; state that in the report.",
 ],
 "interpret": [
  "Compare with the cognitive profile. Adaptive scores well below cognitive may mean lack of opportunity, anxiety or over-support; adaptive above cognitive may mean good scaffolding or an underestimate on the cognitive test.",
  "Watch for adult support suppressing independence — an item 'usually done' may mean usually done by the SNA. Ask who does it.",
  "Home and school ratings often differ; the difference tells you where skills generalise and where they do not.",
  "For young adults and school leavers, use it for transition planning and adult-services referral (tool catalogue 'Vineland-3 adult'): travel, money, self-care and community skills are what the next placement needs to know.",
  "Maladaptive behaviour items are descriptive; they do not diagnose. Use them to prioritise and refer.",
 ],
 "errors": [
  "Reading interview items aloud instead of conducting a semi-structured interview.",
  "Scoring what the child can do in the clinic rather than what they usually do.",
  "Reporting the composite without the subdomain profile.",
  "Using the Vineland alone to suggest intellectual disability.",
  "Missing that 'usually does' means 'an adult does it with him'.",
 ],
 "read": [
  "Sparrow, S. S., Cicchetti, D. V., & Saulnier, C. A. (2016). Vineland Adaptive Behavior Scales, Third Edition (Vineland-3) manual. Pearson. — the interview-technique chapter first.",
  "Tassé, M. J., Schalock, R. L., Balboni, G., Bersani, H., Borthwick-Duffy, S. A., Spreat, S., Thissen, D., Widaman, K. F., & Zhang, D. (2012). The construct of adaptive behavior: Its conceptualization, measurement, and use in the field of intellectual disability. American Journal on Intellectual and Developmental Disabilities, 117(4), 291–303.",
 ],
},

# ---------------------------------------------------------------- TEA-Ch2
{
 "name": "TEA-Ch2",
 "before": [
  "Know what it measures: the Test of Everyday Attention for Children, Second Edition (Manly et al., 2016) is a performance-based battery of attention — sustained, selective and switching attention and related executive control — using game-like tasks. There are junior and older versions by age; check which covers the child (catalogue: 5:0–15:11).",
  "Know what it is not: it measures attention on standardised tasks in a quiet room with an adult present, which is the setting where many children with attentional difficulties do best. It cannot tell you about everyday functioning — pair it with BRIEF-2 or Conners and classroom observation (tool catalogue; Reference Part D, School Age).",
  "Check the kit and equipment before the session: some tasks are timed, some use audio or computer delivery. Test the laptop, audio and response devices; a failed audio track invalidates the task.",
  "Plan the order and breaks. Fatigue affects sustained attention scores directly; do not put it at the end of a long cognitive session.",
 ],
 "administer": [
  "Follow the practice items and scripted instructions exactly. Many tasks depend on the child understanding the rule before the scored trial; the manual says when you may repeat practice.",
  "Observe how the child performs as well as the score: drifting partway through, impulsive responding, self-talk, needing to restart. These are often what makes the result useful to a teacher.",
  "Record anything that interferes — noise, interruptions, the child needing the toilet. On timed attention tasks an interruption is not a minor note.",
 ],
 "score": [
  "Convert raw scores using the manual or scoring software for the child's age; many tasks yield scaled scores and some yield separate speed and accuracy scores. Check which scores the manual recommends interpreting for each task.",
  "Look at speed–accuracy trade-offs; a fast, error-prone child and a slow, accurate child can have similar totals and different needs.",
 ],
 "interpret": [
  "Interpret the pattern across types of attention: difficulty sustaining attention on a dull task is different from difficulty switching between rules, and the recommendations differ (chunked tasks and movement breaks vs explicit transition cues).",
  "Normal-range scores do not rule out attentional difficulty in class — the test setting is structured and one-to-one (Manly et al., 2001 discuss the value and limits of the test context). Weight rater and observation data accordingly.",
  "Consider alternative explanations for low scores: anxiety, fatigue, low mood, language comprehension of instructions, hearing, motivation.",
  "It does not diagnose ADHD. It can describe an attention profile and support a referral to CAMHS or paediatrics, and it can inform School Support level recommendations now (PSI 2.2.2).",
 ],
 "errors": [
  "Concluding 'no attention difficulty' from normal-range test scores despite classroom concern.",
  "Running it at the end of a long session.",
  "Not checking audio or computer equipment before starting.",
  "Presenting TEA-Ch2 findings as evidence for or against ADHD.",
 ],
 "read": [
  "Manly, T., Anderson, V., Crawford, J., George, M., Underbjerg, M., & Robertson, I. H. (2016). Test of Everyday Attention for Children, Second Edition (TEA-Ch2) manual. Pearson.",
  "Manly, T., Anderson, V., Nimmo-Smith, I., Turner, A., Watson, P., & Robertson, I. H. (2001). The differential assessment of children's attention: The Test of Everyday Attention for Children (TEA-Ch), normative sample and ADHD performance. Journal of Child Psychology and Psychiatry, 42(8), 1065–1081.",
 ],
},

# ---------------------------------------------------------------- Leiter-3
{
 "name": "Leiter-3",
 "before": [
  "Know why you would choose it. The Leiter-3 (Roid et al., 2013) assesses non-verbal cognitive ability and attention/memory with instructions given by gesture and demonstration, not speech. It is the option when language disorder, hearing impairment, autism with limited speech or very recent arrival with EAL would make a verbal battery invalid (tool catalogue; Reference Part D, Special Setting).",
  "Know what it cannot tell you: verbal reasoning, which for many children is the area of concern. Use it alongside other information, not instead of understanding the child's language (tool catalogue).",
  "Practise the gestural administration until it is natural. Pantomimed instruction is a skill; awkward or inconsistent gestures are a source of error the norms do not account for.",
  "Norms are US. For children with EAL, a non-verbal test reduces but does not remove cultural loading — familiarity with test materials and the idea of timed puzzles also differ. Record the child's language and schooling history (Cummins, 2000).",
 ],
 "administer": [
  "Keep speech to the minimum the manual allows. If you start explaining in words, you have changed the test; note any verbal support you gave.",
  "Watch how the child approaches the tasks — trial and error vs planning, attention to detail, response to getting items wrong. This is especially informative when you cannot rely on talk.",
  "Check the rules for each subtest (start, stop and timing) in the manual before the session. Some attention and memory subtests have specific timing requirements.",
 ],
 "score": [
  "Score with the manual or scoring software: subtest scaled scores and a Nonverbal IQ, plus attention/memory composites if those subtests were given. Check which subtests feed which composite.",
  "Report confidence intervals and percentiles, and state that the score is a non-verbal estimate.",
 ],
 "interpret": [
  "Report it for what it is: 'non-verbal reasoning, measured without spoken instructions'. Do not present a Nonverbal IQ as a general IQ.",
  "Where the Leiter-3 is in the average range and language is weak, the finding is important: it points toward a language-specific need and toward SLT, not toward a general learning difficulty.",
  "Where it is low, consider attention, motivation, visual processing and unfamiliarity with the task before concluding low ability. Intellectual disability needs an adaptive measure too (Reference Part D).",
  "In a special setting, link findings to the curriculum the child is following (L1LP/L2LP) rather than to mainstream norms.",
 ],
 "errors": [
  "Reporting the Nonverbal IQ as if it were a full-scale IQ.",
  "Giving spoken explanations and not recording it.",
  "Choosing it for an EAL pupil without recording language and schooling history.",
  "Concluding intellectual disability from a non-verbal score alone.",
 ],
 "read": [
  "Roid, G. H., Miller, L. J., Pomplun, M., & Koch, C. (2013). Leiter International Performance Scale, Third Edition (Leiter-3) manual. Stoelting.",
  "Cummins, J. (2000). Language, power and pedagogy: Bilingual children in the crossfire. Multilingual Matters.",
 ],
},

# ---------------------------------------------------------------- WNV
{
 "name": "WNV (Wechsler Non-Verbal)",
 "before": [
  "Know the instrument: the Wechsler Nonverbal Scale of Ability (Wechsler & Naglieri, 2006) for ages 4:0–21:11 uses pictorial directions and brief standard instructions, with minimal language demand (tool catalogue). Subtests differ between the younger and older age batteries, and there are shorter and longer versions — check the manual for which subtests each uses.",
  "Choose it for a reason and write the reason in the report: EAL, language disorder, hearing impairment or a child for whom a verbal battery would measure language rather than reasoning (tool catalogue: 'state why a non-verbal measure was chosen').",
  "Check the norms and instruction languages your kit supports. The WNV was designed with translated instructions for several languages; check whether the child's language is among them and whether an interpreter is needed.",
  "Like any non-verbal measure, it cannot tell you about verbal reasoning (tool catalogue).",
 ],
 "administer": [
  "Use the pictorial directions as designed and the standard verbal instructions only as the manual permits. Practise the pictorial demonstrations beforehand; they should be as fluent as a spoken script.",
  "Some subtests are timed and some involve memory; follow the timing and discontinue rules exactly.",
  "Observe the child's approach and record it: planning, persistence, response to difficulty, use of trial and error.",
 ],
 "score": [
  "Convert raw scores using the manual for the child's age. The WNV yields T-scores for subtests and a full-scale score; check the manual for the score metrics and which subtests feed it.",
  "Report the full-scale score with its confidence interval and percentile, and describe the subtests in plain language.",
 ],
 "interpret": [
  "Frame the result as non-verbal ability. It is not a full picture of cognitive ability and should not be presented as one.",
  "Put it beside what you know about language: an average WNV with weak English or weak language may point to EAL or DLD rather than a general learning difficulty; seek SLT and EAL information before drawing conclusions (Cummins, 2000).",
  "Consider the child's educational history, culture and familiarity with tests; non-verbal does not mean culture-free.",
  "Recommendations should build on the strength — visual supports, modelling and demonstration — at the right Continuum level.",
 ],
 "errors": [
  "Not stating why a non-verbal measure was used.",
  "Describing the result as the child's IQ.",
  "Using English instructions with a child who needed the translated or pictorial version.",
  "Concluding general learning difficulty without language and schooling history.",
 ],
 "read": [
  "Wechsler, D., & Naglieri, J. A. (2006). Wechsler Nonverbal Scale of Ability (WNV) administration and scoring manual, and technical and interpretive manual. Harcourt Assessment / Pearson.",
  "Cummins, J. (2000). Language, power and pedagogy: Bilingual children in the crossfire. Multilingual Matters.",
 ],
},

# ---------------------------------------------------------------- BAS-3
{
 "name": "BAS-3",
 "before": [
  "Know the instrument: the British Ability Scales, Third Edition (Elliott & Smith, 2011, GL Assessment) is a UK-normed cognitive battery for 3:0–17:11 with an Early Years battery and a School Age battery. Core scales give a General Conceptual Ability (GCA) and cluster scores; diagnostic scales assess memory, processing speed and related skills; and there are attainment scales. Check the manual for which subtests belong to each cluster and battery.",
  "Check which edition and norms your service holds (tool catalogue). Some services still hold BAS-II kits; do not mix record forms or norm tables across editions.",
  "Choose it for a reason. The BAS-3's UK norms and flexible item sets are useful for younger children and for children who find a long Wechsler battery hard; write why you chose it over WISC-V UK or WPPSI-IV UK.",
  "As with any cognitive battery, rule out vision, hearing, language and emotional confounds first and write the referral question down.",
 ],
 "administer": [
  "The BAS-3 uses item sets with decision points rather than simple start and stop rules: the child is given a block of items suited to their level, and you decide whether to continue, stop or go back based on the number passed. Learn the decision rules for each subtest before the session.",
  "Follow the scripted instructions and teaching items exactly; record responses verbatim where required.",
  "Record behaviour as you go — approach, persistence, language, attention — just as you would for WISC-V.",
 ],
 "score": [
  "Raw scores convert to ability scores (because different item sets are given to different children) and then to T-scores and standard scores. Check the conversion steps in the manual; this is where scoring errors happen.",
  "Report GCA and cluster scores with confidence intervals and percentiles; check whether differences between clusters are statistically significant and unusual using the manual's tables.",
 ],
 "interpret": [
  "Interpret clusters and subtest patterns with the same caution as any battery — a GCA can hide very different profiles (Watkins, 2000 on profile analysis).",
  "Use the attainment scales for a quick check, but for a full literacy or numeracy picture you need a dedicated attainment test (e.g. WIAT-III UK).",
  "Link findings to classroom demands and recommendations at the right Continuum level: e.g. a weak memory or processing-speed cluster becomes chunked instructions, written backup and extra time at Classroom Support, and a targeted plan at School Support.",
  "State the edition and norms used, and any adaptations. UK norms are closer than US norms to Irish pupils but are not Irish norms; say so.",
 ],
 "errors": [
  "Misapplying the item-set decision rules.",
  "Converting raw scores straight to T-scores without the ability-score step.",
  "Mixing BAS-II and BAS-3 materials or norms.",
  "Reporting a GCA when clusters differ significantly without comment.",
 ],
 "read": [
  "Elliott, C. D., & Smith, P. (2011). British Ability Scales, Third Edition (BAS3) administration and scoring manual, and technical manual. GL Assessment.",
  "Watkins, M. W. (2000). Cognitive profile analysis: A shared professional myth. School Psychology Quarterly, 15(4), 465–479.",
 ],
},

# ---------------------------------------------------------------- Beery VMI
{
 "name": "Beery VMI",
 "before": [
  "Know what it measures: the Beery-Buktenica Developmental Test of Visual-Motor Integration (Beery et al., 2010) asks the child to copy a sequence of increasingly complex geometric forms. It measures the integration of visual perception and fine motor control — relevant to handwriting and copying (Reference Part D, DCD and handwriting).",
  "Know what it cannot tell you alone: whether a low score is visual, motor or integrative. For that you need the supplementary Visual Perception and Motor Coordination tests (tool catalogue).",
  "Check the edition and form (full form vs shorter form for younger children) and the norms; the age range extends from early childhood into adulthood (tool catalogue: 2:0–100).",
  "It is often used by OTs; where an OT is involved, coordinate so the child is not tested twice.",
 ],
 "administer": [
  "Follow the manual: the child copies each form in the booklet without erasing or rotating the booklet; stop according to the discontinue rule. Check the rules before the session.",
  "Observe grip, posture, pressure, speed and hand dominance — often as informative as the score for OT referral and classroom advice.",
  "Give the supplementary tests in the order and conditions the manual specifies if you need to separate visual from motor difficulty.",
 ],
 "score": [
  "Score each copied form against the manual's specific criteria; do not score by impression. Scoring the forms is where trainee error is common — have your first protocols checked.",
  "Convert to standard scores and percentiles for the child's age using the manual.",
 ],
 "interpret": [
  "A low VMI with a normal Visual Perception score points toward motor involvement; the reverse points toward perception. Both low suggests broader difficulty — interpret with care and in context.",
  "Link to classroom demands: copying from the board, handwriting speed (DASH), worksheet layout. Recommendations include reducing copying, providing notes, and access to keyboarding, with RACE applications where relevant at post-primary.",
  "It does not diagnose DCD. That is made by OT/paediatrics with motor assessment (e.g. Movement ABC-2) and history (DCD-Q). You describe and refer.",
  "Consider vision (ophthalmology check) and attention before concluding a visual-motor difficulty.",
 ],
 "errors": [
  "Scoring forms by impression rather than the criteria.",
  "Reporting a low VMI as a diagnosis of DCD.",
  "Not giving the supplementary tests when the question is visual vs motor.",
  "Ignoring vision as a possible factor.",
 ],
 "read": [
  "Beery, K. E., Buktenica, N. A., & Beery, N. A. (2010). The Beery-Buktenica Developmental Test of Visual-Motor Integration (6th ed.) manual. Pearson.",
  "Feder, K. P., & Majnemer, A. (2007). Handwriting development, competency, and intervention. Developmental Medicine and Child Neurology, 49(4), 312–317.",
 ],
},
]
