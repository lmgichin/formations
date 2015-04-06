__author__ = 'lucio'


def startAt(start):

    def incremente(inc):

        return start + inc

    return incremente


f = startAt(10)

print f(2), f(5)