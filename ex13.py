from sys import argv

script, first, second, third = argv


print "This argument has a name:", script
print "My first variable is called:", first
print "My second variable is called:", second
print "My third variable is called:", third

forth = raw_input("4th argument?")
print "%s %s %s %s %s" % (script, first, second, third, forth)

