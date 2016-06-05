'''
Intro to Python: MadLibsss
author: Albert Martinez
class:Design Patterns for Web Programming DPW-1606
instructor: Rebecca Carroll
'''

#gather user input for MadLib story using 'raw_input()' and store in a  variable with a sensible name
age = raw_input('write the first number that comes to mind... now: ')
occupation = raw_input('name an occupation: ')
adverb = raw_input('name an adverb: ')
nickname = raw_input('name a cheesy or funny nickname: ')
object_plural = raw_input('name an object (plural): ')
body_part = raw_input('name a body part: ')
old_term = raw_input('a phrase or term to describe something old: ')
large_number = raw_input('type in a crazy number: ')
verb = raw_input('name an action verb: ')
angry_phrase = raw_input('Imagine your getting married first thing in the morning. Great right? Just wait...'
                         'You haven\'t slept in 2 days due to your neighbor\'s construction project. He finished and you finally get to bed at 10pm the night before your wedding. Your sibling annoyingly staying with you until the wedding wakes you up at 4am with a air horn in your ear. What are the words that come to mind... hmm? : ')
nice_phrase = raw_input('Imagine everything went just absolutely perfect. Your new husband turns to you and asks ready for the rest of our lives together?" You would respond: ')
annoying_person = raw_input('the most annoying person in your life: ')

#MadLib story with placeholder keywords to be filled in by the user input
madlib = '''
The Way it Works at Work
So you are now, what {age} years old, right? You think you know how it works in the {occupation} world
just remember these few tips:
When you greet a coworker in the breakroom say, "Hey, working hard or {adverb} working?" This shows them you are " The {nickname} ."
Make friends with the cleaning staff, they always know where the good {object_plural} are.
Be nice to your boss. Kiss {body_part} to stay on her good side.
If your boss ever asks you to guess her age, REMEMBER:
If she looks {old_term} , shave off {large_number} from your original guess and pray she doesn't {verb} you.
If she looks young, repeat the same step as before.
Lastly, if ever asked to stay overtime and work overtime without getting overtime because it's "volunteer work",
never say, " {angry_phrase} " instead say, " {nice_phrase} "
Good luck,
Love {annoying_person}
xoxo
'''

madlib = madlib.format(**locals())
print madlib