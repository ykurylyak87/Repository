print "You enter a dark room with three doors. Do you go through door #1, door #2 or door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots you eyes into a pool of muck. Good job!"

elif door == "3":
    print "Choose number 1, 2 or 3 to continue"
    number = raw_input('> ')
    
    if number == "1":
        print "You choose number 1"
    
    elif number == "2":
        print "You choose number 2"
        
    elif number == "3":
        print "You choose number 3"
    else:
        "Could you read what I asked you?"
    
else:
    print "You stumble around and fall on a knife and die. Good job!"

