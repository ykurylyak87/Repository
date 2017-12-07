a = "Hello world!\n"

prompt = ('> ')
filename = raw_input(prompt)
txt = open(filename, "a")
txt.write(a),
txt.write("My name is vova")
txt.close

txt = open(filename, "r")
print("This is file contain:\n %s") % txt.read()
txt.close
