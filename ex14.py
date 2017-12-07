import sys
from sys import argv

script, user_name = argv
prompt = '>>> '

print "Hi %s, I am a script %r." % (user_name, script)
print "I want to aks you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What computer do you use for your work?"
computer = raw_input(prompt)

print "How old are you?"
age = raw_input(prompt)

print """
So, you answered %r on question, did you like me.
You live in %r. You are %s years old I don't imagine where is it.
And you have computer %r. Excellent!
""" % (likes, lives, age, computer)
