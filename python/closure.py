__author__ = 'lucio'


# ***
# sample to demonstrate closure in python
# ***

def startAt(start):

    def incremente(inc):


        return start + inc

    return incremente


# ***

f = startAt(10)
g = startAt(20)

print f
print g
print f(2), f(5), f(8)
print g(2), g(5), g(8)