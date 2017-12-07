people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"
    
if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"
    
if people > dogs:
    print "The world is dry!"
    

dogs += 5

if people >= dogs and people <= dogs:
    print "People are greater than or equil to dogs."
    print "People are less than or equil to dogs."

    
if people == dogs:
    dogs += 5
    print "People are dogs."


print "Now number of dogs = %s" % dogs

