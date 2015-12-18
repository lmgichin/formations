# coding: utf-8
__author__ = 'lmaignan'

from itertools import imap, ifilter, ifilterfalse, chain, dropwhile, takewhile, groupby

# #####################################################
# enumerate
# #####################################################


def testEnumerate():

    string = 'ceci est ma chaine'

    for num,mstr in enumerate(string.split()):
        print "{0} is {1}".format(num,mstr)


    liste = [i for i in range(21) if i % 2 == 0]

    for ind, val in enumerate(liste):
        print "{0} is {1}".format(ind, val)




# ####################################################
# yield
# ####################################################

def testYield(max):

    i = 0

    while i < max:
        v = (yield i+1)

        if v is None:
            i += 1
        else:
            i = v


# ####################################################
# zip
# ####################################################

def testZip(liste1, liste2):

    for el1, el2 in zip(liste1, liste2):
        print el1, el2

# ####################################################
# unzip
# ####################################################

unzip = lambda liste: [list(li) for li in zip(*liste)]


# ####################################################
# itertools
# ####################################################

def testIter():

    pair = lambda x: x %2 == 0
    carre = lambda x: x**2

    for elem in imap(carre, range(11)):
        print elem

    print list(ifilter(pair, range(11)))
    print list(ifilterfalse(pair, range(11)))

    print list(chain(range(5), range(7,11), range(25,28)))

    print list(takewhile(lambda i: i < 10, xrange(20)))
    print list(dropwhile(lambda i: i < 10, xrange(20)))

    liste = list('aaaaaaaabbbbbbcccdde')

    for elem, iterateur in groupby(liste):
        print "l'élément {0} est répété {1} fois".format(elem, len(list(iterateur)))

# #######################################################

testEnumerate()


gen = testYield(25)

try:
    while True:
        val =  gen.next()

        if val > 17:
            gen.send(100)

        print val

except StopIteration:
    pass


testZip ([1,2,3,4],['a','b','c','d', 'e'])

print unzip([(1,'a'), (2,'b'), (3,'c')])

testIter()
