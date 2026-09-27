"""CONDS records, batch c15: Sleep disorders (sleep–wake disorders); Somatic Symptom Disorder and Functional
Neurological (Conversion) Disorder; Premenstrual Dysphoric Disorder."""

CORU = "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32"
PSI = "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8"

CONDS = [
# ---------------------------------------------------------------------------------------------------------------
# 1. SLEEP DISORDERS
# ---------------------------------------------------------------------------------------------------------------
{
 "name": "Sleep disorders (sleep–wake disorders)",
 "code": "DSM-5-TR Sleep–Wake Disorders chapter (insomnia disorder, hypersomnolence disorder, narcolepsy, breathing-related sleep disorders incl. obstructive sleep apnoea hypopnoea, circadian rhythm sleep–wake disorders, NREM sleep arousal disorders, nightmare disorder, REM sleep behaviour disorder, restless legs syndrome) · ICD-11 Chapter 07 Sleep–wake disorders — check individual codes before quoting",
 "neps": "5. OTHER (5.3 Medical condition or other diagnosis) — and 1. LEARNING (1.1 Attention, concentration and work skills) where sleepiness presents as inattention",
 "coru": CORU,
 "psi": PSI,
 "law": "Children First Act 2015 · EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · Education (Welfare) Act 2000 · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "A FAMILY, not one condition. DSM-5-TR groups ten or so sleep–wake disorders: INSOMNIA DISORDER; HYPERSOMNOLENCE DISORDER; NARCOLEPSY; BREATHING-RELATED disorders (obstructive sleep apnoea hypopnoea, central apnoea, hypoventilation); CIRCADIAN RHYTHM disorders (including delayed sleep phase); PARASOMNIAS (NREM arousal disorders — sleepwalking and sleep terrors; nightmare disorder; REM sleep behaviour disorder); RESTLESS LEGS SYNDROME; and substance/medication-induced sleep disorder (APA, 2022). The sleep-medicine classification is ICSD-3 (American Academy of Sleep Medicine, 2014; text revision 2023 — check).",
  "INSOMNIA DISORDER: difficulty getting to sleep, staying asleep or waking too early, on at least three nights a week for at least three months, despite adequate opportunity, with daytime impairment (APA, 2022). In children DSM-5-TR allows this to show as bedtime resistance or being unable to sleep without a caregiver's intervention.",
  "DELAYED SLEEP PHASE in adolescence: puberty shifts the body clock later, so the teenager is biologically not sleepy until late and cannot wake easily for school (Carskadon, 2011; Crowley, Acebo & Carskadon, 2007). Add screens, homework and early starts and chronic short sleep follows. It is a biological shift before it is a discipline problem.",
  "OBSTRUCTIVE SLEEP APNOEA (OSA): repeated partial or complete blockage of the upper airway during sleep — in children most often from enlarged tonsils and adenoids, and more common with obesity, Down syndrome and craniofacial differences (Marcus et al., 2012). Signs: habitual loud snoring, witnessed pauses, gasping, mouth breathing, restless sweaty sleep. By day it can look like ADHD — inattention, hyperactivity, irritability — rather than sleepiness (Chervin et al., 2002).",
  "NARCOLEPSY: excessive daytime sleepiness with irresistible sleep attacks, sometimes with CATAPLEXY (sudden loss of muscle tone triggered by laughter or emotion), sleep paralysis and vivid hallucinations on falling asleep or waking. Onset is often in childhood or adolescence and diagnosis is frequently delayed by years — check before quoting a figure.",
  "Sleep is a FOUNDATION for learning, not a lifestyle extra. Short or poor-quality sleep is associated with poorer school performance (Dewald et al., 2010) and with worse attention, mood and behaviour. The EP's job is to ASK ABOUT SLEEP IN EVERY REFERRAL, describe its impact, give evidence-based advice at the level of habit and routine, and refer anything medical.",
  "Diagnosis of a sleep disorder is medical — GP, paediatrics, ENT, paediatric neurology or a sleep service, sometimes with a sleep study (polysomnography). The EP does not diagnose sleep disorders and does not advise on melatonin or other medication (PSI 2.2.2)."
 ],

 "what_it_is_not": [
  "NOT laziness. A teenager who cannot get up for school may have a delayed body clock (Carskadon, 2011) and is often genuinely unable to fall asleep earlier. Sanctions for lateness alone do not move a circadian rhythm.",
  "NOT always tiredness. Sleep-deprived children — especially younger ones — often look OVERACTIVE, irritable and inattentive rather than sleepy. Chervin et al. (2002) found snoring and sleep-disordered breathing symptoms associated with hyperactivity and inattention. A child sleeping six hours will screen positive on almost every behaviour scale.",
  "NOT fixed by melatonin as a first step. Behavioural approaches are the first line for most childhood sleep problems (Mindell et al., 2006), and melatonin is a medicine — prescription-only in Ireland (check current HPRA status) — so any decision about it belongs to the GP, paediatrician or psychiatrist, not the school or the EP.",
  "NOT just 'sleep hygiene'. Hygiene advice (routine, dark room, no screens) is sensible and low-risk, but on its own it is weak treatment for established insomnia; structured behavioural and CBT-based approaches have stronger evidence — check current reviews before quoting effect sizes.",
  "NOT caused solely by screens. Screen use is consistently associated with later bedtimes and shorter sleep (Hale & Guan, 2015), but the association is not all one-way — a young person who cannot sleep may pick up the phone. Address screens without making them the whole story.",
  "NOT harmless when it is 'only snoring'. Habitual loud snoring with pauses or gasping should go to the GP; the AAP guideline recommends screening children for snoring (Marcus et al., 2012).",
  "NOT a behaviour problem when it is a parasomnia. Sleepwalking and sleep terrors happen in partial arousal from deep sleep; the child is not awake and usually has no memory. Nightmares, in contrast, are remembered."
 ],

 "prevalence": [
  "OVERALL: sleep problems are among the most common concerns parents raise about children, but rates vary hugely by definition (parent-reported problem vs diagnosed disorder) — rate not stated here, check before quoting.",
  "OBSTRUCTIVE SLEEP APNOEA: commonly cited at roughly 1–5% of children (Marcus et al., 2012, AAP clinical practice guideline) — check before quoting; snoring alone is far more common.",
  "IRELAND: no Irish population figure stated here — check the Growing Up in Ireland study reports for sleep data before quoting.",
  "EARLY YEARS 0–5: bedtime resistance and night waking are the commonest parent concerns; most respond to behavioural approaches (Mindell et al., 2006). Parasomnias such as sleep terrors peak in the preschool and early school years.",
  "SCHOOL AGE 6–12: OSA peaks in the preschool and early primary years when tonsils and adenoids are relatively large (Marcus et al., 2012). Insomnia often sits beside anxiety.",
  "ADOLESCENT 13–16: circadian delay plus early school starts makes short sleep the norm rather than the exception in many samples (Carskadon, 2011) — specific rates not stated here, check.",
  "HIGHER RISK GROUPS: autistic children, children with ADHD, intellectual disability, cerebral palsy, epilepsy, Down syndrome (OSA), and children with anxiety or depression — sleep problems are markedly more common, rates not stated here, check (treatment trials in these groups include Gringras et al., 2017, autism; Hiscock et al., 2015, ADHD — neither is a prevalence study)."
 ],

 "cooccurring": [
  {"name": "ADHD", "rate": "very common and bidirectional — rate not stated here, check",
   "presents": "difficulty settling, late sleep onset, restless sleep; daytime inattention made worse by short sleep. Stimulant medication can delay sleep onset — a medical matter. Hiscock et al. (2015) showed a brief behavioural sleep intervention improved both sleep and ADHD symptoms."},
  {"name": "AUTISM", "rate": "very common — rate not stated here, check",
   "presents": "long sleep-onset latency, night waking, early waking, rigid bedtime routines, sensory sensitivities (light, noise, pyjamas). Poor sleep amplifies daytime distress and meltdowns."},
  {"name": "ANXIETY AND LOW MOOD", "rate": "very common — rate not stated here, check",
   "presents": "lying awake worrying, needing a parent to fall asleep, early waking in depression, or sleeping far more than usual. Insomnia can precede and predict depression; ask about mood and risk whenever sleep has changed."},
  {"name": "INTELLECTUAL DISABILITY AND GENETIC SYNDROMES", "rate": "elevated — rate not stated here, check",
   "presents": "persistent night waking and early waking; OSA is particularly common in Down syndrome, and some syndromes (e.g., Smith-Magenis) carry characteristic sleep disruption. Usually a CDNT and paediatric matter."},
  {"name": "EPILEPSY", "rate": "elevated — rate not stated here, check",
   "presents": "night-time events that may be seizures or parasomnias — only an EEG and medical assessment can tell them apart; sleep deprivation can also lower seizure threshold."},
  {"name": "EMOTIONALLY BASED SCHOOL AVOIDANCE", "rate": "commonly linked — rate not stated here, check",
   "presents": "late nights, a reversed sleep pattern and inability to get up in the morning, which becomes both a cause and a consequence of non-attendance."},
  {"name": "OBESITY AND CHRONIC ILLNESS", "rate": "elevated — rate not stated here, check",
   "presents": "OSA risk rises with obesity; pain, asthma, eczema and medications all disturb sleep. Medical review via GP."},
  {"name": "TRAUMA AND ADVERSITY", "rate": "elevated — rate not stated here, check",
   "presents": "nightmares, fear of the dark or of sleeping alone, hypervigilance at night. Ask what is happening at home and at night — including who else is in the house."}
 ],

 "recommendations": [
  "ASK ABOUT SLEEP IN EVERY REFERRAL. Bedtime, time asleep, night waking, snoring, morning waking, daytime sleepiness, screens in the bedroom. The BEARS prompts (Owens & Dalzell, 2005) are a quick structure: Bedtime problems, Excessive daytime sleepiness, Awakenings, Regularity and duration, Snoring.",
  "DESCRIBE THE IMPACT, NOT A DIAGNOSIS. Write what you found — e.g., 'Parent reports sleep onset after 23:30 on school nights and loud snoring most nights; teacher reports falling asleep in afternoon lessons' — and recommend medical review. Do not write 'has sleep apnoea' or 'has insomnia'.",
  "REFER — SNORING / PAUSES / GASPING: GP, who can refer to ENT or paediatrics for assessment of possible OSA. Say explicitly in the report that sleep-disordered breathing should be ruled out before attention or behaviour is attributed to anything else.",
  "REFER — EXCESSIVE DAYTIME SLEEPINESS, sleep attacks, collapse with laughter, sleep paralysis or hallucinations at sleep onset: GP for paediatric or neurology referral (possible narcolepsy). Record observations of falling asleep in class factually, with times.",
  "SLEEP ROUTINE ADVICE WITH EVIDENCE, for parents: consistent bedtime and wake time (including weekends, within an hour or so), a short predictable wind-down routine, a dark, quiet, cool room, screens out of the bedroom for the hour before sleep (Hale & Guan, 2015), caffeine avoided in the afternoon and evening, and daylight and activity in the morning. For bedtime resistance and night waking in young children, graduated extinction, bedtime fading and positive routines have the best evidence (Mindell et al., 2006).",
  "ADOLESCENTS: work WITH the circadian shift — anchor the wake time, get morning light, move the bedtime earlier gradually, keep weekend lie-ins modest, and move the phone out of the room at night. Consider whether homework volume and late activities are compressing sleep.",
  "IN SCHOOL: tell teachers when a pupil's attention or behaviour may be sleep-related, so it is not read as defiance; schedule demanding work earlier where a pupil is known to struggle in the afternoon (or later, for a delayed-phase teenager in first class); a flexible start as part of a return plan where medically advised.",
  "CONTINUUM LEVEL: Classroom Support for general advice; School Support where sleep is affecting learning or attendance; School Support Plus where medical services, CDNT or CAMHS are involved.",
  "WHERE A DISABILITY IS PRESENT: the CDNT (and public health nurse in early years) may already offer sleep support — check local arrangements and coordinate rather than duplicate.",
  "DO NOT recommend melatonin, sleeping tablets, antihistamines or supplements, or advise on the timing of ADHD medication. Those are medical decisions (PSI 2.2.2). You can say: 'That's a question for the GP or paediatrician.'"
 ],

 "explain_parent": [
  "'Sleep is the foundation everything else sits on. A child who's short of sleep will look distracted, irritable and overactive — and it can look a lot like ADHD. So before we go further I'd like to understand his sleep properly.'",
  "'The snoring you mentioned is worth taking to the GP. Loud snoring most nights, especially with pauses or gasping, can mean the airway is getting blocked at night — often from tonsils and adenoids — and that's treatable.'",
  "'Teenagers' body clocks genuinely shift later during puberty. She probably isn't sleepy at ten o'clock, and that's biology, not bad habits. What helps is a fixed wake-up time, bright light in the morning, and the phone out of the bedroom at night — and moving bedtime earlier bit by bit.'",
  "'The things that have the best evidence are simple and boring: the same bedtime and wake time every day, a short calm routine, a dark room, no screens in the last hour. I can give you a written plan.'",
  "'Melatonin is a medicine in Ireland, not a supplement, so that's a conversation for the GP or paediatrician. I'm not able to advise on it, but it's a reasonable question to bring to them.'",
  "SIGNPOST: GP first; HSE mychild.ie sleep information for young children; the CDNT or public health nurse where a disability is involved; for adolescents, reliable information on sleep and mental health from Jigsaw or SpunOut. Check links are current before giving them."
 ],

 "explain_teacher": [
  "'Some of what looks like inattention here may be sleep. A child who's been awake till midnight or whose breathing is disrupted at night can present as fidgety, irritable and unfocused rather than yawning.'",
  "'If he falls asleep in class, please note the time, the lesson and what happened just before — factually. That's useful for the doctor.'",
  "'Teenagers' body clocks run later. First class on a Monday is when a delayed-phase teenager is at her worst — if there's any flexibility, put the heavy thinking later.'",
  "'Please don't treat lateness from sleep problems purely as a discipline issue. It won't change the body clock and it adds stress, which makes sleep worse. Let's agree a plan with the family.'",
  "'Homework volume matters. If homework is running past eleven at night, that's worth reviewing — sleep lost to homework costs more learning than it gains.'",
  "'If a child says they're not sleeping because of what's happening at home, or they're frightened at night, that's a child protection conversation — go to the DLP the same day.'"
 ],

 "explain_child": [
  "YOUNGER: 'Sleep is when your brain tidies up and saves everything you learned today. If it doesn't get enough time, the next day feels harder and grumpier. Let's find out what bedtime is like for you.'",
  "OLDER: 'Your body clock moves later when you're a teenager — that's real science, not you being lazy. The trick is to pull it back a bit with a fixed wake-up time and light in the morning, and to keep the phone out of the room at night.'",
  "ASK: 'What time do you usually fall asleep on a school night? What wakes you up? Do you feel tired in school — which lessons?' Use a clock face or a timeline for younger children.",
  "ASK ABOUT THE NIGHT, SAFELY: 'Is there anything that makes it hard to sleep — worries, noise, anything at home?' Listen for fear, conflict, caring responsibilities or anything that suggests a child protection concern.",
  "ASK ABOUT MOOD: 'When you can't sleep, what goes through your head?' Racing worries, low mood or thoughts of not wanting to be here need to be followed up the same day.",
  "AVOID: 'just go to bed earlier' — they usually can't, and it signals you haven't understood."
 ],

 "analogies": [
  "THE PHONE ON 20%: 'He's starting every school day on 20% battery. He can still do things, but everything drains faster and he gets cranky trying.' Works with parents and teachers; explains why sleep-deprived children look irritable and overactive.",
  "THE JET-LAGGED TEENAGER: 'Every Monday she's flying in from a time zone two hours behind. The weekend lie-in puts her there.' Works with parents and adolescents; explains circadian delay and why weekend catch-up makes Mondays worse (Carskadon, 2011).",
  "THE SAVE BUTTON: 'Sleep is when the brain presses save on what it learned today. Skip the sleep and some of the day doesn't get saved.' Works with children and teachers; explains why sleep matters for learning.",
  "THE BLOCKED HOSE: 'At night, the tonsils can squeeze the airway like a foot on a garden hose. His body keeps half-waking to get air, so he never gets deep sleep — and he doesn't remember any of it.' Works with parents; explains OSA without jargon."
 ],

 "language": [
  "Use 'sleep difficulty' or 'short sleep' when describing without a diagnosis; use named disorders (e.g., 'obstructive sleep apnoea', 'narcolepsy') only when diagnosed by a doctor, and say who diagnosed.",
  "Avoid 'lazy', 'can't be bothered to get up', 'up all night on the phone' as explanations in reports. Describe the pattern (times, frequency, impact) and label interpretation as opinion (PSI 1.2.8).",
  "Avoid 'bad sleeper' as a fixed trait for young children — sleep patterns are highly changeable with routine and support.",
  "Talk to parents about sleep without blame. Many parents of children with ADHD or autism have been told to 'try a routine' repeatedly; acknowledge what they have already tried."
 ],

 "red_flags": [
  "RED FLAG — loud habitual snoring with witnessed pauses, gasping or choking at night, especially with daytime hyperactivity or inattention. GP referral for possible OSA before attention is formulated as ADHD.",
  "RED FLAG — sudden sleep attacks, falling asleep in class despite adequate night-time sleep, collapse or buckling knees with laughter, sleep paralysis or hallucinations at sleep onset. Possible narcolepsy — GP / paediatric neurology.",
  "RED FLAG — a recent marked change in sleep (not sleeping, or sleeping all day) alongside low mood, hopelessness, withdrawal or substance use. Ask directly about self-harm and suicidal thoughts; same-day risk route if present.",
  "RED FLAG — a child who is frightened to go to sleep, sleeps in unusual places, is kept up by adults' activity, or discloses anything suggesting abuse or neglect. Child protection route: DLP the same day and report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's own duty.",
  "RED FLAG — night-time events with stiffening, jerking, incontinence or tongue biting. Could be seizures rather than parasomnia — medical assessment.",
  "BOUNDARY — you do not diagnose sleep disorders or advise on melatonin, sleep medication, or ADHD medication timing (PSI 2.2.2). You ask, describe, give behavioural advice within your competence, and refer.",
  "WATCH — the tired, 'switched-off' adolescent. Circadian delay, depression, substance use, caring responsibilities and online life can all look like this. Ask rather than assume."
 ],

 "child_voice": [
  "A TWO-WEEK SLEEP DIARY completed with the young person (bedtime, lights out, time asleep, wakings, wake time, how they felt) — good because it replaces argument with data the young person owns, and shows patterns such as weekend drift.",
  "DAY-AND-NIGHT TIMELINE for younger children — a drawn clock or strip from 'getting home' to 'getting up', with the child adding what happens and how they feel. Good because it surfaces fears, noise, sharing a room or caring roles without a direct interrogation.",
  "SCALING: 'On a scale of 0 to 10, how tired are you in school most days? What would move it up one?' Good because it opens a solution-focused conversation about what the young person is willing to change.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — good because it locates the hardest times of day, which often line up with sleepiness. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "SLEEP MYTHS QUIZ with adolescents — true/false statements about sleep and body clocks. Good because it gives information without lecturing and respects their intelligence."
 ],

 "questions": [
  "Q: 'Could this be ADHD rather than sleep?' — A: 'It could be either, or both — they often come together. But poor sleep can produce exactly the same picture, so it's important to check sleep first. If sleep improves and the difficulties remain, that tells us something too.'",
  "Q: 'Should we try melatonin?' — A: 'Melatonin is a prescription medicine in Ireland, so that's a decision for the GP or paediatrician. What I can help with is the routine side, which is usually tried first and helps on its own for many children.'",
  "Q: 'He snores — is that a problem?' — A: 'Occasional snoring with a cold isn't. Loud snoring most nights, especially if you notice pauses or gasping, is worth a GP visit, because it can disrupt sleep enough to affect behaviour and learning.'",
  "Q: 'She's up till two on her phone — isn't that just her choice?' — A: 'Partly. But teenage body clocks genuinely run later, and the phone makes it worse. A fixed wake time, morning light and the phone out of the room overnight tend to work better than an earlier bedtime alone.'",
  "Q (teacher): 'He's always late — should we sanction him?' — A: 'If the lateness is driven by a sleep problem, sanctions add stress without fixing the cause. Let's agree a plan with home, and involve the GP if there's a medical question.'",
  "Q: 'Will he grow out of the sleepwalking?' — A: 'Many children do — it's common in younger children and often settles. Keep him safe at night and mention it to the GP, particularly if it's frequent, dangerous, or looks like it might be something else.'",
  "Q: 'We've tried everything — nothing works.' — A: 'That's a sign to go back to the GP or your CDNT for a proper assessment, not a sign that you've failed. Some sleep problems have a medical cause that routine alone won't fix.'"
 ],

 "supervision": [
  "Bring a case where attention or behaviour was the referral and sleep turned out to be significant. Ask how your supervisor weighs sleep before formulating attention difficulties.",
  "Clarify the local route for suspected OSA or narcolepsy: GP, paediatrics, ENT, sleep study — who accepts referrals and how long it takes (check locally).",
  "Discuss how to give sleep advice to a family who have been told 'try a routine' many times without it working — and when to stop advising and refer.",
  "Ask how the service handles melatonin questions from parents and schools, word for word, so you stay within PSI 2.2.2.",
  "Discuss a case where sleep disruption raised a child protection question, and how that was handled."
 ],

 "reflection": [
  "ON ASKING — did I ask about sleep in this referral? About snoring, not just bedtime? If not, my formulation may be missing its foundation.",
  "ON HOW I EXPLAINED IT — did the parent leave with a specific, written plan (times, routine, screens) or just 'improve sleep hygiene'?",
  "ON BLAME — did my advice sound like criticism of parenting? Did I acknowledge what the family had already tried?",
  "ON THE ADOLESCENT — did I explain circadian delay to the young person as biology, and involve them in the plan, or talk over them to the parent?",
  "ON MY ROLE — when melatonin came up, did I redirect clearly to the doctor, or drift into advising?",
  "WHAT GOOD LOOKS LIKE: 'Referral was for inattention in second class. I asked about sleep; mum said he snores loudly and she sometimes hears him stop breathing. I wrote that OSA should be ruled out by the GP before attention was formulated further, and gave the teacher strategies in the meantime. ENT review followed.'",
  "WHAT POOR LOOKS LIKE: 'Presents with inattention and hyperactivity; Conners elevated; recommend CAMHS referral for ADHD assessment.' — sleep never asked about."
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "American Academy of Sleep Medicine. (2014). International classification of sleep disorders (3rd ed.). American Academy of Sleep Medicine. — check for the current text revision.",
  "Carskadon, M. A. (2011). Sleep in adolescents: The perfect storm. Pediatric Clinics of North America, 58(3), 637–647.",
  "Chervin, R. D., Archbold, K. H., Dillon, J. E., Panahi, P., Pituch, K. J., Dahl, R. E., & Guilleminault, C. (2002). Inattention, hyperactivity, and symptoms of sleep-disordered breathing. Pediatrics, 109(3), 449–456.",
  "Marcus, C. L., Brooks, L. J., Draper, K. A., Gozal, D., Halbower, A. C., Jones, J., Schechter, M. S., Sheldon, S. H., Spruyt, K., Ward, S. D., Lehmann, C., & Shiffman, R. N. (2012). Diagnosis and management of childhood obstructive sleep apnea syndrome. Pediatrics, 130(3), 576–584.",
  "Mindell, J. A., Kuhn, B., Lewin, D. S., Meltzer, L. J., & Sadeh, A. (2006). Behavioral treatment of bedtime problems and night wakings in infants and young children. Sleep, 29(10), 1263–1276.",
  "Hiscock, H., Sciberras, E., Mensah, F., Gerner, B., Efron, D., Khano, S., & Oberklaid, F. (2015). Impact of a behavioural sleep intervention on symptoms and sleep in children with attention deficit hyperactivity disorder, and parental mental health: Randomised controlled trial. BMJ, 350, h68.",
  "Dewald, J. F., Meijer, A. M., Oort, F. J., Kerkhof, G. A., & Bögels, S. M. (2010). The influence of sleep quality, sleep duration and sleepiness on school performance in children and adolescents: A meta-analytic review. Sleep Medicine Reviews, 14(3), 179–189.",
  "Hale, L., & Guan, S. (2015). Screen time and sleep among school-aged children and adolescents: A systematic literature review. Sleep Medicine Reviews, 21, 50–58.",
  "Crowley, S. J., Acebo, C., & Carskadon, M. A. (2007). Sleep, circadian rhythms, and delayed phase in adolescence. Sleep Medicine, 8(6), 602–612.",
  "Gringras, P., Nir, T., Breddy, J., Frydman-Marom, A., & Findling, R. L. (2017). Efficacy and safety of pediatric prolonged-release melatonin for insomnia in children with autism spectrum disorder. Journal of the American Academy of Child & Adolescent Psychiatry, 56(11), 948–957.",
  "Owens, J. A., Spirito, A., & McGuinn, M. (2000). The Children's Sleep Habits Questionnaire (CSHQ): Psychometric properties of a survey instrument for school-aged children. Sleep, 23(8), 1043–1051.",
  "Owens, J. A., & Dalzell, V. (2005). Use of the 'BEARS' sleep screening tool in a pediatric residents' continuity clinic: A pilot study. Sleep Medicine, 6(1), 63–69."
 ],

 "pathway": {
  "age": "Any age. Bedtime resistance and night waking dominate early years; OSA peaks in the preschool and early primary years with tonsil and adenoid growth (Marcus et al., 2012); circadian delay and insomnia rise through adolescence (Carskadon, 2011); narcolepsy often begins in childhood or adolescence but is recognised late. In schools, sleep usually surfaces indirectly — through inattention, behaviour, lateness or attendance — and only if someone asks.",
  "who_diagnoses": "Ireland: GP as gateway; paediatrics, ENT (for suspected OSA), paediatric neurology or a paediatric sleep service for sleep studies and narcolepsy — availability varies, check locally. CDNT or public health nurse may provide sleep support (not usually diagnosis) where a disability is present. CAMHS where sleep sits within a mental health presentation. Any medication, including melatonin, is prescribed only by a doctor.",
  "who_wrote_report": "GP letter; paediatrician or ENT surgeon; sleep study (polysomnography or oximetry) report; neurologist; CDNT clinician (often OT, psychologist or nurse) describing sleep support; CAMHS clinician. A parent-completed sleep questionnaire (e.g., CSHQ) is a screen, not a diagnosis.",
  "refer_to": "GP first for snoring, pauses in breathing, excessive daytime sleepiness, suspected narcolepsy, restless legs or night-time events that could be seizures. CDNT where the child has a disability and is open to the team. CAMHS / Primary Care Psychology where sleep change sits with anxiety, depression or risk. Tusla where the night-time situation suggests neglect or abuse.",
  "sooner": "'Sleep problems are incredibly common and they hide behind other things — tiredness in children often looks like being wired or cross, not sleepy. Most families don't connect them, and many professionals don't ask. You're here now, and sleep is one of the more changeable things we'll look at.'"
 },

 "differential": [
  "ADHD — inattention and hyperactivity by day. Sleep deprivation and OSA can mimic it closely (Chervin et al., 2002). Rule sleep in or out before attention is attributed to ADHD; they also co-occur.",
  "DEPRESSION — early waking, insomnia or hypersomnia with low mood, loss of interest and fatigue. Ask about mood and risk whenever sleep has changed markedly.",
  "ANXIETY — worry at bedtime, needing a parent present, fear of the dark. Treating the anxiety often improves the sleep.",
  "EPILEPSY — nocturnal seizures can look like parasomnias. Medical assessment, sometimes with EEG.",
  "SUBSTANCES AND MEDICATION — caffeine and energy drinks, nicotine, cannabis, alcohol, stimulant medication and some other medicines disrupt sleep. Ask non-judgementally; medication questions go to the prescriber.",
  "LIFESTYLE AND CIRCUMSTANCE — late screens, long homework, part-time work, caring responsibilities, a crowded or noisy home, homelessness or emergency accommodation. Not a disorder, but it still matters, and some of it raises welfare questions."
 ],

 "next": [
  "Take a sleep history in every referral (BEARS headings); if any medical red flag is present, recommend GP review in writing and say why.",
  "Give the family a short written routine plan based on the evidence (Mindell et al., 2006; Hale & Guan, 2015), agreed with the young person where age allows.",
  "Tell the school what sleep may be contributing, and agree classroom adjustments at School Support level; review in six to eight weeks.",
  "If mood, risk or safeguarding concerns emerged, follow the same-day route first and inform your supervisor the same day."
 ],

 "presentations": [
  "Daytime sleepiness in class",
  "Late arrival and difficulty getting up for school",
  "Inattention possibly secondary to short sleep",
  "Bedtime resistance and night waking",
  "Snoring and disrupted night-time breathing",
  "Fatigue and stamina needs",
  "Night-time fears and nightmares"
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — bedtime resistance, night waking and parasomnias are common; OSA begins to peak.",
   "prevalence": "Common parent concern; OSA commonly cited around 1–5% of children (Marcus et al., 2012) — check before quoting.",
   "see": "Refusal to settle, repeated night waking, needing a parent to fall asleep, sleep terrors, and loud snoring. By day: irritability, overactivity and short attention that may be read as behaviour. Parent and public health nurse report is the main source; behavioural sleep approaches are first line (Mindell et al., 2006), with GP referral for snoring or pauses.",
   "tools": ["Children's Sleep Habits Questionnaire (CSHQ; Owens, Spirito & McGuinn, 2000) — AGE 4–10 · MEASURES: parent report of bedtime resistance, sleep onset, duration, anxiety, night waking, parasomnias, sleep-disordered breathing, daytime sleepiness · CANNOT TELL YOU: a diagnosis; OSA needs a sleep study · TIME: 10 min", "SDQ (2–4 version)"]
  },
  "School Age": {
   "applies": "YES — OSA and insomnia often surface as attention, behaviour or learning referrals.",
   "prevalence": "Rate not stated here for sleep disorders overall — check; OSA commonly cited around 1–5% of children (Marcus et al., 2012).",
   "see": "Inattention, fidgeting, irritability, falling asleep in afternoon lessons, lateness and headaches on waking. Snoring and mouth breathing point to OSA; worry at bedtime points to anxiety. Take a BEARS history, ask the teacher to note times of sleepiness, and refer medical features to the GP before formulating attention difficulties.",
   "tools": ["BEARS sleep screening prompts (Owens & Dalzell, 2005) — AGE 2–18 · MEASURES: structured interview headings: Bedtime, Excessive daytime sleepiness, Awakenings, Regularity/duration, Snoring · CANNOT TELL YOU: a diagnosis or severity · TIME: 5 min", "Children's Sleep Habits Questionnaire (CSHQ; Owens, Spirito & McGuinn, 2000) — AGE 4–10 · MEASURES: parent-reported sleep behaviours across eight subscales · CANNOT TELL YOU: a diagnosis · TIME: 10 min", "SDQ", "Conners-4", "BRIEF-2"]
  },
  "Adolescent": {
   "applies": "YES — circadian delay and insomnia are very common; narcolepsy may emerge.",
   "prevalence": "Short sleep on school nights is widespread in adolescent samples (Carskadon, 2011) — specific rates not stated here, check.",
   "see": "Cannot fall asleep before the early hours, cannot wake for school, sleeps late at weekends, lateness and first-period absence, falling grades. Phones and online life feed it. Sleepiness despite enough sleep, or collapse with laughter, suggests narcolepsy. Always ask about mood, substances and risk when sleep has changed.",
   "tools": ["BEARS sleep screening prompts (Owens & Dalzell, 2005) — AGE 2–18 · MEASURES: structured interview headings · CANNOT TELL YOU: a diagnosis · TIME: 5 min", "Two-week sleep diary — AGE any · MEASURES: bedtime, sleep onset, wakings, wake time, weekday–weekend drift · CANNOT TELL YOU: sleep quality or breathing · TIME: 2 min a day", "RCADS self-report", "MFQ (Mood and Feelings Questionnaire)"]
  },
  "Young Adult": {
   "applies": "YES — sleep problems continue into further education and work; usually adult GP territory.",
   "prevalence": "Rate not stated here — check before quoting.",
   "see": "Irregular schedules in college, part-time night work, insomnia with anxiety or low mood, and narcolepsy sometimes first recognised here. The EP role is recognising sleep's contribution to learning and mood, advising on routine, and signposting to the GP, college health services and disability support where relevant.",
   "tools": ["Adult self-report measures via the service", "Two-week sleep diary — AGE any · MEASURES: sleep timing and regularity · CANNOT TELL YOU: a diagnosis · TIME: 2 min a day"]
  },
  "Special Setting": {
   "applies": "YES — sleep problems are markedly more common in autism, intellectual disability and many genetic and neurological conditions.",
   "prevalence": "Elevated — rate not stated here, check (Gringras et al., 2017 is a melatonin treatment trial in autism, not a prevalence source).",
   "see": "Long settling times, frequent or prolonged night waking, very early waking, and daytime distress or self-injury that fluctuate with sleep. OSA is common in Down syndrome. Staff and parent sleep diaries alongside behaviour records often show the link. Coordinate with the CDNT and paediatrician; melatonin and medication decisions are medical.",
   "tools": ["Children's Sleep Habits Questionnaire (CSHQ; Owens, Spirito & McGuinn, 2000) — AGE 4–10 (used more widely in research — check) · MEASURES: parent-reported sleep behaviours · CANNOT TELL YOU: a diagnosis · TIME: 10 min", "Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3"]
  }
 }
},

# ---------------------------------------------------------------------------------------------------------------
# 2. SOMATIC SYMPTOM DISORDER AND FUNCTIONAL NEUROLOGICAL (CONVERSION) DISORDER
# ---------------------------------------------------------------------------------------------------------------
{
 "name": "Somatic Symptom Disorder and Functional Neurological (Conversion) Disorder",
 "code": "DSM-5-TR Somatic Symptom and Related Disorders chapter: Somatic Symptom Disorder · Functional Neurological Symptom Disorder (Conversion Disorder) · Illness Anxiety Disorder · ICD-11 6C20 Bodily distress disorder · ICD-11 6B60 Dissociative neurological symptom disorder (FND sits in the dissociative block in ICD-11) — check codes before quoting",
 "neps": "5. OTHER (5.3 Medical condition or other diagnosis) — and 3. EMOTIONAL (3.2 Anxiety · 3.6 School attendance) where relevant",
 "coru": CORU,
 "psi": PSI,
 "law": "Children First Act 2015 · Education (Welfare) Act 2000 · EPSEN Act 2004 · Disability Act 2005 · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "SOMATIC SYMPTOM DISORDER (SSD): one or more physical symptoms that are distressing or disrupt daily life, PLUS excessive thoughts, feelings or behaviours about them — persistent worry about seriousness, high health anxiety, or a great deal of time and energy devoted to them — typically lasting more than six months (APA, 2022). Crucially, DSM-5 dropped the requirement that symptoms be 'medically unexplained': SSD can sit alongside a diagnosed medical illness.",
  "FUNCTIONAL NEUROLOGICAL SYMPTOM DISORDER (FND; conversion disorder): symptoms of altered movement or sensation — weakness, paralysis, tremor, jerks, gait disturbance, non-epileptic (functional/dissociative) seizures, loss of speech, sensory loss, visual symptoms — where clinical findings show the symptoms are INCOMPATIBLE with recognised neurological disease (APA, 2022). Diagnosis is made by a doctor on POSITIVE clinical signs (e.g., Hoover's sign for functional weakness), not simply by exclusion (Espay et al., 2018).",
  "The symptoms are REAL and NOT INTENTIONAL. The young person is not pretending, and cannot switch the symptoms off by effort. A useful framing is a problem with the brain's 'software' — how it controls and perceives the body — rather than its 'hardware' structure (Stone, 2016; neurosymptoms.org).",
  "DSM-5 removed the old requirement to identify a preceding psychological stressor for FND. Stress, anxiety, adversity, pain, injury or illness can be PREDISPOSING, PRECIPITATING or PERPETUATING factors, but many young people have none obvious, and hunting for a 'hidden trauma' can damage trust (Espay et al., 2018).",
  "In children and adolescents, functional abdominal pain, headaches, fatigue, dizziness and functional seizures are among the commonest presentations, often after a minor illness or injury, and often in conscientious, high-achieving young people — check before generalising (Kozlowska et al., 2007; Eminson, 2007).",
  "Treatment is led by paediatrics / neurology and typically involves a clear, confident explanation of the diagnosis, then multidisciplinary rehabilitation — physiotherapy, psychological therapy (often CBT-informed), and a graded return to normal activity including school. The explanation itself is part of the treatment (Stone, 2016).",
  "For the EP: MEDICAL ASSESSMENT FIRST, always — the EP does not diagnose SSD or FND. Once a diagnosis is made, the EP's role is to help school understand it, plan a school return that builds function, reduce the maintaining factors in school, and support the young person's wellbeing — in step with the treating team."
 ],

 "what_it_is_not": [
  "NOT 'put on', faking or attention-seeking. Symptoms are experienced as genuinely as any other illness. Deliberately feigned symptoms are a different thing (factitious disorder, malingering) and are not what FND or SSD describe (APA, 2022).",
  "NOT 'all in the head' in the dismissive sense. FND is a disorder of brain functioning — the neurology is involved even when scans are normal (Espay et al., 2018). Telling a family 'it's psychological' or 'psychosomatic' is usually heard as 'we don't believe you', and damages engagement.",
  "NOT a diagnosis of exclusion made because tests were normal. Doctors now diagnose FND on positive signs. And normal tests alone do not make something functional — so the EP never draws that conclusion.",
  "NOT always caused by trauma or abuse. Adversity is a risk factor for some young people, not a universal cause. Assuming trauma is inaccurate and can be harmful; ASKING about safety, as you would for any child, is right.",
  "NOT the same as fabricated or induced illness (FII). FII is a child protection concern where a carer fabricates or induces illness in a child. It is handled through the child protection route (DLP, Tusla), not by EP speculation. Most families of children with functional symptoms are worried, not fabricating.",
  "NOT managed by waiting until symptoms go before returning to school. Prolonged absence and rest tend to maintain disability; graded return to normal routine is part of recovery — planned with the treating team.",
  "NOT the same as chronic fatigue syndrome / ME, long COVID or chronic pain conditions, which have their own medical frameworks and debates. Don't relabel a medically diagnosed condition as functional."
 ],

 "prevalence": [
  "OVERALL: recurrent physical symptoms without full medical explanation (e.g., abdominal pain, headache) are common in childhood; full SSD or FND is much less common — rates not stated here, check before quoting.",
  "PAEDIATRIC FND: reported as uncommon but significant in paediatric neurology practice (Kozlowska et al., 2007, Australian surveillance data) — rate not stated here, check before quoting.",
  "IRELAND: no Irish paediatric figure stated here — check.",
  "EARLY YEARS 0–5: functional neurological symptoms are rare at this age; recurrent tummy aches and headaches as expressions of distress are more usual.",
  "SCHOOL AGE 6–12: recurrent abdominal pain and headaches common; FND becomes more frequent towards the end of primary.",
  "ADOLESCENT 13–16: FND, functional seizures and SSD most often present in adolescence — check before quoting a peak age.",
  "SEX RATIO: FND is reported more often in girls than boys from adolescence onward (Kozlowska et al., 2007) — check before quoting a ratio."
 ],

 "cooccurring": [
  {"name": "ANXIETY DISORDERS", "rate": "common — rate not stated here, check",
   "presents": "worry about the symptoms themselves, school anxiety, health anxiety and perfectionism. Anxiety may be a perpetuating factor or an understandable response to frightening symptoms — do not assume it is the cause."},
  {"name": "DEPRESSION / LOW MOOD", "rate": "common — rate not stated here, check",
   "presents": "loss of activities, friends and school through the symptoms, leading to low mood and hopelessness. Ask about mood and risk directly."},
  {"name": "EMOTIONALLY BASED SCHOOL AVOIDANCE", "rate": "commonly linked — rate not stated here, check",
   "presents": "absence that begins with genuine symptoms and becomes maintained by fear of relapse, falling behind and the difficulty of returning. Needs a joint medical–school return plan."},
  {"name": "AUTISM", "rate": "reported as elevated — rate not stated here, check",
   "presents": "sensory and interoceptive differences, difficulty describing internal states, and high stress in school that may show through the body. Adjust explanation and assessment accordingly."},
  {"name": "GENUINE MEDICAL CONDITIONS, INCLUDING EPILEPSY", "rate": "recognised overlap — rate not stated here, check",
   "presents": "a young person with epilepsy may also have functional seizures; a young person with a gut condition may also have functional pain. The treating doctors distinguish them; the school plan must cover both."},
  {"name": "ADVERSITY, BULLYING OR TRAUMA", "rate": "elevated in some samples — rate not stated here, check",
   "presents": "symptoms that began around a period of stress, loss, bullying or harm. Ask about safety as with any child; follow the child protection route if anything is disclosed."},
  {"name": "SELF-HARM AND SUICIDAL IDEATION", "rate": "elevated in some samples — rate not stated here, check",
   "presents": "hopelessness about recovery and being disbelieved. Ask directly; same-day risk route if present."}
 ],

 "recommendations": [
  "MEDICAL ASSESSMENT FIRST. Where physical symptoms have not been assessed, the first recommendation is GP review — in writing. The EP never concludes that a symptom is functional or 'stress-related'.",
  "WORK FROM THE DIAGNOSIS THE DOCTORS HAVE GIVEN, in their words. Ask the family's permission to liaise with the paediatrician, neurologist or paediatric liaison mental health team, so the school plan matches the medical plan and the messages are consistent.",
  "A WRITTEN SCHOOL RETURN / PARTICIPATION PLAN, agreed with family, young person and treating team: a graded timetable that builds up on a planned schedule rather than 'come in when you feel well'; a named key adult; a quiet space; agreed rest breaks that are scheduled rather than symptom-triggered where the team advises this.",
  "AN AGREED SYMPTOM RESPONSE PLAN — e.g., for a functional seizure: calm, keep safe, time it, no crowding, no emergency call unless the plan says so (the treating team decides the criteria), return to class afterwards if possible. Everyone responds the same way, calmly, without drama or dismissal. Where epilepsy co-exists, the medical seizure plan takes precedence.",
  "REDUCE SCHOOL-BASED MAINTAINING FACTORS: academic pressure, perfectionism, workload catch-up after absence, bullying, exam stress. Negotiate curriculum and homework reduction for a defined period.",
  "PHYSICAL ACCESS AND SAFETY: temporary adjustments for mobility, lifts, seating, PE participation guided by the physiotherapist — and a plan for withdrawing them as function returns.",
  "SUPPORT PSYCHOLOGICAL TREATMENT, don't replace it: the therapy is the treating team's; the EP helps school apply the same approach (e.g., distraction and grounding strategies agreed by the therapist).",
  "CONTINUUM LEVEL: School Support Plus, with coordination between school, paediatrics/neurology, liaison psychiatry or CAMHS, and the family. Consider home tuition or hospital school only as a bridge, with an end point, where the treating team advises.",
  "ATTENDANCE: record carefully; Tusla Education Support Service (TESS) involvement where absence is prolonged — framed supportively, not punitively (check local practice).",
  "DO NOT use 'psychosomatic', 'hysterical', 'all in the head' or 'attention-seeking' in reports or meetings; do not speculate about causes (e.g., trauma) in writing; do not advise on medication or physical treatment."
 ],

 "explain_parent": [
  "'Everyone here believes the symptoms are real. She isn't putting them on, and she can't just switch them off.'",
  "'From what the neurologist said, the way I'd put it is that the hardware — the structure of the brain and nerves — is fine, but the software that controls movement and feeling isn't running properly. That's what functional means. And software problems can improve with the right retraining.'",
  "'Stress can make these symptoms worse, the way it makes headaches worse, but that doesn't mean she's causing them or that it's \"just stress\". Many young people with this have no big stress behind it at all.'",
  "'The research and the doctors agree that getting back to normal life, step by step, is part of getting better. So school's plan will build her back up gradually, in line with what the physio and doctors advise — not all at once, and not waiting until every symptom has gone.'",
  "'I'm not a doctor and I'm not making any medical judgement — I'll work with her doctors so school does the same things they're recommending.'",
  "SIGNPOST: the treating paediatrician or neurologist; neurosymptoms.org (a free patient information site on functional symptoms written by a neurologist); FND Hope and other FND charities — check for current Irish organisations and links before giving them."
 ],

 "explain_teacher": [
  "'The symptoms are real and involuntary. Please don't ask her to prove it or \"try harder\" — and please don't hint that it's put on. That makes it worse.'",
  "'The doctors have ruled in a functional disorder — it's a real problem with how the brain controls the body, and it's treatable. Our part is to help her get back to normal routines steadily.'",
  "'If an episode happens in class: stay calm, keep her safe, follow the plan. Don't crowd her, don't make a drama, and don't ignore her. When it's over, a quiet return to the lesson if she can.'",
  "'Try to keep attention on what she's DOING — the work, the conversation — rather than on the symptoms. Lots of questions about how she's feeling can keep the brain focused on the body.'",
  "'Please help the class respond kindly and calmly. Speculation and gossip among peers are a real risk; agree with her and her family what, if anything, the class is told.'",
  "'Her workload needs to be reduced for now. Catch-up pressure after absence is one of the biggest barriers to return.'"
 ],

 "explain_child": [
  "YOUNGER: 'Your tummy pains are real — nobody thinks you're making them up. Sometimes our bodies send pain signals even when nothing is broken, a bit like a smoke alarm going off when there's toast, not fire. Your doctor is helping, and school is going to help too.'",
  "OLDER: 'Functional means the connection between your brain and body isn't working properly, even though nothing's damaged. It's real, it's not your fault, and people do get better — usually by slowly doing more of their normal life with the right support.'",
  "ASK: 'What's the hardest part of school at the moment? What would make coming in easier? What's one thing you'd like to get back to?'",
  "ASK ABOUT WHAT PEOPLE SAY: 'Has anyone said anything that made you feel they didn't believe you?' — being disbelieved is common and very distressing.",
  "ASK ABOUT MOOD AND SAFETY as with any young person: 'Sometimes when things are this hard people feel really low or have thoughts of hurting themselves — has that happened for you?'",
  "AVOID: 'it's just stress', 'try not to think about it', 'you seemed fine at break'."
 ],

 "analogies": [
  "HARDWARE AND SOFTWARE: 'The computer isn't broken — the hardware's fine — but the software's glitching. You fix software differently from hardware.' Widely used in FND explanation (Stone, 2016; neurosymptoms.org); works with parents, teachers and adolescents.",
  "THE SMOKE ALARM: 'The alarm's going off even though there's only toast, not a fire. The alarm is real and loud. We're helping it recalibrate.' Works with children and parents for functional pain.",
  "THE PIANIST WHO FREEZES: 'A pianist can play a piece perfectly for years and then, one day, the fingers won't do it — nothing's wrong with the hands.' Works with teachers and older adolescents; explains involuntary loss of an automatic skill.",
  "THE WELL-WORN PATH: 'The brain has got into a habit of sending signals down one path. Rehab is about wearing a new path, one step at a time, which is why doing normal things gradually matters.' Works with families; explains graded return."
 ],

 "language": [
  "Use 'functional neurological disorder (FND)', 'functional seizures' or 'functional symptoms' — the terms the treating team uses. Many patients and clinicians now prefer 'functional' over 'conversion', 'pseudo-seizures', 'psychogenic' or 'non-epileptic attack disorder' — check the treating team's preferred term and use it.",
  "Avoid: 'psychosomatic', 'hysterical', 'all in the head', 'put on', 'attention-seeking', 'medically unexplained' (implies no one knows what it is) and 'pseudo-seizures' (implies fake).",
  "Describe observations factually in reports ('on three occasions she was unable to weight-bear in the corridor') and label interpretation as opinion (PSI 1.2.8). Never write a causal hypothesis (e.g., 'secondary to stress at home') without evidence and without the treating team's formulation.",
  "Use the young person's own words for their symptoms; ask them how they would like staff and peers to talk about it."
 ],

 "red_flags": [
  "RED FLAG — any new, worsening or changing physical symptom that has not been assessed medically. GP or treating team first; do not assume it is part of the known functional picture.",
  "RED FLAG — hopelessness, withdrawal, self-harm or suicidal ideation. Ask directly; same-day risk route: supervisor informed the same day, parents informed unless that would increase risk, GP/CAMHS contacted, ED if imminent.",
  "RED FLAG — any disclosure or indicator of abuse or neglect. Child protection route: DLP the same day and report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's own duty.",
  "RED FLAG — concern that illness may be fabricated or induced by a carer. Do not investigate or confront; record factually and follow the child protection route with your supervisor the same day.",
  "BOUNDARY — you do not diagnose SSD or FND, judge whether symptoms are 'real' or 'functional', or advise on medication or physical rehabilitation (PSI 2.2.2). You describe, liaise, plan the school side and refer.",
  "WATCH — the conscientious, high-achieving young person whose symptoms escalate around exams or transitions. Pressure may be a perpetuating factor — handle this with the treating team, not as an accusation.",
  "WATCH — staff or peers who have begun to say 'she's doing it for attention'. Address it quickly; disbelief worsens outcomes and can become bullying."
 ],

 "child_voice": [
  "SOLUTION-FOCUSED PUPIL INTERVIEW with scaling on 'how much of normal school life are you doing now?' — good because it keeps the focus on function and goals rather than symptoms, and gives the young person ownership of the return plan.",
  "'MY SCHOOL DAY' MAP — the young person colours parts of the day by how manageable they feel. Good because it locates pressure points (a subject, a corridor, a peer group) for the graded plan.",
  "A 'WHAT I WANT STAFF TO KNOW' ONE-PAGE PROFILE written with the young person — good because it lets them decide what is shared, reduces repeated explanation, and tells staff how to respond to an episode.",
  "GOAL LADDER for return — steps from 'what I can do now' to 'where I want to be', agreed with the physio and therapist. Good because it makes progress visible and puts the young person in charge of the pace, within the plan.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — good because it surfaces school-based stressors in a familiar format. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/"
 ],

 "questions": [
  "Q: 'So you think she's making it up?' — A: 'No. Nobody thinks that. The symptoms are real and she can't control them. My job is to help school support her recovery in the way her doctors recommend.'",
  "Q: 'The scans were all clear — so why can't he walk?' — A: 'The scans look at the structure, and that's fine. Functional disorders are about how the brain is sending and receiving signals, which scans don't show. The neurologist diagnosed it from specific signs — it's a real, recognised condition.'",
  "Q: 'Is it caused by something that happened to her?' — A: 'Sometimes stress or difficult experiences play a part, and sometimes there's nothing obvious at all. I wouldn't assume either way. If there's something worrying her, we'd want to know — but we're not looking for a hidden cause to blame.'",
  "Q: 'Shouldn't she stay home until it's better?' — A: 'Her doctors will guide this, but in general, staying away for a long time tends to make recovery harder. A careful, gradual return, with the school ready to respond calmly, is usually part of getting better.'",
  "Q (teacher): 'What do I do if she has a seizure in class?' — A: 'Follow the plan we've agreed with her doctors: keep her safe, stay calm, time it, give her space, and don't crowd or fuss. The plan says when to call for help. Afterwards, a quiet return if she's able.'",
  "Q (teacher): 'She seemed fine at lunch and then collapsed in maths — isn't that suspicious?' — A: 'Functional symptoms often fluctuate and can be more likely in some situations than others. That's part of the condition, not evidence she's choosing it. It's also useful information for the plan.'",
  "Q: 'Is this a psychological problem, then?' — A: 'It's best thought of as a brain-and-body problem. Psychology is often part of the treatment, the same way physio is — not because it's imaginary, but because the brain can learn to work differently.'"
 ],

 "supervision": [
  "Rehearse how you explain FND or SSD to a family who feel disbelieved — word for word, without 'psychosomatic' language.",
  "Discuss how to liaise with the treating team: consent, who to contact, and how to make sure school's messages match theirs.",
  "Bring any case where staff attitudes ('she's putting it on') have become a barrier, and plan how to address it.",
  "Discuss the boundary between curiosity about stressors and speculation about causes — what goes in a report and what doesn't.",
  "Discuss the difference between FND and FII, and exactly what you would do if a fabrication concern arose."
 ],

 "reflection": [
  "ON HOW I EXPLAINED IT — did the family leave feeling believed? Did I use the treating team's words, or introduce my own?",
  "ON MEDICAL FIRST — was every physical symptom I wrote about medically assessed? Did I resist concluding anything was 'functional'?",
  "ON CAUSES — did I speculate about trauma or family stress, in the meeting or in writing, without evidence? What would the family feel reading my report?",
  "ON THE RETURN PLAN — was it built on steady, planned increases, or on 'come in when you feel better'? Did the young person help design it?",
  "ON STAFF ATTITUDES — did I challenge disbelief in the staffroom, or let it pass?",
  "WHAT GOOD LOOKS LIKE: 'The neurologist had diagnosed functional seizures. I met the family, used the software explanation from the clinic letter, and we built a six-week return plan with the physio's input and a calm seizure-response protocol. Staff briefing addressed \"attention-seeking\" head on. Attendance rose steadily and episodes in school reduced.'",
  "WHAT POOR LOOKS LIKE: 'Presentation likely psychosomatic, related to anxiety about exams; recommend counselling.' — no medical diagnosis confirmed, pejorative language, speculative cause, no school plan."
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "Espay, A. J., Aybek, S., Carson, A., Edwards, M. J., Goldstein, L. H., Hallett, M., LaFaver, K., LaFrance, W. C., Jr., Lang, A. E., Nicholson, T., Nielsen, G., Reuber, M., Voon, V., Stone, J., & Morgante, F. (2018). Current concepts in diagnosis and treatment of functional neurological disorders. JAMA Neurology, 75(9), 1132–1141.",
  "Stone, J. (2016). Functional neurological disorders: The neurological assessment as treatment. Practical Neurology, 16(1), 7–17.",
  "Kozlowska, K., Nunn, K. P., Rose, D., Morris, A., Ouvrier, R. A., & Varghese, J. (2007). Conversion disorder in Australian pediatric practice. Journal of the American Academy of Child & Adolescent Psychiatry, 46(1), 68–75.",
  "Eminson, D. M. (2007). Medically unexplained symptoms in children and adolescents. Clinical Psychology Review, 27(7), 855–871.",
  "World Health Organization. (2019/2022). International classification of diseases (11th rev.). https://icd.who.int/ — check codes 6C20 and 6B60 in the browser before quoting.",
  "Stone, J. (n.d.). Functional neurological disorder: A patient's guide. https://neurosymptoms.org/ — check for updates."
 ],

 "pathway": {
  "age": "Recurrent functional pains appear from early primary; FND, functional seizures and SSD most often present in adolescence, frequently after a minor illness, injury or period of pressure (Kozlowska et al., 2007) — check before quoting a peak. In schools it usually surfaces through absence, episodes in class, or a medical letter asking for a return plan.",
  "who_diagnoses": "Ireland: paediatrics or paediatric neurology (functional seizures often after EEG or video-EEG), sometimes with a paediatric liaison mental health team at a children's hospital; CAMHS for co-occurring mental health difficulty; adult neurology for young adults. GP as gateway. The EP does not diagnose.",
  "who_wrote_report": "Paediatrician or paediatric neurologist; liaison psychiatrist or clinical psychologist; physiotherapist (functional rehabilitation plan); CAMHS clinician; GP letter. A school-completed symptom log is information for the treating team, not a diagnosis.",
  "refer_to": "GP first for any unassessed physical symptom; then paediatrics/neurology via GP. Liaise (with consent) with the treating team rather than referring in parallel. CAMHS or Primary Care Psychology where anxiety, mood or risk need their own response. Tusla where abuse, neglect or fabrication concerns arise. TESS where attendance is falling.",
  "sooner": "'Functional symptoms are genuinely hard to recognise, and most families go through a long road of tests first — that's how it should be, because the physical side has to be checked properly. You did the right thing getting her checked. Now there's a diagnosis, we can plan.'"
 },

 "differential": [
  "UNDIAGNOSED MEDICAL OR NEUROLOGICAL CONDITION — always first. Only doctors can rule this in or out; functional and organic illness can also co-exist.",
  "EPILEPSY — epileptic and functional seizures can look similar and can co-exist. Distinguished medically, often with video-EEG.",
  "ANXIETY OR DEPRESSION with prominent physical symptoms — tummy aches, headaches, fatigue. The treating team decides which framework fits.",
  "ILLNESS ANXIETY DISORDER — persistent fear of having a serious illness with few or mild symptoms; the focus is the worry rather than the symptom (APA, 2022).",
  "FACTITIOUS DISORDER / MALINGERING — deliberate feigning; rare, and not an EP judgement. Fabricated or induced illness by a carer is a child protection matter.",
  "CHRONIC FATIGUE SYNDROME / ME, POST-VIRAL CONDITIONS AND CHRONIC PAIN — medically defined conditions with their own pathways; do not relabel them."
 ],

 "next": [
  "Confirm with the family (and, with consent, the treating team) that medical assessment has been completed and what the diagnosis is, in their words.",
  "Build the school participation / return plan with the family, young person, school and treating team — graded timetable, key adult, episode response plan, workload reduction, review date — at School Support Plus.",
  "Brief staff on believing, calm, consistent responses; address disbelief explicitly.",
  "Screen mood and ask about risk and safety; follow the same-day route if needed. Review the plan every few weeks and step it up as function returns."
 ],

 "presentations": [
  "Somatic complaints presenting at school (tummy aches, headaches)",
  "Frequent visits to the office or sick bay",
  "Functional seizures or collapses in school",
  "Sudden loss of mobility, speech or sensation",
  "Re-entry to school after illness",
  "Fatigue and stamina needs",
  "School refusal / emotionally based school avoidance"
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — functional neurological symptoms are rare at this age; distress more often shows as tummy aches or regression.",
   "prevalence": "Rare — rate not stated here, check.",
   "see": "Recurrent tummy aches, headaches or clinginess around separation or change, usually transient. Any new neurological symptom in a young child is a medical matter first. The EP role is supporting parents and preschool staff with calm, consistent responses once medical review is done.",
   "tools": ["SDQ (2–4 version)"]
  },
  "School Age": {
   "applies": "YES — recurrent functional abdominal pain and headaches are common; FND emerges towards the end of primary.",
   "prevalence": "Recurrent pains common; FND uncommon — rates not stated here, check (Kozlowska et al., 2007).",
   "see": "Frequent visits to the office with tummy aches or headaches, missed days, and occasionally sudden weakness, limping or collapses. Symptoms may cluster around transitions, tests or stressors — or not. Parent and teacher report, attendance data and liaison with the GP or paediatrician; screen for anxiety and mood.",
   "tools": ["SDQ", "RCADS", "BASC-3"]
  },
  "Adolescent": {
   "applies": "YES — main band for FND, functional seizures and SSD.",
   "prevalence": "Most common presentation band — rate not stated here, check.",
   "see": "Functional seizures, weakness, tremor or gait problems, chronic pain and fatigue, often with high academic standards, exam pressure and escalating absence. Being disbelieved by staff or peers is a common and harmful experience. Self-report of mood and anxiety, direct risk questions, and a return plan built with the treating team.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "BASC-3 SRP", "SDQ"]
  },
  "Young Adult": {
   "applies": "YES — FND and SSD continue into adulthood; adult neurology and adult mental health services lead.",
   "prevalence": "Rate not stated here — check before quoting.",
   "see": "Symptoms affecting college, apprenticeship or work; transition from paediatric to adult services is a known point of disruption. The EP role is advising on reasonable accommodations, liaising with college disability services, and signposting to GP and adult neurology.",
   "tools": ["Adult self-report measures via the service"]
  },
  "Special Setting": {
   "applies": "YES — can occur, but recognition is harder where communication is limited or there is co-existing neurological disability.",
   "prevalence": "Rate not stated here — check.",
   "see": "Changes in movement, seizures or pain behaviour in a pupil who may not be able to describe symptoms, often alongside genuine neurological conditions such as epilepsy or cerebral palsy. Medical assessment is essential and diagnostic overshadowing is a real risk in both directions. Staff observation records (time, setting, what happened before) support the medical team.",
   "tools": ["Functional behaviour assessment (ABC)", "SDQ"]
  }
 }
},

# ---------------------------------------------------------------------------------------------------------------
# 3. PREMENSTRUAL DYSPHORIC DISORDER
# ---------------------------------------------------------------------------------------------------------------
{
 "name": "Premenstrual Dysphoric Disorder (PMDD)",
 "code": "DSM-5-TR Premenstrual Dysphoric Disorder (Depressive Disorders chapter; ICD-10-CM F32.81) · ICD-11 GA34.41 Premenstrual dysphoric disorder (genitourinary chapter, cross-referenced from mood disorders) — check codes before quoting",
 "neps": "3. EMOTIONAL (3.4 Mood) — and 3.7 Risk and safeguarding",
 "coru": CORU,
 "psi": PSI,
 "law": "Children First Act 2015 · EPSEN Act 2004 · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "A DEPRESSIVE DISORDER tied to the menstrual cycle. In most menstrual cycles over the past year, at least five symptoms are present in the final week before a period starts, begin to improve within a few days of the period starting, and become minimal or absent in the week after (APA, 2022, DSM-5-TR).",
  "At least ONE core symptom: marked mood swings or sudden sensitivity to rejection; marked irritability, anger or conflict; marked depressed mood, hopelessness or self-critical thoughts; marked anxiety or feeling on edge. PLUS others to make five: reduced interest, poor concentration, fatigue, appetite change or cravings, sleep change, feeling overwhelmed or out of control, and physical symptoms such as breast tenderness, bloating or joint pain (APA, 2022).",
  "The symptoms must cause clinically significant distress or interfere with school, work, relationships or activities — this is the line between PMDD and common premenstrual symptoms (premenstrual syndrome, PMS), which most menstruating people experience to some degree (Yonkers, O'Brien & Eriksson, 2008).",
  "DIAGNOSIS REQUIRES PROSPECTIVE DAILY RATINGS across at least two symptomatic cycles (APA, 2022). Recall alone is not enough, because the cyclical pattern is the defining feature. The Daily Record of Severity of Problems (DRSP; Endicott, Nee & Harrison, 2006) is a commonly used chart.",
  "The best-supported account is an abnormal SENSITIVITY in the brain to normal hormonal changes across the cycle, rather than abnormal hormone levels (Yonkers et al., 2008). It is a real, biologically based condition, not a character trait.",
  "POST-MENARCHE ONLY. It can begin at any point after periods start, including adolescence, though it is often recognised later. Diagnosis is by a GP, gynaecologist or psychiatrist; treatments (including hormonal options and SSRIs) are medical decisions (RCOG, 2016). The EP does not diagnose or advise on them (PSI 2.2.2).",
  "For the EP: NOTICE a cyclical pattern, ASK sensitively, support RISK responses, REFER via the GP, and help school make practical, discreet adjustments that respect the young person's privacy and dignity."
 ],

 "what_it_is_not": [
  "NOT 'just PMS' or 'hormones'. PMDD is defined by severity and impairment; being told it's normal or that everyone gets it is a common reason young people delay seeking help.",
  "NOT a personality trait or 'being dramatic'. The pattern is cyclical and predictable, which is exactly what distinguishes it from temperament.",
  "NOT diagnosable from a single conversation. It needs prospective daily ratings over at least two cycles (APA, 2022). An EP should never suggest the label on the basis of recall.",
  "NOT the same as premenstrual exacerbation (PME) of another condition. Depression, anxiety, ADHD, bipolar disorder, epilepsy and others can worsen premenstrually; in PME, symptoms are present across the cycle and get worse before a period. The distinction is medical and matters for treatment.",
  "NOT a reason for secrecy or shame. Periods remain a sensitive topic for many young people and families, and cultural and religious attitudes vary — but the condition itself is a recognised health condition and discussing it respectfully is appropriate.",
  "NOT something the school or EP treats. Hormonal treatments and SSRIs are medical decisions (RCOG, 2016); lifestyle and CBT-based approaches also have some evidence — check current guidance before quoting."
 ],

 "prevalence": [
  "OVERALL: DSM-5-TR reports a 12-month prevalence of roughly 2–6% of menstruating individuals (APA, 2022) — check the exact range before quoting.",
  "PREMENSTRUAL SYMPTOMS (not PMDD): very common; most menstruating people report some symptoms (Yonkers et al., 2008) — rate not stated here, check.",
  "IRELAND: no Irish figure stated here — check before quoting.",
  "ADOLESCENT 13–16: fewer studies; prevalence in adolescents is uncertain and diagnosis is often delayed — rate not stated here, check.",
  "YOUNG ADULT 17–26: many people are first diagnosed in their twenties or later, often retrospectively recognising adolescent onset.",
  "SEX: occurs only in people who menstruate. Some trans and non-binary young people menstruate and may experience PMDD with added dysphoria — use their name and pronouns, and involve them in how it is discussed."
 ],

 "cooccurring": [
  {"name": "DEPRESSIVE DISORDERS", "rate": "common — rate not stated here, check",
   "presents": "low mood through the whole cycle that worsens premenstrually (PME) versus clear symptom-free weeks (PMDD). Only daily ratings and medical review can separate them."},
  {"name": "ANXIETY DISORDERS", "rate": "common — rate not stated here, check",
   "presents": "anxiety or panic that intensifies in the luteal phase, including in exams. Track timing alongside the cycle."},
  {"name": "SELF-HARM AND SUICIDAL IDEATION", "rate": "reported as elevated in PMDD — rate not stated here, check",
   "presents": "sudden hopelessness or thoughts of death in the premenstrual week that lift days later. The cyclical pattern does not reduce the seriousness; ask directly and follow the same-day route."},
  {"name": "ADHD", "rate": "possible overlap — rate not stated here, check",
   "presents": "emotional dysregulation and attention difficulties that worsen premenstrually; research is emerging — check before quoting any link."},
  {"name": "AUTISM", "rate": "rate not stated here, check",
   "presents": "increased sensory sensitivity, shutdowns or meltdowns in the premenstrual week; difficulty describing internal states may delay recognition."},
  {"name": "EATING DIFFICULTIES", "rate": "rate not stated here, check",
   "presents": "cravings and binge episodes premenstrually, or restriction; weight and appetite changes need GP review."},
  {"name": "GYNAECOLOGICAL CONDITIONS", "rate": "rate not stated here, check",
   "presents": "painful or heavy periods, endometriosis or polycystic ovary syndrome causing pain, fatigue and absence alongside mood symptoms. GP / gynaecology."}
 ],

 "recommendations": [
  "RISK FIRST. If the young person describes hopelessness, self-harm or suicidal thoughts — even if they 'only happen before a period' — ask directly and follow the same-day risk route: supervisor informed the same day, parents informed unless that would increase risk, GP/CAMHS contacted, ED or emergency services if imminent.",
  "REFER: GP as first step for assessment of cyclical mood symptoms; GP may refer to gynaecology, psychiatry or CAMHS depending on age and severity. Recommend the young person keeps a daily symptom diary for two cycles to bring to the GP (DRSP or similar; Endicott et al., 2006).",
  "DESCRIBE, DON'T LABEL. Write: 'X reports marked irritability, tearfulness and difficulty concentrating in the week before her period, which she describes as easing within a few days of it starting. She has been advised to track this and discuss it with her GP.' Do not write 'X has PMDD' unless a doctor has diagnosed it.",
  "DISCREET SCHOOL ADJUSTMENTS, agreed with the young person: a named adult they can tell, without explanation, 'it's one of those weeks'; permission to leave class briefly without questions; access to a quiet space and toilets; flexibility on deadlines and tests in the premenstrual week where possible; reasonable PE adjustments; water and snacks.",
  "PLAN AROUND PREDICTABILITY: where the pattern is clear, help the young person plan heavier study earlier in the cycle and lighter demands in the symptomatic week. For State examinations, check the SEC's current schemes and deadlines rather than assuming eligibility.",
  "PRIVACY: share only what the young person agrees to share, with named staff. Menstrual health information is sensitive personal and health data (GDPR). Agree the wording.",
  "CONTINUUM LEVEL: Classroom Support or School Support for adjustments; School Support Plus where CAMHS, psychiatry or gynaecology are involved or risk has been identified.",
  "PSYCHOEDUCATION within SPHE and wellbeing programmes can reduce stigma about periods generally — support the school's approach rather than singling out an individual.",
  "DO NOT diagnose, suggest the label from recall, recommend supplements, contraception or medication, or give dietary prescriptions. Those are medical (PSI 2.2.2)."
 ],

 "explain_parent": [
  "'She's described a pattern where her mood drops sharply in the week before her period and lifts a few days after it starts. That pattern is worth taking to the GP.'",
  "'There's a condition called PMDD, where the brain is extra-sensitive to the normal hormone changes in the cycle. I can't tell you whether she has it — that's for the doctor — but the way to find out is to keep a daily chart for two or three months and bring it to the GP.'",
  "'It's not \"just hormones\" or her being difficult. When it's this strong it's a recognised health condition, and there are treatments the doctor can talk through.'",
  "'She told me that in the bad week she sometimes has thoughts of not wanting to be here. I've asked her about it directly and we've made a safety plan. Even though it passes, it's serious, and I'd like her to see the GP this week.'",
  "'In school, we'll put some quiet, practical supports in place that she's agreed to — a named teacher, a bit of flexibility in that week — without everyone needing to know why.'",
  "SIGNPOST: GP; IAPMD (International Association for Premenstrual Disorders) for information and daily tracking resources; Jigsaw (12–25) or SpunOut for mood support; for crisis, Pieta (1800 247 247), Samaritans (116 123), text 50808. Check links and numbers are current before giving them."
 ],

 "explain_teacher": [
  "'She has a cyclical health difficulty that affects her mood and concentration for about a week each month. She's agreed that you should know that much — please keep it private.'",
  "'In that week she may be more irritable, tearful or overwhelmed than usual. It's not attitude and it's not something she can switch off. A quiet word works better than a public correction.'",
  "'If she asks to step out, please let her without questions — that's part of the plan we've agreed.'",
  "'If there's flexibility on a test or deadline that falls in that week, it genuinely helps. Otherwise, a quiet check-in makes a difference.'",
  "'If she ever says anything about hurting herself or not wanting to be here, even if she says it will pass, go to the DLP and principal that day. Don't promise to keep it secret.'"
 ],

 "explain_child": [
  "OLDER (post-menarche only): 'Lots of people notice their mood changes around their period. For some, it's much stronger — a week of feeling really low, angry or overwhelmed, then it lifts. That's a real thing with a name, and a doctor can help work out what's going on.'",
  "'The best way to find out is to track it — a quick daily note of how you feel for a couple of months. It sounds boring, but it's the thing doctors most need.'",
  "ASK, SENSITIVELY AND PRIVATELY: 'Do you notice your mood changes at particular times of the month?' Let the young person lead on how much detail they share; offer a same-gender adult if they would prefer.",
  "ASK ABOUT SAFETY DIRECTLY: 'In the hardest week, do you ever have thoughts of hurting yourself or that life isn't worth living?' Explain confidentiality limits before you ask.",
  "ASK: 'What would help in school during that week? Who would you feel OK telling?'",
  "AVOID: 'it's just your hormones', 'everyone gets that', or joking about periods — these shut the conversation down."
 ],

 "analogies": [
  "THE VOLUME KNOB: 'Everyone's hormones go up and down across the month. For most people it's background music. For some, the brain turns the volume right up, so the same change feels overwhelming.' Works with adolescents and parents; explains sensitivity rather than abnormal hormones (Yonkers et al., 2008).",
  "THE WEATHER FORECAST: 'Once you've tracked it, you can see the storm coming. You can't stop the weather, but you can bring an umbrella — plan lighter days, tell your person.' Works with adolescents; supports tracking and planning.",
  "THE TIDE: 'It comes in, and it goes out again, on a pattern. When the tide's in, it's not the real you talking — and it will go out.' Works with young people in the hard week; helps with hopelessness (alongside a risk response, never instead of one).",
  "THE INVISIBLE CAST: 'If she'd a broken wrist for one week every month, we'd adjust her work for that week without a second thought. This is similar, just invisible.' Works with teachers."
 ],

 "language": [
  "Use 'premenstrual dysphoric disorder (PMDD)' only where diagnosed; otherwise 'cyclical mood symptoms' or 'mood changes linked to her menstrual cycle'.",
  "Avoid: 'hormonal', 'time of the month' jokes, 'PMS-ing', 'overreacting', 'dramatic'. These trivialise and can humiliate.",
  "Be inclusive: not all people who menstruate are girls. Use the young person's name and pronouns, and ask how they want it described.",
  "Use the young person's own words for their experience in reports, and record only what they have agreed may be shared (PSI 1.2.8; GDPR)."
 ],

 "red_flags": [
  "RED FLAG — suicidal ideation, plans or self-harm, even if cyclical. Same-day risk route: supervisor informed the same day, parents informed unless that would increase risk, GP/CAMHS contacted, ED or emergency services if imminent. Supervision follows action; it does not replace it.",
  "RED FLAG — disclosure of abuse, sexual exploitation or coercion. Child protection route: DLP the same day and report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's own duty.",
  "RED FLAG — very heavy or painful periods, fainting, or rapid weight change. GP review for gynaecological or medical causes.",
  "RED FLAG — episodes of unusually elevated mood, reduced need for sleep or psychotic symptoms. Possible bipolar disorder or psychosis — urgent medical/CAMHS referral.",
  "BOUNDARY — you do not diagnose PMDD, suggest the label from recall, or advise on contraception, hormonal treatment, SSRIs or supplements (PSI 2.2.2).",
  "WATCH — pre-menarche children. PMDD cannot be the explanation before periods begin; look elsewhere.",
  "WATCH — the pupil repeatedly sanctioned for 'attitude' in a predictable pattern each month. Ask about timing before assuming behaviour."
 ],

 "child_voice": [
  "DAILY SYMPTOM TRACKER (DRSP or a simple app or paper chart) completed by the young person — good because it gives them evidence and control, is the thing the GP needs, and shows the young person their own pattern.",
  "SCALING CONVERSATIONS for 'good weeks' and 'hard weeks' — good because it names the exceptions and helps plan around them.",
  "A 'WHAT HELPS ME' CARD agreed with the young person and shared only with named staff — good because it avoids repeated explanation and keeps them in charge of privacy.",
  "SOLUTION-FOCUSED PUPIL INTERVIEW, held privately — good because it keeps the focus on what helps, and can include a direct risk question naturally.",
  "IAPMD and Irish youth mental health materials (Jigsaw, SpunOut) — good because self-understanding reduces shame and supports help-seeking. → https://iapmd.org/ · https://jigsaw.ie/ · https://spunout.ie/ (check links are current)"
 ],

 "questions": [
  "Q: 'Isn't everyone moody before their period?' — A: 'Many people get some symptoms. What's different here is how severe it is and how much it's affecting school and friendships — and that it lifts so clearly afterwards. That's worth a GP's view.'",
  "Q: 'Does she have PMDD?' — A: 'I can't say — that's a medical diagnosis, and it needs a couple of months of daily tracking first. What I can say is that the pattern she's described is worth taking to the GP, and tracking will help.'",
  "Q: 'Should she go on the pill?' — A: 'That's a medical decision for her and her doctor. There are several treatment options, and the GP is the right person to talk them through.'",
  "Q (teacher): 'Can I give her extra time on the test because it's her time of the month?' — A: 'Within your usual school flexibility, yes — we've agreed some adjustments for that week. For State exams, the school needs to check the SEC's current schemes rather than assuming anything applies.'",
  "Q: 'She says she wants to die in that week, but then she's fine — is it real?' — A: 'Yes, and it's serious. It being cyclical doesn't make it safer. We follow the same safety steps as we would at any other time, and it's a strong reason to see the GP soon.'",
  "Q: 'Why does she have to track it — can't the doctor just tell?' — A: 'The key feature is the timing — symptoms in the week before, gone the week after. Memory isn't reliable for that, so doctors need a daily record over at least two cycles.'",
  "Q (young person): 'Do my teachers have to know?' — A: 'Only what you agree to, and only the people you choose. We can say you have a health thing that affects one week a month, without saying anything more.'"
 ],

 "supervision": [
  "Rehearse how you raise the menstrual cycle with a young person respectfully, and how you respond if they don't want to discuss it.",
  "Discuss consent and privacy: what can be recorded, who can be told, and how to handle a young person who does not want parents told about cyclical suicidal thoughts.",
  "Rehearse the risk conversation for cyclical suicidal ideation — and what you do the same day.",
  "Discuss cultural and religious sensitivities around periods, and how to adapt your approach with families.",
  "Bring any case where a cyclical pattern was noticed in behaviour records but not explored."
 ],

 "reflection": [
  "ON HOW I EXPLAINED IT — did I describe a pattern and point to the GP, or did I slip into naming a diagnosis?",
  "ON DIGNITY — did the young person decide what was shared and with whom? Did my language respect them?",
  "ON RISK — did I treat cyclical hopelessness as seriously as any other risk, and act the same day?",
  "ON MY OWN COMFORT — did I avoid the topic because it felt awkward? What would help me raise it next time?",
  "ON INCLUSION — did I assume gender, or ask how the young person describes themselves?",
  "WHAT GOOD LOOKS LIKE: 'A Fifth Year had been sanctioned repeatedly for outbursts. The behaviour log showed a roughly monthly pattern. I asked her privately; she described a week of rage and despair before each period, with passing thoughts of dying. I asked directly, made a safety plan, told my supervisor, and met her mum that day. She saw the GP with a tracking chart; school agreed a discreet plan.'",
  "WHAT POOR LOOKS LIKE: 'Behaviour appears hormonal; recommend she tries to manage her moods.' — dismissive, no risk enquiry, no referral, no plan."
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "Yonkers, K. A., O'Brien, P. M. S., & Eriksson, E. (2008). Premenstrual syndrome. The Lancet, 371(9619), 1200–1210.",
  "Endicott, J., Nee, J., & Harrison, W. (2006). Daily Record of Severity of Problems (DRSP): Reliability and validity. Archives of Women's Mental Health, 9(1), 41–49.",
  "Royal College of Obstetricians and Gynaecologists. (2016). Management of premenstrual syndrome (Green-top Guideline No. 48). Published in BJOG (2017), 124(3), e73–e105 — check for updates.",
  "World Health Organization. (2019/2022). International classification of diseases (11th rev.). https://icd.who.int/ — check code GA34.41 in the browser before quoting.",
  "Department of Education and Skills, Health Service Executive, & Department of Health. (2013). Well-being in post-primary schools: Guidelines for mental health promotion and suicide prevention. Government of Ireland."
 ],

 "pathway": {
  "age": "Post-menarche only. Symptoms can begin in adolescence, but diagnosis is often delayed into the twenties or later, partly because symptoms are normalised as 'PMS' and partly because diagnosis needs prospective daily tracking over at least two cycles (APA, 2022). In schools it may surface through a cyclical pattern in behaviour, attendance or mood records, or a disclosure.",
  "who_diagnoses": "Ireland: GP first; gynaecology or psychiatry (adult or CAMHS for under-18s) where more specialist assessment is needed. Diagnosis requires prospective daily ratings. Treatment — hormonal or SSRI — is prescribed only by a doctor. The EP does not diagnose.",
  "who_wrote_report": "GP letter; gynaecologist; psychiatrist or CAMHS clinician; adult mental health service for young adults. A symptom-tracking chart completed by the young person is evidence for the doctor, not a diagnosis.",
  "refer_to": "GP first (urgently if risk); CAMHS via GP where there is risk or co-occurring moderate to severe mood difficulty; Jigsaw (12–25, check area) for mood support; ED or emergency services if risk is imminent; Tusla where abuse, exploitation or neglect is suspected.",
  "sooner": "'Cyclical mood problems are very often dismissed as \"just periods\" — by families, schools and sometimes professionals. Most people wait years before anyone joins the dots. She's noticing the pattern at this age, which puts her ahead.'"
 },

 "differential": [
  "MAJOR DEPRESSIVE DISORDER / PERSISTENT DEPRESSIVE DISORDER — symptoms present across the whole cycle, possibly worse premenstrually (premenstrual exacerbation). Daily ratings separate them.",
  "BIPOLAR DISORDER — mood episodes not tied to the cycle; elevated mood or reduced need for sleep. Urgent medical flag.",
  "ANXIETY DISORDERS — persistent anxiety with premenstrual worsening.",
  "BORDERLINE PERSONALITY FEATURES / EMOTION DYSREGULATION — rapid mood shifts linked to interpersonal events rather than the cycle; handle with great caution in adolescents and leave any such formulation to psychiatry.",
  "MEDICAL CAUSES — thyroid disorder, anaemia (especially with heavy periods), endometriosis, polycystic ovary syndrome, effects of hormonal contraception. GP review.",
  "ADJUSTMENT OR SITUATIONAL STRESS — exams, relationships, family events that happen to coincide. The pattern across several cycles distinguishes them."
 ],

 "next": [
  "If risk emerged: the same-day risk route first, and supervisor informed the same day.",
  "Support the young person to keep a daily symptom chart for two cycles and to see the GP; offer a brief factual letter describing what was observed and reported.",
  "Agree a discreet school plan with the young person — named adult, step-out permission, flexibility in the symptomatic week — at Classroom Support or School Support, with clear privacy boundaries.",
  "Review after two to three cycles, or sooner if mood worsens."
 ],

 "presentations": [
  "Cyclical mood changes or irritability",
  "Cyclical absence or reduced participation",
  "Low mood without diagnostic threshold",
  "Irritability as the presentation of low mood in young people",
  "Self-harm",
  "Menstrual pain and health-related absence"
 ],

 "bands": {
  "Early Years": {
   "applies": "N/A — PMDD occurs only after menarche.",
   "prevalence": "Not applicable at this age.",
   "see": "Not applicable. Irritability and mood changes in young children have other explanations; see the depressive disorders, DMDD and anxiety entries. Early puberty (very early menarche) is a paediatric matter in its own right.",
   "tools": []
  },
  "School Age": {
   "applies": "RARELY — only in pupils who have already started menstruating, usually in the senior primary years.",
   "prevalence": "Rate not stated here — check; very limited data at this age.",
   "see": "A pupil in fifth or sixth class who has started her periods and shows marked monthly mood changes, tearfulness or outbursts. Usually recognised by a parent rather than school. Handle privately and sensitively, involve parents, and refer to the GP; track rather than label.",
   "tools": ["SDQ", "MFQ (Mood and Feelings Questionnaire)"]
  },
  "Adolescent": {
   "applies": "YES — main school band for onset and recognition, though diagnosis is often delayed.",
   "prevalence": "Adolescent rate uncertain — check; adult 12-month prevalence roughly 2–6% (APA, 2022), check before quoting.",
   "see": "A predictable week each month of irritability, rejection sensitivity, low mood, anxiety, poor concentration and fatigue, then recovery. Shows as cyclical conflict, sanctions, absence and dips in performance. Ask privately, screen mood, ask directly about risk, and support daily tracking and a GP visit.",
   "tools": ["Daily Record of Severity of Problems (DRSP; Endicott, Nee & Harrison, 2006) — AGE post-menarche · MEASURES: daily ratings of mood, behavioural and physical premenstrual symptoms across the cycle · CANNOT TELL YOU: a diagnosis on its own — needs two cycles and medical review · TIME: 2–3 min a day", "MFQ (Mood and Feelings Questionnaire)", "RCADS self-report", "BASC-3 SRP"]
  },
  "Young Adult": {
   "applies": "YES — many are first diagnosed in this age range.",
   "prevalence": "Adult 12-month prevalence roughly 2–6% of menstruating individuals (APA, 2022) — check before quoting.",
   "see": "Cyclical mood symptoms affecting college, work and relationships. The EP role is recognition, risk response, and signposting to the GP, college health and disability services, and adult mental health where needed. Reasonable accommodations in further and higher education may apply — check the institution's policy.",
   "tools": ["Adult self-report measures via the service", "Daily Record of Severity of Problems (DRSP; Endicott, Nee & Harrison, 2006) — AGE post-menarche · MEASURES: daily cyclical symptom ratings · CANNOT TELL YOU: a diagnosis on its own · TIME: 2–3 min a day"]
  },
  "Special Setting": {
   "applies": "YES — can occur in post-menarche pupils with intellectual disability or autism, and is easily missed.",
   "prevalence": "Rate not stated here — check.",
   "see": "A monthly pattern of increased distress, self-injury, aggression, withdrawal or sleep disturbance in a pupil who may not be able to describe how she feels. Staff behaviour logs matched against a cycle record (kept with parental consent and respecting dignity) can reveal it. Refer via GP; any medical treatment is a medical decision.",
   "tools": ["Functional behaviour assessment (ABC)", "SDQ"]
  }
 }
},
]
