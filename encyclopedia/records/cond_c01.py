# CONDS records: DLD, DCD, Generalised Anxiety Disorder.
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c01.py

CONDS = [

# =====================================================================================
# 1. DEVELOPMENTAL LANGUAGE DISORDER
# =====================================================================================
{
 "name": "Developmental Language Disorder (DLD)",
 "code": "DSM-5-TR Language Disorder (F80.2) · ICD-11 6A01.2 Developmental language disorder — check sub-codes before quoting",
 "neps": "1. LEARNING (1.2 Language skills)",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "A persistent difficulty LEARNING and USING language — understanding (receptive), expressing (expressive) or both — that has a significant impact on everyday social interaction or educational progress, and is NOT associated with a known biomedical condition (Bishop et al., 2017, CATALISE-2).",
  "DLD is the agreed umbrella term from the CATALISE Delphi consensus (Bishop et al., 2016, 2017). It replaced 'specific language impairment (SLI)', 'language delay' and several local terms. The DSM-5-TR label is Language Disorder (APA, 2022); ICD-11 uses 'developmental language disorder' (WHO, 2019).",
  "CATALISE separates three groups — this is the distinction you must hold:\n▸ DLD — language disorder with no known associated biomedical condition.\n▸ LANGUAGE DISORDER ASSOCIATED WITH X — where X is e.g. autism, intellectual disability, sensorineural hearing loss, cerebral palsy, a genetic syndrome or brain injury.\n▸ LANGUAGE DIFFERENCE — e.g. English as an Additional Language (EAL), or a dialect. Not a disorder.",
  "A low non-verbal IQ does NOT rule out DLD. CATALISE dropped the requirement for a discrepancy between verbal and non-verbal ability; a child with non-verbal scores in the low-average range can have DLD. Only intellectual disability moves it to 'language disorder associated with ID' (Bishop et al., 2017).",
  "It affects one or more of: phonology, grammar (morphosyntax), vocabulary and word meaning (semantics), word finding, discourse and narrative, pragmatics, verbal learning and memory. The profile changes with age, so a child's 'type' at 5 is not their type at 12.",
  "It is LIFELONG in most cases. CATALISE flags that language problems that persist past about age 5 are likely to continue into adulthood (Bishop et al., 2016). Surface grammar may improve; comprehension of complex language, vocabulary depth and narrative commonly remain weak.",
  "Risk factors (e.g. family history, male sex, low parental education) and co-occurring difficulties (ADHD, DCD, dyslexia, speech sound disorder) do NOT exclude DLD — CATALISE lists them separately from the exclusionary 'associated with X' conditions.",
 ],

 "what_it_is_not": [
  "NOT the same as EAL. A child learning English will have a smaller English vocabulary and make grammatical errors for years — that is typical second-language learning. DLD in a bilingual child shows in ALL their languages, including the home language, and in how quickly they learn new words when taught (Bishop et al., 2017). Get a home-language history before anything else.",
  "NOT 'late talking' in a toddler. Many late talkers catch up; DLD is identified when difficulties persist and impact function. CATALISE advises caution about firm identification before about age 5 unless difficulties are severe or broad (Bishop et al., 2016) — check the paper's exact wording before quoting.",
  "NOT a behaviour problem or poor listening. Many children with DLD are first referred for behaviour or attention. Not following an instruction you did not understand looks identical to not complying.",
  "NOT ruled out because the child 'talks all the time'. Fluent, chatty speech can sit over weak comprehension, weak grammar or weak narrative. Receptive difficulty is the most often missed part and carries the worse prognosis.",
  "NOT a speech (articulation) problem. Speech sound disorder concerns producing sounds; DLD concerns language. They can co-occur but are separate.",
  "NOT 'caused by' parents not talking to the child. Environment affects vocabulary; DLD is strongly heritable and occurs in language-rich homes. Say this clearly — parents often carry blame.",
  "NOT something the EP diagnoses. Identification of DLD sits with the SLT (usually with multidisciplinary input). The EP describes the language demand, the classroom impact and the cognitive and attainment profile, and refers.",
 ],

 "prevalence": [
  "OVERALL: about 7% of children at school entry. Norbury et al. (2016), a population study of reception-class children in Surrey (SCALES), estimated DLD at 7.58%, with a further 2.34% having language disorder associated with another condition. In plain terms: roughly two children in a class of 30.",
  "EARLIER ESTIMATE: Tomblin et al. (1997) found around 7.4% of US kindergarten children met criteria for specific language impairment — and most parents had not been told their child had a language difficulty. Under-identification is the norm.",
  "IRELAND: no Irish population prevalence study is cited here — check before quoting. HSE SLT caseload and Department language-class figures reflect identification and service capacity, not prevalence.",
  "EARLY YEARS 0–5: late talking is common and many resolve; firm identification is usually made from about 4–5 onwards.",
  "SCHOOL AGE 6–12: many children with DLD reach school age unidentified and are referred for behaviour, attention or literacy instead.",
  "ADOLESCENT 13–16: often hidden — surface speech sounds typical; difficulties show in subject vocabulary, inference, written expression and social talk.",
  "SEX RATIO: more boys are identified; Norbury et al. (2016) reported a smaller male excess in a population sample than clinic samples suggest. Exact ratio not stated here — check before quoting.",
 ],

 "cooccurring": [
  {"name": "DYSLEXIA / SPECIFIC LEARNING DIFFICULTY",
   "rate": "substantial overlap — rate not stated here, check (see Snowling & Hulme, 2012)",
   "presents": "PRESENTS AS: decoding difficulty plus weak reading comprehension. A child who decodes accurately but cannot answer questions has an oral language problem, not a decoding one. Assess both oral language and word reading."},
  {"name": "ADHD",
   "rate": "elevated — rate not stated here, check",
   "presents": "PRESENTS AS: not following instructions and drifting in whole-class talk. Separate comprehension from attention: does the child follow the SAME instruction when it is short, visual and given one-to-one?"},
  {"name": "DCD",
   "rate": "elevated — rate not stated here, check",
   "presents": "PRESENTS AS: slow, effortful written output on top of weak sentence construction. Written expression then collapses from two directions at once."},
  {"name": "SPEECH SOUND DISORDER",
   "rate": "common co-occurrence — rate not stated here, check",
   "presents": "PRESENTS AS: unintelligible speech that draws attention away from the language difficulty underneath. When speech clears, the language problem is often still there."},
  {"name": "SOCIAL, EMOTIONAL AND BEHAVIOURAL DIFFICULTY",
   "rate": "elevated in adolescence (Conti-Ramsden & Botting, 2008) — rate not stated here, check",
   "presents": "PRESENTS AS: frustration, withdrawal, peer difficulty or 'defiance'. Behaviour referrals with unidentified language need are common. Always screen language in a behaviour referral."},
  {"name": "ANXIETY",
   "rate": "elevated — rate not stated here, check",
   "presents": "PRESENTS AS: avoidance of oral work, freezing when asked a question, school reluctance. Often secondary to repeatedly not understanding and being unable to explain."},
  {"name": "AUTISM (as differential, not co-occurrence in CATALISE terms)",
   "rate": "language disorder in autism is 'language disorder associated with autism' (Bishop et al., 2017)",
   "presents": "PRESENTS AS: structural language difficulty plus social-communication difference. Pragmatic difficulty alone does not make it autism, and structural language difficulty alone does not make it DLD. Refer for multidisciplinary assessment."},
 ],

 "recommendations": [
  "NAME THE LANGUAGE DEMAND, not just the deficit. 'Instructions longer than two key words are lost' is actionable; 'receptive language difficulties' is not.",
  "REDUCE AND CHUNK VERBAL INPUT: short sentences, one instruction at a time, key words stressed, pause, then check understanding by asking the child to SHOW or DO, not 'do you understand?'",
  "VISUAL SUPPORT FOR ALL VERBAL INFORMATION: visual timetable, written or pictured steps on the desk, graphic organisers, modelled examples. Visuals stay; speech disappears.",
  "PRE-TEACH SUBJECT VOCABULARY. Specify: 3–5 key words per topic, taught before the lesson, with meaning, sound structure, use in a sentence and revisited across the week. Ebbels et al. (2019) set out universal, targeted and specialist tiers of language support; do not claim vocabulary teaching has 'the strongest' evidence without checking the source.",
  "SUPPORT NARRATIVE AND WRITTEN EXPRESSION with story frames, sentence starters and oral rehearsal before writing.",
  "ADAPT THE CLASSROOM LANGUAGE ENVIRONMENT, not only the child. The Communication Supporting Classrooms Observation Tool (Dockrell et al., 2015) gives a structured way to feed this back to the teacher.",
  "TAKE SLT TARGETS INTO THE CLASSROOM. Ask for the SLT report and embed its targets in the Student Support Plan, with named person, frequency and review date.",
  "ASSESS COGNITION WITH LANGUAGE LOAD IN MIND. Report verbal and non-verbal indices separately and say why; a Full Scale score that averages across a language disorder misrepresents the child. Consider WNV or Leiter-3 where language would invalidate a verbal battery.",
  "CONTINUUM LEVEL: Classroom Support for differentiation; School Support for targeted vocabulary and language work; School Support Plus where SLT is involved. A Department language class (special class) is an option for some children — check current NCSE / Department eligibility criteria and local availability.",
  "REFER: SLT via HSE Primary Care (mild–moderate, single-need) or CDNT (complex, multiple needs) — check local route. AUDIOLOGY first if hearing has not been checked recently.",
  "DO NOT recommend 'more reading' or a general 'listening programme' as the intervention for a language disorder, and do not report a Full Scale IQ without comment when the verbal index is depressed by language.",
 ],

 "explain_parent": [
  "'Developmental Language Disorder means his brain finds it harder to learn and use language — understanding what's said, finding the words, and putting sentences together. It isn't about how clever he is, and it isn't about his hearing.'",
  "'It's common — about two children in every class of thirty — but it's often missed, because children with DLD can chat away quite happily while not following much of what's said to them.'",
  "'It isn't caused by anything you did or didn't do. It runs in families, and it happens in homes full of talk and books.'",
  "'If you speak another language at home, keep speaking it. Strong home language helps English. We'd only think about DLD if the difficulty is there in both languages.'",
  "'It's usually lifelong, but children learn a great deal with the right support. What makes the biggest difference is the adults around him changing how they talk — shorter sentences, showing as well as telling, teaching new words on purpose.'",
  "SIGNPOST: the child's SLT; RADLD (Raising Awareness of DLD) information for families → https://radld.org/ ; the HSE Primary Care SLT or CDNT route.",
 ],

 "explain_teacher": [
  "'This is a language-learning difficulty, not a listening or behaviour problem. When she doesn't do what you asked, the first hypothesis is that she didn't understand it.'",
  "'Check understanding by asking her to show you or tell you back in her own words. Yes-or-no to \"do you understand?\" tells you nothing — most children with DLD will say yes.'",
  "'One instruction at a time, key words stressed, and back it up visually. What you say disappears; what's on the desk stays.'",
  "'Pre-teach the vocabulary. Three to five key words before the topic starts, with the meaning, how it sounds and a sentence. She'll learn more from the lesson if the words aren't new on the day.'",
  "'Let her rehearse aloud before writing, and give her a sentence starter or a frame. Oral language is the foundation of written language — if she can't say it, she can't write it.'",
  "'Watch the chatty ones. Fluent social talk hides weak comprehension. Test the classroom language, not the playground language.'",
 ],

 "explain_child": [
  "YOUNGER: 'Some people's brains find words tricky — understanding them, remembering them or finding the right one. It's called DLD. It doesn't mean you're not clever. It means you need people to say things a bit slower and show you as well.'",
  "OLDER: 'DLD means your brain learns and uses language differently. You might lose track when people talk a lot, or know what you want to say but not find the words. Lots of people have it. Knowing about it means you can ask for what helps.'",
  "TEACH A SELF-ADVOCACY SENTENCE: 'Can you say that again in a different way?' or 'Can you show me?' Practise it with them — children with DLD often do not know that not understanding is something they are allowed to say.",
  "ASK: 'When is it hardest to understand what the teacher says?' and 'What helps?' — use pictures or a scale if the child's expressive language is limited.",
  "CHECK YOUR OWN LANGUAGE: short sentences, concrete words, visual support, extra wait time. If the child cannot follow your explanation of DLD, you have demonstrated it rather than explained it.",
 ],

 "analogies": [
  "THE RADIO WITH A WEAK SIGNAL: 'He's hearing the words fine — it's that the meaning comes through crackly, and when people talk fast or for a long time, whole bits drop out.' Good with parents and teachers; separates hearing from understanding.",
  "THE WORD WAREHOUSE: 'Everyone stores words in a warehouse. Hers has plenty in it, but they're filed badly, so finding the right one quickly is hard — that's why she says \"the thingy\".' Good for word-finding; works with children from about 8.",
  "LIVING ABROAD WITH SCHOOL-LEVEL FRENCH: 'You can get by in the shop, but in a fast meeting you catch half and nod along.' Good with teachers and adolescents — explains masking and exhaustion.",
  "THE BUILDING WITHOUT SCAFFOLDING: 'Language is the scaffolding every other subject is built on. Without it, reading, maths word problems and history all wobble.' Good for explaining why DLD shows up everywhere.",
 ],

 "language": [
  "'Developmental Language Disorder (DLD)' is the agreed term following CATALISE (Bishop et al., 2017) and is used by RADLD and increasingly by SLT services. Use it in reports alongside any term already on file.",
  "Older reports may say 'specific language impairment (SLI)', 'specific speech and language disorder (SSLD)', 'language delay' or 'receptive/expressive language disorder'. The Irish special-class system has used 'SSLD' — check current Department / NCSE terminology before writing it.",
  "Avoid 'language delay' for a school-age child with persistent difficulty — 'delay' implies catching up, which is misleading.",
  "Avoid 'poor listener', 'doesn't pay attention' or 'lazy with language' in reports. These are interpretations, and PSI 1.2.8 requires opinion to be labelled as such.",
  "Describe what the child CAN do and under what conditions — 'follows two-step instructions with visual support' — rather than only deficits.",
 ],

 "red_flags": [
  "RED FLAG — LOSS of language skills the child previously had (regression). Not DLD. Medical referral via GP / paediatrics without delay.",
  "RED FLAG — hearing never checked, or history of recurrent ear infections / glue ear. Audiology before any language conclusion.",
  "RED FLAG — an adolescent with unidentified DLD in a behaviour, exclusion or youth justice context. Language difficulties are over-represented in these groups (Bryan et al., 2007 — rate not quoted here, check). Screen language before accepting a behavioural formulation.",
  "RED FLAG — disclosure or suspected abuse from a child with limited language. Children with communication difficulties are more vulnerable and less able to disclose. Follow Children First procedures the same day: report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty; supervision follows the action. Do not wait for clearer language.",
  "BOUNDARY — you do not diagnose DLD; the SLT does. You describe language demand and impact, assess cognition and attainment with the language load stated, and refer. PSI 2.2.2.",
  "WATCH — EAL. Do not use English-normed language tests to infer disorder in a child learning English. Use home-language history, dynamic assessment and an interpreter (NEPS interpreter request route — check current process).",
 ],

 "child_voice": [
  "TALKING MATS — visual framework where the child places picture symbols under 'like / not sure / don't like'. Good because it reduces the expressive-language demand of giving a view, which is exactly what DLD makes hard. → https://www.talkingmats.com/",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — Irish, free, already in schools. Read it aloud and simplify wording if needed; good because staff recognise it. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "SCALING WITH A DRAWN LADDER OR FACES — good because it needs a point, not a sentence, and gives you a follow-up ('what makes it a 3?') you can scaffold.",
  "DRAWING AND TALK ('draw a lesson that's hard / easy') — good because the drawing holds the topic while the child searches for words, and it locates the difficulty in a setting.",
  "OBSERVATION OF THE CHILD IN CLASS TALK — good because the child's voice is also what they cannot say; noting where they go silent is data.",
 ],

 "questions": [
  "Q: 'But he talks all the time — how can he have a language disorder?' — A: 'Talking a lot and understanding complex language are different skills. Chatty social talk can sit on top of real difficulty understanding instructions, finding precise words or following a story. It's the classroom language we're looking at.'",
  "Q: 'Is it because we speak Polish at home?' — A: 'No. Learning two languages doesn't cause DLD. Keep using your home language. We'd only think about DLD if the difficulty shows up in Polish too — so what you tell me about how he talks at home is really important.'",
  "Q: 'Will she grow out of it?' — A: 'For most children DLD is long-term. What changes is how well it's supported — with the right help she'll keep making progress, and the adults around her adjusting how they talk makes a big difference.'",
  "Q: 'Is it the same as dyslexia?' — A: 'They're related but different. Dyslexia is mainly about the sounds in words for reading and spelling. DLD is about language more broadly — understanding, vocabulary, sentences. A child can have one, the other, or both, and they often overlap.'",
  "Q: 'Why can't you diagnose it?' — A: 'Identifying DLD is the speech and language therapist's job, because it needs specialist language assessment. What I can do is describe how language is affecting her learning, make sure her cognitive scores are read correctly, and refer.'",
  "Q: 'Her IQ report says she's low average — does that mean it's not DLD?' — A: 'Not necessarily. The consensus definition doesn't require a gap between verbal and non-verbal ability any more. And verbal scores can be pulled down by the language difficulty itself, so the numbers have to be read with that in mind.'",
  "Q: 'Should he go to a language class?' — A: 'It's one option for some children. Places are allocated against criteria and depend on what's available locally, so I can't promise one. What matters first is that the SLT has assessed him, and that whatever setting he's in adapts its language.'",
 ],

 "supervision": [
  "Bring a behaviour or attention referral where you now suspect a language difficulty underneath, and ask how your supervisor would raise that with the school without appearing to dismiss their concern.",
  "Ask about the local SLT route — Primary Care versus CDNT, waiting times, and whether the service accepts EP referrals directly.",
  "Discuss how to report a WISC-V where the VCI is depressed: what to say, what not to calculate, and when to use a non-verbal measure instead.",
  "Bring an EAL case and ask how the service distinguishes language difference from disorder, including use of interpreters.",
  "Ask how language classes are allocated in this region and what evidence the NCSE / Department process currently asks for.",
 ],

 "reflection": [
  "ON HOW I EXPLAINED IT — Did I explain DLD in language the parent (and the child) could follow? If I used 'receptive' and 'expressive' without unpacking them, I modelled the problem.",
  "ON EAL — Did I get a proper home-language history before interpreting English scores? Or did I note 'EAL' in the background section and then read the scores as if it were not there?",
  "ON THE BEHAVIOUR REFERRAL — When the school described defiance, did I ask whether the child understood the instruction? Did I test it?",
  "ON COGNITIVE SCORES — Did I report a Full Scale score that averaged across a language disorder, or did I explain the split and what it means?",
  "ON THE CHILD'S VOICE — Did I adapt my own questions for a child with language difficulty, or did I ask open questions and write 'the child had little to say'?",
  "WHAT GOOD LOOKS LIKE: 'The referral was about behaviour in maths. I asked the teacher to repeat her usual instruction word for word — it was four steps long with two embedded clauses. We rewrote it as two visual steps and the behaviour dropped within a week. That was the formulation.'",
  "WHAT POOR LOOKS LIKE: 'Verbal comprehension was in the low range, consistent with his general ability.' — no consideration of language disorder, no SLT referral, no classroom language recommendations.",
 ],

 "citations": [
  "Bishop, D. V. M., Snowling, M. J., Thompson, P. A., Greenhalgh, T., & CATALISE consortium. (2016). CATALISE: A multinational and multidisciplinary Delphi consensus study. Identifying language impairments in children. PLOS ONE, 11(7), e0158753.",
  "Bishop, D. V. M., Snowling, M. J., Thompson, P. A., Greenhalgh, T., & CATALISE-2 consortium. (2017). Phase 2 of CATALISE: A multinational and multidisciplinary Delphi consensus study of problems with language development: Terminology. Journal of Child Psychology and Psychiatry, 58(10), 1068–1080.",
  "Norbury, C. F., Gooch, D., Wray, C., Baird, G., Charman, T., Simonoff, E., Vamvakas, G., & Pickles, A. (2016). The impact of nonverbal ability on prevalence and clinical presentation of language disorder: Evidence from a population study. Journal of Child Psychology and Psychiatry, 57(11), 1247–1257.",
  "Tomblin, J. B., Records, N. L., Buckwalter, P., Zhang, X., Smith, E., & O'Brien, M. (1997). Prevalence of specific language impairment in kindergarten children. Journal of Speech, Language, and Hearing Research, 40(6), 1245–1260.",
  "Ebbels, S. H., McCartney, E., Slonims, V., Dockrell, J. E., & Norbury, C. F. (2019). Evidence-based pathways to intervention for children with language disorders. International Journal of Language & Communication Disorders, 54(1), 3–19.",
  "Conti-Ramsden, G., & Botting, N. (2008). Emotional health in adolescents with and without a history of specific language impairment (SLI). Journal of Child Psychology and Psychiatry, 49(5), 516–525.",
  "Dockrell, J. E., Bakopoulou, I., Law, J., Spencer, S., & Lindsay, G. (2015). Capturing communication supporting classrooms: The development of a tool and feasibility study. Child Language Teaching and Therapy, 31(3), 271–286.",
  "Bryan, K., Freer, J., & Furlong, C. (2007). Language and communication difficulties in juvenile offenders. International Journal of Language & Communication Disorders, 42(5), 505–520.",
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Language Disorder.",
  "World Health Organization. (2019). International classification of diseases (11th rev.) — 6A01.2 Developmental language disorder.",
 ],

 "pathway": {
  "age": "Concerns often start at 2–3 (late talking), but firm identification is usually from about 4–5, once transient late talking has been separated from persistent difficulty (Bishop et al., 2016). Many children are not identified until school, when curriculum language — instructions, narrative, subject vocabulary — exposes the difficulty. Receptive-only and 'chatty' presentations are identified later, sometimes not until post-primary.",
  "who_diagnoses": "Ireland: a Speech and Language Therapist — HSE Primary Care SLT for mild–moderate single-need presentations; CDNT where needs are complex or multiple. Assessment of Need (Disability Act 2005) may route through either. Private SLT reports are common. Check local routes — they vary by CHO.",
  "who_wrote_report": "HSE Primary Care SLT; CDNT SLT (often within a multidisciplinary report); private SLT; older reports from language-class or early-intervention teams. An EP report may describe language difficulty but should not be the source of a DLD diagnosis.",
  "refer_to": "SLT via Primary Care or CDNT (check local criteria). Audiology via GP / Primary Care if hearing not recently checked. CDNT where autism, ID or motor difficulties also suspected. GP / paediatrics urgently for any language regression.",
  "sooner": "'Language difficulties are one of the most commonly missed needs, because children can seem to talk well while not understanding much. Many parents are never told. You're here now, and support at any age makes a difference.'",
 },

 "differential": [
  "EAL / LANGUAGE DIFFERENCE — check home-language development and exposure; disorder shows in all languages.",
  "HEARING LOSS (including fluctuating glue ear) — audiology first; if sensorineural, it is 'language disorder associated with hearing loss'.",
  "AUTISM — social-communication difference plus restricted/repetitive behaviour; language disorder would be 'associated with autism'. Refer to CDNT.",
  "INTELLECTUAL DISABILITY / GLD — global rather than language-specific difficulty; adaptive functioning also affected. Use a non-verbal measure and adaptive measure.",
  "LIMITED LANGUAGE EXPOSURE / DISADVANTAGE — smaller vocabulary but typical learning rate when taught; dynamic assessment helps separate this.",
  "SELECTIVE MUTISM — speaks fluently at home, not in school; an anxiety presentation, not a language disorder, though the two can co-occur.",
 ],

 "next": [
  "Check hearing history and date of last audiology; request if not recent.",
  "Get a home-language history and the SLT report if one exists; read its targets.",
  "Observe the child in whole-class instruction and note the length and complexity of instructions given.",
  "Write classroom language recommendations with named adult, frequency and review date, at the right Continuum level.",
  "Refer to SLT (Primary Care or CDNT) with specific examples of classroom impact.",
 ],

 "presentations": [
  "Following multi-step verbal instructions",
  "Word-finding difficulty",
  "Narrative and sequencing in spoken account",
  "Vocabulary gap from limited exposure",
  "Participation in oral work and classroom talk",
  "English as an Additional Language (EAL)",
  "Bilingual language development",
  "Interpreter need and how it changes the assessment",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — concerns usually first raised here; firm identification from about 4–5",
   "prevalence": "Norbury et al. (2016): about 7.6% at school entry (reception class, England).",
   "see": "Late first words and phrases, short or telegraphic sentences, difficulty following routines by language alone, frustration and tantrums when not understood. Many late talkers catch up, so describe rather than label, and monitor. Always establish home-language exposure and hearing history first.",
   "tools": ["Preschool Language Scales-5 (PLS-5)", "BPVS-3", "Renfrew Action Picture Test", "Ages & Stages Questionnaires (ASQ-3)"],
  },
  "School Age": {
   "applies": "YES — main window for identification in school",
   "prevalence": "About 7% (Norbury et al., 2016; Tomblin et al., 1997); many still unidentified.",
   "see": "Not following instructions, off-task in whole-class talk, weak narrative, limited vocabulary, difficulty with reading comprehension despite decoding. Often referred for behaviour, attention or literacy rather than language. Verbal comprehension scores lower than visual-spatial or fluid reasoning.",
   "tools": ["CELF-5 UK", "BPVS-3", "Renfrew Action Picture Test", "WISC-V UK", "WNV (Wechsler Non-Verbal)", "YARC (York Assessment of Reading for Comprehension)"],
  },
  "Adolescent": {
   "applies": "YES — often hidden; identified through subject demands or behaviour",
   "prevalence": "Persists from childhood in most cases; adolescent rate not stated here — check.",
   "see": "Surface speech sounds typical; difficulty with subject-specific vocabulary, inference, figurative language and extended writing. Withdrawal, anxiety or conflict in social talk; possible exclusion or behaviour referrals. RACE and subject choice become the practical questions.",
   "tools": ["CELF-5 UK", "WISC-V UK", "WIAT-III UK", "YARC (York Assessment of Reading for Comprehension)", "Access arrangements evidence (RACE)"],
  },
  "Young Adult": {
   "applies": "YES — lifelong; relevant to further education, DSA and workplace",
   "prevalence": "Adult rate not stated here — check. Persistence is the expected outcome.",
   "see": "Difficulty with dense course reading, lectures, written assignments and workplace communication; may never have been identified. Self-advocacy for communication access is the goal. Refer on to adult services; the EP role is usually time-limited here.",
   "tools": ["WAIS-IV UK", "CELF-5 UK", "WIAT-III UK"],
  },
  "Special Setting": {
   "applies": "YES — language classes serve some children with DLD; in other special settings language disorder is usually 'associated with' another condition",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "In a language class, the question is progress against SLT targets and readiness for mainstream. In other special settings, check whether the class's language level matches the pupil, and whether AAC or a total communication approach is used consistently across staff.",
   "tools": ["Communication Matrix / AAC review", "Vineland-3 / ABAS-3", "CELF-5 UK"],
  },
 },
},

# =====================================================================================
# 2. DEVELOPMENTAL COORDINATION DISORDER
# =====================================================================================
{
 "name": "Developmental Coordination Disorder (DCD / dyspraxia)",
 "code": "DSM-5-TR Developmental Coordination Disorder (F82) · ICD-11 6A04 Developmental motor coordination disorder",
 "neps": "1. LEARNING (1.6 Co-ordination — fine motor / handwriting, gross motor / PE skills)",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "A neurodevelopmental condition in which learning and carrying out coordinated motor skills is substantially below what is expected for age and opportunity, and this significantly interferes with daily living, school productivity, play or leisure (APA, 2022, DSM-5-TR).",
  "DSM-5-TR criteria in outline:\n▸ A — motor skills substantially below age and opportunity.\n▸ B — significant, persistent interference with everyday activities and school.\n▸ C — onset in the early developmental period.\n▸ D — not better explained by intellectual disability, visual impairment or a neurological condition affecting movement (e.g. cerebral palsy).",
  "The international recommendations (Blank et al., 2019, European Academy of Childhood Disability) are the current clinical standard. They set out how each criterion should be assessed, recommend a standardised motor test for criterion A (Movement ABC-2 is the most widely used) and a medical examination for criterion D.",
  "It is a disorder of MOTOR LEARNING, not just clumsiness. Children need far more practice to automatise a skill (handwriting, tying laces, riding a bike), and the skill may not transfer to a new context.",
  "Handwriting is often the school-visible part — slow, effortful, poorly formed — but the difficulty also shows in dressing, eating, PE, organisation of materials and practical subjects.",
  "It is LONG-TERM. Many adolescents and adults continue to have motor difficulties, and secondary effects — low self-worth, reduced physical activity, anxiety — are well documented (Blank et al., 2019).",
 ],

 "what_it_is_not": [
  "NOT laziness, carelessness or messiness. Children with DCD usually put in MORE effort for poorer output. Comments such as 'take more care' on written work describe the disorder, not the child's attitude.",
  "NOT the same as 'verbal dyspraxia' / childhood apraxia of speech. That is a speech motor planning disorder under SLT. The word 'dyspraxia' is used loosely for both; check which one a report means.",
  "NOT something children grow out of. Many continue to have difficulties into adolescence and adulthood (Blank et al., 2019). Some skills are learned with practice; new skills remain slow to learn.",
  "NOT diagnosed by the EP. The EP may administer a motor screen if trained, but diagnosis requires OT / physiotherapy assessment of criteria A and B plus medical exclusion of other causes (criterion D). In Ireland this usually sits with CDNT or Primary Care OT with GP / paediatric input.",
  "NOT treated best by 'process' approaches such as sensory integration therapy or perceptual-motor training alone. Task-oriented approaches (e.g. CO-OP, Neuromotor Task Training) have the stronger evidence (Smits-Engelsman et al., 2013; Blank et al., 2019).",
  "NOT only a motor problem in its impact. The psychosocial consequences — being picked last, avoiding PE, exclusion from play — are often what brings the child to an EP.",
 ],

 "prevalence": [
  "OVERALL: DSM-5-TR cites around 5–6% of children aged 5–11 (APA, 2022). Population studies with strict criteria find lower figures: Lingam et al. (2009), using ALSPAC data on UK 7-year-olds, found 1.7% (119 of 6,990) met DSM-IV criteria for DCD, with a further 222 children (about 3%) classed as probable DCD.",
  "IRELAND: no Irish population prevalence study is cited here — check before quoting. CDNT and OT caseload figures reflect service access, not prevalence.",
  "EARLY YEARS 0–5: Blank et al. (2019) advise that diagnosis is generally not made before age 5 unless difficulties are severe, and then confirmed by repeated assessment — check the exact recommendation before quoting.",
  "SCHOOL AGE 6–12: the main identification window, driven by handwriting, PE and self-care demands at school.",
  "ADOLESCENT 13–16: motor difficulty persists for many; secondary effects on self-concept, anxiety and physical activity become prominent.",
  "SEX RATIO: more boys than girls are identified; DSM-5-TR cites a male excess — exact ratio not stated here, check before quoting.",
  "RISK FACTORS: preterm birth and low birth weight are consistently associated (Blank et al., 2019). Always ask about birth history.",
 ],

 "cooccurring": [
  {"name": "ADHD",
   "rate": "high overlap — commonly cited around half in clinical samples; check before quoting",
   "presents": "PRESENTS AS: disorganisation, slow work and restlessness where motor and attention difficulties feed each other. Both need assessing; treating one does not resolve the other."},
  {"name": "DLD",
   "rate": "elevated — rate not stated here, check",
   "presents": "PRESENTS AS: written expression that is weak both in construction (language) and in production (motor). Separate the two by comparing oral and written versions of the same content."},
  {"name": "DYSLEXIA / SPECIFIC LEARNING DIFFICULTY",
   "rate": "elevated — rate not stated here, check",
   "presents": "PRESENTS AS: poor spelling plus poor handwriting. Spelling assessed by dictation is contaminated by handwriting; use a typed or oral spelling check to separate them."},
  {"name": "AUTISM",
   "rate": "motor difficulty common in autism — rate not stated here, check",
   "presents": "PRESENTS AS: clumsiness plus social-communication difference. DSM-5-TR allows both diagnoses; motor difficulty in autism is often overlooked."},
  {"name": "ANXIETY AND LOW SELF-WORTH",
   "rate": "elevated, usually secondary (Blank et al., 2019) — rate not stated here, check",
   "presents": "PRESENTS AS: PE avoidance, 'forgotten' kit, somatic complaints on PE days, reluctance to write, withdrawal at break time. Ask about it directly."},
  {"name": "JOINT HYPERMOBILITY",
   "rate": "reported in some children with DCD — rate not stated here, check",
   "presents": "PRESENTS AS: fatigue and pain with writing, loose grip. Medical / physiotherapy question, not an EP one — flag it in the referral."},
 ],

 "recommendations": [
  "DESCRIBE FUNCTION, NOT JUST SCORES. 'Copies from the board at about half the rate of peers; fatigues after 10 minutes of writing' is actionable. 'Below average fine motor skills' is not.",
  "REDUCE WRITTEN OUTPUT DEMAND: printed notes instead of board copying, cloze or fill-in worksheets, reduced quantity with the same content, and oral or alternative ways of showing learning.",
  "TOUCH-TYPING, EARLY. Specify a programme, daily short practice, and a named adult to monitor. Keyboarding is a skill that itself needs teaching; it is not an instant fix.",
  "ERGONOMICS: chair and table height so feet are flat and forearms rest at elbow height, sloped writing surface if the OT advises, pencil grips only on OT advice.",
  "PE AND PRACTICAL SUBJECTS: adapt for participation, break skills into steps, allow extra practice time, avoid public 'picking teams'. Talk to the PE teacher directly — this is where much of the social cost happens.",
  "ORGANISATION: visual checklists for kit and equipment, a set place for materials, extra time for changing.",
  "USE THE OT's TASK-ORIENTED TARGETS in school: ask for the OT report and embed specific goals (e.g. a CO-OP goal) in the Student Support Plan with practice built into the week.",
  "READ PROCESSING SPEED CAREFULLY in cognitive assessment. WISC-V Coding and Symbol Search have a motor component; low scores may be motor, not cognitive speed. Say so in the report.",
  "RACE at post-primary: build handwriting-speed evidence (DASH) early; check current State Examinations Commission criteria for word processor or scribe.",
  "CONTINUUM LEVEL: Classroom Support for most adaptations; School Support for targeted handwriting / typing; School Support Plus where OT / CDNT is involved.",
  "REFER: OT via HSE Primary Care or CDNT (check local route); GP for medical review to exclude neurological causes (criterion D); physiotherapy for gross motor where the service offers it.",
  "DO NOT recommend sensory integration therapy, perceptual-motor training or retained-reflex programmes as treatments for DCD. The evidence favours task-oriented approaches (Blank et al., 2019; Smits-Engelsman et al., 2013). PSI 4.2.2 applies.",
 ],

 "explain_parent": [
  "'DCD — some people call it dyspraxia — means his brain finds it harder to learn and plan movements. Things other children pick up with a bit of practice, like handwriting, buttons or catching a ball, take him much more practice and more effort.'",
  "'It isn't laziness and it isn't carelessness. When his writing is messy, it's usually because he's working harder than everyone else, not less.'",
  "'It isn't about how clever he is. His ideas are [specific]; getting them onto paper is where the difficulty is.'",
  "'What helps most is practising the specific skills that matter to him in real situations — that's what the OT will do — and reducing the demands that aren't the point, like copying off the board.'",
  "'It's worth protecting his confidence around sport and play. Swimming, cycling or any activity he enjoys counts, even if he's not competitive at it.'",
  "SIGNPOST: Dyspraxia/DCD Ireland → https://www.dyspraxia.ie/ ; HSE Primary Care OT or CDNT route; GP for medical review.",
 ],

 "explain_teacher": [
  "'This is a motor learning difficulty. He needs many more repetitions than other children to learn a movement skill, and more effort to carry it out — so writing tires him quickly.'",
  "'Messy or slow work isn't a sign of not trying. Please don't mark it down for presentation or ask him to redo it neatly — that doubles the task that's hardest for him.'",
  "'Give printed notes rather than board copying, and let him show what he knows in other ways — orally, typed, a diagram.'",
  "'Start touch-typing now. It takes time to become quicker than handwriting, and he'll need it for the Junior and Leaving Cert if handwriting stays slow.'",
  "'In PE, adapt so he takes part — break the skill down, let him practise, don't have captains picking teams. That's where the self-esteem damage happens.'",
  "'Check his seating: feet flat on the floor, table at elbow height. It's cheap and it helps.'",
 ],

 "explain_child": [
  "YOUNGER: 'Your brain and your body are still learning to be a team. Some things — like writing or buttons — need lots more practice for you. That's not your fault, and it doesn't mean you're not clever.'",
  "OLDER: 'DCD means your brain plans movements differently, so skills like handwriting or sport take more practice and more effort. Lots of people have it — some are writers, scientists, engineers. Typing, extra time and practice on the things that matter to you all help.'",
  "ASK: 'Which things in school are hardest because of your hands or your body?' and 'Which ones would you most like to get better at?' — the child's choice of goal is exactly how CO-OP works (Polatajko & Mandich, 2004).",
  "NAME THE EFFORT SPECIFICALLY: 'I can see you worked really hard on that. The ideas in it are good — the writing is the hard bit, and we can find ways round that.'",
  "ASK ABOUT BREAK TIME AND PE: 'What happens at yard time?' Exclusion from games is common and children rarely volunteer it.",
 ],

 "analogies": [
  "WRITING WITH YOUR OTHER HAND: 'Try writing your name with your non-dominant hand. You can do it — but it's slow, it's tiring, and you can't think about anything else at the same time. That's what handwriting is like for her all day.' Works very well with teachers and parents.",
  "THE MANUAL GEARBOX: 'Most people's movements have gone automatic. His are still in manual — every change needs thinking about, so there's less left over for listening or ideas.' Good for explaining fatigue and dual-task difficulty.",
  "THE NEW DANCE ROUTINE: 'Everyone else learned the steps after a few goes. She needs many more run-throughs, and if the music changes she has to learn it again.' Good with children and adolescents; explains poor transfer of skills.",
  "SNOWBOARDING FOR THE FIRST TIME: 'Remember concentrating on every single movement and still falling? That's DCD on a normal school day.' Good with adolescents.",
 ],

 "language": [
  "'Developmental Coordination Disorder (DCD)' is the diagnostic and research term (APA, 2022; Blank et al., 2019). 'Dyspraxia' is widely used in Ireland and the UK and by Dyspraxia/DCD Ireland. Use the term on the report you are reading and note the other.",
  "'Dyspraxia' is sometimes used more broadly to include organisation and planning difficulties, or to mean verbal dyspraxia (a speech disorder). Be precise about which you mean.",
  "Avoid 'clumsy child', 'messy', 'careless', 'lazy handwriting' in reports. These are judgements, and PSI 1.2.8 requires opinion to be labelled.",
  "Avoid 'fine motor delay' for a school-age child with persistent difficulty — 'delay' implies catching up.",
  "Community preference on person-first versus identity-first varies. Ask the young person.",
 ],

 "red_flags": [
  "RED FLAG — LOSS of motor skills previously acquired, or a change in gait, balance or strength. Not DCD. Urgent GP / paediatric referral.",
  "RED FLAG — asymmetry (one side clearly weaker), tremor, or frequent falls with no clear pattern. Neurological question; criterion D requires medical exclusion.",
  "RED FLAG — frequent unexplained bruising or injuries attributed to 'clumsiness'. Consider child protection; do not let a motor explanation close the question. Follow Children First procedures and report to Tusla as soon as practicable if you have reasonable grounds for concern; telling the DLP does not discharge a mandated person's duty.",
  "RED FLAG — withdrawal, low mood or emerging self-harm in an adolescent with DCD. Psychosocial risk is elevated. Follow the risk protocol the same day.",
  "BOUNDARY — you do not diagnose DCD. OT / physiotherapy assess criteria A and B; a doctor excludes other causes. You describe function, assess cognition and attainment with the motor load stated, and refer. PSI 2.2.2.",
  "WATCH — vision. Visual impairment is an exclusion under criterion D. Ask when eyes were last checked and refer to ophthalmology / optometry if unclear.",
 ],

 "child_voice": [
  "PERCEIVED EFFICACY AND GOAL SETTING SYSTEM (PEGS) — picture cards on everyday motor tasks that the child sorts by how well they do them and chooses goals from. Good because it gives the child a way to name priorities, which is how task-oriented intervention starts (Missiuna & Pollock, 2000 — check the current edition).",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — Irish, free, in schools already. Good because it surfaces PE and yard time without leading. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "DAY MAPPING — the child marks a typical school day green / amber / red. Good because motor demands cluster (writing blocks, PE, lunch, changing) and the map shows where.",
  "SCALING ON A LADDER for 'how tired are your hands at the end of a writing lesson?' — good because fatigue is invisible to adults and children rarely report it spontaneously.",
  "DYSPRAXIA/DCD IRELAND young people's materials — Irish, written for young people. Good because self-understanding supports self-advocacy for typing and RACE. → https://www.dyspraxia.ie/",
 ],

 "questions": [
  "Q: 'He's just clumsy — isn't everyone a bit?' — A: 'Everyone has clumsy moments. DCD is when the difficulty learning movement skills is significant enough to get in the way of school and daily life, over time. That's what the assessment looks at.'",
  "Q: 'Is it the same as dyspraxia?' — A: 'Largely, yes. DCD is the clinical term; dyspraxia is the one most people in Ireland use. Dyspraxia is sometimes also used for a speech difficulty, so it's worth being clear which a report means.'",
  "Q: 'Will a pencil grip fix it?' — A: 'It might help comfort for some children, and the OT is the right person to advise on that. It won't fix the underlying motor learning difficulty — that needs practice on specific tasks, and reducing the writing load in the meantime.'",
  "Q: 'Should she stop PE?' — A: 'No. Physical activity matters even more for children with DCD, because they often do less of it. What changes is how PE is run — adapted so she takes part and isn't publicly compared.'",
  "Q: 'Can you diagnose it?' — A: 'No. Diagnosis needs an OT or physio to assess motor skills and a doctor to rule out other causes. I can describe how it's affecting learning and make the referral with that evidence.'",
  "Q: 'His IQ report says slow processing speed — is that DCD?' — A: 'It might be partly. Two of the processing speed tasks involve pencil work, so motor difficulty can pull the score down. I'd want to read it alongside his motor profile before calling it a thinking-speed difficulty.'",
  "Q: 'Will he get a scribe or a laptop in the exams?' — A: 'Possibly. The school applies to the State Examinations Commission against its current criteria, and building evidence early — like handwriting-speed testing — helps. I can't promise the outcome.'",
 ],

 "supervision": [
  "Ask whether EPs in this service administer the Movement ABC-2, and what training is required before you do.",
  "Clarify the local OT route — Primary Care versus CDNT — and what a referral needs to include to be accepted.",
  "Bring a WISC-V profile with a low Processing Speed Index and discuss how to report it where a motor difficulty is suspected.",
  "Discuss how to raise PE adaptation with a post-primary school where PE is taught by a subject teacher you have not met.",
  "Bring a case where a 'behaviour' referral turned out to involve avoidance of written work, and discuss the formulation.",
 ],

 "reflection": [
  "ON HOW I EXPLAINED IT — Did I use the 'write with your other hand' demonstration or something like it, or did I say 'fine motor difficulties' and move on?",
  "ON MY REPORT LANGUAGE — Did I describe written work as 'untidy' or 'careless' anywhere, even in quoting the school? If I quoted it, did I reframe it?",
  "ON PROCESSING SPEED — Did I read low Coding / Symbol Search in light of motor difficulty, or report it as slow cognitive processing?",
  "ON THE BOUNDARY — Did I stay clear that diagnosis is OT / medical, or did my report read as though I had identified DCD?",
  "ON PSYCHOSOCIAL IMPACT — Did I ask about PE, yard time and friendships, or only about handwriting?",
  "WHAT GOOD LOOKS LIKE: 'The school referred for work avoidance. I timed his copying against two peers and it was less than half their rate, with visible fatigue after eight minutes. The recommendation became printed notes and a typing programme; the avoidance reduced once the demand did.'",
  "WHAT POOR LOOKS LIKE: 'Fine motor skills appear weak. OT referral recommended.' — no functional description, no classroom adaptations, nothing the teacher can do this week.",
 ],

 "citations": [
  "Blank, R., Barnett, A. L., Cairney, J., Green, D., Kirby, A., Polatajko, H., Rosenblum, S., Smits-Engelsman, B., Sugden, D., Wilson, P., & Vinçon, S. (2019). International clinical practice recommendations on the definition, diagnosis, assessment, intervention, and psychosocial aspects of developmental coordination disorder. Developmental Medicine & Child Neurology, 61(3), 242–285.",
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Developmental Coordination Disorder.",
  "Lingam, R., Hunt, L., Golding, J., Jongmans, M., & Emond, A. (2009). Prevalence of developmental coordination disorder using the DSM-IV at 7 years of age: A UK population-based study. Pediatrics, 123(4), e693–e700.",
  "Smits-Engelsman, B. C. M., Blank, R., van der Kaay, A.-C., Mosterd-van der Meijs, R., Vlugt-van den Brand, E., Polatajko, H. J., & Wilson, P. H. (2013). Efficacy of interventions to improve motor performance in children with developmental coordination disorder: A combined systematic review and meta-analysis. Developmental Medicine & Child Neurology, 55(3), 229–237.",
  "Polatajko, H. J., & Mandich, A. (2004). Enabling occupation in children: The Cognitive Orientation to daily Occupational Performance (CO-OP) approach. CAOT Publications.",
  "Henderson, S. E., Sugden, D. A., & Barnett, A. L. (2007). Movement Assessment Battery for Children — Second Edition (Movement ABC-2). Pearson.",
  "Barnett, A., Henderson, S. E., Scheib, B., & Schulz, J. (2007). Detailed Assessment of Speed of Handwriting (DASH). Pearson.",
  "Kirby, A., Edwards, L., Sugden, D., & Rosenblum, S. (2010). The development and standardization of the Adult Developmental Co-ordination Disorders/Dyspraxia Checklist (ADC). Research in Developmental Disabilities, 31(1), 131–139.",
  "Missiuna, C., & Pollock, N. (2000). Perceived efficacy and goal setting in young children. Canadian Journal of Occupational Therapy, 67(2), 101–109.",
 ],

 "pathway": {
  "age": "Usually 5–10. Blank et al. (2019) advise against diagnosis before about age 5 except in severe cases, because motor development varies widely in the early years. School then brings handwriting, PE and self-care demands that make the difficulty visible. Milder presentations, and those masked by strong verbal ability, are identified later — sometimes in adolescence through handwriting-speed or exam-access evidence.",
  "who_diagnoses": "Ireland: Occupational Therapist (sometimes with physiotherapy), within HSE Primary Care or a CDNT depending on complexity, with medical input (GP / paediatrician) to exclude neurological or other causes (criterion D). Assessment of Need (Disability Act 2005) may lead to it. Private OT reports are common. Check local routes.",
  "who_wrote_report": "Primary Care or CDNT OT; physiotherapist; community paediatrician; private OT. A Movement ABC-2 score in an EP report is a screening finding, not a diagnosis.",
  "refer_to": "OT via Primary Care or CDNT (check local criteria). GP for medical review, and urgently if any regression, asymmetry or neurological sign. Optometry / ophthalmology if vision unchecked. SLT if verbal dyspraxia or language difficulty is also suspected.",
  "sooner": "'DCD is one of the most under-recognised conditions — children are often called clumsy or careless for years before anyone looks properly. The fact that you've noticed and pushed for this is what matters now.'",
 },

 "differential": [
  "NEUROLOGICAL CONDITION (e.g. mild cerebral palsy, neuromuscular disorder) — exclusion under criterion D; needs medical examination.",
  "VISUAL IMPAIRMENT — exclusion under criterion D; check eye examination.",
  "INTELLECTUAL DISABILITY / GLD — motor skills in line with general ability are not DCD; DSM-5-TR allows both only where motor difficulty exceeds what the ID would explain.",
  "LACK OF OPPORTUNITY — limited early play or practice; criterion A is judged against age AND opportunity.",
  "JOINT HYPERMOBILITY — can mimic or accompany DCD; physiotherapy / medical question.",
  "ADHD — impulsivity and inattention can look like carelessness in motor tasks; assess both.",
 ],

 "next": [
  "Get a functional description: timed copying against peers, fatigue, self-care, PE — from teacher, parent and child.",
  "Check birth history, vision and any medical history; note anything relevant to criterion D.",
  "Write classroom adaptations (output load, typing, seating, PE) at the right Continuum level with a named adult.",
  "Refer to OT (Primary Care or CDNT) with the functional evidence; GP for medical review.",
 ],

 "presentations": [
  "Fine motor difficulty (handwriting, pencil grip)",
  "Gross motor difficulty (PE, balance, ball skills)",
  "Presentation and care of written work",
  "Self-care and independence skills at school",
  "Motor-based sensory difficulties",
  "Sensory modulation difficulties (over- or under-responsive)",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — diagnosis generally not made before about age 5 except in severe cases (Blank et al., 2019)",
   "prevalence": "Not reliably estimated at this age — check before quoting.",
   "see": "Late or effortful milestones (sitting, walking, running), difficulty with stairs, dressing, cutlery, scissors and puzzles; avoidance of climbing and ball play. Describe and monitor rather than label; refer to OT where impact on daily living is clear.",
   "tools": ["Movement ABC-2", "Beery VMI", "Ages & Stages Questionnaires (ASQ-3)", "Griffiths III"],
  },
  "School Age": {
   "applies": "YES — main identification window",
   "prevalence": "DSM-5-TR: around 5–6% of 5–11-year-olds (APA, 2022); strict population estimates lower (Lingam et al., 2009).",
   "see": "Slow, effortful, poorly formed handwriting; difficulty copying from the board; trouble with scissors, rulers and laces; avoidance of PE and ball games; disorganised desk and belongings; fatigue in writing lessons. Often referred as work avoidance or carelessness.",
   "tools": ["DCD-Q", "Movement ABC-2", "Beery VMI", "DASH", "WISC-V UK"],
  },
  "Adolescent": {
   "applies": "YES — persists; exam access and psychosocial impact dominate",
   "prevalence": "Persistence into adolescence is common (Blank et al., 2019); rate not stated here — check.",
   "see": "Handwriting speed limits exam output; practical subjects (science, home economics, technology) are hard; PE avoidance, low physical self-concept, social withdrawal and anxiety may emerge. RACE evidence and typing become priorities.",
   "tools": ["DASH", "Beery VMI", "Movement ABC-2", "Access arrangements evidence (RACE)", "DCD-Q"],
  },
  "Young Adult": {
   "applies": "YES — lifelong; relevant to further education, DSA, driving and workplace",
   "prevalence": "Adult rate not stated here — check.",
   "see": "Difficulty with note-taking, practical or laboratory work, driving, and organisation of daily life. Many first identified here. Refer to adult services; the EP role is usually limited to educational access evidence.",
   "tools": ["DASH-17+", "Adult DCD/Dyspraxia Checklist (ADC; Kirby et al., 2010) — AGE adult · MEASURES: self-report of childhood and current motor and organisational difficulty · CANNOT TELL YOU: diagnosis or motor performance · TIME: about 15 min — check current version"],
  },
  "Special Setting": {
   "applies": "YES — but check whether motor difficulty is 'DCD' or part of another condition (ID, CP, genetic syndrome)",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "The question is usually access — seating, equipment, adapted materials — and whether OT recommendations are actually in place. Where ID is present, DCD is only added if motor difficulty exceeds what the ID explains.",
   "tools": ["Vineland-3 / ABAS-3", "Beery VMI"],
  },
 },
},

# =====================================================================================
# 3. GENERALISED ANXIETY DISORDER
# =====================================================================================
{
 "name": "Generalised Anxiety Disorder",
 "code": "DSM-5-TR Generalized Anxiety Disorder (F41.1) · ICD-11 6B00 Generalised anxiety disorder",
 "neps": "3. EMOTIONAL (3.2 Anxiety)",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Equal Status Acts 2000–2018 · GDPR · Mental Health Act 2001 (for context of CAMHS; check current amendments)",

 "what_it_is": [
  "Excessive, hard-to-control WORRY about a number of different things (schoolwork, family safety, health, the future, world events), present more days than not for at least 6 months, causing significant distress or impairment (APA, 2022, DSM-5-TR).",
  "DSM-5-TR requires associated symptoms — restlessness, fatigue, poor concentration, irritability, muscle tension, sleep disturbance. For CHILDREN only ONE is required (three for adults). ICD-11 describes the same core picture — check its duration wording before quoting.",
  "The core is not fear of one thing but WORRY as a way of coping with UNCERTAINTY. The intolerance-of-uncertainty model (Dugas et al., 1998) is the best-known cognitive account: worry feels like preparation or prevention, so it is maintained.",
  "In school it often looks like perfectionism, repeated reassurance-seeking ('Is this right?'), difficulty starting or finishing work, over-preparation, headaches or tummy aches, and tiredness. These children are frequently compliant and high-achieving, so they are missed.",
  "It is maintained by AVOIDANCE and by adult ACCOMMODATION — reassurance, taking over, removing demands. These reduce anxiety in the moment and increase it over time (Lebowitz et al., 2020).",
  "Anxiety disorders are among the most common mental health conditions in childhood and adolescence (Polanczyk et al., 2015), and they respond well to CBT-based approaches (James et al., 2020).",
 ],

 "what_it_is_not": [
  "NOT ordinary worry. All children worry; GAD is worry that is excessive for the situation, hard to switch off, present across many topics, persistent over months, and interfering with life.",
  "NOT a diagnosis the EP makes. Diagnosis sits with CAMHS or Primary Care Psychology (or a private clinician). The EP describes the anxiety, formulates what maintains it in school, recommends, and refers where the threshold is met.",
  "NOT helped by reassurance on its own. Repeated reassurance is part of the maintaining cycle. What helps is a brief, consistent, confident response and support to tolerate uncertainty.",
  "NOT helped by removing every demand. Avoidance brings short-term relief and long-term growth of the anxiety. The aim is graded, supported approach, not removal.",
  "NOT always a stand-alone problem. Anxiety is frequently SECONDARY to an unmet learning need (dyslexia, DLD, DCD), to autism, or to a real stressor (bullying, family difficulty, trauma). Always ask what the child is worried about and whether it is realistic.",
  "NOT separation anxiety, social anxiety or panic disorder — those have a specific focus. GAD is broad and diffuse. The distinction matters for the treatment and the referral.",
 ],

 "prevalence": [
  "OVERALL: Polanczyk et al. (2015) estimated the worldwide pooled prevalence of ANY anxiety disorder in children and adolescents at about 6.5%. GAD-specific rates vary widely by study and age — rate not stated here, check before quoting.",
  "IRELAND: My World Survey 2 (Dooley et al., 2019) reported elevated anxiety symptoms in a substantial proportion of Irish adolescents and young adults — check the report for exact figures before quoting. Symptom surveys are not diagnostic prevalence.",
  "EARLY YEARS 0–5: GAD is rarely diagnosed; separation anxiety and specific phobias are the typical early anxiety presentations.",
  "SCHOOL AGE 6–12: GAD becomes identifiable, usually as worry about performance, family, health and safety; frequently missed in compliant children.",
  "ADOLESCENT 13–16: rates of anxiety rise, and co-occurrence with low mood becomes more common. Exam years are a pressure point.",
  "SEX RATIO: more girls than boys from adolescence — exact ratio not stated here, check before quoting.",
 ],

 "cooccurring": [
  {"name": "OTHER ANXIETY DISORDERS (separation, social, specific phobia)",
   "rate": "co-occurrence among anxiety disorders is common — rate not stated here, check",
   "presents": "PRESENTS AS: worry that is broad but with one sharper focus (e.g. being away from a parent, or being judged). Record each focus; the referral should name them."},
  {"name": "DEPRESSION / LOW MOOD",
   "rate": "elevated, especially in adolescence — rate not stated here, check",
   "presents": "PRESENTS AS: worry plus withdrawal, loss of interest, hopelessness. Ask directly about mood and about thoughts of self-harm or suicide — asking does not increase risk."},
  {"name": "EMOTIONALLY BASED SCHOOL AVOIDANCE (EBSA)",
   "rate": "frequent pathway — rate not stated here, check",
   "presents": "PRESENTS AS: somatic complaints on school mornings, late arrival, partial attendance, then refusal. Attendance data is part of the anxiety assessment."},
  {"name": "UNIDENTIFIED LEARNING NEED (dyslexia, DLD, DCD)",
   "rate": "anxiety secondary to learning need is common — rate not stated here, check",
   "presents": "PRESENTS AS: worry that clusters around specific subjects or tasks. Assess attainment; if the worry is realistic, the intervention is the learning support."},
  {"name": "AUTISM",
   "rate": "anxiety is common in autistic children and young people — rate not stated here, check",
   "presents": "PRESENTS AS: distress with change, uncertainty and sensory load. Anxiety measures may not fit autistic presentations; consider an autism-adapted measure and CDNT input."},
  {"name": "ADHD",
   "rate": "elevated — rate not stated here, check",
   "presents": "PRESENTS AS: restlessness and poor concentration that could be either. Ask what is going on in the child's head when they cannot concentrate — worry or distraction."},
  {"name": "SLEEP DIFFICULTY",
   "rate": "very common and bidirectional",
   "presents": "PRESENTS AS: bedtime worry, late sleep onset, daytime tiredness. Always ask; poor sleep amplifies anxiety and everything else."},
 ],

 "recommendations": [
  "FORMULATE THE MAINTAINING CYCLE in the report: trigger → worry → avoidance or reassurance → short-term relief → anxiety grows. Name what school does, with the best intentions, that feeds the cycle.",
  "ONE BRIEF, CONSISTENT RESPONSE TO REASSURANCE-SEEKING, agreed across staff: 'I can see you're worried. I think you can do this — have a go and I'll check back in five minutes.' Not dismissive; not a repeated explanation.",
  "PREDICTABILITY: advance notice of changes, a visual timetable, clear success criteria so the child knows what 'finished' looks like. This reduces uncertainty without removing challenge.",
  "GRADED APPROACH, NOT AVOIDANCE: agree a small ladder of steps towards the feared task (e.g. reading aloud to one adult → small group → class), with the child, and review weekly.",
  "TEACH ANXIETY MANAGEMENT: psychoeducation about the anxiety cycle; breathing or grounding strategies; 'worry time' for younger children. School-based CBT-informed programmes such as FRIENDS may be available through NEPS — check local availability.",
  "SUPPORT PERFECTIONISM: time limits on tasks, 'good enough' exemplars, praise for effort and strategy rather than for flawless output.",
  "WORK WITH PARENTS on reducing accommodation — parent-led CBT has good evidence for younger children (Creswell et al., 2017; Lebowitz et al., 2020). Signpost Creswell & Willetts (2019).",
  "ASSESS ATTAINMENT if worry clusters around learning. Anxiety secondary to an unmet need is treated by meeting the need.",
  "MONITOR: agree a simple measure — RCADS repeated, a weekly scaling rating, attendance — and a review date.",
  "CONTINUUM LEVEL: Classroom Support for mild worry; School Support for a targeted plan; School Support Plus where CAMHS, Primary Care Psychology or Jigsaw is involved.",
  "REFER: Primary Care Psychology (mild–moderate) or CAMHS (moderate–severe, or with risk or significant impairment) via GP — check local criteria. Jigsaw for young people aged 12–25 in areas where it operates.",
  "DO NOT advise on medication, and do not recommend blanket removal of demands (e.g. indefinite exemption from oral work) — it maintains the anxiety. PSI 2.2.2.",
 ],

 "explain_parent": [
  "'Everyone worries. What we're seeing with her is worry that's much bigger than the situation, about lots of different things, and it's hard for her to switch off. That's what anxiety at this level looks like.'",
  "'Worry is her brain trying to keep her safe by preparing for every possible problem. The trouble is, it never feels prepared enough — so it keeps going.'",
  "'When she asks for reassurance, it helps in the moment and makes the worry stronger over time. A short, calm, confident answer — then moving on — works better than long explanations. That's hard, and it's not about being cold.'",
  "'Avoiding what she's scared of brings relief today and makes it harder tomorrow. We want to help her take small steps towards things, with support, rather than away from them.'",
  "'This is very treatable. Approaches based on CBT work well for children, and there's good evidence for programmes where parents are coached to help.'",
  "SIGNPOST: Creswell & Willetts (2019), Helping Your Child with Fears and Worries; GP for Primary Care Psychology or CAMHS referral; Jigsaw (12–25) → https://jigsaw.ie/",
 ],

 "explain_teacher": [
  "'She's anxious, not unmotivated. The perfectionism, the rubbing out, the not handing in — that's the worry, not the work ethic.'",
  "'Reassurance is the trap. Agree one short, consistent response across the staff — acknowledge the worry, say you think she can do it, and check back later.'",
  "'Tell her about changes in advance where you can. Uncertainty is the fuel for this kind of anxiety.'",
  "'Please don't remove the thing she's anxious about entirely — that makes it grow. Break it into small steps and let her build up.'",
  "'Give clear success criteria and a time limit. \"Five sentences, ten minutes\" is easier to finish than \"do your best\".'",
  "'The quiet, compliant, high-achieving child can be the most anxious one in the room. They're easy to miss because they're no trouble.'",
 ],

 "explain_child": [
  "YOUNGER: 'Everyone has a worry alarm in their brain. It's meant to go off when there's danger. Yours is a bit too sensitive — it goes off even when things are probably OK. We can help you turn the volume down.'",
  "OLDER: 'Anxiety is your brain trying to protect you by predicting everything that could go wrong. The problem is it keeps going even when it's not helping. Avoiding things makes it louder over time; small steps towards things make it quieter. It's very common, and it gets better.'",
  "EXTERNALISE THE WORRY: 'If your worry was a character, what would it look like? What does it say to you?' Naming it separates the child from the anxiety.",
  "ASK: 'What are the things you worry about most?' (list them), 'What happens in your body?', 'What do you do when the worry comes?' — the last one tells you the maintaining behaviour.",
  "ASK ABOUT RISK DIRECTLY where age-appropriate: 'Sometimes when people feel this worried they have thoughts of hurting themselves or not wanting to be here. Has that happened for you?' Follow the risk protocol the same day if yes.",
 ],

 "analogies": [
  "THE OVER-SENSITIVE SMOKE ALARM: 'It's meant to go off for a fire. Hers goes off for toast. The alarm is real and the fear is real — it's the setting that's off.' Works with children, parents and teachers.",
  "THE BULLY IN YOUR HEAD: 'Worry is like a bully — the more you give in, the more it asks for.' Good with 7–12s; explains why avoidance backfires (used in many CBT programmes for children).",
  "THE SWIMMING POOL: 'You don't get used to cold water by standing on the edge. You get in a bit at a time and your body adjusts.' Good for explaining graded exposure to parents and older children.",
  "THE WHAT-IF MACHINE: 'Her brain is a brilliant what-if machine. It's great for planning and terrible at stopping.' Good with adolescents and high-achieving children; frames the trait without pathologising.",
 ],

 "language": [
  "'Anxiety' is widely understood and generally acceptable. 'Generalised Anxiety Disorder' should only appear in a report where a clinician has diagnosed it — otherwise describe 'significant anxiety' or 'anxiety-related difficulties'.",
  "Avoid 'worrier', 'highly strung', 'drama', 'attention-seeking' in reports. These are judgements and PSI 1.2.8 applies.",
  "Avoid 'school refuser' — use 'emotionally based school avoidance' or describe attendance. The first locates the problem in the child's will.",
  "Use the young person's words for their experience ('stressed', 'panicky', 'overthinking') in the child's-voice section; use clinical terms only where accurate.",
 ],

 "red_flags": [
  "RED FLAG — thoughts of self-harm or suicide, or evidence of self-harm. Same-day risk route: inform the DLP, follow the service risk protocol, contact the parent unless doing so raises risk, and ensure a same-day GP / CAMHS / emergency response as indicated. Supervision follows action; it does not replace it.",
  "RED FLAG — anxiety that is REALISTIC: fear of a person, of going home, of someone at school. Consider abuse, neglect, bullying or domestic violence. Follow Children First; report to Tusla as soon as practicable. Telling the DLP does not discharge a mandated person's duty.",
  "RED FLAG — sudden onset in a previously settled child. Ask what changed — bereavement, family change, trauma, bullying, illness.",
  "RED FLAG — weight loss, restricted eating or physical symptoms that are escalating. Medical review via GP; consider eating difficulties.",
  "BOUNDARY — you do not diagnose GAD, you do not provide ongoing CBT treatment outside your service's remit and competence, and you do not advise on medication. PSI 2.2.2.",
  "WATCH — attendance. Declining attendance is often the first objective sign that anxiety is escalating into EBSA.",
 ],

 "child_voice": [
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — Irish, free, in schools already. Good because it surfaces which parts of the day are hard without leading the child to 'anxiety'. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "WORRY MAPPING / WORRY LIST with ratings — the child lists worries and rates each 0–10. Good because it separates GAD (many topics) from a single-focus anxiety and gives a baseline to monitor.",
  "BODY MAP — the child colours where they feel worry in their body. Good because younger children often cannot name anxiety but can locate the tummy ache or tight chest.",
  "SCALING ON A LADDER ('how worried on a school morning?') — good because it gives a monitoring number and a solution-focused follow-up ('what would one step up look like?').",
  "RCADS SELF-REPORT (8–18) — standardised, gives the young person a structured way to report symptoms they may not say aloud. Good as long as risk is asked about separately, face to face.",
 ],

 "questions": [
  "Q: 'Isn't all this just normal teenage stress?' — A: 'Some worry is normal at every age. What we're looking at is how much, how long, how many areas of life, and how much it's getting in the way. That's what separates ordinary stress from anxiety that needs support.'",
  "Q: 'Should I keep reassuring her?' — A: 'A little, briefly, yes. Long or repeated reassurance tends to feed the worry. One calm, confident answer and then helping her move on works better — it's hard, and it's not about being unkind.'",
  "Q: 'Should we let him stay home when he's this anxious?' — A: 'I understand why — it brings relief straight away. The difficulty is that avoiding school tends to make the anxiety bigger over time. The plan is usually small, supported steps back rather than staying off. If attendance is already dropping, we need to act on that now.'",
  "Q: 'Does she need medication?' — A: 'That's a medical decision and not mine. What I can tell you is that talking-based approaches like CBT are the first-line treatment for anxiety in children, and they work well.'",
  "Q: 'Can you diagnose anxiety?' — A: 'No — a diagnosis would come from CAMHS or Primary Care Psychology. I can describe what's happening in school, what seems to be keeping it going, and put a plan in place, and refer if it's needed.'",
  "Q: 'She's top of the class — how can she be struggling?' — A: 'High achievement and anxiety often go together. The same drive that gets top marks can come from fear of getting it wrong. It's worth asking what it's costing her.'",
  "Q: 'Did we cause this?' — A: 'No. Anxiety comes from a mix of temperament, genes and experience. Parents are often the most important part of the solution — which is why some of the best-evidenced help works through parents.'",
 ],

 "supervision": [
  "Ask what the service's risk protocol requires if a young person discloses self-harm or suicidal thoughts during your session — step by step, and who you phone first.",
  "Clarify the local threshold between Primary Care Psychology and CAMHS, and whether Jigsaw operates in the area.",
  "Bring a case where the school has accommodated anxiety by removing demands, and discuss how to shift the plan without alienating staff or parents.",
  "Discuss the limits of your role in anxiety intervention — what the service offers (e.g. consultation, FRIENDS, brief work) and what must be referred on.",
  "Bring a case where anxiety might be secondary to a learning need or autism, and talk through how you'd assess both.",
 ],

 "reflection": [
  "ON HOW I EXPLAINED IT — Did I explain the anxiety cycle (worry → avoidance → relief → more worry) in words the parent could repeat to someone else?",
  "ON RISK — Did I ask directly about self-harm and suicidal thoughts, or did I avoid it because the child seemed 'just worried'? If I asked, did I act on the answer the same day?",
  "ON ACCOMMODATION — Did my recommendations reduce demands in a way that will feed avoidance, or did they build graded approach?",
  "ON UNDERLYING NEED — Did I check attainment, language and possible autism before formulating this as anxiety alone?",
  "ON MY OWN ANXIETY — Did I rush to reassure the child or parent because their distress made me uncomfortable? That is the same pattern I am advising against.",
  "WHAT GOOD LOOKS LIKE: 'The school had exempted her from all oral work. I mapped her worries with her, and reading aloud was a 9 but answering a question to one adult was a 3. We built a ladder from the 3. By the review she was reading to a small group, and she chose the next step herself.'",
  "WHAT POOR LOOKS LIKE: 'Presents as an anxious child. Referral to CAMHS recommended. Teacher to reassure as needed.' — no formulation, reassurance recommended as the intervention, no risk question recorded.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Generalized Anxiety Disorder.",
  "Polanczyk, G. V., Salum, G. A., Sugaya, L. S., Caye, A., & Rohde, L. A. (2015). Annual research review: A meta-analysis of the worldwide prevalence of mental disorders in children and adolescents. Journal of Child Psychology and Psychiatry, 56(3), 345–365.",
  "James, A. C., Reardon, T., Soler, A., James, G., & Creswell, C. (2020). Cognitive behavioural therapy for anxiety disorders in children and adolescents. Cochrane Database of Systematic Reviews, 2020(11), CD013162.",
  "Dugas, M. J., Gagnon, F., Ladouceur, R., & Freeston, M. H. (1998). Generalized anxiety disorder: A preliminary test of a conceptual model. Behaviour Research and Therapy, 36(2), 215–226.",
  "Creswell, C., Violato, M., Fairbanks, H., White, E., Parkinson, M., Abitabile, G., Leidi, A., & Cooper, P. J. (2017). Clinical outcomes and cost-effectiveness of brief guided parent-delivered cognitive behavioural therapy and solution-focused brief therapy for treatment of childhood anxiety disorders: A randomised controlled trial. The Lancet Psychiatry, 4(7), 529–539.",
  "Lebowitz, E. R., Marin, C., Martino, A., Shimshoni, Y., & Silverman, W. K. (2020). Parent-based treatment as efficacious as cognitive-behavioral therapy for childhood anxiety: A randomized noninferiority study of Supportive Parenting for Anxious Childhood Emotions. Journal of the American Academy of Child & Adolescent Psychiatry, 59(3), 362–372.",
  "Creswell, C., & Willetts, L. (2019). Helping your child with fears and worries (2nd ed.). Robinson.",
  "Chorpita, B. F., Yim, L., Moffitt, C., Umemoto, L. A., & Francis, S. E. (2000). Assessment of symptoms of DSM-IV anxiety and depression in children: A revised child anxiety and depression scale. Behaviour Research and Therapy, 38(8), 835–855.",
  "Spence, S. H. (1998). A measure of anxiety symptoms among children. Behaviour Research and Therapy, 36(5), 545–566.",
  "Dooley, B., O'Connor, C., Fitzgerald, A., & O'Reilly, A. (2019). My World Survey 2: The national study of youth mental health in Ireland. UCD School of Psychology and Jigsaw.",
 ],

 "pathway": {
  "age": "GAD can be diagnosed in childhood but is most often identified from late primary into adolescence, when worry about performance, the future and wider events becomes more elaborate and when exam and social pressures rise. Earlier anxiety tends to present as separation anxiety or specific fears. Compliant, high-achieving children are often identified late because they cause no trouble.",
  "who_diagnoses": "Ireland: CAMHS (moderate–severe, or with risk or significant impairment) or HSE Primary Care Psychology (mild–moderate), usually via GP referral; private clinical psychologist or psychiatrist. Jigsaw (12–25) offers early intervention but not diagnosis in most cases — check local service. Medication, if considered, is prescribed by a psychiatrist or GP, never a psychologist. Check local thresholds; they vary by CHO.",
  "who_wrote_report": "CAMHS psychiatrist, psychologist or multidisciplinary team; Primary Care psychologist; private clinical psychologist or psychiatrist. A school-completed SDQ or an RCADS score in an EP report is a screen, not a diagnosis.",
  "refer_to": "GP as first point for Primary Care Psychology or CAMHS. CAMHS directly where risk is present (check whether local CAMHS accepts non-GP referrals). Jigsaw for 12–25s where available. Same-day emergency route for acute suicide risk. Tusla if abuse or neglect is suspected.",
  "sooner": "'Anxiety is very easy to miss, especially in children who work hard and don't cause trouble — they often hold it together in school and fall apart at home. You've noticed it, and it's very treatable at any age.'",
 },

 "differential": [
  "SEPARATION ANXIETY DISORDER — worry focused on separation from attachment figures.",
  "SOCIAL ANXIETY DISORDER — worry focused on being judged or embarrassed.",
  "OCD — intrusive obsessions and compulsions rather than broad real-life worry.",
  "PTSD / TRAUMA RESPONSE — worry linked to a traumatic event and its reminders; ask about adverse experiences.",
  "DEPRESSION — low mood and loss of interest as the primary feature; often co-occurs.",
  "REALISTIC FEAR — bullying, abuse, family conflict, an unmet learning need. Establish whether the worry fits the facts before calling it disproportionate.",
  "MEDICAL — thyroid problems, caffeine or other substances, medication side-effects. GP review if physical symptoms are prominent.",
 ],

 "next": [
  "Ask directly about risk (self-harm, suicidal thoughts) and act the same day if present.",
  "Map the worries and the maintaining cycle with the child, parent and teacher; gather attendance data.",
  "Check for an underlying learning need or autism before formulating anxiety alone.",
  "Write a school plan: consistent reassurance response, predictability, graded approach, review date and measure.",
  "Refer via GP to Primary Care Psychology or CAMHS if impairment is significant; signpost Jigsaw for 12–25s.",
 ],

 "presentations": [
  "School anxiety presentations (not a standalone diagnosis)",
  "Test and exam anxiety",
  "Performance anxiety in oral work",
  "Anticipatory anxiety about transitions",
  "Somatic complaints presenting at school (tummy aches, headaches)",
  "Anxiety secondary to an unmet learning need",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — separation anxiety and specific fears are the typical early presentations",
   "prevalence": "GAD rate at this age not stated here — check before quoting.",
   "see": "Clinginess at drop-off, frequent 'what if' questions, sleep difficulties, tummy aches, distress at change. Assess through parent and staff report and observation; there is no self-report measure. Primary Care rather than NEPS for clinical-level anxiety.",
   "tools": ["SDQ (2–4 version)", "Preschool Anxiety Scale (Spence et al., 2001) — AGE about 2.5–6.5, parent report · MEASURES: generalised, social, separation, physical-injury fears and OCD symptoms · CANNOT TELL YOU: diagnosis · TIME: about 10 min — check current version"],
  },
  "School Age": {
   "applies": "YES — becomes identifiable; frequently missed in compliant children",
   "prevalence": "Any anxiety disorder about 6.5% worldwide in children and adolescents (Polanczyk et al., 2015); GAD-specific rate — check.",
   "see": "Perfectionism, reassurance-seeking, difficulty starting or finishing work, headaches and tummy aches on school mornings, worry about family, health and news events, poor sleep. Observe at the anxious moment, not a random one. Check attainment for secondary anxiety.",
   "tools": ["RCADS", "RCADS self-report", "SDQ", "Beck Youth Inventories-2", "Spence Children's Anxiety Scale (SCAS; Spence, 1998) — AGE about 8–15 child report, parent version available · MEASURES: generalised anxiety, separation, social, panic/agoraphobia, OCD, physical-injury fears · CANNOT TELL YOU: diagnosis or risk · TIME: about 10 min — check current version and norms"],
  },
  "Adolescent": {
   "applies": "YES — rates rise; co-occurrence with low mood and EBSA common",
   "prevalence": "Anxiety symptoms elevated in Irish adolescents (Dooley et al., 2019) — check figures before quoting.",
   "see": "Worry about exams, the future, appearance and friendships; perfectionism and over-studying or avoidance; fatigue, irritability, sleep problems; declining attendance. Self-report essential; ask about mood, self-harm and substance use directly.",
   "tools": ["RCADS self-report", "RCADS", "MFQ (Mood and Feelings Questionnaire)", "Beck Youth Inventories-2", "BASC-3 SRP"],
  },
  "Young Adult": {
   "applies": "YES — but this is adult mental health territory; know the boundary",
   "prevalence": "Anxiety symptoms elevated in Irish young adults (Dooley et al., 2019) — check figures before quoting.",
   "see": "Worry about study, work, money and relationships; avoidance of lectures or assessments; physical symptoms. Refer to GP, college counselling or adult mental health rather than hold the case.",
   "tools": ["Adult self-report measures via the service", "GAD-7 (Spitzer et al., 2006) — AGE adult · MEASURES: generalised anxiety symptom severity over two weeks · CANNOT TELL YOU: diagnosis or risk · TIME: 2–3 min"],
  },
  "Special Setting": {
   "applies": "YES — anxiety is common but harder to identify where language or cognition is limited",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Anxiety may show as behaviour — distress, aggression, self-injury or withdrawal around change, noise or uncertainty. Standard self-report measures may not be valid; rely on observation, functional assessment and informant report, and consider autism-adapted measures.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3", "Anxiety Scale for Children – ASD (ASC-ASD; Rodgers et al., 2016) — AGE about 8–16, parent and child · MEASURES: anxiety in autistic young people, including uncertainty · CANNOT TELL YOU: diagnosis or risk · TIME: about 10 min — check current version"],
  },
 },
},
]
