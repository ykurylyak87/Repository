animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print animals
for i in animals:
    print i
    
for i in range(len(animals)):
    # Take i number from the range and i numbers from the list
    print "Index %d in the list is %s" % (i, animals[i])

#This is the same, range by default starts with 0    
#for i in range(6):
#    print "Index %d in the list is %s" % (i, animals[i])


#This is example how can we get item from the list
#Fourth item of the list
print "This is forth item from the list animals - %s" % animals[3]
