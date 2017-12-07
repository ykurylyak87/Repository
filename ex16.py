from sys import argv

script, filename = argv

print "I am going to erase %r." % filename
print "If you don't want to erase it, hit CTRL+C (^C)."
print "If you do want that, hit ENTER."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I am going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write these to the file."

target.write("%s \n %s \n %s \n" % (line1, line2, line3))

print "Finally, I am closing file"
target.close()
