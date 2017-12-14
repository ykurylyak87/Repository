from sys import exit

print """
    **********Welcome to my game.************* 
    I hope that adventure will be interesting.
    
    Type "let's begin!" to start
    or "go away" to exit
"""
def hell():
    print "In front of you stay a devil."
    print "What will you do? Talk to him and tell the truth or try to escape?"
    next = raw_input("> ")
    if "talk" in next:
        quit()
    elif "escape" in next:
        print "Devil catch you and you will work for him forever"
    else:
        print "I don't now what to do next"

def golden_room():
    print "You see a lot of gold. Have much will you take?"
    next = int(raw_input("> "))
    if next < 50:
        print "You can have it! You won!"
        quit()
    elif next > 50:
        print "You are so greed. I will move you to hell"
        hell()
    else:
        print "Please type number!"

def red_way():
    print "Now eat it"   
    next = raw_input("> ")
    if "eat" in next:
        print "You have been taken to the golden room!"
        golden_room()

def blue_way():
    print "Now eat it"
    
def start():
    print """
    You have to candies. One blue and one red.
    What color would you chose?
    """
    next = raw_input("> ")
    if next == "red":
        red_way()
    elif next == "blue":
        blue_way()
    else:
        exit(0)

def quit():
    print "You made a great mistake! Good bye!"
    exit(0)


def welcome():
    next = raw_input("> ")
    
    if "let's begin" in next or "start" in next:
        start()
    elif "go away" in next or "exit" in next or "quit" in next:
        quit()
    else:
        print "Are you sure you have read me message, try again"
        welcome()

welcome()
