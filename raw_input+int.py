def sum(x, y):
    z = x + y
    print "Sum of %d and %d = %d" % (x, y, z)

a = int(raw_input("Input first number: "))
b = int(raw_input("Input second number: "))
sum(a, b)

sum(10, 15)
print sum, type(sum)
