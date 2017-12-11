#i = 0 
#numbers = []
def drill(i, n, s, numbers):
    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i += s
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        

    print "The numbers: "

    for num in numbers:
        print "Item: ", num

drill(0, 10, 1, [])



def drill_2(n, s):
    numbers = range(0, n, s)
    for i in numbers:
        print "\nItem: %d" % i,
    
    print "\n", numbers

drill_2(10, 1)
