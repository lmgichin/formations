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

print f
print f(2), f(5), f(8)