from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
indata = open(from_file)
indata = in_file.read()
# One line: indata = open(from_file).read()
# in this case you don't need in_file.close() at
# the end. 

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# One line version:
# from sys import argv; fron os.path import exists; script, from_file, to_file = argv; ...
