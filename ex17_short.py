from sys import argv

script, from_file, to_file = argv

indata = open(from_file).read()
outdata = open(to_file, 'w').write(indata)


