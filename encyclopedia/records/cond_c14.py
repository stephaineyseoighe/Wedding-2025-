# CONDS records, batch c14: Feeding disorders (ARFID, Pica, Rumination), Eating disorders
# (Anorexia Nervosa, Bulimia Nervosa, Binge-Eating Disorder), Elimination disorders (Enuresis, Encopresis).
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c14.py

CORU = "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32"
PSI = "2.2.2 · 2.2.4 · 2.3.1 · 1.3.1 · 1.2.8"
LAW_MED = "Children First Act 2015 · EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · Equal Status Acts 2000–2018 · GDPR"
LAW_ED = "Children First Act 2015 · Mental Health Act 2001 (age of consent and admission of minors — check current provisions) · EPSEN Act 2004 · Equal Status Acts 2000–2018 · GDPR"

# Shared risk bullets for the eating-disorder entries (same-day routes).
ED_MEDICAL_RISK = ("RED FLAG — MEDICAL RISK IS THE FIRST QUESTION. Fainting or dizziness, chest pain or palpitations, feeling "
                   "cold all the time, very rapid weight loss, refusing fluids, repeated vomiting, blood in vomit, or a young "
                   "person who looks unwell → contact the parent/guardian the SAME DAY and advise an urgent GP appointment that day; "
                   "if collapse, chest pain or confusion, call 999/112. Eating disorders can be medically dangerous at ANY weight, "
                   "including 'normal' or higher weight (RCPsych, 2022, MEED). Tell your supervisor the same day. Supervision follows action; it does not replace it.")
ED_SUICIDE_RISK = ("RED FLAG — self-harm, suicidal ideation, plan or intent. Risk is elevated across eating disorders (Arcelus et al., 2011). "
                   "Same-day risk route: ask directly, do not leave the young person alone if risk is imminent, inform parents unless that "
                   "would increase risk, contact GP/CAMHS, and emergency services or ED if imminent. Inform your supervisor the same day.")
CP_ROUTE = ("RED FLAG — disclosure or indicators of abuse or neglect (including deliberate withholding of food, or a child "
            "not being brought to medical appointments). Child protection route: report to Tusla as soon as practicable; "
            "telling the DLP does not discharge a mandated person's duty under the Children First Act 2015.")

CONDS = [

# =====================================================================================
# 1. ARFID
# =====================================================================================
{
 "name": "Avoidant/Restrictive Food Intake Disorder (ARFID)",
 "code": "DSM-5-TR Avoidant/Restrictive Food Intake Disorder (feeding and eating disorders chapter) · ICD-11 6B83 Avoidant-restrictive food intake disorder — verify codes before quoting",
 "neps": "5. OTHER (5.3 Medical condition or other diagnosis) — and 3. EMOTIONAL (3.2 Anxiety) where fear of choking or vomiting drives it",
 "coru": CORU,
 "psi":  PSI,
 "law":  LAW_MED,

 "what_it_is": [
  "A FEEDING OR EATING DISTURBANCE in which the child or young person avoids or restricts food to the point of real consequence: significant weight loss or faltering growth, significant nutritional deficiency, dependence on supplements or tube feeding, and/or marked interference with psychosocial functioning (APA, 2022, DSM-5-TR). Introduced in DSM-5 (2013), replacing the narrower 'feeding disorder of infancy or early childhood'.",
  "NOT DRIVEN BY BODY IMAGE. There is no fear of weight gain and no disturbance in how body shape or weight is experienced — that is what separates it from anorexia nervosa. It is not explained by lack of available food, a culturally sanctioned practice, or a medical condition alone (APA, 2022).",
  "THREE COMMONLY DESCRIBED DRIVERS, which can overlap (Thomas & Eddy, 2019): (1) SENSORY SENSITIVITY — texture, smell, taste, appearance, brand; (2) LACK OF INTEREST in eating or low appetite — forgets to eat, full quickly; (3) FEAR OF AVERSIVE CONSEQUENCES — choking, vomiting, pain, often after a specific frightening event.",
  "It is a DIAGNOSIS MADE ON CONSEQUENCE, not on a short food list. Many children are selective eaters; ARFID is reserved for restriction that harms growth, nutrition or daily life (e.g., cannot eat at school, cannot go on a school trip, cannot eat in front of others).",
  "It occurs at any age but is often identified in childhood, and it is more common in autistic children and children with anxiety (Thomas & Eddy, 2019) — rate not stated here, check before quoting.",
  "Assessment and treatment are MULTIDISCIPLINARY: GP and paediatrics (growth, bloods, medical causes), dietetics, feeding therapy (often SLT and/or OT), and psychology (graded exposure, CBT-AR — Thomas & Eddy, 2019). In Ireland this sits with paediatrics, Primary Care, CDNT (where there is a disability) or CAMHS — pathways vary by area; check locally.",
  "The EP's job: RECOGNISE the pattern, keep MEDICAL review first, describe the impact on the school day, support a low-pressure plan at lunchtime, and REFER — not diagnose.",
 ],

 "what_it_is_not": [
  "NOT ordinary picky eating. Fussy eating is common in toddlers and early childhood and usually eases with time (Taylor, Wernimont, Northstone & Emmett, 2015). ARFID requires harm to growth, nutrition or functioning.",
  "NOT the same as AUTISTIC SENSORY EATING — though they overlap. Many autistic children eat a narrow range for sensory reasons (Cermak, Curtin & Bandini, 2010) without meeting ARFID. When the restriction causes nutritional, growth or functional harm, ARFID may be diagnosed ALONGSIDE autism. The question is consequence, not category.",
  "NOT anorexia in disguise — but be careful. A young person who says 'I'm just not hungry' or 'I don't like it' may be concealing weight-and-shape concerns. ARFID can also shift into, or be mistaken for, other eating disorders. Specialists make the distinction.",
  "NOT 'bad behaviour' or a parenting failure. Pressure, bribes and 'you'll sit there until you eat it' typically raise anxiety and entrench avoidance (Thomas & Eddy, 2019).",
  "NOT something the child will eat 'when hungry enough'. In ARFID a child can go without rather than eat a feared or aversive food.",
  "NOT excluded by a normal-looking weight. Nutritional deficiency (iron, vitamins) and faltering growth can occur without obvious thinness; only medical review can say.",
 ],

 "prevalence": [
  "OVERALL: population estimates vary widely with definition and method — rate not stated here, check before quoting. DSM-5-TR does not give a firm population figure (APA, 2022 — check the text).",
  "IRELAND: no Irish prevalence figure stated here — check before quoting (HSE National Clinical Programme for Eating Disorders material may hold service data).",
  "CLINICAL SAMPLES: ARFID was identified in a notable proportion of young people referred to eating disorder programmes after DSM-5 (Fisher et al., 2014) — check the figure before quoting.",
  "AUTISM, ADHD AND ANXIETY: elevated — rate not stated here, check. Atypical eating is far more common in autistic children than in typically developing children (Mayes & Zickgraf, 2019).",
  "SEX RATIO: unlike anorexia, ARFID is not reported as strongly female-predominant; in some clinical samples males are well represented — check before quoting.",
 ],

 "cooccurring": [
  {"name": "AUTISM", "rate": "elevated — rate not stated here, check",
   "presents": "a very narrow, 'safe' food list (often by brand, colour or texture), distress at new foods or mixed textures, and difficulty eating in a noisy canteen. Sensory profile and predictability matter more than hunger."},
  {"name": "ANXIETY DISORDERS (including specific phobia of choking or vomiting)", "rate": "elevated — rate not stated here, check",
   "presents": "a child who stopped eating solids after choking or a vomiting illness, checks food repeatedly, eats only soft foods, or cannot eat away from home. Fear-based ARFID; graded exposure with clinical input."},
  {"name": "ADHD", "rate": "elevated — rate not stated here, check",
   "presents": "forgetting to eat, low interest in food, or appetite suppressed by stimulant medication (a matter for the prescriber, not the EP). Lunch goes home untouched."},
  {"name": "GASTROINTESTINAL AND MEDICAL CONDITIONS (reflux, allergy, coeliac disease, constipation)", "rate": "not stated here — check",
   "presents": "avoidance that began with real pain or reactions and outlasted them. Medical review first; the learned fear may remain after the medical issue settles."},
  {"name": "DEVELOPMENTAL AND ORAL-MOTOR DIFFICULTIES (including intellectual disability, cerebral palsy)", "rate": "not stated here — check",
   "presents": "coughing, gagging or slow eating; soft-only diet; long mealtimes. Needs SLT dysphagia assessment for safe swallowing before any behavioural plan."},
  {"name": "OTHER EATING DISORDERS", "rate": "not stated here — check",
   "presents": "restriction that gradually acquires weight-and-shape concerns in adolescence. Any statement about wanting to be thinner changes the referral — see the anorexia entry."},
 ],

 "recommendations": [
  "MEDICAL REVIEW FIRST. Write it first: 'Given the restricted diet described, it is recommended that parents arrange a GP review of growth, nutrition and any physical cause, if this has not already happened.' Where weight loss or faltering growth is reported, the GP visit is urgent.",
  "NO PRESSURE AT LUNCH. Staff do not coax, bribe, praise eating, comment on the lunchbox or keep the child in until food is eaten. Neutral, friendly supervision only. Pressure maintains avoidance (Thomas & Eddy, 2019).",
  "PREDICTABLE, CALMER EATING SPACE if the canteen is overwhelming — a quieter table or a familiar peer — agreed with parents and the child, reviewed so it does not become isolation.",
  "SAFE FOODS ARE ALLOWED. The child brings foods they can eat. School healthy-eating policies may need a reasonable adjustment in writing (e.g., exemption from 'no crisps' rules) — agree with the principal and parents.",
  "SCHOOL TRIPS, COOKING CLASS, FOOD-BASED SCIENCE OR HOME ECONOMICS: plan ahead with the family; do not surprise the child with food exposure. Any exposure work belongs in the clinical plan, not ad hoc in class.",
  "CONTINUUM LEVEL: Classroom Support for mild cases with a lunchtime plan; School Support where eating affects attendance, participation or peer relationships; School Support Plus where dietetics, feeding therapy, CDNT or CAMHS are involved — share the school plan with them, with consent.",
  "REFER: GP → paediatrics and dietetics; feeding team (SLT/OT) where oral-motor or sensory; CDNT where there is a disability; CAMHS or Primary Care Psychology where anxiety or phobia drives it. Pathways vary — check locally.",
  "DO NOT diagnose ARFID, recommend diets, supplements, or medication, or set food targets. The EP describes, formulates, recommends school adjustments and refers (PSI 2.2.2).",
 ],

 "explain_parent": [
  "'This isn't fussiness and it isn't your fault. For some children, eating new or certain foods feels genuinely unsafe or unbearable — because of texture, smell, fear of choking, or just very low appetite.'",
  "'The first thing I'd suggest is a GP check of growth and nutrition. That tells us how urgent this is.'",
  "'At school, we'll take the pressure off completely — no one will make comments or make her finish. Pressure usually makes it worse.'",
  "'Help for this usually comes from a team — a dietitian, sometimes a speech and language therapist or OT for feeding, and a psychologist for the fear part. It's slow, step-by-step work.'",
  "'Can you tell me the foods she can eat, how it started, and whether anything scary happened around food — choking, a bad vomiting bug, pain?'",
  "SIGNPOST: GP; HSE dietetics via GP/Primary Care; Bodywhys (the Eating Disorders Association of Ireland) has information for families — check whether current material covers ARFID; the treating team for any home plan.",
 ],

 "explain_teacher": [
  "'This is a recognised eating condition, not being picky. He isn't being difficult — some foods feel unsafe to him.'",
  "'Please don't encourage, bribe or comment on what he eats or doesn't. Neutral is best. Just let him eat his safe foods in peace.'",
  "'If the canteen is loud or smelly, a quieter spot can help — let's agree it with him and review it.'",
  "'Before any trip, cooking class or food-tasting lesson, let the family know so they can plan. No surprises with food.'",
  "'Tell the parents, same day, if he looks unwell, faint or very tired, or you notice he's eating much less than usual.'",
 ],

 "explain_child": [
  "YOUNGER: 'Some tummies and some mouths are extra fussy about food — how it feels, smells or looks. That's not naughty. Lots of grown-ups are going to help you find it a bit easier, slowly.'",
  "OLDER: 'Some people's brains treat certain foods as dangerous or disgusting, even when they're not. That's a real thing with a name, and there's help that works step by step, at your pace.'",
  "ASK: 'What's lunchtime like for you?' · 'Where is the easiest place to eat?' · 'Is there anything that makes eating harder at school — noise, smells, people watching?'",
  "ASK (older): 'Is it more that you're not hungry, that food feels or tastes wrong, or that you're worried something will happen when you eat?' — the answer points to the driver.",
  "DO NOT ask the child to try food with you, and do not praise or comment on eating. The session is about what school is like, not about food performance.",
 ],

 "analogies": [
  "THE SMOKE ALARM: 'Her body's alarm goes off for foods that are actually safe. We don't rip out the alarm or shout at it — we slowly teach it which foods are fine.' Works with parents and teachers.",
  "THE SPIDER PHOBIA: 'Being asked to eat a feared food is like being asked to pick up a spider. Pushing makes the fear bigger; tiny steps with choice make it smaller.' Works with teachers who want to encourage tasting.",
  "THE FUEL GAUGE: 'For some children the hunger gauge is quiet — they don't notice they're running low.' Works with parents of low-interest eaters and with older pupils.",
  "THE PASSPORT: 'Safe foods are her passport to get through the school day. Take it away and she can't travel.' Works with principals asked to bend a healthy-lunch rule.",
 ],

 "language": [
  "Use 'ARFID' or 'avoidant/restrictive food intake disorder' only when a clinician has diagnosed it. Otherwise describe: 'a restricted range of foods', 'eats a small number of safe foods'.",
  "Avoid 'fussy', 'picky', 'spoilt', 'stubborn', 'attention-seeking'. They blame the child and the family.",
  "Say 'safe foods' or 'preferred foods' (the child's and family's term) rather than 'junk'.",
  "Many autistic adults describe their food preferences as sensory needs, not behaviour to be fixed; respect this language while still attending to nutrition and growth.",
 ],

 "red_flags": [
  "RED FLAG — weight loss, faltering growth, fainting, dizziness, looking pale or exhausted, or eating/drinking almost nothing → parent the same day, urgent GP. If the child collapses or is confused, call 999/112.",
  "RED FLAG — coughing, choking or chest infections linked to eating → swallowing needs SLT dysphagia assessment via GP/paediatrics before any feeding plan.",
  "RED FLAG — restriction now accompanied by comments about weight, shape, calories or 'being fat' → consider anorexia; urgent GP and CAMHS route (see that entry).",
  CP_ROUTE,
  "BOUNDARY — you do not diagnose ARFID, recommend diets, supplements or medication, or run exposure therapy. You describe, formulate, recommend school adjustments and refer (PSI 2.2.2).",
  "WATCH — school well-meaning 'encouragement' programmes, sticker charts for eating, or healthy-eating campaigns that single the child out.",
 ],

 "child_voice": [
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) with a lunchtime focus — good because it maps the whole day and lets lunch be one part, not the headline. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "DRAWING THE IDEAL LUNCHTIME (an adaptation of Moran's (2001) Drawing the Ideal Self technique — the adaptation is ours, not Moran's) — good because younger and autistic children can show where, with whom and how, without talking about eating directly.",
  "SENSORY MAPPING of the school day (noisy, smelly, crowded, calm places) — good because it links eating to environment and gives staff specific changes to make.",
  "SOLUTION-FOCUSED SCALING ('0–10, how OK is lunchtime?') — good because it finds what already works and a next small step the child chooses.",
 ],

 "questions": [
  "Q: 'Won't he just eat when he's hungry?' — A: 'In ARFID, no — many children will go without rather than eat a food that feels unsafe. That's why it needs a medical check and a proper plan, not waiting.'",
  "Q: 'Should we make him try one bite at lunch?' — A: 'Not at school. Tasting and exposure work is done gradually by the treating team with his agreement. At school, the best help is no pressure and his safe foods available.'",
  "Q: 'Is this autism?' — A: 'Restricted eating is common in autism but it doesn't on its own mean autism, and ARFID can happen without it. If you have other concerns about his social communication, that's a separate conversation and referral.'",
  "Q: 'Our healthy-eating policy bans some of his safe foods.' — A: 'That's a reasonable adjustment worth writing down. For him those foods are what keeps him going through the day.'",
  "Q: 'Is it anorexia?' — A: 'The difference is why she's not eating. In ARFID it's about the food itself or fear of what might happen; in anorexia it's about weight and shape. If she ever talks about weight or body size, we'd refer urgently.'",
  "Q: 'Who treats this?' — A: 'Usually a team: GP and paediatrics for the medical side, a dietitian, sometimes a feeding therapist, and psychology for the fear. The route depends on your area; the GP is the start.'",
 ],

 "supervision": [
  "Bring the formulation: which driver (sensory, low interest, fear) is most prominent, and what evidence supports that?",
  "Ask about local pathways: who takes ARFID referrals here — paediatrics, CDNT, CAMHS, dietetics? What happens if the child has no disability?",
  "Discuss where your role ends: when a teacher asks you for a food exposure plan, what do you say?",
  "Raise any case where the eating pattern might be changing towards weight-and-shape concerns.",
 ],

 "reflection": [
  "ON THE MEDICAL QUESTION — did I confirm that growth and nutrition have been checked, or did I assume someone else had?",
  "ON PRESSURE — did my recommendations remove pressure at lunch, or did any of them (sticker charts, 'try one bite') add to it?",
  "ON AUTISM — did I treat the eating as 'just autism' and stop there, or did I ask about consequence?",
  "ON THE FAMILY — did the parents leave feeling blamed? How did I frame their efforts?",
  "ON THE CHILD'S VIEW — did I hear what lunchtime is like for them, not only what adults report?",
  "WHAT GOOD LOOKS LIKE: 'GP review recommended; lunchtime plan with a quieter table and safe foods written into the Student Support File; teacher briefed not to comment; referral to dietetics via GP; review in six weeks with the child's scaling.'",
  "WHAT POOR LOOKS LIKE: 'Class teacher to encourage him to try one new food each week and reward with stickers.' — adds pressure, skips medical review and steps into treatment.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "Cermak, S. A., Curtin, C., & Bandini, L. G. (2010). Food selectivity and sensory sensitivity in children with autism spectrum disorders. Journal of the American Dietetic Association, 110(2), 238–246.",
  "Fisher, M. M., Rosen, D. S., Ornstein, R. M., Mammel, K. A., Katzman, D. K., Rome, E. S., Callahan, S. T., Malizio, J., Kearney, S., & Walsh, B. T. (2014). Characteristics of avoidant/restrictive food intake disorder in children and adolescents: A 'new disorder' in DSM-5. Journal of Adolescent Health, 55(1), 49–52.",
  "Mayes, S. D., & Zickgraf, H. (2019). Atypical eating behaviors in children and adolescents with autism, ADHD, other disorders, and typical development. Research in Autism Spectrum Disorders, 64, 76–83.",
  "Taylor, C. M., Wernimont, S. M., Northstone, K., & Emmett, P. M. (2015). Picky/fussy eating in children: Review of definitions, assessment, prevalence and dietary intakes. Appetite, 95, 349–359.",
  "Thomas, J. J., & Eddy, K. T. (2019). Cognitive-behavioral therapy for avoidant/restrictive food intake disorder: Children, adolescents, and adults. Cambridge University Press.",
  "Bryant-Waugh, R., Micali, N., Cooke, L., Lawson, E. A., Eddy, K. T., & Thomas, J. J. (2019). Development of the Pica, ARFID, and Rumination Disorder Interview, a multi-informant, semi-structured interview of feeding disorders across the lifespan: A pilot study for ages 10–22. International Journal of Eating Disorders, 52(4), 378–387.",
 ],

 "pathway": {
  "age": "Often identified in early and middle childhood, when a restricted diet persists beyond the usual fussy-eating years or when growth is affected; also after a precipitating event (choking, vomiting illness) at any age. School-age referrals often come because the child cannot eat at school.",
  "who_diagnoses": "Ireland: paediatrics, CAMHS (including eating disorder teams in some areas), CDNT psychology/psychiatry where there is a disability, or a multidisciplinary feeding service. Dietitians and feeding therapists assess nutrition and feeding skills. The EP does not diagnose.",
  "who_wrote_report": "Paediatrician, dietitian, SLT or OT from a feeding team, CAMHS or CDNT clinician, or a private feeding specialist. Check whether the report is a diagnosis or a description of selective eating.",
  "refer_to": "GP first (growth, bloods, medical causes) → paediatrics and dietetics. SLT/OT feeding team for oral-motor or sensory drivers. CAMHS or Primary Care Psychology for anxiety-driven presentations; CDNT where there is a disability. Pathways vary — check locally.",
  "sooner": "'Lots of children are fussy and grow out of it, so waiting was understandable. What's changed is that it's now affecting his health or his day — and that's exactly the point to get help.'",
 },

 "differential": [
  "TYPICAL PICKY EATING — narrow range but adequate growth, eats socially, no marked distress; eases with time (Taylor et al., 2015).",
  "AUTISTIC SENSORY SELECTIVITY without harm — a real sensory need; ARFID only where consequences meet the threshold.",
  "ANOREXIA NERVOSA — restriction driven by fear of weight gain or body image disturbance. Ask sensitively; specialists decide.",
  "MEDICAL CAUSE — reflux, coeliac disease, allergy, constipation, swallowing difficulty. Medical review first.",
  "LOW MOOD — loss of appetite as part of depression; recent onset, with other mood signs.",
  "NEGLECT OR FOOD INSECURITY — a child with little food rather than a child refusing food. Ask about access; follow the child protection route where indicated.",
 ],

 "next": [
  "Confirm with parents whether there has been a GP/paediatric review of growth and nutrition; if not, recommend it — urgently if weight loss or faltering growth.",
  "Gather a school-day picture: what is eaten, where, with whom, and what happens at trips and food-based lessons.",
  "Agree a no-pressure lunchtime plan and record it in the Student Support File.",
  "Refer or signpost (dietetics, feeding team, CAMHS/CDNT) and agree a review date. If weight-and-shape concerns emerge, switch to the eating disorder route the same day.",
 ],

 "presentations": [
  "Restricted range of foods",
  "Not eating at school",
  "Fear of choking or vomiting",
  "Sensory sensitivity to food textures and smells",
  "Low appetite / forgets to eat",
  "Distress in the canteen",
  "Avoiding school trips or events involving food",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — feeding difficulties are often first raised here, though most early picky eating is typical.",
   "prevalence": "Picky eating is common in early childhood; ARFID rate not stated here — check.",
   "see": "A toddler or preschooler who eats a very small number of foods, gags or vomits with new textures, or has faltering growth. Most referrals at this age belong to paediatrics, dietetics and feeding therapy; the EP role is usually developmental context and preschool advice.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "Vineland-3"],
  },
  "School Age": {
   "applies": "YES — common referral point, because the child cannot eat at school or on trips.",
   "prevalence": "Rate not stated here — check; elevated in autistic and anxious children.",
   "see": "A child who brings the same few foods, does not eat lunch, is distressed in the canteen or avoids parties and trips. Describe impact on the school day and participation; screen for anxiety and autism features; keep the medical review at the front of the plan.",
   "tools": ["SDQ", "RCADS", "Vineland-3",
             "Nine Item ARFID Screen (NIAS; Zickgraf & Ellis, 2018) — AGE developed with adults; child use — check · MEASURES: picky eating, low appetite and fear-based restriction · CANNOT TELL YOU: diagnosis, medical risk or growth status · TIME: about 5 min — specialist screening, check before use"],
  },
  "Adolescent": {
   "applies": "YES — may present for the first time, or persist from childhood.",
   "prevalence": "Rate not stated here — check.",
   "see": "A teenager who avoids eating in front of peers, eats very little all day, or has a fear-of-vomiting pattern. Social isolation and embarrassment are common. Distinguish carefully from anorexia — any weight-and-shape concern changes the route to the eating disorder pathway.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)",
             "Pica, ARFID and Rumination Disorder Interview (PARDI; Bryant-Waugh et al., 2019) — AGE child to adult · MEASURES: presence and profile of ARFID, pica and rumination · CANNOT TELL YOU: anything if used outside specialist training · TIME: 30–60 min — specialist tool, not for EP administration"],
  },
  "Young Adult": {
   "applies": "RARELY — for the school EP; may continue into further education and adult services.",
   "prevalence": "Rate not stated here — check.",
   "see": "A young adult whose restricted diet limits independence, college life, work and relationships. Adult eating disorder or dietetic services lead; the EP role is usually transition planning.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — restricted eating is frequent among children with autism, intellectual disability and complex needs.",
   "prevalence": "Elevated — rate not stated here, check.",
   "see": "A child whose diet is extremely narrow, who may drop foods suddenly, or for whom mealtimes are highly distressing. Check swallowing safety and dental or GI pain first — behaviour may be the only way pain is communicated. Work with the CDNT feeding team; keep mealtimes predictable.",
   "tools": ["Vineland-3 / ABAS-3", "Functional behaviour assessment (ABC)", "Communication Matrix / AAC review"],
  },
 },
},

# =====================================================================================
# 2. PICA
# =====================================================================================
{
 "name": "Pica",
 "code": "DSM-5-TR Pica (feeding and eating disorders chapter) · ICD-11 6B84 Pica — verify codes before quoting",
 "neps": "5. OTHER (5.3 Medical condition or other diagnosis) — and 2. BEHAVIOUR (2.1 Behaviour in class) where it is a safety concern in school",
 "coru": CORU,
 "psi":  PSI,
 "law":  LAW_MED,

 "what_it_is": [
  "PERSISTENT EATING OF NON-NUTRITIVE, NON-FOOD SUBSTANCES over a period of at least ONE MONTH, which is inappropriate to the person's developmental level and not part of a culturally supported or socially normative practice (APA, 2022, DSM-5-TR). Examples: soil, paper, paint chips, chalk, hair, fabric, stones, plaster, ice, soap.",
  "DEVELOPMENTAL LEVEL MATTERS. Mouthing and eating non-food items is normal in infancy. DSM-5-TR suggests a minimum age of about 2 years for diagnosis (APA, 2022 — check the text). In a child with intellectual disability, the relevant comparison is developmental, not chronological, age.",
  "MOST OFTEN SEEN in children and adults with INTELLECTUAL DISABILITY and AUTISM, in young children, and in pregnancy (Williams & McAdam, 2012). It can be missed because it is rarely asked about (Rose, Porcerelli & Neale, 2000).",
  "A MEDICAL QUESTION FIRST. Pica is associated with IRON DEFICIENCY (and sometimes zinc deficiency) — the direction of cause is debated. Risks include lead or other poisoning (e.g., old paint), bowel obstruction or perforation, dental damage, choking and parasitic infection. Any pica needs GP/paediatric review.",
  "IT IS BEHAVIOUR WITH A FUNCTION. Functional assessment often finds it is SENSORY / AUTOMATICALLY REINFORCED (the texture or oral input itself), but it can also be attention-maintained, escape-maintained, or linked to boredom or low stimulation (Williams & McAdam, 2012).",
  "Behavioural interventions — environmental enrichment, safe alternatives with matched sensory properties, teaching discrimination between edible and non-edible, and differential reinforcement — have the strongest evidence base (McAdam, Sherman, Sheldon & Napolitano, 2004; Williams & McAdam, 2012).",
  "For the EP: SAFETY plan first, MEDICAL referral in parallel, then functional assessment and a written behaviour support plan with the school and CDNT.",
 ],

 "what_it_is_not": [
  "NOT normal infant mouthing. Before about age 2, or at an equivalent developmental level, mouthing is exploration.",
  "NOT deliberate self-harm in the usual sense — though it can cause serious harm. Do not assume intent; understand function.",
  "NOT 'naughty'. Punitive responses do not address the sensory or physiological driver and can increase covert pica.",
  "NOT only a behaviour problem. Iron deficiency or other medical factors may be present; a blood test through the GP is part of the picture.",
  "NOT the same as a culturally sanctioned practice (e.g., geophagy in some cultures) — DSM-5-TR excludes culturally supported practices. Ask the family respectfully.",
  "NOT diagnosed separately when it occurs only within another condition and is not severe enough to warrant independent clinical attention (APA, 2022). Many autistic or intellectually disabled children receive support for pica without a separate diagnosis.",
 ],

 "prevalence": [
  "OVERALL: population figures are uncertain and vary with definition — rate not stated here, check before quoting (APA, 2022 notes prevalence is unclear).",
  "INTELLECTUAL DISABILITY: consistently reported as more common, and more common with greater severity of disability (Williams & McAdam, 2012) — check figures before quoting.",
  "AUTISM: elevated — rate not stated here, check.",
  "IRELAND: no Irish figure stated here — check before quoting.",
  "SEX RATIO: not stated here — check.",
 ],

 "cooccurring": [
  {"name": "INTELLECTUAL DISABILITY", "rate": "elevated, higher with greater severity — rate not stated here, check",
   "presents": "eating items from the floor, clothing threads, paper or objects in the environment, often when unoccupied or understimulated. Needs a behaviour support plan and environment check."},
  {"name": "AUTISM", "rate": "elevated — rate not stated here, check",
   "presents": "a strong preference for particular textures in the mouth (chewing sleeves, paper, rubber), often sensory-seeking. A matched safe chew alternative is usually central."},
  {"name": "IRON DEFICIENCY ANAEMIA", "rate": "associated — rate not stated here, check",
   "presents": "craving for ice, soil or clay; tiredness, pallor, poor concentration. Medical assessment and treatment by the GP; the behaviour may reduce once corrected."},
  {"name": "NEGLECT OR UNDERSTIMULATION", "rate": "not stated here — check",
   "presents": "a child in a barren or chaotic environment, hungry or unsupervised. Look at the whole picture; follow the child protection route where there are concerns."},
  {"name": "OBSESSIVE-COMPULSIVE AND ANXIETY PRESENTATIONS", "rate": "not stated here — check",
   "presents": "hair eating (trichophagia) linked to hair pulling, or chewing and swallowing items when anxious. Trichophagia risks a hair bezoar — medical urgency if abdominal pain."},
 ],

 "recommendations": [
  "SAFETY FIRST, WRITTEN DOWN. A risk assessment of the classroom and yard: remove or secure hazardous items (small objects, paint flakes, batteries, magnets, plant material, cleaning products); agree supervision levels at the riskiest times.",
  "MEDICAL REVIEW: 'Parents are advised to discuss this with their GP, including whether blood tests (for example iron levels) are needed.' Any ingestion of batteries, magnets, sharp objects or toxins → emergency medical advice immediately.",
  "FUNCTIONAL BEHAVIOUR ASSESSMENT: ABC recording over a defined period — when, where, what, what happened before and after — to establish function (sensory, attention, escape, boredom).",
  "BEHAVIOUR SUPPORT PLAN based on function: environmental enrichment and structured activity; SAFE ALTERNATIVES with similar sensory properties (e.g., chewable jewellery or tubes recommended by OT, crunchy food agreed with parents); teaching 'food vs not food' discrimination with visuals; redirection without drama; differential reinforcement (Williams & McAdam, 2012).",
  "SNA SUPPORT where the child's care needs meet the scheme's criteria — check the current Department of Education SNA circular and the NCSE process.",
  "CONTINUUM LEVEL: School Support Plus — pica almost always involves outside services (GP/paediatrics, CDNT OT and psychology).",
  "REFER: GP (medical review, bloods); CDNT (OT for sensory alternatives, psychology/behaviour support) where there is a disability; paediatrics; Primary Care Psychology if no disability.",
  "DO NOT use aversive or punitive procedures, and do not advise on supplements or medication (PSI 2.2.2).",
 ],

 "explain_parent": [
  "'Pica means eating things that aren't food. It's more common than people think in children with additional needs, and it's something we can plan for together.'",
  "'The first step is safety and a check with your GP — sometimes low iron or other medical things are part of it, and they can be tested for.'",
  "'For many children the feeling of the thing in their mouth is what they're after. If we can give them something safe that feels similar, the risky eating often reduces.'",
  "'What does he eat, when, and where? Is it worse when he's bored, tired or upset? That helps us work out what it's doing for him.'",
  "SIGNPOST: GP; CDNT keyworker and OT; poisons information advice (the National Poisons Information Centre of Ireland — check current contact details) if a risky item is swallowed; emergency services for batteries, magnets or breathing difficulty.",
 ],

 "explain_teacher": [
  "'This is a recognised condition, not bad behaviour. Our job is to keep her safe and to give her what she's looking for in a safer way.'",
  "'Let's sweep the room for risky items — small bits, paint flakes, crayons that crumble, batteries, magnets.'",
  "'Please record each episode briefly: time, what she ate, what was happening before, what happened after. That tells us what it's for.'",
  "'Redirect calmly to the safe alternative — no big reaction, no telling off. Big reactions can make it more likely.'",
  "'If she swallows something dangerous — a battery, a magnet, anything sharp or a chemical — that's an emergency: follow the school's first aid procedure and call for medical help immediately.'",
 ],

 "explain_child": [
  "YOUNGER / LIMITED LANGUAGE: use visuals — a 'food / not food' sorting board; 'mouth things' box with the safe chew.",
  "OLDER: 'Your mouth really likes chewing and crunching. Some things aren't safe for your tummy. Let's find things that feel good and are safe.'",
  "ASK (where communication allows): 'When do you want to chew?' · 'What does it feel like?' · 'What helps?' — or use a choice board of feelings and times.",
  "OFFER choice among safe alternatives so the child has control.",
 ],

 "analogies": [
  "THE ITCH: 'For some children the need to chew is like an itch. Telling them not to scratch doesn't work; giving them something safe to scratch with does.' Works with teachers and SNAs.",
  "THE SWAP SHOP: 'We're not taking something away, we're swapping it for something safer that does the same job.' Works with parents worried about removing a comfort.",
  "THE EMPTY ROOM: 'In a room with nothing to do, anything becomes interesting — including what's on the floor.' Works when understimulation is a driver.",
 ],

 "language": [
  "Use 'pica' where it has been identified; otherwise describe: 'eats non-food items such as paper and threads'.",
  "Avoid 'disgusting', 'gross', 'naughty' — in front of the child and in writing.",
  "Describe behaviour and function ('appears to seek oral sensory input') rather than labels ('attention-seeking').",
 ],

 "red_flags": [
  "RED FLAG — swallowing batteries (especially button batteries), magnets, sharp objects, or chemicals → EMERGENCY: follow first aid procedure and call 999/112 immediately; do not wait for the next review.",
  "RED FLAG — abdominal pain, vomiting, constipation or swelling in a child with pica → possible obstruction; urgent medical assessment the same day.",
  "RED FLAG — hair eating with abdominal pain → possible hair bezoar; urgent medical review.",
  CP_ROUTE,
  "BOUNDARY — you do not diagnose pica or anaemia, and you do not advise on supplements or medication (PSI 2.2.2).",
  "WATCH — plans that rely only on 'watch him more closely' with no function-based alternative; they tend to fail and exhaust staff.",
 ],

 "child_voice": [
  "OBSERVATION with the child's permission and ABC recording — good because for many children with pica, behaviour is the main communication and needs to be read, not guessed.",
  "TALKING MATS (Murphy, Cameron and colleagues at the University of Stirling) — good because it lets children with limited speech sort activities and feelings into like/dislike and show what helps.",
  "CHOICE-MAKING with real objects (safe chew items) — good because the child's preference among alternatives is the child's voice in the plan.",
 ],

 "questions": [
  "Q: 'Is this dangerous?' — A: 'It can be, depending on what's eaten. That's why the first steps are a safety sweep and a GP check. Batteries, magnets and chemicals are emergencies.'",
  "Q: 'Will he grow out of it?' — A: 'In young children it often fades. In children with additional needs it can persist, but it usually reduces with a good plan that gives him something safe instead.'",
  "Q: 'Should we just tell her no?' — A: 'Calm redirection to something safe works better than telling off. A big reaction can make it more rewarding.'",
  "Q: 'Could it be iron?' — A: 'It can be linked with low iron. Your GP can check with a blood test — that's their decision, not mine.'",
  "Q: 'What's the plan in school?' — A: 'A safe classroom, a record of when it happens, a safe alternative that feels similar, and supervision at the riskiest times. We review it in a few weeks.'",
  "Q: 'Does she need an SNA for this?' — A: 'Possibly, if supervision for safety is a significant care need. That's decided through the NCSE process under the current SNA circular — I can describe the need, but I don't allocate the support.'",
 ],

 "supervision": [
  "Bring the ABC data and your hypothesis about function; ask whether the evidence supports it.",
  "Discuss the risk assessment: who signs it off, how staff are briefed, what happens on trips.",
  "Ask about the CDNT and OT pathway locally and how to link your plan with theirs.",
  "Reflect on any concern that the environment at home or school is understimulating or neglectful, and what threshold applies.",
  "Ask how to word the risk in a report so that it is clear without being alarming or stigmatising.",
 ],

 "reflection": [
  "ON SAFETY — did my recommendations start with a risk assessment and an emergency response, or with behaviour?",
  "ON MEDICAL REVIEW — did I recommend a GP check, and did I avoid suggesting what the test or treatment should be?",
  "ON FUNCTION — was my hypothesis based on data, or on an assumption that it's 'sensory'?",
  "ON DIGNITY — how did I describe the behaviour in writing? Would I be comfortable if the parent read it aloud?",
  "ON THE CHILD'S VOICE — how did I include the child's preferences in the plan?",
  "WHAT GOOD LOOKS LIKE: 'Risk assessment done, GP review recommended, two weeks of ABC data suggest sensory function in unstructured time; safe chew agreed with OT; structured activities added at break; review in four weeks.'",
  "WHAT POOR LOOKS LIKE: 'Staff to say no firmly each time.' — no safety sweep, no medical check, no function.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "McAdam, D. B., Sherman, J. A., Sheldon, J. B., & Napolitano, D. A. (2004). Behavioral interventions to reduce the pica of persons with developmental disabilities. Behavior Modification, 28(1), 45–72.",
  "Rose, E. A., Porcerelli, J. H., & Neale, A. V. (2000). Pica: Common but commonly missed. Journal of the American Board of Family Practice, 13(5), 353–358.",
  "Williams, D. E., & McAdam, D. (2012). Assessment, behavioral treatment, and prevention of pica: Clinical guidelines and recommendations for practitioners. Research in Developmental Disabilities, 33(6), 2050–2057.",
  "Bryant-Waugh, R., Micali, N., Cooke, L., Lawson, E. A., Eddy, K. T., & Thomas, J. J. (2019). Development of the Pica, ARFID, and Rumination Disorder Interview, a multi-informant, semi-structured interview of feeding disorders across the lifespan: A pilot study for ages 10–22. International Journal of Eating Disorders, 52(4), 378–387.",
 ],

 "pathway": {
  "age": "Often noticed in early childhood when mouthing does not fade, or in school-age children with intellectual disability or autism when it becomes a safety concern. Can emerge at any age, including adolescence.",
  "who_diagnoses": "Ireland: paediatrics, CDNT psychology or psychiatry, CAMHS, or adult intellectual disability services. The GP investigates medical factors. The EP does not diagnose.",
  "who_wrote_report": "Paediatrician, CDNT psychologist or behaviour specialist, OT (sensory), or a GP letter. Check whether it includes a functional assessment and medical results.",
  "refer_to": "GP (medical review, bloods) → paediatrics. CDNT (OT, psychology) for children with a disability; Primary Care Psychology otherwise. Emergency services for dangerous ingestion.",
  "sooner": "'Mouthing things is normal for little ones, so it's easy to miss when it keeps going. The important thing is that we're making it safe now and finding out what it's for.'",
 },

 "differential": [
  "DEVELOPMENTALLY APPROPRIATE MOUTHING — in infants or at an equivalent developmental level.",
  "SENSORY-SEEKING CHEWING WITHOUT SWALLOWING — chewing sleeves or pencils is common and not pica unless items are eaten.",
  "HUNGER OR FOOD INSECURITY — eating from bins or taking food is a different question; consider welfare.",
  "TRICHOTILLOMANIA WITH TRICHOPHAGIA — hair pulling with eating; OCD-related pathway.",
  "PSYCHOSIS OR DELUSIONAL BELIEFS — rare in children; eating non-food items for a belief-based reason needs psychiatric review.",
 ],

 "next": [
  "Complete a classroom and yard risk assessment and brief staff on emergency response.",
  "Recommend a GP review, including discussion of iron levels.",
  "Start ABC recording for two weeks and form a function hypothesis.",
  "Agree a function-based plan with the CDNT/OT and review in four weeks.",
 ],

 "presentations": [
  "Eating non-food items",
  "Mouthing and chewing objects",
  "Sensory-seeking behaviour",
  "Hair pulling and eating",
  "Safety concerns in the classroom and yard",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — but only beyond the age at which mouthing is expected (DSM-5-TR suggests about 2 years — check).",
   "prevalence": "Rate not stated here — check.",
   "see": "A toddler or preschooler who persistently eats soil, paint, paper or other items after mouthing would usually fade. Medical review (including iron and lead exposure where old paint is present) is first; the EP supports preschool safety and developmental context.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "Functional behaviour assessment (ABC)"],
  },
  "School Age": {
   "applies": "YES — especially in children with intellectual disability or autism in mainstream or special classes.",
   "prevalence": "Rate not stated here — check; elevated in ID and autism.",
   "see": "Eating paper, crayons, threads or items from the yard, often at unstructured times. Safety plan and GP review first; functional assessment and a written behaviour support plan with CDNT.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3"],
  },
  "Adolescent": {
   "applies": "RARELY — outside intellectual disability, autism or pregnancy.",
   "prevalence": "Rate not stated here — check.",
   "see": "A teenager eating ice, chalk or other items may have iron deficiency; a young person eating hair may have trichotillomania. Medical review first; sensitive exploration of anxiety and mood.",
   "tools": ["Functional behaviour assessment (ABC)", "RCADS self-report"],
  },
  "Young Adult": {
   "applies": "RARELY — for the school EP; relevant to transition into adult disability services.",
   "prevalence": "Rate not stated here — check.",
   "see": "Persisting pica in a young adult with intellectual disability; the plan must travel into adult services. The EP contributes to transition documentation.",
   "tools": ["Vineland-3 adult", "ABAS-3 adult form"],
  },
  "Special Setting": {
   "applies": "YES — the most common setting for pica in school.",
   "prevalence": "Elevated — rate not stated here, check.",
   "see": "Frequent ingestion of items in class or yard, sometimes with limited communication about why. Environment, supervision, safe sensory alternatives and a function-based plan, coordinated with CDNT, OT and SNA support.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3", "Communication Matrix / AAC review"],
  },
 },
},

# =====================================================================================
# 3. RUMINATION DISORDER
# =====================================================================================
{
 "name": "Rumination Disorder",
 "code": "DSM-5-TR Rumination Disorder (feeding and eating disorders chapter) · ICD-11 6B85 Rumination-regurgitation disorder — verify codes before quoting",
 "neps": "5. OTHER (5.3 Medical condition or other diagnosis)",
 "coru": CORU,
 "psi":  PSI,
 "law":  LAW_MED,

 "what_it_is": [
  "REPEATED REGURGITATION OF FOOD after eating, over at least ONE MONTH. The food may be re-chewed, re-swallowed or spat out. It is NOT attributable to a gastrointestinal or other medical condition (e.g., reflux, pyloric stenosis) and does not occur only during another eating disorder (APA, 2022, DSM-5-TR).",
  "EFFORTLESS, not vomiting. The food comes back up without nausea or retching, typically within minutes of eating. Gastroenterology describes this as 'rumination syndrome' (Rome IV criteria; Hyams et al., 2016).",
  "MECHANISM: an unintentional, learned contraction of the abdominal wall muscles pushes stomach contents up. It is behavioural in origin and often not under conscious awareness (Halland, Pandolfino & Barba, 2018).",
  "WHO: infants; children and adults with intellectual disability; and typically developing adolescents and young adults — where it is often misdiagnosed as reflux or bulimia for a long time (Halland et al., 2018).",
  "TREATMENT: the most commonly recommended first-line approach is DIAPHRAGMATIC BREATHING, taught as a competing response after meals, often by a gastroenterology or psychology team (Halland et al., 2018). Medical assessment rules out other causes first.",
  "CONSEQUENCES: weight loss, malnutrition, dental erosion, bad breath, embarrassment and social avoidance — young people may stop eating at school or with friends.",
  "For the EP: support discretion and dignity at school, understand the social impact, and ensure the medical route is in place.",
 ],

 "what_it_is_not": [
  "NOT vomiting from illness. No nausea, no retching; often the food tastes normal.",
  "NOT bulimia. There is no binge and no intent to control weight — but take care: if weight-and-shape concerns are present, the eating disorder route applies.",
  "NOT reflux (GORD), although it is often misdiagnosed as such and treated with reflux medication that does not help (Halland et al., 2018).",
  "NOT deliberate or disgusting behaviour. The young person often cannot stop it without help and is ashamed.",
  "NOT a diagnosis for the school. Only a medical team can exclude other causes.",
  "NOT a reason to exclude the young person from lunch, trips or PE. With privacy arrangements most can take part fully.",
 ],

 "prevalence": [
  "OVERALL: uncertain — rate not stated here, check before quoting (APA, 2022 notes limited data).",
  "INTELLECTUAL DISABILITY: reported as more common — rate not stated here, check.",
  "ADOLESCENTS: probably under-recognised because of misdiagnosis as reflux or vomiting disorders (Halland et al., 2018) — check figures before quoting.",
  "IRELAND: no Irish figure stated here — check.",
  "SEX RATIO: not stated here — check before quoting.",
 ],

 "cooccurring": [
  {"name": "INTELLECTUAL DISABILITY", "rate": "elevated — rate not stated here, check",
   "presents": "regurgitation and re-chewing that may appear self-soothing or self-stimulating, sometimes with weight loss. Behaviour support and medical review together."},
  {"name": "ANXIETY AND DEPRESSION", "rate": "reported in adolescents — rate not stated here, check",
   "presents": "a young person anxious about eating in public, avoiding lunch or social meals, and ashamed of symptoms."},
  {"name": "OTHER EATING DISORDERS", "rate": "not stated here — check",
   "presents": "regurgitation used to control weight, or spitting out to avoid calories. If weight and shape concerns are present, the diagnosis is different."},
  {"name": "FUNCTIONAL GASTROINTESTINAL DISORDERS", "rate": "not stated here — check",
   "presents": "abdominal pain, bloating or constipation alongside regurgitation. Gastroenterology leads."},
 ],

 "recommendations": [
  "MEDICAL FIRST: 'It is recommended that parents discuss the regurgitation with their GP for referral to paediatrics or gastroenterology, if not already in place.'",
  "DISCRETION: access to a private toilet or quiet place after meals; permission to leave class without explanation; water available.",
  "SUPPORT THE TREATMENT PLAN: if diaphragmatic breathing has been taught, agree with the young person whether a discreet reminder or a private space after lunch would help.",
  "PROTECT FROM BULLYING: staff alert to comments; swift response to teasing about smell or spitting.",
  "CONTINUUM LEVEL: Classroom Support for most; School Support where it affects attendance or peer relationships; School Support Plus where outside services are involved.",
  "REFER: GP → paediatrics/gastroenterology; Primary Care or CAMHS psychology where anxiety or low mood is significant; CDNT where there is a disability.",
  "DO NOT diagnose, or suggest the young person is doing it on purpose, and do not comment on food or weight.",
 ],

 "explain_parent": [
  "'Rumination is when food comes back up without being sick. It's a known condition, and it's often a learned muscle habit rather than a stomach illness.'",
  "'The first step is the GP and a gastroenterology or paediatric check, to rule out other causes.'",
  "'There is a treatment that helps many people — a breathing technique taught by the medical team.'",
  "'At school we'll make sure she has privacy and isn't embarrassed or teased.'",
  "SIGNPOST: GP; the treating team's advice sheet; Bodywhys if there are weight or shape concerns.",
 ],

 "explain_teacher": [
  "'This is a medical and behavioural condition, not sickness and not deliberate. She can't just stop.'",
  "'Please let her leave after lunch without asking questions, and keep an eye out for teasing.'",
  "'If she's being sick with nausea, looks unwell, or is losing weight, let the parents know the same day.'",
  "'If she has been given a breathing routine by her medical team, she may want a quiet minute after lunch to do it — please allow that without comment.'",
  "'Don't comment on what she eats — it makes it harder.'",
  "'Treat it as confidential: agree with her and her parents what, if anything, classmates are told, and who on staff needs to know.'",
 ],

 "explain_child": [
  "OLDER: 'This is a real thing — your stomach muscles have learned a habit of pushing food back up. It's not your fault and there's a way to retrain them.'",
  "YOUNGER / LIMITED LANGUAGE: use visuals and a simple after-lunch routine agreed with the family.",
  "ASK: 'What would make lunchtime easier?' · 'Who do you want to know about this?' · 'What do you want people to say if they notice?'",
  "RESPECT privacy: agree what classmates are told, if anything.",
  "DO NOT ask the young person to demonstrate or describe it in detail.",
 ],

 "analogies": [
  "THE HICCUP: 'It's a bit like hiccups — a reflex your body does automatically, not something you choose.' Works with teachers and peers.",
  "THE TYPING HABIT: 'Your muscles have learned a pattern, like typing a password without thinking. Breathing practice teaches a new pattern.' Works with adolescents.",
  "THE WRONG LABEL: 'It's often mistaken for reflux, which is why it can take a long time to find the right help.' Works with parents frustrated by delay.",
 ],

 "language": [
  "Say 'regurgitation' or 'bringing food back up', not 'vomiting' or 'being sick'.",
  "Avoid 'disgusting', 'gross', 'attention-seeking'.",
  "Use the young person's preferred explanation for peers, if any.",
  "In reports, write 'regurgitation after meals, under medical review' rather than 'spits food out' — factual, dignified, not blaming.",
 ],

 "red_flags": [
  "RED FLAG — weight loss, dehydration, fainting or blood in regurgitated material → parent the same day, urgent GP.",
  "RED FLAG — statements about weight, calories or body shape → consider an eating disorder; urgent GP and CAMHS route.",
  "RED FLAG — low mood, self-harm or suicidal thoughts (shame and social withdrawal can be marked) → same-day risk route: ask directly, inform parents unless that would increase risk, contact GP/CAMHS, emergency services if imminent; tell your supervisor the same day.",
  CP_ROUTE,
  "BOUNDARY — you do not diagnose rumination or advise on medication or breathing technique (PSI 2.2.2). Follow the treating team's plan.",
 ],

 "child_voice": [
  "SOLUTION-FOCUSED PUPIL INTERVIEW — good because it keeps the focus on what the young person wants school to be like and on small, controllable changes.",
  "PRIVATE WRITTEN CHECK-IN (e.g., a short note to a trusted adult) — good because the topic is embarrassing and some young people cannot say it aloud.",
  "TALKING MATS for young people with limited speech — good because it lets them show whether lunchtime, toilets or peers are difficult.",
  "SCALING of lunchtime comfort (0–10) over a few weeks — good because it gives the young person a simple way to show change without describing symptoms.",
 ],

 "questions": [
  "Q: 'Is she doing it on purpose?' — A: 'No. It's usually an automatic muscle habit. She needs help to retrain it, not to be told off.'",
  "Q: 'Is it bulimia?' — A: 'Not usually — there's no bingeing and it's not about weight. But if she ever talks about weight or shape, we'd refer urgently.'",
  "Q: 'Why didn't reflux medicine work?' — A: 'Because it's a different problem. A gastroenterologist can confirm that — it's their call.'",
  "Q: 'What can school do?' — A: 'Privacy after meals, no questions, no comments, and a quick response to any teasing.'",
  "Q: 'Will it go away?' — A: 'With the right treatment many young people improve. The treating team will tell you what to expect.'",
  "Q: 'What do we tell the class?' — A: 'Only what she and her parents want. Often the answer is nothing, or \'it's a medical thing and it's private\'. Teasing is dealt with under the anti-bullying policy.'",
  "Q: 'Should she skip lunch in school to avoid it?' — A: 'No — missing meals is a problem in itself. The aim is that she can eat with privacy and support. If she's avoiding eating, that's something to tell her GP.'",
 ],

 "supervision": [
  "Discuss the differential between rumination, reflux and bulimia, and how to raise weight-and-shape questions sensitively.",
  "Ask what gastroenterology or psychology pathways exist locally for rumination syndrome.",
  "Bring any case of a child with intellectual disability where regurgitation is part of a behavioural pattern.",
  "Reflect on how you talk about a topic that the young person finds shameful.",
  "Agree what you will share with the school and what stays confidential.",
 ],

 "reflection": [
  "ON THE MEDICAL ROUTE — did I confirm who is managing this medically?",
  "ON SHAME — did the young person leave with more dignity or less?",
  "ON DIFFERENTIAL — did I consider an eating disorder and ask about weight and shape sensitively?",
  "ON PEERS — have I addressed teasing and what classmates know?",
  "ON MY ROLE — did I stay within describing impact and supporting the plan?",
  "ON LANGUAGE — did my report describe regurgitation neutrally, without words that would embarrass the young person if they read it?",
  "WHAT GOOD LOOKS LIKE: 'GP referral confirmed; private space after lunch agreed with the young person; staff briefed not to comment; bullying response in place; review with the pupil in four weeks.'",
  "WHAT POOR LOOKS LIKE: 'She should stop spitting in class.' — misreads the condition and increases shame.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "Halland, M., Pandolfino, J., & Barba, E. (2018). Diagnosis and treatment of rumination syndrome. Clinical Gastroenterology and Hepatology, 16(10), 1549–1555.",
  "Hyams, J. S., Di Lorenzo, C., Saps, M., Shulman, R. J., Staiano, A., & van Tilburg, M. (2016). Childhood functional gastrointestinal disorders: Child/adolescent. Gastroenterology, 150(6), 1456–1468.",
  "Bryant-Waugh, R., Micali, N., Cooke, L., Lawson, E. A., Eddy, K. T., & Thomas, J. J. (2019). Development of the Pica, ARFID, and Rumination Disorder Interview, a multi-informant, semi-structured interview of feeding disorders across the lifespan: A pilot study for ages 10–22. International Journal of Eating Disorders, 52(4), 378–387.",
 ],

 "pathway": {
  "age": "Infancy (usually medical/paediatric), in children and adults with intellectual disability, and in adolescence, where it is often misdiagnosed as reflux or vomiting for months before recognition.",
  "who_diagnoses": "Ireland: paediatrics or gastroenterology (after ruling out other causes), sometimes with CAMHS or psychology input; CDNT or intellectual disability services where relevant. The EP does not diagnose.",
  "who_wrote_report": "Gastroenterologist, paediatrician, psychologist in a gastroenterology or CAMHS service, or a GP letter.",
  "refer_to": "GP → paediatrics/gastroenterology. CAMHS or Primary Care Psychology if anxiety, low mood or eating disorder concerns. CDNT where there is a disability.",
  "sooner": "'This is often mistaken for reflux, so it can take a long time to get the right name. What matters is that she's now on the right route.'",
 },

 "differential": [
  "GASTRO-OESOPHAGEAL REFLUX DISEASE — medical; different mechanism.",
  "BULIMIA NERVOSA — regurgitation or vomiting with weight-and-shape concerns.",
  "ARFID — food avoidance without regurgitation.",
  "CYCLICAL VOMITING OR OTHER GI CONDITIONS — medical assessment.",
  "ANXIETY-RELATED NAUSEA OR VOMITING — vomiting with nausea before school or tests; different from effortless regurgitation after eating.",
 ],

 "next": [
  "Check whether GP/gastroenterology review is in place; recommend if not.",
  "Agree privacy and anti-bullying arrangements with the young person and school.",
  "Screen sensitively for mood, anxiety and weight-and-shape concerns; refer if present.",
 ],

 "presentations": [
  "Regurgitation after meals",
  "Avoiding eating at school",
  "Embarrassment and social withdrawal",
  "Weight loss",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — for the EP; infant rumination is a paediatric matter.",
   "prevalence": "Rate not stated here — check.",
   "see": "Infants or young children regurgitating and re-chewing food, sometimes linked to understimulation. Paediatrics leads; EP involvement is rare and usually developmental context.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)"],
  },
  "School Age": {
   "applies": "RARELY — outside intellectual disability.",
   "prevalence": "Rate not stated here — check.",
   "see": "Regurgitation after meals, sometimes misread as illness or bad manners. Medical review; privacy arrangements; check for bullying.",
   "tools": ["SDQ", "Functional behaviour assessment (ABC)"],
  },
  "Adolescent": {
   "applies": "YES — the most common school-age presentation in typically developing young people.",
   "prevalence": "Rate not stated here — check.",
   "see": "A teenager bringing food back up after meals, avoiding eating in public, embarrassed and possibly losing weight. Often previously treated for reflux. Medical route, discretion, and screening for mood and eating disorder concerns.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)"],
  },
  "Young Adult": {
   "applies": "RARELY — for the school EP.",
   "prevalence": "Rate not stated here — check.",
   "see": "Persistent regurgitation affecting college or work life; adult gastroenterology and psychology lead.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — more often seen in children with intellectual disability.",
   "prevalence": "Elevated — rate not stated here, check.",
   "see": "Regurgitation and re-chewing as part of a behavioural pattern, sometimes with weight loss. Medical review, functional assessment and a plan with the CDNT.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3"],
  },
 },
},

# =====================================================================================
# 4. ANOREXIA NERVOSA
# =====================================================================================
{
 "name": "Anorexia Nervosa",
 "code": "DSM-5-TR Anorexia Nervosa (restricting type / binge-eating–purging type) · ICD-11 6B80 Anorexia Nervosa — verify codes and subcodes before quoting",
 "neps": "3. EMOTIONAL (3.4 Mood; 3.7 Risk and safeguarding) — and 5. OTHER (5.3 Medical condition or other diagnosis)",
 "coru": CORU,
 "psi":  PSI,
 "law":  LAW_ED,

 "what_it_is": [
  "A serious mental illness with PHYSICAL consequences. DSM-5-TR core features: (A) RESTRICTION of energy intake leading to significantly low body weight for age, sex, developmental trajectory and physical health; (B) intense FEAR OF GAINING WEIGHT or persistent behaviour that interferes with weight gain; (C) DISTURBANCE in the way body weight or shape is experienced, undue influence of weight/shape on self-evaluation, or persistent lack of recognition of the seriousness of low weight (APA, 2022). Read the full criteria before quoting.",
  "TWO SUBTYPES: RESTRICTING (dieting, fasting, excessive exercise) and BINGE-EATING/PURGING (also bingeing and/or vomiting, laxatives, diuretics). Amenorrhoea is no longer a criterion (removed in DSM-5, 2013).",
  "IN CHILDREN AND ADOLESCENTS, 'low weight' includes FAILURE TO MAKE EXPECTED GAINS in a growing young person — a teenager whose weight stays static while they grow in height is losing ground. This is assessed by medical professionals using growth data, not by school staff.",
  "ATYPICAL ANOREXIA (DSM-5-TR 'other specified feeding or eating disorder'): all features present but weight within or above the normal range after significant loss. It can be as medically dangerous as typical anorexia. WEIGHT ALONE DOES NOT TELL YOU HOW ILL SOMEONE IS (RCPsych, 2022, MEED).",
  "MORTALITY IS MARKEDLY ELEVATED — the highest of the eating disorders in the Arcelus, Mitchell, Wales & Nielsen (2011) meta-analysis, from medical complications and suicide; it is often described as among the highest of any psychiatric condition (check the source before quoting that comparison). Early identification and treatment improve outcome; this is why the EP must act quickly and never 'wait and see'.",
  "MULTIFACTORIAL: genetic heritability, temperament (perfectionism, anxiety, harm avoidance), puberty, sociocultural pressure and dieting, life events (Treasure, Duarte & Schmidt, 2020). No single cause, and not caused by parents.",
  "TREATMENT (children and young people): NICE NG69 (2017; check for updates) recommends ANOREXIA-FOCUSED FAMILY THERAPY as first-line, with individual CBT-ED or adolescent-focused psychotherapy as alternatives. In Ireland, treatment is through CAMHS and CAMHS eating disorder teams under the HSE Model of Care (HSE, 2018) — service availability varies; check locally.",
  "THE EP's JOB: recognise, raise concern with parents the same day, route to the GP urgently, support the school to follow the treating team's plan, and keep the school a safe, non-triggering place. NOT to diagnose, weigh, or treat.",
 ],

 "what_it_is_not": [
  "NOT a lifestyle choice, diet or vanity. It is a serious mental illness; the young person often cannot 'just eat' (Treasure et al., 2020).",
  "NOT only in thin, white, affluent teenage girls. Boys and men, children, people from all backgrounds, and people at any body size develop anorexia; boys are under-recognised, often presenting with exercise and muscularity concerns.",
  "NOT excluded by 'normal weight'. Atypical anorexia is serious; rapid weight loss is dangerous regardless of starting weight (RCPsych, 2022).",
  "NOT caused by parents. Family is the main treatment resource in NICE-recommended family therapy (NICE, 2017; Eisler et al., 2016). Blaming families is inaccurate and harmful.",
  "NOT something school can monitor by weighing. Weighing and weight comments in school can worsen the illness; weight monitoring is for the treating team.",
  "NOT 'attention seeking'. Many young people hide their illness for a long time.",
  "NOT resolved when weight is restored. Thoughts and behaviours often persist; relapse is common around transitions and exams.",
 ],

 "prevalence": [
  "OVERALL: DSM-5-TR reports a 12-month prevalence among young females of around 0.4% (APA, 2022 — US data; check before quoting). Lifetime estimates vary by method — check.",
  "IRELAND: the HSE Model of Care for eating disorders (HSE, 2018) gives estimates of need — check the document before quoting any Irish figure.",
  "AGE: onset most commonly in adolescence and young adulthood; onset before puberty is less common (APA, 2022).",
  "SEX RATIO: DSM-5-TR reports a female:male ratio in clinical populations of approximately 10:1 (APA, 2022 — check). Males are probably under-identified.",
  "MORTALITY: markedly elevated compared with peers (Arcelus et al., 2011) — check figures before quoting.",
  "AUTISM: autistic people are over-represented among those with anorexia (Westwood & Tchanturia, 2017) — rate not stated here, check.",
 ],

 "cooccurring": [
  {"name": "ANXIETY DISORDERS AND OCD", "rate": "commonly co-occur — rate not stated here, check",
   "presents": "perfectionism, rigid routines, checking, fear of mistakes; anxiety often predates the eating disorder. Treatment of the eating disorder comes first under the treating team."},
  {"name": "DEPRESSION AND SELF-HARM", "rate": "elevated — rate not stated here, check",
   "presents": "low mood, withdrawal, hopelessness and self-harm. Starvation itself lowers mood and narrows thinking. Suicidal risk must be asked about directly."},
  {"name": "AUTISM", "rate": "over-represented (Westwood & Tchanturia, 2017) — rate not stated here, check",
   "presents": "rigid food rules, sensory restriction, need for sameness and social difficulty. Can be missed in girls; treatment may need adaptation."},
  {"name": "TYPE 1 DIABETES", "rate": "risk of disordered eating is elevated — check",
   "presents": "insulin omission to lose weight ('diabulimia'), unstable blood sugars, missed clinic appointments. Very high medical risk — the diabetes team must be informed."},
  {"name": "HIGH-ACHIEVING, PERFECTIONIST PROFILE", "rate": "not a diagnosis — frequently described",
   "presents": "a conscientious, 'model' pupil whose grades are good and who is praised for discipline and exercise. Their competence can hide the illness."},
  {"name": "ARFID", "rate": "not stated here — check",
   "presents": "restriction without weight-and-shape concerns. The distinction is made by specialists; the two can be confused."},
 ],

 "recommendations": [
  "SAME-DAY ACTION WHEN CONCERN IS RAISED: speak with parents the same day; advise an URGENT GP appointment. Where medical signs are present (fainting, chest pain, dizziness, cold, rapid weight loss), advise the GP that day; if collapse or confusion, call 999/112. Tell your supervisor the same day.",
  "FOLLOW THE TREATING TEAM'S PLAN IN SCHOOL. Ask (with consent) for written guidance on lunch and snack supervision, PE and sport participation, and activity limits. School does not decide these; the treating team does.",
  "NO WEIGHING, MEASURING OR BMI WORK in school for this pupil — and ideally for any pupil. Avoid calorie-counting projects, 'healthy vs unhealthy' food lessons, weight-based fitness targets, and before/after body talk. Consistent with eating-disorder charities' guidance for schools (e.g., Bodywhys — check current resources).",
  "NO COMMENTS on weight, appearance, food or exercise — including praise ('you look well') and concern ('you've lost weight') in front of others.",
  "ACADEMIC ADJUSTMENTS: reduced workload during treatment and recovery; flexible timetable for appointments; realistic, not perfectionist, targets; exam arrangements discussed with the treating team (check current SEC Reasonable Accommodations guidance for what applies).",
  "RETURN TO SCHOOL after admission: a reintegration meeting with the family and treating team; agreed key adult; phased return where advised.",
  "CONTINUUM LEVEL: School Support Plus — CAMHS or another specialist service will be involved. The Student Support File records the school plan, not medical details beyond what is needed.",
  "REFER: GP (urgent) → CAMHS / CAMHS eating disorder team. SIGNPOST Bodywhys for family support. DO NOT diagnose, weigh, set food plans, or advise on medication (PSI 2.2.2).",
 ],

 "explain_parent": [
  "'I'm concerned about some of what school has noticed, and I wanted to talk to you today rather than wait. [Describe specific observations — not weight.]'",
  "'I'd strongly advise a GP appointment as soon as possible — ideally this week, and today if she's fainting, dizzy or very cold. Eating disorders can affect the heart and body before anyone looks unwell.'",
  "'You didn't cause this. Families are actually the most important part of treatment for young people — the recommended treatment involves the whole family.'",
  "'The earlier treatment starts, the better the outlook. It's right to act now.'",
  "'At school we'll follow whatever the treating team advises — about lunch, PE, and workload — and we won't comment on food or weight.'",
  "SIGNPOST: GP; CAMHS via GP referral; Bodywhys (The Eating Disorders Association of Ireland) — helpline, support groups and family programmes — check current contact details and services at bodywhys.ie.",
 ],

 "explain_teacher": [
  "'This is a serious medical and mental health condition. The treating team leads; our job is to follow their plan and keep school safe.'",
  "'Please don't comment on her weight, looks or food — good or bad. Even praise like \"you look healthy\" can be heard as \"you've got fat\".'",
  "'PE, sport and lunch arrangements come from the treating team. If you're not sure, ask — don't decide on the spot.'",
  "'Watch for fainting, dizziness, being very cold, or looking unwell — tell the parents and the principal the same day.'",
  "'Check class materials: no calorie projects, no weighing, no \"good food / bad food\" posters. That protects every pupil, not just her.'",
  "'She may be driving herself hard academically. Help her aim for good enough, not perfect.'",
 ],

 "explain_child": [
  "OLDER (after concern has been raised): 'I've noticed you seem to be finding things hard, and I care about how you're doing. Can we talk about it?' — curious, not confrontational; describe what you've noticed, not weight.",
  "OLDER: 'Some people get caught in a pattern with food and their body that's really hard to get out of alone. It's an illness, not a weakness, and there's help.'",
  "ASK directly and calmly about safety: 'Have you felt dizzy or fainted? Have you ever thought about hurting yourself or not wanting to be alive?'",
  "EXPLAIN LIMITS of confidentiality BEFORE they tell you more: 'If I'm worried about your safety, I'll need to tell your parents and get you help — I'll tell you first.'",
  "YOUNGER (late primary): simple, reassuring: 'Your body needs fuel to grow, think and play. Some worries can make eating really hard. The grown-ups will help.'",
  "DO NOT argue about weight, debate food, or ask them to prove they eat. Expect denial; it is part of the illness, not lying.",
 ],

 "analogies": [
  "THE BULLY IN THE HEAD: 'Many young people describe the illness as a voice that bullies them about food. We're on her side against it — not against her.' Works with parents and teachers; externalising the illness is a common element of family-based treatment (see NICE, 2017; check the treating team's approach).",
  "THE CAR WITH NO FUEL: 'You can't drive a car on an empty tank however well it's built. The brain and heart need fuel to work.' Works with teachers and older pupils.",
  "THE ICEBERG: 'What you see — food and weight — is the tip. Underneath are anxiety, perfectionism and feelings that are hard to handle.' Works with staff groups.",
  "THE RESCUE: 'When someone is drowning, you don't wait for them to ask for help.' Works with parents hesitant to push for an appointment.",
 ],

 "language": [
  "Say 'a young person with anorexia' or 'who is experiencing an eating disorder', not 'an anorexic'.",
  "Avoid weight numbers, BMI and descriptions of the body in reports and meetings with staff. Record 'under the care of [service]' and the school plan.",
  "Avoid 'attention seeking', 'vain', 'manipulative', 'just eat'.",
  "Avoid praising weight loss or 'healthy choices' in any pupil — school language shapes risk for all.",
  "Many people in recovery prefer 'recovery' to 'cure'; follow the young person's language.",
 ],

 "red_flags": [
  ED_MEDICAL_RISK,
  ED_SUICIDE_RISK,
  "RED FLAG — a young person with type 1 diabetes who is losing weight or skipping insulin → same day to parents and the diabetes team via GP.",
  CP_ROUTE,
  "BOUNDARY — you do not diagnose, weigh, set meal plans, or advise on medication or admission (PSI 2.2.2). You recognise, act, record, refer and support the school plan.",
  "BOUNDARY — confidentiality cannot be promised where there is risk. For 16- and 17-year-olds, consent and information-sharing are legally complex in Ireland — check with your supervisor before acting on the young person's wish not to tell parents.",
  "WATCH — the high-achieving, compliant pupil who exercises intensely and skips lunch. Competence can hide serious illness.",
 ],

 "child_voice": [
  "SOLUTION-FOCUSED CONVERSATION about school (not food) — good because it builds trust and finds what the young person wants school to be like, while the treating team handles the illness.",
  "WRITTEN OR TYPED CHECK-IN — good because some young people find it easier to write about feelings than say them aloud.",
  "MFQ OR RCADS SELF-REPORT completed WITH the young person — good because it opens discussion of mood and anxiety, with the EP present to follow up any risk item that session.",
  "YOUNG PERSON'S INPUT TO THE SCHOOL PLAN (what helps at lunch, in PE, in class, who should know) — good because control is a central theme; giving real choice where safe supports engagement.",
 ],

 "questions": [
  "Q: 'Should the school weigh her to keep an eye on things?' — A: 'No. Weighing is done by the treating team, in a planned way. In school it can make the illness worse.'",
  "Q: 'Can she do PE?' — A: 'That's a medical decision. Ask the treating team for written advice; until then, follow their guidance.'",
  "Q: 'She says she's fine and eats loads. Should we believe her?' — A: 'Denial is part of the illness, not lying. We don't argue with her — we pass our concerns to her parents and the GP.'",
  "Q: 'Did we cause this by the healthy-eating week?' — A: 'No single thing causes anorexia. But it's a good moment to review how school talks about food and bodies, for everyone.'",
  "Q: 'She's a normal weight — can it still be anorexia?' — A: 'Yes. It can be serious at any weight. Doctors decide; our job is to raise the concern.'",
  "Q: 'She's asked me not to tell her parents.' — A: 'I understand why she'd ask. But this is a safety issue and parents need to know so she can get help. I'll tell her I'm doing it and support her through it.'",
  "Q: 'How long does recovery take?' — A: 'It varies and can take a long time. Early treatment helps. The treating team is best placed to say.'",
 ],

 "supervision": [
  "Bring any first concern the same day — this is not a 'next supervision' matter.",
  "Discuss how to raise the concern with parents without alarming or blaming.",
  "Ask about local routes: CAMHS eating disorder team availability, GP turnaround, what happens if the GP does not refer.",
  "Reflect on consent and confidentiality for 16–17-year-olds, and what the service's policy says.",
  "Reflect on your own relationship with food, weight and body — it affects what you notice and say.",
 ],

 "reflection": [
  "ON SPEED — did I act the same day? What delayed me, if anything?",
  "ON MEDICAL RISK — did I ask about fainting, dizziness, chest pain and self-harm?",
  "ON LANGUAGE — did my report avoid weight numbers and body descriptions?",
  "ON THE FAMILY — did the parents leave feeling blamed or supported?",
  "ON SCHOOL CULTURE — did my recommendations reduce weight talk for all pupils?",
  "WHAT GOOD LOOKS LIKE: 'Concern raised with parents the same day; urgent GP appointment advised; supervisor informed; after CAMHS involvement, the school plan followed the team's written advice on lunch and PE; no weighing; reduced homework; review with the young person and parents.'",
  "WHAT POOR LOOKS LIKE: 'Recommend the school monitor her weight weekly and encourage healthy choices.' — oversteps role, adds harm, delays referral.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "Arcelus, J., Mitchell, A. J., Wales, J., & Nielsen, S. (2011). Mortality rates in patients with anorexia nervosa and other eating disorders: A meta-analysis of 36 studies. Archives of General Psychiatry, 68(7), 724–731.",
  "Health Service Executive. (2018). Eating disorder services: HSE model of care for Ireland. HSE National Clinical Programme for Eating Disorders & College of Psychiatrists of Ireland. — check for updates.",
  "Eisler, I., Simic, M., Hodsoll, J., Asen, E., Berelowitz, M., Connan, F., Ellis, G., Hugo, P., Schmidt, U., Treasure, J., Yi, I., & Landau, S. (2016). A pragmatic randomised multi-centre trial of multifamily and single family therapy for adolescent anorexia nervosa. BMC Psychiatry, 16, 422.",
  "National Institute for Health and Care Excellence. (2017). Eating disorders: Recognition and treatment (NICE Guideline NG69). https://www.nice.org.uk/guidance/ng69 — check for updates.",
  "Royal College of Psychiatrists. (2022). Medical emergencies in eating disorders (MEED): Guidance on recognition and management (College Report CR233). — check for updates.",
  "Treasure, J., Duarte, T. A., & Schmidt, U. (2020). Eating disorders. The Lancet, 395(10227), 899–911.",
  "Westwood, H., & Tchanturia, K. (2017). Autism spectrum disorder in anorexia nervosa: An updated literature review. Current Psychiatry Reports, 19(7), 41.",
 ],

 "pathway": {
  "age": "Most often identified in adolescence (early to mid-teens), often around puberty, transition to post-primary, exam years or sports focus. Onset in late primary is seen. Identification is often delayed because early signs are praised as 'healthy'.",
  "who_diagnoses": "Ireland: CAMHS (including specialist CAMHS eating disorder teams where available), child and adolescent psychiatry, or adult eating disorder services from 18. GP and paediatrics assess medical risk. The EP does not diagnose.",
  "who_wrote_report": "CAMHS psychiatrist or psychologist, CAMHS eating disorder team, paediatrician (medical), a private psychiatrist, or discharge summary after admission. Check whether it includes guidance for school.",
  "refer_to": "GP URGENTLY (same day if medical signs) → CAMHS / CAMHS eating disorder team. Emergency services if collapse or imminent risk. Bodywhys for family support.",
  "sooner": "'It's very common for early signs to look like healthy eating or being sporty, so don't blame yourselves. The important thing is that we're acting now, and early treatment really helps.'",
 },

 "differential": [
  "ARFID — restriction without fear of weight gain or body image disturbance.",
  "MEDICAL CAUSES OF WEIGHT LOSS — coeliac disease, inflammatory bowel disease, thyroid, diabetes, cancer. The GP assesses these.",
  "DEPRESSION — appetite loss with low mood, without weight-and-shape preoccupation.",
  "BULIMIA NERVOSA — binge–purge cycles without significantly low weight.",
  "OCD — food rituals driven by contamination fears rather than weight.",
  "FOOD INSECURITY OR NEGLECT — not enough food available; child protection route.",
 ],

 "next": [
  "Speak with parents the same day; advise urgent GP; inform supervisor the same day.",
  "Ask directly about medical symptoms and self-harm; follow the same-day routes as needed.",
  "With consent, request written guidance for school from the treating team.",
  "Agree the school plan: key adult, lunch, PE, workload, language; record in the Student Support File; set a review.",
 ],

 "presentations": [
  "Restrictive eating and skipping lunch",
  "Excessive exercise",
  "Preoccupation with weight, shape or calories",
  "Perfectionism and academic overdrive",
  "Social withdrawal around food",
  "Fainting or dizziness in school",
  "Low mood and self-harm",
 ],

 "bands": {
  "Early Years": {
   "applies": "N/A — anorexia nervosa is not a presentation at this age; restricted eating in early years is a feeding question (see ARFID).",
   "prevalence": "Not applicable — see ARFID and typical picky eating.",
   "see": "Not seen. A young child who restricts food needs medical review and a feeding assessment; body-image language in a very young child warrants a conversation with parents and GP.",
   "tools": [],
  },
  "School Age": {
   "applies": "RARELY — but onset in late primary (10–12) is seen and easily missed.",
   "prevalence": "Rate not stated here — check; lower than in adolescence.",
   "see": "An older primary pupil who has stopped eating lunch, talks about 'healthy' or 'bad' food, exercises obsessively or has lost weight. Early onset can progress quickly and growth can be affected. Same-day parent conversation and urgent GP.",
   "tools": ["SDQ", "RCADS",
             "Children's Eating Attitudes Test (ChEAT; Maloney, McGuire & Daniels, 1988) — AGE about 8–13 · MEASURES: eating attitudes and dieting behaviour · CANNOT TELL YOU: diagnosis or medical risk; not for EP screening in isolation · TIME: about 10 min — check current use"],
  },
  "Adolescent": {
   "applies": "YES — peak onset band.",
   "prevalence": "DSM-5-TR 12-month prevalence around 0.4% in young females (US) — check before quoting.",
   "see": "Skipping meals, rigid food rules, intense exercise, baggy clothes, withdrawal from friends, perfectionism and falling concentration. Boys may present through muscularity and exercise. Same-day action; urgent GP; CAMHS; school follows the treating team's plan.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Beck Youth Inventories-2",
             "Eating Disorder Examination Questionnaire (EDE-Q; Fairburn & Beglin, 1994) — AGE adolescents and adults (adolescent norms — check) · MEASURES: restraint and eating, shape and weight concerns · CANNOT TELL YOU: medical risk or diagnosis; specialist-team measure, not for EP use · TIME: about 15 min"],
  },
  "Young Adult": {
   "applies": "YES — onset and relapse at transition to college and independence.",
   "prevalence": "Rate not stated here — check.",
   "see": "A young adult at college whose eating disorder begins or relapses away from family. Transition from CAMHS to adult services is a known risk point; plan with the treating team.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — especially autistic young people, where presentation may differ.",
   "prevalence": "Autistic people over-represented among those with anorexia (Westwood & Tchanturia, 2017) — rate not stated here, check.",
   "see": "Rigid food rules and sensory restriction that intensify, with emerging weight-and-shape concerns; or anxiety-driven restriction in a young person with limited ability to describe it. Treatment may need autism-informed adaptation; the school provides predictability and follows the plan.",
   "tools": ["Vineland-3 / ABAS-3", "RCADS self-report"],
  },
 },
},

# =====================================================================================
# 5. BULIMIA NERVOSA
# =====================================================================================
{
 "name": "Bulimia Nervosa",
 "code": "DSM-5-TR Bulimia Nervosa · ICD-11 6B81 Bulimia Nervosa — verify codes before quoting",
 "neps": "3. EMOTIONAL (3.4 Mood; 3.7 Risk and safeguarding) — and 5. OTHER (5.3 Medical condition or other diagnosis)",
 "coru": CORU,
 "psi":  PSI,
 "law":  LAW_ED,

 "what_it_is": [
  "An eating disorder of RECURRENT BINGE EATING followed by INAPPROPRIATE COMPENSATORY BEHAVIOUR to prevent weight gain — self-induced vomiting, laxative or diuretic misuse, fasting or excessive exercise — with self-evaluation unduly influenced by body shape and weight (APA, 2022, DSM-5-TR). First described by Russell (1979).",
  "BINGE = eating an amount of food larger than most people would in a similar period, WITH A SENSE OF LOSS OF CONTROL (APA, 2022). Loss of control is the key subjective feature.",
  "FREQUENCY: DSM-5-TR requires binges and compensatory behaviour, on average, at least once a week for three months (APA, 2022 — check). Specialists judge severity.",
  "WEIGHT IS USUALLY IN OR ABOVE THE 'NORMAL' RANGE. This makes bulimia HIDDEN — the young person does not look ill, and often goes to great lengths to conceal it.",
  "THE BINGE–PURGE CYCLE: strict dieting → hunger and emotional triggers → binge → shame → purging or restriction → more dieting (Fairburn, 2008). It is maintained by dieting and shame, not by lack of willpower.",
  "MEDICAL RISK: vomiting and laxative misuse cause ELECTROLYTE DISTURBANCE (especially low potassium), which can affect heart rhythm; also dehydration, dental erosion, swollen salivary glands and oesophageal damage (RCPsych, 2022). The risk is not visible.",
  "TREATMENT (young people): NICE NG69 (2017; check for updates) recommends BULIMIA-FOCUSED FAMILY THERAPY as first-line, with individual CBT-ED as an alternative. In Ireland, through CAMHS and eating disorder services (HSE, 2018).",
 ],

 "what_it_is_not": [
  "NOT greed or lack of self-control. Dieting and restriction drive bingeing (Fairburn, 2008; Stice, 2002).",
  "NOT 'less serious' than anorexia. Medical risk (especially electrolyte disturbance) and suicide risk are elevated (Arcelus et al., 2011).",
  "NOT confined to girls or to any body size.",
  "NOT only vomiting. Compensatory behaviour includes fasting, laxatives, diuretics, exercise and, in type 1 diabetes, insulin omission.",
  "NOT a secret the school should keep. Once staff suspect it, parents need to know and the GP needs to be involved.",
  "NOT fixed by nutrition advice alone. It is a psychological disorder with a specific evidence-based treatment.",
 ],

 "prevalence": [
  "OVERALL: DSM-5-TR reports a 12-month prevalence of around 1%–1.5% among young females (APA, 2022 — US data; check before quoting).",
  "IRELAND: check the HSE Model of Care (HSE, 2018) and Bodywhys for current Irish estimates before quoting.",
  "AGE: onset typically in adolescence or young adulthood (APA, 2022).",
  "SEX RATIO: DSM-5-TR reports a female:male ratio in clinical populations of approximately 10:1 (check). Males under-identified.",
  "HIDDEN: many cases are never seen by services — rate not stated here, check.",
 ],

 "cooccurring": [
  {"name": "DEPRESSION", "rate": "commonly co-occurs — rate not stated here, check",
   "presents": "low mood, shame and self-criticism following binges; withdrawal; falling schoolwork. Direct question about suicide needed."},
  {"name": "SELF-HARM AND SUICIDALITY", "rate": "elevated (Arcelus et al., 2011) — check",
   "presents": "self-injury alongside bulimic behaviour, often in secret. Same-day risk route."},
  {"name": "ANXIETY DISORDERS", "rate": "commonly co-occur — rate not stated here, check",
   "presents": "social anxiety, body-focused anxiety, fear of eating in public."},
  {"name": "SUBSTANCE USE", "rate": "elevated — rate not stated here, check",
   "presents": "alcohol or drug use in older adolescents, sometimes alongside impulsive behaviour."},
  {"name": "ADHD", "rate": "associated — rate not stated here, check",
   "presents": "impulsivity and emotional dysregulation contributing to binge episodes."},
  {"name": "TYPE 1 DIABETES", "rate": "elevated risk of disordered eating — check",
   "presents": "insulin omission as a purging behaviour; very high medical risk. Diabetes team must be informed."},
 ],

 "recommendations": [
  "SAME-DAY ACTION on concern: speak with parents the same day; advise an urgent GP appointment; tell your supervisor the same day. If vomiting blood, collapse or chest pain — 999/112.",
  "FOLLOW THE TREATING TEAM'S PLAN for lunch, toilet access after meals, PE and workload. Ask (with consent) for written guidance.",
  "NO WEIGHT OR FOOD COMMENTS, no weighing, no calorie projects; review whole-school food and body messages.",
  "PROTECT PRIVACY while being alert: staff do not search bags or monitor toilets unless the treating team specifically advises and the young person knows.",
  "ACADEMIC ADJUSTMENTS: flexibility for appointments, reduced workload during treatment, support with concentration and exam pressure (check current SEC guidance).",
  "CONTINUUM LEVEL: School Support Plus — CAMHS or another specialist service involved.",
  "REFER: GP (urgent) → CAMHS / eating disorder service. SIGNPOST Bodywhys. DO NOT diagnose, advise on medication, or give diet plans (PSI 2.2.2).",
 ],

 "explain_parent": [
  "'I wanted to talk today because school has noticed some things that concern us, and early help matters. [Specific observations.]'",
  "'Please see your GP soon — ideally this week. Some of these behaviours can affect the body's salts and the heart, even when someone looks well.'",
  "'This isn't about willpower or bad behaviour. Cutting back on food often triggers episodes of losing control over eating, and then shame and trying to get rid of the food. It's a cycle, and it can be broken with treatment.'",
  "'The recommended treatment for young people involves the family. You're part of the solution.'",
  "SIGNPOST: GP; CAMHS; Bodywhys (helpline, support groups, family programmes — check current services at bodywhys.ie).",
 ],

 "explain_teacher": [
  "'This is a serious eating disorder that often doesn't show on the outside. She may look completely well.'",
  "'No comments on weight, food or appearance — including compliments.'",
  "'If she looks unwell, faints, or you're worried she's been vomiting, tell the parents and principal the same day.'",
  "'The treating team will advise on things like toilet access after lunch and PE. Please follow that plan, and ask if unsure.'",
  "'Shame is a big part of this. Keep things private and matter-of-fact.'",
  "'If a pupil tells you about a friend, thank them, reassure them they did the right thing, and pass it on the same day — don't ask them to keep watch.'",
 ],

 "explain_child": [
  "OLDER: 'Lots of people get stuck in a cycle — cutting back, then losing control with food, then feeling awful and trying to undo it. It's really common, it's not your fault, and it can be treated.'",
  "ASK: 'Have you felt faint, dizzy, or had your heart race?' · 'Have you ever thought about hurting yourself or not wanting to be alive?'",
  "EXPLAIN LIMITS of confidentiality before they disclose more.",
  "OFFER control where safe: 'Who would you like to be there when we talk to your parents? What should we say?'",
  "DO NOT ask for details of binges or purging, or react with shock. Stay calm and warm.",
 ],

 "analogies": [
  "THE PENDULUM: 'The harder you push the pendulum one way — strict dieting — the harder it swings back — bingeing.' Works with parents, teachers and young people (after Fairburn, 2008).",
  "THE HIDDEN LEAK: 'The damage from purging is like a leak inside a wall — you can't see it until something goes wrong. That's why a doctor needs to check.' Works with parents who say she looks fine.",
  "THE TRAP: 'It feels like a solution at first, and then it becomes a trap.' Works with older adolescents.",
 ],

 "language": [
  "Say 'a young person with bulimia' or 'experiencing an eating disorder'.",
  "Avoid 'greedy', 'disgusting', 'attention-seeking', 'she's not that thin'.",
  "Keep medical details out of school records beyond what is needed to support the plan.",
  "Follow the young person's language about their recovery.",
 ],

 "red_flags": [
  ED_MEDICAL_RISK,
  ED_SUICIDE_RISK,
  "RED FLAG — vomiting blood, severe abdominal pain, or signs of laxative overdose → emergency; 999/112.",
  CP_ROUTE,
  "BOUNDARY — you do not diagnose, weigh, set meal plans, or advise on medication (PSI 2.2.2).",
  "BOUNDARY — you cannot keep suspected bulimia confidential from parents; check with your supervisor about 16–17-year-olds and consent.",
  "WATCH — frequent trips to the toilet after eating, dental problems, swollen cheeks, scarred knuckles, food disappearing. Report concerns; do not investigate.",
 ],

 "child_voice": [
  "SOLUTION-FOCUSED CONVERSATION — good because it keeps the focus on school and hope, and avoids shame-laden detail.",
  "MFQ or RCADS SELF-REPORT completed WITH the young person — good because mood is central and the EP can follow up risk items immediately.",
  "WRITTEN CHECK-IN — good because shame makes spoken disclosure hard.",
  "YOUNG PERSON'S INPUT TO THE SCHOOL PLAN — good because it reduces secrecy and builds engagement.",
  "SCALING of how school feels (0–10) at each review — good because it tracks change without asking for symptom detail.",
 ],

 "questions": [
  "Q: 'She's not thin — is it really serious?' — A: 'Yes. Most young people with bulimia are in the normal weight range. The risk is inside — especially to the heart through changes in the body's salts. That's why a GP check is important.'",
  "Q: 'Should we check the toilets after lunch?' — A: 'Not unless the treating team advises it and she knows. Covert monitoring increases shame and secrecy.'",
  "Q: 'She told a friend and the friend told us. What do we do?' — A: 'Thank the friend, support them, and tell the parents the same day. Tell her you're doing it and why.'",
  "Q: 'Will a diet help her control it?' — A: 'No — dieting usually fuels the cycle. Treatment focuses on regular eating and breaking the cycle, led by specialists.'",
  "Q: 'Is it anorexia?' — A: 'They're related and can overlap. Specialists make that distinction; for school the response is the same — act today, GP, follow the plan.'",
  "Q: 'She's 17 — can we tell her parents?' — A: 'Where there is a risk to her health, parents need to know. The consent law for 16–17-year-olds is complicated; I'll check with my supervisor, but safety comes first.'",
 ],

 "supervision": [
  "Bring any first concern the same day.",
  "Discuss consent and confidentiality for older adolescents.",
  "Ask about local CAMHS eating disorder capacity and what happens while waiting.",
  "Reflect on how you responded to disclosure: calm, warm, clear about next steps?",
  "Consider whether school culture (sport, weight talk, exams) is contributing, and how to raise it.",
  "Plan how to support friends who raised the concern, and how much they are told.",
 ],

 "reflection": [
  "ON SPEED — same-day action or a delay?",
  "ON SHAME — did my language reduce or increase it?",
  "ON MEDICAL RISK — did I explain hidden risk clearly to parents?",
  "ON CONFIDENTIALITY — did I explain the limits before the young person disclosed more?",
  "ON ROLE — did I stay out of diet advice and treatment?",
  "ON FRIENDS — did I look after the peer who told us, without making them responsible?",
  "WHAT GOOD LOOKS LIKE: 'Concern raised with parents that day, urgent GP advised, supervisor informed; after CAMHS involvement, school plan agreed with the young person — private toilet access, no food comments, reduced homework, key adult.'",
  "WHAT POOR LOOKS LIKE: 'Staff to monitor lunch and toilets and report back.' — secret surveillance with no referral.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "Arcelus, J., Mitchell, A. J., Wales, J., & Nielsen, S. (2011). Mortality rates in patients with anorexia nervosa and other eating disorders: A meta-analysis of 36 studies. Archives of General Psychiatry, 68(7), 724–731.",
  "Fairburn, C. G. (2008). Cognitive behavior therapy and eating disorders. Guilford Press.",
  "Health Service Executive. (2018). Eating disorder services: HSE model of care for Ireland. HSE National Clinical Programme for Eating Disorders & College of Psychiatrists of Ireland. — check for updates.",
  "National Institute for Health and Care Excellence. (2017). Eating disorders: Recognition and treatment (NICE Guideline NG69). https://www.nice.org.uk/guidance/ng69 — check for updates.",
  "Royal College of Psychiatrists. (2022). Medical emergencies in eating disorders (MEED): Guidance on recognition and management (College Report CR233). — check for updates.",
  "Russell, G. (1979). Bulimia nervosa: An ominous variant of anorexia nervosa. Psychological Medicine, 9(3), 429–448.",
  "Stice, E. (2002). Risk and maintenance factors for eating pathology: A meta-analytic review. Psychological Bulletin, 128(5), 825–848.",
 ],

 "pathway": {
  "age": "Typically identified in mid-to-late adolescence or young adulthood. Often hidden for a long time; a friend, a dentist or a GP may be first to notice.",
  "who_diagnoses": "Ireland: CAMHS (including eating disorder teams where available), psychiatry, adult eating disorder services from 18. GP assesses medical risk. The EP does not diagnose.",
  "who_wrote_report": "CAMHS psychiatrist or psychologist, eating disorder team, GP letter, or private clinician.",
  "refer_to": "GP (urgent) → CAMHS / eating disorder service. Emergency services if medical emergency. Bodywhys for family support.",
  "sooner": "'Bulimia is very good at hiding — most families don't know for a long time. You're getting help now, and that's what matters.'",
 },

 "differential": [
  "ANOREXIA NERVOSA, BINGE-EATING/PURGING TYPE — similar behaviours with significantly low weight.",
  "BINGE-EATING DISORDER — binges without regular compensatory behaviour.",
  "RUMINATION DISORDER — effortless regurgitation without binge or weight concern.",
  "MEDICAL CAUSES OF VOMITING — gastrointestinal illness, pregnancy.",
  "DEPRESSION WITH APPETITE CHANGE — without the binge–compensate cycle.",
 ],

 "next": [
  "Speak with parents the same day; advise urgent GP; inform supervisor the same day.",
  "Ask directly about medical symptoms and self-harm.",
  "With consent, request written school guidance from the treating team.",
  "Agree and record the school plan; review with the young person.",
 ],

 "presentations": [
  "Binge eating and loss of control",
  "Vomiting after meals",
  "Preoccupation with weight and shape",
  "Low mood and shame",
  "Frequent toilet trips after eating",
  "Dental and physical signs noticed by others",
 ],

 "bands": {
  "Early Years": {
   "applies": "N/A — not a presentation at this age.",
   "prevalence": "Not applicable at this band.",
   "see": "Not seen. Vomiting in a young child is a medical matter; hidden eating or food hoarding is better understood in terms of hunger, anxiety, attachment or neglect.",
   "tools": [],
  },
  "School Age": {
   "applies": "RARELY — onset before adolescence is uncommon.",
   "prevalence": "Rate not stated here — check; low before adolescence.",
   "see": "Secret eating or food hoarding in primary school is more often linked to anxiety, trauma, food insecurity or loss-of-control eating than bulimia. Explore the context; purging in a young child needs same-day parent contact and GP.",
   "tools": ["SDQ", "RCADS"],
  },
  "Adolescent": {
   "applies": "YES — main onset band.",
   "prevalence": "DSM-5-TR 12-month prevalence around 1%–1.5% in young females (US) — check before quoting.",
   "see": "Often hidden: normal weight, secretive eating, disappearing to the toilet after meals, low mood, self-criticism. Friends may raise it first. Same-day parent contact and urgent GP; CAMHS; school follows the treating team's plan.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Beck Youth Inventories-2",
             "Eating Disorder Examination Questionnaire (EDE-Q; Fairburn & Beglin, 1994) — AGE adolescents and adults · MEASURES: restraint, eating, shape and weight concern; binge and purge frequency · CANNOT TELL YOU: medical risk or diagnosis; specialist-team measure, not for EP use · TIME: about 15 min"],
  },
  "Young Adult": {
   "applies": "YES — onset and continuation into college and adulthood.",
   "prevalence": "Rate not stated here — check.",
   "see": "A student managing bulimia away from home, often without help. Transition to adult services is a risk point.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "RARELY — identified less often; may be under-recognised.",
   "prevalence": "Rate not stated here — check.",
   "see": "Vomiting or binge-like eating in a young person with additional needs needs medical review first; understanding may require functional assessment and careful communication support.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3"],
  },
 },
},

# =====================================================================================
# 6. BINGE-EATING DISORDER
# =====================================================================================
{
 "name": "Binge-Eating Disorder",
 "code": "DSM-5-TR Binge-Eating Disorder · ICD-11 6B82 Binge eating disorder — verify codes before quoting",
 "neps": "3. EMOTIONAL (3.4 Mood) — and 5. OTHER (5.3 Medical condition or other diagnosis)",
 "coru": CORU,
 "psi":  PSI,
 "law":  LAW_ED,

 "what_it_is": [
  "RECURRENT EPISODES OF BINGE EATING — eating a larger amount than most people would in a similar time, WITH A SENSE OF LOSS OF CONTROL — WITHOUT the regular compensatory behaviour of bulimia (APA, 2022, DSM-5-TR). Recognised as a separate diagnosis in DSM-5 (2013).",
  "Binges are marked by several of: eating much more rapidly than normal; eating until uncomfortably full; eating large amounts when not physically hungry; eating alone because of embarrassment; feeling disgusted, depressed or very guilty afterwards. There is MARKED DISTRESS about bingeing (APA, 2022 — check full criteria).",
  "FREQUENCY: on average at least once a week for three months (APA, 2022 — check).",
  "It is described as the most common eating disorder in adult population studies (Hudson, Hiripi, Pope & Kessler, 2007 — US data). In children and younger adolescents, researchers use the term LOSS-OF-CONTROL EATING because the amount eaten is harder to judge (Tanofsky-Kraff, Marcus, Yanovski & Yanovski, 2008).",
  "IT IS NOT DEFINED BY BODY SIZE. It occurs at any weight, though it is associated with higher weight. People with BED face heavy WEIGHT STIGMA, which itself worsens eating and mental health (Puhl & Latner, 2007).",
  "MAINTAINED BY dieting and restriction, emotional regulation (eating to cope with distress), shame and secrecy (Fairburn, 2008; Stice, 2002).",
  "TREATMENT: NICE NG69 (2017; check for updates) recommends psychological treatment focused on binge eating (for example CBT-ED); it notes weight-loss programmes alone are not a treatment for BED — check the current wording. In Ireland, via CAMHS or eating disorder services; availability varies.",
 ],

 "what_it_is_not": [
  "NOT greed or 'overeating'. The defining feature is loss of control and distress, not quantity alone.",
  "NOT the same as being in a higher weight body. Many people in higher-weight bodies do not have BED; people of any weight can have it.",
  "NOT fixed by dieting. Dieting often increases bingeing (Neumark-Sztainer et al., 2006; Stice, 2002).",
  "NOT a less serious eating disorder. It is associated with depression, anxiety, suicidality and physical health problems — check rates before quoting.",
  "NOT a school's job to address through weight loss, food monitoring or 'healthy eating' interventions targeting the pupil.",
  "NOT confined to girls; the sex ratio is more even than for anorexia and bulimia (APA, 2022).",
 ],

 "prevalence": [
  "OVERALL: DSM-5-TR reports 12-month prevalence among US adults of about 1.6% in females and 0.8% in males (APA, 2022 — check before quoting).",
  "ADOLESCENTS: loss-of-control eating is reported in a notable proportion of young people — rate not stated here, check.",
  "IRELAND: check the HSE Model of Care (HSE, 2018) and Bodywhys for estimates.",
  "SEX RATIO: less skewed than anorexia or bulimia (APA, 2022).",
  "AGE: onset typically adolescence or young adulthood (APA, 2022).",
 ],

 "cooccurring": [
  {"name": "DEPRESSION", "rate": "commonly co-occurs — rate not stated here, check",
   "presents": "low mood, shame and self-criticism after binges; withdrawal and low self-worth, often worsened by weight-related teasing."},
  {"name": "ANXIETY", "rate": "commonly co-occurs — rate not stated here, check",
   "presents": "eating to manage anxiety or stress; avoidance of eating in front of others."},
  {"name": "ADHD", "rate": "associated — rate not stated here, check",
   "presents": "impulsivity and emotional dysregulation contributing to binges; eating when bored or understimulated."},
  {"name": "WEIGHT-RELATED BULLYING", "rate": "common for young people in higher-weight bodies (Puhl & Latner, 2007) — check",
   "presents": "teasing, exclusion, avoidance of PE and changing rooms, school avoidance. Bullying is a trigger and maintaining factor; address under the anti-bullying procedures."},
  {"name": "TRAUMA AND ADVERSITY", "rate": "associated — rate not stated here, check",
   "presents": "eating to soothe distress; history of adversity. Trauma-informed approach; safeguarding where relevant."},
 ],

 "recommendations": [
  "RAISE CONCERN WITH PARENTS and advise a GP appointment. Tell your supervisor. Ask directly about mood and self-harm.",
  "ZERO TOLERANCE FOR WEIGHT-RELATED BULLYING: act under the school's anti-bullying procedures; staff model respectful language.",
  "NO WEIGHT OR FOOD MONITORING and no singling out in healthy-eating activities; no weighing; no BMI work in class.",
  "PE AND CHANGING: private changing option, choice of kit, focus on enjoyment and skill rather than weight or fitness targets.",
  "EMOTIONAL SUPPORT: a key adult; teach and practise emotion-regulation strategies that do not involve food, aligned with any treatment plan.",
  "CONTINUUM LEVEL: School Support where distress and bullying affect school life; School Support Plus when a specialist service is involved.",
  "REFER: GP → CAMHS or Primary Care Psychology / eating disorder service. SIGNPOST Bodywhys. DO NOT recommend diets, weight loss, or medication (PSI 2.2.2).",
 ],

 "explain_parent": [
  "'What she's describing — feeling out of control with food and then very upset — is a recognised eating disorder. It isn't greed or lack of willpower.'",
  "'Diets usually make it worse. The treatment focuses on regular eating and managing feelings, not on weight loss.'",
  "'I'd recommend a GP appointment to talk about it and look at the right service.'",
  "'At school we'll focus on stopping any teasing and making PE and lunch comfortable. We won't comment on her weight.'",
  "SIGNPOST: GP; Bodywhys (helpline and support — check current services); CAMHS or Primary Care Psychology via GP.",
 ],

 "explain_teacher": [
  "'This is an eating disorder, not a lack of self-control. Shame is a big part of it.'",
  "'Please don't comment on his weight or lunch, and don't single him out in healthy-eating lessons.'",
  "'Any weight-related teasing needs to be dealt with firmly, every time.'",
  "'In PE, a private changing option and a focus on taking part, not on weight, make a real difference.'",
  "'If he seems very low or talks about hurting himself, tell the DLP and me the same day.'",
  "'Check lessons for weight-focused content — calorie counting, BMI calculations, \'good and bad foods\'. They land hardest on pupils like him.'",
 ],

 "explain_child": [
  "OLDER: 'Lots of people find that when things are hard, food becomes a way of coping — and then it feels out of control. That's really common, it's not your fault, and there's help that works.'",
  "ASK: 'How are you feeling in yourself lately?' · 'Has anyone been unkind about your body?' · 'Have you ever thought about hurting yourself?'",
  "YOUNGER: 'Sometimes when we feel big feelings, we eat to feel better. Let's find other things that help too.'",
  "OFFER control over who is told and what the school plan includes.",
  "DO NOT discuss weight, suggest diets or praise weight loss.",
 ],

 "analogies": [
  "THE PRESSURE COOKER: 'Stress builds up with nowhere to go, and food becomes the release valve. Treatment helps find other valves.' Works with parents and older pupils.",
  "THE PENDULUM: 'The stricter the diet, the harder the swing back.' Works with parents tempted to restrict (after Fairburn, 2008).",
  "THE SMOKE AND THE FIRE: 'Bingeing is the smoke; the fire is often stress, low mood or hurt. We need to look at the fire.' Works with teachers.",
 ],

 "language": [
  "Say 'binge eating' or 'loss-of-control eating'; avoid 'overeating', 'greedy', 'lazy'.",
  "Avoid weight-stigmatising terms; many people prefer 'higher weight' to 'obese' or 'overweight' in everyday language (Puhl & Latner, 2007) — follow the young person's lead.",
  "Keep weight out of school reports unless a specialist has asked for school input on it.",
 ],

 "red_flags": [
  ED_SUICIDE_RISK,
  "RED FLAG — weight-related bullying that is severe, persistent or online → anti-bullying procedures and parent contact; consider safeguarding if exploitation or threats.",
  "RED FLAG — purging, fasting or rapid weight loss → the picture may be bulimia or anorexia; same-day parent contact and urgent GP.",
  CP_ROUTE,
  "BOUNDARY — you do not diagnose, recommend weight loss, diets or medication (PSI 2.2.2).",
  "WATCH — school 'healthy weight' initiatives that single out higher-weight pupils; they can worsen binge eating and shame.",
 ],

 "child_voice": [
  "SOLUTION-FOCUSED CONVERSATION — good because it focuses on strengths and preferred futures, not weight.",
  "MFQ or RCADS SELF-REPORT completed together — good because low mood and anxiety are frequent and the EP can follow up risk items immediately.",
  "BULLYING MAP (where and when teasing happens) — good because it gives practical, school-controlled targets for change.",
  "YOUNG PERSON'S INPUT TO PE AND LUNCH ARRANGEMENTS — good because it builds agency and reduces avoidance.",
 ],

 "questions": [
  "Q: 'Shouldn't he just go on a diet?' — A: 'Diets usually make binge eating worse. The recommended treatment works on regular eating, feelings and the binge cycle — not weight loss.'",
  "Q: 'Is this really an eating disorder? He just eats too much.' — A: 'The key is loss of control and distress. It's a recognised condition, and it's treatable.'",
  "Q: 'He's being teased about his weight. Is that part of this?' — A: 'Weight teasing makes binge eating and low mood worse. Stopping it is one of the most useful things school can do.'",
  "Q: 'Can he be excused from PE?' — A: 'Ideally he stays in PE with adjustments — private changing, choice of kit, a focus on taking part. Excusing him can increase isolation.'",
  "Q: 'Who treats it?' — A: 'The GP is the start. Depending on your area, it may be CAMHS, Primary Care Psychology or an eating disorder service. Bodywhys can help while you wait.'",
  "Q: 'Should we tell him to stop eating so much at lunch?' — A: 'No. Comments about food add shame, and shame fuels bingeing. Leave lunch to the family and treating team.'",
 ],

 "supervision": [
  "Reflect on your own attitudes to weight — weight bias is common among professionals and affects practice (Puhl & Latner, 2007).",
  "Discuss how to raise binge eating sensitively with a young person and family.",
  "Ask about local services that accept BED referrals for adolescents.",
  "Bring any case where weight-related bullying is central and how to challenge school culture.",
  "Discuss how to write about weight neutrally in reports, or leave it out.",
 ],

 "reflection": [
  "ON WEIGHT BIAS — did my language or recommendations focus on weight rather than wellbeing?",
  "ON BULLYING — did I address teasing as a primary target?",
  "ON MOOD — did I ask directly about low mood and self-harm?",
  "ON ROLE — did I avoid diet advice?",
  "ON THE YOUNG PERSON'S VOICE — did they shape the plan?",
  "ON SCHOOL CULTURE — did I name any whole-school practice (weigh-ins, fitness league tables) that needs to change?",
  "WHAT GOOD LOOKS LIKE: 'GP recommended, supervisor informed, mood and risk asked about, anti-bullying plan in place, PE adjustments agreed with the young person, no weight comments; referral via GP to psychology.'",
  "WHAT POOR LOOKS LIKE: 'Recommend a healthy-eating programme and weekly weigh-ins with the school nurse.' — stigmatising, harmful and outside role.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "Fairburn, C. G. (2008). Cognitive behavior therapy and eating disorders. Guilford Press.",
  "Hudson, J. I., Hiripi, E., Pope, H. G., Jr., & Kessler, R. C. (2007). The prevalence and correlates of eating disorders in the National Comorbidity Survey Replication. Biological Psychiatry, 61(3), 348–358.",
  "National Institute for Health and Care Excellence. (2017). Eating disorders: Recognition and treatment (NICE Guideline NG69). https://www.nice.org.uk/guidance/ng69 — check for updates.",
  "Neumark-Sztainer, D., Wall, M., Guo, J., Story, M., Haines, J., & Eisenberg, M. (2006). Obesity, disordered eating, and eating disorders in a longitudinal study of adolescents: How do dieters fare 5 years later? Journal of the American Dietetic Association, 106(4), 559–568.",
  "Puhl, R. M., & Latner, J. D. (2007). Stigma, obesity, and the health of the nation's children. Psychological Bulletin, 133(4), 557–580.",
  "Stice, E. (2002). Risk and maintenance factors for eating pathology: A meta-analytic review. Psychological Bulletin, 128(5), 825–848.",
  "Tanofsky-Kraff, M., Marcus, M. D., Yanovski, S. Z., & Yanovski, J. A. (2008). Loss of control eating disorder in children age 12 years and younger: Proposed research criteria. Eating Behaviors, 9(3), 360–365.",
 ],

 "pathway": {
  "age": "Onset typically adolescence or young adulthood. In children, loss-of-control eating may be noticed first; it often goes unrecognised because the focus falls on weight.",
  "who_diagnoses": "Ireland: CAMHS, psychiatry, eating disorder services, adult services from 18. The GP is the usual first contact. The EP does not diagnose.",
  "who_wrote_report": "CAMHS clinician, eating disorder team, Primary Care Psychology, GP letter, or private clinician.",
  "refer_to": "GP → CAMHS / Primary Care Psychology / eating disorder service (varies by area — check locally). Bodywhys for support.",
  "sooner": "'Binge eating is often hidden and often misunderstood as just eating too much. The fact that you're asking now means he can get the right kind of help.'",
 },

 "differential": [
  "BULIMIA NERVOSA — binges plus regular compensatory behaviour.",
  "ANOREXIA NERVOSA, BINGE-PURGE TYPE — with significantly low weight.",
  "EMOTIONAL EATING WITHOUT LOSS OF CONTROL — common and not a disorder.",
  "MEDICAL OR MEDICATION EFFECTS ON APPETITE — some medications and conditions increase appetite; GP question.",
  "PRADER-WILLI SYNDROME — genetic syndrome with hyperphagia; medical diagnosis.",
  "FOOD INSECURITY — eating large amounts when food is available after scarcity; consider welfare.",
 ],

 "next": [
  "Raise the concern with parents and recommend a GP appointment; inform supervisor.",
  "Ask about mood and self-harm; follow the same-day route if needed.",
  "Put anti-bullying and PE adjustments in place; record in the Student Support File.",
  "Review with the young person in four to six weeks.",
 ],

 "presentations": [
  "Loss-of-control eating",
  "Secretive eating",
  "Weight-related bullying",
  "Low mood and shame about eating",
  "Avoidance of PE and changing rooms",
 ],

 "bands": {
  "Early Years": {
   "applies": "N/A — not diagnosed at this age.",
   "prevalence": "Not applicable at this band.",
   "see": "Not seen as BED. A young child who eats large amounts or seeks food constantly needs medical review (including genetic causes) and a look at hunger, routine and wellbeing at home.",
   "tools": [],
  },
  "School Age": {
   "applies": "RARELY — as BED; loss-of-control eating may be seen.",
   "prevalence": "Rate not stated here — check.",
   "see": "Secret eating, food hoarding, eating when upset. Explore context (stress, bullying, adversity, food insecurity) before assuming an eating disorder. Address bullying and emotional needs; GP if concern persists.",
   "tools": ["SDQ", "RCADS"],
  },
  "Adolescent": {
   "applies": "YES — onset commonly here.",
   "prevalence": "Rate not stated here — check.",
   "see": "A young person who describes losing control with food, eats in secret, feels ashamed and low, and may be teased about weight. GP; psychology; anti-bullying; PE adjustments; no weight focus.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Beck Youth Inventories-2",
             "Eating Disorder Examination Questionnaire (EDE-Q; Fairburn & Beglin, 1994) — AGE adolescents and adults · MEASURES: eating, shape and weight concern, binge frequency · CANNOT TELL YOU: diagnosis; specialist-team measure, not for EP use · TIME: about 15 min"],
  },
  "Young Adult": {
   "applies": "YES — onset and continuation.",
   "prevalence": "Rate not stated here — check.",
   "see": "A student using food to cope with stress, often with shame and weight stigma. Adult services and college counselling.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "RARELY — as BED; food seeking in special settings has other explanations to check first.",
   "prevalence": "Rate not stated here — check.",
   "see": "Food seeking in a young person with intellectual disability or a genetic syndrome (e.g., Prader-Willi) is a medical and behavioural question, not BED. Functional assessment and medical review.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3"],
  },
 },
},

# =====================================================================================
# 7. ENURESIS
# =====================================================================================
{
 "name": "Enuresis (bedwetting and daytime wetting)",
 "code": "DSM-5-TR Enuresis (elimination disorders chapter; nocturnal only / diurnal only / nocturnal and diurnal) · ICD-11 6C00 Enuresis — verify codes and subcodes before quoting",
 "neps": "5. OTHER (5.3 Medical condition or other diagnosis) — and 3. EMOTIONAL (3.1 Confidence and self-esteem) where shame or bullying is prominent",
 "coru": CORU,
 "psi":  PSI,
 "law":  LAW_MED,

 "what_it_is": [
  "REPEATED VOIDING OF URINE into bed or clothes, at a frequency of at least twice a week for three consecutive months OR with clinically significant distress or impairment, in a child of at least 5 years of age (or equivalent developmental level), not due to a substance or another medical condition (APA, 2022, DSM-5-TR). Check the full criteria before quoting.",
  "SUBTYPES (DSM-5-TR): NOCTURNAL ONLY (bedwetting — by far the most common), DIURNAL ONLY (daytime wetting), and NOCTURNAL AND DIURNAL. The International Children's Continence Society (ICCS) uses slightly different terms: 'enuresis' for night-time wetting only, 'daytime incontinence' for daytime; and MONOSYMPTOMATIC (night only, no daytime bladder symptoms) versus NON-MONOSYMPTOMATIC (Austin et al., 2016).",
  "PRIMARY vs SECONDARY: PRIMARY — the child has never been reliably dry. SECONDARY — wetting returns after a dry period (ICCS uses at least six months). Secondary onset is more often linked to a stressor, a medical cause (e.g., urinary tract infection, diabetes, constipation) or life events (Austin et al., 2016).",
  "NIGHT-TIME WETTING is mainly BIOLOGICAL: some combination of producing a large volume of urine at night (nocturnal polyuria), a bladder that holds less or is overactive at night, and difficulty waking to bladder signals. It runs strongly in families (Nevéus et al., 2020). It is not laziness and not usually psychological in origin.",
  "DAYTIME WETTING often involves bladder overactivity, holding on too long (voiding postponement), CONSTIPATION, or urinary tract infection — and in school, AVOIDING THE TOILETS (dirty, no locks, no privacy, not allowed to go).",
  "TREATMENT is medical and behavioural, led by the GP, paediatrics or a continence service: advice on drinks and regular toileting, enuresis ALARMS, and medication where the doctor decides (NICE, 2010, CG111 — check for updates). The EP does not advise on medication.",
  "WHY THE EP SEES IT: shame, bullying, school trips and sleepovers avoided, low self-esteem, and sometimes behaviour or attendance problems that turn out to be about toilets. The EP's job is dignity, a practical school plan, and making sure the medical route is in place.",
 ],

 "what_it_is_not": [
  "NOT laziness, naughtiness or 'doing it on purpose'. Punishment, shaming or withdrawing privileges for wet nights is ineffective and harmful; NICE CG111 advises rewards, if used, for agreed behaviours (e.g., using the toilet before bed) rather than for dry nights, which the child cannot control (NICE, 2010 — check wording).",
  "NOT usually caused by emotional problems. Emotional difficulties are more often a CONSEQUENCE of wetting — though secondary onset can follow stress, and the two interact (von Gontard et al., 2011).",
  "NOT something to 'wait out' if the child is distressed. NICE CG111 advises that younger children should not be excluded from management simply because of age — check the current wording.",
  "NOT a school discipline matter. Restricting toilet access during class, or requiring a child to ask publicly, can cause daytime wetting and constipation.",
  "NOT, on its own, evidence of abuse. Most wetting has no such cause. But a NEW onset with other concerns deserves thought — see red flags.",
  "NOT a diagnosis for the EP to make. Medical causes (UTI, diabetes, constipation, neurological or structural problems) are ruled out by the GP or paediatrics first.",
 ],

 "prevalence": [
  "OVERALL: DSM-5-TR gives prevalence of enuresis of around 5%–10% among 5-year-olds, 3%–5% among 10-year-olds and around 1% among those aged 15 or older (APA, 2022 — check before quoting).",
  "COURSE: most children become dry over time, with a spontaneous resolution each year, but a small proportion continue into adolescence (Nevéus et al., 2020 — check figures before quoting).",
  "SEX RATIO: nocturnal enuresis more common in boys; diurnal wetting more common in girls (APA, 2022 — check).",
  "IRELAND: no Irish prevalence figure stated here — check before quoting.",
  "ADHD: enuresis is more common in children with ADHD than in peers (von Gontard et al., 2011) — rate not stated here, check.",
 ],

 "cooccurring": [
  {"name": "CONSTIPATION", "rate": "commonly associated — rate not stated here, check",
   "presents": "wetting (especially daytime) alongside infrequent, hard or painful stools, tummy pain or soiling. Treating constipation often improves wetting; GP leads (NICE, 2010, CG99)."},
  {"name": "ADHD", "rate": "elevated (von Gontard et al., 2011) — rate not stated here, check",
   "presents": "a child who does not notice or postpones bladder signals because absorbed in activity; forgetful about toilet routines. Scheduled prompts help."},
  {"name": "AUTISM AND INTELLECTUAL DISABILITY", "rate": "delayed continence more common — rate not stated here, check",
   "presents": "delayed toilet training, sensory aversion to school toilets (hand dryers, smells, flushing), rigid toileting routines. Toilet training programmes adapted to the child."},
  {"name": "EMOTIONAL AND BEHAVIOURAL DIFFICULTIES", "rate": "elevated, especially with daytime wetting (von Gontard et al., 2011) — check",
   "presents": "low self-esteem, anxiety, withdrawal from social events, or behaviour that masks embarrassment. Often a consequence as much as a cause."},
  {"name": "SLEEP-DISORDERED BREATHING", "rate": "associated — rate not stated here, check",
   "presents": "snoring, pauses in breathing, tiredness in class alongside bedwetting. Medical referral via GP."},
  {"name": "TYPE 1 DIABETES OR URINARY TRACT INFECTION", "rate": "medical causes to exclude",
   "presents": "new wetting with thirst, weight loss or tiredness (diabetes), or pain and frequency (UTI). Same-day GP if thirst and weight loss."},
 ],

 "recommendations": [
  "MEDICAL REVIEW FIRST: 'It is recommended that parents discuss the wetting with their GP if not already done, to rule out medical causes and consider treatment options.' New-onset wetting with thirst, weight loss or tiredness → GP the same day.",
  "FREE AND PRIVATE TOILET ACCESS: a discreet toilet pass or signal; never refuse or delay toilet access; access to a clean, private toilet (e.g., accessible staff toilet) where needed.",
  "SCHEDULED TOILET BREAKS for daytime wetting, discreetly prompted (e.g., a vibrating watch or quiet cue), if the treating clinician recommends them.",
  "DRINKS: allow water bottles throughout the day — restricting fluids at school is not recommended and can worsen bladder control (NICE, 2010, CG111 — check the guidance on fluids).",
  "DIGNIFIED CHANGE PLAN: spare clothes kept in school, a private place to change, a named adult, and an agreed script — written into an intimate care plan consistent with the school's policy and Children First guidance.",
  "TRIPS AND SLEEPOVERS: plan discreetly with parents (e.g., the child's own sleeping bag with a liner, discreet adult support, medication timing if prescribed). Wetting should not exclude a child from residential trips.",
  "CONTINUUM LEVEL: Classroom Support for most — toilet access and discretion; School Support if self-esteem, bullying or attendance is affected; School Support Plus where continence services or CDNT are involved.",
  "REFER: GP → paediatrics / continence service (HSE provision varies by area — check). CDNT for children with disabilities. DO NOT diagnose, advise on medication or alarms, or set fluid targets (PSI 2.2.2).",
 ],

 "explain_parent": [
  "'Wetting is really common and it's not his fault or yours. At night it's mostly about how the body makes urine and how deeply he sleeps — it often runs in families.'",
  "'The GP is the right first step — to check for anything medical and talk about treatments. There are effective ones, like alarms, and the GP can advise on others.'",
  "'At school, we'll make sure he can go to the toilet whenever he needs, has spare clothes, and can change privately. No one will make a fuss.'",
  "'Please don't punish wet nights. He can't control them. If you use rewards, reward things he can control — like going to the toilet before bed.'",
  "'Has anything changed recently — at home, at school, with his health? Wetting coming back after being dry can sometimes follow stress or illness.'",
  "SIGNPOST: GP; Public Health Nurse; HSE continence services where available (check locally); ERIC, The Children's Bowel & Bladder Charity (UK) has practical family and school information — check its current resources and note it is UK-based.",
 ],

 "explain_teacher": [
  "'This is medical, not behavioural. He isn't choosing to wet.'",
  "'He must be allowed to go to the toilet whenever he needs — no waiting, no asking in front of the class. A discreet signal or pass works well.'",
  "'Please let him keep a water bottle. Cutting back on drinks makes bladders worse, not better.'",
  "'If there's an accident, deal with it quietly: a private word, spare clothes, a private place to change. No comments in front of others.'",
  "'Watch for teasing and act on it straight away under the anti-bullying policy.'",
  "'If the school toilets are dirty, lack locks or feel unsafe, children avoid them — that's worth raising with the principal for everyone.'",
 ],

 "explain_child": [
  "YOUNGER: 'Lots of children have wet beds or accidents — more than you'd think, even in your class. Your body is still learning. It's not your fault and no one will be cross.'",
  "OLDER: 'Your bladder and your brain are still learning to talk to each other at night. It's really common, it runs in families, and there are things that help.'",
  "ASK: 'Is it easy to get to the toilet when you need to in school?' · 'Are the toilets OK — clean, private?' · 'Has anyone said anything unkind?'",
  "ASK: 'What would make it easier if you had an accident at school?' — let the child choose the signal, the adult and the plan.",
  "AGREE what classmates are told — usually nothing — and who on staff needs to know.",
 ],

 "analogies": [
  "THE ALARM CLOCK: 'Some children sleep so deeply that the bladder's alarm doesn't wake them. It's not that they don't care — the signal isn't getting through yet.' Works with parents and children.",
  "THE SMALL BUCKET: 'Some bladders hold less at night, or the body makes more urine overnight. The bucket overflows before morning.' Works with children and parents.",
  "LEARNING TO RIDE A BIKE: 'Every child learns at a different speed — some take longer, and you don't punish them for wobbling.' Works with parents feeling frustrated.",
 ],

 "language": [
  "Say 'wetting', 'bedwetting', 'accidents' or the family's own words — use what the child is comfortable with.",
  "Avoid 'dirty', 'baby', 'lazy', 'disgusting', and any language implying the child chooses it.",
  "In reports, write factually and minimally: 'daytime wetting under GP review; school support plan in place' — the report may be read by the child later.",
  "'Intimate care plan' is the usual school term for the written arrangement — check the school's policy wording.",
 ],

 "red_flags": [
  "RED FLAG — new wetting with excessive thirst, frequent urination, weight loss or tiredness → possible diabetes; parent the same day and GP the same day.",
  "RED FLAG — pain on passing urine, fever, blood in urine → possible infection; GP promptly.",
  "RED FLAG — wetting with new weakness, numbness, back pain or problems walking → neurological cause possible; urgent medical review.",
  "RED FLAG — sudden secondary wetting together with other indicators of harm (fear of a particular person or place, sexualised behaviour, injuries, disclosure) → child protection route: report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty. Wetting ALONE is not evidence of abuse; do not assume, and do not ignore a pattern.",
  "BOUNDARY — you do not diagnose, recommend medication or alarms, or set fluid limits (PSI 2.2.2).",
  "WATCH — a child who is avoiding drinking or eating at school to avoid needing the toilet, or who is being refused toilet access in class.",
 ],

 "child_voice": [
  "PRIVATE, SHORT CONVERSATION with a trusted adult — good because the child's embarrassment is the main barrier; a private setting makes an honest account possible.",
  "SCHOOL TOILET AUDIT FROM THE CHILD'S VIEW (drawing or photos of where they feel OK and not OK) — good because it shows the environmental barriers staff cannot see.",
  "PIERS-HARRIS 3 or a self-esteem scale — good because it gives a way to hear how the child sees themselves, and wetting often dents self-concept.",
  "CHILD CHOOSES THE PLAN (signal, adult, change location) — good because control over dignity restores confidence.",
 ],

 "questions": [
  "Q: 'He's 7 — shouldn't he be dry by now?' — A: 'Many children aren't dry at night at 7. It's common and treatable. It's worth seeing the GP, especially if it bothers him.'",
  "Q: 'Should we stop him drinking so he doesn't have accidents?' — A: 'No. Holding back drinks makes bladders more irritable. Regular drinks and regular toilet trips work better.'",
  "Q: 'Is something wrong at home?' — A: 'Usually not. Wetting is mostly physical. If it's started again after being dry, it's worth asking gently about stress or health — and of course we act on any other worry.'",
  "Q: 'Can she go on the school tour?' — A: 'Yes, with a discreet plan. Wetting shouldn't stop a child going. We'll plan it privately with her parents.'",
  "Q: 'Should we give a reward for dry days?' — A: 'Only reward what she can control — like using the toilet at break. Rewarding dry days can backfire when it's not in her control.'",
  "Q: 'Can the SNA help with changing?' — A: 'That depends on the school's intimate care policy and the SNA allocation for care needs. Check the policy and current SNA guidance.'",
 ],

 "supervision": [
  "Discuss how to raise wetting with parents without implying blame.",
  "Bring any case where secondary wetting coincides with other safeguarding indicators and check your thinking on threshold.",
  "Ask about local continence services and how children get referred.",
  "Discuss intimate care policies and how to recommend dignified plans that fit them.",
  "Reflect on how you would respond if a teacher describes the child as 'doing it for attention' — and how to reframe without alienating the teacher.",
 ],

 "reflection": [
  "ON DIGNITY — did my plan protect the child's privacy in every step?",
  "ON THE MEDICAL ROUTE — did I confirm a GP review before recommending anything else?",
  "ON TOILETS — did I ask about the school toilets themselves, not only the child?",
  "ON SAFEGUARDING — did I hold the possibility without assuming it?",
  "ON THE CHILD'S VOICE — did the child choose any part of the plan?",
  "WHAT GOOD LOOKS LIKE: 'GP review confirmed; discreet toilet pass; water bottle allowed; spare clothes and private change area; named adult; plan agreed with child and parents; teasing addressed; review in six weeks.'",
  "WHAT POOR LOOKS LIKE: 'He should be reminded to go at break and lose golden time for accidents.' — punitive, ineffective and shaming.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "Austin, P. F., Bauer, S. B., Bower, W., Chase, J., Franco, I., Hoebeke, P., Rittig, S., Vande Walle, J., von Gontard, A., Wright, A., Yang, S. S., & Nevéus, T. (2016). The standardization of terminology of lower urinary tract function in children and adolescents: Update report from the standardization committee of the International Children's Continence Society. Neurourology and Urodynamics, 35(4), 471–481.",
  "National Institute for Health and Care Excellence. (2010). Bedwetting in under 19s (Clinical Guideline CG111). https://www.nice.org.uk/guidance/cg111 — check for updates.",
  "National Institute for Health and Care Excellence. (2010). Constipation in children and young people: Diagnosis and management (Clinical Guideline CG99). https://www.nice.org.uk/guidance/cg99 — check for updates.",
  "Nevéus, T., Fonseca, E., Franco, I., Kawauchi, A., Kovacevic, L., Nieuwhof-Leppink, A., Raes, A., Tekgül, S., Yang, S. S., Rittig, S., & Austin, P. F. (2020). Management and treatment of nocturnal enuresis — an updated standardization document from the International Children's Continence Society. Journal of Pediatric Urology, 16(1), 10–19.",
  "von Gontard, A., Baeyens, D., Van Hoecke, E., Warzak, W. J., & Bachmann, C. (2011). Psychological and psychiatric issues in urinary and fecal incontinence. The Journal of Urology, 185(4), 1432–1437.",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government of Ireland.",
  "Azrin, N. H., & Foxx, R. M. (1971). A rapid method of toilet training the institutionalized retarded. Journal of Applied Behavior Analysis, 4(2), 89–99.",
 ],

 "pathway": {
  "age": "Nocturnal enuresis is usually raised from about age 5–7, when most peers are dry and sleepovers and school tours begin. Daytime wetting is noticed in school from the infant classes. Secondary wetting can appear at any age.",
  "who_diagnoses": "Ireland: GP, paediatrics, or a paediatric continence or urology service (availability varies — check locally). CDNT for children with disabilities. The EP does not diagnose.",
  "who_wrote_report": "GP letter, paediatrician, continence nurse, urologist, or CDNT clinician. Check whether medical causes have been excluded and what treatment is in place.",
  "refer_to": "GP first → paediatrics / continence service. Public Health Nurse for family support. CDNT where there is a disability. Tusla if child protection concerns.",
  "sooner": "'Lots of families wait because they're told children grow out of it — and many do. What matters is that she's upset now, and help is available, so it's a good time.'",
 },

 "differential": [
  "MEDICAL CAUSES — UTI, diabetes, constipation, structural or neurological problems; GP excludes.",
  "TOILET AVOIDANCE AT SCHOOL — environmental (dirty, no locks, bullying in toilets) or anxiety-based; ask the child.",
  "DEVELOPMENTAL DELAY IN CONTINENCE — in children with intellectual disability or autism, judged against developmental level.",
  "EMOTIONAL REGRESSION AFTER STRESS — new sibling, bereavement, family change; secondary onset.",
  "MALTREATMENT — rare explanation; consider only with other indicators and follow the child protection route.",
 ],

 "next": [
  "Confirm whether a GP review has happened; recommend one.",
  "Agree a discreet school plan: toilet access, drinks, spare clothes, change location, named adult.",
  "Address teasing and any toilet-environment problems.",
  "Review in six weeks with the child and parents; escalate if distress or attendance is affected.",
 ],

 "presentations": [
  "Daytime wetting accidents",
  "Bedwetting affecting trips and sleepovers",
  "Toilet avoidance at school",
  "Shame and low self-esteem",
  "Teasing and bullying about accidents",
  "Delayed toilet training",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — diagnosis requires age 5 or equivalent developmental level; toilet training variation is normal before then.",
   "prevalence": "Not diagnosed under 5 — toilet training timing varies widely.",
   "see": "A preschooler who is not yet toilet trained is usually within the normal range. Concern arises where there is also developmental delay, pain, constipation or distress. Advice to preschool on relaxed, consistent routines; GP for pain or constipation.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "Vineland-3"],
  },
  "School Age": {
   "applies": "YES — the main band for referral.",
   "prevalence": "DSM-5-TR: around 5%–10% of 5-year-olds and 3%–5% of 10-year-olds (check before quoting).",
   "see": "Daytime accidents in class or yard, avoidance of toilets, reluctance to go on trips or sleepovers, teasing. Medical review first; dignified school plan; attention to self-esteem and bullying.",
   "tools": ["SDQ", "Piers-Harris 3", "Vineland-3"],
  },
  "Adolescent": {
   "applies": "YES — less common, but the emotional impact is greater.",
   "prevalence": "DSM-5-TR: around 1% at 15 or older (check before quoting).",
   "see": "A teenager hiding bedwetting, avoiding residential trips, sleepovers and relationships, with shame and low mood. Medical review; discreet planning for trips; check mood.",
   "tools": ["RCADS self-report", "Piers-Harris 3"],
  },
  "Young Adult": {
   "applies": "RARELY — for the school EP.",
   "prevalence": "Rate not stated here — check.",
   "see": "Persisting enuresis into adulthood is uncommon and managed by adult urology or continence services; may affect college accommodation choices.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — continence is often delayed in children with intellectual disability and autism.",
   "prevalence": "Delayed continence more common — rate not stated here, check.",
   "see": "A child still in pads or with frequent accidents, often with sensory barriers to toilet use. Adapted toilet training programmes (e.g., based on Azrin & Foxx, 1971), visual schedules, sensory-friendly toilets, and an intimate care plan with CDNT and SNA support.",
   "tools": ["Vineland-3 / ABAS-3", "Functional behaviour assessment (ABC)", "Communication Matrix / AAC review"],
  },
 },
},

# =====================================================================================
# 8. ENCOPRESIS
# =====================================================================================
{
 "name": "Encopresis (soiling)",
 "code": "DSM-5-TR Encopresis (elimination disorders chapter; with constipation and overflow incontinence / without) · ICD-11 6C01 Encopresis — verify codes and subcodes before quoting",
 "neps": "5. OTHER (5.3 Medical condition or other diagnosis) — and 3. EMOTIONAL (3.1 Confidence and self-esteem) · 3.7 Risk and safeguarding where there are other indicators",
 "coru": CORU,
 "psi":  PSI,
 "law":  LAW_MED,

 "what_it_is": [
  "REPEATED PASSAGE OF FAECES INTO INAPPROPRIATE PLACES (clothes, floor), whether involuntary or intentional, at least once a month for at least three months, in a child of at least 4 years of age (or equivalent developmental level), not attributable to a substance or a medical condition except through a mechanism involving constipation (APA, 2022, DSM-5-TR). Check the full criteria before quoting.",
  "TWO SUBTYPES: WITH CONSTIPATION AND OVERFLOW INCONTINENCE — by far the more common — and WITHOUT constipation (APA, 2022). Gastroenterology uses the Rome IV terms 'functional constipation' and 'functional non-retentive faecal incontinence' (Hyams et al., 2016).",
  "THE CONSTIPATION CYCLE: a painful or frightening bowel movement → the child holds on (stool withholding) → stool builds and hardens → the bowel stretches and loses sensation → liquid stool leaks around the blockage (overflow), without the child feeling it or being able to stop it. The child often genuinely does not know it has happened (NICE, 2010, CG99).",
  "THIS IS WHY PUNISHMENT FAILS. The child cannot feel or control the leakage. Treatment is MEDICAL first — clearing the blockage and keeping stools soft (the GP or paediatrician decides how) — plus regular toilet sitting routines and behavioural support over months (NICE, 2010, CG99; Tabbers et al., 2014).",
  "RETENTIVE vs NON-RETENTIVE: soiling WITHOUT constipation is less common and more often linked to emotional, behavioural or developmental factors, or to toileting in the wrong place for a reason the child can explain (Hyams et al., 2016). It still needs medical review first.",
  "IMPACT: shame, smell, bullying, social exclusion, school avoidance and family conflict are common, and are often more disabling than the soiling itself (Joinson et al., 2006).",
  "For the EP: MEDICAL CAUSE RULED OUT FIRST (GP/paediatrics); a DIGNIFIED school toileting plan; attention to bullying and self-esteem; and SAFEGUARDING KEPT IN MIND — soiling can occasionally be one indicator of abuse or neglect, but it is NEVER assumed from soiling alone.",
 ],

 "what_it_is_not": [
  "NOT laziness, defiance or 'doing it deliberately'. In overflow soiling the child cannot feel it. Blame and punishment increase withholding and worsen the cycle (NICE, 2010, CG99).",
  "NOT diarrhoea. Overflow soiling can look like loose stool; it is actually a sign of constipation. Stopping 'loose' stool with the wrong approach can make it worse — medical assessment matters.",
  "NOT evidence of abuse by itself. Most soiling is caused by constipation. Treating a soiling child as a probable abuse victim causes harm; ignoring clear indicators also causes harm. Hold both.",
  "NOT a behaviour for school to manage with sanctions, sticker charts for 'clean pants', or sending the child home as a rule.",
  "NOT resolved quickly. Treatment commonly takes months, and relapse is common — plans need to last (NICE, 2010, CG99).",
  "NOT the family's fault. Parents are often exhausted and ashamed; they need information and support, not blame.",
 ],

 "prevalence": [
  "OVERALL: DSM-5-TR reports that approximately 1% of 5-year-olds have encopresis (APA, 2022 — check before quoting).",
  "CONSTIPATION: most childhood soiling is associated with constipation (NICE, 2010, CG99; APA, 2022) — check the exact proportion before quoting.",
  "SEX RATIO: more common in boys (APA, 2022 — check).",
  "IRELAND: no Irish prevalence figure stated here — check before quoting.",
  "PSYCHOLOGICAL DIFFICULTIES: children who soil have higher rates of emotional and behavioural difficulties and are more often bullied than peers (Joinson et al., 2006) — rates not stated here, check.",
 ],

 "cooccurring": [
  {"name": "CONSTIPATION", "rate": "the most common associated factor — check proportion before quoting",
   "presents": "infrequent, large or painful stools, tummy pain, poor appetite, stool withholding postures (crossing legs, standing on tiptoe, hiding). Medical treatment first."},
  {"name": "ENURESIS / DAYTIME WETTING", "rate": "commonly associated — rate not stated here, check",
   "presents": "wetting alongside soiling; constipation affects the bladder too. The GP addresses both."},
  {"name": "ADHD", "rate": "elevated — rate not stated here, check",
   "presents": "ignoring bowel signals while absorbed in activity; difficulty sticking to toilet-sitting routines. Scheduled prompts and routine help."},
  {"name": "AUTISM AND INTELLECTUAL DISABILITY", "rate": "delayed bowel continence more common — rate not stated here, check",
   "presents": "sensory aversion to toilets, rigid routines (e.g., only using a nappy to open bowels), fear of flushing. Adapted toilet training with CDNT."},
  {"name": "ANXIETY AND LOW SELF-ESTEEM", "rate": "elevated (Joinson et al., 2006) — check",
   "presents": "fear of school toilets, avoidance of PE and changing rooms, social withdrawal, school refusal. Often a consequence of soiling and bullying."},
  {"name": "OPPOSITIONAL OR BEHAVIOURAL DIFFICULTIES", "rate": "associated in some children (Joinson et al., 2006) — check",
   "presents": "defiance around toileting, hiding soiled clothes, smearing. Look beneath the behaviour — shame, pain and power struggles are common drivers."},
  {"name": "TRAUMA OR MALTREATMENT", "rate": "a minority — never assumed; rate not stated here",
   "presents": "new-onset soiling with other indicators — fear of a particular person or place, sexualised behaviour, injuries, disclosure, marked change in behaviour. Child protection route."},
 ],

 "recommendations": [
  "MEDICAL CAUSE RULED OUT FIRST: 'It is recommended that parents discuss the soiling with their GP, if not already done, so that constipation and other medical causes can be assessed and treated.' This goes first in the report.",
  "DIGNIFIED TOILETING PLAN, written into an intimate care plan consistent with the school's policy and Children First guidance: a named adult (and a second named adult); a private, clean toilet with a lock; a change kit (wipes, bags, spare clothes) kept discreetly; an agreed discreet signal; a script for staff; and a record kept confidentially.",
  "SCHEDULED TOILET SITTING if the clinical plan includes it (often after meals, when the gut reflex helps): e.g., a few minutes after lunch, discreetly arranged, with a footstool if needed (NICE, 2010, CG99 — follow the treating clinician's instructions).",
  "FREE TOILET ACCESS at all times. Never withhold or delay toilet access as a sanction or classroom rule.",
  "PROTECT FROM BULLYING AND EXCLUSION: act quickly on teasing; do not send the child home routinely — this can reinforce withholding and damage attendance; do not exclude from trips or PE (plan discreetly instead).",
  "SUPPORT SELF-ESTEEM AND PARTICIPATION: strengths-based roles, a key adult, friendship support.",
  "CONTINUUM LEVEL: Classroom Support for discreet access and a change plan; School Support where bullying, self-esteem or attendance is affected; School Support Plus where paediatrics, continence services, CAMHS or CDNT are involved.",
  "REFER: GP → paediatrics / continence service. CAMHS or Primary Care Psychology if significant emotional or behavioural difficulties persist once the medical plan is in place. CDNT for children with disabilities. Tusla where child protection concerns arise. DO NOT diagnose, or advise on laxatives, diet or medication (PSI 2.2.2).",
 ],

 "explain_parent": [
  "'Soiling is much more common than people think, and it's usually caused by constipation. The bowel gets stretched and stops giving the right signals, so leaks happen without him feeling them.'",
  "'That means he really can't control it at the moment. Telling off or punishing makes children hold on more, which makes it worse.'",
  "'The GP is the right first step — treatment usually starts with clearing things out and keeping things soft, and it can take months. That's normal.'",
  "'In school, we'll put a private plan in place: a named adult, a clean toilet, spare clothes, and no fuss. We'll deal firmly with any teasing.'",
  "'I know this can be exhausting and upsetting for the whole family. You're not doing anything wrong by asking for help.'",
  "SIGNPOST: GP; Public Health Nurse; continence services (check locally); ERIC, The Children's Bowel & Bladder Charity (UK) for practical information — check current resources and note it is UK-based.",
 ],

 "explain_teacher": [
  "'This is a medical problem — usually constipation. He often can't feel it happening. It isn't bad behaviour or laziness.'",
  "'Please never make comments in front of the class or send him out with a public message. Use the agreed signal and the named adult.'",
  "'Toilet access whenever he needs it — no waiting. And don't send him home as a routine; that tends to make things worse.'",
  "'If you notice smell, just use the quiet signal and let the named adult take it from there. Keep your tone ordinary.'",
  "'Teasing needs to be stopped straight away. Children who soil are bullied more — protecting him is part of the plan.'",
  "'If you ever notice other things that worry you — injuries, fear of someone, something he says — follow the child protection procedure. The soiling alone is not a reason for concern about abuse.'",
 ],

 "explain_child": [
  "YOUNGER: 'Sometimes poo gets stuck and the tummy gets stretched, so it can't feel when poo is coming. That's why accidents happen. It's not your fault. The doctor and your mum are going to help your tummy get better.'",
  "OLDER: 'This is a body thing, usually from constipation. Your bowel's signals aren't working properly right now. It takes time, but it does get better.'",
  "ASK: 'What's the hardest part about school at the moment?' · 'Are the toilets OK to use?' · 'Has anyone said anything unkind?'",
  "ASK: 'If you needed to change, what would help? Who would you want to help you?' — the child chooses the adult and the signal.",
  "AGREE what classmates know (usually nothing) and reassure the child that staff will keep it private.",
 ],

 "analogies": [
  "THE OVERSTRETCHED BALLOON: 'When a balloon is blown up too much and let down, it goes floppy. The bowel is like that — it's been stretched and needs time to get its shape and feeling back.' Works with parents and children.",
  "THE TRAFFIC JAM: 'Hard poo is stuck like a traffic jam, and the runny stuff squeezes past it. That's why it looks like diarrhoea but it's actually constipation.' Works with parents and teachers.",
  "THE BROKEN DOORBELL: 'The bell that tells him poo is coming isn't ringing properly at the moment. He can't answer a bell he can't hear.' Works with teachers who think the child 'must know'.",
 ],

 "language": [
  "Say 'soiling' or 'accidents', or the family's words; use 'poo' with children if that is the family's word.",
  "Avoid 'dirty', 'smelly', 'baby', 'disgusting', 'deliberate', 'lazy' — in speech and writing.",
  "In reports: factual and minimal — 'soiling, under GP review; intimate care plan in place' — the child or family may read it later.",
  "Write any safeguarding concern in the child protection record, not in the psychological report, and state facts rather than inferences.",
 ],

 "red_flags": [
  "RED FLAG — soiling together with other indicators of harm: disclosure, sexualised behaviour inappropriate to age, genital or anal injury or soreness noticed during intimate care, fear of a particular adult or place, or marked unexplained change in behaviour → child protection route: report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty. NICE child maltreatment guidance (NICE, 2009, CG89) lists some wetting and soiling presentations among alerting features in specific contexts — check the exact wording. Soiling ALONE is not evidence of abuse; never assume it.",
  "RED FLAG — neglect indicators (child repeatedly sent to school soiled, no medical care sought despite advice, poor hygiene with other neglect signs) → discuss with DLP and follow the child protection route.",
  "RED FLAG — soiling with weight loss, blood in stool, vomiting, a swollen abdomen or leg weakness → urgent medical review the same day.",
  "BOUNDARY — you do not diagnose, examine, or advise on laxatives, diet or medication (PSI 2.2.2). Intimate care is carried out under the school's policy, not by the EP.",
  "WATCH — school practices that punish or shame: sending home routinely, restricting toilets, public comments, reward charts for 'clean pants' the child cannot control.",
 ],

 "child_voice": [
  "PRIVATE CONVERSATION WITH A TRUSTED ADULT — good because shame is the main barrier and the child will only speak where safe and private.",
  "DRAWING OR MAPPING THE SCHOOL DAY (where it's hard, where it's OK) — good because it shows toilet, PE and yard barriers without direct discussion of soiling.",
  "PIERS-HARRIS 3 or another self-concept measure — good because self-esteem is often affected and this gives the child a voice in describing it.",
  "CHILD CHOOSES elements of the plan (named adult, signal, change location) — good because control over dignity rebuilds confidence and engagement.",
  "SOLUTION-FOCUSED SCALING at reviews — good because it tracks how school feels without requiring the child to describe accidents.",
 ],

 "questions": [
  "Q: 'He's doing it on purpose — he knows when he needs to go.' — A: 'With constipation-related soiling, the bowel is stretched and he often can't feel it. It looks deliberate but usually isn't. Punishment makes children hold on more.'",
  "Q: 'Should we send him home when it happens?' — A: 'Not as a rule. A private change plan keeps him in school. Sending home can make him hold on and miss learning.'",
  "Q: 'Is this a sign of abuse?' — A: 'Almost always, no — it's usually constipation. We don't assume abuse from soiling. But if there are other worrying signs, we follow the child protection procedure as we would for any child.'",
  "Q: 'Who changes him?' — A: 'That's set out in the school's intimate care policy and plan — usually two named adults, with parents' agreement. SNA support depends on the current SNA guidance and allocation — check.'",
  "Q: 'The GP gave medicine and it's worse — he's leaking more.' — A: 'That's something to tell the GP straight away; they may adjust the plan. It's their decision. In school, we'll make sure the change plan copes with it.'",
  "Q: 'How long will this take?' — A: 'Often months, and setbacks are normal. We'll plan for the long run and review regularly.'",
  "Q: 'Should he have a reward chart?' — A: 'If the treating team uses one, reward things he can control — like sitting on the toilet after lunch — not clean pants.'",
 ],

 "supervision": [
  "Bring any case where soiling sits alongside other possible indicators of harm — talk through threshold, the Children First route and what to record, the same day if needed.",
  "Discuss how to write about soiling in a report with dignity and minimal detail.",
  "Ask how the school's intimate care policy works and how to recommend a plan that fits it.",
  "Reflect on your own reactions (disgust, embarrassment) and how they might leak into language or recommendations.",
 ],

 "reflection": [
  "ON MEDICAL FIRST — did I confirm GP involvement before anything else?",
  "ON DIGNITY — would the child be comfortable with every word in the plan and the report?",
  "ON SAFEGUARDING — did I hold the possibility in mind without assuming it, and act on any other indicators?",
  "ON SCHOOL PRACTICE — did I challenge sending home, toilet restrictions or punishments?",
  "ON THE FAMILY — did parents leave less ashamed than they arrived?",
  "WHAT GOOD LOOKS LIKE: 'GP review in place; intimate care plan with two named adults, private toilet, change kit and discreet signal; toilet sitting after lunch as per GP plan; anti-bullying response; self-esteem support; review with child and parents in six weeks.'",
  "WHAT POOR LOOKS LIKE: 'Parents to be called to collect him after each incident; loss of yard time for accidents.' — punitive, increases withholding, damages attendance and self-worth.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787",
  "Hyams, J. S., Di Lorenzo, C., Saps, M., Shulman, R. J., Staiano, A., & van Tilburg, M. (2016). Childhood functional gastrointestinal disorders: Child/adolescent. Gastroenterology, 150(6), 1456–1468.",
  "Joinson, C., Heron, J., Butler, U., von Gontard, A., & the Avon Longitudinal Study of Parents and Children Study Team. (2006). Psychological differences between children with and without soiling problems. Pediatrics, 117(5), 1575–1584.",
  "National Institute for Health and Care Excellence. (2010). Constipation in children and young people: Diagnosis and management (Clinical Guideline CG99). https://www.nice.org.uk/guidance/cg99 — check for updates.",
  "National Institute for Health and Care Excellence. (2009). Child maltreatment: When to suspect maltreatment in under 18s (Clinical Guideline CG89). https://www.nice.org.uk/guidance/cg89 — check for updates.",
  "Tabbers, M. M., DiLorenzo, C., Berger, M. Y., Faure, C., Langendam, M. W., Nurko, S., Staiano, A., Vandenplas, Y., & Benninga, M. A. (2014). Evaluation and treatment of functional constipation in infants and children: Evidence-based recommendations from ESPGHAN and NASPGHAN. Journal of Pediatric Gastroenterology and Nutrition, 58(2), 258–274.",
  "von Gontard, A., Baeyens, D., Van Hoecke, E., Warzak, W. J., & Bachmann, C. (2011). Psychological and psychiatric issues in urinary and fecal incontinence. The Journal of Urology, 185(4), 1432–1437.",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government of Ireland.",
  "Azrin, N. H., & Foxx, R. M. (1971). A rapid method of toilet training the institutionalized retarded. Journal of Applied Behavior Analysis, 4(2), 89–99.",
 ],

 "pathway": {
  "age": "Diagnosis from age 4 (or equivalent developmental level). Often noticed in the infant classes and early primary, when accidents in school become visible and peers notice; can begin or recur at any age, including after a painful episode of constipation or a life stressor.",
  "who_diagnoses": "Ireland: GP and paediatrics (constipation and soiling), paediatric gastroenterology for complex cases, continence services where available; CAMHS where emotional factors dominate; CDNT for children with disabilities. The EP does not diagnose.",
  "who_wrote_report": "GP letter, paediatrician, gastroenterologist, continence nurse, CAMHS clinician or CDNT. Check whether constipation has been assessed and what the treatment plan is.",
  "refer_to": "GP first → paediatrics / continence service. CAMHS or Primary Care Psychology if emotional or behavioural difficulties persist once medical treatment is in place. CDNT where there is a disability. Tusla if child protection concerns.",
  "sooner": "'Families often feel too embarrassed to ask, or are told children will grow out of it. What matters is that you've asked now. It usually starts with the GP, and it does get better with the right plan.'",
 },

 "differential": [
  "FUNCTIONAL CONSTIPATION WITH OVERFLOW — the commonest cause; medical treatment.",
  "MEDICAL CAUSES — Hirschsprung disease, spinal problems, coeliac disease, thyroid, anal fissure; GP and paediatrics exclude.",
  "TOILET TRAINING NOT YET ESTABLISHED — judge against developmental level, especially in autism and intellectual disability.",
  "TOILET AVOIDANCE AT SCHOOL — fear of school toilets (dirty, no locks, bullying, sensory) leading to withholding.",
  "EMOTIONAL OR BEHAVIOURAL FACTORS — non-retentive soiling linked to stress, family change or power struggles.",
  "MALTREATMENT — a small minority; considered only with other indicators; child protection route.",
 ],

 "next": [
  "Confirm GP/paediatric review; recommend it first in the report.",
  "Agree a written intimate care plan with the child, parents and principal.",
  "Address bullying, sending-home practices and toilet access.",
  "Hold safeguarding in mind; act on any other indicators the same day.",
  "Review in six weeks; refer for psychological support if difficulties persist once the medical plan is in place.",
 ],

 "presentations": [
  "Soiling accidents in school",
  "Stool withholding",
  "Smell and peer rejection",
  "Hiding soiled clothing",
  "Toilet avoidance at school",
  "Shame, low self-esteem and school avoidance",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — diagnosis from age 4; toilet training timing varies widely before then.",
   "prevalence": "Not diagnosed under 4 — constipation in young children is common (check figures).",
   "see": "A preschooler who withholds stools, is frightened of the toilet, or soils after a painful bowel movement. GP for constipation; relaxed, consistent routines in preschool; no pressure or shaming.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "Vineland-3"],
  },
  "School Age": {
   "applies": "YES — the main band for referral.",
   "prevalence": "DSM-5-TR: around 1% of 5-year-olds (check before quoting).",
   "see": "Accidents in class, smell noticed by peers, hiding soiled clothes, avoiding school toilets, teasing and isolation. Medical review first; intimate care plan; anti-bullying; self-esteem support; safeguarding held in mind but never assumed.",
   "tools": ["SDQ", "Piers-Harris 3", "Vineland-3"],
  },
  "Adolescent": {
   "applies": "RARELY — uncommon, but often with greater shame and emotional impact.",
   "prevalence": "Rate not stated here — check.",
   "see": "A teenager who soils is likely to be hiding it, avoiding PE, trips and friendships, and may be very low. Medical review; highly discreet plan; check mood and self-harm; hold safeguarding in mind.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Piers-Harris 3"],
  },
  "Young Adult": {
   "applies": "RARELY — for the school EP.",
   "prevalence": "Rate not stated here — check.",
   "see": "Persisting faecal incontinence into adulthood is usually managed by adult gastroenterology or disability services; transition planning and dignity at college or work.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — bowel continence is often delayed in children with intellectual disability and autism.",
   "prevalence": "Delayed continence more common — rate not stated here, check.",
   "see": "A child who opens bowels only in a nappy, fears flushing, or smears. Medical review for constipation (often underlying), sensory-adapted toileting, visual schedules, structured toilet training (e.g., based on Azrin & Foxx, 1971), and an intimate care plan with CDNT and SNA support. Safeguarding held in mind — children with disabilities are at higher risk of abuse and less able to tell.",
   "tools": ["Vineland-3 / ABAS-3", "Functional behaviour assessment (ABC)", "Communication Matrix / AAC review"],
  },
 },
},

]
