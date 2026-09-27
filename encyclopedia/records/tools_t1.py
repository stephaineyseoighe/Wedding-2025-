"""Part G tool teaching records — batch t1 (ten tools).

Written to agree with src/tool_catalogue.json and Reference Part A
('4. WISC-V administration to proficiency standard', 'Behavioural and
emotional rating scales') and Part D (rows 507–650).
No norms, cut-offs, reliability figures or item counts are stated as fact:
where they matter the entry says 'check the manual'.
"""

TOOLS = [
# ---------------------------------------------------------------- WISC-V UK
{
 "name": "WISC-V UK",
 "before": [
  "Write the referral question down before you choose the WISC-V, and ask whether it needs a cognitive battery at all. Progress over time, function in class or one specific skill are better answered by curriculum-based measures, observation or a targeted attainment test (Reference Part A, macro skill 4, 'Knowing when not to use it').",
  "Check the age and the edition. WISC-V UK covers 6:0–16:11 (Wechsler, 2016); at 6:0–7:7 it overlaps with WPPSI-IV UK, and from 16:0 you can choose WAIS-IV. Confirm whether the child has had a Wechsler test in the last twelve months — practice effects (larger on some indices than others — check the retest gains by index in the technical manual) make a short-interval retest hard to defend.",
  "Rule out the confounds before the session, not after: vision and hearing (ask about glue ear and the last audiology/ophthalmology check), language history and length of English-medium schooling, medication and sleep, and any recent upset. Record the answers — they go in the report.",
  "Know the rules cold. Start points, reverse rules, discontinue rules and permitted queries differ by subtest and there is no master rule; build a one-page crib per subtest from the administration manual and practise until you never reach for it. Hesitation is what a proficiency examiner watches for.",
  "Decide in advance which composites you need (primary indices, and whether GAI, CPI, Non-verbal or Quantitative Reasoning are relevant) so you administer the subtests that feed them. Which subtests feed which composite is set out in the manual — check it rather than relying on memory.",
 ],
 "administer": [
  "Follow the script verbatim, including the demonstration and teaching items. Every departure from standard procedure weakens the comparison with the UK standardisation sample, because that sample was not tested that way.",
  "Query only where the manual marks a response as queryable, with the specified neutral wording, and mark Q and P on the protocol. Over-querying from kindness inflates the score; under-querying scores the child on incomplete information. If you get it wrong, note it on the protocol at the time and say so in the report.",
  "Record verbatim — errors, self-corrections and order of response. The test is whether another psychologist could re-score your protocol and reach the same scaled scores.",
  "Write the clinical half as you go: planning versus diving in, response to failure, help-seeking, checking, effect of time pressure, fatigue across the session. Three sentences of behavioural observation after every administration, including practice ones.",
  "If you must adapt (breaks, split sessions, a child with a motor or sensory need, EAL), record exactly what was changed and why, and interpret the affected scores with that caution in the report.",
 ],
 "score": [
  "Calculate chronological age in years, months and days twice. The wrong age band produces a plausible but wrong profile and nobody downstream will notice.",
  "Hand-score your first protocols and have them checked before relying on Q-global or Q-interactive. Software prevents arithmetic errors, not transcription errors — a transposed raw score changes an index.",
  "Report every composite with its 95% confidence interval and percentile rank. A scaled score of 7 and an index of 85 are the same statement (one standard deviation below the mean); percentile rank is the clearest thing to give a school.",
  "Check subtest splits within each index against the critical values and base rates in the manual before you call anything a strength or weakness. A statistically significant difference can still be common in the standardisation sample.",
 ],
 "interpret": [
  "Ask both questions and do not confuse them: normative (how does this child compare with their age group?) and ipsative (how does this ability compare with the child's own average?). A flat low profile has no ipsative weaknesses and real normative ones.",
  "If the two subtests in an index diverge substantially, the index describes no coherent ability — report the subtest pattern and say the index is not interpretable. Where index scatter is large, consider GAI rather than FSIQ. The workbook's working rule — index scatter of 23 points or more (about 1.5 SD) makes FSIQ hard to interpret — is a heuristic from Flanagan and Kaufman (2004, Essentials of WISC-IV assessment), written for the WISC-IV; it is not a WISC-V manual rule, Pearson's position is that FSIQ can remain valid despite scatter, and GAI only helps when the scatter comes from Working Memory/Processing Speed rather than within the reasoning indices. Treat it as a prompt to think, confirm your service's practice, and always say in the report why you used GAI or FSIQ.",
  "Treat index and subtest patterns as hypotheses to corroborate with attainment, observation and history, not as findings in themselves. Independent bifactor re-analyses (Canivez et al., 2017) find the general factor carries most of the common variance, and subtest profile analysis has weak diagnostic support (Watkins, 2000). Pearson's position differs — know that the debate is live.",
  "Interpret the Verbal Comprehension Index in the light of language exposure. For a child with EAL or a short time in English-medium education, a low VCI is a statement about exposure, not verbal reasoning; the Non-verbal Index may be the fairer comparison, though no index is culture-free.",
  "State plainly what the WISC-V does not establish: it does not diagnose ADHD, autism, dyslexia or intellectual disability. Intellectual disability needs an adaptive measure (ABAS-3 or Vineland-3) and history alongside it. It contributes to a formulation and to recommendations at the right Continuum of Support level.",
 ],
 "errors": [
  "A reversal error — failing to reverse when the rule requires it changes the basal, the raw score and the index.",
  "Unpermitted queries or prompts that are not marked on the protocol.",
  "Reporting 'his IQ is 97' with no confidence interval or percentile.",
  "Reporting FSIQ from widely scattered indices, or switching to GAI without saying why.",
  "Using the wrong age band because the age calculation was not checked twice.",
 ],
 "read": [
  "Wechsler, D. (2016). WISC-V UK administration and scoring manual, and technical and interpretive manual. Pearson. — administration chapters first, then chapters 1–2 of the technical manual for the structure.",
  "Flanagan, D. P., & Alfonso, V. C. (2017). Essentials of WISC-V assessment. Wiley.",
  "Canivez, G. L., Watkins, M. W., & Dombrowski, S. C. (2017). Structural validity of the Wechsler Intelligence Scale for Children–Fifth Edition: Confirmatory factor analyses with the 16 primary and secondary subtests. Psychological Assessment, 29(4), 458–472.",
  "Watkins, M. W. (2000). Cognitive profile analysis: A shared professional myth. School Psychology Quarterly, 15(4), 465–479.",
 ],
},

# ---------------------------------------------------------------- Griffiths III
{
 "name": "Griffiths III",
 "before": [
  "Know who uses it. The Griffiths III (Green et al., 2016) covers birth to 6 years and in Ireland is usually administered by CDNT psychologists, early intervention teams and paediatric services — not by NEPS. Only accredited users trained on a recognised Griffiths course may administer it; check whether you hold that accreditation before you consider it, and in most cases you will not.",
  "What the EP usually does is read and use a Griffiths III report someone else wrote: to plan preschool or school entry, to inform an AIM application or a consultation with preschool staff, or to support a special class or special school application. Your task is translation and application, not re-testing.",
  "Know the five subscales before you read the report: A Foundations of Learning, B Language and Communication, C Eye and Hand Co-ordination, D Personal-Social-Emotional, E Gross Motor. The overall developmental quotient summarises them and can hide very uneven development.",
  "Check the date of the assessment and the child's age then. A profile from two years ago in a 3-year-old is a description of a different child; ask the family and setting what has changed since.",
 ],
 "administer": [
  "If you are not an accredited user, you do not administer it — say so plainly if a school or parent asks you to. What you can do is gather the information that sits beside it: developmental history, PHN and GP records, preschool staff consultation and structured play observation (Reference Part D, Early Years).",
  "If you shadow a CDNT colleague administering it, watch how play-based items are presented, how the parent is involved, and how the examiner decides the child is not engaging versus not able. Those judgements are where the reliability lives.",
  "Ask the family how typical the session was — sleep, illness, unfamiliar room, separation. Young children's performance on the day varies more than school-age children's.",
 ],
 "score": [
  "Scoring and conversion to developmental quotients, percentiles and age equivalents are done by the accredited administrator using the manual. Do not recalculate or re-derive scores from a report; if a number looks wrong, contact the author.",
  "When quoting from a Griffiths III report, quote the subscale results with the author's name, role and date, not only the overall quotient. Age equivalents are easy to misunderstand — prefer percentiles or plain descriptions when you pass them on.",
 ],
 "interpret": [
  "It is not an IQ test and not a diagnosis (tool catalogue). Say so to schools: a low Foundations of Learning score at 3 does not mean intellectual disability, and it does not predict a school-age cognitive score with any precision.",
  "Look at the shape across subscales. Delay across all five points to a global picture that the CDNT will be following; a dip only in Language and Communication with the rest in range points toward language and SLT; a Personal-Social-Emotional dip needs the social communication history.",
  "Translate each subscale into what the preschool or junior infant teacher will see and what they can do: e.g. Eye and Hand Co-ordination → scissors, pencil grip, dressing; link to OT advice already given. Recommendations go to Classroom Support or School Support level in the NEPS Continuum, or to AIM levels in preschool.",
  "Where you and the CDNT report differ, the difference is information — setting, time and demand differ. Raise it with the CDNT keyworker rather than writing a contradicting conclusion.",
 ],
 "errors": [
  "Administering it without accreditation, or being drawn into re-testing a child the CDNT has just assessed.",
  "Treating the overall developmental quotient as an IQ.",
  "Quoting an old Griffiths result as though it describes the child now.",
  "Passing on age equivalents without explanation to school staff.",
 ],
 "read": [
  "Green, E., Stroud, L., O'Connell, R., Bloomfield, S., Cronje, J., Foxcroft, C., Hunter, K., Lane, H., Marais, R., Marx, C., McAlinden, P., Paradice, R., & Venter, D. (2016). Griffiths Scales of Child Development (3rd ed.): Part I overview and Part II administration and scoring. Hogrefe. — check the author list against your copy.",
  "Frederickson, N., & Cline, T. (2015). Special educational needs, inclusion and diversity (3rd ed.). Open University Press. — the chapters on early identification.",
 ],
},

# ---------------------------------------------------------------- ASQ-3
{
 "name": "Ages & Stages Questionnaires (ASQ-3)",
 "before": [
  "Know what it is: a parent-completed developmental screen (Squires & Bricker, 2009) for children from 1 to 66 months, covering communication, gross motor, fine motor, problem solving and personal-social, plus open 'overall' questions. It is a screen, not an assessment (tool catalogue).",
  "Pick the right interval questionnaire for the child's age on the day it is completed. The manual gives the age window for each questionnaire and the rule for correcting for prematurity — check both; using the wrong interval makes the result meaningless.",
  "The ASQ-3 does not screen social-emotional development in depth. If behaviour, relating or regulation is the concern, the separate ASQ:SE-2 exists — check whether your service holds it and whether it is licensed for your use.",
  "Check your licence and language version. ASQ-3 is copyright material, and evidence for its accuracy varies by language version and context (Velikonja et al., 2017); for a family whose first language is not English, check which versions exist and whether an interpreter is needed.",
 ],
 "administer": [
  "Where possible have the parent try the activities with the child rather than answer from memory; the questionnaire is built for this. Some items need simple materials (blocks, a ball, paper) — have them ready.",
  "Offer to complete it with the parent rather than handing it over, especially where literacy or English is a question, and record that you did. Explain the three response options ('yes', 'sometimes', 'not yet') and that 'not yet' is expected for some items.",
  "Ask the preschool keyworker for their view alongside the parent's. The ASQ-3 can be completed by a childcare provider — check the manual on this — and a home–setting difference is useful information.",
 ],
 "score": [
  "Score each domain by adding item scores and compare the total with the cut-off and monitoring zone for that interval in the manual. Do not quote cut-off values from memory.",
  "Read the 'overall' section answers carefully — parental concern about hearing, vision, behaviour or regression is often more important than the domain totals, and must be followed up even if every domain is above cut-off.",
 ],
 "interpret": [
  "Three outcomes, three actions: above cut-off → share activities and rescreen as the manual advises; in the monitoring zone → practice activities and planned rescreen; below cut-off → refer for further assessment. Say which in your record.",
  "A below-cut-off result is a reason to refer, not a finding of delay. The route in Ireland is usually via the GP or PHN to Primary Care (SLT, OT, psychology) or to the CDNT; where a disability is suspected the family can apply for an Assessment of Need under the Disability Act 2005 — check current local pathways.",
  "A passing screen does not close a concern. If the parent, keyworker or your observation says something is wrong, act on that — screens miss children, and ASQ accuracy varies by version and context (Velikonja et al., 2017).",
  "Interpret in context: prematurity, illness, bilingual exposure and limited opportunity (e.g. no access to pencils or stairs) all lower item scores without indicating delay.",
 ],
 "errors": [
  "Using the wrong age-interval questionnaire, or not correcting for prematurity when the manual requires it.",
  "Reporting a below-cut-off score as 'developmental delay'.",
  "Ignoring the overall questions because the domain scores were fine.",
  "Handing the form to a parent with low literacy or limited English and treating their answers as valid.",
 ],
 "read": [
  "Squires, J., & Bricker, D. (2009). Ages & Stages Questionnaires (3rd ed.): User's guide. Paul H. Brookes. — the chapters on choosing intervals, scoring and follow-up.",
  "Velikonja, T., Edbrooke-Childs, J., Calderon, A., Sleed, M., Brown, A., & Deighton, J. (2017). The psychometric properties of the Ages & Stages Questionnaires for ages 2–2.5: A systematic review. Child: Care, Health and Development, 43(1), 1–17.",
 ],
},

# ---------------------------------------------------------------- Bayley-4
{
 "name": "Bayley-4",
 "before": [
  "Know who uses it. The Bayley-4 (Bayley & Aylward, 2019) covers 16 days to 42 months and is used mainly by paediatric and neonatal follow-up services, CDNT psychologists and early intervention teams. It is rarely administered by a trainee EP (tool catalogue); you will far more often read its results in a report.",
  "Know its structure so you can read the report: Cognitive, Language (receptive and expressive) and Motor (fine and gross) are administered directly to the child; Social-Emotional and Adaptive Behaviour come from caregiver questionnaires. Check the manual for exactly which subtests and composites your edition reports.",
  "Note whether the scores were corrected for prematurity and at what age the child was tested. Neonatal follow-up reports often use corrected age; if the report does not say, ask.",
  "Be clear with the family and setting about what it can and cannot do: it describes development now, and it predicts later cognitive ability poorly (Hack et al., 2005, with an earlier edition). A low score at 18 months is a description, not a forecast.",
 ],
 "administer": [
  "If you are not trained and supervised on it, you do not administer it. Your contribution is the context around it: developmental history, PHN records, preschool staff consultation and observation of the child in play.",
  "If you observe a colleague administer it, watch how the examiner balances standard presentation with keeping a toddler engaged, and how the parent's presence is managed. Note which items the child refused rather than failed — the report should distinguish them.",
  "Ask the family whether the session was typical. Tiredness, illness, separation and a strange room affect infant performance more than school-age performance.",
 ],
 "score": [
  "Scoring and norm conversion are done by the administering professional using the manual; the Bayley-4 changed item scoring from earlier editions — check the manual before comparing with a Bayley-III result.",
  "When you quote a Bayley-4 result, name the scale, the score type, the date and the author, and note whether age was corrected. Do not compare Bayley-III and Bayley-4 scores as though they were on one scale without checking the manual's guidance.",
 ],
 "interpret": [
  "Read it for pattern, not a single number. Delay confined to language points toward SLT and hearing checks; delay confined to motor points toward physiotherapy and OT; delay across cognitive, language and motor is a global picture that the CDNT will follow over time.",
  "Do not convert a Bayley-4 cognitive score into a statement about intelligence or intellectual disability. Diagnosis of intellectual disability is not made from an infant test, and predictive validity for later cognitive scores is limited (Hack et al., 2005).",
  "What the EP does with it: translate it into what preschool and school staff will see and can do, use it (with the family's consent) to plan AIM supports, school entry and Continuum of Support level, and flag when a school-age reassessment by the appropriate service is due.",
  "Where your observation and the Bayley-4 report disagree, treat that as information about setting and time. Discuss it with the CDNT keyworker before you write anything that contradicts it.",
 ],
 "errors": [
  "Treating a toddler's Bayley-4 cognitive score as an IQ or a prediction.",
  "Ignoring whether age was corrected for prematurity.",
  "Comparing Bayley-III and Bayley-4 scores directly without checking the manual.",
  "Offering to administer it without training and supervision on the instrument.",
 ],
 "read": [
  "Bayley, N., & Aylward, G. P. (2019). Bayley Scales of Infant and Toddler Development (4th ed.): Administration manual and technical manual. Pearson.",
  "Hack, M., Taylor, H. G., Drotar, D., Schluchter, M., Cartar, L., Wilson-Costello, D., Klein, N., Friedman, H., Mercuri-Minich, N., & Morrow, M. (2005). Poor predictive validity of the Bayley Scales of Infant Development for cognitive function of extremely low birth weight children at school age. Pediatrics, 116(2), 333–341.",
 ],
},

# ---------------------------------------------------------------- WPPSI-IV UK
{
 "name": "WPPSI-IV UK",
 "before": [
  "Check whether you need a cognitive test at this age at all. In early years NEPS involvement is usually consultation, not assessment (Reference Part D, Early Years). Use the WPPSI-IV where a specific decision (e.g. special class or school placement, a question of global delay) needs a standardised cognitive picture.",
  "Know the two age bands. WPPSI-IV UK runs 2:6–7:7 (Wechsler, 2013) and the battery differs for the younger band (2:6–3:11) and the older band (4:0–7:7); both bands yield a Full Scale IQ, but the younger band has three primary indices (Verbal Comprehension, Visual Spatial, Working Memory) and all five primary indices (adding Fluid Reasoning and Processing Speed) are available only in the older band. Check the manual for which subtests belong to each.",
  "At 6:0–7:7 it overlaps with the WISC-V UK. Choose deliberately: the WPPSI-IV has lower floors and more child-friendly materials; the WISC-V gives more ceiling for an able 7-year-old. Record why you chose.",
  "Plan for a young child: short attention, need for breaks, separation from a parent, toileting. Rule out hearing and vision problems and note language exposure before you begin.",
 ],
 "administer": [
  "Learn the start, reverse and discontinue rules for each subtest, as for the WISC-V. The WPPSI-IV adds more teaching items and manipulatives (e.g. Zoo Locations, Animal Coding, Bug Search) — practise handling the materials until you do not have to think about them.",
  "Engagement is part of standard procedure: praise effort, not correctness, and use the permitted encouragements in the manual. Breaks and splitting across two sessions may be needed — check what the manual allows and record what you did.",
  "Write behavioural observations throughout: separation, compliance, persistence after failure, language used, motor control. At this age these observations often matter more than the scores.",
 ],
 "score": [
  "Calculate age in years, months and days twice; the band and the norms depend on it. Hand-score early protocols and have them checked.",
  "Report composites with 95% confidence intervals and percentile ranks. Check subtest and index differences against the manual's critical values and base rates before calling anything a strength or weakness.",
 ],
 "interpret": [
  "Index scatter is less stable at this age than at school age — do not build a profile argument on it (tool catalogue; Reference Part D). Report the overall level and the behavioural picture; treat index differences as tentative.",
  "Scores in early childhood are less stable over time than at school age. Write findings as a description of the child now, and recommend review rather than implying a fixed level.",
  "For a child with EAL or limited preschool experience, verbal indices reflect exposure; the manual's non-verbal composite may be fairer, but say what it cannot tell you.",
  "Link findings to what preschool or junior infant staff can do, at the right Continuum of Support level. If global difficulties are suggested, add an adaptive measure (ABAS-3 or Vineland-3) and liaise with the CDNT rather than implying a diagnosis.",
 ],
 "errors": [
  "Building an index-profile argument for a 4-year-old.",
  "Using the older-band structure for a child under 4:0, or the wrong age band through a miscalculated age.",
  "Not recording breaks, split sessions or adaptations.",
  "Reporting scores without the behavioural observations that explain them.",
 ],
 "read": [
  "Wechsler, D. (2013). WPPSI-IV UK administration and scoring manual, and technical and interpretive manual. Pearson.",
  "Raiford, S. E., & Coalson, D. L. (2014). Essentials of WPPSI-IV assessment. Wiley.",
 ],
},

# ---------------------------------------------------------------- CELF-5 UK
{
 "name": "CELF-5 UK",
 "before": [
  "Know whose test it usually is. The CELF-5 UK (Wiig, Semel & Secord, 2017) is a speech and language therapist's instrument in Irish practice; in Part D it is listed as 'CELF-5 via SLT'. Check the publisher's user qualification level and your service's policy before you consider using it yourself.",
  "Most often you will read a CELF-5 report written by an SLT (Primary Care or CDNT). Know the structure so you can read it: a Core Language Score plus Receptive, Expressive and Language Content indexes, with Language Structure at ages 5–8 and Language Memory at ages 9–21 — check the manual for which subtests feed each at each age.",
  "Age range 5:0–21:11 (tool catalogue). Under 5, the CELF Preschool edition is the relevant SLT tool; check what your local SLT uses.",
  "Know what it cannot tell you: pragmatic language in real contexts (tool catalogue). The CELF-5 includes a Pragmatics Profile and observational rating scale, but these are informant or observation tools and need classroom observation beside them.",
 ],
 "administer": [
  "If you do administer any part, follow the script exactly: the stimuli are verbal and a changed word changes the item. Record verbatim responses for expressive subtests — they are scored on exact structure.",
  "Your usual role is to gather what the SLT does not see: classroom observation of oral participation, instruction-following and peer talk; teacher report; the child's own view of being understood (Reference Part D, School Age).",
  "Before requesting an SLT assessment, check hearing (audiology) and whether one has already been done — duplicate testing within a short interval contaminates both.",
 ],
 "score": [
  "Scoring and conversion are done from the manual tables; the scores that matter for decisions are the Core Language Score and index scores with confidence intervals. Do not quote cut-offs from memory — check the manual.",
  "When you cite an SLT's CELF-5 findings, quote the author, date and the index scores, and keep their wording for any diagnostic conclusion; do not restate it as your own.",
 ],
 "interpret": [
  "Language difficulty is identified by the SLT; the diagnostic framework in current use is Developmental Language Disorder (Bishop et al., 2017), which relies on functional impact and persistence, not a single test score. The EP does not diagnose DLD.",
  "Read the pattern across indices. Receptive weakness changes what the child can take from classroom talk; expressive weakness changes how they show what they know. Both have different classroom recommendations.",
  "Integrate with cognitive and attainment findings. A low WISC-V Verbal Comprehension Index alongside a low CELF-5 is not two findings — language is likely driving both. Reading comprehension difficulty with intact decoding often sits here too.",
  "Translate into Continuum of Support recommendations: vocabulary pre-teaching, visual support for instructions, checking understanding, and time to respond; name the SLT programme the school should implement.",
 ],
 "errors": [
  "Administering it without checking user qualification and service policy.",
  "Treating the CELF-5 as a measure of pragmatic or social communication.",
  "Reporting language and verbal cognitive scores as independent weaknesses.",
  "Referring to SLT without first checking hearing and existing assessments.",
 ],
 "read": [
  "Wiig, E. H., Semel, E., & Secord, W. A. (2017). Clinical Evaluation of Language Fundamentals (5th ed., UK). Pearson. — the examiner's manual and interpretation chapters.",
  "Bishop, D. V. M., Snowling, M. J., Thompson, P. A., Greenhalgh, T., & the CATALISE-2 consortium. (2017). Phase 2 of CATALISE: A multinational and multidisciplinary Delphi consensus study of problems with language development: Terminology. Journal of Child Psychology and Psychiatry, 58(10), 1068–1080.",
 ],
},

# ---------------------------------------------------------------- BPVS-3
{
 "name": "BPVS-3",
 "before": [
  "Know what it measures and nothing more: receptive vocabulary — the child hears a word and points to one of four pictures (Dunn et al., 2009). It does not measure expressive language, grammar or understanding of connected speech (tool catalogue).",
  "Age range 3:0–16:11 (tool catalogue). It is quick (about ten minutes) and has no spoken response, which makes it useful with shy, selectively mute or young children — but that does not make it a measure of general ability.",
  "It is heavily exposure-dependent. For a child with EAL or limited language-rich experience, a low score describes English vocabulary exposure, not capacity. Record language history before you use it.",
  "Decide what question it answers. It is a quick check on whether vocabulary is part of the picture, often before or alongside a request for SLT assessment, and pairs with an expressive vocabulary measure (Reference Part D lists EVT-3).",
 ],
 "administer": [
  "Use the start point for age and the basal and ceiling rules in the manual. Say the word exactly as scripted, once, without gesture or emphasis; do not use the word in a sentence.",
  "Watch for pointing without looking, impulsive responding and position bias (always the same corner). Note them — they affect how much you trust the score.",
  "Check hearing first. A child with a mild or fluctuating hearing loss can fail items for acoustic, not vocabulary, reasons.",
 ],
 "score": [
  "Raw score is the ceiling item minus errors — check the exact rule in the manual. Convert to a standard score and percentile with confidence interval using the age tables.",
  "Avoid reporting age equivalents to schools without explanation; they suggest a precision the test does not have and are easy to misread.",
 ],
 "interpret": [
  "A low BPVS-3 score says the child recognises fewer English words than age peers. It does not say why. Language exposure, DLD, hearing, attention and general learning difficulty are all possible — the other evidence decides.",
  "Compare it with the WISC-V Verbal Comprehension Index, CELF-5 findings if an SLT has assessed, and reading comprehension. Low vocabulary with intact decoding often explains poor reading comprehension.",
  "A score in the average range does not rule out language difficulty. Children with DLD may have adequate single-word vocabulary and still struggle with grammar and connected speech.",
  "Recommendations follow the finding at the right Continuum of Support level: explicit vocabulary teaching, pre-teaching topic words, and, where the pattern suggests more, a referral to SLT via Primary Care or the CDNT.",
 ],
 "errors": [
  "Reporting a BPVS-3 score as a measure of intelligence or general language.",
  "Using it with an EAL child and interpreting a low score as a difficulty.",
  "Treating an average score as ruling out language disorder.",
  "Not checking hearing before testing.",
 ],
 "read": [
  "Dunn, L. M., Dunn, D. M., Styles, B., & Sewell, J. (2009). The British Picture Vocabulary Scale (3rd ed.). GL Assessment. — manual, including the notes on EAL.",
  "Bishop, D. V. M., Snowling, M. J., Thompson, P. A., Greenhalgh, T., & the CATALISE-2 consortium. (2017). Phase 2 of CATALISE: A multinational and multidisciplinary Delphi consensus study of problems with language development: Terminology. Journal of Child Psychology and Psychiatry, 58(10), 1068–1080.",
 ],
},

# ---------------------------------------------------------------- Conners-4
{
 "name": "Conners-4",
 "before": [
  "Know the family of forms. Conners-4 (Conners, 2022) covers 6:0–18:11 with parent and teacher forms, and a self-report form from 8 (tool catalogue); for adolescents the self-report is part of the standard picture (Reference Part D, Adolescent). For 2–6 years the relevant instrument is Conners EC (Conners, 2009), parent and teacher/childcare forms — check the exact age range in its manual.",
  "Be clear what it is for: rating ADHD-related behaviour and its impact across settings. It does not diagnose ADHD (tool catalogue), and NICE (2018) guidance is that ADHD should not be diagnosed on rating scale or observation data alone. Diagnosis is made by CAMHS, paediatrics or psychiatry, not the EP.",
  "Choose full, short or index forms for the question, and check which your service holds and whether it is scored online. Check the manual for which scales each form yields.",
  "Plan for critical items. Check whether your version includes items on risk (for example self-harm or severe conduct) and decide beforehand what you will do if one is endorsed: same-day follow-up, your service's risk procedure and, where a child protection concern arises, Children First.",
 ],
 "administer": [
  "Give each rater clear instructions: the time frame the form specifies, rate what you see rather than what you think causes it, and there are no right answers. Ask teachers how long they have known the child — a teacher six weeks into the year is rating a stranger.",
  "Get at least one home and one school rater; add the self-report where age allows and read it with the young person's literacy in mind — offer to read items aloud and record that you did.",
  "Check for omissions and response style before the rater leaves or when the form comes back. The manual gives rules for too many omitted items and for response-style indicators — check them.",
 ],
 "score": [
  "Score each rater separately. Report T-scores with the manual's descriptive band and percentile, and translate into plain words — 'higher than most children of this age rated by teachers', not only a number.",
  "Look at the profile across scales and the impairment items, not only the ADHD index or total. Check your service's scoring software version against the manual.",
 ],
 "interpret": [
  "Parent–teacher disagreement is a finding, not a flaw (tool catalogue). Cross-informant agreement is typically modest (Achenbach et al., 1987; De Los Reyes et al., 2015), and the pattern tells you about setting demands and support.",
  "Consider the alternatives explicitly: anxiety, trauma, language disorder, learning difficulty, sleep problems, hearing, and a mismatch between demand and ability all raise attention and hyperactivity ratings. Say in the report what you considered and why.",
  "Integrate with classroom observation (momentary time sampling with a comparison peer), BRIEF-2, WISC-V Working Memory and Processing Speed and work samples (Reference Part D, School Age). A rating scale alone is informant perception.",
  "Write recommendations at the right Continuum of Support level and, where the picture warrants it, a referral to CAMHS or Primary Care/paediatrics via the GP with the family's consent. Do not advise on medication (PSI 2.2.2).",
 ],
 "errors": [
  "Writing that the Conners-4 'indicates ADHD'.",
  "Using Conners-4 with a 5-year-old instead of Conners EC.",
  "Leaving out the self-report for an adolescent.",
  "Missing an endorsed critical item because only the totals were read.",
  "Treating parent–teacher disagreement as one rater being wrong.",
 ],
 "read": [
  "Conners, C. K. (2022). Conners 4th Edition (Conners 4): Manual. Multi-Health Systems. — and Conners, C. K. (2009). Conners Early Childhood manual. Multi-Health Systems.",
  "National Institute for Health and Care Excellence. (2018, updated 2019). Attention deficit hyperactivity disorder: Diagnosis and management (NG87). NICE. — check for updates.",
  "De Los Reyes, A., Augenstein, T. M., Wang, M., Thomas, S. A., Drabick, D. A. G., Burgers, D. E., & Rabinowitz, J. (2015). The validity of the multi-informant approach to assessing child and adolescent mental health. Psychological Bulletin, 141(4), 858–900.",
 ],
},

# ---------------------------------------------------------------- BRIEF-2
{
 "name": "BRIEF-2",
 "before": [
  "Know what it measures: everyday executive function as seen by raters — inhibit, self-monitor, shift, emotional control, initiate, working memory, plan/organise, task-monitor, organisation of materials (Gioia et al., 2015). Check the manual for the exact scales and indexes on each form.",
  "Know the forms. Parent and teacher forms cover 5–18 (tool catalogue); a self-report form is available for adolescents — check the manual for its age range — and Part D lists BRIEF-2 self-report for the adolescent band. Below school age the BRIEF-P is the relevant version; for adults, BRIEF-A.",
  "Know what it cannot tell you: performance on executive tasks. Ratings and performance-based measures correlate weakly and can disagree while both are valid (Toplak et al., 2013; tool catalogue).",
  "Decide your raters: at least one parent and one teacher, and the young person where age allows. For post-primary, choose the subject teacher who sees the most relevant demands.",
 ],
 "administer": [
  "Instruct raters on the time frame in the manual, to rate behaviour they have seen, and to answer every item. Explain that items are about everyday behaviour, not ability.",
  "Check the validity scales when forms come back — the manual provides negativity, inconsistency and infrequency checks. An elevated negativity score changes how you read the whole form.",
  "For the self-report, read items aloud if literacy is a concern and record that you did. Ask the young person afterwards which items felt most true — the answers make good report quotes.",
 ],
 "score": [
  "Score each rater separately and check validity scales first. Report scale and index T-scores with percentiles and the manual's interpretive descriptors; do not quote elevation cut-offs from memory — check the manual.",
  "Look at the pattern across indexes (behaviour, emotion and cognitive regulation) and scales, not only the global composite. A global score can hide one scale driving everything.",
 ],
 "interpret": [
  "Elevated ratings say the child's everyday self-regulation is causing concern in that setting. They do not diagnose ADHD or any other condition; BRIEF-2 elevations are common across ADHD, autism, anxiety, trauma and acquired brain injury.",
  "Read home–school and adult–self differences as information about setting demands and insight. Adolescents often rate themselves lower than adults do — neither is automatically right.",
  "Pair it with a performance measure where the question needs it (Reference Part D lists TEA-Ch2 and WISC-V Working Memory) and with observation. Discrepancy between ratings and performance is common and should be explained, not ignored.",
  "Its best use is intervention planning: each elevated scale suggests a specific classroom or home strategy (e.g. plan/organise → task breakdown and visual schedules; shift → warning before transitions). Place these at the right Continuum of Support level.",
 ],
 "errors": [
  "Ignoring the validity scales.",
  "Reporting only the global composite.",
  "Treating an elevated BRIEF-2 as evidence of ADHD.",
  "Leaving out the self-report for an adolescent.",
  "Reading disagreement with a performance test as one measure being wrong.",
 ],
 "read": [
  "Gioia, G. A., Isquith, P. K., Guy, S. C., & Kenworthy, L. (2015). Behavior Rating Inventory of Executive Function (2nd ed.): Professional manual. PAR.",
  "Toplak, M. E., West, R. F., & Stanovich, K. E. (2013). Practitioner review: Do performance-based measures and ratings of executive function assess the same construct? Journal of Child Psychology and Psychiatry, 54(2), 131–143.",
 ],
},

# ---------------------------------------------------------------- SDQ
{
 "name": "SDQ",
 "before": [
  "Know what it is: a brief screen (Goodman, 1997) with five subscales — emotional symptoms, conduct problems, hyperactivity/inattention, peer relationship problems and prosocial behaviour — plus an impact supplement. It is free to use on paper from the official SDQ website but may not be altered; check the terms at sdqinfo.org.",
  "Choose the right version. Parent and teacher forms cover 4–17; a self-report form covers 11–17; a separate 2–4 version for parents and preschool staff exists (Reference Part D, Early Years) — check which items differ from the 4–17 version.",
  "Use the version with the impact supplement. It asks about overall difficulty, chronicity, distress, social impairment and burden (Goodman, 1999), and it carries more information than the scales (tool catalogue).",
  "Be clear what it is for: a general screen of emotional and behavioural difficulty. Where the referral is specific (e.g. attention, social communication, anxiety), use a focused instrument alongside it (Reference Part A, Behavioural and emotional rating scales).",
 ],
 "administer": [
  "Give it to at least one parent and one teacher, and to the young person from 11. For under-11s, get the child's view in conversation and quote it — the SDQ is not a substitute for the child's voice (CORU 2.3; UNCRC Article 12).",
  "Explain the response options and time frame on the form, and to rate what they see. Offer to go through it with parents where literacy or English is a concern, and record that you did.",
  "Use the official translated versions where needed — check sdqinfo.org for the language — rather than translating on the spot.",
 ],
 "score": [
  "Score by hand or with the official online scorer. Report subscale and total difficulties scores with the banding the source gives, and translate them into plain words. Do not quote band thresholds from memory — check the current scoring guidance, which differs by informant and version.",
  "Score the impact supplement separately and report it. A child with modest scale scores and high impact is a different child from one with high scores and no impact.",
 ],
 "interpret": [
  "Elevated means unusual relative to the norm group, not disordered. The SDQ does not diagnose anything (tool catalogue); say which band and what it means, and what you did next.",
  "Parent–teacher–self disagreement is information about setting and perspective (Achenbach et al., 1987; De Los Reyes et al., 2015). A child high at home and average at school may be holding it together all day.",
  "Read the item level and the impact supplement for risk and planning: which difficulties, in which settings, causing how much distress. Distress or impairment reported by the young person triggers a conversation, and any disclosure of self-harm or harm follows the same-day risk and child protection route.",
  "Use it to decide next steps within the NEPS Continuum of Support: consultation and a Classroom or School Support plan for most; School Support Plus with a focused assessment where scores and impact are high; referral to CAMHS or Primary Care via the GP where the picture suggests a mental health need, with the family's consent.",
 ],
 "errors": [
  "Using the 4–17 form for a 3-year-old instead of the 2–4 version.",
  "Using a version without the impact supplement, or not scoring it.",
  "Reporting a 'very high' band as though it were a diagnosis.",
  "Not getting the self-report for an adolescent.",
  "Missing an item or impact answer that signals distress because only the totals were read.",
 ],
 "read": [
  "Goodman, R. (1997). The Strengths and Difficulties Questionnaire: A research note. Journal of Child Psychology and Psychiatry, 38(5), 581–586. — and the current scoring guidance at sdqinfo.org.",
  "Goodman, R. (1999). The extended version of the Strengths and Difficulties Questionnaire as a guide to child psychiatric caseness and consequent burden. Journal of Child Psychology and Psychiatry, 40(5), 791–799.",
  "Achenbach, T. M., McConaughy, S. H., & Howell, C. T. (1987). Child/adolescent behavioral and emotional problems: Implications of cross-informant correlations for situational specificity. Psychological Bulletin, 101(2), 213–232.",
 ],
},
]
