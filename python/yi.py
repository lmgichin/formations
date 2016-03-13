def mongen(max):

    print "debut"

    for i in range(max+1):
        yield i
        print "apres yield"


    print "fin fonction"

for val in mongen(2):
    print val
"""
n = mongen(2)
print n
print n.next()
print n.next()
print n.next()
print n.next()
"""