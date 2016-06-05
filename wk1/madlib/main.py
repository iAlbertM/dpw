'''
Project Info
Intro to Python: MadLib
author: Albert Martinez
class:Design Patterns for Web Programming DPW-1606
instructor: Rebecca Carroll
'''
# MadLib details
madlib = dict() # instantiating the user_info dictionary
# assigning key:value pairs to the user_info dictionary
madlib = {'title':'The Way it Works at Work', 'author': 'Albert Martinez', 'course': 'DPW1606'}
title = madlib['title']
author = madlib['author']
course = madlib['course']
# Questions: gather user input for madlib story using 'raw_input()' and store in a  variable with a sensible name
name = raw_input('what is your name: ')
age = raw_input('how young are you: ')
occupation = raw_input('what is your dream job: ')
sex = raw_input('what is your sex: type \"1\" for male or \"2\" for female: ')
old_age = raw_input('write the first NUMBER that comes to mind when you think of... \"old\": ')
young_age = raw_input('what is the first NUMBER that comes to mind when you think of... \"young\": ')
number = raw_input('type in a number from 1-25: ')
greet_adverb = raw_input('name an adverb: ')
greet_nickname = raw_input('name a cheesy or funny nickname: ')
object_plural = raw_input('name an object (plural): ')
body_part = raw_input('name a body part: ')
old_term = raw_input('a phrase or term to describe something old: ')
verb = raw_input('name an action verb: ')
mad_phrase = raw_input('To get rid of people asking 4 donations or volunteer work, you say: ')
nice_phrase = raw_input('Imagine \"The One\" asks you out. You say: ')
salutation = ['Love, Mom & Dad', 'Later sis, Big Brother', 'Sincerely, Uncle Sam']
# use user sex to determine the name prefix when greeting the user
prefix = ["Mr. ", "Ms./Mrs. "]
if sex == 1:
    greeting = str(prefix[0]) + name
elif sex == 2:
    greeting = str(prefix[1]) + name
else:
    greeting = "earthling, " + name

# MadLib welcome phrase concatenation
greet = "Thank you for your responses. Welcome to your MadLib Story, " + greeting

# MadLib story
message = '''
{greet}\n
{title}\n
Hey {name}. Your Mom and Dad told me your doing well in school and close to graduating.\n
So you're now, what, {age} years old, right? Getting ready for a real world job is a big deal. Let me give you a few tips that you should remember:\n
\tWhen you greet a coworker in the break room say, \"Hey, working hard or {greet_adverb} working?\" This shows them you are \" The {greet_nickname} .\"\n
\tMake friends with the cleaning staff, they always know where the good {object_plural} are.\n
\tIf your boss ever asks you to guess her age, DON'T but If you must, REMEMBER:\n
\t\tIf she looks {old_term}, which is anything {old_age} years old and above, shave off {number} from your original guess and pray she doesn't {verb} you.\n
\t\tIf she looks young, which is anything under {young_age}, repeat the same step as above.\n
Lastly, if ever asked to stay after work hours and \"volunteer\" your time, never say:\n
\t\" {mad_phrase} \"\n
instead look her square in the eyes and with a great big smile say,\n
\t\" {nice_phrase} \"\n
{salutation[0]}\n
xo\n
\n
MadLib Credits\n
{title}\n
created by:\t{author}\n
course:\t{course}
'''
message = message.format(**locals())
print message
