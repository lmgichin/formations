__author__ = 'lucio'

import random

def mongen(nb, max):

    i = 0

    while i < nb:

        yield random.randrange(max)
        i += 1


for n in mongen(15,100):
    print n