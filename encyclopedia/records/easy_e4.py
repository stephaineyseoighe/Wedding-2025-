"""Easy Read versions of presentation entries 77 onwards (records/easy_e4.py)."""

_H = ["WHAT IT IS", "WHAT YOU MIGHT NOTICE", "WHAT HELPS", "WHO CAN HELP", "WORDS TO KNOW"]
EASY = {}


def _add(name, body):
    parts = [p.strip() for p in body.strip().split("\n#\n")]
    assert len(parts) == 5, name
    out = []
    for h, p in zip(_H, parts):
        out.append(h)
        out.extend("• " + line.strip() for line in p.splitlines() if line.strip())
    EASY["presentation::" + name] = "\n".join(out)


_add("Anxiety secondary to an unmet learning need", """
This is worry that comes from a learning difficulty. No one has spotted it or helped with it yet.
The work feels too hard, again and again. Mistakes happen in front of others.
When the learning need gets help, the worry often gets less.
#
Worry in some lessons, like English, Irish or maths. Less worry in sport or art.
Not wanting to read aloud. Tummy aches before spelling tests.
Older pupils may start to miss school.
#
Help with the learning need first, like extra reading or maths support.
No reading aloud without a chance to practise first. Other ways to do work. Extra time in tests.
Tell the pupil why the work is hard. Knowing why can ease the worry.
Check both learning and worry at each review.
#
The school and the psychologist look at the learning need first.
If the worry stays after help, or is very bad, the GP or CAMHS can help.
If a child talks about self-harm, act the same day.
#
Anxiety: strong worry or fear.
GP: general practitioner. Your family doctor.
CAMHS: Child and Adolescent Mental Health Services. The health service for young people with serious mental health needs.
""")

_add("Rigidity and routine that is not OCD", """
A strong need for things to stay the same. The child likes set routines and rules.
Change can cause real upset. This is not the same as OCD.
Routines are normal in young children. Needing sameness can be part of autism. It can also come from worry about what comes next.
#
Upset when there is a new teacher or the timetable changes.
Needing to do things one set way. Finding it hard to switch tasks.
This is not being stubborn. The upset is real.
#
Picture timetables. Warning before changes.
Small planned changes, with support and praise, step by step.
Keep harmless routines that help the child feel calm. Do not force them to stop.
#
The school plans ahead for changes it knows about.
The CDNT or CAMHS can look at autism. The GP can help if OCD is a worry.
The psychologist describes what they see. They do not diagnose autism or OCD.
#
OCD: obsessive compulsive disorder. Unwanted thoughts push a person to do things to ease the worry.
Autism: a different way of thinking, talking and sensing the world.
Diagnose: to say formally what condition someone has.
CDNT: Children's Disability Network Team.
CAMHS: Child and Adolescent Mental Health Services.
GP: general practitioner. Your family doctor.
""")

_add("Repeated checking of work", """
A pupil checks, redoes or rubs out work again and again. They may keep asking "Is this right?"
This slows their work down, or stops it.
Checking eases worry for a moment. But the more you check, the less sure you feel.
It can be part of OCD, worry or wanting things perfect. It can also be a fair habit for a pupil who makes more mistakes.
#
Very slow work, or work not finished.
Holes rubbed in the page. This is checking, not being careless.
Older pupils may run out of time in exams.
#
Agree one check for each task, or a checklist to use once. Praise stopping.
Answer "Is this right?" once. Then say "You've checked. Trust it."
In tests: mark it, move on, come back once.
Tools like spell-checkers if there is a real learning need.
#
Teachers and parents can use the same plan.
If it might be OCD, the GP can refer to Primary Care Psychology or CAMHS.
Special OCD therapy is done by health services, not by the school psychologist.
#
OCD: obsessive compulsive disorder. Unwanted thoughts push a person to do things to ease the worry.
GP: general practitioner. Your family doctor.
CAMHS: Child and Adolescent Mental Health Services.
Refer: to ask another service to help.
""")

_add("Ritual at transitions", """
A set of steps a child must do when changing activity. For example, touching the door frame, or packing a bag in one order.
The change cannot go on until the steps are done. Stopping them causes big upset.
Little rituals are normal in young children. What matters is how strong and costly they are.
The same ritual can have different reasons: autism, worry or OCD. The reason decides what helps.
#
Rituals at the start of the day, coming in from the yard, or going home.
Rituals may need a closer look if they last past age 6 or 7, take more than a few minutes, or the child hides them.
Teenagers may hide rituals, like counting in their head or arriving late.
#
Make changes easy to predict: picture timetables, a "now and next" board, a warning, the same adult at the door.
Allow short harmless rituals. Agree small changes with the child. Never take a ritual away without warning.
Fewer room changes where possible.
#
The school writes the supports into the student support file.
The GP can refer to Primary Care or CAMHS if rituals come from scary thoughts, take lots of time, or got worse fast.
The CDNT can help if autism has not been looked at.
#
Ritual: a set of steps done the same way every time.
OCD: obsessive compulsive disorder. Unwanted thoughts push a person to do things to ease the worry.
GP: general practitioner. Your family doctor.
CAMHS: Child and Adolescent Mental Health Services.
CDNT: Children's Disability Network Team.
""")

_add("Low mood without diagnostic threshold", """
A young person seems sadder, flatter or harder on themselves than usual. It affects how they get on in school.
No one has said they have depression. You should not suggest it.
Low mood like this is common. It still matters and needs support.
#
Sadness that goes on for weeks and changes how they cope.
Low mood can show as being cross or saying no, not just sadness.
Normal sadness after a loss that is easing with time is different.
#
One key adult who checks in often and briefly.
Small, doable activities they used to enjoy, like a club or time with a friend.
Deal with what keeps the low mood going, like bullying or too much work.
Review after 4 to 6 weeks. If it is not better, get more help.
#
The GP, Jigsaw, Primary Care Psychology or CAMHS. The GP can refer on.
The psychologist describes the mood and checks for risk. They do not diagnose depression.
#
Depression: a health condition with long-lasting low mood.
Diagnose: to say formally what condition someone has.
GP: general practitioner. Your family doctor.
Jigsaw: a youth mental health service for ages 12 to 25.
CAMHS: Child and Adolescent Mental Health Services.
""")

_add("Loss of interest in school activities previously enjoyed", """
A pupil used to love something, like hurling, choir or art. Now they have stopped going or trying.
The adults who knew them before notice the change.
It can be a sign of low mood. But it can have other reasons too.
#
They say things are boring or pointless, or they are tired.
They drop activities and do not replace them with anything.
Changing interests as you grow up is normal. Dropping everything is the worry.
#
Find out if something happened, like bullying or a new coach. Fix that if you can.
Reconnect with one thing they liked, in a small easy way.
Less pressure to perform for a while. Review in 4 to 6 weeks.
It is not laziness. Telling them to try harder rarely helps.
#
The school and a key adult.
The GP, if the loss of interest is wide, lasts weeks and comes with other signs of low mood. The GP can refer to Primary Care or CAMHS.
If they talk about not wanting to be alive, follow the school's safety steps that same day.
#
Low mood: feeling sad, flat or down.
GP: general practitioner. Your family doctor.
CAMHS: Child and Adolescent Mental Health Services.
""")

_add("Withdrawal from peers", """
A child spends less time with other children than before. For example, eating alone or staying in at break.
Some children pull back. Other children are pushed out by their peers. These need different help.
Some children want to join but feel shy. Some are happy alone.
Withdrawal can be a sign of low mood.
#
A change from how the child used to be.
The child seems upset or lonely.
A child who has always liked quiet time and is happy is not a worry.
#
Structured time with others, like a lunch club, a buddy or a shared job.
Work with the class group if the child is being left out.
A key adult who checks in on how they feel.
Do not just tell them to go and play. This can make it worse.
#
The school deals with any bullying.
If you worry about abuse, tell Tusla (the child and family agency) quickly.
If they talk about self-harm, act the same day. The GP or CAMHS can help.
#
Peers: children of the same age.
Withdrawal: pulling away from other people.
Tusla: the Child and Family Agency.
GP: general practitioner. Your family doctor.
CAMHS: Child and Adolescent Mental Health Services.
""")

_add("Irritability as the presentation of low mood in young people", """
Low mood does not always look like sadness.
In some young people it looks like being cross, snappy or quick to anger.
School may see it only as bad behaviour. Then the low mood is missed.
#
Snapping, getting angry fast, sulking.
Getting upset easily when things go wrong.
It lasts a long time, happens in many places, and is a change from before.
#
See the anger as a sign of how the pupil feels, not just as behaviour.
Stay calm. Give them time and space. Talk about it later.
A key adult who checks in on mood.
Punishments on their own do not help the mood underneath.
#
Parents can help with sleep and other things at home.
The GP can refer to Primary Care or CAMHS if it lasts and comes with other signs of low mood.
If they talk about self-harm, act the same day.
#
Low mood: feeling sad, flat or down.
Irritability: getting cross or angry easily.
GP: general practitioner. Your family doctor.
CAMHS: Child and Adolescent Mental Health Services.
""")

_add("Complex or developmental trauma", """
This describes the effects of harm that happened again and again while a child was growing up. It is often abuse, neglect or violence at home.
It can affect trust, feelings, behaviour, learning and how the child sees themselves.
It is not a diagnosis. The psychologist does not say a child "has" it.
#
Always being on guard. Getting upset very fast.
Finding it hard to trust adults. Feeling shame. Trying to control things.
Finding changes and goodbyes hard.
Other needs, like ADHD or a language difficulty, can be missed.
#
Safety, connection and calm come first.
A named key adult and a steady routine.
Warn the child about changes. Plan goodbyes.
Clear, kind limits. Fix things after an upset. Do not shame.
#
Services work together through one plan, including Tusla social workers and CAMHS.
The GP can refer to CAMHS if things are severe.
If you see signs of abuse, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own.
#
Trauma: the effect of very frightening or harmful events.
Diagnosis: a formal name for a condition, given by a qualified person.
ADHD: attention deficit hyperactivity disorder.
Tusla: the Child and Family Agency.
CAMHS: Child and Adolescent Mental Health Services.
GP: general practitioner. Your family doctor.
""")

_add("Adverse Childhood Experiences (ACEs)", """
ACEs are hard things that can happen in childhood, like abuse, neglect or problems at home.
Research found that adults who had more ACEs had more health problems, on average.
This is a research idea. It is not a way to score one child.
#
An ACE score does not predict what will happen to one child.
Most children with many ACEs do not end up with these problems.
Caring adults and feeling you belong at school protect children.
Calling a child "high ACE" is unfair and wrong.
#
A named key adult and a sense of belonging, like clubs or jobs.
Steady routines.
Use ACE ideas to make the whole school more caring, not to pick out children.
Do not write ACE scores in reports.
#
Tusla family support can help families who need it.
If you find out about abuse happening now, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own.
#
ACE: adverse childhood experience. A hard or harmful thing that happens in childhood. ACEs means more than one.
Tusla: the Child and Family Agency.
Neglect: when a child's basic needs are not met.
""")

_add("Bereavement reaction", """
This is how a child reacts when someone important to them dies.
Grief is a normal response to loss. It is not an illness.
Children's grief comes and goes. They can be very sad one moment and playing the next. This does not mean they do not care.
Grief can come back at big moments, like Confirmation or exams.
#
Grief that comes and goes, or comes back at big moments.
Wanting to talk about the person, or not wanting to.
Staying close to the person in memory is normal and helpful.
#
A named adult speaks to the child soon after they come back.
Agree with the child what the class will be told.
A quiet space or time-out card. Less homework for a while, with a review.
Note the date of the death, so teachers can plan for it each year.
Do not avoid talking about the person who died.
#
The Irish Childhood Bereavement Network, Barnardos and Rainbows Ireland. The GP if you are worried.
If a death affects the whole school, NEPS helps the school respond.
If the child talks about wanting to die, act the same day.
#
Bereavement: when someone close to you dies.
Grief: the feelings you have after a loss.
GP: general practitioner. Your family doctor.
NEPS: National Educational Psychological Service. The psychologists who work with schools.
""")

_add("Displacement, asylum and resettlement", """
This is about children who had to leave their home country and are settling in Ireland.
Things before, during and after the journey can affect them.
Most of these children cope well. They do best with a stable school, language support and a sense of belonging.
#
Many have lived through scary events. Not all are traumatised.
Good playground English can hide difficulty with school English.
Not knowing English well is not a learning difficulty.
#
Belonging and safety first: a buddy, a named adult, picture timetables, a steady routine.
Support with English. Value and keep the home language.
Use an interpreter to talk with families.
Do not push the child to tell their story.
Give time and language support before testing for special needs.
#
Tusla, community groups and the GP.
Signs of trafficking or abuse: tell Tusla (the child and family agency) quickly.
If the child talks about self-harm, act the same day.
#
Asylum: safety given by a country to someone who fled danger.
Traumatised: badly affected by a very frightening event.
Interpreter: a person who changes speech from one language to another.
Tusla: the Child and Family Agency.
GP: general practitioner. Your family doctor.
""")

_add("Trauma-informed classroom practice", """
A way of running the whole class and school. It assumes some pupils have lived through hard things.
Routines, relationships and responses to behaviour are set up to help, not to cause more harm.
Staff do not need to know which pupils have had hard times.
The ideas are sound. But research has not yet tested specific packages well.
#
Calm adults and steady routines.
Helping a child calm down before talking about consequences.
Fixing relationships after a conflict.
It still has rules and limits. It is not therapy.
#
Picture timetables and warning before changes.
A calm voice, fewer people watching, time to settle. Then talk.
Staff learn to coach children about feelings.
Staff need support too. Calm staff help calm children.
#
The whole school team.
If a child tells you about abuse, tell Tusla (the child and family agency) quickly.
Talk to the principal about staff support if staff are worn out.
#
Trauma: the effect of very frightening or harmful events.
Trauma-informed: aware of how trauma affects people, and acting on it.
Tusla: the Child and Family Agency.
""")

_add("Emotionally Based School Avoidance (school refusal)", """
A child finds it very hard to go to school because of strong feelings, usually worry.
Parents know about the absence. They have usually tried hard to get the child to school.
It is not a diagnosis. It describes what is happening.
#
Worry, upset or tummy aches about going to school.
It is different from mitching, where the child hides the absence from parents.
Worry, low mood, learning needs, autism and bullying can all play a part.
#
Act early. Do not wait until the child "feels ready". Staying away makes the return harder.
A step-by-step return plan agreed with the young person.
A key adult, a safe place in school, and a warm welcome each morning.
Do not blame parents. They are often worn out from trying.
#
The school, the parents and the psychologist plan together.
The GP can refer to Primary Care or CAMHS if worry or low mood is serious.
The principal must tell Tusla's school attendance service when absences reach a set level.
#
EBSA: emotionally based school avoidance.
Diagnosis: a formal name for a condition, given by a qualified person.
GP: general practitioner. Your family doctor.
CAMHS: Child and Adolescent Mental Health Services.
Tusla: the Child and Family Agency.
""")

_add("Truancy distinguished from EBSA", """
Truancy means a young person misses school without their parents knowing, or against their wishes.
They are usually not at home. They are not very worried about school itself.
This is different from EBSA. It needs a different plan.
Truancy can be a sign of an unmet need, like a learning difficulty, bullying or trouble at home.
#
Ask: do the parents know? Where is the young person? Are they upset about school?
Some who mitch are avoiding one thing they fear, like a test or a bully. Ask them.
The two can mix or change over time.
#
Build a link first: a key adult, a mentor, or something they like.
Help with the need underneath, like learning support or bullying.
Clear, fair consequences, like calling a parent the same day.
Punishment alone rarely works in the long run.
#
The school's home link teacher and Tusla's school attendance service.
CAMHS, addiction services or Tusla if there are worries about drugs or being used by others.
Signs of being used or harmed: tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own. Call the Gardaí if there is danger now.
#
Truancy: missing school without permission. Also called mitching.
EBSA: emotionally based school avoidance. Missing school because of strong worry.
Tusla: the Child and Family Agency.
CAMHS: Child and Adolescent Mental Health Services.
Gardaí: the Irish police.
""")

_add("Parentally condoned absence", """
A parent keeps the child at home, or lets them stay home, for reasons that are not accepted.
For example, to help at home, for company, or for a holiday in term time.
The parent, not the child, is the main reason for the absence.
Parents have a legal duty about school attendance.
#
Some parents are worn out by their child's upset and have stopped trying.
Some parents need the child at home because of illness, money problems or caring.
It is not always neglect. Understand the family first.
#
A named school contact for the parent.
Practical help, like a breakfast club, transport or a morning routine.
Help for the parent's own needs, like the GP or family support.
Give the child good reasons to come: a friend, a club, a job to do.
#
The school's home link teacher and Tusla's school attendance service.
The psychologist helps plan how attendance can work.
If absence hides harm or neglect, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own.
#
Condoned: allowed.
Neglect: when a child's basic needs are not met.
Tusla: the Child and Family Agency.
GP: general practitioner. Your family doctor.
""")

_add("Absence due to chronic illness", """
A child misses a lot of school because of a long-term health condition. Examples are asthma, diabetes or epilepsy.
Missing school means missed teaching and time away from friends.
The illness itself can also cause tiredness, pain or side effects from medicine.
#
Gaps in learning after time off.
Feeling left out, low or less confident.
Some children also start to worry about coming back.
#
A health care plan made by the school, parents and medical team.
Work sent home, a named contact, and catch-up teaching on return.
Keep the child in touch with classmates, with cards, calls or visits.
Help in state exams if the illness affects how they do.
A shorter school day only with medical advice and a review date.
#
The medical team leads on the illness.
The school and psychologist lead on learning and belonging.
The psychologist does not give advice on medicine or treatment.
#
Chronic illness: an illness that lasts a long time.
Health care plan: a written plan for how school will help with a health need.
""")

_add("Late arrival and partial attendance", """
A pupil is marked present but misses part of the day.
They may come late most days, leave early, or miss certain lessons.
This can be an early sign of a bigger problem with going to school.
#
Lateness can hide in the records because the pupil is "present".
Missing the first lesson every day adds up over a year.
Common reasons: morning worry, sleep problems, caring for others at home, or avoiding one lesson.
#
Make arriving easy: someone to meet them, a quiet place first, a job to do. No public comments about being late.
Talk about sleep with the parent and young person.
Find out why they avoid a certain lesson. Change what you can.
A shorter day only as part of a plan with an end date.
Punishment for lateness can make worry-based lateness worse.
#
The school and the family.
The GP, if sleep problems go on.
Tusla family support, if home life makes it hard.
If lateness hides injury or neglect, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own.
#
Partial attendance: being in school for only part of the day.
Neglect: when a child's basic needs are not met.
GP: general practitioner. Your family doctor.
Tusla: the Child and Family Agency.
""")

_add("Return-to-school planning after extended absence", """
A step-by-step plan to help a pupil come back after a long time away.
The time away might be because of worry, illness, a death, a hospital stay or a family crisis.
The plan uses small agreed steps. Each step adds a bit more time or challenge.
#
Waiting until the child "feels ready" tends to keep the worry going.
Going back full time on day one often does not work after months away.
Setbacks are normal and expected.
#
Write the plan with clear steps, dates and who does what.
Agree what classmates are told. Tell the teachers. Have a safe place and an exit card.
If there is a setback, go back one step, not back to full absence.
Praise each step, not only the final goal.
Every step needs a date and a review.
#
The psychologist often joins up the school, family, young person and any health service.
If the same step keeps failing, look at the plan again. A health referral may help.
If a child talks about self-harm or harm, act the same day.
#
Extended absence: a long time away from school.
Exit card: a card a pupil can show to leave class for a short break.
Referral: asking another service to help.
""")

_add("Pathological Demand Avoidance (PDA) profile", """
A pattern where a child strongly avoids everyday requests.
They may use distraction, excuses or pretend play to avoid them. Under more pressure, they may have a meltdown.
PDA is not an official diagnosis. It is used as a profile, often within autism.
Research on it is small, and experts disagree about it.
Many think the avoidance comes from worry and a strong need for control.
#
Avoiding simple requests, even ones the child might like.
Getting very upset or angry when pushed.
It is not the same as being defiant.
#
Ask in gentle, indirect ways, like "I wonder if..." Give choices.
Agree a few things that must happen, like safety. Be flexible about the rest.
A trusted adult and a safe space.
Use the same approach at home and in school.
Do not drop all expectations.
#
The school and family, often with the CDNT.
Questions about diagnosis go to the CDNT or CAMHS.
If there is injury or self-harm, use a safety plan.
#
PDA: pathological demand avoidance. A name for strong avoidance of requests.
Diagnosis: a formal name for a condition, given by a qualified person.
Autism: a different way of thinking, talking and sensing the world.
CDNT: Children's Disability Network Team.
CAMHS: Child and Adolescent Mental Health Services.
""")

_add("Peer relationship difficulties and social isolation", """
A child finds it hard to make or keep friends.
Other children may ignore them or not want them around.
Being disliked by others is more worrying than being overlooked.
#
Being alone at break.
Being left out of games or groups.
Some children are happy with few friends. The worry is upset or being left out.
It is not a diagnosis. It can go with autism, ADHD, DLD or worry.
#
Involve other children, like buddy systems or Circle of Friends.
Structured break times, like lunch clubs or games.
Teach skills like joining in and taking turns, in real settings.
Teachers show how to include everyone.
#
The school, and sometimes the SLT or the CDNT.
If bullying is the cause, follow the school's bullying steps.
If the child talks about self-harm, act the same day.
#
Peers: children of the same age.
ADHD: attention deficit hyperactivity disorder.
DLD: developmental language disorder. Lasting difficulty learning and using language.
SLT: speech and language therapist.
CDNT: Children's Disability Network Team.
Circle of Friends: a way to get classmates to support a child.
""")

_add("Bullying", """
Bullying is harmful behaviour aimed at someone, again and again.
The person doing it has more power.
It can be physical, words, leaving someone out, or online.
Bullying about who someone is, like race, disability or being gay or trans, is named in Irish rules.
#
A one-off falling out between equals is not bullying. But a serious one-off may still need action.
Bullying is not just part of growing up. It can harm mental health for a long time.
Never blame the child being bullied.
#
Follow the school's anti-bullying rules, called Bí Cineálta.
Whole-school approaches work better than work with one child.
Support for the child being bullied: a key adult, safe spaces, peer support.
Help the children doing the bullying too. Understand their needs.
#
The whole school. The psychologist gives advice but does not investigate.
Sexual bullying, sharing images, or bullying by adults: tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own. The Gardaí may be needed.
If a child talks about self-harm, act the same day.
#
Bí Cineálta: the Irish school rules on bullying. It means "be kind".
Tusla: the Child and Family Agency.
Gardaí: the Irish police.
""")

_add("Social adaptive skills", """
These are everyday social skills. They help you get on with others.
They include making friends, play, coping, following social rules and being responsible.
It is about what a person usually does in real life. Not what they can do in a test.
#
A child may know how to say hello, but not do it in the yard.
Low scores may come from not having the chance to learn, not from low ability.
These skills can be taught. They can grow over time.
#
Teach skills in real places: saying hello, joining in, asking for help, taking turns.
Use pictures and lots of practice.
Make chances to be with others, like clubs and jobs.
Home and school work on the same goals. Set one or two goals and review each term.
#
Parents and teachers fill in rating forms, like the Vineland.
An SLT can help if language is part of the difficulty. The CDNT can help children with disabilities.
If skills are lost, see the GP.
#
Adaptive skills: the everyday skills you need to manage daily life.
Rating form: a list of questions about how a person usually acts.
SLT: speech and language therapist.
CDNT: Children's Disability Network Team.
GP: general practitioner. Your family doctor.
""")

_add("Co-operation with peers in group work", """
This is about how a pupil works with classmates on a task.
It means sharing, taking a role, giving ideas and accepting other ideas.
Group work asks a lot at once: fast talk, a shared goal, taking turns, noise.
Pupils are often put in groups but not taught how to work as a group.
#
Taking over, pulling back, or disrupting the group.
This usually shows a missing skill. It is not refusing.
It is not a diagnosis. It is common with autism, ADHD, DLD, worry, and in very able pupils.
#
Teach group skills first. Give clear roles with role cards, like reader or timekeeper. Swap roles.
Start in pairs, then threes.
Set tasks where each person has a part that the group needs.
Choose a small, patient, stable group.
Tell the pupil the task and their role before it starts.
#
The class teacher, with advice from the psychologist.
The CDNT, Primary Care or CAMHS, only if there are wider social difficulties in many places.
#
Diagnosis: a formal name for a condition, given by a qualified person.
ADHD: attention deficit hyperactivity disorder.
DLD: developmental language disorder.
CDNT: Children's Disability Network Team.
CAMHS: Child and Adolescent Mental Health Services.
""")

_add("Turn-taking and shared play", """
This is about how a young child waits for a turn, gives up a toy, and shares a game.
These skills are the first steps to friendship.
They grow in stages: first with an adult, then with toys, then sharing a game.
Play skills can be taught.
#
Grabbing toys or finding waiting very hard.
Wanting to play but not knowing how to join in.
Many three-year-olds cannot yet wait without help. This is normal.
It is not selfishness or poor parenting.
#
Teach turn-taking with an adult first, then one child, then a small group.
Use a "my turn" card or a sand timer.
Use games about things the child loves, like building bricks.
Teach words to join in, like "Can I play?" Stay close at first.
Praise waiting straight away.
#
The class teacher and early years staff.
The family can ask the CDNT for help if there are other signs, like language delay.
Do not wait to decide.
#
Shared play: playing the same game together.
CDNT: Children's Disability Network Team.
""")

_add("Reading social cues and repair after conflict", """
This is about two skills.
Reading cues: understanding faces, tone of voice and body language.
Repair: noticing you have upset someone and fixing it.
Some children think others mean harm when they do not. Others miss the cue.
Misunderstanding can go both ways, for example between autistic and non-autistic people.
#
Fights or fallings-out that the child did not see coming.
The child is often upset and wants to fix it, but does not know how.
It is common with autism, ADHD, DLD, after trauma, and with little chance to play with others.
#
Teach cues with real class moments, photos and videos.
Talk after a conflict: what happened, who was hurt, how to put it right. An adult helps.
Practise a few phrases when calm, like "Can we start again?"
Help others understand the child's style. A flat face is not rudeness.
Forced "sorry" does not teach real repair.
#
The school, using its approach to fixing harm.
The family can ask the CDNT or an SLT if a communication difficulty may be there.
#
Cues: small signs that show what someone feels or means.
ADHD: attention deficit hyperactivity disorder.
DLD: developmental language disorder.
CDNT: Children's Disability Network Team.
SLT: speech and language therapist.
""")

_add("Masking and the cost of it", """
Masking means hiding your differences to fit in.
For example, copying others, forcing eye contact, or holding back movements that calm you.
Masking takes a lot of effort. It can lead to tiredness, worry and needs being missed.
Most research is on autistic people, especially girls and women.
#
The child seems fine in school but falls apart at home.
Meltdowns, not talking, or being very tired after school.
Parents and teachers may describe two different children.
It is not lying. It does not prove or rule out autism.
#
School and home believe each other and plan together.
Make it safer not to mask: breaks, a quiet space, fidgets, less forced eye contact.
Lighter demands after school. Adjust homework if tiredness is big.
A key adult the child does not need to perform for.
#
The family can ask the CDNT about autism.
CAMHS or Primary Care Psychology if there is low mood, worry or self-harm.
#
Masking: hiding your true self or differences to fit in.
Autism: a different way of thinking, talking and sensing the world.
CDNT: Children's Disability Network Team.
CAMHS: Child and Adolescent Mental Health Services.
""")

_add("Loneliness without observable difficulty", """
Loneliness is the painful feeling that your friendships are fewer or less close than you want.
It is about how it feels, not how many people are around you.
Some pupils seem fine. They have someone to sit with. But they still feel alone.
Adults often miss these quiet pupils.
#
Nothing may show on the outside. You need to ask.
Some pupils like being alone and are happy. Others are always in a group but lonely.
Loneliness can come before or with low mood and worry.
#
Teachers ask every pupil, in private, how connected they feel.
Clubs based on interests, buddies and a steady partner for tasks.
A key adult who asks about friends as well as work.
When moving school, place the pupil with at least one peer they know, if possible.
#
The family can go to Primary Care Psychology, Jigsaw or CAMHS if there is low mood or risk.
If a child talks about self-harm or feeling a burden, act the same day.
If there is a child protection worry, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own.
#
Jigsaw: a youth mental health service.
CAMHS: Child and Adolescent Mental Health Services.
Tusla: the Child and Family Agency.
""")

_add("Self-advocacy", """
Self-advocacy means speaking up for yourself.
You understand your own needs and strengths. You know what help you have a right to.
You tell the right adult what you need. You help lead your own plan.
Children have a right to be heard, and to have their views taken seriously.
#
It matters most when moving on, like to secondary school, state exams or college.
There, adults stop offering help. The student has to ask.
Asking for agreed help is not being demanding.
A pupil who never asks for help, even when stuck, may be worried or feel bad about themselves.
#
Include the pupil in every plan meeting in some way. Write their views in their own words.
Explain their strengths and needs to them in plain words.
Practise short phrases for asking. Help cards for younger pupils.
A one-page profile for the next school, teacher or college.
Younger pupils and those who use AAC can speak up with choices and symbols.
#
A key adult who helps the pupil practise.
Parents, who help decide how and when to share a diagnosis.
The pupil and family decide who else is told about a diagnosis.
#
Self-advocacy: speaking up for yourself.
AAC: augmentative and alternative communication. Ways to talk without speech, like symbols or devices.
Diagnosis: a formal name for a condition, given by a qualified person.
""")

_add("LGBTQ+ identity support", """
Support for pupils who are lesbian, gay, bisexual, trans, questioning, or otherwise LGBTQ+.
The aim is that they are safe, included and able to learn.
Being LGBTQ+ is not a mental health condition. It is not a reason to refer on its own.
When distress happens, it is usually caused by bullying, rejection or unfair treatment. Not by who the person is.
#
Many LGBTQ+ pupils are doing well.
Some face nasty remarks or bullying in school.
Guidance on gender identity for young people is still changing, and experts disagree.
#
Deal with homophobic and transphobic bullying under the school's Bí Cineálta rules.
At least one named adult the pupil trusts. Signs that show the school is welcoming.
Let the pupil control who knows. Never "out" a pupil. If safety means you must share, explain why first.
Requests about names or uniform are school decisions with the pupil and parents. Check current guidance.
Never try to change a person's sexuality or gender identity.
#
BeLonG To supports schools.
The family can go to Primary Care Psychology, Jigsaw or CAMHS for mental health needs.
The GP can refer to specialist gender services if the young person and family want this.
#
LGBTQ+: lesbian, gay, bisexual, transgender, questioning, and others.
Out: to tell others someone is LGBTQ+ without their agreement.
Bí Cineálta: the Irish school rules on bullying.
CAMHS: Child and Adolescent Mental Health Services.
GP: general practitioner. Your family doctor.
""")

_add("Cultural and linguistic identity", """
This is about how a pupil's culture, religion and languages shape their time in school.
It includes newcomers, Travellers, Roma pupils, Irish speakers and Deaf pupils who use Irish Sign Language.
It is not a disorder.
Pupils who keep both their home culture and their new one usually do best.
#
A pupil may sound fluent in chat within a year or two.
School language takes much longer to learn. This is often misread.
Learning English is not a special educational need in itself.
Do not lower expectations because of background.
#
Say the pupil's name correctly. Show their languages and cultures in class.
Teach subject words ahead. Use pictures. Let them think in their home language.
Use interpreters with families. Do not ask the child to interpret.
Deal with racism through the school's bullying rules.
#
Teachers and language support staff.
The family can go to an SLT or the CDNT only if there is a difficulty in the home language too.
Do not decide there is a language disorder, learning disability or autism from English-only tests.
#
Traveller: a member of the Irish Traveller community, a recognised ethnic group.
Interpreter: a person who changes speech from one language to another.
SLT: speech and language therapist.
CDNT: Children's Disability Network Team.
""")

_add("Attitude towards staff", """
This describes how a pupil gets on with adults in school.
They may be warm, wary, rude, too friendly or not interested.
It is about the relationship, not only the child.
Good relationships with teachers help pupils learn and take part.
#
The pupil may get on well with some adults and badly with others. That difference tells you something.
The attitude often has a history, like past unfair treatment or work that is too hard.
It is not a fixed part of the child. It is not a diagnosis.
#
Build the relationship on purpose. Short, regular one-to-one time where the teacher follows the child's lead.
A friendly hello each day, not linked to work or behaviour.
Learn what works for the adults the pupil gets on with. Share it.
After a conflict, the adult makes a fresh start.
If the work is too hard, change the work.
Do not write "poor attitude" in a report.
#
The class teacher and a key adult.
If a child seems afraid of adults, think about trauma. Follow the child protection steps if you are worried.
#
Trauma: the effect of very frightening or harmful events.
Diagnosis: a formal name for a condition, given by a qualified person.
Child protection: the rules and steps to keep children safe from harm.
""")

_add("Trust and the effect of one key adult", """
Some pupils find it hard to trust adults in school.
One trusted adult can make a big difference to how they cope.
Early relationships shape whether a child expects adults to be safe.
Irish research shows that young people with "one good adult" have better mental health.
#
The pupil may test, avoid or cling to adults.
A strong bond with a key adult is not a problem to stop. Independence grows from feeling safe.
It is not the same as the rare condition called attachment disorder.
#
Choose a key adult the pupil already trusts. Give them time for short, regular contact.
Plan for absence: a second known adult and warning before changes.
Support the key adult. This is hard work.
The key adult helps the pupil build more trusting relationships.
#
The key adult supports. They do not give therapy.
The family or social worker can ask CAMHS, Primary Care Psychology or Tusla for specialist help.
If a child tells the key adult about abuse, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own.
#
Key adult: one trusted adult in school who is there for the pupil.
Attachment: the bond a child forms with the people who care for them.
CAMHS: Child and Adolescent Mental Health Services.
Tusla: the Child and Family Agency.
""")

_add("Response to authority and to being corrected", """
This describes what a pupil does when an adult tells them what to do or corrects them.
They may do it, argue, shut down, get angry, laugh or cry.
Being corrected can make some pupils feel shame. They defend themselves rather than defy.
Some expect to be rejected. They take small corrections very hard.
Poor reactions often show missing skills, not unwillingness.
#
The worst reactions come with certain triggers. Finding them is key.
It is not always defiance. It can be shame, worry, confusion, too much noise, or feeling it is unfair.
It is not proof of ODD.
#
Correct in private and keep it short. Use a quiet word or an agreed signal.
Talk about the task, not the person. Say "the next step is", not "you're lazy".
Reconnect soon after, so the pupil knows the relationship is fine.
Work with the pupil on the times this keeps happening.
More punishment usually makes it worse.
#
The class teacher and school team.
The family can go to CAMHS or Primary Care for wider mental health questions.
If a pupil self-harms or says "I'm useless", check risk the same day. If there is a child protection worry, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own.
#
ODD: oppositional defiant disorder. A diagnosis about ongoing angry, defiant behaviour.
Shame: a painful feeling of being bad as a person.
CAMHS: Child and Adolescent Mental Health Services.
Tusla: the Child and Family Agency.
""")

_add("Relationship with the SNA and dependence on adult proximity", """
This is about how a pupil gets on with their SNA, or another adult who is close by most of the day.
It asks if the pupil now needs that adult for things they could do alone.
In Ireland, the SNA helps with care needs. The SNA does not teach.
Research found that having an adult always close by can cut a pupil off from the teacher and classmates.
#
The pupil waits for the adult before starting work.
Less time with classmates.
Upset when the SNA is away.
This is not a criticism of the SNA. It is about how the role is set up.
#
The teacher plans and teaches. The SNA supports care needs. They plan together if possible.
Set goals for doing things alone, like starting work without a prompt.
The SNA sits nearby, not beside. They step back so classmates can join in.
Plan slowly to reduce support. Never take the SNA away suddenly.
#
The school, the parents and the SENO decide together.
SNA support is given through the NCSE, not by the psychologist.
#
SNA: special needs assistant.
NCSE: National Council for Special Education.
SENO: special educational needs organiser. They work for the NCSE and decide on school support.
""")

_add("Help-seeking from adults", """
This is about whether, when and how a pupil asks adults for help.
It can be help with schoolwork, or with feelings and staying safe.
Some pupils do not ask because they fear looking stupid, or they feel embarrassed.
Pupils ask adults they trust and who respond well.
#
A pupil who never asks may still be struggling.
How adults respond decides if the pupil asks again.
It is not a diagnosis. It can go with worry, low mood or language difficulty.
#
Make asking normal. Teachers praise questions. Everyone uses help cards.
Private ways to ask: a help card, a worry box, a named adult.
When a pupil asks, respond warmly and helpfully.
Show the pupil who to ask for what: work, friends, or feeling unsafe.
#
The class teacher, a named adult or the guidance counsellor.
The family can go to Primary Care Psychology, Jigsaw or CAMHS for emotional needs.
If a pupil shows signs of self-harm or abuse, act the same day. Tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own.
#
Guidance counsellor: a teacher trained to help pupils with personal and career choices.
Jigsaw: a youth mental health service.
CAMHS: Child and Adolescent Mental Health Services.
Tusla: the Child and Family Agency.
""")

_add("Uncorrected refractive error", """
This is an eye focusing problem. Glasses could fix it, but right now they are not.
Maybe no one has found it. Maybe the child does not wear their glasses. Maybe the glasses are old.
Check the child's eyes first, before testing reading.
If eyes are not checked, reading and other test scores cannot be trusted.
#
Squinting, or finding the board or books hard to see.
Some children see far away well but struggle up close. This is easy to miss.
Passing a school eye check does not rule it out.
This is not dyslexia, and does not cause it.
#
Get an eye test first.
If the child has glasses, make a plan to wear them in class. Glasses in a bag do not help.
Sit near the board, with good light, until then.
Look at reading again a few weeks after the child has glasses.
Coloured overlays are not a treatment for reading.
#
An optician, or the GP or HSE eye services.
The psychologist asks about the last eye test. They do not test eyes.
#
Refractive error: when the eye does not focus light properly.
Optician: a person trained to test eyes and give glasses.
Dyslexia: a lasting difficulty with reading and spelling words.
GP: general practitioner. Your family doctor.
HSE: Health Service Executive. The Irish public health service.
""")

_add("Visual fatigue in extended reading", """
A pupil reads well at first. Then, over time, their reading gets worse.
They get slower, make more mistakes and lose their place.
The key sign is that it gets worse the longer they read.
Eye problems up close may be part of it. Only an eye expert can say.
#
Rubbing eyes, blurry vision, headaches or tiredness.
Stopping after a short time. This is not laziness.
It is not dyslexia. In dyslexia, reading is hard from the first line.
#
Get a full eye test. Mention the tiredness with close work.
Short reading times with breaks. Look far away and move around.
Bigger, clearer print. Good light. Less glare on screens.
Audio books or text read aloud for long texts.
Coloured overlays and tinted glasses are not advised for reading.
#
An optician, or the GP or HSE eye services.
Sudden double vision or bad headaches: see a doctor the same day.
The psychologist describes and refers. They do not diagnose eye problems.
#
Visual fatigue: eyes getting tired.
Dyslexia: a lasting difficulty with reading and spelling words.
Optician: a person trained to test eyes and give glasses.
GP: general practitioner. Your family doctor.
HSE: Health Service Executive. The Irish public health service.
""")

_add("Access to print", """
This is about whether a pupil can see and use the print in class.
That means worksheets, books, the board, screens and exam papers.
It is about seeing, not reading skill.
It depends on the pupil's eyes, the print itself, and the room.
#
Trouble with faint photocopies, busy pages or small print.
It matters for pupils with sight loss. It also matters for pupils with dyslexia or attention needs.
Bigger print is not always better. The right size is different for each pupil.
#
Clear plain fonts, good size and spacing, strong contrast, tidy pages.
Good seating and light. No glare. Give the pupil their own copy of board work.
Tablets with zoom, and text read aloud.
This removes a barrier. It does not teach reading.
#
The Visiting Teacher for pupils with sight loss. They advise on print size and tools.
An optician or eye doctor.
The psychologist does not choose print sizes or aids.
#
Visiting Teacher: a teacher who visits schools to support pupils with sight or hearing loss.
Contrast: how clearly the print stands out from the page.
Dyslexia: a lasting difficulty with reading and spelling words.
""")

_add("Listening in noise vs listening one-to-one", """
A pupil understands well in a quiet room with one adult.
But they struggle in a noisy class, yard or canteen.
This difference is the key sign. A quiet test room may hide the problem.
Children need speech to stand out from noise more than adults do.
#
Missing instructions in class, but doing fine one-to-one.
Tired, frustrated or pulling away in noisy places.
It is not "selective listening". The pupil may be trying hard.
A hearing test that was normal before does not rule it out. Hearing can change.
#
Get a hearing test if there has not been one recently.
Seat near the teacher, away from noise. Face the pupil when talking.
Cut noise: soft furnishings, closed doors.
Write key words and instructions on the board.
Ask the pupil to repeat back key instructions.
#
The GP, and hearing services called audiology.
The Visiting Teacher, if there is a hearing loss.
Sudden hearing loss or ear pain with discharge: see the GP the same day.
Only audiology can diagnose APD.
#
Audiology: the service that tests hearing.
APD: auditory processing disorder. Difficulty making sense of sounds. Experts disagree about it.
GP: general practitioner. Your family doctor.
Visiting Teacher: a teacher who visits schools to support pupils with sight or hearing loss.
""")

_add("Classroom acoustics and seating", """
This is about how easy it is to hear in the classroom.
Noise, echo, how far away the teacher is, and where the pupil sits all matter.
The aim is to change the room, not only help the child.
Noise can make learning harder for all children.
#
It matters most for pupils with hearing loss, language needs, attention needs, autism, or who are learning English.
Old buildings and prefabs can be very noisy.
A pupil may do worse in some rooms than others.
The front row is not always best. It may be near a noisy projector.
#
Seat the pupil near the teacher, with a clear view of their face, away from doors, heaters and projectors.
Cut noise: soft furnishings, pads on chair legs, closed doors, noisy machines off.
Teachers face the class when talking. They repeat pupils' answers. They use pictures.
Tell school leaders about noise problems.
#
The Visiting Teacher, if a pupil has hearing loss. They advise on the room and equipment.
Audiology and engineers measure sound. The psychologist does not.
#
Acoustics: how sound travels in a room.
Echo: sound bouncing back off walls.
Audiology: the service that tests hearing.
Visiting Teacher: a teacher who visits schools to support pupils with sight or hearing loss.
""")

_add("Hearing history during the years phonics was taught", """
This is a question about the past.
Did the child have poor hearing, often from glue ear, in the first years of school?
Those are the years when children learn letter sounds.
If a child could not hear sounds well then, gaps may stay, even when hearing gets better.
Research is mixed. Some children are affected, many are not. It is an idea to test.
#
Reading or spelling difficulties later, often around age 8.
Hearing may be fine now. The past still matters.
A child can have both a glue ear history and dyslexia.
#
Teach the missing letter sounds clearly, whatever the cause.
Do not wait to give reading support.
Write the hearing history in the student support file.
Good seating and less noise if hearing still goes up and down.
#
The GP can refer to audiology if hearing has not been checked lately.
Doctors and ear specialists decide about ear treatment.
If reading does not improve with teaching, look at dyslexia and other reasons.
#
Glue ear: sticky fluid behind the eardrum. It can make hearing go up and down.
Phonics: teaching the links between letters and sounds.
Dyslexia: a lasting difficulty with reading and spelling words.
Audiology: the service that tests hearing.
GP: general practitioner. Your family doctor.
""")

_add("Physical disability (non-cerebral palsy)", """
This covers physical disabilities other than cerebral palsy.
They can affect moving, using hands, energy, or getting around school.
Doctors and the CDNT diagnose and manage the condition.
The psychologist looks at what it means for learning, joining in, wellbeing and friends in this school.
#
Many pupils have typical thinking skills. Some have extra learning needs. Do not assume either way.
Low expectations are one of the biggest barriers.
PE, yard, trips and friends matter as much as getting into buildings.
#
Plan access with the school, OT and physio: seating, equipment, toileting, fire drills, trips.
Other ways to record work, like typing or a scribe. Extra time where needed. Adapted PE.
Plan for tiredness, rest breaks and catch-up after hospital stays.
Include the pupil in PE, yard games, clubs and trips.
Keep the learning goals. Change how the pupil gets to them.
#
The CDNT, OT, physio and medical team.
The SENO, for school resources.
The psychologist does not give medical advice.
#
CDNT: Children's Disability Network Team.
OT: occupational therapist. Helps with everyday tasks and equipment.
Physio: physiotherapist. Helps with movement.
PE: physical education.
SENO: special educational needs organiser.
""")

_add("Multiple disabilities", """
A child has two or more big disabilities at once.
For example, a physical disability, a learning disability and sight loss.
Together, the needs are bigger than any one alone.
This describes the child. It is not a diagnosis.
#
The key questions are: how does the child communicate? What can they see and hear?
How do they move, and are they comfortable? When are they most alert?
Each child is different. Describe this child, not the label.
Normal tests may not suit. Watching the child and other tools still give useful information.
#
One joined-up plan with every team's input.
A communication passport. It shows how the child says yes, no, more, stop, pain and "I like this".
Teach at the child's most alert times. Build in rest and position changes.
Set small goals you can see. Review each term.
#
The CDNT usually leads. It includes psychology, speech, OT, physio and social work.
Doctors, nurses and the Visiting Teacher.
Parents and the SENO decide on school placement.
#
Diagnosis: a formal name for a condition, given by a qualified person.
Communication passport: a short booklet that tells adults how a child communicates.
CDNT: Children's Disability Network Team.
OT: occupational therapist.
SENO: special educational needs organiser.
""")

_add("Chronic illness affecting school", """
This is about how a long-term health condition affects a child at school.
Examples are diabetes, asthma, epilepsy or cancer treatment.
It can affect attendance, energy, learning, friends and wellbeing.
Doctors manage the illness. The psychologist looks at the effect on school.
#
Missed teaching. Low marks may come from missed lessons, not a learning difficulty.
Symptoms that come and go. This is part of many conditions, not attention-seeking.
Some children feel worried or low. Many cope well.
#
A health care plan with parents and the medical team. Link it to the student support file.
A catch-up plan for the most important work, with a named teacher.
Private ways to deal with symptoms, like a toilet pass, water, snacks or rest.
Tell classmates only if the child and parents agree.
Keep the learning goals. Change the pace and access.
#
The medical team, for medical questions.
Home tuition if the child is away a long time.
Primary Care Psychology or CAMHS if worry or low mood is big.
#
Chronic illness: an illness that lasts a long time.
Health care plan: a written plan for how school will help with a health need.
CAMHS: Child and Adolescent Mental Health Services.
""")

_add("Fatigue and stamina needs", """
A child runs out of energy before the school day ends.
Their work gets worse through the day or week. They need rest after effort.
Tiredness can be physical or mental. It can come from sleep, pain, medicine or a health condition.
Doctors find the cause. School plans around the pattern.
#
Good in the morning, worse in the afternoon.
Worse on Fridays or after PE.
A tired child may look like they are not paying attention.
This is not laziness.
#
Do hard work when the child is freshest, usually mornings.
Rest breaks without asking in front of others. Less writing, or a scribe.
A plan for PE, trips and homework, made with the child, parents and health team.
In secondary school, less to carry. Plan exam help early.
Do not push the child to build stamina without the health team's plan.
#
The GP or medical team, if tiredness is new or getting worse. Go promptly.
An OT, for saving energy and equipment.
If tiredness comes with low mood or thoughts of self-harm, follow the safety steps.
#
Fatigue: a strong, lasting tiredness.
Stamina: how long you can keep going.
PE: physical education.
GP: general practitioner. Your family doctor.
OT: occupational therapist.
""")

_add("Medication effects on attention and learning", """
Medicine can change how a child pays attention, feels, eats or acts at school.
This can happen when a medicine starts, stops, changes, or wears off.
For example, ADHD medicine may wear off in the afternoon, or make the child less hungry at lunch.
Some seizure medicines can make a child sleepy or slower.
#
Attention or mood changes at certain times of day.
Eating little at lunch.
Medicine is not always the reason. The child may be tired or hungry, or find afternoon lessons hard.
#
Do hard work when the child is most alert. Plan lighter tasks for low times.
A snack at a later break may help. Parents can ask the doctor.
School keeps a simple record of what it sees. Parents can share it with the doctor.
Test reports say when the test was done and when medicine was taken.
#
The doctor who prescribed the medicine. Parents talk to them.
A pharmacist can answer factual questions.
The psychologist never gives advice on starting, stopping or changing medicine.
Big mood changes or thoughts of self-harm after a change: parents contact the doctor urgently.
#
ADHD: attention deficit hyperactivity disorder.
Prescribe: when a doctor decides on a medicine for someone.
Pharmacist: a person trained in medicines who works in a chemist.
""")

_add("Missed curriculum from hospital admissions", """
A child has gaps in learning because of time in hospital.
The gaps come from missed teaching, not a learning difficulty.
Some subjects build step by step, like maths, Irish and early reading. These suffer most.
Hospital school work may not match the class work.
#
Low test scores after long absence. These show missed teaching, not ability to learn.
The child may also be tired or worried.
Missed friends, routines and feeling part of the class.
#
Find the few key skills needed for class work now. Teach those first.
Short, frequent catch-up sessions. Check progress every half term.
Teach key words for the current topic ahead, so the child can join in now.
Do not try to catch up on everything. It is too much.
Do not say the child has dyslexia until the gaps are taught and progress checked.
#
A named teacher leads the catch-up.
The hospital teacher and home tuition, with parents' agreement.
The medical team, if the illness or treatment may affect thinking.
#
Curriculum: what is taught in school.
Home tuition: teaching at home when a child cannot go to school.
Dyslexia: a lasting difficulty with reading and spelling words.
""")

_add("Re-entry to school after illness", """
A planned return to school after a big illness, injury, operation or hospital stay.
Coming back is a big change in itself.
The child may look different, get tired faster, think more slowly or feel worried.
Friendships and routines in class may have moved on.
#
A full day on the first day often does not work.
Some problems show up later, especially after a brain injury.
Worry about coming back after a scary illness is understandable. It is not school refusal.
#
A written plan: a step-by-step timetable, rest, a key adult, what classmates are told, and catch-up work.
Agree the plan with the child, parents and medical team. Share it with all teachers.
A safe place, an exit card, and a seat near the door or a friend.
Tell the class a short, honest explanation, only if the child and parents agree.
Review again at the start of the next school year.
#
The medical team and home tuition.
Primary Care Psychology or CAMHS for worry, low mood or nightmares.
The CDNT or a brain injury specialist after a brain injury.
#
Re-entry: coming back.
Exit card: a card a pupil can show to leave class for a short break.
CAMHS: Child and Adolescent Mental Health Services.
CDNT: Children's Disability Network Team.
""")

_add("Parent-infant mental health / 0–3 attachment work", """
Infant mental health is how a baby or toddler learns to feel, calm, bond and explore.
It grows through the relationship with the people who care for them.
The focus is the relationship, not just the baby.
Parent-infant work helps with the parent's mental health, their past, and reading the baby's signals.
#
Most problems come from stress, illness, low mood or a baby who is hard to settle. Not from lack of love.
It is not a judgement that the parent is "bad".
Insecure bonds are common. They are not the same as the rare condition attachment disorder.
School psychologists rarely do this work. They meet older children who had it.
#
Programmes that support the relationship, like Circle of Security, through services that offer them.
In preschool: one steady key person, set routines, and comfort before correction.
For older children: a key adult and steady routines in school.
Describe behaviour and relationships. Do not write "attachment disorder" in reports.
#
The parent's GP, the public health nurse, and Primary Care Psychology.
The CDNT if development is also a worry.
Tusla family support if the family needs help.
#
Infant: a baby.
Attachment: the bond a child forms with the people who care for them.
GP: general practitioner. Your family doctor.
CDNT: Children's Disability Network Team.
Tusla: the Child and Family Agency.
""")

_add("Early Intervention Team caseload (0–6, pre-diagnostic)", """
A young child, up to age 6, is known to the health service because of worries about development.
They do not have a diagnosis yet.
These teams are now called Children's Disability Network Teams. Many people still use the old name.
Children can get help without a diagnosis. But waiting lists are often long.
#
Many of these children make good progress.
Some get a diagnosis later. Some do not.
It does not predict what will happen.
#
The CDNT usually leads. The school psychologist mostly gives advice, not tests.
Do not repeat tests another service has done.
Plan the move to primary school with a meeting, with parents' agreement.
Plan from the child's needs: picture timetables, a key adult, communication help.
Do not promise a diagnosis, a date or extra support.
#
The CDNT is the lead service.
The SENO, for school resources.
If a child loses skills they had, see the GP or a paediatrician promptly.
#
Diagnosis: a formal name for a condition, given by a qualified person.
CDNT: Children's Disability Network Team. The health team for children with disabilities.
SENO: special educational needs organiser.
Paediatrician: a children's doctor.
GP: general practitioner. Your family doctor.
""")

_add("Delayed developmental milestones", """
A young child has not reached some skills at the usual age.
This might be walking, using hands, talking, getting on with others, or looking after themselves.
It describes timing. It does not explain why.
There are many possible reasons, from normal differences to hearing loss or health conditions.
#
Delay may be in one area, like late talking, or in several areas.
Early delays do not tell us for sure what will happen later.
Losing skills the child had is different from delay. It needs a doctor quickly.
#
Get help early. Do not just wait, if the delay is big or in several areas.
In preschool, set goals for the child's current level. Build them into play and routines.
AIM support in preschool does not need a diagnosis.
Plan the move to primary school early.
#
The GP or public health nurse can refer to the CDNT, therapists and children's doctors.
If you see signs of neglect, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own.
Doctors and the CDNT diagnose. The psychologist describes.
#
Milestones: skills most children learn by a certain age.
AIM: Access and Inclusion Model. Support to help children with disabilities take part in preschool.
GP: general practitioner. Your family doctor.
CDNT: Children's Disability Network Team.
Tusla: the Child and Family Agency.
Neglect: when a child's basic needs are not met.
""")

_add("AIM level and preschool support already in place", """
AIM is a scheme that helps children with disabilities take part in the free preschool year.
It has seven levels. The first three help every child. Levels 4 to 7 are extra help for one child.
Extra help can be expert advice, equipment, therapy, or an extra adult in the room.
A child does not need a diagnosis to get AIM.
#
AIM help shows what the child needed and what worked.
AIM ends when the child leaves preschool. The school must plan what comes next.
An AIM level does not mean the child will get an SNA in school. They are separate schemes.
#
A planning meeting before September, with parents' agreement.
Share what worked in preschool, like a picture timetable or a key person.
Use what worked from day one in school. Review at half term.
Parents contact the SENO early about SNA support, special classes or transport.
#
The preschool applies for AIM with parents.
The SENO, for school supports.
Any child protection worry: tell Tusla (the child and family agency) quickly. Telling the safeguarding person is not enough on its own.
#
AIM: Access and Inclusion Model.
Diagnosis: a formal name for a condition, given by a qualified person.
SNA: special needs assistant.
SENO: special educational needs organiser.
Tusla: the Child and Family Agency.
""")

_add("Transition from preschool to primary", """
This is about a child moving from preschool or home into junior infants.
There is a bigger group, new adults, longer days, new routines and more formal learning.
Most children manage well. Some need a plan.
Good moves depend on sharing information and building relationships between settings and families.
#
Children who may need more help: those with disabilities, worry, new to English, in care, or with no preschool.
It is not a test the child passes or fails. The school must be ready for the child too.
Some children cope in September but struggle later.
#
A meeting before the child starts, if needed. Extra visits and a photo book of the school.
A steady key adult, a picture timetable, clear routines and a quiet space.
Teach routines like lining up, toilet and lunch.
A shorter day only for the first weeks, with a plan to build up.
Waiting a year to start school is a decision to make carefully. It is not a routine answer.
#
Parents, the preschool and the school, often using Mo Scéal forms.
The CDNT, the SENO, or the school psychologist if there are bigger worries.
Any child protection worry: tell Tusla (the child and family agency) quickly. Telling the safeguarding person is not enough on its own.
#
Transition: a move from one place or stage to another.
Mo Scéal: forms that pass information from preschool to primary school.
CDNT: Children's Disability Network Team.
SENO: special educational needs organiser.
Tusla: the Child and Family Agency.
""")

_add("Care-experienced children (foster, kinship, residential, aftercare)", """
A child who is, or was, in the care of the State.
They may live with foster carers, relatives, or in a care home. Older young people may get aftercare.
Tusla is responsible for children in care.
Being in care is not a diagnosis or a problem in itself.
#
Many care-experienced children do well. Do not assume problems.
Many have lived through harm, loss and many moves.
Changes of school and home explain much of the gap in results.
School can be one of the most important safe places in their life.
#
A named key adult with regular contact. A safe place.
A plan for hard times, like before and after family visits.
Steady routines and warning before changes. Take care with topics like family trees.
A plan for learning gaps. Keep the child in the same school where possible.
Share only the history that is needed and agreed.
#
The social worker, with consent, so school is part of care planning.
CAMHS or Tusla therapy services for bigger needs.
An aftercare worker for older young people.
#
Care-experienced: has been in the care of the State.
Foster care: living with a family who is not your birth family.
Aftercare: support after leaving care, into the early twenties for some.
Tusla: the Child and Family Agency.
CAMHS: Child and Adolescent Mental Health Services.
""")

_add("Child protection and welfare concerns", """
This is when there is a reasonable worry that a child has been harmed, is being harmed, or may be harmed.
Harm can be neglect, emotional abuse, physical abuse or sexual abuse.
Psychologists are mandated persons. By law, they must report worries above a set level of harm.
This is not something you assess. It is a set of steps you follow.
#
You must tell Tusla (the child and family agency) quickly.
Telling the school's safeguarding person is not enough on its own. You can make a joint report with them.
You cannot promise to keep it secret.
#
Report to Tusla quickly. Tell the school's safeguarding person. Write down what you did and when.
If a child is in danger right now, call the Gardaí on 999 or 112.
Talk to your supervisor after you report, not instead of reporting.
With Tusla's advice, school gives the child a trusted adult and a steady routine.
Do not question the child to find out what happened.
#
Tusla and the Gardaí find out what happened. The psychologist does not.
Your supervisor helps you after you act.
#
Mandated person: someone the law says must report child protection worries.
Neglect: when a child's basic needs are not met.
Tusla: the Child and Family Agency.
Gardaí: the Irish police.
""")

_add("Domestic violence exposure", """
A child lives, or lived, in a home where one adult abuses another.
Abuse can be physical, sexual, emotional, about money, or controlling behaviour.
Children do not only see it. They hear it, live with it, and may be pulled into it.
It is always a child protection matter to think about.
#
Worry, being always on guard, and trouble concentrating.
Effects on feelings, behaviour and learning. These differ with age and support.
Stress can go on after the abuser leaves.
The parent who is abused is not to blame.
#
If you are worried, tell Tusla (the child and family agency) quickly. Tell the school's safeguarding person too.
A trusted adult, a steady routine and a quiet space in school.
Avoid sudden loud noises or shouting.
Check court orders: who can collect the child, and what can be shared.
#
Tusla.
Domestic violence services like Women's Aid and Safe Ireland.
Primary Care Psychology or CAMHS for big trauma needs.
If anyone is in danger right now, call the Gardaí.
#
Domestic violence: abuse between adults in a home.
Coercive control: a pattern of controlling and frightening someone.
Tusla: the Child and Family Agency.
CAMHS: Child and Adolescent Mental Health Services.
Gardaí: the Irish police.
""")

_add("Parenting capacity concerns", """
This is a worry about whether a parent can meet a child's needs.
Needs include safety, care, warmth, play, guidance and a steady home.
It can happen with parent mental illness, drug or alcohol use, a disability or a lot of stress.
Tusla social workers assess this. The psychologist does not.
#
It is not a judgement about a parent's love. Many parents love their children but still struggle.
Most families are helped with family support, not child protection.
#
Meitheal, a Tusla family support plan that families choose to join.
Family resource centres and the school's home link teacher.
Practical help in school, like a breakfast club or homework club, and a trusted adult.
Parenting courses, if the family wants them.
In reports, describe the child's needs. Do not judge the parent.
#
Tusla and family support services.
The GP, for the parent's health.
If you see signs of neglect or abuse, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own.
#
Parenting capacity: how able a parent is to meet a child's needs.
Meitheal: a Tusla way of bringing family support together.
Tusla: the Child and Family Agency.
GP: general practitioner. Your family doctor.
""")

_add("Family functioning difficulties", """
This is about patterns in a family that affect a child's wellbeing or school life.
It may be about how the family talks, argues, shares roles or solves problems.
Examples: parents fighting, separation, a death, or someone in the family who is ill or has an addiction.
The child's needs are seen in the context of family relationships.
#
Every family has strengths and stresses. Do not call a family "dysfunctional".
It works both ways. A child's needs can also cause family stress.
Hard times, like handovers between parents.
#
A trusted adult and steady routines in school.
Be flexible at hard times.
Send information to both parents if both are guardians, unless a court order says not to.
Parenting courses, like Parents Plus, if offered locally.
Never take sides in a parents' dispute.
#
Family resource centres, Primary Care, Meitheal and family therapy services.
Rainbows, for loss and separation. CAMHS for serious mental health needs.
If a child tells you about abuse or neglect, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own.
If a child talks about self-harm, act the same day.
#
Guardian: a person with legal rights and duties for a child.
Meitheal: a Tusla way of bringing family support together.
CAMHS: Child and Adolescent Mental Health Services.
Tusla: the Child and Family Agency.
""")

_add("Housing and economic problems", """
A child's school life is affected by poverty, debt, hunger, overcrowding or poor housing.
It includes families who are homeless or in emergency places like hotels or family hubs.
This is about the child's situation. It is not a disorder.
#
Long journeys to school. Nowhere to do homework. Poor sleep and hunger.
Missed school, shame and lost friendships.
Low marks may come from these hard times, not a learning difficulty.
It is not a parenting failure. Housing and money problems are often the main cause.
#
School meals, breakfast club, homework club, and help with uniform and books.
Keep this private, so the child is not singled out.
Be flexible with homework. Do not punish lateness caused by long travel.
Advice must work where the child lives now. Do not suggest a quiet study space if there is none.
#
The school's home link teacher and the School Completion Programme.
Citizens Information, MABS, and charities like Focus Ireland, Threshold or St Vincent de Paul.
If you see signs of neglect, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own.
#
Emergency accommodation: short-term places to stay for homeless families.
MABS: Money Advice and Budgeting Service.
Neglect: when a child's basic needs are not met.
Tusla: the Child and Family Agency.
""")

_add("Social exclusion, discrimination, acculturation difficulty", """
A child's wellbeing or school life is affected by being left out, treated unfairly, or finding it hard to adapt between cultures.
This can affect Traveller and Roma children, migrant children, refugees, LGBTQ+ young people and children of minority faiths.
Irish law bans discrimination in education.
These are about the child's situation. They are not disorders.
#
A child learning English may seem to struggle. This is not about their ability to learn.
Tests made for other groups may be unfair to the child.
Exclusion is a problem for the whole school to fix, not only the child.
#
Say names correctly. Show the child's culture and language in class. Buddy systems.
Support with English. Value the home language. Teach school routines clearly.
Anti-bullying rules that name racism, homophobia and anti-Traveller behaviour.
Staff training where it is needed.
#
Primary Care Psychology or CAMHS for serious upset or trauma.
Services for refugees. Traveller and Roma groups for family support.
Racist bullying or threats: the school must act. Follow child protection steps if there is harm.
#
Discrimination: treating someone unfairly because of who they are.
Acculturation: adapting to a new culture.
LGBTQ+: lesbian, gay, bisexual, transgender, questioning, and others.
CAMHS: Child and Adolescent Mental Health Services.
""")

_add("Knowing which service does what, and the referral route", """
This is a skill for the psychologist, not a need in the child.
It means knowing which Irish service helps with which need, and how to refer.
For example: NEPS for school psychology, CDNTs for complex disability needs, Primary Care for less complex needs.
CAMHS for serious mental health needs. Tusla for child protection and family support. NCSE for SNA support and school places.
#
Referring to everyone can confuse families. Referrals may be turned down.
Services and their rules change. Check before you advise.
Knowing each service also stops tests being done twice.
#
Keep an up-to-date list of local services and how to refer.
In reports, say which service, why, and who makes the referral.
Be honest with families about waiting times.
Check that referrals arrived.
Do not promise that a service will accept a child.
#
Your supervisor helps you keep the list up to date.
If a child at risk falls between services, tell your supervisor. Do not leave the child without a plan.
Child protection worries always go to Tusla.
#
Referral: asking another service to help.
NEPS: National Educational Psychological Service.
CDNT: Children's Disability Network Team. CDNTs means more than one.
CAMHS: Child and Adolescent Mental Health Services.
NCSE: National Council for Special Education.
SNA: special needs assistant.
Tusla: the Child and Family Agency.
""")

_add("Multi-disciplinary meetings and your role in them", """
This is a skill for the psychologist.
It means getting ready for, taking part in, and following up on meetings with other professionals and the family.
The psychologist shares a view on learning, behaviour and wellbeing, and practical ideas for school.
Parents and the child are part of the team. Their views should shape the meeting.
#
Working together helps everyone understand the child.
It can also be hard: unclear roles, power differences and sharing information.
Know who leads the meeting. It is not always the psychologist.
#
Before: tell parents big findings in private first. Check consent to share information.
During: use plain words. Ask the child's and parents' views. Agree clear actions, with names and dates.
After: check the notes are right. Do what you agreed.
Do not agree to things you cannot do.
#
The meeting chair, if parents are left out or overwhelmed.
Child protection worries raised in a meeting: tell Tusla (the child and family agency) quickly. Do not wait for the notes.
#
Multi-disciplinary: with people from different professions.
Consent: agreeing to something after it is explained.
Tusla: the Child and Family Agency.
""")

_add("Professional and service boundaries", """
This is about the psychologist's role, not the child.
It means knowing what is and is not yours to do.
The school psychologist assesses, plans, advises and refers.
They do not diagnose medical or mental health conditions or give advice on medicine.
Some decisions belong to the school, like discipline or staffing.
#
A case may raise a question that belongs to another service. The risk is answering it anyway.
Boundaries do not mean "refer everything". You can still describe what you see and help the school now.
Boundaries differ between services.
#
Write in your role. Say "a referral is advised", not "he has ADHD".
Pair every referral with something the school can do now.
Name who decides, like the NCSE for SNA support or the SEC for exam help.
Never promise support that another body decides on.
#
Your supervisor helps you check your role.
Child protection is the one boundary that never stops you acting. Tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own. Then talk to your supervisor.
#
Diagnose: to say formally what condition someone has.
ADHD: attention deficit hyperactivity disorder.
NCSE: National Council for Special Education.
SNA: special needs assistant.
SEC: State Examinations Commission.
Tusla: the Child and Family Agency.
""")

_add("Classroom environment", """
This is about the room itself, and how it helps or blocks learning.
It includes noise, light, heat, busy walls, seating, space and where things are kept.
It also includes routines, like timetables and signals for changes.
Research links room design and busy walls to how much children learn.
#
It is not a judgement on the teacher. Many things, like an old building, are outside their control.
Where the child sits and how changes are signalled often matter more than the lights.
If a child still struggles in a well-set-up room, look at the child's own needs too.
A child who covers their ears or runs from the room needs a closer look.
#
Seat the child near the teacher, away from doors and noise, with a clear view. Try it, then review.
Keep walls near the teaching area calm and tidy.
A picture timetable and one signal for changes help the whole class.
Agree noise levels. Have a quiet work spot as a normal routine, not a punishment.
Do not sit a child apart forever as a behaviour plan.
#
The class teacher and school.
The Visiting Teacher and hearing or eye services, for pupils with sight or hearing loss. The psychologist does not choose equipment.
#
Environment: the space and conditions around you.
Visiting Teacher: a teacher who visits schools to support pupils with sight or hearing loss.
""")

_add("Teaching match", """
This is about how well the lesson fits where the child is now.
Work may be too hard, too easy, too fast, or in a form the child cannot use.
Children stay on task and understand more when work is at the right level.
The stage of learning matters too. New skills need showing. Slow but correct skills need practice.
#
Off-task behaviour when work is too hard.
Boredom and behaviour problems when work is too easy.
Problems in one subject only. Look at the fit in that class first.
It is not a judgement on the teacher.
#
Set work alone that the child can mostly get right with effort. Keep harder work for when there is help.
Show new skills and give feedback. Give short, frequent practice for slow skills.
Same topic, easier way in, like an easier text, audio or a reading partner.
Check if things improve after 6 to 8 weeks.
Check the work level before blaming attention or motivation.
#
The class teacher, with support from the school.
The school decides teaching methods and groups. The psychologist describes the fit.
If work is too hard in every subject, check for a hidden learning, language or sensory need.
#
Differentiate: change work so different pupils can do it.
Motivation: the wish to do something.
""")

_add("Curriculum demands", """
This is about what the school programme asks of the child at this stage.
It includes how much reading and writing, how hard the language is, the pace, and the type of tests.
Demands jump at known times, like middle primary and the start of secondary school.
The way work is presented can make it harder than it needs to be.
#
A child who coped for years may suddenly struggle. The child may not have changed. The demands have.
A sudden drop at these times may point to a hidden language or reading need.
#
Keep the learning goal. Change the way in: audio, less copying, word lists, charts.
Teach subject words before a new topic.
Clear examples, one task per page, and numbered steps.
For some pupils with a general learning disability, the school may consider a different programme. The school decides this with the family.
Do not decide a programme from a single test score.
#
The school and the family decide programmes and subject levels.
The psychologist describes the child and the demands.
Check that a reduced programme still fits, from time to time.
#
Curriculum: what is taught in school.
General learning disability: finding most learning harder than other children the same age.
""")

_add("Attendance and transitions", """
This describes how often a child is in school, and how they manage changes during the day.
It includes days missed, lateness, part days and shorter timetables.
Changes include arriving, moving between lessons, after break and after holidays.
By law, the principal tells Tusla when a pupil misses 20 days or more in a school year.
#
When: which days and times, like after weekends.
Why: illness, family, worry, being sent home, bullying or learning needs.
Lateness and missing the same lesson each week count too.
A shorter day on its own does not fix the problem.
#
A warm, set routine for arriving. A named adult at the door.
Follow up on the first day of absence.
A plan with a slow return if needed, a key adult and a safe place. Review with the family every two weeks.
A picture timetable and warning before changes.
A shorter day only with parents' agreement, an end date and a plan to go back full time.
Do not blame parents in writing.
#
Tusla's school attendance service, when absence goes on.
The GP, Primary Care or CAMHS for mental health needs.
If absence is linked to signs of abuse, neglect or self-harm, act the same day. Tell Tusla (the child and family agency) quickly.
#
Attendance: being in school.
Tusla: the Child and Family Agency.
GP: general practitioner. Your family doctor.
CAMHS: Child and Adolescent Mental Health Services.
""")

_add("Transition planning (early years to primary, primary to post-primary, school leaver)", """
This is planning for a child to move from one setting to another.
The main moves are: preschool to primary, primary to secondary, and leaving school.
Information, relationships and supports need to move with the child.
Supports do not move on their own. They must be planned, and some must be applied for again.
#
Pupils with extra needs are more likely to find moves hard.
Parents' worry and the new school's readiness matter too.
A move is a process, not one visit in June.
#
Start early. For complex needs, start at least a year before.
Fill in the forms that pass on information, like Mo Scéal or the Education Passport. Say what works.
Visits, photos of key places and people, the timetable ahead, a key adult and a buddy.
Apply again for SNA support or a special class in time. AIM does not continue into primary school.
Do not promise a place or support that someone else decides.
#
The SENO and NCSE, for resources.
The school and family, for young people near 18 with no plan for adult services.
If the child refuses the new school or struggles, review early.
#
Transition: a move from one place or stage to another.
SNA: special needs assistant.
AIM: Access and Inclusion Model. Preschool support for children with disabilities.
SENO: special educational needs organiser.
NCSE: National Council for Special Education.
""")

_add("Assistive technology", """
Assistive technology means tools that help a pupil learn and take part.
They can be simple, like reading rulers or pencil grips.
They can be everyday tech, like dictation, read-aloud or keyboards.
Or they can be special equipment, like switches or braille devices.
Choose the tool last. First think about the student, the places and the tasks.
#
A laptop in a cupboard does not help. Training and daily use matter.
Tools are often dropped if the pupil did not help choose them.
Tools can help with reading, writing, getting organised, attention and moving.
#
Match each tool to a task, like read-aloud for a history book.
Use it as a normal part of class, across subjects. Then it can be used in exams too.
Plan who trains the pupil and staff, and who looks after the device.
Plan for the tool to move with the pupil to a new class or school.
#
OT, SLT and the Visiting Teacher advise on special devices.
The school applies through the SENO for special equipment.
The psychologist describes the task. They do not choose equipment.
#
Assistive technology: tools that help a person do things they find hard.
OT: occupational therapist.
SLT: speech and language therapist.
SENO: special educational needs organiser.
Visiting Teacher: a teacher who visits schools to support pupils with sight or hearing loss.
""")

_add("Reasonable Accommodations in State Examinations (RACE)", """
RACE is a scheme for the Junior and Leaving Cert exams.
It gives supports that remove barriers, without changing what is tested.
The school applies. The SEC decides.
A psychologist's report is not needed. A report does not mean a pupil will get support.
#
Supports include help with reading, a computer or recorder for writing, and a spelling waiver in language subjects.
There are also supports for hearing, sight and physical needs.
Supports should match how the pupil normally works in school.
Trauma and hard life events are outside RACE. Other exam arrangements may apply.
#
Describe the pupil's need, not what they should get.
Train pupils early in typing or recording, so it is their normal way of working.
Try supports in school exams first.
Tell the school early about any tests you did, so dates are not missed.
Never promise a support. Never quote the rules from memory.
#
The school, which applies and does the testing.
The SEC, which decides.
Families can appeal a decision. Closing dates are strict.
#
RACE: Reasonable Accommodations at the Certificate Examinations.
SEC: State Examinations Commission. The body that runs the state exams.
Accommodation: a change that makes a test fair for someone.
Appeal: asking for a decision to be looked at again.
""")

_add("SNA and resource teaching allocation", """
This is about how extra adults are given to schools and used for a child.
Schools get special education teaching time based on the school's overall needs, not on single reports.
A child does not need a report to get this teaching support.
The NCSE gives SNA support to schools. The SNA helps with care needs. An SNA is not a teacher.
#
How support is used matters as much as how much there is.
An adult always by the child's side can mean less time with classmates and the teacher.
The schemes are being reviewed. Check before you advise.
#
Describe needs clearly, like "needs help with toileting twice a day". Do not say "needs an SNA".
The child with the most need gets at least as much teacher time as others.
Plan to reduce SNA help over time, with review dates.
Give special teaching time clear goals and a way to check progress.
#
The NCSE decides on SNA support.
The school decides how teaching time is used.
The psychologist describes needs. They do not give out SNA support or teaching hours.
#
SNA: special needs assistant.
NCSE: National Council for Special Education.
Allocation: how much support a school is given.
""")

_add("Home learning environment", """
This is about learning at home: reading together, talking, playing with letters and numbers, and time for homework.
What parents do with children matters more than their job or schooling.
Help with learning at home makes a real difference.
Every home has strengths.
#
Many families with little money give rich learning at home.
A home language other than English is a strength.
Reports should describe home life fairly, with the parent's agreement. No judging words.
#
Add small things to what already happens, like reading at bedtime or talking at dinner.
Parents read and talk in the language they know best.
School can help: homework club, lending books or devices, short texts home.
Only suggest things the family can really do.
#
The school's home link teacher, local libraries and parent programmes.
Young carer supports if a young person does a lot of caring at home.
If you see signs of neglect, tell Tusla (the child and family agency) quickly.
#
Home learning environment: the learning that happens at home.
Neglect: when a child's basic needs are not met.
Tusla: the Child and Family Agency.
""")

_add("Community context", """
This is about the area and community around the child and school.
It includes money, housing, travel, and the help that is close by.
It also includes strengths, like family, sports clubs, youth services and cultural groups.
The community shapes what happens at home and in school.
#
Some schools get extra help because times are hard in their area.
Hard times in an area do not decide a child's future.
Describe this family's barriers and strengths. Do not stereotype a community.
#
Link families to community supports, like family resource centres and youth services.
Meitheal can join up help from different services, if the family agrees.
Find one local activity, like a club or library, that could help the child belong.
If many children face the same local problem, the psychologist raises it with their service.
Check a service exists locally before suggesting it.
#
The school's home link teacher and the School Completion Programme.
Family resource centres and youth services.
Risk from others in the community: follow safety steps. Involve Tusla and the Gardaí as needed.
#
Community: the people and places around you.
Meitheal: a Tusla way of bringing family support together.
Tusla: the Child and Family Agency.
Gardaí: the Irish police.
""")

_add("Continuum of Support level and whether it was actually implemented", """
The Continuum of Support has three levels: Classroom Support, School Support and School Support Plus.
This asks two things. What level is the child at? And did the planned support really happen, for long enough?
Research shows that support works better when it is carried out carefully.
"We tried that" may mean it was never done as planned.
#
A plan with vague goals, no review date and no progress record is only an intention.
Poor progress after good support tells us more than poor progress with no real support.
It is not a criticism of teachers. Time, staff and training all matter.
#
Say the level in the report, and whether the support happened.
If not, write a clear plan: what, how often, how long, who, how to measure, and when to review.
Help the school set goals and review them.
Move up a level only when support at this level was done and reviewed.
#
The principal and the school's special needs team carry out the plan.
The psychologist advises and helps.
If the same gap shows up in many cases, talk with the principal.
#
Continuum of Support: the three levels of support used in Irish schools.
Implemented: carried out.
""")

_add("Whole-school policy and practice", """
This is about the school's rules, plans and culture, and how they work in real life.
It includes rules on special needs, behaviour, bullying, wellbeing, attendance and child protection.
The psychologist notices patterns across many cases and helps the school review its policies.
A written policy on its own rarely changes classrooms. Training, coaching and leadership are needed.
#
Several children with the same problem can point to a whole-school issue. For example, many lunchtime problems may point to yard supervision.
It is not judging a school from one case.
#
Start with the school's own priorities. Agree a focus with the principal.
Link to national guides, like the Wellbeing Framework and Bí Cineálta.
Pair every policy change with training and follow-up.
Talk with groups of staff when the problem is school-wide.
#
The Board of Management owns the policies. The psychologist advises.
If a practice puts children at risk, tell the principal and your supervisor. Follow child protection steps where needed.
Check any suspension or shorter day has a plan to return.
#
Policy: a school's written rules and plans.
Bí Cineálta: the Irish school rules on bullying.
Board of Management: the group that runs the school.
""")

_add("Staff training need identified through casework", """
Working with individual children can show that staff need more training in one area.
Examples are autism, worry, behaviour or reading support.
Training that helps with this can help many children.
Talks alone rarely change teaching. Practice, feedback and coaching in class work much better.
#
The same advice failing in several cases.
It is not a criticism of staff. It is a gap in the system.
Gaps can come from new pupil needs, staff changes or no access to training.
#
Name the need clearly, like "training in structured teaching for autistic pupils".
Match it to the right training provider.
Build in follow-up, like coaching or watching each other teach.
Agree priorities with the principal.
Do not name staff in written feedback.
#
Providers like NEPS, Oide, the NCSE Support Service and Middletown Centre for Autism.
The psychologist only trains in areas they know well.
If a training gap leads to harmful practice, tell the principal and your supervisor quickly.
#
Casework: working with individual children.
NEPS: National Educational Psychological Service.
Oide: the Irish support service for teachers' learning.
NCSE: National Council for Special Education.
""")
