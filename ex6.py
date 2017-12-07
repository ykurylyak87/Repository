x = "There are %d types of people" % 10
binary = "Python"
do_not = "no"
y = "Who understand %r, and who %s" % (binary, do_not)

print x
print y

print "I said: %s" % x
print "And also I said: '%s'" % y

hilarious = False
joke_evaluation = "Is that fanny?! %r"

print joke_evaluation % hilarious

w = "This is a part of a string from the left "
e = "and this from the right"

print w + e
