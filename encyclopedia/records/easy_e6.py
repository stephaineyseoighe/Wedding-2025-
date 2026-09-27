# EASY READ versions of micro-skills 110-219 (src/entries.json['micro'][110:220]).
# Validate with: python3 check_easy.py records/easy_e6.py

EASY = {}


def _e(name, learn, why, how, words):
    parts = ["WHAT YOU LEARN TO DO"] + ["• " + x for x in learn]
    parts += ["WHY IT MATTERS"] + ["• " + x for x in why]
    parts += ["HOW YOU KNOW YOU CAN DO IT"] + ["• " + x for x in how]
    parts += ["WORDS TO KNOW"] + ["• " + x for x in words]
    EASY["micro::" + name] = "\n".join(parts)


_e("Consider family, culture and community influence",
   ["You find out about the child's home language, culture and family.",
    "You ask how the family sees the problem."],
   ["Home language changes what test scores mean.",
    "A child can chat well in English but still find school English hard."],
   ["Your report says clearly how language and culture affect the scores.",
    "It is not just a note in the background."],
   ["Formulation: your written idea of why the child is having a hard time.",
    "Interpreter: a person who puts words from one language into another."])

_e("Consider the school environment as a contributor",
   ["You look at the school as part of the reason for a problem.",
    "You look at class size, teacher changes, moves and the help really given."],
   ["The school is not just a backdrop. It can add to the difficulty.",
    "The help on paper may not be happening in real life.",
    "If you miss this, you may suggest what the school already does."],
   ["You have thought about class size, teacher changes and moves.",
    "At least one of your ideas for help is about the school setting."],
   ["Recommendation: an idea you write down for what should help."])

_e("Show the levels interacting rather than listed",
   ["You show how the child, family and school affect each other.",
    "You say which of these links makes the difficulty bigger."],
   ["A list does not explain anything.",
    "Showing the links tells the reader where to help."],
   ["Your formulation joins the parts up.",
    "Each part is linked to at least one other part.",
    "At least one idea for help aims at one of these links."],
   ["Formulation: your written idea of why the child is having a hard time."])

_e("Know the programmes available locally",
   ["You find out which reading programmes each school already runs.",
    "You find out who is trained to use them."],
   ["An idea the school cannot carry out is wasted.",
    "You have to ask each school. Do not guess.",
    "Do not name a programme from memory."],
   ["You can name what each of your schools has.",
    "You use that list every time you write ideas for help."],
   ["Programme: a planned set of lessons to help a skill, like reading."])

_e("Match the programme to the phonological profile",
   ["You work out which part of reading is hard for the child.",
    "You then pick help that works on that part."],
   ["Reading has different parts, like sounds, speed and meaning.",
    "A child can find one part hard and the others fine.",
    "The wrong help wastes a term. The school may think help does not work."],
   ["Your idea for help follows from what the assessment found.",
    "You name the hard part before you name a programme."],
   ["Phonological: to do with the sounds in words.",
    "Assessment: finding out about a child's needs, for example with tests."])

_e("Specify how often, how long, over what period",
   ["You say how often help happens and for how long.",
    "You say how many weeks it runs, and when it starts and is checked."],
   ["'Reading support' on its own is a wish, not a plan.",
    "Schools often give too little help, and then think it did not work."],
   ["Your plan says how many sessions a week and how many minutes.",
    "It says the group size, the number of weeks and the review date.",
    "The school agrees it can do this."],
   ["Session: one time the help happens, like one lesson.",
    "Review: a meeting to check how things are going."])

_e("Identify who delivers and whether they are trained",
   ["You say who in the school gives the help.",
    "You check that person is trained, or say how they will be trained."],
   ["'In school' means nobody in particular.",
    "Staff may each think someone else is doing it.",
    "Special needs assistants are mainly for care needs, not teaching. Check the current rules."],
   ["Each idea for help names the job of the person who gives it.",
    "It says who they can ask for advice after you leave."],
   ["Role: a person's job, like class teacher.",
    "Special needs assistant: a staff member who helps with a child's care needs."])

_e("Take a baseline before it starts",
   ["You measure the child's skill before help starts.",
    "You write the date and how you did it, so someone else could repeat it."],
   ["Without a starting point, you cannot tell if help worked.",
    "The yearly school test is too slow to show change in one term."],
   ["There is a dated measure from before the first session.",
    "It checks the skill the help is for."],
   ["Baseline: a measure taken before help starts, to compare with later."])

_e("Set a review point and a measure",
   ["You set a date to check if help worked.",
    "You say what to measure and who does it."],
   ["You cannot change a plan if you did not measure it.",
    "Trainees leave. Most reviews happen after they go.",
    "A review only you can run will not happen."],
   ["Someone other than you could do the review.",
    "The plan says what the result will help decide."],
   ["Review: a meeting to check how things are going."])

_e("Know concrete–pictorial–abstract sequencing",
   ["You learn a way to teach maths in three steps.",
    "First real objects, then pictures, then numbers and signs."],
   ["It is one way of teaching maths that has good evidence.",
    "A common mistake is moving to numbers too early.",
    "Another is using objects just for fun, not to show how maths works."],
   ["You can explain it to a teacher in about two minutes.",
    "You use no jargon and give one example linked to the child.",
    "You say what the teacher should see before moving on."],
   ["Concrete: real objects you can touch, like cubes.",
    "Abstract: numbers and signs on paper.",
    "Jargon: special words that most people do not know."])

_e("Distinguish fact retrieval from conceptual difficulty",
   ["You work out why a child finds maths hard.",
    "Is it remembering number facts quickly, or understanding how numbers work? Or both?"],
   ["These two problems need different help.",
    "Drilling facts will not help a child who does not understand numbers yet."],
   ["Your report says which problem it is and shows your evidence.",
    "Your idea for help aims at the right one."],
   ["Fact retrieval: remembering number facts quickly, like 3 + 4 = 7.",
    "Conceptual: to do with understanding an idea."])

_e("Recommend at the right point on the Continuum",
   ["You say which level of school support the child needs.",
    "You say why that level and not the one below."],
   ["Irish schools give help at three levels.",
    "If you do not name a level, the school has to guess.",
    "Going to the top level too quickly can take help from another child."],
   ["Every maths idea for help names the level.",
    "It also says what the class teacher keeps doing."],
   ["Continuum of Support: the three levels of help in Irish schools. They are Classroom Support, School Support and School Support Plus."])

_e("Specify what success would look like",
   ["You say what the child will be able to do if help works.",
    "You say how and when it is checked, and by whom."],
   ["'Better at numbers' cannot be checked.",
    "Without a clear goal, the review is just opinion.",
    "The child may stay in help that is not working."],
   ["A teacher would know if the help worked.",
    "The goal is about what the child does, not the help given."],
   ["Success criterion: a clear sign that shows the help worked."])

_e("Know the evidence base for what you recommend",
   ["You check the research behind any group or class programme you suggest.",
    "You say plainly how strong the evidence is and any known risk."],
   ["Some programmes have good evidence. Others have mixed evidence.",
    "Putting children with behaviour difficulties in one group can make things worse.",
    "Suggesting what a school likes, not what works, is misleading."],
   ["You can name a study you have read.",
    "You do not say something is proven when it is not."],
   ["Evidence: research that shows whether something works.",
    "Mindfulness: a way of paying calm attention to the present moment."])

_e("Co-facilitate rather than only observe",
   ["You run part of a group session together with a school staff member.",
    "You set ground rules at the start."],
   ["Watching a group is not the same as running one.",
    "Running a group means managing time, turns and children who will not join in.",
    "Working with staff helps the group go on after you leave."],
   ["You delivered part of the group yourself.",
    "Just watching does not show you can do it."],
   ["Co-facilitate: run a group together with another person.",
    "Ground rules: rules the group agrees at the start."])

_e("Adapt delivery to the group in front of you",
   ["You notice when a group is not following you.",
    "You change the surface, like pace, examples or seating."],
   ["If you change the key parts, you cannot tell if the programme works.",
    "If you never change anything, children switch off."],
   ["You changed something because of how the group reacted.",
    "You kept the key parts the same.",
    "You wrote down what you changed and why."],
   ["Programme: a planned set of sessions with key parts."])

_e("Measure something before and after",
   ["You measure the children before and after a group.",
    "You check the group was run as planned and ask staff what they saw."],
   ["Without this, you cannot say if the group worked.",
    "A short check in the first and last week is often enough."],
   ["There is outcome data, even if it is simple.",
    "You report the result honestly, with its limits."],
   ["Outcome data: information that shows what changed."])

_e("Leave the teacher able to run it",
   ["You plan from the start to hand the group over to a staff member.",
    "You run it together first, then hand it over."],
   ["Help that stops when you leave has failed.",
    "You leave, but the school keeps the children."],
   ["A named staff member has led sessions and has the materials.",
    "They know what to do if a child tells them something worrying.",
    "They have a date to run it again."],
   ["Handover: passing work on to someone else to carry on."])

_e("Use open questions and reflective listening",
   ["You ask open questions that let people tell their story.",
    "You say back what you heard, and gently name feelings."],
   ["Every meeting with a parent or pupil depends on these skills.",
    "Without them you get little information and can harm trust.",
    "This is everyday good talking, not therapy."],
   ["The young person talks more than you do.",
    "You sum up and let them correct you."],
   ["Open question: a question that cannot be answered with yes or no.",
    "Reflective listening: saying back what you heard, to show you understood."])

_e("Hold silence without filling it",
   ["You wait quietly for a few seconds after someone answers.",
    "You tell the difference between someone thinking and someone upset."],
   ["Waiting often gets more than another question.",
    "Filling silence can cut off what the young person was about to say."],
   ["You waited.",
    "If the young person was upset, you responded to that."],
   ["Silence: a pause when nobody speaks."])

_e("Use scaling or solution-focused questioning",
   ["You use a named way of asking questions in a pupil interview.",
    "For example, you ask the pupil to rate things from 0 to 10."],
   ["It gives the interview a clear shape.",
    "Without a method, an interview can drift into a chat that is hard to use."],
   ["You used a named method, not just a chat.",
    "You changed it to suit the child's age.",
    "You wrote down what it found."],
   ["Solution-focused: asking about what already works and what could be better.",
    "Scaling question: asking someone to rate something on a number line."])

_e("Recognise when the work exceeds your competence",
   ["You say what your role is at the start.",
    "You notice when a talk goes beyond what you can do, and say so kindly."],
   ["You can listen and help people think. You cannot give therapy.",
    "Going too far is one of the more serious mistakes a trainee can make.",
    "Talk of self-harm, suicide or abuse must go through child protection steps the same day."],
   ["You named your limit before you reached it.",
    "You passed on risk the same day, then told your supervisor."],
   ["Competence: what you are trained and able to do safely.",
    "Therapy: treatment for mental health problems."])

_e("Know the onward referral route and use it",
   ["When a problem is beyond you, you stop and refer on.",
    "You give a named service, how to reach it and what happens next."],
   ["'See someone' leaves the person with nowhere to go.",
    "Services can include the family doctor and child mental health services.",
    "For a child protection worry, tell Tusla (the child and family agency) quickly.",
    "Telling the school's safeguarding person is not enough on its own."],
   ["You referred on rather than carrying on.",
    "For risk, you used the child protection steps the same day."],
   ["Refer: pass someone on to another service for help.",
    "Tusla: the child and family agency in Ireland.",
    "Safeguarding person: the staff member who leads on child protection in a school."])

_e("Close the relationship properly",
   ["You say early on when the work will end.",
    "At the end you sum up and say what happens next."],
   ["An unclear ending leaves a parent waiting for contact that never comes.",
    "That does more harm than a clear ending."],
   ["There was a clear ending, not a fade-out.",
    "You said what is written down and who will see it.",
    "You named who to contact after you leave."],
   ["Ending: the planned finish of your work with a family."])

_e("State the Continuum level for each recommendation",
   ["You name the level of school support for every idea for help.",
    "If the level is higher than now, you say why."],
   ["Irish schools give help at three levels.",
    "With no level, the school has to guess. It often guesses the lowest.",
    "The level also tells the school which forms to fill in."],
   ["The level is written in the text of every idea for help."],
   ["Continuum of Support: the three levels of help in Irish schools. They are Classroom Support, School Support and School Support Plus.",
    "Recommendation: an idea you write down for what should help."])

_e("Check the school can actually resource it",
   ["Before you finish your ideas for help, you ask the school if it can do them.",
    "You write down that you asked."],
   ["An idea nobody can staff just sits in a file.",
    "The family may feel a promise was broken.",
    "Asking first keeps your ideas honest."],
   ["You asked the principal or special education teacher before you wrote it."],
   ["Resource: to have the staff and time to do something.",
    "Special education teacher: a teacher who gives extra help to pupils who need it."])

_e("Name who delivers",
   ["You start every idea for help with the job of the person who does it.",
    "For example, class teacher, principal or parent."],
   ["'The school should' belongs to nobody, so it often does not happen.",
    "Name a job, not a person, because staff can move."],
   ["Every idea for help is given to a named role."],
   ["Role: a person's job, like class teacher.",
    "Recommendation: an idea you write down for what should help."])

_e("Name how often and for how long",
   ["For direct help, you say how often it happens.",
    "You say how long each time and for how many weeks."],
   ["How much help a child gets affects how well it works.",
    "'Regular' could mean almost anything.",
    "Without this, you cannot tell if help failed or was never really given."],
   ["The amount of help is written down clearly.",
    "You do not use words like 'regular' or 'ongoing' instead."],
   ["Dose: how much of the help the child gets."])

_e("Limit the number so they can be acted on",
   ["You keep your list of ideas for help short.",
    "You put the most important first."],
   ["A busy teacher cannot do fifteen things.",
    "She may pick the easiest ones, not the most important.",
    "If you cannot pick the most important, your thinking is not finished."],
   ["Five ideas that happen beat fifteen that do not.",
    "Extra ideas go in a separate handout."],
   ["Prioritise: decide what matters most and put it first."])

_e("State how progress will be measured",
   ["For each idea for help, you say how progress is measured.",
    "You say who measures it and when."],
   ["Without a measure, help goes on or stops on a feeling.",
    "A measure with no named person is not taken."],
   ["A measure and the person who takes it are both named."],
   ["Measure: a way of checking a skill, often with a score.",
    "Baseline: a measure taken before help starts."])

_e("Set a review date",
   ["You end every report with a date to check how things are going.",
    "You say whose job it is to set up the meeting."],
   ["Without a date, reviews happen only when things go wrong.",
    "A date stops help going on long after it stopped working."],
   ["There is a date, written as day, month and year."],
   ["Review: a meeting to check how things are going."])

_e("Build at least one on a strength",
   ["You use something the child is good at to help them.",
    "At least one idea for help in each report does this."],
   ["Only fixing weak spots tells everyone the child is a list of problems.",
    "Strengths can be a way to help.",
    "A good talker may learn by talking through ideas before writing."],
   ["Your ideas are not only about making up for weak spots.",
    "The strength is real and you can show evidence for it."],
   ["Strength: something a child is good at.",
    "Deficit: something a child finds hard."])

_e("Plan the first three sentences",
   ["Before meeting a parent, you plan how you will start.",
    "You welcome them and ask what they know and want.",
    "You say what the meeting will cover and how long it takes."],
   ["Parents often arrive expecting a verdict.",
    "Until they hear the main point, they may take in little else."],
   ["You knew how you would open.",
    "You practised it first."],
   ["Feedback session: a meeting where you tell a parent what you found."])

_e("Give the overall picture before the detail",
   ["You tell parents the main message first, in plain words.",
    "Then you give the detail."],
   ["Parents often wait for the main point and miss everything before it.",
    "Starting with scores puts a number between the parent and their child."],
   ["You did not start with scores.",
    "The main message came near the start."],
   ["Score: a number from a test."])

_e("Agree next steps and who does what",
   ["At the end of a meeting, you agree out loud what happens next.",
    "Each action has a person or role. You send it in writing after."],
   ["Understanding without action is just a chat.",
    "Parents often leave not knowing what happens next."],
   ["Someone left the meeting with an action to do."],
   ["Action: a task someone agrees to do.",
    "Role: a person's job, like class teacher."])

_e("Avoid jargon and check understanding repeatedly",
   ["You explain special words the first time you use them.",
    "You check more than once that the parent understands."],
   ["Words like 'working memory' may mean nothing to a parent.",
    "'Does that make sense?' often just gets a polite yes.",
    "Asking a person to say it back in their own words works better."],
   ["You checked understanding more than once.",
    "You used open questions to check."],
   ["Jargon: special words that most people do not know.",
    "Open question: a question that cannot be answered with yes or no."])

_e("Name strengths specifically rather than as preamble",
   ["You name real strengths that belong to this child.",
    "You link them to what you found or what you suggest."],
   ["Parents know the pattern: nice words, then 'however'.",
    "General praise sounds like softening before bad news.",
    "A real strength shows you have seen the child, not just the scores."],
   ["Your praise does not sound like a formula.",
    "The strength has evidence behind it."],
   ["Strength: something a child is good at."])

_e("Ask what the parent hopes to hear before starting",
   ["At the start, you ask what the parent wants to know.",
    "You let their answer shape the order of the meeting."],
   ["Parents often come with one big question.",
    "Until it is answered, they may not hear anything else.",
    "Asking gives the parent some control."],
   ["You asked."],
   ["Feedback session: a meeting where you tell a parent what you found."])

_e("Deliver difficult information clearly",
   ["You give hard news in plain words.",
    "You warn before it, pause after it and check what the parent heard."],
   ["It is tempting to soften news until it disappears.",
    "Clear news is kinder in the long run.",
    "Parents who find out later from others lose trust."],
   ["The parent left knowing what was found."],
   ["Finding: something you found out from your work."])

_e("Hold silence when someone is upset",
   ["When a parent is upset, you stop talking.",
    "You say something short and kind if needed, then let them speak first."],
   ["Silence gives the parent time to take in the news.",
    "Filling it tells them the meeting matters more than their feelings."],
   ["You did not fill the silence."],
   ["Silence: a pause when nobody speaks."])

_e("Answer the question actually asked",
   ["You check you understand the parent's question.",
    "You answer that question, not an easier one."],
   ["Parents ask hard questions, like 'did I cause this?'",
    "Answering a different question tells them the real one cannot be said.",
    "You may not know the answer, but you can still respond to the question."],
   ["You answered the real question, not an easier one.",
    "If you could not answer, you said so."],
   ["Parent: the mother, father or carer of the child."])

_e("Say what you do not know",
   ["You say plainly when you do not know something.",
    "You keep it separate from what you do know."],
   ["Often the honest answer about the future is 'we are not sure'.",
    "False certainty can break trust later.",
    "'I don't know, and here is how we will find out' is a good answer."],
   ["You admitted you were not sure.",
    "You said what would help you find out."],
   ["Uncertainty: not knowing for sure."])

_e("Use a named consultation model",
   ["You use one named way of running meetings with teachers.",
    "You use it again and again."],
   ["Without a model, a meeting becomes a chat that ends in advice.",
    "A model gives you steps to come back to."],
   ["You can say which model you used.",
    "You can say which step each part of the meeting was."],
   ["Consultation: a meeting where you help a teacher or parent think a problem through.",
    "Model: a set way of doing something, with steps."])

_e("Contract at the start",
   ["At the start of a meeting, you agree what it is for.",
    "You agree how long it takes, who does what and what comes out of it."],
   ["A teacher may expect something different from what you plan.",
    "If you do not agree this, unspoken hopes take over."],
   ["You both know what the meeting is for.",
    "You asked what the teacher expected."],
   ["Contract: agree the purpose and plan of a meeting at the start.",
    "Consultation: a meeting where you help a teacher or parent think a problem through."])

_e("Ask questions that open rather than close",
   ["In meetings with teachers, you mostly ask questions.",
    "The plan comes from the teacher, not from you."],
   ["Questions help turn a worry into a clear problem.",
    "'Have you tried...?' can sound like criticism.",
    "A teacher who makes the plan is more likely to use it."],
   ["The teacher came up with the solution."],
   ["Consultation: a meeting where you help a teacher or parent think a problem through."])

_e("Identify who holds the problem and who holds the power",
   ["You work out who is most worried about a child.",
    "You work out who has the power to change things."],
   ["These are not always the same person.",
    "A plan made with someone who has no power may never happen."],
   ["You noticed the difference.",
    "You did something about the gap before the meeting ended."],
   ["Consultation: a meeting where you help a teacher or parent think a problem through."])

_e("Agree actions with a review point",
   ["You end every meeting with clear actions and who does them.",
    "You set a review date.",
    "You send a written record within a day."],
   ["Without a record and a date, agreements fade away.",
    "A written record lets everyone see the actions."],
   ["The actions are clear and dated."],
   ["Review: a meeting to check how things are going.",
    "Record: a written note of what was agreed."])

_e("Build capacity rather than doing it for them",
   ["In meetings, you help the teacher learn a way of solving problems.",
    "You leave them able to use it again, not just a plan for one child."],
   ["One psychologist cannot see every child.",
    "If you fix it for the teacher, the next child comes back to you.",
    "Trainees often want to be the expert. Try not to."],
   ["The teacher could do it again without you."],
   ["Capacity: the skills and know-how people have to do something themselves.",
    "Consultation: a meeting where you help a teacher or parent think a problem through."])

_e("Understand how SET hours are allocated",
   ["You learn how schools get special education teaching hours.",
    "You explain it to parents in plain words."],
   ["The hours go to the school as a block, not to one child.",
    "The school decides how to use them.",
    "Many parents think a report or diagnosis gets their child hours. It does not.",
    "The rules change, so check the current rules each year."],
   ["You can explain this to a parent.",
    "You ask what they now plan to ask the school."],
   ["SET: special education teaching. This is extra teaching for pupils who need it.",
    "Diagnosis: a professional name for a condition."])

_e("Cite the specific circular rather than 'guidance'",
   ["When you write about school support rules, you name the exact circular.",
    "You open the current one on the day you write, and quote only what it says."],
   ["Circulars change and get replaced.",
    "'Department guidance says' cannot be checked.",
    "A number and title let the principal check what you wrote."],
   ["You name the circular by number and title.",
    "You do not copy a number from an old report."],
   ["Circular: an official letter from the Department of Education that sets out rules for schools."])

_e("Know how the school deploys what it has",
   ["You learn the difference between what the school gets and how it uses it.",
    "You find out how support is used for this child."],
   ["Asking for 'more hours' asks the school to take them from another child.",
    "It can also make you look like you do not know how schools work."],
   ["You keep what the school gets and how it uses it separate.",
    "Your ideas for help say how to use the time the school has."],
   ["Allocation: the support time a school is given.",
    "Deployment: how the school uses that time."])

_e("Know the SENO route and what the NCSE can do",
   ["You learn who decides each kind of support for a child.",
    "You learn how to contact them."],
   ["Some things the school decides. Others go to a special needs officer outside the school.",
    "Special needs assistants are for big care needs, not learning support.",
    "The rules have changed. Check the current website before you advise anyone."],
   ["You know who to contact and for what.",
    "You word your ideas so the right person can act on them."],
   ["SENO: Special Educational Needs Organiser. This person handles requests for special needs assistants and special class places.",
    "NCSE: National Council for Special Education. This is the body the Special Educational Needs Organisers work for."])

_e("Map each Continuum level against provision",
   ["You draw up a picture of how a school really gives support at each level.",
    "You use at least two sources and note where they differ."],
   ["The policy says what should happen. The map shows what does happen.",
    "Two schools with the same hours can get very different results."],
   ["The map is complete and accurate.",
    "It is not copied just from the policy.",
    "You use it when you think about children in that school."],
   ["Continuum of Support: the three levels of help in Irish schools.",
    "Provision: the help a school actually gives."])

_e("Identify a gap in the continuum",
   ["You name one gap in how a school organises support.",
    "You link it to what it means for a child you work with."],
   ["It tells you if a problem is about the child or about how help is given.",
    "If the problem is how help is given, working with one child will not fix it.",
    "One clear gap is worth more than a long list."],
   ["You named one gap.",
    "It has more than one source and is about the system, not one staff member."],
   ["Gap: something missing in how support is given."])

_e("Say what would close the gap",
   ["You suggest one change that would close a gap in support.",
    "The school must be able to do it with what it already has."],
   ["A gap with no suggested change is no use to the school.",
    "Schools can usually carry out one change, not five.",
    "A change that needs things the school does not have gets dropped."],
   ["You suggested something the school could do.",
    "You agreed it with the people who would do it.",
    "You said how to check if it worked."],
   ["Gap: something missing in how support is given."])

_e("Present the map back to the school",
   ["You show the school your map of how it gives support.",
    "You describe, not judge, and offer one change."],
   ["A map left in your folder changes nothing for children.",
    "Someone must own the next step, or nothing happens."],
   ["The school used it, not just received it.",
    "There is an agreed action, a named owner and a review date.",
    "You followed up on that date."],
   ["Map: a written picture of how a school organises support."])

_e("Arrange visits early in the placement",
   ["You book visits to special schools and special classes early.",
    "You ask in the first week and get confirmed dates, with a backup date."],
   ["Your training needs visits to special education settings. You have not done any yet.",
    "The placement is short, and settings may need weeks of notice.",
    "If you leave it late, the gap carries into next year."],
   ["The visits are in your placement plan.",
    "They are booked in the first weeks."],
   ["Placement: time spent training in a real service.",
    "Special education setting: a special school or special class."])

_e("Observe structure, staffing and communication supports",
   ["On visits, you look at how a special setting works as a whole.",
    "You look at staff, lessons, ways of communicating and where pupils go next."],
   ["You will be asked if a child needs a special class or school.",
    "You cannot answer honestly if you have never seen one.",
    "Look at the whole system, not only the children."],
   ["You can describe how the setting works.",
    "You can say what kind of need it suits.",
    "You can say how it differs from others you saw."],
   ["Special education setting: a special school or special class.",
    "Curriculum: what is taught."])

_e("Talk to therapy and SNA staff, not only teachers",
   ["On visits, you talk to all the staff who support pupils each day.",
    "You note what each role does."],
   ["Much of the day may be run by assistants and therapists.",
    "Only the people using a communication system can tell you if everyone uses it."],
   ["You spoke to the people giving day-to-day support.",
    "You did not take the teacher's account as the whole picture."],
   ["SNA: special needs assistant. This is a staff member who helps with a child's care needs.",
    "Therapist: a professional, like a speech therapist, who works on a skill."])

_e("Log each visit separately in Appendix 5",
   ["You write a separate record for each setting you visit.",
    "You give the date, type of setting, age range and what you saw."],
   ["A special school and a special class are different places.",
    "One combined entry cannot show the range of places you saw.",
    "Your records are the proof you met this training need."],
   ["Each setting has its own entry.",
    "You write what changed in your thinking, in your own words.",
    "You leave out anything that could identify someone."],
   ["Appendix 5: the training log where you record your experience.",
    "Setting: a place where children are taught, like a special class."])

_e("Understand how casework is prioritised here",
   ["You learn how this service decides who is seen first.",
    "You use this to set honest timescales."],
   ["Each service decides this in its own way.",
    "Do not assume it works like your last placement.",
    "Often the rules are not written down. You learn them at team meetings."],
   ["You know what decides the waiting list.",
    "You tell schools and families honestly what to expect."],
   ["Casework: work with individual children.",
    "Prioritise: decide who or what comes first."])

_e("Note what the service can and cannot offer",
   ["You learn what your service can and cannot give.",
    "You check who will carry out each idea for help, and if they can."],
   ["An idea the service cannot deliver will not happen.",
    "The family may then blame the school or service.",
    "Knowing the limits tells you when to point families to other services."],
   ["You know the limits before you suggest help.",
    "You point people honestly to other services when needed."],
   ["Service: the team you work in, like a school psychology service.",
    "Signpost: tell someone where else to go for help."])

_e("Prepare something to contribute",
   ["You go into each team meeting with one small thing to say.",
    "For example, a question about a case or an offer to help."],
   ["Sitting silent for a whole term wastes it.",
    "Team meetings are a safe place to practise speaking up.",
    "Small and specific is better than trying to impress."],
   ["You spoke.",
    "You logged what you said, not just that you went."],
   ["Contribution: something you say or offer to the group."])

_e("Contribute a psychological perspective",
   ["In team meetings, you give a psychologist's view in plain words.",
    "You add something other professionals did not bring."],
   ["Different professions think about cases in different ways.",
    "Disagreements are often about how people see a case, not the facts.",
    "If you add nothing new, there is no point in you being there."],
   ["You added something another profession would not.",
    "You noticed where your view differed from theirs."],
   ["Perspective: a way of seeing and understanding something.",
    "Jargon: special words that most people do not know."])

_e("Learn a structured problem-solving model",
   ["You learn a set of steps for meetings with teachers.",
    "Define the problem, look at it, plan, try it, then check it."],
   ["Getting the problem clear early seems to matter most.",
    "Without steps, you slip into giving advice.",
    "Advice is often politely ignored."],
   ["You can name the steps and follow them in order.",
    "Your notes record the problem, the plan and a review date."],
   ["Model: a set way of doing something, with steps.",
    "Consultation: a meeting where you help a teacher or parent think a problem through."])

_e("Learn a solution-focused approach",
   ["You learn to ask about times when things go well.",
    "You ask people to rate things from 0 to 10.",
    "You agree one small step that builds on what works."],
   ["It is quick and suits busy teachers.",
    "You used it before. Now you use it with skill.",
    "Asking the questions but still giving advice misses the point."],
   ["You can use rating and 'when does it go well' questions.",
    "You follow up each answer."],
   ["Solution-focused: asking about what already works and what could be better.",
    "Scaling question: asking someone to rate something on a number line."])

_e("Ask your supervisor which model they use",
   ["You ask your supervisor which model they use for meetings with teachers.",
    "You ask if they were trained in it."],
   ["Irish rules do not name meeting models, so you could miss learning one.",
    "The answer tells you what you can learn by watching.",
    "It also tells you what to read about elsewhere."],
   ["You know which model they use.",
    "You know if they were trained in it."],
   ["Supervisor: the experienced psychologist who guides your training.",
    "Model: a set way of doing something, with steps."])

_e("Follow one model explicitly for a set of consultations",
   ["You use one named model for a series of meetings.",
    "You record it each time."],
   ["You learn by doing one thing again and again, and thinking about it.",
    "Trying lots of models means you learn none well.",
    "If you never name the model, you cannot show you learned it."],
   ["You can say what the model gave you.",
    "You can say where it did not work and what you would use instead."],
   ["Model: a set way of doing something, with steps.",
    "Consultation: a meeting where you help a teacher or parent think a problem through."])

_e("Cite current peer-reviewed evidence",
   ["When you say something works, you name the research behind it.",
    "You say honestly how strong the evidence is."],
   ["Teachers will act on what you tell them.",
    "'Research shows' with no source cannot be checked.",
    "Check that findings fit Irish classrooms."],
   ["The evidence is easy to see.",
    "You give a short list of sources.",
    "You have read them yourself."],
   ["Peer-reviewed: research checked by other experts before it is published.",
    "Evidence: research that shows whether something works."])

_e("Pitch it at teachers rather than examiners",
   ["You make training talks useful for teachers.",
    "Each part ends with what to do, not only what to know."],
   ["Teachers want something they can use on Monday.",
    "A talk full of theory loses the room quickly.",
    "Training is one of your strengths, so build on it."],
   ["Every piece of research you mention is turned into a practical point.",
    "The theory and full sources go in a one-page handout."],
   ["Citation: naming the research you are using.",
    "Handout: a sheet of paper people take away."])

_e("End with three things the school could do this term",
   ["You end a training talk with three clear actions.",
    "The school could do them this term with what it has."],
   ["People keep one page, not fifty slides.",
    "Training alone rarely changes practice without follow-up.",
    "Big hopes like 'be inclusive' cannot be done, so they won't be."],
   ["The actions can be done, not just hoped for.",
    "Each says who does what."],
   ["Action: a task someone agrees to do.",
    "Term: part of the school year."])

_e("Collect and file feedback from the school",
   ["At the end of a training talk, you ask staff for short feedback.",
    "For example: what will you do differently? What was missing?"],
   ["It takes two minutes and gives you evidence.",
    "A feedback form shows what people thought and plan to do.",
    "It does not show that their practice really changed."],
   ["You have evidence the training helped staff.",
    "You sum up the feedback honestly.",
    "Where you can, you check later if actions were taken."],
   ["Feedback: what people tell you about how something went.",
    "Anonymous: without names."])

_e("Meet the child at their level, literally and in register",
   ["You fit how you sit, speak and pace to the child in front of you.",
    "You keep changing as you get to know them."],
   ["A worried or wary child may score lower than they really are.",
    "Good rapport is part of getting true scores.",
    "Do not talk down to a teenager or over a small child's head."],
   ["The child was not talked down to or over.",
    "You matched the real child, not just the age on the form."],
   ["Rapport: a feeling of trust and ease between two people.",
    "Register: the style of words you use, like formal or chatty."])

_e("Explain what will happen and why",
   ["At the start, you tell the child who you are and why you are there.",
    "You say what will happen, how long it takes and who will be told."],
   ["Children often think they are in trouble.",
    "Tell them some tasks get too hard for everyone.",
    "Then a hard task does not feel like failing."],
   ["The child could say it back to you.",
    "You did not just ask 'OK?'"],
   ["Assessment: finding out about a child's needs, for example with tests."])

_e("Give the child a real choice early",
   ["You give the child one real choice near the start.",
    "Then you do what they chose."],
   ["In an assessment the child has almost no control.",
    "One real choice changes that and often helps effort.",
    "A fake choice teaches the child your offers are not real."],
   ["Something was truly the child's to decide."],
   ["Assessment: finding out about a child's needs, for example with tests.",
    "Choice: a real chance to decide something."])

_e("Notice and respond to reluctance",
   ["You notice early when a child does not want to go on.",
    "You change what you do rather than pushing."],
   ["Signs include quieter answers, fast guessing and 'I don't know'.",
    "Scores taken under pressure can be wrong.",
    "Stopping and coming back another day can be better."],
   ["You adjusted rather than pushed on.",
    "You wrote down what you saw and did.",
    "Your report says what this means for the scores."],
   ["Reluctance: not wanting to do something.",
    "Score: a number from a test."])

_e("Ask the child what they think would help",
   ["You ask the child what would help them.",
    "You write it down in their words."],
   ["Children have a right to give their views on things that affect them.",
    "Children often know what helps, but no one asks.",
    "Asking is not enough. Their view should make a difference."],
   ["You asked for the child's view.",
    "Your report shows where it shaped an idea for help, or why not."],
   ["View: what someone thinks about something.",
    "Right: something every child should have by law."])

_e("Know who does what in this school",
   ["You learn the job of each person in the school.",
    "You go to the right person first for each request."],
   ["The principal makes decisions and gives out time.",
    "The class teacher does most of what you suggest.",
    "The special needs assistant often knows the child best.",
    "Jobs and titles differ from school to school."],
   ["You went to the right person."],
   ["Role: a person's job, like class teacher.",
    "Special needs assistant: a staff member who helps with a child's care needs."])

_e("Negotiate a shared referral question",
   ["You agree a clear question with the school and parent before assessing.",
    "You write it down."],
   ["Schools often ask for a label, like 'test for dyslexia'.",
    "You need to find out what they really need to know.",
    "If everyone has a different question, the report pleases nobody."],
   ["The school and the parent both know the question."],
   ["Referral: a request for a psychologist to get involved.",
    "Dyslexia: a lasting difficulty with reading and spelling words."])

_e("Manage disagreement rather than avoiding it",
   ["When someone disagrees with you, you talk about it openly.",
    "You ask what they see and what would change your mind."],
   ["Teachers sometimes disagree, and sometimes they are right.",
    "Disagreement that is avoided does not go away.",
    "It comes back as ideas that never get used."],
   ["The disagreement was talked about.",
    "You agreed a next step, even if you still differ."],
   ["Finding: something you found out from your work."])

_e("Maintain the relationship afterwards",
   ["You send a short written summary within a day.",
    "You go back to the school to check how things are going."],
   ["A written summary stops people forgetting what was agreed.",
    "Schools notice psychologists who vanish after testing.",
    "After a disagreement, you may need to repair the relationship."],
   ["You went back.",
    "You made contact again after any disagreement."],
   ["Summary: a short note of the main points."])

_e("Prepare the structure before the meeting",
   ["Before meeting a parent, you write a one-page plan.",
    "It has the main message, the order, plain words and next steps."],
   ["Parents often wait for the main point and miss everything else.",
    "Give the main message in the first two minutes.",
    "People forget much of what they hear, so structure matters."],
   ["You knew the order you would take.",
    "You followed your plan."],
   ["Structure: the order and shape of a meeting."])

_e("Use plain language and check understanding",
   ["You explain every finding without jargon.",
    "Before the end, you ask the parent to say it back in their own words."],
   ["If you cannot explain it simply, you may not understand it well enough.",
    "'Does that make sense?' nearly always gets a yes.",
    "A parent who understands can speak up for their child."],
   ["You checked what the parent understood.",
    "You fixed anything they got wrong."],
   ["Jargon: special words that most people do not know.",
    "Finding: something you found out from your work."])

_e("Lead with the child, not the scores",
   ["You start by describing the child as you met them.",
    "You link each finding to something the parent knows from home or school."],
   ["Parents know their child as a person, not a set of numbers.",
    "If they recognise their child, they are more likely to trust hard news."],
   ["The parent can recognise their child in what you say."],
   ["Score: a number from a test.",
    "Finding: something you found out from your work."])

_e("Name strengths specifically",
   ["You name at least one real strength and the evidence for it.",
    "You show how it links to what happens next."],
   ["Made-up or vague praise sounds like comfort.",
    "It makes parents doubt the rest of what you say.",
    "Real strengths can be built on in the plan."],
   ["You gave real, specific praise, not general praise."],
   ["Strength: something a child is good at.",
    "Evidence: facts that show something is true."])

_e("Hold distress without rushing past it",
   ["When a parent is upset, you stop and name it kindly.",
    "You allow silence and wait until they are ready.",
    "You offer a second meeting if needed."],
   ["News can bring grief, anger, guilt or relief.",
    "Rushing on tells the parent their feelings are in the way."],
   ["You slowed down."],
   ["Distress: strong upset or worry."])

_e("Leave the parent with something concrete",
   ["At the end of a meeting, you say what happens next.",
    "You say who does each thing and by when.",
    "You give one thing the parent can do and a written summary."],
   ["A parent with a feeling but no plan will soon be ringing around.",
    "Parents often do not know how school support or other services work."],
   ["The parent knows what happens next.",
    "They know when the report will arrive."],
   ["Next steps: the actions that come after the meeting."])

_e("Use the service's format and terminology",
   ["You write notes the way your service does.",
    "You use its forms and only the short forms it accepts."],
   ["Each service keeps records in its own way.",
    "The next person to open the file must be able to use it.",
    "You will leave while some cases are still open."],
   ["Your notes match the service's way of doing things.",
    "A colleague who never met the child can understand them."],
   ["Template: a set form to fill in.",
    "Service: the team you work in."])

_e("Store and transfer records lawfully",
   ["You keep and send records only in approved ways.",
    "Nothing goes on your own phone, laptop, cloud or chat apps."],
   ["Records hold private health information protected by law.",
    "Trainees often slip up to save time.",
    "A photo of a form on your phone can be a data breach."],
   ["Nothing that could identify a child is on your own devices.",
    "Rough notes are destroyed as the policy says."],
   ["Data breach: when private information goes where it should not.",
    "Identifiable: could show who someone is."])

_e("Separate fact from opinion and label opinion",
   ["In notes, you keep what you saw, what you were told and what you think apart.",
    "You say who told you each thing and mark your opinion as yours."],
   ["'Left his seat four times' is fact. 'Not engaged' is opinion.",
    "Families and others, like a court, may read your notes.",
    "Opinion written as fact cannot be checked."],
   ["A reader can tell which is fact and which is opinion."],
   ["Opinion: what you think, not what you saw.",
    "Source: the person or place information came from."])

_e("Avoid conjecture",
   ["You do not write guesses in records as if they were facts.",
    "You check every note for guesses before filing it."],
   ["A guess like 'probably a condition' can spread to other records.",
    "It can shape how others see the child before they meet them."],
   ["You did not guess in the record.",
    "Ideas to check go to supervision, or are clearly marked as questions."],
   ["Conjecture: a guess with no real evidence.",
    "Supervision: regular meetings with an experienced psychologist who guides you."])

_e("Write the same day",
   ["You write your notes on the same day as the contact.",
    "You plan a short writing time after each visit."],
   ["Notes written at the time are more trusted.",
    "Memory soon fills in gaps.",
    "A note written later takes longer and loses detail."],
   ["Your notes are written at the time.",
    "If you write it the next day, you record both dates honestly."],
   ["Contemporaneous: written at or near the time it happened."])

_e("Record consent, contacts and decisions",
   ["Your file shows consent, every contact and every decision.",
    "Each decision has an owner, a date and a review point."],
   ["Anyone should be able to see what you did and when.",
    "A common mistake is writing what was said but not what was decided."],
   ["The file shows what you did and when."],
   ["Consent: agreeing to something after it is explained.",
    "Review point: a date to check how things are going."])

_e("Know the countersigning standard before drafting",
   ["You ask your supervisor how they want reports done before you write.",
    "You keep a checklist and write to it."],
   ["Your supervisor signs your report and puts their name to it.",
    "Each service has its own form and way of reporting scores.",
    "Finding out from a returned draft wastes time."],
   ["You asked at the start.",
    "You did not reuse your last service's form."],
   ["Countersign: when your supervisor signs your work too.",
    "Draft: an early version of a report."])

_e("Proofread against the service template",
   ["You check every draft carefully before your supervisor sees it.",
    "You check it in separate goes, against the test forms and the template."],
   ["Common mistakes are another child's name or a wrongly copied score.",
    "A parent who spots one may stop trusting the whole report.",
    "A wrong score can change what the school does."],
   ["There are no mistakes in scores or names.",
    "You send the test forms and scoring with the draft."],
   ["Proofread: check writing carefully for mistakes.",
    "Template: a set form to fill in."])

_e("Include a tool rationale",
   ["In your report, you say why you chose each test for this question.",
    "You say if any results should be read with care for this child."],
   ["It shows you planned the assessment from the question.",
    "It helps a later psychologist know what the results can answer."],
   ["The reasons are there for every test."],
   ["Rationale: the reason for a choice.",
    "Referral question: the question the assessment is trying to answer."])

_e("Include an integration section",
   ["Your report has a part that brings all the findings together.",
    "It is organised by question or theme, not test by test."],
   ["It shows where the findings agree and where they clash.",
    "It says what you make of any clash.",
    "Without it, your supervisor cannot see your thinking."],
   ["It is not just a list of tests.",
    "Each paragraph uses more than one source."],
   ["Integration: bringing different findings together into one picture.",
    "Finding: something you found out from your work."])

_e("Name the framework in the formulation",
   ["You name the framework your formulation uses.",
    "You reference it properly and follow its steps."],
   ["Without a framework, a formulation is just a hunch.",
    "Naming it tells the reader how you organised the evidence."],
   ["The framework is named and referenced.",
    "The formulation really follows it."],
   ["Framework: a set way of organising ideas.",
    "Formulation: your written idea of why the child is having a hard time."])

_e("Include a limitations paragraph",
   ["Every report says what limits the results for this child.",
    "Each limit is linked to the conclusion it affects."],
   ["A report with no limits section is not good enough to sign.",
    "The limits must be about this child, not general words.",
    "For example, a test in a second language may underrate the child."],
   ["Every report has one, with no exceptions.",
    "You do not paste in the same words each time."],
   ["Limitation: something that makes a result less sure."])

_e("Write recommendations a teacher could act on Monday",
   ["You write ideas for help a teacher could use straight away.",
    "Each says who, what, how often, with what, and when."],
   ["Teachers want to know what to do on Monday.",
    "Vague ideas give nobody a task, so they rarely happen.",
    "Each idea is set at a level of school support."],
   ["Your ideas are specific, can be resourced and have dates."],
   ["Recommendation: an idea you write down for what should help.",
    "Continuum of Support: the three levels of help in Irish schools."])

_e("Quote the child's own words",
   ["Your report includes the child's own words about their views.",
    "The child knows you are doing this."],
   ["Children have a right to give their views and be taken seriously.",
    "Their view should make a difference, not just be written down.",
    "Without it, the report is about the child but the child is missing."],
   ["The child comes across as a person.",
    "At least one idea for help responds to what they said."],
   ["View: what someone thinks about something.",
    "Quote: the exact words someone said."])

_e("Judge who will read this and what they need",
   ["Before you write, you decide who the main reader is.",
    "You answer their question early."],
   ["Parents, teachers and other professionals each want different things.",
    "A teacher wants to know what to do. A parent wants to know what it means.",
    "A document written for no one in particular helps nobody fully."],
   ["You can name the main reader.",
    "You have thought about the other readers too."],
   ["Reader: the person who will read what you write."])

_e("Change register between family and professional audiences",
   ["You write one version for the family and one for professionals.",
    "They sound different but say the same thing."],
   ["A family letter full of scores leaves parents unsure.",
    "A letter to another service that is too chatty may lack detail they need.",
    "The two versions must not contradict each other."],
   ["The two versions read differently.",
    "Adding a word list to the professional report is not enough."],
   ["Register: the style of words you use, like formal or chatty.",
    "Professional: a trained worker, like a doctor or therapist."])

_e("Produce an accessible or plain-language version",
   ["You make an easy-to-read version of a report when someone needs it.",
    "You record that you did it and why."],
   ["Some parents find reading hard or read in another language.",
    "Some have an intellectual disability. Some readers are young people.",
    "Services must not treat people unfairly because of disability or race."],
   ["An easy version exists when it is needed.",
    "You avoid long sentences and sayings if an interpreter will be used."],
   ["Plain language: clear, simple words that most people understand.",
    "Interpreter: a person who puts words from one language into another."])

_e("Check the young person could read what is written about them",
   ["Before a report goes out, you read it as the young person would.",
    "You change words so they are accurate and respectful."],
   ["Young people may read their report, now or later.",
    "They have a right to see their own records.",
    "Harsh labels teach them how adults see them."],
   ["You thought about them as a reader.",
    "Where it fits, you made a version for them."],
   ["Respectful: showing care and value for a person."])

_e("Submit vetting early enough to clear before day one",
   ["You check what vetting each placement needs.",
    "You apply early and have it cleared before your first day."],
   ["By law, you cannot work with children until vetting is back.",
    "It can take a while, and the time varies.",
    "Lost days come off your placement."],
   ["Your vetting is cleared, not waiting.",
    "You do not assume old vetting carries over."],
   ["Vetting: an official check on you before you can work with children.",
    "Placement: time spent training in a real service."])

_e("Complete Children First training and file the certificate",
   ["You do the free online Children First course before your placement.",
    "You keep the certificate on file."],
   ["It teaches how to spot and report worries about a child.",
    "Placements and your university expect it.",
    "It is the starting point for child protection skills."],
   ["Your certificate is dated before the placement starts.",
    "You know where the service's child safety statement is."],
   ["Children First: the Irish law and guidance on keeping children safe.",
    "Certificate: a paper that shows you finished a course."])

_e("Know the Tusla reporting thresholds",
   ["You learn when a worry about a child must be reported.",
    "You learn the types of harm the law names."],
   ["For most harm, the law asks if the child is seriously harmed or at risk.",
    "For sexual abuse, it does not need to be serious.",
    "Anyone with reasonable grounds for concern should tell Tusla (the child and family agency) quickly.",
    "Read the full guidance. There are rules not covered here."],
   ["You can say what reaches the level for reporting.",
    "You do not wait for proof. Reasonable grounds are enough."],
   ["Tusla: the child and family agency in Ireland.",
    "Threshold: the point at which you must act.",
    "Reasonable grounds: a sensible reason to be worried."])

_e("Know you are a mandated person and what that means",
   ["You learn that psychologists must report serious harm to children by law.",
    "You tell Tusla (the child and family agency) quickly."],
   ["Telling the school's safeguarding person is not enough on its own.",
    "You can make a joint report with them.",
    "It is not certain if trainees count. Check in writing, and act as if you do."],
   ["You know the duty is yours and cannot be passed on.",
    "You make the report or check your name is on it, and keep a record."],
   ["Mandated person: someone who must report serious harm to children by law.",
    "Tusla: the child and family agency in Ireland.",
    "Safeguarding person: the staff member who leads on child protection in a school."])

_e("Complete health and safety and lone working induction",
   ["You learn your service's safety steps for working alone.",
    "You follow them for every visit."],
   ["You often work alone in schools, homes and cars.",
    "Someone needs to know where you are and when you are due back.",
    "Home visits can carry extra risk."],
   ["You know what to do for a home visit.",
    "You check the file for risks before you go.",
    "You sign out, even for a short visit."],
   ["Lone working: working on your own, without a colleague nearby.",
    "Induction: training when you start somewhere new."])
